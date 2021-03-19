from rest_framework import serializers

from .models import Sonnet


class SonnetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sonnet
        fields = ['number', 'text']
