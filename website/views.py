from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'Ausweg-web/Home.html')

def about(request):
    return render (request, 'Ausweg-web/About.html', {'title': 'About'})

