from rest_framework import serializers 
from Customer.models import Customer
  
class CustomerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Customer
        fields = ('id'
                  'name',
                  'email',
                  'gender',
                  'dob',
                  'mobile'
                  )
        
            