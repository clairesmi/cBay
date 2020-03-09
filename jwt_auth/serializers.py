# pylint: disable=no-member,arguments-differ
from rest_framework import serializers
from django.contrib.auth import get_user_model
# encryption package for passwords is built in
# import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from items.serializers import ListingSerializer
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True) #so password cannot be read
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'does not match'})

            #ONLY COMMENT OUT FOR DEVELOPMENT TO ALLOW SIMPLE PASSWORDS
        # try:
        #     validations.validate_password(password=password)
        # except ValidationError as err:
        #     raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password)
        return data

    # listed_item = ListingSerializer(many=True)

    class Meta:

        model = User
        fields = ('username', 'email', 'password', 'password_confirmation',
        'profile_image', 'recommendations')
        extra_kwargs = {'recommendations': {'required': False}}
        