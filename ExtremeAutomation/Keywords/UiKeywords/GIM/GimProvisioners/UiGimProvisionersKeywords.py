from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.GIM.GimprovisionersConstants import \
    GimprovisionersConstants


class UiGimProvisionersKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGimProvisionersKeywords, self).__init__()
        self.api_const = self.constants.API_GIM_PROVISIONERS
        self.command_const = GimprovisionersConstants()

    def gim_prv_associate_ot_with_provisioner(self, element_name, prv_uname, prv_pwd, prv_fname, prv_lname,
                                              prv_email, ot_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [prv_uname] - Provisioner user name
        [prv_pwd] - Provisioner password
        [prv_fname] - Provisioner First Name
        [prv_lname] - Provisioner Last Name
        [prv_email] - Provisioner Email
        [ot_name] - OT name to associate

        Creating provisioner by associating Onboarding Template
        """
        args = {"prv_uname": prv_uname,
                "prv_pwd": prv_pwd,
                "prv_fname": prv_fname,
                "prv_lname": prv_lname,
                "prv_email": prv_email,
                "ot_name": ot_name
                }

        return self.execute_keyword(element_name, args, self.command_const.PRV_ASSOCIATE_OT_WITH_PROVISIONER, **kwargs)

    def gim_prv_should_exist(self, element_name, prv_uname, prv_fname, prv_lname, prv_email, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [prv_uname] - Created GIM Provisioner User Name
        [prv_fname] - Created in GIM Provisioner First Name
        [prv_lname] - Created in GIM Provisioner Last Name
        [prv_email] - Created in GIM Provisioner Email

        Validating GIM Provisioner user name, first name, last name and email from provisioner table
        """
        args = {"prv_uname": prv_uname,
                "prv_fname": prv_fname,
                "prv_lname": prv_lname,
                "prv_email": prv_email
                }

        return self.execute_keyword(element_name, args, self.command_const.PRV_SHOULD_EXIST, **kwargs)

    def gim_prv_verify_provisioner_signed(self, element_name, signed_in_prov, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [signed_in_prov] - Signed in GIM Provisioner USERNAME

        Validating GIM Provisioner user name after successful login
        """
        args = {"signed_in_prov": signed_in_prov,
                }

        return self.execute_keyword(element_name, args, self.command_const.PRV_VERIFY_PROVISIONER_SIGNED, **kwargs)

    def gim_xmc_enforce_all(self, element_name, xmc_un, xmc_pwd, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [xmc_un] - User name of XMC
        [xmc_pwd] - Password of XMC

        Enforcing All from XMC application before creating gust users/devices
        """
        args = {"xmc_un": xmc_un,
                "xmc_pwd": xmc_pwd
                }

        return self.execute_keyword(element_name, args, self.command_const.XMC_ENFORCE_ALL, **kwargs)

    def gim_prv_should_not_exist(self, element_name, prv_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [prv_name] - provisioner name

        Given provisioner should not exists
        """
        args = {"prv_name": prv_name
                }

        return self.execute_keyword(element_name, args, self.command_const.PRV_SHOULD_NOT_EXIST, **kwargs)

    def gim_prv_multiple_ot_association(self, element_name, prv_uname, prv_pwd, prv_fname, prv_lname, prv_email,
                                        ot_name1, ot_name2, ot_name3, ot_name4, ot_name5, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [prv_uname] - Provisioner user name
        [prv_pwd] - Provisioner password
        [prv_fname] - Provisioner First Name
        [prv_lname] - Provisioner Last Name
        [prv_email] - Provisioner Email
        [ot_name1-5] - OT name to associate

        Creating provisioner by associating Onboarding Template
        """
        args = {"prv_uname": prv_uname,
                "prv_pwd": prv_pwd,
                "prv_fname": prv_fname,
                "prv_lname": prv_lname,
                "prv_email": prv_email,
                "ot_name1": ot_name1,
                "ot_name2": ot_name2,
                "ot_name3": ot_name3,
                "ot_name4": ot_name4,
                "ot_name5": ot_name5
                }

        return self.execute_keyword(element_name, args, self.command_const.PRV_MULTIPLE_OT_ASSOCIATION, **kwargs)

    def gim_prv_label_validation_login(self, element_name, locale, u_label, pwd_label, login_label, terms_label,
                                       about_label, outlook_label, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [u_label] - Created GIM Provisioner User Name
        [login_label] - Created in GIM Provisioner First Name
        [terms_label] - Created in GIM Provisioner Last Name
        [about_label] - Created in GIM Provisioner Email
        [outlook_label] - Created in GIM Provisioner Email

        Validating GIM Provisioner user name, first name, last name and email from provisioner table
        """
        args = {"locale": locale,
                "u_label": u_label,
                "pwd_label": pwd_label,
                "login_label": login_label,
                "terms_label": terms_label,
                "about_label": about_label,
                "outlook_label": outlook_label
                }

        return self.execute_keyword(element_name, args, self.command_const.PRV_LABEL_VALIDATION_LOGIN, **kwargs)

    def gim_prv_error_invalid_login(self, element_name, error_text, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [error_text] - Error text after invalid login

        Getting error text after invalid login credentials
        """
        args = {"error_text": error_text
                }

        return self.execute_keyword(element_name, args, self.command_const.PRV_ERROR_INVALID_LOGIN, **kwargs)

    def gim_prv_log_out(self, element_name, log_out, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [log_out] - logout text

        logging out from provisioner
        """
        args = {"log_out": log_out
                }

        return self.execute_keyword(element_name, args, self.command_const.PRV_LOGOUT, **kwargs)

    def gim_prv_label_page_validation_after_login(self, element_name, signed_in_prov, member_of_onboarding_templates,
                                                  ot_name, footer_prov, application_name, guest_users_title,
                                                  devices_title, sponsor_title, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [signed_in_prov] - Signed in user name
        [member_of_onboarding_templates] - Member of OT label
        [ot_name] - Name of OT
        [footer_prov] - Footer logged in provisioner
        [application_name] - Application name
        [guest_users_title] - Title of guest user
        [devices_title] - Title of device
        [sponsor_title] - Title of sponsor


        Label validation of provisioners login page after successful login
        """
        args = {"signed_in_prov": signed_in_prov,
                "member_of_onboarding_templates": member_of_onboarding_templates,
                "ot_name": ot_name,
                "footer_prov": footer_prov,
                "application_name": application_name,
                "guest_users_title": guest_users_title,
                "devices_title": devices_title,
                "sponsor_title": sponsor_title
                }

        return self.execute_keyword(element_name, args, self.command_const.PRV_LABEL_PAGE_VALIDATION_AFTER_LOGIN,
                                    **kwargs)

    def gim_prv_label_guest_users_page_validation(self, element_name, guest_users_title, button_add, button_edit,
                                                  button_delete, button_extend_expiration, button_resend_password,
                                                  button_print, button_filter, user_name, first_name, last_name,
                                                  email, sms_address, enabled, start_time, end_time,
                                                  onboarding_template, provisioner, meeting_id, sponsor_name,
                                                  sponsor_email, sponsor_response, users_pagination_msg,
                                                  page_before_page_text, page_after_page_text,
                                                  displaying_guest_users, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [guest_users_title] - Guest Users label
        [button_add] - Add label
        [button_edit] - Edit label
        [button_delete] - Delete label
        [button_extend_expiration] - Extend Expiration label
        [button_resend_password] - Resend password label
        [button_print] - Print label
        [button_filter] - Filter label
        [user_name] - User name label from table
        [first_name] - First name label from table
        [last_name] - Last name label from table
        [email] - Email label from table
        [sms_address] - SMS address label from table
        [enabled] - Enabled label from table
        [start_time] - Start time label from table
        [end_time] - End time label from table
        [onboarding_template] - OT label from table
        [provisioner] - provisioner label from table
        [meeting_id] - Meeting id label from table
        [sponsor_name] - Sponsor name label from table
        [sponsor_email] - Sponsor email label from table
        [sponsor_response] - Sponsor response label from table
        [users_pagination_msg] - Users pagination message
        [page_before_page_text] - Page before page text
        [page_after_page_text] - Page after page text
        [displaying_guest_users] - Displaying of Guest Users

        Validating Provisioners Guest users page
        """
        args = {"guest_users_title": guest_users_title,
                "button_add": button_add,
                "button_edit": button_edit,
                "button_delete": button_delete,
                "button_extend_expiration": button_extend_expiration,
                "button_resend_password": button_resend_password,
                "button_print": button_print,
                "button_filter": button_filter,
                "user_name": user_name,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "sms_address": sms_address,
                "enabled": enabled,
                "start_time": start_time,
                "end_time": end_time,
                "onboarding_template": onboarding_template,
                "provisioner": provisioner,
                "meeting_id": meeting_id,
                "sponsor_name": sponsor_name,
                "sponsor_email": sponsor_email,
                "sponsor_response": sponsor_response,
                "users_pagination_msg": users_pagination_msg,
                "page_before_page_text": page_before_page_text,
                "page_after_page_text": page_after_page_text,
                "no_guest_to_display": displaying_guest_users
                }

        return self.execute_keyword(element_name, args, self.command_const.PRV_LABEL_GUEST_USERS_PAGE_VALIDATION,
                                    **kwargs)

    def gim_prv_label_devices_page_validation(self, element_name, device_title, button_add, button_edit,
                                              button_delete, button_extend_expiration, button_filter, mac_address,
                                              device_name, device_type_group, device_type, source, enabled,
                                              asset_type, start_time, end_time, onboarding_template, provisioner,
                                              devices_per_page, page_before_page_text, page_after_page_text,
                                              no_device_to_display, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [device_title] - Devices label
        [button_add] - Add label
        [button_edit] - Edit label
        [button_delete] - Delete label
        [button_extend_expiration] - Extend Expiration label
        [button_filter] - Filter label
        [mac_address] - MAC Address label from table
        [device_name] - Device name label from table
        [device_type_group] - Device Type Group label from table
        [device_type] - Device Type label from table
        [source] - Source label from table
        [enabled] - Enabled label from table
        [asset_type] - Asset Type label from table
        [start_time] - Start time label from table
        [end_time] - End time label from table
        [onboarding_template] - OT label from table
        [provisioner] - provisioner label from table
        [devices_per_page] - Devices pagination message
        [page_before_page_text] - Page before page text
        [page_after_page_text] - Page after page text
        [no_device_to_display] - No device to display

        Validating Provisioners Devices page
        """
        args = {"device_title": device_title,
                "button_add": button_add,
                "button_edit": button_edit,
                "button_delete": button_delete,
                "button_extend_expiration": button_extend_expiration,
                "button_filter": button_filter,
                "mac_address": mac_address,
                "device_name": device_name,
                "device_type_group": device_type_group,
                "device_type": device_type,
                "source": source,
                "enabled": enabled,
                "asset_type": asset_type,
                "start_time": start_time,
                "end_time": end_time,
                "onboarding_template": onboarding_template,
                "provisioner": provisioner,
                "devices_per_page": devices_per_page,
                "page_before_page_text": page_before_page_text,
                "page_after_page_text": page_after_page_text,
                "no_device_to_display": no_device_to_display
                }

        return self.execute_keyword(element_name, args, self.command_const.PRV_LABEL_DEVICES_PAGE_VALIDATION, **kwargs)

    def gim_prv_label_sponsors_page_validation(self, element_name, sponsor_title, button_view, button_approve,
                                               button_deny_lock, button_extend_expiration, button_send_email,
                                               button_resend_details, button_print, button_filter, user_name,
                                               first_name, last_name, sponsor_response, email, sms_address,
                                               start_time, end_time, onboarding_template, provisioner, sponsor_name,
                                               sponsor_email, users_pagination_msg, page_before_page_text,
                                               page_after_page_text, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [sponsor_title] - Sponsor's label
        [button_view] - View label
        [button_approve] - Approve label
        [button_deny_lock] - Deny/lock label
        [button_extend_expiration] - Extend Expiration label
        [button_send_email] - Send Email label
        [button_resend_details] - Resend details
        [button_print] - Print label
        [button_filter] - Filter label
        [user_name] - User name label from table
        [first_name] - First name label from table
        [last_name] - Last name label from table
        [sponsor_response] - Sponsor response label from table
        [email] - Email label from table
        [sms_address] - SMS address label from table
        [start_time] - Start time label from table
        [end_time] - End time label from table
        [onboarding_template] - OT label from table
        [provisioner] - provisioner label from table
        [sponsor_name] - Sponsor name label from table
        [sponsor_email] - Sponsor email label from table
        [users_pagination_msg] - Users pagination message
        [page_before_page_text] - Page before page text
        [page_after_page_text] - Page after page text

        Validating Provisioner's Sponsor page
        """
        args = {"sponsor_title": sponsor_title,
                "button_view": button_view,
                "button_approve": button_approve,
                "button_deny_lock": button_deny_lock,
                "button_extend_expiration": button_extend_expiration,
                "button_send_email": button_send_email,
                "button_resend_details": button_resend_details,
                "button_print": button_print,
                "button_filter": button_filter,
                "user_name": user_name,
                "first_name": first_name,
                "last_name": last_name,
                "sponsor_response": sponsor_response,
                "email": email,
                "sms_address": sms_address,
                "start_time": start_time,
                "end_time": end_time,
                "onboarding_template": onboarding_template,
                "provisioner": provisioner,
                "sponsor_name": sponsor_name,
                "sponsor_email": sponsor_email,
                "users_pagination_msg": users_pagination_msg,
                "page_before_page_text": page_before_page_text,
                "page_after_page_text": page_after_page_text
                }

        return self.execute_keyword(element_name, args, self.command_const.PRV_LABEL_SPONSORS_PAGE_VALIDATION, **kwargs)

    def gim_prv_logout_validation(self, element_name, menu_support, menu_about, logout, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [menu_support] - Menu Support from logout
        [menu_about] - Menu About from logout
        [logout] - Menu logout from logout

        Validating Logout menu fields
        """
        args = {"menu_support": menu_support,
                "menu_about": menu_about,
                "logout": logout
                }

        return self.execute_keyword(element_name, args, self.command_const.PRV_LOGOUT_VALIDATION, **kwargs)
