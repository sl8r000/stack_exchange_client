import requests


class BaseHTTPClient(object):
    def __init__(self, url, queryvars):
        self.url = url
        self.queryvars = queryvars
        self.queryvars['pagesize'] = 100

    def get(self, **params):
        all_params = dict(self.queryvars.items() + params.items())
        response = requests.get(self.url, params=all_params)
        response.raise_for_status()

        response = response.json(strict=False)
        return response['items']

    # The lazy man's alias for self.get()
    @property
    def g(self):
        return self.get()
