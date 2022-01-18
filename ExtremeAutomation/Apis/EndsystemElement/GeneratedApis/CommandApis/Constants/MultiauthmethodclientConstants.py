"""
This class outlines all the constants for the multiauthmethodclient API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(MultiauthmethodclientConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class MultiauthmethodclientConstants(ApiConstants):
    def __init__(self):
        super(MultiauthmethodclientConstants, self).__init__()
        self.CHANGE_TO_ATGAPPS_DIR = {"constant": "change_to_atgapps_dir",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.change_to_atgapps_dir}
        self.RUN_MULTIUSER_CONFIG = {"constant": "run_multiuser_config",
                                     "tags": ["COMMAND_CLI"],
                                     "link": self.link.run_multiuser_config}
        self.RUN_MULTIUSER_CONFIG_NO_LOGOFF = {"constant": "run_multiuser_config_no_logoff",
                                               "tags": ["COMMAND_CLI"],
                                               "link": self.link.run_multiuser_config_no_logoff}
        self.SWITCH_TO_ROOT = {"constant": "switch_to_root",
                               "tags": ["COMMAND_CLI"],
                               "link": self.link.switch_to_root}
