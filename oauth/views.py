from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from allauth.socialaccount.models import SocialAccount

from member.models import Member


class OAuthLoginView(View):
    def get(self, request, *args, **kwargs):
        user = SocialAccount.objects.get(user=request.user)
        member_email = ""
        if user.provider == "google":
            member_email = user.extra_data.get("email")
        elif user.provider == "kakao":
            member_email = user.extra_data.get("kakao_account").get("email")
        elif user.provider == "naver":
            member_email = user.extra_data.get("email")

        # get_or_create()는 object, created 형태의 튜플을 리턴한다.
        # object는 가져온 객체이고 created는 create했다면 true, get했다면 false이다.
        member, created = Member.objects.get_or_create(member_email=member_email, member_type=user.provider)
        if created or member.member_id is None:
            return render(request, 'member/join.html', {"member_email": member_email, "member_type": user.provider})

        request.session['id'] = member.id
        return redirect('/post/list/1')


def login_cancelled(request):
    return redirect('member:login')
