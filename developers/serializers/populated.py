from .common import DeveloperSerializer
from skills.serializers.common import SkillSerializer
from projects.serializers.common import ProjectSerializer


class PopulatedDeveloperSerializer(DeveloperSerializer):
    skills = SkillSerializer(many=True)
    projects = ProjectSerializer(many=True)

    # from .common import BookSerializer
# from genres.serializers.common import GenreSerializer
# from comments.serializers.populated import populatedCommentSerializer
# from artists.serializers.common import ArtistSerializers
# from jwt_auth.serializers.common import UserSerializers


# class populatedBookSerializer(BookSerializer):
#     genres = GenreSerializer(many=True)
#     comments = populatedCommentSerializer(many=True)
#     artist =  ArtistSerializers()
#     owner = UserSerializers()
