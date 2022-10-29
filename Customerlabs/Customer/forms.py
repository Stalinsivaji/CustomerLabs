from django import forms
from Customer.models import Customer
  
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('id','name', 'email', 'gender', 'dob', 'mobile')
        
    