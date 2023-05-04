# Generated by Django 4.2 on 2023-04-30 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('developers', '0024_remove_developer_owner_remove_developer_project_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='skill',
        ),
        migrations.AddField(
            model_name='developer',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='developers', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
