from django.contrib import admin
from django.contrib.auth import get_user_model #Django's authentication system uses the concept of a "user" to represent the people interacting with your web application. The get_user_model function returns the User model that is currently active in the project. By default, this function returns the User model defined in the django.contrib.auth.models module, but it can be customized by defining a custom user model in your project.

User = get_user_model() #The line of code User = get_user_model() retrieves the user model defined in the Django project and assigns it to a variable named User.
admin.site.register(User)

