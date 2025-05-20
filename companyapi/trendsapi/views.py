from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Roc_Trends
from .serializer import Roc_Trends_serializer

# Create your views here.
class Roc_Trends_viewset(viewsets.ModelViewSet):
    queryset= Roc_Trends.objects.all()
    serializer_class= Roc_Trends_serializer
    permission_classes= [IsAuthenticated]