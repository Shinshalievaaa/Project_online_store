from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product

def home(request):
    products = Product.objects.order_by('-created_at')[:5]
    for product in products:
        print(product.name)
    return render(request, 'home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(name, phone, message)
        return HttpResponse('Данные успешно отправлены')
    else:
        return render(request, 'contacts.html')
