"""
This class outlines all the constants for the netsightutilities API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(NetsightutilitiesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class NetsightutilitiesConstants(ApiConstants):
    def __init__(self):
        super(NetsightutilitiesConstants, self).__init__()
        self.DEMO_POST = {"constant": "demo_post",
                          "tags": ["COMMAND_REST"],
                          "link": self.link.demo_post}
        self.DEMO_READ_LOG = {"constant": "demo_read_log",
                              "tags": ["COMMAND_REST"],
                              "link": self.link.demo_read_log}
        self.DEMO_READ_LOG_ALL = {"constant": "demo_read_log_all",
                                  "tags": ["COMMAND_REST"],
                                  "link": self.link.demo_read_log_all}
        self.INSTALL_NETSIGHT = {"constant": "install_netsight",
                                 "tags": ["COMMAND_REST", "COMMAND_XMC_REST"],
                                 "link": self.link.install_netsight}
        self.NETSIGHT_LOG_COPY = {"constant": "netsight_log_copy",
                                  "tags": ["COMMAND_REST", "COMMAND_XMC_REST"],
                                  "link": self.link.netsight_log_copy}
        self.NETSIGHT_SCRIPT_COPY = {"constant": "netsight_script_copy",
                                     "tags": ["COMMAND_REST", "COMMAND_XMC_REST"],
                                     "link": self.link.netsight_script_copy}
        self.RESTART_NETSIGHT_AND_REDEPLOY_WAR_FILE = {"constant": "restart_netsight_and_redeploy_war_file",
                                                       "tags": ["COMMAND_REST", "COMMAND_XMC_REST"],
                                                       "link": self.link.restart_netsight_and_redeploy_war_file}
