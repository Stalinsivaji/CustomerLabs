"""Customerlabs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path,include
from Customer import views 
from django.urls import re_path as url

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('',views.index),
    url(r'^', include('Customer.urls')),
    url(r'^products/$', views.product_list, name='product_list'),
    url(r'^create/$', views.product_create, name='product_create'),
    url(r'^products/(?P<pk>\d+)/update/$', views.product_update, name='product_update'),
    url(r'^products/(?P<pk>\d+)/delete/$', views.product_delete, name='product_delete'),
]
