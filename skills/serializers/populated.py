from.common import SkillSerializer
from developers.serializers.common import DeveloperSerializer

class PopulatedSkillSerializer(SkillSerializer):
    developers = DeveloperSerializer(many=True)
    