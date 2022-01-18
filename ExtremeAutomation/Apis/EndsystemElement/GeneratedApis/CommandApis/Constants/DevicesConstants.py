"""
This class outlines all the constants for the devices API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DevicesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DevicesConstants(ApiConstants):
    def __init__(self):
        super(DevicesConstants, self).__init__()
        self.SHOW_ALL_DEVICE_ASSETTAGS = {"constant": "show_all_device_assettags",
                                          "tags": ["COMMAND_CLI", "COMMAND_NORTHBOUND"],
                                          "link": self.link.show_all_device_assettags}
        self.SHOW_ALL_DEVICE_BASEMACS = {"constant": "show_all_device_basemacs",
                                         "tags": ["COMMAND_CLI", "COMMAND_NORTHBOUND"],
                                         "link": self.link.show_all_device_basemacs}
        self.SHOW_ALL_DEVICE_IPS = {"constant": "show_all_device_ips",
                                    "tags": ["COMMAND_CLI", "COMMAND_NORTHBOUND"],
                                    "link": self.link.show_all_device_ips}
        self.SHOW_ALL_DEVICE_NICKNAMES = {"constant": "show_all_device_nicknames",
                                          "tags": ["COMMAND_CLI", "COMMAND_NORTHBOUND"],
                                          "link": self.link.show_all_device_nicknames}
        self.SHOW_ALL_DEVICE_SYSNAMES = {"constant": "show_all_device_sysnames",
                                         "tags": ["COMMAND_CLI", "COMMAND_NORTHBOUND"],
                                         "link": self.link.show_all_device_sysnames}
        self.SHOW_DEVICE_ASSETTAG = {"constant": "show_device_assettag",
                                     "tags": ["COMMAND_CLI", "COMMAND_NORTHBOUND"],
                                     "link": self.link.show_device_assettag}
        self.SHOW_DEVICE_BASEMAC = {"constant": "show_device_basemac",
                                    "tags": ["COMMAND_CLI", "COMMAND_NORTHBOUND"],
                                    "link": self.link.show_device_basemac}
        self.SHOW_DEVICE_BOOTPROM = {"constant": "show_device_bootprom",
                                     "tags": ["COMMAND_NORTHBOUND"],
                                     "link": self.link.show_device_bootprom}
        self.SHOW_DEVICE_CHASSISID = {"constant": "show_device_chassisid",
                                      "tags": ["COMMAND_NORTHBOUND"],
                                      "link": self.link.show_device_chassisid}
        self.SHOW_DEVICE_CHASSIS_TYPE = {"constant": "show_device_chassis_type",
                                         "tags": ["COMMAND_NORTHBOUND"],
                                         "link": self.link.show_device_chassis_type}
        self.SHOW_DEVICE_DEVICEDISPLAYFAMILY = {"constant": "show_device_devicedisplayfamily",
                                                "tags": ["COMMAND_NORTHBOUND"],
                                                "link": self.link.show_device_devicedisplayfamily}
        self.SHOW_DEVICE_DEVICEID = {"constant": "show_device_deviceid",
                                     "tags": ["COMMAND_NORTHBOUND"],
                                     "link": self.link.show_device_deviceid}
        self.SHOW_DEVICE_DEVICENAME = {"constant": "show_device_devicename",
                                       "tags": ["COMMAND_NORTHBOUND"],
                                       "link": self.link.show_device_devicename}
        self.SHOW_DEVICE_FIRMWARE = {"constant": "show_device_firmware",
                                     "tags": ["COMMAND_NORTHBOUND"],
                                     "link": self.link.show_device_firmware}
        self.SHOW_DEVICE_ID = {"constant": "show_device_id",
                               "tags": ["COMMAND_NORTHBOUND"],
                               "link": self.link.show_device_id}
        self.SHOW_DEVICE_IP = {"constant": "show_device_ip",
                               "tags": ["COMMAND_NORTHBOUND"],
                               "link": self.link.show_device_ip}
        self.SHOW_DEVICE_NAME = {"constant": "show_device_name",
                                 "tags": ["COMMAND_NORTHBOUND"],
                                 "link": self.link.show_device_name}
        self.SHOW_DEVICE_NICKNAME = {"constant": "show_device_nickname",
                                     "tags": ["COMMAND_CLI", "COMMAND_NORTHBOUND"],
                                     "link": self.link.show_device_nickname}
        self.SHOW_DEVICE_SYSNAME = {"constant": "show_device_sysname",
                                    "tags": ["COMMAND_CLI", "COMMAND_NORTHBOUND"],
                                    "link": self.link.show_device_sysname}
