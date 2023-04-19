from .views import ProjectListView, projectDetailView
from django.urls import path

urlpatterns=[
    path('', ProjectListView.as_view()),
    path('<int:pk>/', projectDetailView.as_view())
]