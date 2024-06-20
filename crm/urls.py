from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.account_profile, name='account_profile'),
    path('table/', views.table, name='table'),
]
