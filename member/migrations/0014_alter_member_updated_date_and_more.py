# Generated by Django 5.0.1 on 2024-02-08 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0013_alter_member_updated_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 13, 8, 23, 214594)),
        ),
        migrations.AlterField(
            model_name='memberfile',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 13, 8, 23, 214594)),
        ),
    ]
