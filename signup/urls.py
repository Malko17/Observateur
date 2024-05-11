from django.urls import path
from .views import UserRegisterView, logout_user, UserEditView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name= 'register'),
    path('logout_user/', logout_user, name='logout_user'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
   
    
]