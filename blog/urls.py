from django.shortcuts import render
from django.urls import path
from blog.views import home, kategori_list

urlpatterns = [
    path('', home, name='home' ),
    path('kategori_list', kategori_list, name='kategori_list'),
]