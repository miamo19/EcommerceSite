from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from store.models import Product

# Create your views here.
def home(response):
    return HttpResponse('Hello World')
def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={'pdt':products})

def product_details(request, slug):
    #product = Product.objects.get(slug=lug) this is same as below code
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', {'products':product})