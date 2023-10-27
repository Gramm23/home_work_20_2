from django.shortcuts import render

from main.models import Product


def index(request):
    products = Product.objects.all()
    context = {
        "object_list": products
    }
    return render(request, 'main/index.html', context)


def product_info(request, product_id):
    product = Product.objects.get(id=product_id)
    data = {
        "product": product
    }
    return render(request, 'main/info.html', data)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Name: {name}, (Email: {email}), Message: {message}')
    return render(request, 'main/contact.html')
