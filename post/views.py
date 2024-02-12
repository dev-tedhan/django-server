import math
import datetime
import os

from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView

from member.models import Member
from post.models import Post, PostFile


class PostWriteView(View):
    def get(self, request, *args, **kwargs):
        member_name = Member.objects.get(id=request.session['id']).member_name
        return render(request, "post/write.html", {"member_name": member_name})

    def post(self, request, *args, **kwargs):
        datas = request.POST
        files = request.FILES

        datas = {
            'member_id': request.session['id'],
            'post_title': datas['post-title'],
            'post_content': datas['post-content']
        }

        post = Post.objects.create(**datas)
        for key in files:
            PostFile.objects.create(post=post, image=files[key], preview=key == "upload1")

        return redirect(post.get_absolute_url())




class PostListView(View):
    def get(self, request, page=1, *args, **kwargs):
        size = 5
        offset = (page - 1) * size
        limit = page * size
        total = Post.objects.all().count()
        page_count = 5
        end_page = math.ceil(page / page_count) * page_count
        start_page = end_page - page_count + 1
        real_end = math.ceil(total / size)
        end_page = real_end if end_page > real_end else end_page

        if end_page == 0:
            end_page = 1

        datas = {
            'posts': list(Post.objects.all())[offset:limit],
            'start_page': start_page,
            'end_page': end_page,
            'page': page,
            'real_end': real_end,
            'page_count': page_count,
            'member_name': Member.objects.get(id=request.session['id']).member_name,
        }

        return render(request, 'post/list.html', datas)

class PostDetailView(View):
    def get(self, request, post_id, *args, **kwargs):
        post = Post.objects.get(id=post_id)
        post.post_read_count = post.post_read_count + 1
        post.updated_date = datetime.datetime.now()
        post.save(update_fields=['post_read_count', 'updated_date'])
        return render(request, 'post/detail.html', {'post': post})


class PostUpdateView(View):
    def get(self, request, post_id, *args, **kwargs):
        post = Post.objects.get(id=post_id)
        return render(request, 'post/update.html', {'post': post})

    def post(self, request, post_id, *args, **kwargs):
        datas = request.POST
        files = request.FILES

        datas = {
            'post_title': datas['post-title'],
            'post_content': datas['post-content'],
            'updated_date': datetime.datetime.now()
        }

        posts = Post.objects.filter(id=post_id)
        post = posts.first()

        posts.update(**datas)
        PostFile.objects.filter(post_id=post_id).delete()

        for key in files:
            PostFile.objects.create(post=post, image=files[key], preview=key == "upload1")
        return redirect('post:detail', post_id=post_id)


class PostDeleteView(View):
    def get(self, request, post_id, *args, **kwargs):
        Post.objects.get(id=post_id).delete()
        return redirect('post:list', page=1)

class PostFileDownloadView(View):
    def get(self, request, file_path, *args, **kwargs):
        file_path = file_path.replace('-', '/')
        file_name = file_path.split('/')[-1]
        print(file_path, file_name)
        # file_path: 파일이 있는 경로 설정, 경로에 파일 이름 포함 가능
        fs = FileSystemStorage(file_path)
        # fs.open("파일 이름", 'rb')
        response = FileResponse(fs.open("", 'rb'),
                                content_type='application/image')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'

        return response


