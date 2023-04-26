from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings

import jwt
User = get_user_model()

class JWTAuthentication(BasicAuthentication):

    def authenticate(self, request):
        # get the authorization header from the request
        auth_header = request.headers.get('Authorization')

        # check that the auth_header has a value
        if not auth_header:
            return None

        # check that the token is a Bearer token
        if not auth_header.startswith('Bearer'):
            raise PermissionDenied(detail="invalid auth token format")

        # remove bearer from the start of the token
        token = auth_header.replace('Bearer ', '')

        # get the payload, take the sub (the user id) and make sure the user exists
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])

            # find the user using the user id from the payload (id = sub)
            user = User.objects.get(pk=payload.get('sub'))

        # if the token is not valid for any reason
        except jwt.exceptions.InvalidTokenError:
            raise PermissionDenied(detail="Invalid token")


        except User.DoesNotExist:
            raise PermissionDenied(detail="User not found")

        return (user, token)