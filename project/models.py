import datetime

from django.db import models


class Period(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        abstract = True
