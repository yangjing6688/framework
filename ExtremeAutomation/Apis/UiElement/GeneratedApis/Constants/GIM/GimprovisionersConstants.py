"""
This class outlines all the constants for the gimprovisioners API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(GimprovisionersConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class GimprovisionersConstants(ApiConstants):
    def __init__(self):
        super(GimprovisionersConstants, self).__init__()
        self.PRV_ASSOCIATE_OT_WITH_PROVISIONER = {"constant": "prv_associate_ot_with_provisioner",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.prv_associate_ot_with_provisioner}
        self.PRV_ERROR_INVALID_LOGIN = {"constant": "prv_error_invalid_login",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.prv_error_invalid_login}
        self.PRV_LABEL_DEVICES_PAGE_VALIDATION = {"constant": "prv_label_devices_page_validation",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.prv_label_devices_page_validation}
        self.PRV_LABEL_GUEST_USERS_PAGE_VALIDATION = {"constant": "prv_label_guest_users_page_validation",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.prv_label_guest_users_page_validation}
        self.PRV_LABEL_PAGE_VALIDATION_AFTER_LOGIN = {"constant": "prv_label_page_validation_after_login",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.prv_label_page_validation_after_login}
        self.PRV_LABEL_SPONSORS_PAGE_VALIDATION = {"constant": "prv_label_sponsors_page_validation",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.prv_label_sponsors_page_validation}
        self.PRV_LABEL_VALIDATION_LOGIN = {"constant": "prv_label_validation_login",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.prv_label_validation_login}
        self.PRV_LOGOUT = {"constant": "prv_logout",
                           "tags": ["COMMAND_SELENIUM"],
                           "link": self.link.prv_logout}
        self.PRV_LOGOUT_VALIDATION = {"constant": "prv_logout_validation",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.prv_logout_validation}
        self.PRV_MULTIPLE_OT_ASSOCIATION = {"constant": "prv_multiple_ot_association",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.prv_multiple_ot_association}
        self.PRV_SHOULD_EXIST = {"constant": "prv_should_exist",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.prv_should_exist}
        self.PRV_SHOULD_NOT_EXIST = {"constant": "prv_should_not_exist",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.prv_should_not_exist}
        self.PRV_VERIFY_PROVISIONER_SIGNED = {"constant": "prv_verify_provisioner_signed",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.prv_verify_provisioner_signed}
        self.XMC_ENFORCE_ALL = {"constant": "xmc_enforce_all",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.xmc_enforce_all}
