from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    source_link = models.CharField(max_length=300)
    

    def __str__(self):
        return f"{self.project_name}"
