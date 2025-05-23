"""
URL configuration for myweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from blog.views import kategori_list
from myweb.views import home, blog, contact
from django.urls import include, path
from myweb.auth import akun_login



from django.conf import settings
from django.conf.urls.static import static

############### UNTUK MEDIA ##################
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('index.html', home, name='home'),
    # path('contact-stl.html', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('contact', contact, name='contact'),
    path('kategori_list.html', kategori_list, name='kategori_list'),
    path('dashboard/', include('blog.urls')),
    path('auth/login', akun_login, name='akun_login'),
]

############### UNTUK MEDIA ##################
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
