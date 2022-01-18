"""
This class outlines all the constants for the devicegroups API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(DevicegroupsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class DevicegroupsConstants(ApiConstants):
    def __init__(self):
        super(DevicegroupsConstants, self).__init__()
        self.DEVICEGROUPS_CONFIRM_DEVICE_GROUP_EXISTS = {"constant": "devicegroups_confirm_device_group_exists",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.devicegroups_confirm_device_group_exists}
        self.DEVICEGROUPS_CREATE_DEVICE_GROUP = {"constant": "devicegroups_create_device_group",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.devicegroups_create_device_group}
        self.DEVICEGROUPS_DELETE_DEVICE_GROUP = {"constant": "devicegroups_delete_device_group",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.devicegroups_delete_device_group}
        self.DEVICEGROUPS_RENAME_DEVICE_GROUP = {"constant": "devicegroups_rename_device_group",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.devicegroups_rename_device_group}
        self.DEVICEGROUPS_WAIT_FOR_DEVICE_GROUP_ADD = {"constant": "devicegroups_wait_for_device_group_add",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.devicegroups_wait_for_device_group_add}
        self.DEVICEGROUPS_WAIT_FOR_DEVICE_GROUP_REMOVE = {"constant": "devicegroups_wait_for_device_group_remove",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.devicegroups_wait_for_device_group_remove}
