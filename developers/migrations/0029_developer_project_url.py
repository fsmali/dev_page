# Generated by Django 4.2 on 2023-04-30 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_description'),
        ('developers', '0028_developer_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='project_url',
            field=models.ManyToManyField(related_name='developers', to='projects.project'),
        ),
    ]
