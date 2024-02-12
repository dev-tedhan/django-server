# Generated by Django 5.0.1 on 2024-02-08 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_alter_post_updated_date_alter_postfile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 13, 8, 23, 214594)),
        ),
        migrations.AlterField(
            model_name='postfile',
            name='image',
            field=models.ImageField(upload_to='post/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='postfile',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 13, 8, 23, 214594)),
        ),
    ]
