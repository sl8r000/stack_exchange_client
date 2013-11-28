import ConfigParser
import os

from stack_exchange_client import StackExchangeClient

if __name__ == '__main__':
    parser = ConfigParser.ConfigParser()
    parser.read(os.path.dirname(os.path.realpath(__file__)) + '/config.ini')
    site = parser.get('Stack Exchange Info', 'site')
    client_id = parser.get('Stack Exchange Info', 'client_id')
    key = parser.get('Stack Exchange Info', 'key')

    if client_id != '' and key != '' and site != '':
        client = StackExchangeClient(site=site, client_id=int(client_id), key=key)

    print 'Object client ready.'
