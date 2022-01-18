"""
This class outlines all the constants for the tunnel API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(TunnelConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class TunnelConstants(ApiConstants):
    def __init__(self):
        super(TunnelConstants, self).__init__()
        self.CHECK_TUNNEL_EXISTS = {"constant": "check_tunnel_exists",
                                    "tags": ["PARSE_CLI"],
                                    "link": self.link.check_tunnel_exists}
        self.CHECK_TUNNEL_L2TB_PORT = {"constant": "check_tunnel_l2tb_port",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_tunnel_l2tb_port}
        self.CHECK_TUNNEL_MODE = {"constant": "check_tunnel_mode",
                                  "tags": ["PARSE_CLI"],
                                  "link": self.link.check_tunnel_mode}
