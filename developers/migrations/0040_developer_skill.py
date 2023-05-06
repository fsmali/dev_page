# Generated by Django 4.2 on 2023-05-01 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
        ('developers', '0039_remove_developer_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='skill',
            field=models.ManyToManyField(related_name='developers', to='skills.skill'),
        ),
    ]