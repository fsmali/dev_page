# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from django.db import IntegrityError

from .models import Skill
from .serializers.common import SkillSerializer
from .serializers.populated import PopulatedSkillSerializer


class SkillListView(APIView):

    def get(self, _request):
        skill = Skill.objects.all()
        serializied_skills = PopulatedSkillSerializer(skill, many=True)
        return Response(serializied_skills.data, status=status.HTTP_200_OK)

    def post(self, request):
        skill_to_create = SkillSerializer(data=request.data)
        try:
            skill_to_create.is_valid()
            skill_to_create.save()
            return Response(skill_to_create.data, status=status.HTTP_201_CREATED)
        except(IntegrityError, AssertionError) as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail":"unprocessable entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class SkillDetailView(APIView):
    def get_skills(self, pk):
        try:
            return Skill.objects.get(pk=pk)
        except Skill.DoesNotExist:
            raise NotFound(detail= f"the skill with the id-{pk} not found")
    def get(self, _request, pk):
        skill = self.get_skills(pk=pk)
        serializied_skill = PopulatedSkillSerializer(skill)
        return Response(serializied_skill.data, status=status.HTTP_200_OK)
    def put(self, request, pk):
        update_to_skill = self.get_skills(pk=pk)
        updated_skill = SkillSerializer(update_to_skill, data=request.data)
        try:
            updated_skill.is_valid()
            updated_skill.save()
            return Response(updated_skill.data, status=status.HTTP_202_ACCEPTED)
        except(AssertionError, IntegrityError) as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail":"Unprocessable entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    def delete(self, request, pk):
        skill_to_delete = self.get_skills(pk=pk)
        skill_to_delete.delete()
        return Response({"detail":f"the skill with id-{pk} has benn deleted"}, status=status.HTTP_204_NO_CONTENT)







