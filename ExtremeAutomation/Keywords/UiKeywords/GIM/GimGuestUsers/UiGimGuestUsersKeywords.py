from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.GIM.GimguestusersConstants \
    import GimguestusersConstants


class UiGimGuestUsersKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGimGuestUsersKeywords, self).__init__()
        self.api_const = self.constants.API_GIM_GUEST_USERS
        self.command_const = GimguestusersConstants()

    def gim_gu_create_guest_user(self, element_name, gu_otname, gu_fname, gu_lname, gu_uname, gu_pwd, gu_email,
                                 gu_cellphone, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_otname] - OT name
        [gu_fname] - Guest user's first name
        [gu_lname] - Guest user's last name
        [gu_uname] - Guest user's user name
        [gu_pwd] -  Guest user's password
        [gu_email] - Guest user's email id
        [gu_cellphone] - Guest user's cell phone

        Creating guest user from provisioner
        """
        args = {"gu_otname": gu_otname,
                "gu_fname": gu_fname,
                "gu_lname": gu_lname,
                "gu_uname": gu_uname,
                "gu_pwd": gu_pwd,
                "gu_email": gu_email,
                "gu_cellPhone": gu_cellphone
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_CREATE_GUEST_USER, **kwargs)

    def gim_gu_guest_user_should_exist(self, element_name, gu_uname, gu_fname, gu_lname, gu_email, gu_otname, gu_prv,
                                       **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_uname] - Guest user's user name
        [gu_fname] - Guest user's first name
        [gu_lname] - Guest user's last name
        [gu_email] - Guest user's email id
        [gu_otname] - OT name
        [gu_prv] - Provisioner name

        Validating guest user's user name, first, last name, email, OT name and provisioner from guest users table
        """
        args = {"gu_uname": gu_uname,
                "gu_fname": gu_fname,
                "gu_lname": gu_lname,
                "gu_email": gu_email,
                "gu_otname": gu_otname,
                "gu_prv": gu_prv
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_GUEST_USER_SHOULD_EXIST, **kwargs)

    def gim_gu_click_nav_bar(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Clicks on Guest users from left navigation bar
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.GU_CLICK_NAV_BAR, **kwargs)

    def gim_gu_table_start_end_time(self, element_name, gu_uname, gu_str_time, gu_end_time, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_uname] - Guest user's user name
        [gu_str_time] - Guest user's start time
        [gu_end_time] - Guest user's end time

        Validating guest user's specific start and end time from the table
        """
        args = {"gu_uname": gu_uname,
                "gu_str_time": gu_str_time,
                "gu_end_time": gu_end_time
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_TABLE_START_END_TIME, **kwargs)

    def gim_gu_table_sms(self, element_name, gu_uname, gu_sms, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_uname] - Guest user's user name
        [gu_sms] - Guest user's sms

        Validating guest user's sms from the table
        """
        args = {"gu_uname": gu_uname,
                "gu_sms": gu_sms
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_TABLE_SMS, **kwargs)

    def gim_gu_table_meeting_id(self, element_name, gu_uname, gu_meeting_id, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_uname] - Guest user's user name
        [gu_meeting_id] - Guest user's meeting id

        Validating guest user's meeting id from the table
        """
        args = {"gu_uname": gu_uname,
                "gu_meeting_id": gu_meeting_id
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_TABLE_MEETING_ID, **kwargs)

    def gim_gu_table_sponsor_name(self, element_name, gu_uname, gu_sponsor_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_uname] - Guest user's user name
        [gu_sponsor_name] - Guest user's sponsor name

        Validating guest user's sponsor name from the table
        """
        args = {"gu_uname": gu_uname,
                "gu_sponsor_name": gu_sponsor_name
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_TABLE_SPONSOR_NAME, **kwargs)

    def gim_gu_table_sponsor_email(self, element_name, gu_uname, gu_sponsor_email, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_uname] - Guest user's user name
        [gu_sponsor_email] - Guest user's sponsor email

        Validating guest user's sponsor email from the table
        """
        args = {"gu_uname": gu_uname,
                "gu_sponsor_email": gu_sponsor_email
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_TABLE_SPONSOR_EMAIL, **kwargs)

    def gim_gu_table_sponsor_response(self, element_name, gu_uname, gu_sponsor_response, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_uname] - Guest user's user name
        [gu_sponsor_response] - Guest user's sponsor's response

        Validating guest user's sponsors response from the table
        """
        args = {"gu_uname": gu_uname,
                "gu_sponsor_response": gu_sponsor_response
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_TABLE_SPONSOR_RESPONSE, **kwargs)

    def gim_gu_duration_val_add_gu(self, element_name, gu_otname, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_otname] - Guest user's OT name

        Validating guest user's duration
        """
        args = {"gu_otname": gu_otname
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_DURATION_VAL_ADD_GU, **kwargs)

    def gim_gu_account_on_val_add_gu(self, element_name, gu_otname, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_otname] - Guest user's OT name

        Validating guest user's account validity
        """
        args = {"gu_otname": gu_otname
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_ACCOUNT_ON_VAL_ADD_GU, **kwargs)

    def gim_gu_add(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Clicks on Add button from Guest users table
        """
        args = {
        }

        return self.execute_keyword(element_name, args, self.command_const.GU_ADD, **kwargs)

    def gim_gu_edit(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Clicks on Edit button from Guest users table
        """
        args = {
        }

        return self.execute_keyword(element_name, args, self.command_const.GU_EDIT, **kwargs)

    def gim_gu_delete(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Clicks on Delete button from Guest users table
        """
        args = {
        }

        return self.execute_keyword(element_name, args, self.command_const.GU_DELETE, **kwargs)

    def gim_gu_ext_exp(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Clicks on Extend Expiration button from Guest users table
        """
        args = {
        }

        return self.execute_keyword(element_name, args, self.command_const.GU_EXT_EXP, **kwargs)

    def gim_gu_load(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Clicks on Load button from Guest users table
        """
        args = {
        }

        return self.execute_keyword(element_name, args, self.command_const.GU_LOAD, **kwargs)

    def gim_gu_resend_pwd(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Clicks on Resend Password button from Guest users table
        """
        args = {
        }

        return self.execute_keyword(element_name, args, self.command_const.GU_RESEND_PWD, **kwargs)

    def gim_gu_show_filters(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Clicks on Show Filters button from Guest users table
        """
        args = {
        }

        return self.execute_keyword(element_name, args, self.command_const.GU_SHOW_FILTERS, **kwargs)

    def gim_gu_add_success_msg(self, element_name, gu_otname, gu_fname, gu_lname, gu_uname, gu_pwd, gu_email,
                               gu_cellphone, success_msg, un_pwd, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_otname] - OT name
        [gu_fname] - Guest user's first name
        [gu_lname] - Guest user's last name
        [gu_uname] - Guest user's user name
        [gu_pwd] -  Guest user's password
        [gu_email] - Guest user's email id
        [gu_cellphone] - Guest user's cell phone
        [success_msg] - Success message
        [un_pwd] - Username and Password

        Validating success message while creating guest user
        """
        args = {"gu_otname": gu_otname,
                "gu_fname": gu_fname,
                "gu_lname": gu_lname,
                "gu_uname": gu_uname,
                "gu_pwd": gu_pwd,
                "gu_email": gu_email,
                "gu_cellPhone": gu_cellphone,
                "success_msg": success_msg,
                "un_pwd": un_pwd
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_ADD_SUCCESS_MSG, **kwargs)

    def gim_gu_user_name_should_not_exist(self, element_name, gu_username, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_username] - Guest user username

        Validating guest user should  not exists from the table
        """
        args = {"gu_username": gu_username
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_USER_NAME_SHOULD_NOT_EXIST, **kwargs)

    def gim_gu_validation_username_field(self, element_name, gu_otname, enabled_or_disabled, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_otname] - Guest user username
        [enabled_or_disabled] - expected form enabled or disabled

        Validating whether username filed is enabled or in disabled form while creating guest user
        """
        args = {"gu_otname": gu_otname,
                "enabled_or_disabled": enabled_or_disabled
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_VALIDATION_USERNAME_FIELD, **kwargs)

    def gim_gu_create_gu_username_field(self, element_name, gu_otname, gu_fname, gu_lname, gu_uname, gu_pwd, gu_email,
                                        gu_cellphone, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_otname] - OT name
        [gu_fname] - Guest user's first name
        [gu_lname] - Guest user's last name
        [gu_uname] - Guest user's user name
        [gu_pwd] -  Guest user's password
        [gu_email] - Guest user's email id
        [gu_cellphone] - Guest user's cell phone

        Creating guest user with random generated username
        """
        args = {"gu_otname": gu_otname,
                "gu_fname": gu_fname,
                "gu_lname": gu_lname,
                "gu_uname": gu_uname,
                "gu_pwd": gu_pwd,
                "gu_email": gu_email,
                "gu_cellPhone": gu_cellphone
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_CREATE_GU_USERNAME_FIELD, **kwargs)

    def gim_gu_create_gu_validate_un_pwd(self, element_name, gu_otname, gu_fname, gu_lname, email, cellphone,
                                         username_type, gu_uname, un_length, un_case_type, prefix_suffix,
                                         random_static, number, static, pwd_type, gu_pwd, confirm_pwd,
                                         pwd_range_or_number, pwd_length, pwd_case_type, gim_url, admin_un,
                                         admin_pwd, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_otname] - OT name
        [gu_fname] - Guest user's first name
        [gu_lname] - Guest user's last name
        [gu_uname] - Guest user's user name
        [email] - Email Address of Guest
        [cellPhone] - Mobile number of Guest
        [username_type] - Type of Username
                            a. Guest Defined
                            b. Generate username with:
                                    i.Random Generated Username
                            c. FirstNameLastName
                                    i. No Prefix Suffix
                                    ii. Add Prefix
                                         a. Random Numbers
                                         b. Static
                                    iii. Add Suffix
                                         a. Random Numbers
                                         b. Static
                            d. FirstInitialLastName
                                    i. No Prefix Suffix
                                    ii. Add Prefix
                                         a. Random Numbers
                                         b. Static
                                    iii. Add Suffix
                                         a. Random Numbers
                                         b. Static
        [gu_uname] - Username of the guest user
        [un_length] - Length of the username
        [un_case_type] - Case Type of Username for Random Generated
                            a. Lower
                            b. Upper
                            c. Number
        [prefix_suffix] - Selects any one of the following options
                            a. No Prefix Suffix
                            b. Add Prefix
                            c. Add Suffix
        [random_static] - Selects either of following options:
                            a. Random Numbers
                            b. Static
        [number] - Inputs the number of Random numbers
        [static] - Inputs the Static prefix/Suffix
        [pwd_type] - Type of Password
                        a. Guest Defined
                        b. Random
                        c. Use Username as Password
                        d. Use Static Password
        [gu_pwd] -  Guest user's password
        [confirm_pwd] - confirms the password for the second time
        [pwd_range_or_number] - Specifies whether the password length is defined within a Range or a specified number
        [pwd_length] - Length of the password. This can either be a Range (8-10) or a number (15)
        [pwd_case_type] - Case Type of Password
                            a. Lower
                            b. Upper
                            c. Number
                            d. Special Characters
        [gim_url] - Url of GIM admin
        [admin_un] - GIM admin username
        [admin_pwd] - GIM admin password

        Creating Guest User,Validating Username & Password,Validating the created guest user in Provisioner and admin.
        """
        args = {"gu_otname": gu_otname,
                "gu_fname": gu_fname,
                "gu_lname": gu_lname,
                "email": email,
                "cellPhone": cellphone,
                "username_type": username_type,
                "gu_uname": gu_uname,
                "un_length": un_length,
                "un_case_type": un_case_type,
                "prefix_suffix": prefix_suffix,
                "random_static": random_static,
                "number": number,
                "static": static,
                "pwd_type": pwd_type,
                "gu_pwd": gu_pwd,
                "confirm_pwd": confirm_pwd,
                "pwd_range_or_number": pwd_range_or_number,
                "pwd_length": pwd_length,
                "pwd_case_type": pwd_case_type,
                "gim_url": gim_url,
                "admin_un": admin_un,
                "admin_pwd": admin_pwd
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_CREATE_GU_VALIDATE_UN_PWD, **kwargs)

    def gim_gu_create_gu_validate_acc_validity(self, element_name, gu_otname, gu_fname, gu_lname, gu_uname, pwd,
                                               gu_email, cellphone, time, change_no_change, change_time,
                                               error_no_error, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [
        Validates the Password length and case type.
        """
        args = {"gu_otname": gu_otname,
                "gu_fname": gu_fname,
                "gu_lname": gu_lname,
                "gu_uname": gu_uname,
                "pwd": pwd,
                "gu_email": gu_email,
                "cellphone": cellphone,
                "time": time,
                "change_nochan": change_no_change,
                "change_time": change_time,
                "error_no_error": error_no_error
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_CREATE_GU_VALIDATE_ACC_VALIDITY,
                                    **kwargs)

    def gim_gu_create_gu_validate_un_pwd_sponsor(self, element_name, gu_otname, gu_fname, gu_lname, email, cellphone,
                                                 username_type, gu_uname, un_length, un_case_type, prefix_suffix,
                                                 random_static, number, static, pwd_type, gu_pwd, confirm_pwd,
                                                 pwd_range_or_number, pwd_length, pwd_case_type, gim_url,
                                                 self_sponsor, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_otname] - OT name
        [gu_fname] - Guest user's first name
        [gu_lname] - Guest user's last name
        [gu_uname] - Guest user's user name
        [email] - Email Address of Guest
        [cellPhone] - Mobile number of Guest
        [username_type] - Type of Username
                            a. Guest Defined
                            b. Generate username with:
                                    i.Random Generated Username
                            c. FirstNameLastName
                                    i. No Prefix Suffix
                                    ii. Add Prefix
                                         a. Random Numbers
                                         b. Static
                                    iii. Add Suffix
                                         a. Random Numbers
                                         b. Static
                            d. FirstInitialLastName
                                    i. No Prefix Suffix
                                    ii. Add Prefix
                                         a. Random Numbers
                                         b. Static
                                    iii. Add Suffix
                                         a. Random Numbers
                                         b. Static
        [gu_uname] - Username of the guest user
        [un_length] - Length of the username
        [un_case_type] - Case Type of Username for Random Generated
                            a. Lower
                            b. Upper
                            c. Number
        [prefix_suffix] - Selects any one of the following options
                            a. No Prefix Suffix
                            b. Add Prefix
                            c. Add Suffix
        [random_static] - Selects either of following options:
                            a. Random Numbers
                            b. Static
        [number] - Inputs the number of Random numbers
        [static] - Inputs the Static prefix/Suffix
        [pwd_type] - Type of Password
                        a. Guest Defined
                        b. Random
                        c. Use Username as Password
                        d. Use Static Password
        [gu_pwd] -  Guest user's password
        [confirm_pwd] - confirms the password for the second time
        [pwd_range_or_number] - Specifies whether the password length is defined within a Range or a specified number
        [pwd_length] - Length of the password. This can either be a Range (8-10) or a number (15)
        [pwd_case_type] - Case Type of Password
                            a. Lower
                            b. Upper
                            c. Number
                            d. Special Characters
        [gim_url] - Url of GIM admin
        [self_sponsor] - Specifies whether the guest user creation is with Self Approval or Sponsor Approval.

        Creates GuestUser from Self Service, Validates username & Password, Validates Guest user in Admin Page.
        """
        args = {"gu_otname": gu_otname,
                "gu_fname": gu_fname,
                "gu_lname": gu_lname,
                "email": email,
                "cellPhone": cellphone,
                "username_type": username_type,
                "gu_uname": gu_uname,
                "un_length": un_length,
                "un_case_type": un_case_type,
                "prefix_suffix": prefix_suffix,
                "random_static": random_static,
                "number": number,
                "static": static,
                "pwd_type": pwd_type,
                "gu_pwd": gu_pwd,
                "confirm_pwd": confirm_pwd,
                "pwd_range_or_number": pwd_range_or_number,
                "pwd_length": pwd_length,
                "pwd_case_type": pwd_case_type,
                "gim_url": gim_url,
                "self_sponsor": self_sponsor
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_CREATE_GU_VALIDATE_UN_PWD_SPONSOR,
                                    **kwargs)

    def gim_gu_table_complete_validation(self, element_name, gu_uname, gu_fname, gu_lname, gu_email, gu_sms,
                                         gu_start_time, gu_end_time, gu_otname, gu_prv, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_uname] - Guest user's user name
        [gu_fname] - Guest user's first name
        [gu_lname] - Guest user's last name
        [gu_email] - Guest user's email id
        [gu_sms] - Guest user's SMS Address
        [gu_start_time] - Guest user's Start Time
        [gu_end_time] - Guest user's End Time
        [gu_otname] - OT name
        [gu_prv] - Provisioner name

        Validating guest user's user name, first, last name, email, OT name and provisioner from guest users table
        """
        args = {"gu_uname": gu_uname,
                "gu_fname": gu_fname,
                "gu_lname": gu_lname,
                "gu_email": gu_email,
                "gu_sms": gu_sms,
                "gu_start_time": gu_start_time,
                "gu_end_time": gu_end_time,
                "gu_otname": gu_otname,
                "gu_prv": gu_prv
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_TABLE_COMPLETE_VALIDATION, **kwargs)

    def gim_gu_summary_validation(self, element_name, gu_uname, gu_summary_key, gu_summary_value, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_uname] - Guest user's user name
        [gu_summary_key] - Summary Key from Guest users window
        [gu_summary_value] - Summary Value with respect to key

        Validating guest user's summary based on the key name
        """
        args = {"gu_uname": gu_uname,
                "gu_summary_key": gu_summary_key,
                "gu_summary_value": gu_summary_value
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_SUMMARY_VALIDATION, **kwargs)

    def gim_gu_notification_email_sms_un_pwd(self, element_name, gu_notification, ot_save, ot_cancel, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_notification] -
        [ot_save] -
        [ot_cancel] -
        Clicks on Extend Expiration button from Guest users table
        """
        args = {
            "gu_notification": gu_notification,
            "ot_save": ot_save,
            "ot_cancel": ot_cancel
        }

        return self.execute_keyword(element_name, args, self.command_const.GU_NOTIFICATION_EMAIL_SMS_UN_PWD, **kwargs)

    def gim_gu_notification_create_gu(self, element_name, gu_otname, gu_fname, gu_lname, gu_uname, gu_pwd, gu_email,
                                      gu_cellphone, user_email, user_sms, read_from_pop, text_from_pop, ok, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_otname] - OT name
        [gu_fname] - Guest user's first name
        [gu_lname] - Guest user's last name
        [gu_uname] - Guest user's user name
        [gu_pwd] -  Guest user's password
        [gu_email] - Guest user's email id
        [gu_cellphone] - Guest user's cell phone
        [user_email] - Guest user's email
        [user_sms] - Guest user's user-sms
        [read_from_pop] - read from pop up, if yes provide 'yes_read_from_pop'
        [text_from_pop] - text from pop-up
        [ok] - ok button

        Creating guest user from provisioner
        """
        args = {
            "gu_otname": gu_otname,
            "gu_fname": gu_fname,
            "gu_lname": gu_lname,
            "gu_uname": gu_uname,
            "gu_pwd": gu_pwd,
            "gu_email": gu_email,
            "gu_cellPhone": gu_cellphone,
            "user_email": user_email,
            "user_sms": user_sms,
            "read_from_pop": read_from_pop,
            "text_from_pop": text_from_pop,
            "ok": ok
        }

        return self.execute_keyword(element_name, args, self.command_const.GU_NOTIFICATION_CREATE_GU, **kwargs)

    def gim_gu_notification_ss_gu(self, element_name, self_prov, req_approval, gu_fname, gu_lname, gu_uname, gu_pwd,
                                  gu_email, gu_cell_phone, sponsor_fname, sponsor_lname, sponsor_email, sponsor_type,
                                  sp_submit, sp_ok, user_email, user_sms, text_from_pop, **kwargs):
        """
        Keyword Arguments:
        [element_name] 	- The UI element(s) the keyword should be run against
        [gu_fname]		- First Name of the Guest User.
        [gu_lname]		- Last Name of the Guest User.
        [gu_uname]		- User Name of the Guest User.
        [gu_pwd]		- Password of the Guest User.
        [gu_email]		- Email of the Guest User.
        [gu_cell_phone] - Cell phone number of the Guest User.
        [sponsor_fname] - Sponsor first name
        [sponsor_lname] - sponsor Laste name
        [sponsor_email] -sponsor email for approve or deny

        Enter the Custom Attribute Values for Guest Users
        """
        args = {
            "self_prov": self_prov,
            "req_approval": req_approval,
            "gu_fname": gu_fname,
            "gu_lname": gu_lname,
            "gu_uname": gu_uname,
            "gu_pwd": gu_pwd,
            "gu_email": gu_email,
            "gu_cell_phone": gu_cell_phone,
            "sponsor_fname": sponsor_fname,
            "sponsor_lname": sponsor_lname,
            "sponsor_email": sponsor_email,
            "sponsor_type": sponsor_type,
            "sp_submit": sp_submit,
            "sp_ok": sp_ok,
            "user_email": user_email,
            "user_sms": user_sms,
            "text_from_pop": text_from_pop
        }

        return self.execute_keyword(element_name, args, self.command_const.GU_NOTIFICATION_SS_GU, **kwargs)

    def gim_gu_create_accessible_to_prov_options(self, element_name, gu_otname, fl_name, gu_fname, gu_lname, gu_uname,
                                                 pwd, gu_email, cellphone, sms_gateway_list, doe_yes_or_no,
                                                 doe_option, acc_exp, acc_exp_option, error_no_error, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_otname] - Selects the Onboarding Template from the dropdown.
        [fl_name] - Specifies whether first name and last name needs to be entered or not.
        [gu_fname] - First name of Guest User
        [gu_lname] - Last Name of Guest User
        [gu_uname] - Username of Guest User
        [pwd] - Password of Guest User
        [gu_email] - Email of Guest User
        [cellphone] - Mobile Number of Guest User
        [sms_gateway_list] - Validates the Changes in Guest User Creation page, for SMS Gateway
        [doe_yes_or_no] - Validates the Changes in Guest User Creation page, with delete on expire enabled/disabled.
        [doe_option] - Validates the Changes in Guest User Creation page, for the following options.
                        a. Delete on Expire
                        b. Do Not Delete on Expire
        [acc_exp] - Validates the Changes in Guest User Creation page, with Account Expiration enabled/disabled.
        [acc_exp_option] - Validates the Changes in Guest User Creation page, for the following options
                            a. Max Expiration Time
                            b. Permanent
        [error_no_error] - To Handle the Error Conditions.

        Validates the Provisioner Options and Creates a Guest User.
        """
        args = {"gu_otname": gu_otname,
                "fl_name": fl_name,
                "gu_fname": gu_fname,
                "gu_lname": gu_lname,
                "gu_uname": gu_uname,
                "pwd": pwd,
                "gu_email": gu_email,
                "cellphone": cellphone,
                "sms_gateway_list": sms_gateway_list,
                "doe_yes_or_no": doe_yes_or_no,
                "doe_option": doe_option,
                "acc_exp": acc_exp,
                "acc_exp_option": acc_exp_option,
                "error_no_error": error_no_error
                }

        return self.execute_keyword(element_name, args, self.command_const.GU_CREATE_ACCESSIBLE_TO_PROV_OPTIONS,
                                    **kwargs)

    def gim_gu_enable_or_disable_delete_expiry(self, element_name, gu_otname, gu_fname, gu_lname, gu_uname, gu_pwd,
                                               gu_enable, gu_email, gu_cellphone, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gu_otname] - OT name
        [gu_fname] - Guest user's first name
        [gu_lname] - Guest user's last name
        [gu_uname] - Guest user's user name
        [gu_pwd] -  Guest user's password
        [gu_enable]- Guest user's enable or disable
        [gu_email] - Guest user's email id
        [gu_cellphone] - Guest user's cell phone

        This keyword is used to enable or disable or delete or expiry of guest users
        """
        args = {
            "gu_otname": gu_otname,
            "gu_fname": gu_fname,
            "gu_lname": gu_lname,
            "gu_uname": gu_uname,
            "gu_pwd": gu_pwd,
            "gu_enable": gu_enable,
            "gu_email": gu_email,
            "gu_cellPhone": gu_cellphone
        }

        return self.execute_keyword(element_name, args, self.command_const.GU_ENABLE_OR_DISABLE_DELETE_EXPIRY, **kwargs)

    def gim_gu_sponsor_approval_from_provisioner_login(self, element_name, approve_or_deny, spon_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [approve_or_deny] - if approve provide 'approve' or if deny provide 'deny'
        [spon_name] - Name of the sponsor

        This keyword is used to approve or deny users from sponsors from provisioner's page
        """
        args = {
            "approve_or_deny": approve_or_deny,
            "spon_name": spon_name
        }

        return self.execute_keyword(element_name, args, self.command_const.GU_SPONSOR_APPROVAL_FROM_PROVISIONER_LOGIN,
                                    **kwargs)

    def gim_gu_admin_gu_filters(self, element_name, primary_value, compare_value, text_value, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [primary_value] - Primary value from the first drop down of the filter selection
        [compare_value] - Compare value from the second drop down of the filter selection
        [text_value] - Text value from the the filter selection

        This keyword is used to filter the guest users from admin and provisioner's page
        """
        args = {
            "primary_value": primary_value,
            "compare_value": compare_value,
            "text_value": text_value
        }

        return self.execute_keyword(element_name, args, self.command_const.GU_ADMIN_GU_FILTERS, **kwargs)

    def gim_gu_resend_details(self, element_name, resend_details, gu_uname, approval, fname, lname, mail_pwd, mobile,
                              sp_name, sp_pwd, url, username, password, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [resend_details] - This Option helps to identify among the following options
                            a. Resend Password
                            b. Resend All Details
                            c. Resend Details is not Enabled.
        [gu_uname] - Username of the Guest user
        [approval] - This option is to differentiate between
                     a. self provision
                     b. self provision with sponsor approval
        [fname] - Firstname of the guest user
        [lname] - Lastname of the guest user
        [mail_pwd] - Password of the hmail login
        [mobile] - Mobile Number of the guest user
        [ss_name] - Sponsor Name
        [ss_pwd] - Sponsor Password
        [url] - GIM Admin URL
        [username] - GIM Admin username
        [password] - GIM Admin Password

        This keyword is used to resend gu details
        """
        args = {"resend_details": resend_details,
                "gu_uname": gu_uname,
                "approval": approval,
                "fname": fname,
                "lname": lname,
                "mail_pwd": mail_pwd,
                "mobile": mobile,
                "ss_name": sp_name,
                "ss_pwd": sp_pwd,
                "url": url,
                "username": username,
                "password": password
                }
        return self.execute_keyword(element_name, args, self.command_const.GU_RESEND_DETAILS, **kwargs)
