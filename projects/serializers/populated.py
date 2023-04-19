from .common import ProjectSerializer
from skills.serializers.common import SkillSerializer
from comments.serializers.common import CommentSerializer

class PopulatedProjectSerializer(ProjectSerializer):
    skills = SkillSerializer(many=True)
    comments = CommentSerializer(many=True)

