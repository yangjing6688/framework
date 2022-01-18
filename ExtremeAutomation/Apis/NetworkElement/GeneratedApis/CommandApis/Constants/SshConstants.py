"""
This class outlines all the constants for the ssh API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(SshConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class SshConstants(ApiConstants):
    def __init__(self):
        super(SshConstants, self).__init__()
        self.CLEAR_CLIENT_SOURCE_INTERFACE = {"constant": "clear_client_source_interface",
                                              "tags": ["COMMAND_CLI"],
                                              "link": self.link.clear_client_source_interface}
        self.DISABLE = {"constant": "disable",
                        "tags": ["COMMAND_CLI"],
                        "link": self.link.disable}
        self.DISABLE_CLIENT = {"constant": "disable_client",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.disable_client}
        self.ENABLE = {"constant": "enable",
                       "tags": ["COMMAND_CLI"],
                       "link": self.link.enable}
        self.ENABLE_CLIENT = {"constant": "enable_client",
                              "tags": ["COMMAND_CLI"],
                              "link": self.link.enable_client}
        self.SET_CLIENT_SOURCE_INTERFACE = {"constant": "set_client_source_interface",
                                            "tags": ["COMMAND_CLI"],
                                            "link": self.link.set_client_source_interface}
        self.SET_TCP_PORT = {"constant": "set_tcp_port",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.set_tcp_port}
        self.SET_VERSION = {"constant": "set_version",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.set_version}
        self.SHOW = {"constant": "show",
                     "tags": ["COMMAND_CLI"],
                     "link": self.link.show}
        self.SHOW_CLIENT_STATUS = {"constant": "show_client_status",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_client_status}
        self.SHOW_REKEY = {"constant": "show_rekey",
                           "tags": ["COMMAND_CLI"],
                           "link": self.link.show_rekey}
        self.SHOW_SERVER_STATUS = {"constant": "show_server_status",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_server_status}
        self.SHOW_SESSION = {"constant": "show_session",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.show_session}
