from django.urls import re_path as url,include 
from Customer import views 
#Json Formate
# http://127.0.0.1:8000/api/Customer
urlpatterns = [ 
    url(r'^api/Customer$', views.Customer_list),
    url(r'^api/Customer/(?P<pk>[0-9]+)$', views.Customer_detail),
    url(r'^api/Customer/published$', views.Customer_list_published),
    url(r'^products/$', views.product_list, name='product_list'),
    url(r'^create/$', views.product_create, name='product_create'),
    url(r'^products/(?P<pk>\d+)/update/$', views.product_update, name='product_update'),
    url(r'^products/(?P<pk>\d+)/delete/$', views.product_delete, name='product_delete'),
]