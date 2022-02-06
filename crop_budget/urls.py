from django.urls import path,include
from crop_budget import views

urlpatterns = [
    path('',views.home,name='home'),
]
