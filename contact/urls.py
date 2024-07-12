from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter() # our router

router.register('contact_us', views.ContactUsViewSet) #router antena
urlpatterns = [
    path('', include(router.urls)),
]