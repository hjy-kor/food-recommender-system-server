# Generated by Django 4.0.4 on 2022-05-16 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a4app', '0002_rename_uesr_id_user_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
    ]
