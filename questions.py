from base_http_client import BaseHTTPClient


class QuestionsIds(BaseHTTPClient):

    @property
    def answers(self):
        return BaseHTTPClient(self.url + 'answers/', self.queryvars)

    @property
    def comments(self):
        return BaseHTTPClient(self.url + 'comments/', self.queryvars)

    @property
    def linked(self):
        return BaseHTTPClient(self.url + 'linked/', self.queryvars)

    @property
    def related(self):
        return BaseHTTPClient(self.url + 'related/', self.queryvars)

    @property
    def timeline(self):
        return BaseHTTPClient(self.url + 'timeline/', self.queryvars)


class Questions(BaseHTTPClient):

    def ids(self, id_or_ids):
        if isinstance(id_or_ids, list):
            url = self.url + ';'.join(str(input_id) for input_id in id_or_ids) + '/'
        else:
            url = self.url + str(id_or_ids) + '/'
        return QuestionsIds(url, self.queryvars)

    @property
    def featured(self):
        return BaseHTTPClient(self.url + 'featured/', self.queryvars)

    @property
    def unanswered(self):
        return BaseHTTPClient(self.url + 'unanswered/', self.queryvars)

    @property
    def no_answers(self):
        return BaseHTTPClient(self.url + 'no-answers/', self.queryvars)
