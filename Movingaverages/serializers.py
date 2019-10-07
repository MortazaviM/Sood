#from rest_framework import serializers 
from Movingaverages.models import data
from rest_framework_mongoengine import serializers
from rest_framework import serializers as rest_serializers

class DataSerializer(serializers.DocumentSerializer):
    class Meta:
        model=data
        fields='__all__'

class MovingAverageSerializer(rest_serializers.Serializer):
    MA55=rest_serializers.ListField()
    MA50=rest_serializers.ListField()
    MA21=rest_serializers.ListField()
    MA20=rest_serializers.ListField()
    MA10=rest_serializers.ListField()
    MA8=rest_serializers.ListField()
    ALEN1050=rest_serializers.DictField()
    ALEN520=rest_serializers.DictField()