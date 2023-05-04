from django.db import models


class Developer(models.Model):
    title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    based_in = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    img = models.CharField(max_length=300,null=True, blank=True)
    facebook = models.CharField(max_length=300,null=True, blank=True)
    instagram = models.CharField(max_length=300,null=True, blank=True)
    git_hub = models.CharField(max_length=300,null=True, blank=True)
    linkden = models.CharField(max_length=300,null=True, blank=True)
    info = models.TextField(max_length=5000)
    skill = models.ManyToManyField('skills.Skill', related_name='developers')
    project = models.ManyToManyField('projects.Project', related_name="developers")
    # owner = models.ForeignKey('jwt_auth.User', related_name='developers', on_delete=models.CASCADE)
    
    

    def __str__(self):
        return f"{self.title}-{self.first_name}"
