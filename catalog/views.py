from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product, Category

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def new_product(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        category_fk = request.POST['category_id']
        category = Category.objects.get(id=category_fk)
        image_file = request.FILES.get('image_product')
        price = request.POST['price']
        product = Product(name=name, description=description, image_product=image_file, category=category, price=price)
        product.save()
        context = {'categories': categories,
                   'product_added': True}
        return render(request, 'new_product.html', context)
    else:
        context = {'categories': categories,
                   'product_added': False}
        return render(request, 'new_product.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(name, phone, message)
        return HttpResponse('Данные успешно отправлены')
    else:
        return render(request, 'contacts.html')
