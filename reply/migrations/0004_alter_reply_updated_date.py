# Generated by Django 5.0.1 on 2024-02-06 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reply', '0003_alter_reply_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 6, 15, 33, 11, 839405)),
        ),
    ]
