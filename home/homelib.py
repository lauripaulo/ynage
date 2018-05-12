"""
Ynage class library with utilities and helper classes.
"""

from github import Github, Repository

CLIENT_ID = '260496816d82dc2ed7c2'
CLIENT_SECRET = '87f7f6112c5d9c94aaad5d4b5e03d880a5627d15'


class GithubHelper:
    """
    helper class to deal with Github stuff.
    """
    gh: Github

    def __init__(self):
        self.gh = Github(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, per_page=5)

    def search(self, keyword, language):
        """
        search all repos that matches the keyword and language parameters. Returns a PaginatedList object.
        :param keyword: string
        :param language: string
        :return: github.PaginatedList.PaginatedList
        """
        result = self.gh.search_repositories(keyword, 'stars', 'asc', language=language, archived='false', fork='false')
        return result[:5]


if __name__ == '__main__':
    gh = GithubHelper()
    result = gh.search('arduino', 'Java')
    for repo in result:
        print('Id:{} - Name: {}'.format(repo.id, repo.name))
        print('Description: {}'.format(repo.description))
        print('Language: {}'.format(repo.language))
        print('URL: {}'.format(repo.url))
        print('')
