"""
Ynage class library with utilities and helper classes.
"""

import dateparser
from github import Github
from home.models import GithubRepository

CLIENT_ID = '260496816d82dc2ed7c2'
CLIENT_SECRET = '87f7f6112c5d9c94aaad5d4b5e03d880a5627d15'


class GithubHelper:
    """
    helper class to deal with Github stuff.
    """
    gh: Github

    def __init__(self):
        self.gh = Github(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, per_page=5)
        self.repository_list = []

    def search(self, keyword, language):
        """
        search all repos that matches the keyword and language parameters. Returns a PaginatedList object.
        :param keyword: string
        :param language: string
        """
        list = self.gh.search_repositories(keyword, 'stars', 'desc', language=language, archived='false', fork='false')
        self.repository_list = list[:5]


class RepositoryHandler:

    def get_remote_repositories(self, keyword, language):
        gh = GithubHelper()
        gh.search(keyword, language)
        data_list = []
        for repository in gh.repository_list:
            data = self.repo2model(repository)
            data.save()
            data_list.append(data)
        return data_list

    def delete(self, id):
        GithubRepository.objects.filter(id=id).delete()

    @staticmethod
    def list_saved_repositories():
        return GithubRepository.objects.all()

    @staticmethod
    def repo2model(repo):
        """
        creates a data model class from a github repository class
        :param repo: Repository
        :return: model.GithubRepository
        """
        data = GithubRepository()
        data.id = repo.id
        data.name = repo.name
        data.full_name = repo.full_name if repo.full_name != None else ""
        data.description = repo.description if repo.description != None else ""
        data.fork = repo.fork
        data.url = repo.url
        data.created_at = dateparser.parse(str(repo.created_at))
        data.homepage = repo.homepage if repo.homepage != None else ""
        data.size = repo.size
        data.language = repo.language
        data.open_issues = repo.open_issues
        data.watchers = repo.watchers
        data.html_url = repo.html_url if repo.html_url else ""
        data.git_url = repo.git_url if repo.git_url else ""
        return data


if __name__ == '__main__':
    gh = GithubHelper()
    gh.search('arduino', 'Java')
    result = gh.repository_list
    for repo in gh.repository_list:
        print('Id:{} - Name: {}'.format(repo.id, repo.name))
        print('Description: {}'.format(repo.description))
        print('Language: {}'.format(repo.language))
        print('URL: {}'.format(repo.url))
        print('')

    # print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    # rh = RepositoryHandler()
    # repositories = rh.get_remote_repositories('raspberry', 'C')
    # for repo in repositories:
    #     print('Id:{} - Name: {}'.format(repo.id, repo.name))
    #     print('Description: {}'.format(repo.description))
    #     print('Language: {}'.format(repo.language))
    #     print('URL: {}'.format(repo.url))
    #     print('')
