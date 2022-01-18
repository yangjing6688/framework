from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.GIM.GimcustomattributesConstants \
    import GimcustomattributesConstants


class UiGimCustomAttributeKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGimCustomAttributeKeywords, self).__init__()
        self.api_const = self.constants.API_GIM_CUSTOM_ATTRIBUTES
        self.command_const = GimcustomattributesConstants()

    def gim_cu_tab_check(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against

        Validates the Custom Attribute Tab existence
        """
        args = {
        }
        return self.execute_keyword(element_name, args, self.command_const.CU_TAB_CHECK, **kwargs)

    def gim_cu_guest_users_tab_check(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against

        Validates the Guest Users Tab existence under Custom Attributes
        """
        args = {}
        return self.execute_keyword(element_name, args, self.command_const.CU_GUEST_USERS_TAB_CHECK, **kwargs)

    def gim_cu_devices_tab_check(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against

        Validates the Devices Tab existence under Custom Attributes
        """
        args = {}
        return self.execute_keyword(element_name, args, self.command_const.CU_DEVICES_TAB_CHECK, **kwargs)

    def gim_cu_add_locale(self, element_name, lang, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against
        [lang]         - Determines the locale to be added out of the following:
                            a. France
                            b. Duetsch
                            c. Espanol
                            d. Italiano
                            e. Portugues
                            f. Svenska
                            g. Nederlands
                            h. Russia

        Adds the Locale under Preferences tab
        """
        args = {"lang": lang
                }
        return self.execute_keyword(element_name, args, self.command_const.CU_ADD_LOCALE, **kwargs)

    def gim_cu_ot_with_custom_attributes(self, element_name, gu_or_de, cf1_man_or_opt, cf2_man_or_opt, cf3_man_or_opt,
                                         cf4_man_or_opt, cf5_man_or_opt, cf6_man_or_opt, ot_save, **kwargs):
        """
        Keyword Arguments:
        [element_name] 		- The UI element(s) the keyword should be run against
        [gu_or_de]			- Determines the GuestUsers or Devices tab while creating OT.
        [cf1_man_or_opt]	- Determines to select Mandatory or optional radio button for Custom Field-1
        [cf2_man_or_opt]	- Determines to select Mandatory or optional radio button for Custom Field-2
        [cf3_man_or_opt]	- Determines to select Mandatory or optional radio button for Custom Field-3
        [cf4_man_or_opt]	- Determines to select Mandatory or optional radio button for Custom Field-4
        [cf5_man_or_opt]	- Determines to select Mandatory or optional radio button for Custom Field-5
        [cf6_man_or_opt]	- Determines to select Mandatory or optional radio button for Custom Field-6
        [ot_save]          - Determines whether to Save the above configuration or proceed further.

        Enables Custom Attributes and Mandatory/Optional selection while Creating OT for GuestUsers and Devices.
        """
        args = {"gu_or_de": gu_or_de,
                "cf1_man_or_opt": cf1_man_or_opt,
                "cf2_man_or_opt": cf2_man_or_opt,
                "cf3_man_or_opt": cf3_man_or_opt,
                "cf4_man_or_opt": cf4_man_or_opt,
                "cf5_man_or_opt": cf5_man_or_opt,
                "cf6_man_or_opt": cf6_man_or_opt,
                "ot_save": ot_save}
        return self.execute_keyword(element_name, args, self.command_const.CU_OT_WITH_CUSTOM_ATTRIBUTES, **kwargs)

    def gim_cu_gu_with_custom_attributes(self, element_name, prov_or_self, gu_otname, gu_fname, gu_lname, gu_uname,
                                         gu_pwd, gu_email, gu_cell_phone, **kwargs):
        """
        Keyword Arguments:
        [element_name] 	- The UI element(s) the keyword should be run against
        [prov_or_self] 	- Provisioner or Self-Service
        [gu_otname]	   	- OT name to be selected.
        [gu_fname]		- First Name of the Guest User.
        [gu_lname]		- Last Name of the Guest User.
        [gu_uname]		- User Name of the Guest User.
        [gu_pwd]		- Password of the Guest User.
        [gu_email]		- Email of the Guest User.
        [gu_cell_phone] - Cell phone number of the Guest User.

        Enter the Custom Attribute Values for Guest Users
        """
        args = {"prov_or_self": prov_or_self,
                "gu_otname": gu_otname,
                "gu_fname": gu_fname,
                "gu_lname": gu_lname,
                "gu_uname": gu_uname,
                "gu_pwd": gu_pwd,
                "gu_email": gu_email,
                "gu_cell_phone": gu_cell_phone}
        return self.execute_keyword(element_name, args, self.command_const.CU_GU_WITH_CUSTOM_ATTRIBUTES, **kwargs)

    def gim_cu_validate_gu_with_custom_attributes(self, element_name, label1_lang1, label2_lang1, label3_lang1,
                                                  label4_lang1, label5_lang1, label6_lang1, prov_or_self, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against
        [label1_lang1]	- Custom Field-1
        [label2_lang1]	- Custom Field-2
        [label3_lang1]	- Custom Field-3
        [label4_lang1]	- Custom Field-4
        [label5_lang1]	- Custom Field-5
        [label6_lang1]	- Custom Field-6
        [prov_or_self] - Provisioner or Self

        Validates the Custom Attributes in the New Guest User/ New Device Page.
        """
        args = {"label1": label1_lang1,
                "label2": label2_lang1,
                "label3": label3_lang1,
                "label4": label4_lang1,
                "label5": label5_lang1,
                "label6": label6_lang1,
                "prov_or_self": prov_or_self}
        return self.execute_keyword(element_name, args, self.command_const.CU_VALIDATE_GU_WITH_CUSTOM_ATTRIBUTES,
                                    **kwargs)

    def gim_cu_gu_input_mandatory_values(self, element_name, prov_or_self, custom1, custom2, custom3, custom4,
                                         custom5, custom6, group, error_or_no, approval, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against
        [prov_or_self]	- Provisioner or Self Service Page.
        [custom1]		- Value for Custom Attribute-1
        [custom2]		- Value for Custom Attribute-2
        [custom3]		- Value for Custom Attribute-3
        [custom4]		- Value for Custom Attribute-4
        [custom5]		- Value for Custom Attribute-5
        [custom6]  		- Value for Custom Attribute-6
        [group]			- Device or GuestUser.
        [error_or_no]   - To Deal with the negative scenarios, determining whether expecting a error msg or not
        [approval]      - Determines whether to go with sponsor approval or not

        Entering the Mandatory Values for Custom Attributes
        """
        args = {"prov_or_self": prov_or_self,
                "custom1": custom1,
                "custom2": custom2,
                "custom3": custom3,
                "custom4": custom4,
                "custom5": custom5,
                "custom6": custom6,
                "group": group,
                "error_or_no": error_or_no,
                "approval": approval}
        return self.execute_keyword(element_name, args, self.command_const.CU_GU_INPUT_MANDATORY_VALUES, **kwargs)

    def gim_cu_de_with_custom_attributes(self, element_name, prov_or_self, de_otname, de_mac, de_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] 	- The UI element(s) the keyword should be run against
        [prov_or_self]	- Provisioner or Self Service Page.
        [de_otname]		- Selects the OT.
        [de_mac]		- MAC Address of the Device.
        [de_name]		- Device Name.

        Enter the Mandatory Values for Devices
        """
        args = {"prov_or_self": prov_or_self,
                "de_otname": de_otname,
                "de_mac": de_mac,
                "de_name": de_name}
        return self.execute_keyword(element_name, args, self.command_const.CU_DE_WITH_CUSTOM_ATTRIBUTES, **kwargs)

    def gim_cu_self_service(self, element_name, gu_or_de, ss_name, ss_pwd, ss_email, ot, **kwargs):
        """
        Keyword Arguments:
        [element_name] 	- The UI element(s) the keyword should be run against
        [gu_or_de]		- Selects Guest User Or Device from Dropdown
        [ss_name]		- Self Service Name.
        [ss_pwd]		- Self Service Password.
        [ss_email]		- Email.
        [ot]			- OT Name.

        Creating a Self Service Provisioner
        """
        args = {"gu_or_de": gu_or_de,
                "ss_name": ss_name,
                "ss_pwd": ss_pwd,
                "ss_email": ss_email,
                "ot": ot}
        return self.execute_keyword(element_name, args, self.command_const.CU_SELF_SERVICE, **kwargs)

    def gim_cu_self_service_provisioning(self, element_name, ss_name, browser=None, **kwargs):
        """
        Keyword Arguments:
        [element_name] 	- The UI element(s) the keyword should be run against
        [gu_or_de]		- Selects Guest User Or Device from Dropdown
        [ss_name]		- Self Service Name.
        [browser]		- Browser name. If browser not specified, default is chrome.

        Creating a Self Service Provisioner
        """
        args = {"ss_name": ss_name,
                "browser": browser if browser is not None else "chrome"
                }
        return self.execute_keyword(element_name, args,
                                    self.command_const.CU_SELF_SERVICE_PROVISIONING, **kwargs)

    def gim_cu_validate_ssn_in_services_page(self, element_name, ss_name, browser=None, **kwargs):
        """
        Keyword Arguments:
        [element_name] 	- The UI element(s) the keyword should be run against
        [ss_name]		- Self-Service Name that needs to be validated in Self Provisioning services page.
        [browser]		- Browser in which self provisioning URL should open.

        Validates Self Service Name in Services Page and Opens the URL
        """
        args = {"ss_name": ss_name,
                "browser": browser if browser is not None else "chrome"
                }
        return self.execute_keyword(element_name, args,
                                    self.command_const.CU_VALIDATE_SSN_IN_SERVICES_PAGE, **kwargs)

    def gim_cu_config_email_notification(self, element_name, ss_email, email_server, **kwargs):
        """
        Keyword Arguments:
        [element_name] 	- The UI element(s) the keyword should be run against
        [ss_email]		- Email Address while enabling the Email Notification.
        [email_server]	- Email Server IP Address.

        Configuring the Email Notification
        """
        args = {"ss_email": ss_email,
                "email_server": email_server}
        return self.execute_keyword(element_name, args, self.command_const.CONFIG_EMAIL_NOTIFICATION, **kwargs)

    def gim_cu_select_ot_from_dropdown(self, element_name, ot_type, **kwargs):
        """
        Keyword Arguments:
        [element_name] 	- The UI element(s) the keyword should be run against
        [ot_type]		- Determines the type of OT that needs to ve created.
                               a. Guest User and Device Provisioning.
                               b. Self Service with Sponsor Approval.
                               c. Guest User and Device Provisioning using API
                               d. Guest User Provisioning using Outlook Add-in
                               e. Guest User Provisioning using Voucher

        Selects the OT from drop down
        """
        args = {"ot_type": ot_type}
        return self.execute_keyword(element_name, args, self.command_const.SELECT_OT_FROM_DROPDOWN, **kwargs)

    def gim_cu_input_custom_field(self, element_name, lang_number, gu_or_de, label1_lang1, label2_lang1, label3_lang1,
                                  label4_lang1, label5_lang1, label6_lang1, **kwargs):
        """
        Keyword Arguments:
        [element_name] 	- The UI element(s) the keyword should be run against
        [lang_number]	- Language number in GuestUsers/Devices tab under Custom Attributes
        [gu_or_de]		- Selecting GuestUsers or Devices Tab under Custom Attributes.
        [label1_lang1]	- Custom Field-1 value.
        [label2_lang1]	- Custom Field-2 value.
        [label3_lang1]	- Custom Field-3 value.
        [label4_lang1]	- Custom Field-4 value.
        [label5_lang1]	- Custom Field-5 value.
        [label6_lang1]	- Custom Field-6 value.

        Enters Custom field Keys for all different Languages
        """
        args = {"lang_number": lang_number,
                "gu_or_de": gu_or_de,
                "label1": label1_lang1,
                "label2": label2_lang1,
                "label3": label3_lang1,
                "label4": label4_lang1,
                "label5": label5_lang1,
                "label6": label6_lang1}
        return self.execute_keyword(element_name, args, self.command_const.CU_INPUT_CUSTOM_FIELD, **kwargs)

    def gim_cu_entry_should_not_exist(self, element_name, gu_or_de, gu_uname, **kwargs):
        """
        Keyword Arguments:
        [element_name] 	- The UI element(s) the keyword should be run against
        [gu_or_de]		- To select GuestUsers or Devices tab
        [gu_uname]		- Username or MAC for Guest User and Device Respectively.

        Check whether the Guest User and Device Entry doesn't exists in the table.
        """
        args = {"gu_or_de": gu_or_de,
                "gu_uname": gu_uname}
        return self.execute_keyword(element_name, args, self.command_const.ENTRY_SHOULD_NOT_EXIST, **kwargs)

    def gim_cu_verify_devices_added(self, element_name, device_mac, **kwargs):
        """
        Keyword Arguments:
        [element_name]  - The UI element(s) the keyword should be run against
        [device_mac]	- MAC address of the Device.

        Checks the device mac existence
        """
        args = {"device_mac": device_mac
                }
        return self.execute_keyword(element_name, args, self.command_const.VERIFY_DEVICE_ADDED, **kwargs)
