import ast
import json
import base64
import requests
import subprocess

from io import BytesIO
from io import StringIO
from robot.libraries.BuiltIn import BuiltIn

from common.Utils import Utils
from common.JsonUtils import JsonUtils


class RestRequest:
    def __init__(self):
        self.at = -1
        self.utils = Utils()
        self.json_utils = JsonUtils()

    def generate_access_token(self, username, password, path="login"):
        """
        - This Keyword is used to get the access token
        :param username: username
        :param password: password
        :param path: API Endpoint path
        :return: returns access_token
        """
        self.utils.print_info("Username: ", username)
        self.utils.print_info("Password: ", password)

        access_token = -1
        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        self.utils.print_info("Base URL: ", base_url)

        url = f"{base_url}/{path}"
        data_raw = '{"username": "' + username + '" , "password": "' + password + '"}'
        headers = {'Content-Type': 'application/json'}

        curl_cmd = f"curl --location --request POST {base_url}/{path} --header 'Content-Type: application/json' --data-raw '{data_raw}'"
        self.utils.print_info("====================================")
        self.utils.print_info("Curl Command: ", curl_cmd)
        self.utils.print_info("====================================")

        try:
            response = requests.request("POST", url, headers=headers, data=data_raw)
        except Exception as e:
            self.utils.print_info("Error: ", e)
            return -1

        if response.text:
            self.utils.print_info("response text: ", response.text)

            try:
                access_token = self.json_utils.get_json_value(response.text, "access_token")
            except Exception as e:
                self.utils.print_info(e)

            self.at = access_token
            return access_token
        else:
            self.utils.print_info("No response from REST Gateway")
            return -1

    def rest_api_get(self, path, access_token="default"):
        """
        - This Keyword is used to get the access token
        :param access_token: access token
        :param path: API Endpoint path
        :return: returns access_token
        """
        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")
            self.utils.print_info("Reusing existing Access Token: ", access_token)

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        self.utils.print_info("Base URL: ", base_url)

        url = base_url + path
        curl_cmd = f"curl -v --location --request GET '{url}' --header 'Authorization: Bearer {access_token}'"

        self.utils.print_info("====================================")
        self.utils.print_info("Curl Command: ", curl_cmd)
        self.utils.print_info("====================================")

        data_raw = {}
        headers = {'Authorization': 'Bearer ' + access_token}

        self.utils.print_info("API URL: ", url)
        self.utils.print_info("API Headers: ", headers)

        try:
            response = requests.request("GET", url, headers=headers, data=data_raw)
            get_response = json.dumps(json.loads(response.text), indent=4, sort_keys=True)
            self.utils.print_info("Response Code: ", response)
            self.utils.print_info("Response Info: ", response.text)

            return response.text
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def rest_api_post(self, path, post_data, access_token = "default", return_output="default", result_code="default", role="default"):
        """
        - This Keyword is used for REST API post
        :param path: URL Path
        :param post_data: data to post
        :param access_token: access token
        :return: returns output
        """
        self.utils.print_info("Return Output :", return_output)
        self.utils.print_info("Role : ", role)

        self.utils.print_info("URL Path : ", path)
        self.utils.print_info("POST Data: ", post_data)

        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url = base_url + path

        curl_cmd = f"curl -v --location --request POST '{url}' -H 'Content-Type: application/json' -H 'Authorization: Bearer {access_token}' -d " + post_data

        self.utils.print_info("*****************************")
        self.utils.print_info("Curl Command: ", curl_cmd.encode())

        process = subprocess.Popen(curl_cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        self.utils.print_info("stdout: ", stdout)
        self.utils.print_info("stderr: ", stderr)

        return stdout
