from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter() # our router

router.register('appointment', views.AppointmentViewSet) #router antena
urlpatterns = [
    path('', include(router.urls)),
]