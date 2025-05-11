from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.new, name= 'new'),
    path("order/",views.order, name='order')
]