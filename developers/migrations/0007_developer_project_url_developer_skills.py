# Generated by Django 4.2 on 2023-04-27 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('skills', '0001_initial'),
        ('developers', '0006_remove_developer_project_url_remove_developer_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='project_url',
            field=models.ManyToManyField(blank=True, null=True, related_name='developers', to='projects.project'),
        ),
        migrations.AddField(
            model_name='developer',
            name='skills',
            field=models.ManyToManyField(blank=True, null=True, related_name='developers', to='skills.skill'),
        ),
    ]
