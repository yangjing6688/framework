import json
import subprocess

from extauto.common.Utils import Utils

from robot.libraries.BuiltIn import BuiltIn

HTTP_PROTOCOL = "HTTP/1.1"


class Xapi:
    def __init__(self):
        self.at = -1
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
        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        self.utils.print_info("Base URL: ", base_url)

        data_raw = '{"username": "' + username + '" , "password": "' + password + '"}'

        # data_raw = '{\"username\": \"xiqproductionqa+auto1-blr-tb1-va@gmail.com\", \"password\": \"Extreme@123\"}'
        # curl_cmd = "curl --location --request POST 'https://gcp1-api.qa.xcloudiq.com/login' --header 'Content-Type: application/json' --data-raw '{\"username\": \"xiqextremeqa+auto1-g7r2@gmail.com\", \"password\": \"Extreme@123\"}'"

        curl_cmd = f"curl --location --request POST {base_url}/{path} --header 'Content-Type: application/json' --data-raw '{data_raw}'"

        self.utils.print_info("Curl Command: ", curl_cmd)

        process = subprocess.Popen(curl_cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        self.utils.print_debug("stdout: ", stdout)
        self.utils.print_debug("stderr: ", stderr)

        try:
            access_token = self.get_json_value(stdout, "access_token")
        except Exception as e:
            self.utils.print_info(e)
            return access_token
        self.at = access_token
        return access_token

    def get_json_value(self, json_data, json_key, key_type='default'):
        """
         - This Keyword is used to get the  key_str value from the api response json raw data

         :param json_data:  raw json data
         :param json_key: json key
         :param key_type: index or
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

        try:
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
        except Exception as e:
            self.utils.print_info("Error in interpreting JSON data")
            return -1

    def get_json_values(self, json_data, json_key):
        """
         - This Keyword is used to get the  key_str value from the api response json raw data

         :param json_data:  raw json data
         :param json_key: json key
         :return: returns value
         """
        json_keys = json_key.split(',')
        json_val = -1

        for key1 in json_keys:
            key_type, _key = key1.split('=')
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
        :return: key_str value
        """
        encoding = 'utf-8'
        return json_data.decode(encoding)

    def rest_api_get(self, path, access_token="default"):
        """
        - This Keyword is used to get the access token

        :param access_token: access token
        :param path: API Endpoint path
        :return: returns access_token
        """
        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        self.utils.print_info("Base URL: ", base_url)

        url = base_url + path
        curl_cmd = f"curl -v --location --request GET '{url}' --header 'Authorization: Bearer {access_token}'"

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

    def rest_api_post(self, path, post_data, access_token="default", return_output="default", result_code="default",
                      role="default"):
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

        if result_code:
            if 'HTTP/1.1 202' in str(stderr):
                return 1
        return stdout

    def rest_api_post_with_file(self, path, file_path, access_token = "default", return_output="default", result_code="default", role="default"):
        self.utils.print_info("Return Output :", return_output)
        self.utils.print_info("Role : ", role)

        self.utils.print_info("URL Path : ", path)
        self.utils.print_info("File Path: ", file_path)

        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url = base_url + path

        curl_cmd = f"curl --location --request POST '{url}' -H 'Content-Type: multipart/form-data' -H 'Authorization: Bearer {access_token}' --form 'file=@{file_path}' "

        self.utils.print_info("*****************************")
        self.utils.print_info("Curl Command: ", curl_cmd.encode())

        process = subprocess.Popen(curl_cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        self.utils.print_info("stdout: ", stdout)
        self.utils.print_info("stderr: ", stderr)

        if result_code:
            if 'HTTP/1.1 202' in str(stderr):
                return 1
        return stdout

    def rest_api_post_with_no_file(self, path, access_token = "default", return_output="default", result_code="default", role="default"):
        self.utils.print_info("Return Output :", return_output)
        self.utils.print_info("Role : ", role)
        self.utils.print_info("URL Path : ", path)

        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url = base_url + path

        curl_cmd = f"curl --location --request POST '{url}' -H 'Content-Type: multipart/form-data' -H 'Authorization: Bearer {access_token}' "

        self.utils.print_info("*****************************")
        self.utils.print_info("Curl Command: ", curl_cmd.encode())

        process = subprocess.Popen(curl_cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        self.utils.print_info("stdout: ", stdout)
        self.utils.print_info("stderr: ", stderr)

        if result_code:
            if 'HTTP/1.1 202' in str(stderr):
                return 1
        return stdout

    def rest_api_put(self, path, put_data="default", access_token="default", return_output="default", result_code="default", role="default"):
        self.utils.print_info("Return Output :", return_output)
        self.utils.print_info("Role : ", role)

        self.utils.print_info("URL Path : ", path)
        self.utils.print_info("PUT Data: ", put_data)

        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url = base_url + path


        if put_data == "default":
            curl_cmd = f"curl -v --location --request PUT '{url}' -H 'Content-Type: application/json' -H 'Authorization: Bearer {access_token}' "
        else:
            curl_cmd = f"curl -v --location --request PUT '{url}' -H 'Content-Type: application/json' -H 'Authorization: Bearer {access_token}' -d " + put_data

        # curl_cmd = f"curl -v --location --request PUT '{url}' -H 'Content-Type: application/json' -H 'Authorization: Bearer {access_token}' -d "  + put_data

        self.utils.print_info("*****************************")
        self.utils.print_info("Curl Command: ", curl_cmd.encode())

        process = subprocess.Popen(curl_cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        self.utils.print_info("stdout: ", stdout)
        self.utils.print_info("stderr: ", stderr)

        if result_code == 'response_map':
            httpCode = 200
            if 'HTTP/1.1 200' in str(stderr):
                htppCode = 200
            elif 'HTTP/1.1 400' in str(stderr):
                httpCode = 400
            elif 'HTTP/1.1 500' in str(stderr):
                httpCode = 500
            return {'httpCode': httpCode, 'response': stdout}

        if result_code:
            if 'HTTP/1.1 200' in str(stderr):
                return 1
        return stdout

    def rest_api_patch(self, path, patch_data="default", access_token="default", return_output="default", result_code="default", role="default"):
        self.utils.print_info("Return Output :", return_output)
        self.utils.print_info("Role : ", role)

        self.utils.print_info("URL Path : ", path)
        self.utils.print_info("PATCH Data: ", patch_data)

        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url = base_url + path


        if patch_data == "default":
            curl_cmd = f"curl -v --location --request PATCH '{url}' -H 'Content-Type: application/json' -H 'Authorization: Bearer {access_token}' "
        else:
            curl_cmd = f"curl -v --location --request PATCH '{url}' -H 'Content-Type: application/json' -H 'Authorization: Bearer {access_token}' -d " + patch_data

        self.utils.print_info("*****************************")
        self.utils.print_info("Curl Command: ", curl_cmd.encode())

        process = subprocess.Popen(curl_cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        self.utils.print_info("stdout: ", stdout)
        self.utils.print_info("stderr: ", stderr)

        if result_code == 'response_map':
            httpCode = 200
            if 'HTTP/1.1 200' in str(stderr):
                htppCode = 200
            elif 'HTTP/1.1 400' in str(stderr):
                httpCode = 400
            elif 'HTTP/1.1 500' in str(stderr):
                httpCode = 500
            return {'httpCode': httpCode, 'response': stdout}

        if result_code:
            if 'HTTP/1.1 200' in str(stderr):
                return 1
        return stdout

    def rest_api_delete(self, path, delete_data, access_token="default", return_output="default", result_code="default",
                        role="default"):
        self.utils.print_info("Return Output :", return_output)
        self.utils.print_info("Role : ", role)

        self.utils.print_info("URL Path : ", path)
        self.utils.print_info("POST Data: ", delete_data)

        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url = base_url + path

        curl_cmd = f"curl -v --location --request DELETE '{url}/{delete_data}' -H 'Content-Type: application/json' -H 'Authorization: Bearer {access_token}'"

        self.utils.print_info("*****************************")
        self.utils.print_info("Curl Command: ", curl_cmd.encode())

        process = subprocess.Popen(curl_cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        self.utils.print_info("stdout: ", stdout)
        self.utils.print_info("stderr: ", stderr)

        return stdout

    def get_json_values_for(self, required_key, json_data, key_val):
        _key, _val = key_val.split(':')
        if isinstance(json_data, bytes):
            json_values = json.loads(json_data.decode('utf-8'))
            for _item in json_values['data']:
                if _item[_key] == _val:
                    return _item[required_key]

    def get_http_response_code(self, curl_command_std_err_message):
        index = self.find_nth_occurrence_index(curl_command_std_err_message, HTTP_PROTOCOL, 2)
        self.utils.print_info("index: ", index)
        # print(index)
        http_response_code = curl_command_std_err_message[index + len(HTTP_PROTOCOL):index + len(HTTP_PROTOCOL) + 4]

        self.utils.print_info("http_response_code: ", http_response_code)
        return http_response_code

    def find_nth_occurrence_index(self, source, search, position):
        return source.find(search, source.find(search) + position)

    # This method returns http response  code for the corresponding post api request.
    # It will be useful to validate expected http response code with actual response code.
    def rest_api_post_v1(self, path, post_data, access_token="default", return_output="default", role="default"):
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
        http_response_code = self.get_http_response_code(stderr.decode('utf-8'))
        self.utils.print_info("rest_api_post_v1->http_response_code: ", http_response_code)
        return http_response_code

    # This method returns http response code and response body for the corresponding post api request.
    # It will be useful to validate expected http response code with actual response code
    # and expected response body with actual response body.
    def rest_api_post_v2(self, path, post_data, access_token="default", return_output="default", role="default"):
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
        self.utils.print_info("stderr->decode: ", stderr.decode('utf-8'))

        http_response_code = self.get_http_response_code(stderr.decode('utf-8'))
        self.utils.print_info("rest_api_post_v2->http_response_code: ", http_response_code)
        return http_response_code, stdout.decode('utf-8')

    # This method returns http response  code for the corresponding delete api request.
    # It will be useful to validate expected http response code with actual response code.
    def rest_api_delete_v1(self, path, delete_data, access_token="default", return_output="default", role="default"):
        self.utils.print_info("Return Output :", return_output)
        self.utils.print_info("Role : ", role)

        self.utils.print_info("URL Path : ", path)
        self.utils.print_info("Delete Data: ", delete_data)

        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url = base_url + path

        curl_cmd = f"curl -v --location --request DELETE '{url}/{delete_data}' -H 'Content-Type: application/json' -H 'Authorization: Bearer {access_token}'"

        self.utils.print_info("*****************************")
        self.utils.print_info("Curl Command: ", curl_cmd.encode())

        process = subprocess.Popen(curl_cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        self.utils.print_info("stdout: ", stdout)
        self.utils.print_info("stderr: ", stderr)
        http_response_code = self.get_http_response_code(stderr.decode('utf-8'))
        self.utils.print_info("rest_api_delete_v1->http_response_code: ", http_response_code)
        return http_response_code

    # This method returns http response code and response body for the corresponding delete api request.
    # It will be useful to validate expected http response code with actual response code
    # and expected response body with actual response body.
    def rest_api_delete_v2(self, path, delete_data, access_token="default", return_output="default", role="default"):
        self.utils.print_info("Return Output :", return_output)
        self.utils.print_info("Role : ", role)

        self.utils.print_info("URL Path : ", path)
        self.utils.print_info("Delete Data: ", delete_data)

        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url = base_url + path

        curl_cmd = f"curl -v --location --request DELETE '{url}/{delete_data}' -H 'Content-Type: application/json' -H 'Authorization: Bearer {access_token}'"

        self.utils.print_info("*****************************")
        self.utils.print_info("Curl Command: ", curl_cmd.encode())

        process = subprocess.Popen(curl_cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        self.utils.print_info("stdout: ", stdout)
        self.utils.print_info("stderr: ", stderr)
        http_response_code = self.get_http_response_code(stderr.decode('utf-8'))
        self.utils.print_info("rest_api_delete_v2->http_response_code: ", http_response_code)
        return http_response_code, stdout.decode('utf-8')

    # This method returns http response code and response body for the corresponding get api request.
    # It will be useful to validate expected http response code with actual response code
    # and expected response body with actual response body.
    def rest_api_get_v1(self, path, access_token="default"):
        """
        - This Keyword is used to get the access token

        :param access_token: access token
        :param path: API Endpoint path
        :return: returns access_token
        """
        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        self.utils.print_info("Base URL: ", base_url)

        url = base_url + path
        curl_cmd = f"curl -v --location --request GET '{url}' --header 'Authorization: Bearer {access_token}'"

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
        http_response_code = self.get_http_response_code(stderr.decode('utf-8'))
        self.utils.print_info("rest_api_get_v1->http_response_code: ", http_response_code)
        return http_response_code

    # This method returns http response code and response body for the corresponding get api request.
    # It will be useful to validate expected http response code with actual response code
    # and expected response body with actual response body.
    def rest_api_get_v2(self, path, access_token="default"):
        """
        - This Keyword is used to get the access token

        :param access_token: access token
        :param path: API Endpoint path
        :return: returns access_token
        """
        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        self.utils.print_info("Base URL: ", base_url)

        url = base_url + path
        curl_cmd = f"curl -v --location --request GET '{url}' --header 'Authorization: Bearer {access_token}'"

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
        http_response_code = self.get_http_response_code(stderr.decode('utf-8'))
        self.utils.print_info("rest_api_get_v2->http_response_code: ", http_response_code)
        return http_response_code, stdout.decode('utf-8')

    def get_json_value_from_list_json(self, required_key, json_data, key_val):
        _key, _val = key_val.split(':')
        if isinstance(json_data, bytes):
            json_values = json.loads(json_data.decode('utf-8'))
            for _item in json_values:
                if _item[_key] == _val:
                    return _item[required_key]
