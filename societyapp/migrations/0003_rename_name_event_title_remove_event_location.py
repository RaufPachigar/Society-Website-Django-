# Generated by Django 5.1 on 2024-11-17 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('societyapp', '0002_rename_description_notice_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
    ]