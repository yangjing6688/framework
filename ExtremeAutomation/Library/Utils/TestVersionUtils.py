
import inspect
import logging
import requests
import json
import os
import base64


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class JobsSuitesVersions():
    """ Manage data inside the tbedmgr 'jobsSuitesVersions' table """ 

    # Retrieve the 'encoded' URL and PAT string from the ENV:
    #
    magic_key = os.getenv('MAGIC_KEY')
    base64_bytes = magic_key.encode("ascii")
    string_bytes = base64.b64decode(base64_bytes)
    decoded_magic_key = string_bytes.decode("ascii")
    decoded_pat,base_url = decoded_magic_key.split('#')

    # TODO: Remove this: For local testing only
    base_url = 'http://vossbld-6.extremenetworks.com:8087'

    test_version_url = base_url + '/tbedmgr/testsuites/storeversioninfo'

    test_headers = {
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'authorization': 'PAT ' + decoded_pat
        }

    url = test_version_url
    headers = test_headers

    def post(self, **kwargs):
        """ Add data via the tbedmgr microservice """

        json_data = {
            "name": kwargs.get('name'),
            "version": kwargs.get('version'),
            "type": kwargs.get('type'),
            "jobsSuites_uuid": kwargs.get('jobsSuites_uuid')
        }

        try:
            res = requests.post(self.url, headers=self.headers, json=json_data)
            res.raise_for_status()
        except (Exception, requests.exceptions.HTTPError) as e:
            msg = f"Error: {res.text}, {str(e)}"
            logger.exception(msg)
            return msg
        return True

if __name__ == '__main__':

    test_data = {
        "name": "some name",
        "version": "some version data",
        "type": "some type",
        "jobsSuites_uuid": "7b60c0b4-aa7a-43fd-b71f-6ed6aa9f76b3"
    }
    cls = JobsSuitesVersions()
    print(cls.post(**test_data))
