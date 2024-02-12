import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member, MemberFile


class MemberCheckId(APIView):
    def get(self, request, member_id, *args, **kwargs):
        print(member_id);
        return Response({'status': Member.objects.filter(member_id=member_id).exists()})

class MemberJoinView(View):

    def get(self, request, *args, **kwargs):
        # request와 실제 경로를 작성하여 이동한다.
        return render(request, 'member/join.html')

    def post(self, request, *args, **kwargs):
        # member_email은 중복가능, member_type과 함께 검사
        token, check_all, check, member_name, member_birth, member_phone, member_id, member_password, member_email, member_type = request.POST.values()
        # update()사용 시, updated_date의 auto_now=True는 동작하지 않는다.
        # save()사용 시, auto_now=True가 동작한다.
        member = Member.objects.filter(member_email=member_email, member_type=member_type)

        if member.exists():
            # 이미 회원 정보가 있다면(OAuth로 로그인), 수정
            member.update(
                member_id=member_id,
                member_password=member_password,
                member_name=member_name,
                member_birth=member_birth,
                member_phone=member_phone,
                updated_date=datetime.datetime.now()
            )
        else:
            # 회원 정보가 없다면, 추가
            Member.objects.create(
                member_id=member_id,
                member_password=member_password,
                member_email=member_email,
                member_name=member_name,
                member_birth=member_birth,
                member_phone=member_phone
            )

        # 이동할 urls 경로를 작성한다.
        return redirect('member:login')


class MemberLoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'member/login.html')

    def post(self, request, *args, **kwargs):
        token, member_id, member_password = request.POST.values()
        print(member_id, member_password)
        members = Member.objects.filter(member_id=member_id, member_password=member_password)
        member = members.first()
        if members.exists():
            request.session['id'] = member.id
            return redirect('post:list page=1')
        return render(request, 'member/login.html', {'check': False})

class MyPageView(View):
    def get(self, request, *args, **kwargs):
        member = Member.objects.get(id=request.session["id"])
        return render(request, 'member/mypage.html', {'member': member})

    def post(self, request, *args, **kwargs):
        datas = request.POST
        member_name = datas['member-name']
        member_password = datas['member-password']
        id = request.session["id"]
        member = Member.objects.get(id=id)
        if member.member_password == member_password:
            member.member_name = member_name
            member.updated_date = datetime.datetime.now()
            member.save(update_fields=['member_name', 'updated_date'])

            files = request.FILES
            member_files = MemberFile.objects.filter(member_id=id)
            if not member_files.exists():
                member_file = MemberFile(member=member, updated_date=datetime.datetime.now())
            else:
                member_file = member_files.first()
            # key는 input[type=file]태그의 name
            for key in files:
                member_file.image = files[key]
                member_file.updated_date = datetime.datetime.now()
                member_file.save()
            return redirect('member:mypage')

        return render(request, 'member/mypage.html', {'check': False})


