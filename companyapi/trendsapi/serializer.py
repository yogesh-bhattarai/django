from rest_framework import serializers
from .models import Roc_Trends

class Roc_Trends_serializer(serializers.ModelSerializer):
    class Meta:
        model= Roc_Trends
        fields='__all__'