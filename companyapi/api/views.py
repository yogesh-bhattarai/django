from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serilizer import CompanySerilizer,EmployeeSerilizer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    serializer_class= CompanySerilizer
    @action(detail= True, methods=['get'])
    def employee(self,request,pk=None):
        company= Company.objects.get(pk=pk)
        emps= Employee.objects.filter(company=company)
        emps_serializer= EmployeeSerilizer(emps,many=True,context= {'request':request})
        return Response(emps_serializer.data)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerilizer