from unittest.mock import MagicMock

from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from django.utils.timezone import now

from home.homelib import RepositoryHandler, GithubHelper
from home.views import index, browse, delete


# Create your tests here.

class RepositoryHandlerTestCase(TestCase):

    def test_homelib_repo2model_fullfields_ok(self):
        timestamp = now()
        data = MagicMock()
        data.id = MagicMock(return_value=1)
        data.name = MagicMock(return_value='name')
        data.full_name = MagicMock(return_value='full_name')
        data.description = MagicMock(return_value='description')
        data.fork = MagicMock(return_value=1)
        data.url = MagicMock(return_value='url')
        data.created_at = MagicMock(return_value=timestamp)
        data.homepage = MagicMock(return_value='homepage')
        data.size = MagicMock(return_value='size')
        data.language = MagicMock(return_value='language')
        data.open_issues = MagicMock(return_value='open_issues')
        data.watchers = MagicMock(return_value=1)
        data.html_url = MagicMock(return_value='html_url')
        data.git_url = MagicMock(return_value='git_url')
        model = RepositoryHandler.repo2model(data)
        self.assertEqual(data.id, model.id)
        self.assertEqual(data.name, model.name)
        self.assertEqual(data.full_name, model.full_name)
        self.assertEqual(data.description, model.description)
        self.assertEqual(data.fork, model.fork)
        self.assertEqual(data.url, model.url)
        self.assertEqual(data.created_at, model.created_at)
        self.assertEqual(data.homepage, model.homepage)
        self.assertEqual(data.size, model.size)
        self.assertEqual(data.language, model.language)
        self.assertEqual(data.open_issues, model.open_issues)
        self.assertEqual(data.watchers, model.watchers)
        self.assertEqual(data.html_url, model.html_url)
        self.assertEqual(data.git_url, model.git_url)

    def test_homelib_repo2model_emptyfields(self):
        data = MagicMock()
        data.full_name = MagicMock(return_value=None)
        data.description = MagicMock(return_value=None)
        data.homepage = MagicMock(return_value=None)
        data.html_url = MagicMock(return_value=None)
        data.git_url = MagicMock(return_value=None)
        model = RepositoryHandler.repo2model(data)
        self.assertEqual(len(model.full_name), 0)
        self.assertEqual(len(model.description), 0)
        self.assertEqual(len(model.homepage), 0)
        self.assertEqual(len(model.html_url), 0)
        self.assertEqual(len(model.git_url), 0)


class GithubHelperTestCase(TestCase):

    def test_search_all_fields(self):
        helper = GithubHelper()
        helper.gh.search_repositories = \
            MagicMock(return_value=['repository1', 'repository2',
                                    'repository3', 'repository4',
                                    'repository5', 'repository6'])
        helper.search('keyword', 'language')
        self.assertEqual(len(helper.repository_list), 5)
        self.assertEqual(helper.repository_list[0], 'repository1')
        self.assertEqual(helper.repository_list[1], 'repository2')
        self.assertEqual(helper.repository_list[2], 'repository3')
        self.assertEqual(helper.repository_list[3], 'repository4')
        self.assertEqual(helper.repository_list[4], 'repository5')


class RepositoryHandlerTestCase(TestCase):

    def test_get_remote_repositories(self):
        model = MagicMock()
        model.save = MagicMock()
        handler = RepositoryHandler()
        handler.helper.search = MagicMock()
        handler.helper.repository_list = ['repository1']
        handler.repo2model = MagicMock(return_value=model)
        result = handler.get_remote_repositories('keyword', 'language')
        handler.helper.search.assert_called_with('keyword', 'language')
        self.assertEqual(result[0], model)


class IndexPageTest(TestCase):

    def test_root_url_resolves_to_index(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertIn('<h1>Github shiny repositories search tool</h1>', html)
        self.assertIn('<form action="/browse/" method="post">', html)
        self.assertIn('<input class="btn btn-primary" type="submit" value="Search and save"/>', html)


class BrowsePageTest(TestCase):

    def test_browse_url_resolves_to_browse(self):
        found = resolve('/browse/')
        self.assertEqual(found.func, browse)

    def test_browse_returns_correct_html(self):
        request = HttpRequest()
        response = browse(request)
        html = response.content.decode('utf8')
        self.assertIn('<h1>Github saved repositories</h1>', html)
        self.assertIn('<p class="lead">Here you can browse and see details of your saved repositories.</p>', html)

    def test_browse_request_post(self):
        request = HttpRequest()
        request.POST = {'keyword': 'test', 'language': '0'}
        response = browse(request)
        html = response.content.decode('utf8')
        self.assertIn('<h1>Github saved repositories</h1>', html)
        self.assertIn('<p class="lead">Here you can browse and see details of your saved repositories.</p>', html)

class DeletePageTest(TestCase):

    def test_delete_url_resolves_to_browse(self):
        found = resolve('/delete/1/')
        self.assertEqual(found.func, delete)
