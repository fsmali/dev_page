# Generated by Django 4.2 on 2023-04-27 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0005_alter_developer_project_url_alter_developer_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='project_url',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='skills',
        ),
    ]
