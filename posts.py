from base_http_client import BaseHTTPClient


class Posts(BaseHTTPClient):

    def ids(self, id_or_ids):
        if isinstance(id_or_ids, list):
            url = self.url + ';'.join(str(input_id) for input_id in id_or_ids) + '/'
        else:
            url = self.url + str(id_or_ids) + '/'
        return PostIds(url, self.queryvars)


class PostIds(BaseHTTPClient):

    @property
    def comments(self):
        url = self.url + 'comments/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def revisions(self):
        url = self.url + 'revisions/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def suggested_edits(self):
        url = self.url + 'suggested-edits/'
        return BaseHTTPClient(url, self.queryvars)
