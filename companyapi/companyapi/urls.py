"""
URL configuration for companyapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

"""

from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/",views.home, name="home"),
    path("api/",include("trendsapi.urls")),
    path("api-auth/",include("rest_framework.urls")),
    path("api/token/",obtain_auth_token)
]
