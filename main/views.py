from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
    pk_url_kwarg = 'product_id'


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Name: {name}, (Email: {email}), Message: {message}')
    return render(request, 'main/contact.html')


class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'description', 'unit_price', 'image', 'category',)
    success_url = reverse_lazy('main:index')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'description', 'unit_price', 'image', 'category',)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main:index')
