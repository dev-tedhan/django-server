# Generated by Django 5.0.1 on 2024-02-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_id',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
