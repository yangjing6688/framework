"""
This class outlines all the constants for the gimadministration API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(GimadministrationConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class GimadministrationConstants(ApiConstants):
    def __init__(self):
        super(GimadministrationConstants, self).__init__()
        self.ADMIN_ADD_NAC_APPLIANCE = {"constant": "admin_add_nac_appliance",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.admin_add_nac_appliance}
        self.ADMIN_ADD_RADIUS = {"constant": "admin_add_radius",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.admin_add_radius}
        self.ADMIN_PREF_ADD_LOCALE = {"constant": "admin_pref_add_locale",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.admin_pref_add_locale}
        self.ADMIN_PREF_DEL_LOCALE = {"constant": "admin_pref_del_locale",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.admin_pref_del_locale}
        self.GIM_ACE_PAGE_VALIDATION = {"constant": "gim_ace_page_validation",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.gim_ace_page_validation}
        self.GIM_ADMINISTRATION_DEFAULT_PAGE_VALIDATION = {"constant": "gim_administration_default_page_validation",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.gim_administration_default_page_validation}
        self.GIM_ADMIN_ACCOUNT_SETTINGS_VALIDATION = {"constant": "gim_admin_account_settings_validation",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.gim_admin_account_settings_validation}
        self.GIM_ADMIN_ACE_RADIUS_PAGE_VALIDATION = {"constant": "gim_admin_ace_radius_page_validation",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.gim_admin_ace_radius_page_validation}
        self.GIM_ADMIN_ACE_TABS_PAGE_VALIDATION = {"constant": "gim_admin_ace_tabs_page_validation",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.gim_admin_ace_tabs_page_validation}
        self.GIM_ADMIN_ADD_SMS_GATEWAY = {"constant": "gim_admin_add_sms_gateway",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.gim_admin_add_sms_gateway}
        self.GIM_ADMIN_ADD_SMS_PROVIDER = {"constant": "gim_admin_add_sms_provider",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.gim_admin_add_sms_provider}
        self.GIM_ADMIN_CHANGE_SMS_DEFAULT_GATEWAY = {"constant": "gim_admin_change_sms_default_gateway",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.gim_admin_change_sms_default_gateway}
        self.GIM_ADMIN_CHANGE_VISIBILITY = {"constant": "gim_admin_change_visibility",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.gim_admin_change_visibility}
        self.GIM_ADMIN_DELETE_SMS_GATEWAY = {"constant": "gim_admin_delete_sms_gateway",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.gim_admin_delete_sms_gateway}
        self.GIM_ADMIN_EDIT_DELETE_SMS_GATEWAY = {"constant": "gim_admin_edit_delete_sms_gateway",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.gim_admin_edit_delete_sms_gateway}
        self.GIM_ADMIN_EMAIL_NOTIFICATION = {"constant": "gim_admin_email_notification",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.gim_admin_email_notification}
        self.GIM_ADMIN_EMAIL_PAGE_VALIDATION = {"constant": "gim_admin_email_page_validation",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.gim_admin_email_page_validation}
        self.GIM_ADMIN_LICENSE_VALIDATION = {"constant": "gim_admin_license_validation",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.gim_admin_license_validation}
        self.GIM_ADMIN_NOTIFICATION_PAGE_VALIDATION = {"constant": "gim_admin_notification_page_validation",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.gim_admin_notification_page_validation}
        self.GIM_ADMIN_RESTORE_DEFAULT_NAC_APPLIANCE_CONFIGURATION = {"constant": "gim_admin_restore_default_nac_appliance_configuration",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.gim_admin_restore_default_nac_appliance_configuration}
        self.GIM_ADMIN_SECONDARY_NAC_APPLIANCE_CONFIGURATION = {"constant": "gim_admin_secondary_nac_appliance_configuration",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.gim_admin_secondary_nac_appliance_configuration}
        self.GIM_ADMIN_SMS_GATEWAY_SHOULD_NOT_EXIST = {"constant": "gim_admin_sms_gateway_should_not_exist",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.gim_admin_sms_gateway_should_not_exist}
        self.GIM_ADMIN_TEST_CONNECTION_NAC_APPLIANCE_CONNECTION = {"constant": "gim_admin_test_connection_nac_appliance_connection",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.gim_admin_test_connection_nac_appliance_connection}
        self.GIM_ADMIN_TEST_EMAIL_NOTIFICATION = {"constant": "gim_admin_test_email_notification",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.gim_admin_test_email_notification}
        self.GIM_ADMIN_VALIDATING_SMS_GATEWAYS = {"constant": "gim_admin_validating_sms_gateways",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.gim_admin_validating_sms_gateways}
