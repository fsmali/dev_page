# Generated by Django 4.2 on 2023-04-30 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0023_developer_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='project_url',
        ),
    ]
