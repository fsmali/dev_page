from rest_framework import serializers
from django.contrib.auth import password_validation,get_user_model
from django.contrib.auth.hashers import make_password #The make_password function is a built-in function in Django's contrib.auth.hashers module that allows you to securely hash a password using one of the available password hashers in Django.
from django.core.exceptions import ValidationError

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)#write_only=True is a serializer option that specifies that the field should be used only during serialization (when converting a Python object to JSON or another serialization format), and not during deserialization (when converting JSON or another serialization format back to a Python object). This means that the field will not be included in the serialized representation of the object.

    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({'password_confirmation':'does not match password field'})#In this case, the validate method is used to validate that the password and password_confirmation fields match. The method retrieves these fields from the data dictionary using the pop method, which removes them from the dictionary. This is because the password and password_confirmation fields are not actual fields on the serializer, but are instead write-only fields used to create or update a user object.
        try:
            password_validation.validate_password(password=password)
        except ValidationError as err:
            raise ValidationError({'password'}, err)
        data['password'] = make_password(password)
        return data
    
    class Meta:
        model = User
        fields = ( "first_name", "last_name","username", "email", 'password','password_confirmation')