"""
This class outlines all the constants for the resetdevice API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(ResetdeviceConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class ResetdeviceConstants(ApiConstants):
    def __init__(self):
        super(ResetdeviceConstants, self).__init__()
        self.BYPASS_INITIAL_SETUP = {"constant": "bypass_initial_setup",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.bypass_initial_setup}
        self.LOGIN_AFTER_RESET = {"constant": "login_after_reset",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.login_after_reset}
        self.RESET_FACTORY_DEFAULT = {"constant": "reset_factory_default",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.reset_factory_default}
        self.RESET_NOW = {"constant": "reset_now",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.reset_now}
        self.RESET_SYSTEM = {"constant": "reset_system",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.reset_system}
        self.RESET_SYSTEM_TO_CONFIG = {"constant": "reset_system_to_config",
                                       "tags": ["COMMAND_CLI"],
                                       "link": self.link.reset_system_to_config}
        self.RUN_FAILOVER = {"constant": "run_failover",
                             "tags": ["COMMAND_CLI"],
                             "link": self.link.run_failover}
        self.RUN_FAILOVER_WARM = {"constant": "run_failover_warm",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.run_failover_warm}
