# Generated by Django 4.2 on 2023-04-27 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0010_developer_project_url_developer_skills'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developer',
            old_name='skills',
            new_name='skill',
        ),
    ]
