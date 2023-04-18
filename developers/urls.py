from django.urls import path
from .views import DeveloperListView ,DeveloperDetailView

urlpatterns =[
    path('', DeveloperListView.as_view()),
    path('<int:pk>/', DeveloperDetailView.as_view())
]