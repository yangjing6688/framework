import json
import requests

from robot.libraries.BuiltIn import BuiltIn

from extauto.common.Cli import Cli
from extauto.common.Utils import Utils

class NetworkPolicy:
    def __init__(self):
        self.cli = Cli()
        self.utils = Utils()

    def get_list_of_network_policy_ids(self, path, access_token="default"):
        """
        - This Keyword is used to send a get request and print the output
        :param path: API Endpoint path
        :param access_token: access token
        :return: returns list of network policy ids
        """
        response = self._rest_api_get_response(path, access_token=access_token)
        self.utils.print_info("Response Code: ", response)
        assert response.status_code == requests.codes.ok
        try:
            get_response = json.loads(response.text)
            self.utils.print_info("Response Info: ", get_response)
            if 'data' in get_response:
                return [ x['id'] for x in get_response['data']]

        except Exception as e:
            self.utils.print_info(e)

    def _prepare_rest_request(self, path, access_token="default"):
        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")
            self.utils.print_info("Reusing existing Access Token: ", access_token)

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        self.utils.print_info("Base URL: ", base_url)

        url = base_url + path

        headers = {'Authorization': 'Bearer ' + access_token}

        self.utils.print_info("API URL: ", url)
        self.utils.print_info("API Headers: ", headers)

        return url, headers


    def rest_api_get_check(self, path, access_token="default", status_code=200):
        """
        - This Keyword is used to initiate a get request and check the return status

        :param access_token: access token
        :param path: API Endpoint path
        :param status_code: Rest api response code to verify
        :return: returns access_token
        """
        response = self._rest_api_get_response(path, access_token=access_token)
        self.utils.print_info("Response Code: ", response)
        assert response.status_code == status_code
        try:
            get_response = json.dumps(json.loads(response.text), indent=4, sort_keys=True)
            self.utils.print_info("Response Info: ", get_response)
            return get_response
        except Exception as e:
            self.utils.print_info(e)

    def rest_api_get_check_not(self, path, access_token="default", status_code=200):
        """
        - This Keyword is used to initiate a get request and fail if the request has failed

        :param access_token: access token
        :param path: API Endpoint path
        :param status_code: Rest api response code to verify
        :return: returns access_token
        """
        response = self._rest_api_get_response(path, access_token=access_token)
        self.utils.print_info("Response Code: ", response)
        assert response.status_code != requests.codes.ok
        try:
            get_response = json.dumps(json.loads(response.text), indent=4, sort_keys=True)
            self.utils.print_info("Response Info: ", get_response)
            return get_response
        except Exception as e:
            self.utils.print_info(e)

    def _rest_api_get_response(self, path, access_token="default"):
        url, headers = self._prepare_rest_request(path, access_token = access_token)
        data_raw = {}
        try:
            return requests.request("GET", url, headers=headers, data=data_raw)

        except Exception as e:
            self.utils.print_info(e)
