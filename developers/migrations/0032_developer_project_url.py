# Generated by Django 4.2 on 2023-05-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_description'),
        ('developers', '0031_developer_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='project_url',
            field=models.ManyToManyField(related_name='developers', to='projects.project'),
        ),
    ]
