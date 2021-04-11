from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'Ausweg-web/Home.html', {'title': 'Home'})

def store(request):
    context = {}
    return render (request, 'Ausweg-web/store.html', context)

def cart(request):
    context = {}
    return render (request, 'Ausweg-web/cart.html', context)

def checkout(request):
    context = {}
    return render (request, 'Ausweg-web/checkout.html', context)    


def about(request):
    return render (request, 'Ausweg-web/About.html', {'title': 'About'})

