# Generated by Django 5.0.1 on 2024-02-07 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_updated_date_alter_postfile_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 7, 14, 39, 40, 505937)),
        ),
        migrations.AlterField(
            model_name='postfile',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 7, 14, 39, 40, 505937)),
        ),
    ]