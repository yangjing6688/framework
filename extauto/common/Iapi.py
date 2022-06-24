import json
import time
import subprocess
import re

from extauto.common.Utils import Utils
from robot.libraries.BuiltIn import BuiltIn
from switchAPI import Switchapi
from extauto.xiq.defs.SwitchRestConfDefinitions import SwitchRestConfDefinitions

class Iapi:
    def __init__(self):
        self.utils = Utils()
        self.switchingAPI = Switchapi()
        self.switchRestConfDefinitions = SwitchRestConfDefinitions()
        self.at = -1
        self.ct = -1


    def generate_tokens(self, username, password, path="login"):
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

        base_url = BuiltIn().get_variable_value("${IAPI_BASE_URL}")
        self.utils.print_info("Base URL: ", base_url)

        data_urlencode_raw =  "--data-urlencode 'client_id=browser' " \
                              "--data-urlencode 'client_secret=secret' " \
                              "--data-urlencode 'grant_type=password' " \
                              f"--data-urlencode 'username={username}' " \
                              f"--data-urlencode 'password={password}'"

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

    def generate_tokens_with_secret(self, username, password, secret, path="login"):
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

        base_url = BuiltIn().get_variable_value("${IAPI_BASE_URL}")
        self.utils.print_info("Base URL: ", base_url)

        data_urlencode_raw =  "--data-urlencode 'client_id=browser' " \
                              f"--data-urlencode 'client_secret={secret}' " \
                              "--data-urlencode 'grant_type=password' " \
                              f"--data-urlencode 'username={username}' " \
                              f"--data-urlencode 'password={password}'"

        curl_cmd = f"curl -v -k --location --request POST {base_url}/{path} --header 'Content-Type: application/x-www-form-urlencoded' {data_urlencode_raw}"

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
        self.utils.print_info("*************************************************")

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

    def rest_iapi_get(self, path, base_url="", access_token="default", csrf_token="default"):
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

        if access_token == -1:
            return -1

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

    def rest_iapi_post(self, path, post_data, base_url="", access_token="default", csrf_token="", convert_post_data=False):
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

        if access_token == -1:
            return -1

        url = base_url + path

        if convert_post_data:
            post_data = json.dumps(post_data)
            curl_cmd = f"curl -v -k --location --request POST '{url}' -H 'Content-Type: application/json' -H 'accept: application/json' -H 'Authorization: Bearer {access_token}' -d '" + post_data + "'"
        else:
            curl_cmd = f"curl -v -k --location --request POST '{url}' -H 'Content-Type: application/json' -H 'accept: application/json' -H 'Authorization: Bearer {access_token}' -d " + post_data

        if csrf_token == "":
            csrf_token = BuiltIn().get_variable_value("${CSRF_TOKEN}")
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

    def rest_iapi_post_with_file(self, path, file_path, base_url="", access_token="default", csrf_token=""):
        """
        - This Keyword is used to get the access token
        :param access_token: access token
        :param csrf_token: csrf-token
        :param path: API Endpoint path
        :param file_path: File path
        :param base_url: Base URL if not using the default
        :return: returns access_token
        """
        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")
        if base_url == "":
            base_url = BuiltIn().get_variable_value("${BASE_URL}")
        self.utils.print_info("Base URL: ", base_url)

        if access_token == -1:
            return -1

        url = base_url + path
        curl_cmd = f"curl --location --request POST '{url}' -H 'Content-Type: multipart/form-data' -H 'Authorization: Bearer {access_token}' --form 'files=@{file_path}' "

        if csrf_token == "":
            csrf_token = BuiltIn().get_variable_value("${CSRF_TOKEN}")
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

    def rest_api_post1(self, path, post_data, access_token = "default", return_output="default", result_code="default", role="default"):
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

    def rest_iapi_put(self, path, post_data, base_url="", access_token="default", csrf_token="", convert_post_data=False):
        """
        - RESET PUT
        :param path: API Endpoint path
        :param path: API post data
        :param path: API base url
        :param access_token: access token
        :param csrf_token: csrf-token
        :param flag to indicate if josn body need to be changed to string
        :param base_url: Base URL if not using the default
        :return: returns stdoutput
        """
        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")
        if base_url == "":
            base_url = BuiltIn().get_variable_value("${BASE_URL}")
        self.utils.print_info("Base URL: ", base_url)

        if access_token == -1:
            return -1

        url = base_url + path

        if convert_post_data:
            post_data = json.dumps(post_data)
            curl_cmd = f"curl -v -k --location --request PUT '{url}' -H 'Content-Type: application/json' -H 'accept: application/json' -H 'Authorization: Bearer {access_token}' -d '" + post_data + "'"
        else:
            curl_cmd = f"curl -v -k --location --request PUT '{url}' -H 'Content-Type: application/json' -H 'accept: application/json' -H 'Authorization: Bearer {access_token}' -d " + post_data

        if csrf_token == "":
            csrf_token = BuiltIn().get_variable_value("${CSRF_TOKEN}")
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

    def rest_iapi_delete(self, path, base_url="", access_token="default", csrf_token=""):
        """
        - REST DELETE
        :param path: API Endpoint path
        :param base_url: Base URL if not using the default
        :param access_token: access token
        :param csrf_token: csrf-token
        :return: returns stdout
        """
        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")
        if base_url == "":
            base_url = BuiltIn().get_variable_value("${BASE_URL}")
        self.utils.print_info("Base URL: ", base_url)

        if access_token == -1:
            return -1

        url = base_url + path

        curl_cmd = f"curl -v -k --location --request DELETE '{url}' -H 'Content-Type: application/json' -H 'Authorization: Bearer {access_token}'"

        if csrf_token == "":
            csrf_token = BuiltIn().get_variable_value("${CSRF_TOKEN}")
            curl_cmd = curl_cmd + " --header 'X-CSRF-Token: " + csrf_token + "'"

        self.utils.print_info("*****************************")
        self.utils.print_info("Curl Command: ", curl_cmd)

        process = subprocess.Popen(curl_cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        self.utils.print_debug("stdout: ", stdout)
        self.utils.print_debug("stderr: ", stderr)

        return stdout

    def get_current_data(self):
        self.utils.print_info("End Time: ", int(time.time()))

        return int(time.time()) * 1000

    def get_start_data(self, start_data):
        start_time = start_data - 1622444400
        self.utils.print_info("End Time: ", start_time)

        return start_time

    def update_json_value(self, json_data, key, value):
        self.utils.print_debug("JSON Data: ", json_data)
        self.utils.print_debug("Key: ", key)
        self.utils.print_debug("Value: ", value)

        json_data[key] = value

        return json_data


    def find_match_element(self, json_data, json_key_to_match, json_value_to_match):
        """
        - This Keyword is used to find the matching element from the jso raw data
        :param json_data: raw json list
        :param json_key_to_match: key str to look for
        :param json_value_to_match: value to match
        :return: the json of the matched element
        """
        #json_values = json.loads(json_data)
        for element in json_data:
            #print(element)
            current_val = self.get_json_val(element, json_key_to_match)
            if current_val == json_value_to_match:
                return element
        return None

    def find_match_element_on_multiple_keys(self, json_data, json_keys_to_match):
        """
        - This Keyword is used to find the matching element from the json raw data
        :param json_data: raw json list
        :param json_keys_to_match: Dictionary of keys and values to look match
        :return: the json of the matched element
        """
        print ('In find_match_element_on_multiple_keys')
        for element in json_data:
            #print(element)
            match_found = True
            for json_key_to_match, json_value_to_match  in json_keys_to_match.items():
                current_val = self.get_json_val(element, json_key_to_match)
                print ('Current value to match in the raw data: {}, expected value {}'.format(current_val, json_value_to_match))
                if str(current_val) != json_value_to_match:
                    match_found = False
                    print ('Current val did not match expected val')
                    break
                else:
                    print('Current val matched expected val')
            if match_found is True:
                print ('Returning matched element {}'.format(element))
                return element
        return None

    def rest_iapi_delete(self, path, delete_data, base_url="", access_token="default", csrf_token=""):
        if access_token == "default":
            access_token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")
        if base_url == "":
            base_url = BuiltIn().get_variable_value("${BASE_URL}")
        self.utils.print_info("Base URL: ", base_url)

        if access_token == -1:
            return -1

        url = base_url + path
        curl_cmd = f"curl -v --location --request DELETE '{url}?{delete_data}' -H 'Content-Type: application/json' -H 'Authorization: Bearer {access_token}'"

        if csrf_token == "":
            csrf_token = BuiltIn().get_variable_value("${CSRF_TOKEN}")
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

    def verify_port_speed_DUT_XIQ(self,xiqSpeed,dutip,mgmtportspeed,nos: str,totalports =""):
        """
        - This function is to validate all supported speed in XIQ and DUT
        :param xiqSpeed: Speed of all the Ports in XIQ
        :param dutip: DUT IP to fetch interfaces data
        :param mgmtportspeed: Applicable for EXOS if Mgmt port exists, provide speed of Mgmt port
        :param nos: exos or voss
        :param totalports: Applicable for VOSS - Total Number of ports to fetch in VOSS #VOSS-21883
        :return: if matches returns 1 else 0
        """
        speeddict = {}

        if nos.lower()== "exos":
            dutdata = self.switchingAPI.switch_restconf(nos,dutip, resourceurl= self.switchRestConfDefinitions.interfaces_Multiple[nos.lower()],method="GET")
            interface = dutdata["openconfig-interfaces:interfaces"]

        if nos.lower()== "voss":
            # since voss won't fetch all the interfaces in a single stretch, we have to do seperate poll for VOSS CR: VOSS-21883
            voss_interfaces_bunch = []
            interface = {}
            for port in range(1,int(totalports)+1):
                dutdata= self.switchingAPI.switch_restconf(nos,dutip,("{}=1%2F{}".format(self.switchRestConfDefinitions.interfaces_Single[nos.lower()], port)),method="GET")
                voss_interfaces_bunch.append(dutdata["openconfig-interfaces:interface"][0])
                time.sleep(0.5)
            dutdata= self.switchingAPI.switch_restconf(nos,dutip,"openconfig-interfaces:interfaces/interface=mgmt",method="GET")
            voss_interfaces_bunch.append(dutdata["openconfig-interfaces:interface"][0])
            interface["interface"]= voss_interfaces_bunch
            if dutdata is None:
                return 0

        effecSpeed = ""
        for each in interface["interface"]:
            try:
                effecSpeed = each["openconfig-if-ethernet:ethernet"]["state"]["effective-speed"]
                if effecSpeed in speeddict:
                    speeddict[effecSpeed] += 1
                else:
                    speeddict[effecSpeed] = 1
            except KeyError as e:
                self.utils.print_info(e)

        self.utils.print_info("speed of ports without Mgmt ports ",speeddict)
        if nos.lower()== "exos":
            if mgmtportspeed is not None:
                if int(mgmtportspeed) in speeddict:
                    speeddict[int(mgmtportspeed)] += 1
                else:
                    speeddict[int(mgmtportspeed)] = 1
            else:
                #Since Mgmt port is not available so we increase the count
                speeddict[int(0)]+=1

        self.utils.print_info("Speed of ports in DUT ",speeddict)

        dutSpeed = {"data": []}
        for key, value in speeddict.items():
            tempDict = {}
            tempDict["supportedMode"] = str(key)
            tempDict["supportedModeCount"] = int(value)
            dutSpeed["data"].append(tempDict)
        xiqSpeed = json.loads(xiqSpeed)
        match = 0
        dutSpeed_sorted = sorted(dutSpeed["data"], key=lambda i: int(i['supportedMode']))
        xiqSpeed_sorted = sorted(xiqSpeed["data"], key=lambda i: int(i['supportedMode']))
        self.utils.print_info("DUT Speed:", dutSpeed_sorted)
        self.utils.print_info("Port speed in XIQ", xiqSpeed_sorted)

        if dutSpeed_sorted == xiqSpeed_sorted:
            self.utils.print_info("Port speed of DUT and in XIQ matches")

            match=1
        else:
            print("Finding the exact failure")
            if len(dutSpeed_sorted) != len(xiqSpeed_sorted):
                self.utils.print_info("There is a mismatch between number of Active ports in XIQ and DUT")
            else:
                for i in range(len(dutSpeed_sorted)):
                    self.utils.print_info('For the supported Mode {} supported Speed to match current value: {}, expected value {}'.format(dutSpeed_sorted[i]["supportedMode"],
                                                                                                                   dutSpeed_sorted[i]["supportedModeCount"],
                                                                                                                   xiqSpeed_sorted[i]["supportedModeCount"]))
                    if dutSpeed_sorted[i] == xiqSpeed_sorted[i]:
                        self.utils.print_info("No mismatch with Supported Mode Current Value: {}, expected value {}".format(
                                                        dutSpeed_sorted[i]["supportedModeCount"],
                                                        xiqSpeed_sorted[i]["supportedModeCount"]))
                    else:
                        self.utils.print_info('There is a mismatch with supported Mode current value: {}, expected value {}'.format(
                                                        dutSpeed_sorted[i]["supportedModeCount"],
                                                        xiqSpeed_sorted[i]["supportedModeCount"]))
        return match

    def get_negotiated_speed_of_port(self,nos: str,dutip,portnumber):
        """
        Returns the current speed of a port in DUT
        :param nos: exos or voss
        :param dutip: Ip address of the DUT to fetch interface details
        :param portnumber: Exact interface port to retrive the interface details
        :return: Current Speed of Port in DUT
        """
        if nos.lower() =="exos":
            dutdata = self.switchingAPI.switch_restconf(nos, dutip, ("openconfig-interfaces:interfaces/interface=%s"%(portnumber)), method="GET")
        elif nos.lower()=="voss":
            slot_port = re.findall("(\d+)\/(\d+)",portnumber)
            slot = slot_port[0][0]
            port = slot_port[0][1]
            dutdata = self.switchingAPI.switch_restconf(nos, dutip,
                                              ("openconfig-interfaces:interfaces/interface={}%2F{}".format(slot,port)),
                                              method="GET")

        open_config_interface = self.get_json_val(dutdata,"openconfig-interfaces:interface")
        open_config_interface = open_config_interface[0]
        openconfig_ethernet = self.get_json_val(open_config_interface,"openconfig-if-ethernet:ethernet")
        speed = self.get_json_val(openconfig_ethernet,"state")
        effective_speed = self.get_json_val(speed,"effective-speed")

        return  effective_speed

    def Extract_image_name(self,data=""):
        """
        This Keyword is used to fetch the images list from Dictionary
        :param data: The output from xiq that contains images
        :return: list of images
        """
        imagesData =self.get_json_val(data,"data")
        self.utils.print_info(imagesData)
        imagename =[]
        for each_images in imagesData:
            if self.get_json_val(each_images,"scope") =="GLOBAL":
                imagename.append(each_images["imageName"])
        return imagename

    def perform_firmware_images_check(self,yamlfileinputs,variants,platform):
        """
        The main keyword to fetch image details from XIQ using IAPI
        API: 'https://g2r1.qa.xcloudiq.com/services/misc/deviceimagemetadatas/all?productType=<Product_type>&ownerId=<ownerid>&ownerIds=<ownerid>
        :param yamlfileinputs: Image details from Yaml File
        :param variants: The variant for which this validation done Eg: X440_G2_12t_10_G4
        :param platform:   summitx/onie/5520-voss/...
        :return: 1 on successful validation else 0
        """
        #construct URL and get data
        expectedImagesFromFile = yamlfileinputs[platform]
        expectedImages = []
        for key, value in expectedImagesFromFile.items():
            if value is not None:
                expectedImages.append(value)

        self.utils.print_info("The Images expected to present in XIQ are  %s \n"%(expectedImages))

        result = 1
        url = ("{}services/misc/deviceimagemetadatas/all?productType={}&ownerId={}&ownerIds={}".format(BuiltIn().get_variable_value("${IAPI_AIO_URL}"),
                                                                                                        variants,BuiltIn().get_variable_value("${OWNER_ID}"), BuiltIn().get_variable_value("${OWNER_ID}")))
        self.utils.print_info("URL to get all images = ",url)
        fetchedImages = self.rest_iapi_get(url, base_url=BuiltIn().get_variable_value("${TEST_URL}"))
        imageFromXIQ= self.Extract_image_name(fetchedImages)
        verificationResult = self.verify_firmware_images(imageFromXIQ,expectedImages,variants)

        if not verificationResult:
            result = 0

        return  result

    def verify_firmware_images(self,images_from_xiq ,image_actual,variant):
        """
        This method compares images from XIQ and Expected Images

        :param imagesfromxiq: List of images fetched from XIQ
        :param imageactual: List of Images fetched from YAML file
        :return: returns the following:
        returns 0:
            1. if there is a mismatch in total number of images between XIQ and Expected
            2. if Expected images doesn't present in XIQ
            3. if XIQ list of images contains more images than expected
        :returns 1:
            1. if the images list in XIQ and Expected are same.
        """
        returnflag = 0
        self.utils.print_info("Images present in XIQ ---- ",images_from_xiq)
        self.utils.print_info("Actual images expected are ---- ", image_actual)
        replaceSpaces = lambda x: [each.replace(' ', '').lower() for each in x]

        imagesfromxiq = replaceSpaces(images_from_xiq)
        imageExpected = replaceSpaces(image_actual)
        if len(imagesfromxiq) != len(imageExpected):
            self.utils.print_info("**** variant **** %s ***** Total number of images from XIQ and expected list are different"%(variant))
            if len(imagesfromxiq) > len(imageExpected):
                self.utils.print_error("**** variant **** %s ***** The following images are present more in XIQ %s"%(variant,set(imagesfromxiq) - set(imageExpected)))
            else:
                self.utils.print_error("**** variant **** %s ***** The expected images doesn't present in XIQ %s" % (variant,set(imageExpected) - set(imagesfromxiq)))

            return returnflag
        elif len(imageExpected) == 0 or len(imagesfromxiq) ==0:
            self.utils.print_error("**** variant **** %s ***** No images exists - Image from XIQ: %s and Expected images: %s"%(variant,imagesfromxiq,imageExpected))
            return  returnflag
        for eachimage in imagesfromxiq:
            if eachimage in imageExpected:
                self.utils.print_info("**** variant **** %s ***** Image from XIQ: %s present in expected list of Images"%(variant,eachimage))
                imageExpected.remove(eachimage)
            else:
                self.utils.print_error("**** variant **** %s ***** Image list from XIQ: %s doesn't present in expected list of images %s"%(variant,eachimage,imageExpected))
                return  returnflag

        if len(imageExpected) !=0:
            self.utils.print_error("**** variant **** %s ***** seems XIQ doesn't contain actual list of images and there are some residual %s"%(variant,imageExpected))
            return returnflag
        else:
            returnflag = 1
            self.utils.print_info("**** variant **** %s ***** Images from XIQ is same as that of Expected Images"%(variant))
            return  returnflag
