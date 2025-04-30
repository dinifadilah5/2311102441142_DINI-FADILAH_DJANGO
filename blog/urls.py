from xml.etree.ElementInclude import include

from django.shortcuts import render
from django.urls import path
from blog.views import kategori_list,home

urlpatterns = [
    path('', home, name='home' ),
    path('myweb/', include('myweb.urls')),
    path('kategori/list', kategori_list, name='kategori_list'),

]