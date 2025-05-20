from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet,EmployeeViewSet
from rest_framework.routers import DefaultRouter

# router= DefaultRouter()
# router.register(r'company', CompanyViewSet)
# router.register(r'employee',EmployeeViewSet)
# urlpatterns = [
# path("", include(router.urls)),

# ]