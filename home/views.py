from django.shortcuts import render

from home.forms import SearchForm
from home.homelib import RepositoryHandler


# Create your views here.
def index(request):
    form = SearchForm()
    context = {
        'form': form
    }
    return render(request, 'home/index.html', context)


def browse(request):
    keyword = None
    language = None
    repository_list = []
    form = SearchForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            keyword = request.POST['keyword']
            language_id = int(request.POST['language']) - 1
            language = form.languages[language_id][1]
            ghr = RepositoryHandler()
            repository_list = ghr.get_remote_repositories(keyword, language)
    else:
        ghr = RepositoryHandler()
        repository_list = ghr.list_saved_repositories()
    context = {
        'keyword': keyword,
        'language': language,
        'repository_list': repository_list
    }
    return render(request, 'home/browse.html', context)


def delete(request, delete_id):
    ghr = RepositoryHandler()
    if request.method == 'GET':
        ghr.delete(int(delete_id))
    repository_list = ghr.list_saved_repositories()
    context = {
        'keyword': "",
        'language': "",
        'repository_list': repository_list
    }
    return render(request, 'home/browse.html', context)


def csrf_failure(request, reason=""):
    form = SearchForm()
    context = {
        'form': form,
        'message': "You need to search again, "
                   "probably your browser was idle for too long."
    }
    return render(request, 'home/index.html', context)
