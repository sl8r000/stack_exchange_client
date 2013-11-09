import requests
import time
from database_population.log import logger

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
        if 'backoff' in response:
            print "Backing off for {} seconds".format(response['backoff'])
            time.sleep(response['backoff'])

        logger.debug('Quota Remaining: {}'.format(response['quota_remaining']))

        additional_information = '\n'.join(['{}={}'.format(key, value) for key, value in response.items() if key != 'items'])
        logger.debug('Additional Information:\n{}'.format(additional_information))

        return response['items']


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


class CommentsIds(BaseHTTPClient):
    pass


class Comments(BaseHTTPClient):

    def ids(self, id_or_ids):
        if isinstance(id_or_ids, list):
            url = self.url + ';'.join(str(input_id) for input_id in id_or_ids) + '/'
        else:
            url = self.url + str(id_or_ids) + '/'
        return CommentsIds(url, self.queryvars)


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


class Search(BaseHTTPClient):

    @property
    def advanced(self):
        return BaseHTTPClient(self.url + 'advanced/', self.queryvars)


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


class StackExchangeClient(object):

    BASE_URL = 'http://api.stackexchange.com/2.1/'

    def __init__(self, site, client_id, key):
        self.site = site
        self.client_id = client_id
        self.key = key

        self.url = StackExchangeClient.BASE_URL
        self.queryvars = {'site': self.site, 'client_id': self.client_id, 'key': self.key}

    @property
    def answers(self):
        url = self.url + 'answers/'
        return Answers(url, self.queryvars)

    @property
    def comments(self):
        url = self.url + 'comments/'
        return Comments(url, self.queryvars)

    @property
    def questions(self):
        url = self.url + 'questions/'
        return Questions(url, self.queryvars)

    @property
    def users(self):
        url = self.url + 'users/'
        return Users(url, self.queryvars)

    @property
    def search(self):
        return Search(self.url + 'search/', self.queryvars)

    @property
    def tags(self):
        return Tags(self.url + 'tags/', self.queryvars)