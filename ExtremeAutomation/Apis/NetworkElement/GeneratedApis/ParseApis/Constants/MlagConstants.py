"""
This class outlines all the constants for the mlag API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(MlagConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class MlagConstants(ApiConstants):
    def __init__(self):
        super(MlagConstants, self).__init__()
        self.CHECK_PORT_IS_IN_MLAG = {"constant": "check_port_is_in_mlag",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.check_port_is_in_mlag}
        self.VERIFY_MLAG_PEER_AUTH_IS_SET = {"constant": "verify_mlag_peer_auth_is_set",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.verify_mlag_peer_auth_is_set}
        self.VERIFY_MLAG_PEER_AUTH_MD5_KEY = {"constant": "verify_mlag_peer_auth_md5_key",
                                              "tags": ["PARSE_CLI"],
                                              "link": self.link.verify_mlag_peer_auth_md5_key}
        self.VERIFY_MLAG_PEER_EXISTS = {"constant": "verify_mlag_peer_exists",
                                        "tags": ["PARSE_CLI"],
                                        "link": self.link.verify_mlag_peer_exists}
        self.VERIFY_MLAG_PEER_IPADDRESS = {"constant": "verify_mlag_peer_ipaddress",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.verify_mlag_peer_ipaddress}
        self.VERIFY_MLAG_PEER_NAME = {"constant": "verify_mlag_peer_name",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.verify_mlag_peer_name}
        self.VERIFY_MLAG_PORT_PEER_ID = {"constant": "verify_mlag_port_peer_id",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.verify_mlag_port_peer_id}
        self.VERIFY_MLAG_PORT_RELOAD_DELAY_IS_SET = {"constant": "verify_mlag_port_reload_delay_is_set",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.verify_mlag_port_reload_delay_is_set}
