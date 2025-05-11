from rest_framework import serializers
from .models import Company

class CompanySerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Company
        fields= '__all__'
