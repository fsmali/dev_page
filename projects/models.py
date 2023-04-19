from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300, null=True, blank=True)
    source_link = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField('skills.Skill', related_name="projects")
    # This line of code is defining a field named description in a Django model. The field is of type TextField, which allows for longer text strings to be stored compared to CharField.The null=True argument means that the field can be left empty, i.e., it can be NULL in the database.

    def __str__(self):
        return f"{self.title}"




