# Generated by Django 4.2 on 2023-04-30 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
        ('developers', '0025_remove_developer_skill_developer_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='skill',
            field=models.ManyToManyField(related_name='developers', to='skills.skill'),
        ),
    ]
