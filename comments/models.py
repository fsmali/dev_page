from django.db import models

class Comment(models.Model):
    text = models.TextField(max_length=300)
    created_at =models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('projects.Project', related_name= 'comments', on_delete=models.CASCADE)
    #This line of code defines a foreign key relationship between the Comment model and the Project model.In particular, it specifies that each Comment instance is associated with a single Project instance through a foreign key field called project. The ForeignKey argument 'projects.Project' indicates that the related model is the Project model in the projects app, while the related_name argument 'comments' specifies the name of the reverse relation from the Project model back to the Comment model.The on_delete argument specifies the behavior to adopt when the referenced Project instance is deleted. In this case, models.CASCADE is specified, which means that when a Project instance is deleted, all associated Comment instances will be deleted as well.

    def __str__(self):
        return self.text
