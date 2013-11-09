from base_http_client import BaseHTTPClient


class AnswersIds(BaseHTTPClient):

    @property
    def comments(self):
        url = self.url + 'comments/'
        return BaseHTTPClient(url, self.queryvars)


class Answers(BaseHTTPClient):

    def ids(self, id_or_ids):
        if isinstance(id_or_ids, list):
            url = self.url + ';'.join(str(input_id) for input_id in id_or_ids) + '/'
        else:
            url = self.url + str(id_or_ids) + '/'
        return AnswersIds(url, self.queryvars)
