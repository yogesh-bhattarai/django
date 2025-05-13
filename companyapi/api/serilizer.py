from rest_framework import serializers
from .models import Company, Employee

class CompanySerilizer(serializers.HyperlinkedModelSerializer):
    company_id= serializers.ReadOnlyField()
    class Meta:
        model= Company
        fields= '__all__'


class EmployeeSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Employee
        fields= '__all__'
