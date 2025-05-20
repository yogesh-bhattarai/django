from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import Roc_Trends_viewset

router= DefaultRouter()
router.register('Roc_trends',Roc_Trends_viewset,basename='Roc_trends')

urlpatterns=[
    path('',include(router.urls))
]