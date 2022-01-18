"""
This class outlines all the constants for the eciqdevices API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EciqdevicesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EciqdevicesConstants(ApiConstants):
    def __init__(self):
        super(EciqdevicesConstants, self).__init__()
        self.STORE_DEVICE_ID_FOR_SERIAL_NUMBER = {"constant": "store_device_id_for_serial_number",
                                                  "tags": ["PARSE_REST"],
                                                  "link": self.link.store_device_id_for_serial_number}
        self.VERIFY_DEVICE_FIRMWARE = {"constant": "verify_device_firmware",
                                       "tags": ["PARSE_REST"],
                                       "link": self.link.verify_device_firmware}
        self.VERIFY_DEVICE_IP = {"constant": "verify_device_ip",
                                 "tags": ["PARSE_REST"],
                                 "link": self.link.verify_device_ip}
        self.VERIFY_DEVICE_MAC = {"constant": "verify_device_mac",
                                  "tags": ["PARSE_REST"],
                                  "link": self.link.verify_device_mac}
        self.VERIFY_DEVICE_MODEL = {"constant": "verify_device_model",
                                    "tags": ["PARSE_REST"],
                                    "link": self.link.verify_device_model}
        self.VERIFY_DEVICE_SERIAL_NUMBER = {"constant": "verify_device_serial_number",
                                            "tags": ["PARSE_REST"],
                                            "link": self.link.verify_device_serial_number}
