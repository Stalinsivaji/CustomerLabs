from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from Customer.models import Customer
from Customer.serializers import CustomerSerializer
from rest_framework.decorators import api_view
from django.template.loader import render_to_string

from django.shortcuts import render, redirect, get_object_or_404
 
from Customer.models import Customer
from Customer.forms import CustomerForm
 
from django.http import JsonResponse

 
def index(request):
    return render(request, 'index.html')

@api_view(['GET', 'POST', 'DELETE'])
def Customer_list(request):
    if request.method == 'GET':
        customer = Customer.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            customer = customer.filter(title__icontains=title)
        
        customer_serializer = CustomerSerializer(customer, many=True)
        return JsonResponse(customer_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Customer.objects.all().delete()
        return JsonResponse({'message': '{} Customer were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def Customer_detail(request, pk):
    try: 
        customer = Customer.objects.get(pk=pk) 
    except Customer.DoesNotExist: 
        return JsonResponse({'message': 'The customer does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        customer_serializer = Customer(customer) 
        return JsonResponse(customer_serializer.data) 
 
    elif request.method == 'PUT': 
        customer_data = JSONParser().parse(request) 
        customer_serializer = Customer(customer, data=customer_data) 
        if customer_serializer.is_valid(): 
            customer_serializer.save() 
            return JsonResponse(customer_serializer.data) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        customer.delete() 
        return JsonResponse({'message': 'Customer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def Customer_list_published(request):
    customer = Customer.objects.filter(published=True)
        
    if request.method == 'GET': 
        customer_serializer = CustomerSerializer(customer, many=True)
        return JsonResponse(customer_serializer.data, safe=False)
    
def product_list(request):
    products = Customer.objects.all()
    return render(request, 'product_list.html', {'products': products})

def save_product_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            products = Customer.objects.all()
            data['html_product_list'] = render_to_string('partial_product_list.html', {
                'products': products
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
 
 
def product_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
    else:
        form = CustomerForm()
    return save_product_form(request, form, 'partial_product_create.html')
 
 
def product_update(request, pk):
    product = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=product)
    else:
        form = CustomerForm(instance=product)
    return save_product_form(request, form, 'partial_product_update.html')
 
 
def product_delete(request, pk):
    product = get_object_or_404(Customer, pk=pk)
    data = dict()
    if request.method == 'POST':
        product.delete()
        data['form_is_valid'] = True
        products = Customer.objects.all()
        data['html_product_list'] = render_to_string('partial_product_list.html', {
            'products': products
        })
    else:
        context = {'product': product}
        data['html_form'] = render_to_string('partial_product_delete.html', context, request=request)
    return JsonResponse(data)