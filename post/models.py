import math
import datetime

from django.db import models

from member.models import Member
from project.models import Period


class Post(Period):
    post_title = models.CharField(max_length=200, null=False, blank=True)
    post_content = models.CharField(max_length=500, null=False, blank=True)
    post_read_count = models.BigIntegerField(default=0)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        db_table = 'tbl_post'

    def get_absolute_url(self):
        return f"/post/detail/{self.id}"

    def change_date_format(self):
        now = datetime.datetime.now()
        create_date = self.created_date
        gap = math.floor((now - create_date).seconds / 60)

        if gap < 1:
            return "방금 전"

        if gap < 60:
            return f"{gap}분 전"

        gap = math.floor(gap / 60)

        if gap < 24:
            return f"{gap}시간 전"

        gap = math.floor(gap / 24)

        if gap < 31:
            return f"{gap}일 전"

        gap = math.floor(gap / 31)

        if gap < 12:
            return "${gap}개월 전"

        gap = math.floor(gap / 12)
        return f"{gap}년 전"


class PostFile(Period):
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False, upload_to='post/%Y/%m/%d')
    preview = models.BooleanField(default=False)

    class Meta:
        db_table = 'tbl_post_file'

    def __str__(self):
        return self.image.url.replace("/", "-")[1:]
