from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter() # our router

router.register('services', views.ServiceViewSet) 
urlpatterns = [
    path('', include(router.urls)),
]