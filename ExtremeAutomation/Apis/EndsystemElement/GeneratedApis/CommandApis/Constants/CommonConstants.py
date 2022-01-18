"""
This class outlines all the constants for the common API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(CommonConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class CommonConstants(ApiConstants):
    def __init__(self):
        super(CommonConstants, self).__init__()
        self.GET_DIR = {"constant": "get_dir",
                        "tags": ["COMMAND_CLI"],
                        "link": self.link.get_dir}
        self.REMOVE_FILE = {"constant": "remove_file",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.remove_file}
