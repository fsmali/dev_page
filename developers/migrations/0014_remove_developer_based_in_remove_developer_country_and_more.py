# Generated by Django 4.2 on 2023-04-28 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0013_developer_project_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='based_in',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='country',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='git_hub',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='info',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='linkden',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='project_url',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='title',
        ),
    ]
