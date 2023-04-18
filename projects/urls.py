from .views import ProjectListView
from django.urls import path

urlpatterns=[
    path('', ProjectListView.as_view())
]