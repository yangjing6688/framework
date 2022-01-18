"""
This class outlines all the constants for the gimfilemanager API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(GimfilemanagerConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class GimfilemanagerConstants(ApiConstants):
    def __init__(self):
        super(GimfilemanagerConstants, self).__init__()
        self.FM_CONTENTS_UNDER_FILE_MANAGER = {"constant": "fm_contents_under_file_manager",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.fm_contents_under_file_manager}
        self.FM_DEFAULT_SAMPLE_FILES = {"constant": "fm_default_sample_files",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.fm_default_sample_files}
        self.FM_FILE_MANAGER_AVAILABILITY = {"constant": "fm_file_manager_availability",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.fm_file_manager_availability}
        self.FM_PREF_TAB_EXIST = {"constant": "fm_pref_tab_exist",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.fm_pref_tab_exist}
