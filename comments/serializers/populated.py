from .common import CommentSerializer
from projects.serializers.common import ProjectSerializer

class PopulatedCommentSerializer(CommentSerializer):
    project =ProjectSerializer(many=True)