import ast
import json
import pycurl
import base64
import subprocess
import requests
from io import BytesIO
from io import StringIO

from common.Utils import Utils
from common.Cli import Cli

from robot.libraries.BuiltIn import BuiltIn

class Switchapi:
    def __init__(self, baseurl="/rest/restconf/data/", timeout=30, username="admin", password=""):

        self.baseurl= baseurl
        self.username= username
        self.password= password
        self.timeout =timeout
        self.utils = Utils()
        self.builtin = BuiltIn()
        self.headers = {'Accept': 'application/json'}
        self.authtoken = {}

    def _generate_auth_token(self,dutip):
        """
        Generates Authentication token for VOSS device
        :param dutip: IP of VOSS dut
        :return: None assigns to self.authtoken
        """
        url= "http://"+dutip+":8080/auth/token"
        self.utils.print_info("***************")
        self.utils.print_info("Generating Auth token for VOSS and IP Of DUT is {} and URL is {}".format(dutip,url))
        self.utils.print_info("***************")
        credentials= {"username":"rwa","password":"rwa"}
        response = requests.post(url, json=credentials, timeout=self.timeout)
        self.utils.print_info("The status code of Request is {}".format(response.status_code))
        try:
            response = response.json()
            self.authtoken[dutip] = response["token"]
            return response["token"]
        except ValueError:
            self.utils.print_info("No json Response")
            return None

    def switch_restconf(self,nos: str,dutip: str,resourceurl: str,method: str,data: json = ""):
        """
        A bridge between EXOS and VOSS Rest conf
        :param nos: exos or voss
        :param dutip: IP of DUT
        :param resourceurl: Resource URL to perform Rest operation
        :param method: POST/GET/PATCH/DELETE supported
        :param data: For POST and PATCH - data in json format
        :return:
        """
        url = self._get_switch_url(dutip,resourceurl,nos)
        headers = self.headers
        if nos.lower() == "voss":
            if dutip in self.authtoken:
                headers["X-Auth-Token"] = self.authtoken[dutip]
            else:
                authToken = self._generate_auth_token(dutip)

                if authToken is not None:
                    headers["X-Auth-Token"] = self.authtoken[dutip]
                else:
                    self.utils.print_info("There is a problem with fetching Auth Tokens")
                    return None
        if method.lower() =="get":
            return self._switch_api_get(url,headers)
        if method.lower() == "post":
            headers["Content-type"] = 'application/json'
            return self._switch_api_post(url, headers,data)
        if method.lower() == "patch":
            return self._switch_api_patch(url, headers,data)
        if method.lower() == "delete":
            return self._switch_api_delete(url, headers)

    def _switch_api_get(self,url,headers):
        """
        Purpose: Perform "GET" operation on EXOS/VOSS DUT
        :params: dutip - IP of DUT for rest execution
        :params: url - URL for GET request
        :return: response of GET request
        """

        self.utils.print_info("*********************")
        self.utils.print_info("URL: ",url)
        self.utils.print_info("Headers: ",headers)
        response= requests.get(url,headers = headers,auth=(self.username,self.password),timeout = self.timeout)
        self.utils.print_info("The Status Code for GET Request is {}".format(response.status_code))
        self.utils.print_info("The response obtained for GET Request is {}".format(response.json()))
        self.utils.print_info("*********************")
        response = response.json()
        return response

    def _switch_api_post(self,url,headers,data):
        """
        Purpose: Perform "POST" operation on EXOS/VOSS DUT
        :param dutip:
        :param resourceUrl:
        :param jsonData:
        :return: response if any else None
        """
        self.utils.print_info("*********************")
        self.utils.print_info("URL for POST Request: ",url)
        self.utils.print_info("Headers: ",headers)
        convertedData = json.loads(data)
        response= requests.post(url, data=json.dumps(convertedData),headers=headers,auth=(self.username,self.password),timeout = self.timeout)
        self.utils.print_info("The Status code for Post Request is {}".format(response.status_code))

        try:
            response = response.json()
            self.utils.print_info("Response of POST Request ", response)
        except ValueError:
            self.utils.print_info("No JSON Response")
            return None
        return response
    def _switch_api_delete(self,url,headers):
        """
        Purpose: Perform "DELETE" operation on EXOS/VOSS DUT
        :param dutip:
        :param resourceUrl:
        :return: response if any else None
        """
        self.utils.print_info("*********************")
        self.utils.print_info("URL for DELETE Request: ", url)
        self.utils.print_info("Headers: ", headers)
        response = requests.delete(url, headers= headers, auth=(self.username, self.password),timeout= self.timeout)
        self.utils.print_info("The Response code for Delete Request is {}".format(response.status_code))
        try:
            response = response.json()
        except ValueError:
            self.utils.print_debug("No JSON Response")
            return None
        return response

    def _switch_api_patch(self, url,headers,data):
        """
        Purpose: Perform "POST" operation on EXOS/VOSS DUT
        :param dutip:
        :param resourceUrl:
        :param jsonData:
        :return: response if any else None
        """
        self.utils.print_info("*********************")
        self.utils.print_info("URL for PATCH Request: ", url)
        self.utils.print_info("Headers: ", headers)

        convertedData = json.loads(data)
        response = requests.patch(url, data=json.dumps(convertedData), headers=headers,auth=(self.username, self.password), timeout=self.timeout)
        self.utils.print_info("The Response code for Patch Request is {}".format(response.status_code))
        try:
            response = response.json()
        except ValueError:
            self.utils.print_debug("No JSON Response")
            return None
        return response
    def _get_switch_url(self,dutip,resourceUrl,nos):
        """
        Construct Restconf URL for EXOS/VOSS
        :param dutip: IP of DUT
        :param resourceUrl: Resource url in addition to Base URL
        :param nos: exos or voss
        :return: Completely constructed URL
        """
        if nos.lower() == "exos":
            url = "http://" + dutip + self.baseurl + resourceUrl
        if nos.lower() == "voss":
            url = "http://" + dutip +":8080" +self.baseurl + resourceUrl
        return  url