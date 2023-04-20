from .common import ProjectSerializer
from skills.serializers.common import SkillSerializer
from comments.serializers.common import CommentSerializer
from developers.serializers.common import DeveloperSerializer

class PopulatedProjectSerializer(ProjectSerializer):
    skills = SkillSerializer(many=True)
    comments = CommentSerializer(many=True)
    developer = DeveloperSerializer()

