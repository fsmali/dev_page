# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.db import IntegrityError

from .models import Project
from .serializers.populated import PopulatedProjectSerializer
from .serializers.common import ProjectSerializer


class ProjectListView(APIView):
    
    permission_classes = (IsAuthenticatedOrReadOnly, )#This line of code defines a tuple named permission_classes that contains a single permission class IsAuthenticatedOrReadOnly.In Django REST Framework (DRF), permissions are used to control access to views and APIs. The IsAuthenticatedOrReadOnly class is a built-in permission class provided by DRF that allows authenticated users to perform any HTTP method (GET, POST, PUT, DELETE, etc.) on the view or API, while unauthenticated users are only allowed to perform safe methods (GET, HEAD, OPTIONS).

    def get(self, _request):
        projects = Project.objects.all()
        serialized_project =ProjectSerializer(projects, many=True)#Setting many=True on a serializer indicates that you want to serialize a collection of objects, typically a queryset or a list of objects.
        return Response({"detail":f" All projecs data have been fetched", "data":serialized_project.data}, status=status.HTTP_200_OK)
    
    def post(self,request):
        request.data["owner"] = request.user.id
        porject_to_create = ProjectSerializer(data=request.data)
        try:
            porject_to_create.is_valid()
            porject_to_create.save()
            return Response({"detail":f" New project has been created", "data":porject_to_create.data}, status=status.HTTP_201_CREATED)
        except (AssertionError,IntegrityError) as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail":"unprocessable error"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class projectDetailView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise NotFound(detail= f"Cant find that project with that pk-{pk}")
        
    def get(self, _request, pk):
        project = self.get_project(pk=pk)
        serialized_project = PopulatedProjectSerializer(project)
        return Response({"detail":f"the project with the id-{pk} has been fetched", "data":serialized_project.data}, status=status.HTTP_202_ACCEPTED)
    
    def put(self, request,  pk):
        project_to_updata = self.get_project(pk=pk)
        updated_project = ProjectSerializer(project_to_updata, data=request.data)  
        try:
            updated_project.is_valid()
            updated_project.save()
            return Response({"detail":f"the project with the id-{pk} has been updated", "data":updated_project.data}, status=status.HTTP_201_CREATED)
        except(AssertionError, IntegrityError) as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail":"unprocessable entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    def delete(self, _request, pk):
        project_to_delete = self.get_project(pk=pk)
        project_to_delete.delete()
        return Response({"detail":f"the project with the id-{pk} has been deleted"}, status=status.HTTP_204_NO_CONTENT)
