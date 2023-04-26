from .common import ProjectSerializer
# from skills.serializers.common import SkillSerializer
# from comments.serializers.populated import PopulatedCommentSerializer
from developers.serializers.common import DeveloperSerializer
# from jwt_auth.serializers.common import UserSerializer

class PopulatedProjectSerializer(ProjectSerializer):
    # skills = SkillSerializer(many=True)
    # comments = PopulatedCommentSerializer(many=True)
    developers = DeveloperSerializer(many=True)
    # owner = UserSerializer()