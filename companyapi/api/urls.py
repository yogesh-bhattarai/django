from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r'company', CompanyViewSet)
urlpatterns = [
path("", include(router.urls)),

]