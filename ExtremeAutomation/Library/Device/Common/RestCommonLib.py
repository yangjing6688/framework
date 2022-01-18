import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
import base64
import json


class RestCommonLib(object):

    @staticmethod
    def getOauthToken(username, password, host, port):
        """
        Returns an oauth token for TRM's rest server.
        """
        urllib3.disable_warnings(InsecureRequestWarning)
        payload = {'grant_type': 'password',
                   'password': password,
                   'username': username,
                   'scope': 'read write',
                   'client_secret': '123456',
                   'client_id': 'clientapp'
                   }

        encoded_auth = base64.b64encode(b'clientapp:123456').decode('ascii')
        header_param = {'Authorization': 'Basic ' + str(encoded_auth),
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                        }
        file_item = requests.post('https://' + host + ':' + str(port) + '/oauth/token?', params=payload,
                                  headers=header_param, verify=False)
        resp_dict = json.loads(file_item.text)

        return resp_dict['access_token']
