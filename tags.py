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
        return TopTagsSuffix(self.url + 'top-askers/', self.queryvars)

    @property
    def top_answerers(self):
        return TopTagsSuffix(self.url + 'top-answerers/', self.queryvars)


class TopTagsSuffix(BaseHTTPClient):

    @property
    def month(self):
        return self._periods('month')

    @property
    def all_time(self):
        return self._periods('all_time')

    def _periods(self, month_or_all_time):
        if month_or_all_time not in ['month', 'all_time']:
            raise Exception('Input {} must be equal to either "month" or "all_time"'.format(month_or_all_time))

        return BaseHTTPClient(self.url + '{}/'.format(month_or_all_time), self.queryvars)


class Tags(BaseHTTPClient):

    def tags(self, tag_or_tags):
        if isinstance(tag_or_tags, list):
            url = self.url + ';'.join(str(tag) for tag in tag_or_tags) + '/'
        else:
            url = self.url + str(tag_or_tags) + '/'
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
