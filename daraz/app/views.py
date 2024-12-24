from django.shortcuts import render
from . models import Mens, Womens, Product

def app (request) :

    appData = Mens.objects.all()

    data = {
        'tittle' : 'Mens Product at Daraz . . .',
        'appData' : appData
    }

    return render (request, 'index.html', {'data' : data})

def women (request) :

    womenData = Womens.objects.all()

    data = {
        'tittle' : 'Women Product at Daraz . . .',
        'womenData' : womenData
    }
    
    return render (request, 'women.html', {'data' : data})

def product_list(request, category=None):
    if category:
        # Normalize the category to match the model's category values (capitalized)
        category = category.capitalize()
        products = Product.objects.filter(categories=category)
    else:
        products = Product.objects.all()

    return render(request, 'index.html', {'products': products})