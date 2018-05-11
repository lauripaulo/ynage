from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    context = {
        'test_message': 'This is django!!!'
    } 
    return render(request, 'home/index.html', context)