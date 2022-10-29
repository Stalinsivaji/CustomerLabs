from django.db import models

# Create your models here.
class Customer(models.Model):
    Male = 1
    Female = 2
    Trasansgender = 3
   

    
    PRODUCT_TYPES = (
        (Male, 'Male'),
        (Female, 'Female'),
        (Trasansgender, 'Trasansgender'), 
    )
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50) 
    gender = models.PositiveSmallIntegerField(choices=PRODUCT_TYPES,blank=True,null=True)    
    dob = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)     
    
    class Meta:  
        db_table = "Customer_product"   