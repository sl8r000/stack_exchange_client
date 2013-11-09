from base_http_client import BaseHTTPClient


class CommentsIds(BaseHTTPClient):
    pass


class Comments(BaseHTTPClient):

    def ids(self, id_or_ids):
        if isinstance(id_or_ids, list):
            url = self.url + ';'.join(str(input_id) for input_id in id_or_ids) + '/'
        else:
            url = self.url + str(id_or_ids) + '/'
        return CommentsIds(url, self.queryvars)
