# Generated by Django 5.0.1 on 2024-02-13 10:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reply', '0018_alter_reply_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]