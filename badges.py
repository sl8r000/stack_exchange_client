from base_http_client import BaseHTTPClient


class Badges(BaseHTTPClient):

    def ids(self, id_or_ids):
        if isinstance(id_or_ids, list):
            url = self.url + ';'.join(str(input_id) for input_id in id_or_ids) + '/'
        else:
            url = self.url + str(id_or_ids) + '/'
        return BadgesIds(url, self.queryvars)

    @property
    def name(self):
        url = self.url + 'name/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def recipients(self):
        url = self.url + 'recipients/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def tags(self):
        url = self.url + 'tags/'
        return BaseHTTPClient(url, self.queryvars)


class BadgesIds(BaseHTTPClient):

    @property
    def recipients(self):
        url = self.url + 'recipients/'
        return BaseHTTPClient(url, self.queryvars)
