from rest_framework import serializers
from django.contrib.auth import get_user_model
from items.serializers import NestedUserSerializer
from .models import Profile
User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):

    user = NestedUserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'
        