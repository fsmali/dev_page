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
    
    def post(self, request):
        comment_to_create =CommentSerializer(data=request.data)
        try:
            comment_to_create.is_valid()
            comment_to_create.save()
            return Response({"detail":f"the comment has been created", "data":comment_to_create.data}, status=status.HTTP_201_CREATED)
        except(AssertionError, IntegrityError) as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail":"unprocessable entity",}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
class CommentDetailView(APIView):
    def get_comment(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise NotFound(detail=f"the comment with the pk{pk} has not found")
    def get(self, _request, pk):
        comment = self.get_comment(pk=pk)
        serialized_comment = PopulatedCommentSerializer(comment)
        return Response({"detail":f"the comment with the id-{pk} has been found","data":serialized_comment.data},status=status.HTTP_200_OK)
    def put(self,request, pk):
        commnet_to_update = self.get_comment(pk=pk)
        updated_comment = CommentSerializer(commnet_to_update, data=request.data)
        try:
            updated_comment.is_valid()
            updated_comment.save()
            return Response({"detail":f"the comment with the id-{pk} has been updated","data":updated_comment.data},status=status.HTTP_202_ACCEPTED)  
        except(AssertionError, IntegrityError) as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail":"unprocessable entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self,_request, pk):
        comment_to_delete = self.get_comment(pk=pk)
        comment_to_delete.delete()
        return Response({"detail":f"the comment with the id-{pk} has been deleted"},status=status.HTTP_204_NO_CONTENT)    

