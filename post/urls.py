from django.urls import path
from django.views.generic import TemplateView

from post.views import PostWriteView, PostListView, PostDetailView, PostFileDownloadView, PostUpdateView, PostDeleteView

app_name = 'post'

urlpatterns = [
    path('list/<int:page>/', PostListView.as_view(), name='list'),
    path('mypage/', TemplateView.as_view(template_name='post/mypage.html'), name='mypage'),
    path('write/', PostWriteView.as_view(), name='write'),
    path('update/<int:post_id>/', PostUpdateView.as_view(), name='update'),
    path('delete/<int:post_id>/', PostDeleteView.as_view(), name='delete'),
    path('detail/<int:post_id>/', PostDetailView.as_view(), name='detail'),
    path('download/<str:file_path>/', PostFileDownloadView.as_view(), name='download'),
]