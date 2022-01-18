"""
This class outlines all the constants for the maps API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(MapsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class MapsConstants(ApiConstants):
    def __init__(self):
        super(MapsConstants, self).__init__()
        self.MAPS_CONFIRM_MAPS_MENU_EXISTS = {"constant": "maps_confirm_maps_menu_exists",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.maps_confirm_maps_menu_exists}
        self.MAPS_CONFIRM_MAP_EXISTS = {"constant": "maps_confirm_map_exists",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.maps_confirm_map_exists}
        self.MAPS_CREATE_MAP = {"constant": "maps_create_map",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.maps_create_map}
        self.MAPS_DELETE_MAP = {"constant": "maps_delete_map",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.maps_delete_map}
        self.MAPS_EDIT_MAP = {"constant": "maps_edit_map",
                              "tags": ["COMMAND_SELENIUM"],
                              "link": self.link.maps_edit_map}
        self.MAPS_RENAME_MAP = {"constant": "maps_rename_map",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.maps_rename_map}
        self.MAPS_SELECT_MAP = {"constant": "maps_select_map",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.maps_select_map}
        self.MAPS_WAIT_FOR_MAP_ADD = {"constant": "maps_wait_for_map_add",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.maps_wait_for_map_add}
        self.MAPS_WAIT_FOR_MAP_REMOVE = {"constant": "maps_wait_for_map_remove",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.maps_wait_for_map_remove}
