from base_http_client import BaseHTTPClient


class UserComments(BaseHTTPClient):

    def toid(self, other_user_id):
        return BaseHTTPClient(self.url + '{}/'.format(other_user_id))


class UserNotifications(BaseHTTPClient):
    
    @property
    def unread(self):
        return BaseHTTPClient(self.url + 'unread/')


class UserQuestions(BaseHTTPClient):

    @property
    def featured(self):
        return BaseHTTPClient(self.url + 'featured/')

    @property
    def no_answers(self):
        return BaseHTTPClient(self.url + 'no-answers/')

    @property
    def unaccepted(self):
        return BaseHTTPClient(self.url + 'unaccepted/')

    @property
    def unanswered(self):
        return BaseHTTPClient(self.url + 'unanswered/')


class UserReputationHistory(BaseHTTPClient):

    @property
    def full(self):
        return BaseHTTPClient(self.url + 'full/')


class UserTags(BaseHTTPClient):

    def tags(self, tag_or_tags):
        if isinstance(tag_or_tags, list):
            url = self.url + ';'.join(str(tag) for tag in tag_or_tags) + '/'
        else:
            url = self.url + str(tag_or_tags) + '/'
        return UserTagsTags(url, self.queryvars)


class UserTagsTags(BaseHTTPClient):

    @property
    def top_answers(self):
        return BaseHTTPClient(self.url + 'top-answers/')

    @property
    def top_questions(self):
        return BaseHTTPClient(self.url + 'top-questions/')


class UsersIds(BaseHTTPClient):

    @property
    def answers(self):
        url = self.url + 'answers/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def badges(self):
        url = self.url + 'badges/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def comments(self):
        url = self.url + 'comments/'
        return UserComments(url, self.queryvars)

    @property
    def favorites(self):
        url = self.url + 'favorites/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def mentioned(self):
        url = self.url + 'mentioned/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def notifications(self):
        url = self.url + 'notifications/'
        return UserNotifications(url, self.queryvars)

    @property
    def privileges(self):
        url = self.url + 'privileges/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def questions(self):
        url = self.url + 'questions/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def reputation(self):
        url = self.url + 'reputation/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def reputation_history(self):
        url = self.url + 'reputation-history/'
        return UserReputationHistory(url, self.queryvars)

    @property
    def suggested_edits(self):
        url = self.url + 'suggested-edits/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def tags(self):
        url = self.url + 'tags/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def timeline(self):
        url = self.url + 'timeline/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def top_answer_tags(self):
        url = self.url + 'top-answer-tags/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def top_question_tags(self):
        url = self.url + 'top-question-tags/'
        return BaseHTTPClient(url, self.queryvars)

    @property
    def write_permissions(self):
        url = self.url + 'write-permissions/'
        return BaseHTTPClient(url, self.queryvars)


class Moderators(BaseHTTPClient):

    @property
    def elected(self):
        return BaseHTTPClient(self.url + 'elected/', self.queryvars)

class Users(BaseHTTPClient):

    @property
    def moderators(self):
        url = self.url + 'moderators/'
        return Moderators(url, self.queryvars)

    def ids(self, id_or_ids):
        if isinstance(id_or_ids, list):
            url = self.url + ';'.join(str(input_id) for input_id in id_or_ids) + '/'
        else:
            url = self.url + str(id_or_ids) + '/'
        return UsersIds(url, self.queryvars)
