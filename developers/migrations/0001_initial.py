# Generated by Django 4.2 on 2023-04-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('based_in', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('img', models.CharField(max_length=300)),
                ('facebook', models.CharField(max_length=300)),
                ('instagram', models.CharField(max_length=300)),
                ('git_hub', models.CharField(max_length=300)),
                ('linkden', models.CharField(max_length=300)),
                ('info', models.TextField(max_length=1000)),
                ('project', models.ManyToManyField(related_name='developers', to='projects.project')),
                ('skills', models.ManyToManyField(related_name='developers', to='skills.skill')),
            ],
        ),
    ]
