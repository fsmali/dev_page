from .common import DeveloperSerializer
from projects.serializers.common import ProjectSerializer
from skills.serializers.common import SkillSerializer
from comments.serializers.populated import PopulatedCommentSerializer
from jwt_auth.serializers.common import UserSerializer



class PopulatedDeveloperSerializer(DeveloperSerializer):
    project = ProjectSerializer(many=True)
    skills = SkillSerializer(many=True)
    comments = PopulatedCommentSerializer(many=True)
    owner = UserSerializer()