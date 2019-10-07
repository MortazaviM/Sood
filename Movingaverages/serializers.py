#from rest_framework import serializers 
from Signal.models import data
from rest_framework_mongoengine import serializers


class DataSerializer(serializers.DocumentSerializer):
    class Meta:
        model=data
        fields='__all__'