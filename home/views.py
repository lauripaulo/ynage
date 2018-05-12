from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    context = {
        'test_message': 'django index page.'
    } 
    return render(request, 'home/index.html', context)

def search(request):
    context = {
        'test_message': 'django search page.'
    }
    return render(request, 'homee/search.html', context)

def browse(request):
    context = {
        'test_message': 'django browse page.'
    }
    return render(request, 'home/browse.html', context)