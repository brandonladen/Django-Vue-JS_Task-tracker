from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserLoginAPIView,UserLogoutAPIView, UserRegisterAPIView, view_profile, edit_profile


urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('signup/', UserRegisterAPIView.as_view(), name='signup'),
    
    path('profile/', view_profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    
]