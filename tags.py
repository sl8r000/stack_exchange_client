from base_http_client import BaseHTTPClient


class TagsIds(BaseHTTPClient):

    @property
    def info(self):
        return BaseHTTPClient(self.url + 'info/', self.queryvars)

    @property
    def faq(self):
        return BaseHTTPClient(self.url + 'faq/', self.queryvars)

    @property
    def related(self):
        return BaseHTTPClient(self.url + 'related/', self.queryvars)

    @property
    def synonyms(self):
        return BaseHTTPClient(self.url + 'synonyms/', self.queryvars)

    @property
    def wikis(self):
        return BaseHTTPClient(self.url + 'wikis/', self.queryvars)

    @property
    def top_askers(self):
        return BaseHTTPClient(self.url + 'top-askers/all_time', self.queryvars)

    @property
    def top_answerers(self):
        return BaseHTTPClient(self.url + 'top-answerers/all_time', self.queryvars)


class Tags(BaseHTTPClient):

    def ids(self, id_or_ids):
        if isinstance(id_or_ids, list):
            url = self.url + ';'.join(str(input_id) for input_id in id_or_ids) + '/'
        else:
            url = self.url + str(id_or_ids) + '/'
        return TagsIds(url, self.queryvars)

    @property
    def moderator_only(self):
        return BaseHTTPClient(self.url + 'moderator-only/', self.queryvars)

    @property
    def required(self):
        return BaseHTTPClient(self.url + 'required/', self.queryvars)

    @property
    def synonyms(self):
        return BaseHTTPClient(self.url + 'synonyms/', self.queryvars)
