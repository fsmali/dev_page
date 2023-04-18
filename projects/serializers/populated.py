from .common import ProjectSerializer
from developers.serializers.common import DeveloperSerializer

class PopulatedProjectSerializer(ProjectSerializer):
    developers = DeveloperSerializer(many=True)