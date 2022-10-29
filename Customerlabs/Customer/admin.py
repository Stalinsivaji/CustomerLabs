# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Customer


class Customers(admin.ModelAdmin):
         list_display= ("id","name","email","gender","dob","mobile")

admin.site.register(Customer,Customers)