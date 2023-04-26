# Generated by Django 4.2 on 2023-04-25 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('developers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='developers', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]