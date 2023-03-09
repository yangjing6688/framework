import json
import subprocess

from robot.libraries.BuiltIn import BuiltIn

from extauto.common.Utils import Utils


class Internal_api:
    def __init__(self):
        self.utils = Utils()

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
        csrf_token = -1
        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        self.utils.print_info("Base URL: ", base_url)

        # Commented on 1/18/23 because it is unused
        # data_raw = '{"username": "' + username + '" , "password": "' +  password  \
        #            + '" , "grant_type": "' + "password"  \
        #            + '" , "client_id": "' + "browser"  \
        #            + '" , "client_secret": "' + "secret"   \
        #            + '"}'

        data_urlencode_raw = "--data-urlencode 'client_id=browser' \
--data-urlencode 'client_secret=secret' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'username=" + username + "' \
--data-urlencode 'password=" + password + "'"



        #data_raw = '{\"username\": \"xiqproductionqa+auto1-blr-tb1-va@gmail.com\", \"password\": \"Extreme@123\"}'
        #curl_cmd = "curl --location --request POST 'https://gcp1-api.qa.xcloudiq.com/login' --header 'Content-Type: application/json' --data-raw '{\"username\": \"xiqextremeqa+auto1-g7r2@gmail.com\", \"password\": \"Extreme@123\"}'"

        curl_cmd = f"curl -k --location --request POST {base_url}/{path} --header 'Content-Type: application/x-www-form-urlencoded' {data_urlencode_raw}"

        self.utils.print_info("Curl Command: ", curl_cmd)

        process = subprocess.Popen(curl_cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        self.utils.print_debug("stdout: ", stdout)
        self.utils.print_debug("stderr: ", stderr)

        try:
            access_token = self.get_json_value(stdout,"access_token")
            csrf_token = self.get_json_value(stdout,"csrfToken")
            self.utils.print_info("CSRF Token ", csrf_token)
            self.utils.print_info("Access Token ", access_token)
        except Exception as e:
            self.utils.print_info(e)
            return [access_token, csrf_token]
        self.at = access_token
        self.ct = csrf_token
        return [access_token, csrf_token]

    def get_json_value(self, json_data, json_key, key_type='default'):
        """
         - This Keyword is used to get the  key_str value from the api response json raw data

         :param json_data:  raw json data
         :param json_key: json key
         :param index: optional index of the array
         :return: value
         """
        self.utils.print_debug("JSON Data: ", json_data)
        self.utils.print_debug("JSON Data Type: ", type(json_data))
        self.utils.print_debug("JSON Key: ", json_key)
        self.utils.print_debug("JSON Key Type: ", key_type)

        json_values = json.loads(json_data)
        self.utils.print_debug("json_values: ", json_values)

        return json_values[json_key]

    def get_json_val(self, json_data, json_key, key_type='default'):
        """
         - This Keyword is used to get the  key_str value from the api response json raw data

         :param json_data:  raw json data
         :param json_key: json key
         :param key_type: optional index of the array
         :return: value
         """
        self.utils.print_info("*************************************************")
        self.utils.print_info("JSON Data: ", json_data)
        self.utils.print_info("JSON Data Type: ", type(json_data))
        self.utils.print_info("JSON Key: ", json_key)
        self.utils.print_info("JSON Key Data Type: ", type(json_key))
        self.utils.print_info("JSON Key Type: ", key_type)

        if isinstance(json_data, bytes):
            json_values = json.loads(json_data.decode('utf-8'))
            if key_type == 'index':
                return json_values[int(json_key)]
            self.utils.print_info("JSON DATA is bytes. Returning Value: ", json_values[json_key])
            return json_values[json_key]

        elif isinstance(json_data, dict):
            self.utils.print_info("JSON DATA is dict. Returning Value: ", json_data[str(json_key)])
            return json_data[str(json_key)]

        elif isinstance(json_data, list):
            self.utils.print_info("JSON DATA is list. Returning Value: ", json_data[int(json_key)])
            return json_data[int(json_key)]

    def get_json_values(self, json_data, json_key):
        """
         - This Keyword is used to get the  key_str value from the api response json raw data

         :param json_data:  raw json data
         :param json_key: json key
         :param index: optional index of the array
         :return: value
         """
        json_keys = json_key.split(',')
        json_val = -1

        for key1 in json_keys:
            key_type, _key= key1.split('=')
            self.utils.print_debug("json_data: ", json_data)
            self.utils.print_debug("_key: ", _key)
            self.utils.print_debug("key_type: ", key_type)

            json_val = self.get_json_val(json_data, _key, key_type)
            json_data = json_val
        return json_val

    def get_json_value_as_string(self, json_data):
        """
        - This Keyword is used to get the  key_str value from the api response json raw data

        :param json_data:  raw json data from the API call to get the device ids
        :param device_mac: mac of the device to match the dict
        :param key_str:  key string to get the value
        :return: key_str value
        """
        encoding = 'utf-8'
        return json_data.decode(encoding)

    def rest_api_get(self, path, base_url="", access_token="default", csrf_token=""):
        """
        - This Keyword is used to get the access token

        :param access_token: access token
        :param csrf_token: csrf-token
        :param path: API Endpoint path
        :param base_url: Base URL if not using the default
        :return: returns access_token
        """
        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")
        if base_url == "":
            base_url = BuiltIn().get_variable_value("${BASE_URL}")
        self.utils.print_info("Base URL: ", base_url)

        url = base_url + path
        curl_cmd = f"curl -k -v --location --request GET '{url}' --header 'Authorization: Bearer {access_token}'"

        if csrf_token != "":
            curl_cmd = curl_cmd + " --header 'X-CSRF-Token: " + csrf_token + "'"

        self.utils.print_info("*****************************")
        self.utils.print_info("Curl Command: ", curl_cmd)

        process = subprocess.Popen(curl_cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        self.utils.print_debug("stdout: ", stdout)
        self.utils.print_debug("stderr: ", stderr)

        self.utils.print_info("*****************************")
        self.utils.print_info("JSON OUTPUT")
        self.utils.print_info(json.dumps(json.loads(stdout), indent=4, sort_keys=True))
        self.utils.print_info("*****************************")

        return stdout

    def rest_api_post(self, path, post_data, access_token = "default", return_output="default", result_code="default", role="default"):
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
        #lines = stderr.split("\n")
        #for line in lines:
        #    print (line)
        #self.utils.print_info("*****************************")
        #self.utils.print_info("JSON OUTPUT")
        #self.utils.print_info(json.dumps(json.loads(stdout), indent=4, sort_keys=True))
        #self.utils.print_info("*****************************")

        return stdout
