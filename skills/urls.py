from django.urls import path
from .views import SkillListView, skillDetailView

urlpatterns = [
    path('', SkillListView.as_view()),
    path('<str:pk>/', skillDetailView.as_view())
]
