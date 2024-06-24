from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.account_profile, name='account_profile'),
    path('table/', views.table, name='table'),
    path('add_record/', views.add_record, name='add_record'),
    path('client_record/<int:pk>/', views.client_record, name='client_record'),
    path('delete_record/<int:pk>/', views.delete_record, name='delete_record'),
]
