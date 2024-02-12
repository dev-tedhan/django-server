from django.db.models import F
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member
from post.models import Post
from reply.models import Reply


class ReplyWriteAPI(APIView):
    def post(self, request, post_id):
        datas = request.data
        datas = {
            'post': Post.objects.get(id=post_id),
            'member': Member.objects.get(id=request.session['id']),
            'reply_content': datas['replyContent']
        }
        Reply.objects.create(**datas)
        return Response('success')


class ReplyListAPI(APIView):
    def get(self, request, post_id, page):
        size = 5
        offset = (page - 1) * size
        limit = page * size
        replies = Reply.objects.filter(post_id=post_id).annotate(member_name=F('member__member_name'), image=F('member__memberfile__image')).values('id', 'reply_content', 'member_name', 'image', 'created_date', 'member__id');
        return Response(replies[offset:limit])
