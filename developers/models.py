from django.db import models


class Developer(models.Model):
    title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    based_in = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    img = models.CharField(max_length=300)
    facebook = models.CharField(max_length=300)
    instagram = models.CharField(max_length=300)
    git_hub = models.CharField(max_length=300)
    linkden = models.CharField(max_length=300)
    info = models.TextField(max_length=1000)
    skills = models.ManyToManyField('skills.Skill', related_name="developers")
    project = models.ManyToManyField('projects.Project', related_name="developers")
    owner = models.ForeignKey('jwt_auth.User', related_name='developers', on_delete=models.CASCADE)
    
    

    def __str__(self):
        return f"{self.title}-{self.first_name}"
