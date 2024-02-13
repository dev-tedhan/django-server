from django.urls import path

from member.views import MemberJoinView, MemberLoginView, MemberCheckId, MyPageView

app_name = 'member'

urlpatterns = [
    path('check-id/<str:member_id>', MemberCheckId.as_view()),
    path('join/', MemberJoinView.as_view(), name='join'),
    path('login/', MemberLoginView.as_view(), name='login'),
    path('mypage/', MyPageView.as_view(), name='mypage'),
]