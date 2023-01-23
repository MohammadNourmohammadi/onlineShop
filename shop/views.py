from django.shortcuts import render
from django.views import generic
from .models import Product, Category
from cart.forms import Add2CartForm


class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

    def get_queryset(self):
        return Category.objects.all()


class ProductDetailView(generic.DetailView):
    context_object_name = 'product'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Add2CartForm()
        return context
