from unicodedata import name
from django.urls import path
from crop_budget import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('crop/',views.crop,name='crop'),
    path('accounts/login',
    auth_views.LoginView.as_view(template_name='crop_budget/login.html'
        ,redirect_authenticated_user=True),
    name='login'),
    path('accounts/register',
    views.register,
    name='register'),
    path('accounts/logout/',views.logout,name='logout')
]
