"""
This class outlines all the constants for the eciqcommonobjects API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EciqcommonobjectsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EciqcommonobjectsConstants(ApiConstants):
    def __init__(self):
        super(EciqcommonobjectsConstants, self).__init__()
        self.COMMON_OBJECTS_COLLAPSE_SECTION = {"constant": "common_objects_collapse_section",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.common_objects_collapse_section}
        self.COMMON_OBJECTS_EXPAND_SECTION = {"constant": "common_objects_expand_section",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.common_objects_expand_section}
        self.COMMON_OBJECTS_SELECT_SUB_SECTION = {"constant": "common_objects_select_sub_section",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.common_objects_select_sub_section}
