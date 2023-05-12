from django.shortcuts import render, redirect
from .models import Products
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
products = Products.objects.all()

# Create your views here.



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home_view(request):
    if 'userid' in request.session:
        product = {
            'products' : products
        }
        response = render(request,'home_page/index.html',product) 
        response.set_cookie('test','This data is stored in broweser as a cookie.',600)
        return response
    return redirect('login_page')