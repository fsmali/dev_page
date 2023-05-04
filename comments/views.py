from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.request import  Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from developers.models import Developer 

from django.db import IntegrityError

from .models import Comment
from .serializers.common import CommentSerializer 
from .serializers.populated import PopulatedCommentSerializer

class CommentListView(APIView):
    permission_classes =(IsAuthenticated, )
    def get(self, _request):
        comments = Comment.objects.all()
        serialized_commnets = PopulatedCommentSerializer(comments, many=True)
        return Response(serialized_commnets.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        # developer_title=request.data.get("title", None)
        # developer = Developer.objects.get(title=developer_title)
        # request.data['developer']=developer.id
        request.data["owner"] =request.user.id
        comment_to_create =CommentSerializer(data=request.data)
        try:
            comment_to_create.is_valid()
            comment_to_create.save()
            return Response(comment_to_create.data, status=status.HTTP_201_CREATED)
        except(AssertionError, IntegrityError) as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail":"unprocessable entity",}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
class CommentDetailView(APIView):
    permission_classes =(IsAuthenticated, )
    def get_comment(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise NotFound(detail=f"the comment with the pk{pk} has not found")
    def get(self, _request, pk):
        comment = self.get_comment(pk=pk)
        serialized_comment = PopulatedCommentSerializer(comment)
        return Response(serialized_comment.data,status=status.HTTP_200_OK)
    def put(self,request, pk):
        request.data["owner"] =request.user.id
        try:
            commnet_to_update = self.get_comment(pk=pk)
            if commnet_to_update.owner != request.user:#The problem with the code if updated_comment.owner != request.user: raise PermissionDenied() is that updated_comment is an instance of CommentSerializer, not an instance of a comment object. Therefore, it does not have an owner attribute. Instead, you should check the owner of the comment object that the serializer is serializing.
              raise PermissionDenied()
            updated_comment = CommentSerializer(commnet_to_update, data=request.data)
            
        
            updated_comment.is_valid()
            updated_comment.save()
            return Response(updated_comment.data,status=status.HTTP_202_ACCEPTED)  
        except(AssertionError, IntegrityError) as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail":"unprocessable entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        

    def delete(self, request, pk):
        try:
            comment_to_delete = self.get_comment(pk=pk)
            if comment_to_delete.owner != request.user:
              raise PermissionDenied()
            comment_to_delete.delete()
            return Response({"detail":f"the comment with the id-{pk} has been deleted"},status=status.HTTP_204_NO_CONTENT)   
        except Comment.DoesNotExist:
            raise NotFound(detail="comment not found")

