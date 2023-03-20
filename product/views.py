from django.shortcuts import get_object_or_404, render

from product.models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'product/index.html', {'products': products}) 



def detail(request, slug: str):
    products = get_object_or_404(Product, slug=slug)
    return render(request, 'product/detail.html', {'product': products})


