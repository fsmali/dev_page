# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.exceptions import NotFound
from rest_framework import status

from django.db import IntegrityError
from .models import Project
from .serializers.populated import PopulatedProjectSerializer
from .serializers.common import ProjectSerializer


class ProjectListView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serialized_project =ProjectSerializer(projects)
        return Response(serialized_project.data, status=status.HTTP_200_OK)
