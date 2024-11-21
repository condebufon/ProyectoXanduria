from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import userviewset

router_us = DefaultRouter()
router_us.register(prefix='User',basename='User',viewset=userviewset)


