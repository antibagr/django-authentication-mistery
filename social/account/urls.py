from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('me/', views.profile, name='account_profile'),
    path('about/', views.about, name='account_about'),
    path('password/', views.change_password, name='account_change_password'),
]
