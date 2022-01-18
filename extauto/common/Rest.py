import json
import pycurl
from io import StringIO
from common.Utils import Utils
from common.Cli import Cli
from robot.libraries.BuiltIn import BuiltIn
from io import BytesIO
import base64
import subprocess


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

    def _api_requests(self, url, header, method, data='default'):
        """
        - This method is used to call the API requests using pycurl

        :param url: api complete url
        :param header: header in list format
        :param method: methods to call i.e GET, PUT, POST
        :param data: data to be put or post
        :return: response_code, json_response, total_time
        """
        self.utils.print_info(url)
        self.utils.print_info(header)
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.HTTPHEADER, header)
        c.setopt(pycurl.VERBOSE, True)

        if method == "GET":
            c.setopt(pycurl.HTTPGET, 1)

        if method == "POST":
            c.setopt(pycurl.POSTFIELDS, data)

        if method == "PUT":
            c.setopt(pycurl.CUSTOMREQUEST, " PUT ")
            c.setopt(pycurl.POSTFIELDS, data)

        if method == "DELETE":
            c.setopt(pycurl.CUSTOMREQUEST, " DELETE ")

        c.setopt(pycurl.WRITEFUNCTION, buffer.write)
        c.perform()

        try:
            json_response = buffer.getvalue()
        except ValueError:
            json_response = "No Output"

        response_code = c.getinfo(pycurl.RESPONSE_CODE)
        total_time = c.getinfo(pycurl.TOTAL_TIME)

        c.close()

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
        header = [f"X-AH-API-CLIENT-SECRET: {client_secret}",
                  f"X-AH-API-CLIENT-ID: {client_id}",
                  f"Authorization: Bearer {access_token}",
                  f"X-AH-API-CLIENT-REDIRECT-URI: https://extremenetworks.com"
                  ]

        response_code, json_response, total_time = self._api_requests(url_path, header, "GET")

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

    """
    Below Keyword are obsolete .... Will delete them Soon
    def get_access_token_curl(self, role="default"):
        username = None
        password = None
        method = "POST"

        self.utils.print_info("Role : ", role)

        if role == "default":
            username = BuiltIn().get_variable_value("${USERNAME}")
            password = BuiltIn().get_variable_value("${PASSWORD}")
        if role == "msp":
            username = BuiltIn().get_variable_value("${MSP_USERNAME}")
            password = BuiltIn().get_variable_value("${MSP_PASSWORD}")
        if role == "msp1":
            username = BuiltIn().get_variable_value("${MSP_USERNAME1}")
            password = BuiltIn().get_variable_value("${MSP_PASSWORD1}")
        if role == "devops":
            username = BuiltIn().get_variable_value("${DEVOPS_USERNAME}")
            password = BuiltIn().get_variable_value("${DEVOPS_PASSWORD}")

        grant_type = "..."
        scope = "..."

        self.utils.print_info("Username : ", username)
        self.utils.print_info("Password : ", password)

        data_binary = {"userId": username, "password": password, "grantType": grant_type, "scope": scope}
        json_data = json.dumps(data_binary)

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        rest_url = BuiltIn().get_variable_value("${REST_URL}")

        token_url = base_url + rest_url
        self.utils.print_info("OAUTH Token URL: ", token_url)

        curl_url = "curl -H \"Content-Type: application/json\" -X " + method + " --data-binary \'%s\'"\
                                                                               % json_data + " " + token_url
        json_result = self.cli.exec_shell_command(curl_url)
        self.utils.print_info("json_result : ", json_result)

        at = self.get_json_value(json_result, "access_token")

        self.utils.print_info("Access Token: ", at)

        return at

    def pycurl_request(self, url, auth_bearer, method, data="default"):
        self.utils.print_info("-------------------------------------------------------------")
        self.utils.print_info("HTTP Method: ", method)
        self.utils.print_info("-------------------------------------------------------------")
        buf = cStringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json', auth_bearer])
        c.setopt(pycurl.VERBOSE, True)

        if method == "POST":
            c.setopt(pycurl.POSTFIELDS, data)

        if method == "PUT":
            c.setopt(pycurl.CUSTOMREQUEST, " PUT ")
            c.setopt(pycurl.POSTFIELDS, data)

        if method == "DELETE":
            c.setopt(pycurl.CUSTOMREQUEST, " DELETE ")

        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.perform()

        try:
            json_response = buf.getvalue()
        except ValueError:
            json_response = "No Output"

        response_code = c.getinfo(pycurl.RESPONSE_CODE)
        total_time = c.getinfo(pycurl.TOTAL_TIME)

        c.close()

        self.utils.print_info("HTTP Status Code: ", response_code)
        self.utils.print_info("Response : ", json_response)
        self.utils.print_info("Time: ", total_time)

        return response_code, json_response, total_time

    def rest_api_get(self, url_path, role="default", result_code="default"):
        if result_code == "default":
            result_code = -1

        at = self.get_access_token_curl(role)

        base_url = BuiltIn().get_variable_value("${BASE_URL}")

        _url = base_url + url_path
        self.utils.print_info("URL: ", _url)

        auth_bearer = 'Authorization: Bearer %s' % at

        response_code, json_response, total_time = self.pycurl_request(_url, auth_bearer, "GET")

        if response_code == int(result_code):
            self.utils.print_info("Success")
            return 1
        elif response_code == 200:
            self.utils.print_info("Success")
            return json_response
        else:
            self.utils.print_info("Failed")
            return json_response

    def rest_api_post(self, url_path, post_data, return_output="default", result_code="default", role="default"):
        self.utils.print_info("Return Output :", return_output)
        self.utils.print_info("Role : ", role)

        self.utils.print_info("URL Path : ", url_path)
        self.utils.print_info("POST Data: ", post_data)

        at = self.get_access_token_curl(role)

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url1 = base_url + url_path
        auth_bearer = 'Authorization: Bearer %s' % at

        response_code, json_response, total_time = self.pycurl_request(url1, auth_bearer, "POST", post_data)

        if return_output != "default":
            return json_response

        if response_code == int(result_code):
            self.utils.print_info("Success")
            return 1
        else:
            self.utils.print_info("Failed")
            return json_response

    def rest_api_post_with_output(self, url_path, post_data, return_output="default", result_code="default",
                                  role="default"):
        self.utils.print_info("Return Output :", return_output)
        self.utils.print_info("Role : ", role)

        self.utils.print_info("URL Path : ", url_path)
        self.utils.print_info("POST Data: ", post_data)

        at = self.get_access_token_curl(role)

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url1 = base_url + url_path
        auth_bearer = 'Authorization: Bearer %s' % at

        response_code, json_response, total_time = self.pycurl_request(url1, auth_bearer, "POST", post_data)

        if return_output != "default":
            return json_response

        if response_code == int(result_code):
            self.utils.print_info("Success")
            return json_response
        else:
            self.utils.print_info("Failed")
            return json_response

    def rest_api_put(self, url_path, put_data, return_output="default", result_code="default", role="default"):
        at = self.get_access_token_curl(role)

        self.utils.print_debug("Return Output: ", return_output)
        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url1 = base_url + url_path
        auth_bearer = 'Authorization: Bearer %s' % at

        response_code, json_response, total_time = self.pycurl_request(url1, auth_bearer, "PUT", put_data)

        if response_code == int(result_code):
            self.utils.print_info("Success")
            return 1
        else:
            self.utils.print_info("Failed")
            return -1

    def rest_api_put_with_output(self, url_path, put_data, role="default", result_code="default"):
        at = self.get_access_token_curl(role)

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url1 = base_url + url_path
        auth_bearer = 'Authorization: Bearer %s' % at

        response_code, json_response, total_time = self.pycurl_request(url1, auth_bearer, "PUT", put_data)

        self.utils.print_info("HTTP Status Code: ", response_code)
        self.utils.print_info("Response : ", json_response)
        self.utils.print_info("Time: ", total_time)

        if response_code == int(result_code):
            self.utils.print_info("Success")
            return json_response
        else:
            self.utils.print_info("Failed")
            return -1

    def rest_api_delete(self, url_path, result_code="default", role="default"):

        at = self.get_access_token_curl(role)

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url1 = base_url + url_path
        auth_bearer = 'Authorization: Bearer %s' % at

        response_code, json_response, total_time = self.pycurl_request(url1, auth_bearer, "DELETE")

        if response_code == int(result_code):
            self.utils.print_info("Success")
            return 1
        else:
            self.utils.print_info("Failed")
            return -1

    def rest_api_delete_code(self, url_path, return_output="default", result_code="default", role="default"):
        self.utils.print_info("URL Path : ", url_path)
        at = self.get_access_token_curl(role)

        self.utils.print_debug("Return Output: ", return_output)

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url1 = base_url + url_path
        auth_bearer = 'Authorization: Bearer %s' % at
        self.utils.print_info("auth_token: ", auth_bearer)
        buf = cStringIO.StringIO()

        c = pycurl.Curl()
        c.setopt(pycurl.URL, url1)
        c.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json', auth_bearer])
        c.setopt(pycurl.VERBOSE, True)
        c.setopt(pycurl.CUSTOMREQUEST, " DELETE ")
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.perform()

        json_response = buf.getvalue()
        response_code = c.getinfo(pycurl.RESPONSE_CODE)
        total_time = c.getinfo(pycurl.TOTAL_TIME)
        self.utils.print_info("json_response: ", json_response)
        self.utils.print_info("HTTP Status Code: ", response_code)
        self.utils.print_info("Time: ", total_time)

        if response_code == int(result_code):
            self.utils.print_info("Success")
            return 1
        else:
            self.utils.print_info("Failed")
            return -1

    def entitle_ap_to_msp(self, ap_serial, ap_hw_number, base_url="default"):
        self.utils.print_info("Entitling AP")
        msp_name = BuiltIn().get_variable_value("${MSP_NAME}")
        post_data = '{"deviceEntitlements" : [{"contractNumber" : "4-5575081431", ' \
                    '"account" : {"accountName" : "' + msp_name + '", ' \
                                                                  '"accountCsn" : "Msp-tenantid-2UDipMmvZyeRHmLe"}, ' \
                                                                  '"entitlementId" : "2KBQQ9J", ' \
                                                                  '"entitlementService" : "00000", ' \
                                                                  '"start" : "8/24/2015", ' \
                                                                  '"end" : "8/24/2020", ' \
                                                                  '"status" : "active", ' \
                                                                  '"hardwarePartNumber" : "' + ap_hw_number + '", ' \
                                                                  '"serialNumber" : "' + ap_serial + '", ' \
                                                                  '"quantity" : 1}]}'
        url_path = "v1/update/deviceentitlements"
        at = "cfafb44d81e477026bae73444d096894"

        if base_url == "default":
            base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url1 = base_url + url_path
        method = "POST"
        curl_url = "curl -X %s -iH \"Content-Type: application/json\" -H \"Authorization: Bearer %s\" " % (method, at) \
                   + " --data-binary " + "'" + post_data + "' " + url1
        self.utils.print_info("curl_url : ", curl_url)
        
        json_result = self.cli.exec_shell_command(curl_url)
        self.utils.print_info("json_result: ", json_result)
        if "errorMessage" in json_result:
            return -1
        else:
            return 1 """
    def get_json_value(self, json_data, json_key):
        self.utils.print_debug("JSON Data: ", json_data)
        self.utils.print_debug("JSON Key: ", json_key)

        json_values = json.loads(json_data)
        self.utils.print_info(json_values)
        return json_values[json_key]

    def get_json_value_recursive(self, json_data, json_key):
        value1 = self.get_json_value(json_data, json_key)
        self.utils.print_info("Value: ", value1)

    def curl_command(self, _url):
        self.utils.print_info("Getting URL: ", _url)
        buf = None
        c = None

        try:
            buf = StringIO()
            c = pycurl.Curl()
            c.setopt(pycurl.URL, _url)
            c.setopt(pycurl.VERBOSE, True)
            c.setopt(pycurl.SSL_VERIFYPEER, 0)
            c.setopt(pycurl.SSL_VERIFYHOST, 0)
            c.setopt(pycurl.WRITEFUNCTION, buf.write)
            c.perform()

        except Exception as e:
            self.utils.print_info(e)
            self.utils.print_info("Error while URL Get")

        try:
            json_response = buf.getvalue()
        except ValueError:
            json_response = "No Output"

        response_code = c.getinfo(pycurl.RESPONSE_CODE)
        total_time = c.getinfo(pycurl.TOTAL_TIME)

        c.close()

        self.utils.print_info("HTTP Status Code: ", response_code)
        self.utils.print_info("Response : ", json_response)
        self.utils.print_info("Time: ", total_time)

        return response_code
