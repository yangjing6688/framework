"""
This class outlines all the constants for the iotuserdevices API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(IotuserdevicesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class IotuserdevicesConstants(ApiConstants):
    def __init__(self):
        super(IotuserdevicesConstants, self).__init__()
        self.DEV_ADD_MAC_DEVICES = {"constant": "dev_add_mac_devices",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.dev_add_mac_devices}
        self.DEV_CREATE_DEVICE_USING_SELF_PROVISIONER = {"constant": "dev_create_device_using_self_provisioner",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.dev_create_device_using_self_provisioner}
        self.DEV_CREATE_DEV_VALIDATE_ACC_VALIDITY = {"constant": "dev_create_dev_validate_acc_validity",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.dev_create_dev_validate_acc_validity}
        self.DEV_CREATE_USER_DEVICE = {"constant": "dev_create_user_device",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.dev_create_user_device}
        self.DEV_DE_SELECT_DEVICE_TYPE = {"constant": "dev_de_select_device_type",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.dev_de_select_device_type}
        self.DEV_NAVIGATE_DEVICE_TYPES = {"constant": "dev_navigate_device_types",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.dev_navigate_device_types}
        self.DEV_SELECT_DEVICE_TYPE = {"constant": "dev_select_device_type",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.dev_select_device_type}
        self.DEV_SEL_OT_DEVICES = {"constant": "dev_sel_ot_devices",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.dev_sel_ot_devices}
        self.DEV_USER_DEVICE_SHOULD_EXIST = {"constant": "dev_user_device_should_exist",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.dev_user_device_should_exist}
        self.DEV_VERIFY_DEFAULT_SELECTED_DEVICE_TYPES = {"constant": "dev_verify_default_selected_device_types",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.dev_verify_default_selected_device_types}
        self.DEV_VERIFY_DEVICE_ADDED = {"constant": "dev_verify_device_added",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.dev_verify_device_added}
        self.DEV_VERIFY_ONLY_SELECTED_DEVICE_TYPE_IN_DROP_DOWN = {"constant": "dev_verify_only_selected_device_type_in_drop_down",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.dev_verify_only_selected_device_type_in_drop_down}
