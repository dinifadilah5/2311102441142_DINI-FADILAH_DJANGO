from xml.etree.ElementInclude import include

from django.shortcuts import render
from django.urls import path
from blog.views import (
    kategori_list,
    home,
    dashboard,
    kategori_add,
    kategori_update,
    kategori_delete,
    artikel_list, artikel_delete, artikel_detail, artikel_update, artikel_add
)

urlpatterns = [
    path('', dashboard, name='dashboard' ),
    # path('myweb/', include('myweb.urls')),
    path('kategori/list', kategori_list, name='kategori_list'),
    path('kategori/add', kategori_add, name='kategori_add'),
    path('kategori/update/<int:id_kategori>', kategori_update, name='kategori_update'),
    path('kategori/delete/<int:id_kategori>', kategori_delete, name='kategori_delete'),
    path('artikel/list', artikel_list, name='artikel_list' ),
    path('artikel/add', artikel_add, name='artikel_add' ),
    path('artikel/detail/<int:id_artikel>', artikel_detail, name='artikel_detail' ),
    path('artikel/update/<int:id_artikel>', artikel_update, name='artikel_update'),
    path('artikel/delete/<int:id_artikel>', artikel_delete, name='artikel_delete'),

]