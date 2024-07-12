from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter() # our router

router.register('list', views.DoctorViewSet) #router antena
router.register('specialization', views.SpecializationViewSet) #router antena
router.register('list', views.DesignationViewSet) #router antena
router.register('available_time', views.AvailableTimeViewSet) #router antena
router.register('reviews', views.ReviewViewSet) #router antena

urlpatterns = [
    path('', include(router.urls)),
]