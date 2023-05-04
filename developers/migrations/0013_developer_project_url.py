# Generated by Django 4.2 on 2023-04-27 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('developers', '0012_remove_developer_project_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='project_url',
            field=models.ManyToManyField(related_name='developers', to='projects.project'),
        ),
    ]
