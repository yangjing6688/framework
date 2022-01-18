from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.GIM.GimselfserviceConstants import GimselfserviceConstants


class UiGimSelfServiceKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGimSelfServiceKeywords, self).__init__()
        self.api_const = self.constants.API_GIM_SELF_SERVICE
        self.command_const = GimselfserviceConstants()

    def gim_self_service_add(self, element_name, serv_name, serv_type, pwd, conf_pwd, serv_email, ot_name, terms,
                             intervals, redirection, url_text, dev_check, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [serv_name] - Name of the Self service
        [serv_type] - Type of the Self service
        [pwd] - Password
        [conf_pwd] - Confirm Password
        [serv_email] - Self service email
        [ot_name] - Name of the Onboarding Template
        [terms] - Terms
        [intervals] - Intervals
        [redirection] - Redirection
        [url_text] - URL text
        [dev_check] - Checkbox for device user auth

        Creating Self service Provisioners
        """
        args = {"serv_name": serv_name,
                "serv_type": serv_type,
                "pwd": pwd,
                "conf_pwd": conf_pwd,
                "serv_email": serv_email,
                "ot_name": ot_name,
                "terms": terms,
                "intervals": intervals,
                "redirection": redirection,
                "url_text": url_text,
                "dev_check": dev_check
                }

        return self.execute_keyword(element_name, args, self.command_const.SELF_SERVICE_ADD, **kwargs)

    def gim_self_service_delete(self, element_name, serv_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [serv_name] - Name of the Self service

        Deleting Self service Provisioners
        """
        args = {"serv_name": serv_name
                }

        return self.execute_keyword(element_name, args, self.command_const.SELF_SERVICE_DELETE, **kwargs)

    def gim_self_service_edit(self, element_name, serv_name, edit_email, terms, intervals, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [serv_name] - Name of the Self service
        [edit_email] - Self service email
        [terms] - Terms
        [intervals] - Intervals

        Editing Self service Provisioners
        """
        args = {"serv_name": serv_name,
                "edit_email": edit_email,
                "terms": terms,
                "intervals": intervals
                }
        return self.execute_keyword(element_name, args, self.command_const.SELF_SERVICE_EDIT, **kwargs)

    def gim_self_service_provisioners_page_validation(self, element_name, serv_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_name] - OT Name from table

        Default validation of OT table before and after selecting OT
        """
        args = {"serv_name": serv_name
                }

        return self.execute_keyword(element_name, args, self.command_const.SELF_SERVICE_PROVISIONERS_PAGE_VALIDATION,
                                    **kwargs)

    def gim_self_service_should_exist(self, element_name, serv_name, serv_email, serv_type, ot_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [serv_name] - Name of the Self service
        [serv_email] - Self service email
        [serv_type] - Type of the Self service
        [ot_name] - Name of the Onboarding Template

        Created Self service for provisioner should exists from the table
        """
        args = {"serv_name": serv_name,
                "serv_email": serv_email,
                "serv_type": serv_type,
                "ot_name": ot_name
                }

        return self.execute_keyword(element_name, args, self.command_const.SELF_SERVICE_SHOULD_EXIST, **kwargs)

    def gim_self_service_should_not_exist(self, element_name, serv_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [serv_name] - Name of the Self service

        Created Self service for provisioner should not exists from the table
        """
        args = {"serv_name": serv_name
                }
        return self.execute_keyword(element_name, args, self.command_const.SELF_SERVICE_SHOULD_NOT_EXIST, **kwargs)

    def gim_self_provisioning_service_page_validation(self, element_name, serv_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [serv_name] - Name of the Self service

        Created Self service for provisioner should not exists from the table
        """
        args = {"serv_name": serv_name
                }
        return self.execute_keyword(element_name, args, self.command_const.SELF_PROVISIONING_SERVICE_PAGE_VALIDATION,
                                    **kwargs)

    def gim_self_provisioning_service_should_exist(self, element_name, serv_name, serv_type, serv_status, serv_url,
                                                   copy_url, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [serv_name] - Name of the Self service
        [serv_type] - Type of the Self-Service Guest User or Device
        [serv_status] - Self-Service status
        [serv_url] - Self-Service URL
        [copy_url_gu] - COPY URL

        Created Self Provisioner should exists from the table
        """
        args = {"serv_name": serv_name,
                "serv_type": serv_type,
                "serv_status": serv_status,
                "serv_url": serv_url,
                "copy_url": copy_url
                }
        return self.execute_keyword(element_name, args, self.command_const.SELF_PROVISIONING_SERVICE_SHOULD_EXIST,
                                    **kwargs)

    def gim_self_provisioning_service_should_not_exist(self, element_name, serv_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [serv_name] - Name of the Self service

        Created Self provisioner should not exists from the table
        """
        args = {"serv_name": serv_name
                }
        return self.execute_keyword(element_name, args, self.command_const.SELF_PROVISIONING_SERVICE_SHOULD_NOT_EXIST,
                                    **kwargs)

    def gim_self_service_duplicate_handling(self, element_name, error_text, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [error_text] - Error text on duplicate self-service dialog box

        Created Self service for provisioner should not exists from the table
        """
        args = {"error_text": error_text
                }
        return self.execute_keyword(element_name, args, self.command_const.SELF_SERVICE_DUPLICATE_HANDLING, **kwargs)

    def gim_self_service_gu_registration_page_validation(self, element_name, first_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [error_text] - Error text on duplicate self-service dialog box

        This keyword used to validate Self Service Guest User page
        """
        args = {"first_name": first_name
                }
        return self.execute_keyword(element_name, args,
                                    self.command_const.SELF_SERVICE_GU_REGISTRATION_PAGE_VALIDATION, **kwargs)

    def gim_self_service_device_registration_page_validation(self, element_name, macaddress, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [macAddress] - Mac Address of a device

        This keyword used to validate Self Service Guest User page
        """
        args = {"macAddress": macaddress
                }
        return self.execute_keyword(element_name, args,
                                    self.command_const.SELF_SERVICE_DEVICE_REGISTRATION_PAGE_VALIDATION, **kwargs)

    def gim_self_service_gu_reg_sponsor_appr_page_validation(self, element_name, first_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [first_name] - First name of register guest user

        This keyword used to validate Self Service Guest User page
        """
        args = {"first_name": first_name
                }
        return self.execute_keyword(element_name, args,
                                    self.command_const.SELF_SERVICE_GU_REG_SPONSOR_APPR_PAGE_VALIDATION, **kwargs)

    def gim_self_service_gu_registration(self, element_name, gu_fname, gu_lname, gu_uname, gu_pwd, gu_email,
                                         gu_cell_phone, user_cell_phone_carrier, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_fname] - Guest User First name
        [gu_lname] - Guest User Last name
        [gu_uname] - Guest User  name
        [gu_pwd] - Guest User Password
        [gu_email] - Guest User Email
        [gu_cell_phone] - Guest User Mobile number
        [userCellPhoneCarrier] - Guest User SMS Carrier

        This keyword is used for registering Guest user with different SMS Carriers in Data Driven Model
        """
        args = {"gu_fname": gu_fname,
                "gu_lname": gu_lname,
                "gu_uname": gu_uname,
                "gu_pwd": gu_pwd,
                "gu_email": gu_email,
                "gu_cell_phone": gu_cell_phone,
                "user_cell_phone_carrier": user_cell_phone_carrier
                }
        return self.execute_keyword(element_name, args, self.command_const.SELF_SERVICE_GU_REGISTRATION, **kwargs)

    def gim_self_service_device_registration(self, element_name, error_text, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [error_text] - Error text on duplicate self-service dialog box

        This keyword used to validate Self Service Guest User page
        """
        args = {"error_text": error_text
                }
        return self.execute_keyword(element_name, args, self.command_const.SELF_SERVICE_DEVICE_REGISTRATION, **kwargs)

    def gim_self_service_gu_registration_sponsor_approval(self, element_name, gu_fname, gu_lname, gu_uname, gu_pwd,
                                                          gu_email, gu_cell_phone, user_cell_phone_carrier,
                                                          sponsor_type, spon_fname, spon_lname, spon_email,
                                                          spon_email_domain, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [error_text] - Error text on duplicate self-service dialog box
        [gu_fname] - Gu First Name
        [gu_lname] - Gu Last Name
        [gu_uname] - Gu User Name
        [gu_pwd] - Gu Password
        [gu_email] - Gu Email
        [gu_cell_phone] - Gu Cell Phone
        [user_cell_phone_carrier] - Phone Carrier Name
        [sponsor_type] - Sponsor Type
        [spon_fname] - Sponsor First Name
        [spon_lname] - Sponsor Last Name
        [spon_email] - Sponsor Email
        [spon_email_domain] - Sponsor Email Domain

        This keyword used to validate Self Service Guest User page
        """
        args = {"gu_fname": gu_fname,
                "gu_lname": gu_lname,
                "gu_uname": gu_uname,
                "gu_pwd": gu_pwd,
                "gu_email": gu_email,
                "gu_cell_phone": gu_cell_phone,
                "user_cell_phone_carrier": user_cell_phone_carrier,
                "sponsor_type": sponsor_type,
                "spon_fname": spon_fname,
                "spon_lname": spon_lname,
                "spon_email": spon_email,
                "spon_email_domain": spon_email_domain
                }
        return self.execute_keyword(element_name, args,
                                    self.command_const.SELF_SERVICE_GU_REGISTRATION_SPONSOR_APPROVAL, **kwargs)

    def gim_self_provisioning_service_edit(self, element_name, serv_name, edit_email, terms, intervals, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [serv_name] - Name of the Self provisioning service
        [edit_email] - Self service email
        [terms] - Terms of use
        [intervals] - Auto refresh Intervals

        This keyword used to edit Self service Provisioner
        """
        args = {"serv_name": serv_name,
                "edit_email": edit_email,
                "terms": terms,
                "intervals": intervals
                }
        return self.execute_keyword(element_name, args, self.command_const.SELF_PROVISIONING_SERVICE_EDIT, **kwargs)

    def gim_self_service_edit_authenticator(self, element_name, serv_name, true_false, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [serv_name] - Name of the Self service

        Editing Self service Provisioners for authenticator
        """
        args = {"serv_name": serv_name,
                "true_false": true_false
                }

        return self.execute_keyword(element_name, args, self.command_const.SELF_SERVICE_EDIT_AUTHENTICATOR, **kwargs)

    def gim_self_service_locale_header_footer_val(self, element_name, toolbar_text, menu_support, menu_about,
                                                  submit_button, clear_button, submit_tool_tip, clear_tool_tip,
                                                  **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [toolbar_text] - Toolbar displaying text
        [menu_support] - Toolbar contains menu 'support'
        [menu_about] - Toolbar contains menu 'about'
        [submit_button] - Footer contains 'submit' button text
        [clear_button] - Footer contains 'clear' button text
        [submit_tool_tip] - Footer contains 'submit' button tool tip
        [clear_tool_tip] - Footer contains 'clear' button tool tip

        This keyword used to validate header, toolbar and footer of Self Service device registering page
        """
        args = {"toolbar_text": toolbar_text,
                "menu_support": menu_support,
                "menu_about": menu_about,
                "submit_button": submit_button,
                "clear_button": clear_button,
                "submit_tool_tip": submit_tool_tip,
                "clear_tool_tip": clear_tool_tip
                }
        return self.execute_keyword(element_name, args, self.command_const.SELF_SERVICE_LOCALE_HEADER_FOOTER_VAL,
                                    **kwargs)

    def gim_self_service_locale_body_val(self, element_name, register_device, with_authenticator, prv_un, prv_pwd,
                                         device_mac_ad, device_type_grp, device_type, device_terms, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [register_device] - Error text on duplicate self-service dialog box
        [with_authenticator] - with authenticator, if neeeded provide 'yes_authenticator'
        [prv_un] - Authenticator user name
        [prv_pwd] - Authenticator password
        [device_mac_ad] - Devices MAC Address
        [device_type_grp] - Device Family group
        [device_type] - Device Type
        [device_terms] - Label of Terms

        This keyword used to validate body text of Self Service device registering page
        """
        args = {"register_device": register_device,
                "with_authenticator": with_authenticator,
                "prv_un": prv_un,
                "prv_pwd": prv_pwd,
                "device_mac_ad": device_mac_ad,
                "device_type_grp": device_type_grp,
                "device_type": device_type,
                "device_terms": device_terms
                }
        return self.execute_keyword(element_name, args, self.command_const.SELF_SERVICE_LOCALE_BODY_VAL, **kwargs)

    def gim_self_service_device_reg_page_val_locale(self, element_name, locale_reg_device, locale_mac_ad,
                                                    locale_type_grp, locale_type, locale_terms, locale_submit,
                                                    locale_clear, menu_support, menu_about, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [locale_reg_device] - Label 'Register a New Device'
        [locale_mac_ad] - Label device 'MAC Address'
        [locale_type_grp] - Label 'Device Type Group'
        [locale_type] - Label 'Device Type'
        [locale_terms] - Label 'Terms of Use:'
        [locale_submit] - Label 'Submit' button
        [locale_clear] - Label 'Clear' button
        [menu_support] - Label 'menu support'
        [menu_about] = Label 'menu about

        This keyword used to validate text while register a new device from self provisioning page
        """
        args = {"locale_reg_device": locale_reg_device,
                "locale_mac_ad": locale_mac_ad,
                "locale_type_grp": locale_type_grp,
                "locale_type": locale_type,
                "locale_terms": locale_terms,
                "locale_submit": locale_submit,
                "locale_clear": locale_clear,
                "menu_support": menu_support,
                "menu_about": menu_about
                }
        return self.execute_keyword(element_name, args, self.command_const.SELF_SERVICE_DEVICE_REG_PAGE_VAL_LOCALE,
                                    **kwargs)

    def gim_self_service_dev_reg_page_select_locale(self, element_name, locale, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [locale] - Local name

        This keyword used to click on the selected locale while register a new device from self provisioning page
        """
        args = {"locale": locale
                }
        return self.execute_keyword(element_name, args, self.command_const.SELF_SERVICE_DEV_REG_PAGE_SELECT_LOCALE,
                                    **kwargs)
