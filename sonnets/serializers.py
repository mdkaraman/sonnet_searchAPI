from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Sonnet


class SonnetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sonnet
        fields = ['number', 'text']

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'id', 'username']