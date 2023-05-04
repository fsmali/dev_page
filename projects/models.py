from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    source_link = models.CharField(max_length=300)
    # created_at = models.DateTimeField(auto_now_add=True)
    # skills = models.ManyToManyField('skills.Skill', related_name="projects")
    # This line of code is defining a field named description in a Django model. The field is of type TextField, which allows for longer text strings to be stored compared to CharField.The null=True argument means that the field can be left empty, i.e., it can be NULL in the database.
    # developer = models.ForeignKey('developers.Developer', related_name="projects", on_delete=models.CASCADE)
    #The first model, "Developer. The second model, which this code snippet is a part of, has a field called "developer" that is a foreign key to the "Developer" model. The foreign key relationship is defined using the ForeignKey method from Django's models module
    #The related_name parameter specifies the name of a reverse relation from the "Developer" model back to this model. In this case, it is set to "projects," so each "Developer" object will have a related manager called "projects" that can be used to access all the "Project" objects that have a foreign key pointing to that "Developer" object.
    #The on_delete parameter specifies what should happen when the related "Developer" object is deleted. In this case, it is set to CASCADE, which means that when a "Developer" object is deleted, all the "Project" objects that have a foreign key pointing to that "Developer" object will also be deleted.
    # owner = models.ForeignKey('jwt_auth.User', related_name='projects', on_delete=models.CASCADE)
    #In this case, the foreign key is defined on a model that has a relationship with the jwt_auth.User model. The jwt_auth.User model is specified as a string to avoid circular import errors.
    #The related_name argument is used to specify the name of the reverse relation from the related model back to the model with the foreign key. In this case, it is named 'projects', so you can access the related projects from a jwt_auth.User instance by calling user.projects.all().

    def __str__(self):
        return f"{self.project_name}"
