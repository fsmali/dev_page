# Generated by Django 4.2 on 2023-05-01 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0037_alter_developer_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='project',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='skill',
        ),
    ]
