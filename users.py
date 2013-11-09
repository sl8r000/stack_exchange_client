from base_http_client import BaseHTTPClient


class UsersIds(BaseHTTPClient):

    @property
    def answers(self):
        url = self.url + 'answers/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def badges(self):
        url = self.url + 'badges/'
        return BaseHTTPClient(url, self.queryvars)

    # missing {toid} functionality
    @property
    def comments(self):
        url = self.url + 'comments/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def favorites(self):
        url = self.url + 'favorites/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def mentioned(self):
        url = self.url + 'mentioned/'
        return BaseHTTPClient(url, self.queryvars)

    # missing unread functionality
    @property
    def notifications(self):
        url = self.url + 'notifications/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def privileges(self):
        url = self.url + 'privileges/'
        return BaseHTTPClient(url, self.queryvars)

    # missing featured, no-answers, unaccepted, unanswered functionality
    @property
    def questions(self):
        url = self.url + 'questions/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def reputation(self):
        url = self.url + 'reputation/'
        return BaseHTTPClient(url, self.queryvars)

    # Notice the hyphen. Missing reputation-history functionality
    @property
    def reputation_history(self):
        url = self.url + 'reputation-history/'
        return BaseHTTPClient(url, self.queryvars)

    # Notice the hyphen.
    @property
    def suggested_edits(self):
        url = self.url + 'suggested-edits/'
        return BaseHTTPClient(url, self.queryvars)

    # missing {tags}/top-answers and {tags}/top-questions functionality
    @property
    def tags(self):
        url = self.url + 'tags/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def timeline(self):
        url = self.url + 'timeline/'
        return BaseHTTPClient(url, self.queryvars)

    # Notice the hyphen.
    @property
    def top_answer_tags(self):
        url = self.url + 'top-answer-tags/'
        return BaseHTTPClient(url, self.queryvars)

    # Notice the hyphen.
    @property
    def top_question_tags(self):
        url = self.url + 'top-question-tags/'
        return BaseHTTPClient(url, self.queryvars)

    # Notice the hyphen.
    @property
    def write_permissions(self):
        url = self.url + 'write-permissions/'
        return BaseHTTPClient(url, self.queryvars)

    # Missing unread functionality
    @property
    def inbox(self):
        url = self.url + 'inbox/'
        return BaseHTTPClient(url, self.queryvars)


class Users(BaseHTTPClient):

    # Missing elected functionality
    @property
    def moderators(self):
        url = self.url + 'moderators/'
        return BaseHTTPClient(url, self.queryvars)

    def ids(self, id_or_ids):
        if isinstance(id_or_ids, list):
            url = self.url + ';'.join(str(input_id) for input_id in id_or_ids) + '/'
        else:
            url = self.url + str(id_or_ids) + '/'
        return UsersIds(url, self.queryvars)
