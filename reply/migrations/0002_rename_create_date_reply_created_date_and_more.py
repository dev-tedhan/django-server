# Generated by Django 5.0.1 on 2024-02-06 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reply', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='update_date',
            new_name='updated_date',
        ),
    ]