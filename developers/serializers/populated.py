from .common import DeveloperSerializer
from projects.serializers.common import ProjectSerializer



class PopulatedDeveloperSerializer(DeveloperSerializer):
    projects = ProjectSerializer(many=True)

