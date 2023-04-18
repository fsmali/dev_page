from django.db import models


class Developer(models.Model):
    title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    img = models.CharField(max_length=300)
    skills = models.ManyToManyField('skills.Skill', related_name="developers")
    projects = models.ManyToManyField(
        'projects.Project', related_name="developers")

    def __str__(self):
        return f"{self.title}-{self.first_name}"
