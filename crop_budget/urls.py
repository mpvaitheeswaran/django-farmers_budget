from django.urls import path
from crop_budget import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/login',
    auth_views.LoginView.as_view(template_name='crop_budget/login.html'
        ,redirect_authenticated_user=True),
    name='login'),
]
