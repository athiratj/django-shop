from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Welcome to Django project</h1>")

def about(request):
    return HttpResponse("<h1>About page.</h1>")