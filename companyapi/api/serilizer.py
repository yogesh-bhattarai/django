from rest_framework import serializers
from .models import Company

class CompanySerilizer(serializers.HyperlinkedModelSerializer):
    company_id= serializers.ReadOnlyField()
    class Meta:
        model= Company
        fields= '__all__'
