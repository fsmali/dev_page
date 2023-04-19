from django.urls import path
from .views import SkillListView, SkillDetailView

urlpatterns = [
    path('', SkillListView.as_view()),
    path('<str:pk>/', SkillDetailView.as_view())
]
