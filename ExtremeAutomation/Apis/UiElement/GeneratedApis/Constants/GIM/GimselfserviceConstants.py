"""
This class outlines all the constants for the gimselfservice API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(GimselfserviceConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class GimselfserviceConstants(ApiConstants):
    def __init__(self):
        super(GimselfserviceConstants, self).__init__()
        self.SELF_PROVISIONING_SERVICE_EDIT = {"constant": "self_provisioning_service_edit",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.self_provisioning_service_edit}
        self.SELF_PROVISIONING_SERVICE_PAGE_VALIDATION = {"constant": "self_provisioning_service_page_validation",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.self_provisioning_service_page_validation}
        self.SELF_PROVISIONING_SERVICE_SHOULD_EXIST = {"constant": "self_provisioning_service_should_exist",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.self_provisioning_service_should_exist}
        self.SELF_PROVISIONING_SERVICE_SHOULD_NOT_EXIST = {"constant": "self_provisioning_service_should_not_exist",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.self_provisioning_service_should_not_exist}
        self.SELF_SERVICE_ADD = {"constant": "self_service_add",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.self_service_add}
        self.SELF_SERVICE_DELETE = {"constant": "self_service_delete",
                                    "tags": ["COMMAND_SELENIUM"],
                                    "link": self.link.self_service_delete}
        self.SELF_SERVICE_DEVICE_REGISTRATION_PAGE_VALIDATION = {"constant": "self_service_device_registration_page_validation",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.self_service_device_registration_page_validation}
        self.SELF_SERVICE_DEVICE_REG_PAGE_VAL_LOCALE = {"constant": "self_service_device_reg_page_val_locale",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.self_service_device_reg_page_val_locale}
        self.SELF_SERVICE_DEV_REG_PAGE_SELECT_LOCALE = {"constant": "self_service_dev_reg_page_select_locale",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.self_service_dev_reg_page_select_locale}
        self.SELF_SERVICE_DUPLICATE_HANDLING = {"constant": "self_service_duplicate_handling",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.self_service_duplicate_handling}
        self.SELF_SERVICE_EDIT = {"constant": "self_service_edit",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.self_service_edit}
        self.SELF_SERVICE_EDIT_AUTHENTICATOR = {"constant": "self_service_edit_authenticator",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.self_service_edit_authenticator}
        self.SELF_SERVICE_GU_REGISTRATION = {"constant": "self_service_gu_registration",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.self_service_gu_registration}
        self.SELF_SERVICE_GU_REGISTRATION_PAGE_VALIDATION = {"constant": "self_service_gu_registration_page_validation",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.self_service_gu_registration_page_validation}
        self.SELF_SERVICE_GU_REGISTRATION_SPONSOR_APPROVAL = {"constant": "self_service_gu_registration_sponsor_approval",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.self_service_gu_registration_sponsor_approval}
        self.SELF_SERVICE_GU_REG_SPONSOR_APPR_PAGE_VALIDATION = {"constant": "self_service_gu_reg_sponsor_appr_page_validation",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.self_service_gu_reg_sponsor_appr_page_validation}
        self.SELF_SERVICE_LOCALE_BODY_VAL = {"constant": "self_service_locale_body_val",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.self_service_locale_body_val}
        self.SELF_SERVICE_LOCALE_HEADER_FOOTER_VAL = {"constant": "self_service_locale_header_footer_val",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.self_service_locale_header_footer_val}
        self.SELF_SERVICE_PROVISIONERS_PAGE_VALIDATION = {"constant": "self_service_provisioners_page_validation",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.self_service_provisioners_page_validation}
        self.SELF_SERVICE_SHOULD_EXIST = {"constant": "self_service_should_exist",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.self_service_should_exist}
        self.SELF_SERVICE_SHOULD_NOT_EXIST = {"constant": "self_service_should_not_exist",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.self_service_should_not_exist}
