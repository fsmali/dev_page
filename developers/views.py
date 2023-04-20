# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.db import IntegrityError

from .models import Developer
from .serializers.common import DeveloperSerializer
from .serializers.populated import PopulatedDeveloperSerializer


class DeveloperListView(APIView):
    def get(self, _request):
        developers = Developer.objects.all()
        serialized_developers = PopulatedDeveloperSerializer(
            developers, many=True)
        return Response({"detail":"all developers have been fetched","data":serialized_developers.data}, status=status.HTTP_200_OK)

    def post(self, request):
        developers_to_add = DeveloperSerializer(data=request.data)
        try:
            developers_to_add.is_valid()
            developers_to_add.save()

            return Response({"detail":"developer has been cretated","data":developers_to_add.data}, status=status.HTTP_201_CREATED)
        except (IntegrityError, AssertionError) as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "unprocessable entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class DeveloperDetailView(APIView):
    def get_developers(self, pk):
        try:
            return Developer.objects.get(pk=pk)
        except Developer.DoesNotExist:
            raise NotFound(detail="Can't find that developers!")

    def get(self, _request, pk):
        developer = self.get_developers(pk=pk)
        serialized_developer = DeveloperSerializer(developer)
        return Response({"detail":f"developer with the id-{pk} have been fetched","data":serialized_developer.data}, status=status.HTTP_200_OK)

    def put(self, reguest, pk):
        update_to_developer = self.get_developers(pk=pk)
        updated_developer = DeveloperSerializer(
            update_to_developer, data=reguest.data)

        try:
            updated_developer.is_valid()
            updated_developer.save()
            return Response({"detail":f"developer with the if-{pk} have been updated","data":updated_developer.data}, status=status.HTTP_202_ACCEPTED)
        except (AssertionError, IntegrityError) as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "unprocessable entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        developers_to_delete = self.get_developers(pk=pk)
        developers_to_delete.delete()
        return Response({"detail": f"developers with id-{pk} has been deleted"}, status=status.HTTP_204_NO_CONTENT)
