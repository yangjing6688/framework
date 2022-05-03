import json
import requests
import base64
import subprocess
from urllib3.exceptions import InsecureRequestWarning

from extauto.common.Utils import Utils
from extauto.common.Cli import Cli
from robot.libraries.BuiltIn import BuiltIn

class Rest:
    def __init__(self):
        self.utils = Utils()
        self.cli = Cli()
        self.builtin = BuiltIn()

    def generate_access_token(self, auth_code, client_secret, client_id, redirect_uri):
        """
        - This Keyword is used to get the access token

        :param auth_code:
        :param client_secret: client secret key
        :param client_id: client id
        :param redirect_uri: redirect url
        :return: return json result
        """
        url = f"{redirect_uri}/acct-webapp/services/acct/thirdparty/accesstoken?authCode={auth_code}"

        curl_cmd = f"curl --location --request POST '{url}' --header 'X-AH-API-CLIENT-SECRET: {client_secret}' " \
                   f"--header 'X-AH-API-CLIENT-ID: {client_id}'  --header 'X-AH-API-CLIENT-REDIRECT-URI: {redirect_uri}'"

        self.utils.print_info("Curl Command: ", curl_cmd)

        json_response = self.cli.exec_shell_command(curl_cmd)
        try:
            data = self.get_json_value(json_response, "data")
            return json_response
        except KeyError as e:
            err_msg = self.get_json_value(json_response, "error")['message']
            self.builtin.fail(err_msg)

    def get_value_from_gen_access_token_resp(self, json_data, owner_id, key):
        """
        - This method is used to get the key value from generated access token response
        :param json_data: raw json data
        :param owner_id: owner id to get the data
        :return:
        """
        data = self.get_json_value(json_data, "data")
        return data[owner_id][key]

    def _api_requests(self, url, headers, method, data='default'):
        """
        - This method is used to call the API requests using requests

        :param url: api complete url
        :param headers: headers in dictionary format
        :param method: methods to call i.e GET, PUT, POST
        :param data: data to be put or post
        :return: response_code, json_response, total_time
        """
        self.utils.print_info(url)
        self.utils.print_info(headers)

        try:
            if method == "GET":
                r = requests.get(url, headers=headers)

            if method == "POST":
                r = requests.post(url, headers=headers, data=data)

            if method == "PUT":
                r = requests.put(url, headers=headers, data=data)

            if method == "DELETE":
                r = requests.delete(url, headers=headers)

            json_response = r.json()
            response_code = r.status_code
            total_time = r.elapsed.total_seconds()
        except ValueError:
            json_response = "No Output"
            response_code = None
            total_time = None


        self.utils.print_info("HTTP Status Code: ", response_code)
        self.utils.print_info("Response : ", json_response)
        self.utils.print_info("Time: ", total_time)

        return response_code, json_response, total_time

    def xapi_get_method(self, url_path, client_secret, client_id, access_token):
        """
        - This keyword is used to request the REST AIP GET Call
        - Keyword Usage:
         - ``XAPI Get Method  ${URL_PATH}   ${CLIENT_SECRET}   ${CLIENT_ID}   ${ACCESS_TOKEN}

        :param url_path: Complete url path
        :param client_secret: client secret
        :param client_id: client id
        :param access_token: access token
        :return: json response
        """
        headers = {
            "X-AH-API-CLIENT-SECRET": client_secret,
            "X-AH-API-CLIENT-ID": client_id,
            "Authorization": f"Bearer {access_token}",
            "X-AH-API-CLIENT-REDIRECT-URI": "https://extremenetworks.com"
        }

        response_code, json_response, total_time = self._api_requests(url_path, headers, "GET")

        if response_code == 200:
            self.utils.print_info("Success")
            return json_response
        else:
            self.utils.print_info("Failed")
            return json_response

    def generate_auth_code(self, gdc_url, client_id, username, password):
        user_pass = f"{username}:{password}"
        auth_header = base64.b64encode(user_pass.encode()).decode()

        curl_cmd = f"curl -v '{gdc_url}/services/oauth2/authorize?response_type=code&client_id={client_id}&redirect_uri=https://extremenetworks.com' " \
                   f"-H 'Authorization: Basic {auth_header}'"

        self.utils.print_info("****************************************************")
        self.utils.print_info("Curl Command: ", curl_cmd)
        self.utils.print_info("****************************************************")

        # WHY WOULD YOU EVER DO THIS???????
        process = subprocess.Popen(curl_cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        self.utils.print_info("stdout: ", stdout)
        self.utils.print_info("****************************************************")
        self.utils.print_info("stderr: ", stderr)
        self.utils.print_info("****************************************************")

        for line in stderr.split():
            if "code=" in line.decode():
                self.utils.print_info("****************************************************")

                self.utils.print_info("Code Line: ", line)
                self.utils.print_info("Auth Code : ", line.decode().split("code=")[-1])
                self.utils.print_info("****************************************************")

                return line.decode().split("code=")[-1]

        self.builtin.fail("Please check the Curl verbose output")

    def get_data_from_api_resp(self, json_data, device_mac, key_str):
        """
        - This Keyword is used to get the  key_str value from the api response json raw data

        :param json_data:  raw json data from the API call to get the device ids
        :param device_mac: mac of the device to match the dict
        :param key_str:  key string to get the value
        :return: key_str value
        """
        _data = self.get_json_value(json_data, "data")
        for d in _data:
            if d['macAddress'] == device_mac:
                return d[key_str]

        self.builtin.fail("Device details not present json response")
        return -1

    def get_location_id_from_api_resp(self, json_data):
        """
        - This Keyword is used to get the  location id from api response json raw data

        :param json_data:  raw json data from the API call to get the device ids
        :return: location id
        """
        _data = self.get_json_value(json_data, "data")
        location_id = _data['locationId']
        if location_id:
            return location_id
        self.builtin.fail("Device details not present json response")
        return -1

    def get_presence_of_client_from_api_response(self, json_data, client_mac, key_str):
        """
        - This method is used to get the client information from the raw json data
        - Client Mac is required to match the particular clients dict in the json resopnse
        - Keyword Usage:
         - ``Get Presence Of Client From Api Response  ${JSON_DATA}   ${CLIENT_MAC}   clientMacAddress``
         - ``Get Presence Of Client From Api Response  ${JSON_DATA}   ${CLIENT_MAC}   associated``
         - ``Get Presence Of Client From Api Response  ${JSON_DATA}   ${CLIENT_MAC}   engaged``

        :param json_data:
        :param client_mac:
        :param key_str:
        :return: key corresponding value
        """
        _data = self.get_json_value(json_data, "data")
        clients_data = _data['presence']
        for data in clients_data:
            if data['clients'][0]['clientMacAddress'] == client_mac:
                return data['clients'][0][key_str]

        if client_mac in clients_data:
            return client_mac

        self.builtin.fail("The clients presence data not available in the api response")
        return -1

    def get_json_value(self, json_data, json_key):
        self.utils.print_debug("JSON Data: ", json_data)
        self.utils.print_debug("JSON Key: ", json_key)

        json_values = json.loads(json_data)
        self.utils.print_info(json_values)
        return json_values[json_key]

    def get_json_value_recursive(self, json_data, json_key):
        value1 = self.get_json_value(json_data, json_key)
        self.utils.print_info("Value: ", value1)

    # Not used anywhere...  Should we delete? or convert to requests? - petersadej
    # def curl_command(self, _url):
    #     self.utils.print_info("Getting URL: ", _url)
    #     # Suppress only the single warning from urllib3 needed.
    #     requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    #     buf = None
    #     c = None

    #     try:
    #         buf = StringIO()
    #         c = pycurl.Curl()
    #         c.setopt(pycurl.URL, _url)
    #         c.setopt(pycurl.VERBOSE, True)
    #         c.setopt(pycurl.SSL_VERIFYPEER, 0)
    #         c.setopt(pycurl.SSL_VERIFYHOST, 0)
    #         c.setopt(pycurl.WRITEFUNCTION, buf.write)
    #         c.perform()

    #     except Exception as e:
    #         self.utils.print_info(e)
    #         self.utils.print_info("Error while URL Get")

    #     try:
    #         json_response = buf.getvalue()
    #     except ValueError:
    #         json_response = "No Output"

    #     response_code = c.getinfo(pycurl.RESPONSE_CODE)
    #     total_time = c.getinfo(pycurl.TOTAL_TIME)

    #     c.close()

    #     self.utils.print_info("HTTP Status Code: ", response_code)
    #     self.utils.print_info("Response : ", json_response)
    #     self.utils.print_info("Time: ", total_time)

    #     return response_code
