from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter() # our router

router.register('list', views.PatientViewSet) #router antena
urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationApiView.as_view(), name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.UserLogutView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', views.activate, name='active'),
]