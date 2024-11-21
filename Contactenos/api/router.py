# from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import contactviewset

router_con = DefaultRouter()
router_con.register(prefix='ContactMessage',basename='ContactMessage',viewset=contactviewset)


