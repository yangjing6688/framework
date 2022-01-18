"""
This class outlines all the constants for the xcaclients API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(XcaclientsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class XcaclientsConstants(ApiConstants):
    def __init__(self):
        super(XcaclientsConstants, self).__init__()
        self.CLICK_CLIENT_MAC_ADDRESS_TO_OPEN_CLIENT_INFO = {"constant": "click_client_mac_address_to_open_client_info",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.click_client_mac_address_to_open_client_info}
        self.REFRESH_CLIENTS_PAGE = {"constant": "refresh_clients_page",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.refresh_clients_page}
        self.SELECT_ALL_CLIENTS = {"constant": "select_all_clients",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.select_all_clients}
        self.VERIFY_CLIENT_DOES_NOT_EXIST = {"constant": "verify_client_does_not_exist",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.verify_client_does_not_exist}
        self.VERIFY_CLIENT_EXISTS = {"constant": "verify_client_exists",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.verify_client_exists}
        self.VERIFY_CLIENT_INFORMATION = {"constant": "verify_client_information",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.verify_client_information}
