from base_http_client import BaseHTTPClient
from answers import Answers
from comments import Comments
from questions import Questions
from users import Users
from tags import Tags


class Search(BaseHTTPClient):

    @property
    def advanced(self):
        return BaseHTTPClient(self.url + 'advanced/', self.queryvars)


class StackExchangeClient(object):

    BASE_URL = 'http://api.stackexchange.com/2.1/'

    def __init__(self, site, client_id, key):
        self.site = site
        self.client_id = client_id
        self.key = key

        self.url = StackExchangeClient.BASE_URL
        self.queryvars = {'site': self.site, 'client_id': self.client_id, 'key': self.key}

    @property
    def answers(self):
        url = self.url + 'answers/'
        return Answers(url, self.queryvars)

    @property
    def comments(self):
        url = self.url + 'comments/'
        return Comments(url, self.queryvars)

    @property
    def questions(self):
        url = self.url + 'questions/'
        return Questions(url, self.queryvars)

    @property
    def users(self):
        url = self.url + 'users/'
        return Users(url, self.queryvars)

    @property
    def search(self):
        return Search(self.url + 'search/', self.queryvars)

    @property
    def tags(self):
        return Tags(self.url + 'tags/', self.queryvars)
