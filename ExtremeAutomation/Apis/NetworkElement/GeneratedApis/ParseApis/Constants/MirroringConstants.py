"""
This class outlines all the constants for the mirroring API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(MirroringConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class MirroringConstants(ApiConstants):
    def __init__(self):
        super(MirroringConstants, self).__init__()
        self.CHECK_PORT_MIRROR_EGRESS_EXISTS = {"constant": "check_port_mirror_egress_exists",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.check_port_mirror_egress_exists}
        self.CHECK_PORT_MIRROR_ENABLED = {"constant": "check_port_mirror_enabled",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.check_port_mirror_enabled}
        self.CHECK_PORT_MIRROR_EXISTS = {"constant": "check_port_mirror_exists",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_port_mirror_exists}
        self.CHECK_PORT_MIRROR_INGRESS_EGRESS_EXISTS = {"constant": "check_port_mirror_ingress_egress_exists",
                                                        "tags": ["PARSE_CLI"],
                                                        "link": self.link.check_port_mirror_ingress_egress_exists}
        self.CHECK_PORT_MIRROR_INGRESS_EXISTS = {"constant": "check_port_mirror_ingress_exists",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.check_port_mirror_ingress_exists}
