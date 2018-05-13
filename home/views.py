from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from home.homelib import RepositoryHandler
from home.forms import SearchForm


# Create your views here.
def index(request):
    form = SearchForm()
    context = {
        'test_message': 'django index page.',
        'form': form
    }
    return render(request, 'home/index.html', context)


def browse(request):
    form = SearchForm(request.POST)
    if form.is_valid():
        keyword = request.POST['keyword']
        language = request.POST['language']
        context = {
            'test_message': 'django browse page.',
            'keyword': keyword,
            'language': language
        }
    return render(request, 'home/browse.html', context)
