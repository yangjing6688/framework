import json
import requests


from extauto.common.Utils import Utils
from extauto.common.Xapi import Xapi
from robot.libraries.BuiltIn import BuiltIn


class XAPISwitch:
    def __init__(self):
        self.at = -1
        self.utils = Utils()
        self.Xapi = Xapi()
        self.headers = {"Accept": "application/json", "Content-Type": "application/json"}
        self.cliCommandSet={}
        self.buildCLICommandSet()

    def extract_by_device_type(self, deviceList, device_type='EXOS',
            device_model='5520', stack_mac='null'):
        """
        - The keyword is used to extract a device ID of the specified type from the List
        :param deviceList:  - List of all devices
        :param device_type:  - Type of device needed
            EXOS - 5520 , 5420 EXOS devices
            VOSS - 5520 , 5420 VOSS devices
            Stack - 5520 , 5420 in homogeneous stacks ( only EXOS)
        :param device_model : - Model of the universal hardware to be searched for
        :return:   - ID of the requested device
        """
        device_type = device_type.upper()

        if device_type == 'VOSS':
            if device_model == '5520':
                searchStr = "FabricEngine_5520"
            else:
                searchStr = "FabricEngine_5420"
        else:
            if device_model == '5520':
                searchStr = "SwitchEngine_5520"
            else:
                searchStr = "SwitchEngine_5420"

        for device in deviceList:
            if device_type == 'STACK':
                if searchStr in device["product_type"] and "Stack" in device["hostname"] and stack_mac in device["mac_address"]:
                    return device["id"]
            else:
                if searchStr in device["product_type"] and "Stack" not in device["hostname"]:
                    return device["id"]
        return -1

    def extract_by_device_serial(self, deviceList, deviceSerial):
        '''

        :param deviceList: List of devices
        :param deviceSerial: Serial # to be searched for
        :return: Device ID of the device
        '''

        for device in deviceList:
            self.utils.print_info(device)
            if deviceSerial in device["serial_number"] :
                return device["id"]

        return -1

    def sendCLI_multiple_devices(self, URLpath, deviceIDList, CLIList):
        """
        :param URLpath  :   The endpoint for the XAPI Request
        :param deviceIDList:  The list of Devices for which the Request is to be sent
        :param CLIList: List of CLI commands to be sent
        :return: 1 for SUCCESS -1 for FAILURE
        """
        token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")
        self.headers["Authorization"] = "Bearer " + token

        if deviceIDList is None or CLIList is None:
            self.utils.print_error("Please enter a valid device ID along with the CLI set to be executed")
            return -1

        self.utils.print_info(deviceIDList)

        formattedList=[]
        if "," in str(deviceIDList):
            splitList = str.split(deviceIDList,',')
            print(splitList)
            formattedList = [int(i) for i in splitList]
            self.utils.print_info("New list is ", formattedList)
        else :
            formattedList.append(deviceIDList)
            self.utils.print_info("New String is ",formattedList)

        payload = json.dumps({
            "devices": {
                "ids": formattedList
            },
            "clis": [
                CLIList
            ]
        })

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url = base_url + URLpath

        self.utils.print_info("payload is " + payload)
        self.utils.print_info("URL is " + url)

        try :
            response = requests.post(url, headers=self.headers, data=payload, timeout=180)
            print(response.text)
            self.utils.print_info(response.text)
            if response is None:
                self.utils.print_error("ERROR: Not able to login into ExtremeCloudIQ - no response!")
                return -1
            if response.status_code != 200:
                self.utils.print_error(f"Error sending CLI command - HTTP Status Code: {str(response.status_code)}")
                raise TypeError(str(response.status_code))
            ResponseCode = self.ExtractResponseCode(response, deviceIDList)
            self.utils.print_info(ResponseCode)

            self.utils.print_info(response.text)
            if len(ResponseCode['Error']):
                self.utils.print_error("Devices with error in XAPI Response",ResponseCode['Error'])
                return -1
            else:
                self.utils.print_info("Devices with successful XAPI Response",ResponseCode['Success'])
                return 1
        except Exception as e:
                self.utils.print_error("Exception in URL request ", e)
                return -1

    def sendCLI_module_multiple_devices(self,deviceIDList,Module,NOS):
        '''

        :param deviceIDList: List of devices that the CLI is to be sent to
        :param Module: THe module for which the CLIs are to be sent
        :param NOS: EXOS/VOSS
        :return:  1 for SUCCESS -1 for FAILURE
        '''
    def sendCLI_device_endpoint(self, deviceID, CLIList):
        """
        :param deviceID:  The list of Devices for which the Request is to be sent
        :param CLIList: List of CLI commands to be sent
        :return: 1 for SUCCESS -1 for FAILURE
        """
        token = BuiltIn().get_variable_value("${ACCESS_TOKEN}")
        self.headers["Authorization"] = "Bearer " + token

        payload = json.dumps(
            [
                CLIList
            ]
        )

        base_url = BuiltIn().get_variable_value("${BASE_URL}")
        url = base_url + "/devices/" + str(deviceID) + "/:cli"

        response = requests.post(url, headers=self.headers, data=payload, timeout=180)

        try:
            if response is None:
                self.utils.print_error("ERROR: Not able to login into ExtremeCloudIQ - no response!")
                return -1
            if response.status_code != 200:
                self.utils.print_error("Error sending CLI command - HTTP Status Code:", str(response.status_code))
                return -1
            ResponseStatus = self.ExtractResponseCode(response, str(deviceID))

            self.utils.print_info("Response Code List is ",ResponseStatus)
            if  ResponseStatus["Error"]:
                self.utils.print_error("Error: ", str(ResponseStatus["Error"]))
                return -1
            else:
                self.utils.print_info("The following devices worked fine :",str(ResponseStatus["Success"]))
        except Exception as e:
                self.utils.print_error("Exception: ", e)
                return -1
        return 1

    def sendCLI_module_device_endpoint(self,deviceID,Module,NOS):
        '''

        :param deviceID: ID of device that the CLI is to be sent to
        :param Module: THe module for which the CLIs are to be sent
        :param NOS: EXOS/VOSS
        :return:  1 for SUCCESS -1 for FAILURE
        '''
        try:
            self.utils.print_info("Command Set",self.cliCommandSet)
            self.utils.print_info("Module",self.cliCommandSet[str.upper(Module)][str.upper(NOS)])
            #return 1
        except Exception as e:
            self.utils.print_error("Exception is :",e)
            return -1

        return self.sendCLI_device_endpoint(deviceID,self.cliCommandSet[str.upper(Module)][str.upper(NOS)])

    def ExtractResponseCode(self, response, deviceIDList):
        '''

        :param response: The URL response recieved
        :param deviceIDList: The device ID
        :return: The response code for the CLI response
        '''

        self.utils.print_info("Entering the Extract Response Code")
        respdict = json.loads(response.text)
        self.utils.print_info(respdict["device_cli_outputs"])

        if "," in str(deviceIDList):
            deviceNewList = str.split(deviceIDList,',')
        else:
            ResponseCode = {}
            ResponseCode["Error"] = []
            ResponseCode["Success"] = []
            deviceResponseCode = respdict["device_cli_outputs"][str(deviceIDList)][0]['response_code']
            if deviceResponseCode == 'CLI_RESPONSE_CODE_ERR_TIMEOUT':
                ResponseCode['Error'].append(deviceIDList)
            else:
                ResponseCode['Success'].append(deviceIDList)
            #deviceNewList = [deviceIDList]
            self.utils.print_info("The new list is :",ResponseCode)
            return ResponseCode
        ResponseCode={}
        ResponseCode["Error"]=[]
        ResponseCode["Success"]=[]
        for deviceID in deviceNewList:
            self.utils.print_info("DeviceID: ",deviceID)
            self.utils.print_info("Testing1 :", respdict["device_cli_outputs"][deviceID][0]['response_code'])
            deviceResponseCode = respdict["device_cli_outputs"][deviceID][0]['response_code']

            if deviceResponseCode == 'CLI_RESPONSE_CODE_ERR_TIMEOUT':
                ResponseCode['Error'].append(deviceID)
            else:
                ResponseCode['Success'].append(deviceID)

        return ResponseCode

    def buildCLICommandSet(self):
        '''
        Initiates the CLICommand dictionary with the list of commands for all the supported modules
        :return:None
        '''
        self.cliCommandSet['LLDP'] = {
            'EXOS' : 'show lldp ports 1\renable lldp ports 1\rshow lldp ports 1\rdisable lldp ports 1\rshow lldp ports 1\r',
            'VOSS' : 'en\rcon terminal\rinterface gig 1/1\rno auto-sense enable\rlldp status txAndrx\rshow lldp port 1/1\rno lldp status\rshow lldp port 1/1\r',
            'STACK': 'show lldp ports 1:1\renable lldp ports 1:1\rshow lldp ports 1:1\rdisable lldp ports 1:1\rshow lldp ports 1:1\r'
        }

        self.cliCommandSet['PORTDESC'] = {
            'EXOS': 'show ports 1 description\rconfigure ports 1 description-string Test123\rshow ports 1 description\r',
            'VOSS': 'show interface gigabit Ethernet name 1/1\ren\rcon terminal\rinterface gig 1/1\rno auto-sense enable\rname Test123\rshow interface gigabit Ethernet name 1/1\rno name\rshow interface gigabit Ethernet name 1/1\r',
            'STACK': 'show ports 1:1 description\rconfigure ports 1:1 description-string Test123\rshow ports 1:1 description\r'
        }

        self.cliCommandSet['PORTSPEED'] = {
            'EXOS': 'show ports 1 configuration\rconfigure ports 1 auto off speed 1000 duplex full\rshow ports 1 configuration\rconfigure ports 1 auto on\r',
            'VOSS': 'show interface gigabit Ethernet l1-config 1/1\ren\rcon terminal\rinterface gig 1/1\rno auto-sense enable\rno auto-negotiation enable\rspeed 1000\rduplex full\rshow interface gigabit Ethernet l1-config 1/1\rauto-negotiation enable\rshow interface gigabit Ethernet l1-config 1/1\r',
            'STACK': 'show ports 1:1 configuration\rconfigure ports 1:1 auto off speed 1000 duplex full\rshow ports 1:1 configuration\rconfigure ports 1 auto on\r'
        }

        self.cliCommandSet['STORMCTRL'] = {
            'EXOS' : 'show ports 1 information detail | inc Rate\rconfigure ports 1 rate-limit flood unknown-destmac 108108\rshow ports 1 information detail | inc Rate\rconfigure ports 1 rate-limit flood unknown-destmac no-limit\rshow ports 1 information detail | inc Rate\r',
            'VOSS': 'show interface gigabit Ethernet l1-config 1/1\ren\rcon terminal\rinterface gig 1/1\rno auto-sense enable\rno auto-negotiation enable\rspeed 1000\rduplex full\rshow interface gigabit Ethernet l1-config 1/1\rauto-negotiation enable\rshow interface gigabit Ethernet l1-config 1/1\r',
            'STACK': 'show ports 1:1 information detail | inc Rate\rconfigure ports 1:1 rate-limit flood unknown-destmac 108108\rshow ports 1:1 information detail | inc Rate\rconfigure ports 1:1 rate-limit flood unknown-destmac no-limit\rshow ports 1:1 information detail | inc Rate\r'
        }

        self.cliCommandSet['ELRP'] = {
            'EXOS': 'show elrp disabled-ports\rconfigure elrp-client disable-ports exclude 1\rshow elrp disabled-ports\rconfigure elrp-client disable-ports include 1\rshow elrp disabled-ports\r',
            'STACK': 'show elrp disabled-ports\rconfigure elrp-client disable-ports exclude 1:1\rshow elrp disabled-ports\rconfigure elrp-client disable-ports include 1:1\rshow elrp disabled-ports\r'
        }

        self.cliCommandSet['VLAN'] = {
            'EXOS' : 'show vlan\rcreate vlan test\rconfigure vlan test tag 100\r configure vlan test add ports 1 tagged\rshow vlan\r delete vlan test\r show vlan\r',
            'VOSS': 'show vlan basic\ren\rcon terminal\rvlan create 100 type port-mstprstp 0\rvlan members add 100 1/10 portmember\rshow vlan basic\rvlan delete 100\rshow vlan basic\r',
            'STACK': 'show vlan\rcreate vlan test\rconfigure vlan test tag 100\r configure vlan test add ports 1:1 tagged\rshow vlan\r delete vlan test\r show vlan\r'
        }

        self.cliCommandSet['STP'] = {
            'EXOS' : 'show stpd\rcreate stpd s1\rshow stpd\rcreate vlan test\rconfigure vlan test add ports 1 \rconfigure stpd s1 add vlan test \rshow stpd\rconfigure stpd delete vlan test\rdelete test\rshow vlan\rshow stpd\r',
            'VOSS' : 'show vlan basic\ren\rcon terminal\rvlan create 100 type port-mstprstp 0\rvlan members add 100 1/10 portmember\rshow vlan basic\rvlan delete 100\rshow vlan basic\r',
            'STACK': 'show stpd\rcreate stpd s1\rshow stpd\rcreate vlan test\rconfigure vlan test add ports 1:1 \rconfigure stpd s1 add vlan test\rshow stpd\rconfigure stpd delete vlan test\rdelete test\rshow vlan\rshow stpd\r'
        }

        self.cliCommandSet['POE'] = {
            'EXOS': 'show inline-power\rdisable inline-power port 1\rshow inline-power\renable inline-power port 1\rshow inline-power\r',
            'VOSS': 'show vlan basic\ren\rcon terminal\rvlan create 100 type port-mstprstp 0\rpoe poe-power-usage-threshold 30\rvlan members add 100 1/10 portmember\rshow vlan basic\rvlan delete 100\rshow vlan basic\r',
            'STACK': 'show ports 1:1 configuration\rconfigure ports 1:1 auto off speed 1000 duplex full\rshow ports 1:1 configuration\rconfigure ports 1 auto on\r'
        }



