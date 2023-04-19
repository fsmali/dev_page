from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.request import  Request
from rest_framework import status

from django.db import IntegrityError

from .models import Comment
from .serializers.common import CommentSerializer 
from .serializers.populated import PopulatedCommentSerializer

class CommentListView(APIView):
    def get(self, _request):
        comments = Comment.objects.all()
        serialized_commnets = PopulatedCommentSerializer(comments, many=True)
        return Response({"detail":f"all commments have been fetched", "data":serialized_commnets.data}, status=status.HTTP_200_OK)

