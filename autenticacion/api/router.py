# from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import autoViewset

router_aut = DefaultRouter()
router_aut.register(prefix='Autologin',basename='Autologin',viewset=autoViewset)


