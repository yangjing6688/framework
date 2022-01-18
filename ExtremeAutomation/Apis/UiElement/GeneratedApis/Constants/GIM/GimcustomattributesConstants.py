"""
This class outlines all the constants for the gimcustomattributes API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(GimcustomattributesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class GimcustomattributesConstants(ApiConstants):
    def __init__(self):
        super(GimcustomattributesConstants, self).__init__()
        self.CONFIG_EMAIL_NOTIFICATION = {"constant": "config_email_notification",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.config_email_notification}
        self.CU_ADD_LOCALE = {"constant": "cu_add_locale",
                              "tags": ["COMMAND_SELENIUM"],
                              "link": self.link.cu_add_locale}
        self.CU_DEVICES_TAB_CHECK = {"constant": "cu_devices_tab_check",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.cu_devices_tab_check}
        self.CU_DE_WITH_CUSTOM_ATTRIBUTES = {"constant": "cu_de_with_custom_attributes",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.cu_de_with_custom_attributes}
        self.CU_GUEST_USERS_TAB_CHECK = {"constant": "cu_guest_users_tab_check",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.cu_guest_users_tab_check}
        self.CU_GU_INPUT_MANDATORY_VALUES = {"constant": "cu_gu_input_mandatory_values",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.cu_gu_input_mandatory_values}
        self.CU_GU_WITH_CUSTOM_ATTRIBUTES = {"constant": "cu_gu_with_custom_attributes",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.cu_gu_with_custom_attributes}
        self.CU_INPUT_CUSTOM_FIELD = {"constant": "cu_input_custom_field",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.cu_input_custom_field}
        self.CU_OT_WITH_CUSTOM_ATTRIBUTES = {"constant": "cu_ot_with_custom_attributes",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.cu_ot_with_custom_attributes}
        self.CU_SELF_SERVICE = {"constant": "cu_self_service",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.cu_self_service}
        self.CU_SELF_SERVICE_PROVISIONING = {"constant": "cu_self_service_provisioning",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.cu_self_service_provisioning}
        self.CU_TAB_CHECK = {"constant": "cu_tab_check",
                             "tags": ["COMMAND_SELENIUM"],
                             "link": self.link.cu_tab_check}
        self.CU_VALIDATE_GU_WITH_CUSTOM_ATTRIBUTES = {"constant": "cu_validate_gu_with_custom_attributes",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.cu_validate_gu_with_custom_attributes}
        self.CU_VALIDATE_SSN_IN_SERVICES_PAGE = {"constant": "cu_validate_ssn_in_services_page",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.cu_validate_ssn_in_services_page}
        self.ENTRY_SHOULD_NOT_EXIST = {"constant": "entry_should_not_exist",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.entry_should_not_exist}
        self.VERIFY_DEVICE_ADDED = {"constant": "verify_device_added",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.verify_device_added}
