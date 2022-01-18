from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.GIM.GimonboardingtemplatesConstants \
    import GimonboardingtemplatesConstants


class UiGimOnboardingTemplatesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGimOnboardingTemplatesKeywords, self).__init__()
        self.api_const = self.constants.API_GIM_ONBOARDING_TEMPLATES
        self.command_const = GimonboardingtemplatesConstants()

    def gim_ot_signed_in_user_should_exist(self, element_name, signed_in_user, signed_user_footer_text, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [signed_in_user] - Signed in GIM Admin USERNAME
        [signed_user_footer_text] - GIM Admin USERNAME at footer text

        Validating GIM Admin USERNAME from content panel and footer text after successful login
        """
        args = {"signed_in_user": signed_in_user,
                "signed_user_footer_text": signed_user_footer_text}

        return self.execute_keyword(element_name, args, self.command_const.OT_SIGNED_IN_USER_SHOULD_EXIST, **kwargs)

    def gim_ot_signed_user_footer(self, element_name, signed_user_footer_text, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [signed_user_footer_text] - USERNAME at footer text

        Validating GIM Admin USERNAME from footer text after successful login
        """
        args = {"signed_user_footer_text": signed_user_footer_text}

        return self.execute_keyword(element_name, args, self.command_const.OT_SIGNED_USER_FOOTER, **kwargs)

    def gim_ot_add(self, element_name, ot_name, ot_type, ot_api_chk, ot_global, ot_duration, ot_time, ot_save,
                   **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_name] - Name of the Onboarding Template
        [ot_type] - Type of OT, select any one of OT types 'default, sponsor, api and outlook'
        [ot_api_chk] - Checkbox option to 'check' or None for REST API type
        [ot_global] - Checkbox option to 'check' or None for global
        [ot_duration] - Duration in int, otherwise default (8)
        [ot_time] - Selection of time in Hours, Minutes and Seconds. If None, default time selection (hours)
        [ot_save] - Save button, if parameter contains 'save' it will save it otherwise None

        Creating Onboarding Template default, sponsor, REST Api and Outlook plugin based on selection of OT type
        """
        args = {"obt_name": ot_name,
                "ot_type": ot_type,
                "ot_api_chk": ot_api_chk,
                "ot_global": ot_global,
                "ot_duration": ot_duration,
                "ot_time": ot_time,
                "ot_save": ot_save}

        return self.execute_keyword(element_name, args, self.command_const.OT_ADD, **kwargs)

    def gim_ot_should_exist(self, element_name, ot_name, ot_type, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_name] - Name of the Onboarding Template
        [ot_type] - Type of the Onboarding Template

        Validating created Onboarding Template Name and Type from OT table
        """
        args = {"ot_name": ot_name,
                "ot_type": ot_type}

        return self.execute_keyword(element_name, args, self.command_const.OT_SHOULD_EXIST, **kwargs)

    def gim_ot_verify_admin_signed(self, element_name, signed_in_user, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [signed_in_user] - Signed in USERNAME

        Validating GIM Admin USERNAME from content panel after successful login
        """
        args = {"signed_in_user": signed_in_user}

        return self.execute_keyword(element_name, args, self.command_const.OT_VERIFY_ADMIN_SIGNED, **kwargs)

    def gim_ot_common_tab(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Enabled or disabled tab status of OT by selecting different Onboarding template types from Common tab
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.OT_COMMON_TAB, **kwargs)

    def gim_ot_device_family_types(self, element_name, signed_in_user, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [signed_in_user] -  Signed in user

        Default validation from Device Family Types tab of onboarding template
        """
        args = {"signed_in_user": signed_in_user}

        return self.execute_keyword(element_name, args, self.command_const.OT_DEVICE_FAMILY_TYPES, **kwargs)

    def gim_ot_guest_users(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Default validation from Guest Users tab of onboarding template
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.OT_GUEST_USERS, **kwargs)

    def gim_ot_iot_user_devices(self, element_name, signed_in_user, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [signed_in_user] -  Signed in user

        Default validation from IOT User Devices tab of onboarding template
        """
        args = {"signed_in_user": signed_in_user}

        return self.execute_keyword(element_name, args, self.command_const.OT_IOT_USER_DEVICES, **kwargs)

    def gim_ot_notification(self, element_name, ot_name, sms_temp_avilable_var, sms_temp_avilable_var_names,
                            sms_message_text, sms_message_text_area, email_available_var, email_available_var_names,
                            email_subject_text, email_message_text, tems_text, tems_text_area, term_of_use, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_name] - Name of the Onboarding Template
        [sms_temp_avilable_var] - Label of SMS Template from SMS
        [sms_temp_avilable_var_names] - List of Available Variables from SMS Template
        [sms_message_text] - Label of Message from SMS Template
        [sms_message_text_area] - List from SMS Message text area
        [email_available_var] - Label of Available Variables from Email
        [email_available_var_names] - List of Available Variables from Email Template
        [email_subject_text] - Label of Subject from Email Subject
        [email_message_text] - List of Messages from Email Message
        [tems_text] - Label Terms
        [tems_text_area] - Terms default content
        [term_of_use] - Defining your own text

        Default validation from Notification tab of onboarding template
        """
        args = {"ot_name": ot_name,
                "sms_temp_avilable_var": sms_temp_avilable_var,
                "sms_temp_avilable_var_names": sms_temp_avilable_var_names,
                "sms_message_text": sms_message_text,
                "sms_message_text_area": sms_message_text_area,
                "email_available_var": email_available_var,
                "email_available_var_names": email_available_var_names,
                "email_subject_text": email_subject_text,
                "email_message_text": email_message_text,
                "tems_text": tems_text,
                "tems_text_area": tems_text_area,
                "term_of_use": term_of_use}

        return self.execute_keyword(element_name, args, self.command_const.OT_NOTIFICATION, **kwargs)

    def gim_ot_advanced(self, element_name, signed_in_user, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [signed_in_user] -  Signed in user

        Default validation from Advanced tab of onboarding template
        """
        args = {"signed_in_user": signed_in_user}

        return self.execute_keyword(element_name, args, self.command_const.OT_ADVANCED, **kwargs)

    def gim_ot_summary_common(self, element_name, summary_key, summary_value, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [summary_key] - Field name from summary of Common field set
        [summary_value] - Field value from summary of Common field set

        Summary of common field set validation from created onboarding template
        """
        args = {"summary_key": summary_key,
                "summary_value": summary_value}

        return self.execute_keyword(element_name, args, self.command_const.OT_SUMMARY_COMMON, **kwargs)

    def gim_ot_summary_guest_users(self, element_name, summary_key, summary_value, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [summary_key] - Field name from summary of Guest Users field set
        [summary_value] - Field value from summary of Guest Users field set

        Summary of Guest Users field set validation from created onboarding template
        """
        args = {"summary_key": summary_key,
                "summary_value": summary_value}

        return self.execute_keyword(element_name, args, self.command_const.OT_SUMMARY_GUEST_USERS, **kwargs)

    def gim_ot_summary_device_family(self, element_name, summary_key, summary_value, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [summary_key] - Field name from summary of Device Family Types field set
        [summary_value] - Field value from summary of Device Family Types field set

        Summary of Device Family Types field set validation from created onboarding template
        """
        args = {"summary_key": summary_key,
                "summary_value": summary_value}

        return self.execute_keyword(element_name, args, self.command_const.OT_SUMMARY_DEVICE_FAMILY, **kwargs)

    def gim_ot_summary_iot_user_devices(self, element_name, summary_key, summary_value, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [summary_key] - Field name from summary of IOT User Devices field set
        [summary_value] - Field value from summary of IOT User Devices field set

        Summary of IOT User Devices field set validation from created onboarding template
        """
        args = {"summary_key": summary_key,
                "summary_value": summary_value}

        return self.execute_keyword(element_name, args, self.command_const.OT_SUMMARY_IOT_USER_DEVICES, **kwargs)

    def gim_ot_summary_mobile_app(self, element_name, summary_key, summary_value, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [summary_key] - Field name from summary of Mobile App field set
        [summary_value] - Field value from summary of Mobile App field set

        Summary of Mobile App field set validation from created onboarding template
        """
        args = {"summary_key": summary_key,
                "summary_value": summary_value}

        return self.execute_keyword(element_name, args, self.command_const.OT_SUMMARY_MOBILE_APP, **kwargs)

    def gim_ot_summary_notification(self, element_name, summary_key, summary_value, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [summary_key] - Field name from summary of Notification field set
        [summary_value] - Field value from summary of Notification field set

        Summary of Notification field set validation from created onboarding template
        """
        args = {"summary_key": summary_key,
                "summary_value": summary_value}

        return self.execute_keyword(element_name, args, self.command_const.OT_SUMMARY_NOTIFICATION, **kwargs)

    def gim_ot_summary_advanced(self, element_name, summary_key, summary_value, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [summary_key] - Field name from summary of Advanced field set
        [summary_value] - Field value from summary of Advanced field set

        Summary of Advanced field set validation from created onboarding template
        """
        args = {"summary_key": summary_key,
                "summary_value": summary_value}

        return self.execute_keyword(element_name, args, self.command_const.OT_SUMMARY_ADVANCED, **kwargs)

    def gim_ot_summary_sponsor(self, element_name, summary_key, summary_value, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [summary_key] - Field name from summary of Sponsor field set
        [summary_value] - Field value from summary of Sponsor field set

        Summary of Sponsor field set validation from created onboarding template
        """
        args = {"summary_key": summary_key,
                "summary_value": summary_value}

        return self.execute_keyword(element_name, args, self.command_const.OT_SUMMARY_SPONSOR, **kwargs)

    def gim_ot_select_ot_edit(self, element_name, ot_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_name] - OT name to select from OT table

        Selecting given onboarding template from OT table for edit
        """
        args = {"ot_name": ot_name}

        return self.execute_keyword(element_name, args, self.command_const.OT_SELECT_OT_EDIT, **kwargs)

    def gim_ot_cancel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Clicks on Cancel button from Common tab of Add Onboarding Template
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.OT_CANCEL, **kwargs)

    def gim_ot_save(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Clicks on Save button from Common tab of Add Onboarding Template
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.OT_SAVE, **kwargs)

    def gim_ot_select_ot_copy(self, element_name, ot_name, ot_copy_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_name] - OT name to select from OT table
        [ot_copy_name] - New Name to the copying OT

        Copy onboarding template from OT table
        """
        args = {"ot_name": ot_name,
                "ot_copy_name": ot_copy_name}

        return self.execute_keyword(element_name, args, self.command_const.OT_SELECT_OT_COPY, **kwargs)

    def gim_ot_select_ot_delete(self, element_name, ot_delete, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_delete] - OT name to delete from OT table

        Delete onboarding template from OT table
        """
        args = {"ot_delete": ot_delete}

        return self.execute_keyword(element_name, args, self.command_const.OT_SELECT_OT_DELETE, **kwargs)

    def gim_ot_refresh(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Clicks on Refresh button from onboarding template table
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.OT_REFRESH, **kwargs)

    def gim_ot_click_nav_bar(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Clicks on OnBoarding Template from left navigation bar
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.OT_CLICK_NAV_BAR, **kwargs)

    def gim_ot_default_validation(self, element_name, ot_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_name] - OT Name from table

        Default validation of OT table before and after selecting OT
        """
        args = {"ot_name": ot_name}

        return self.execute_keyword(element_name, args, self.command_const.OT_DEFAULT_VALIDATION, **kwargs)

    def gim_ot_edit_common(self, element_name, ot_name, ot_duration, ot_time, ot_save, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_name] - OT Name from table
        [ot_duration] - Duration in int
        [ot_time] - Selection of time Hours, Minutes and Seconds
        [ot_save] - If value is save, clicks on Save others None


        Editing of OT from Common tab
        """
        args = {"ot_edit_name": ot_name,
                "ot_edit_duration": ot_duration,
                "ot_edit_time": ot_time,
                "ot_save": ot_save}

        return self.execute_keyword(element_name, args, self.command_const.OT_EDIT_COMMON, **kwargs)

    def gim_ot_edit_guest_users(self, element_name, ot_save, ot_gu_rights, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_save] - If value is save, clicks on Save others None
        [ot_gu_rights] - Checkbox to check or uncheck for guest user rights

        Editing of OT from Guest Users tab
        """
        args = {"ot_save": ot_save,
                "ot_gu_rights": ot_gu_rights}

        return self.execute_keyword(element_name, args, self.command_const.OT_EDIT_GUEST_USERS, **kwargs)

    def gim_ot_edit_devices(self, element_name, ot_save, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_save] - If value is save, clicks on Save others None

        Editing of OT from Devices tab
        """
        args = {"ot_save": ot_save}

        return self.execute_keyword(element_name, args, self.command_const.OT_EDIT_DEVICES, **kwargs)

    def gim_ot_edit_device_family(self, element_name, ot_save, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_save] - If value is save, clicks on Save others None

        Editing of OT from Devices Family Types tab
        """
        args = {"ot_save": ot_save}

        return self.execute_keyword(element_name, args, self.command_const.OT_EDIT_DEVICE_FAMILY, **kwargs)

    def gim_ot_edit_advanced(self, element_name, ot_save, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_save] - If value is save, clicks on Save others None

        Editing of OT from Advanced tab
        """
        args = {"ot_save": ot_save}

        return self.execute_keyword(element_name, args, self.command_const.OT_EDIT_ADVANCED, **kwargs)

    def gim_ot_edit_notification(self, element_name, ot_save, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_save] - If value is save, clicks on Save others None

        Editing of OT from Notification tab
        """
        args = {"ot_save": ot_save}

        return self.execute_keyword(element_name, args, self.command_const.OT_EDIT_NOTIFICATION, **kwargs)

    def gim_ot_add_sponsor(self, element_name, ot_spon_domain, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_spon_domain] - domain name

        Adding domain to Sponsor
        """
        args = {"ot_spon_domain": ot_spon_domain}

        return self.execute_keyword(element_name, args, self.command_const.OT_ADD_SPONSOR, **kwargs)

    def gim_ot_select_otname_row_table(self, element_name, ot_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_name] - Onboarding Template

        Selecting OT from OT table based on OT name
        """
        args = {"ot_name": ot_name}

        return self.execute_keyword(element_name, args, self.command_const.OT_SELECT_OTNAME_ROW_TABLE, **kwargs)

    def gim_ot_expected_ot_exist_table(self, element_name, ot_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_name] - Onboarding Template

        Validating the existence of OT from OT table based on OT name
        """
        args = {"ot_name": ot_name}

        return self.execute_keyword(element_name, args, self.command_const.OT_EXPECTED_EXIST_TABLE, **kwargs)

    def gim_ot_gu_notification(self, element_name, ot_gu_notif, check, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_name] - Onboarding Template
        [check] - Check is boolean for enabled or disabled state

        Validating guest notifications status from guest users tab of onboarding template
        """
        args = {"ot_gu_notif": ot_gu_notif,
                "check": check}

        return self.execute_keyword(element_name, args, self.command_const.OT_GU_NOTIFICATION, **kwargs)

    def gim_ot_gu_acc_prv_gen_acc_act(self, element_name, add_ot_click_gu, ot_account_act, ot_save, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [add_ot_click_gu] - If value is yes clicks on Guest users tab of OT
        [ot_account_act] - time_based or first_login account
        [ot_save] - If value is save, clicks on Save others None

        Validation and selection of  First Login or Time Based accounts from guest users tab of onboarding template
        """
        args = {"add_ot_click_gu": add_ot_click_gu,
                "ot_account_act": ot_account_act,
                "ot_save": ot_save}

        return self.execute_keyword(element_name, args, self.command_const.OT_GU_ACC_PRV_GEN_ACC_ACT, **kwargs)

    def gim_ot_gu_acc_prv_gen_acc_exp(self, element_name, add_ot_click_gu, ot_save, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [add_ot_click_gu] - If value is yes clicks on Guest users tab of OT
        [ot_account_act] - time_based or first_login account
        [ot_save] - If value is save, clicks on Save others None

        Validation and Selection of Account expiry by selecting Permanent and other options from guest users tab of OT
        """
        args = {"add_ot_click_gu": add_ot_click_gu,
                "ot_save": ot_save}

        return self.execute_keyword(element_name, args, self.command_const.OT_GU_ACC_PRV_GEN_ACC_EXP, **kwargs)

    def gim_ot_should_not_exist(self, element_name, ot_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_name] - Name of the Onboarding Template

        Created Onboarding Template should not exists from the table
        """
        args = {"ot_name": ot_name}

        return self.execute_keyword(element_name, args, self.command_const.OT_SHOULD_NOT_EXIST, **kwargs)

    def gim_ot_gu_edit_username_field(self, element_name, uncheck, ot_save, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [uncheck] - Un-checking the check box of Edit username field
        [ot_save] - Save OT

        Edit Username field from Generate username option from Guest Users tab of OT
        """
        args = {"uncheck": uncheck,
                "ot_save": ot_save}

        return self.execute_keyword(element_name, args, self.command_const.OT_GU_EDIT_USERNAME_FIELD, **kwargs)

    def gim_ot_delete_error_text(self, element_name, ot_error_text, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_error_text] - Error message text

        Validating error message while deleting OT which has associated with members
        """
        args = {"ot_error_text": ot_error_text}

        return self.execute_keyword(element_name, args, self.command_const.OT_DELETE_ERROR_TEXT, **kwargs)

    def gim_ot_multiple_row_selection(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Multiple row selection from Onboarding Template table
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.OT_MULTIPLE_ROW_SELECTION, **kwargs)

    def gim_ot_table_should_empty(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        OT Table should be empty
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.OT_TABLE_SHOULD_EMPTY, **kwargs)

    def gim_ot_gu_username(self, element_name, username_type, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [username_type] - Type of Username of the Guest User.
                            a. Guest Defined
                            b. Generate Username with
                            c. Use Email as Username
                            d. Use Mobile Phone as Username

        Select the UserName Type for Guest User
        """
        args = {"username_type": username_type}

        return self.execute_keyword(element_name, args, self.command_const.OT_GU_USERNAME, **kwargs)

    def gim_ot_gu_password(self, element_name, pwd_type, confirm_pwd, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [pwd_type] - Type of Password for the Guest User.
                            a. Guest Defined
                            b. Random Generated
                            c. Use Username as Password
                            d. Use Static Password

        Select the UserName Type for Guest User
        """
        args = {"pwd_type": pwd_type,
                "confirm_pwd": confirm_pwd}

        return self.execute_keyword(element_name, args, self.command_const.OT_GU_PASSWORD, **kwargs)

    def gim_ot_gu_random_un(self, element_name, un_length, random_un_type_lower, random_un_type_upper,
                            random_un_type_number, error_or_noerror, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [un_length] - Length of the Random Username
        [random_un_type_lower] - Selects the checkbox Lowercase
        [random_un_type_upper] - Selects the checkbox Uppercase
        [random_un_type_number] - Selects the checkbox Number

        Selects the UserName Type for Guest User under Random Generated Username
        """
        args = {"un_length": un_length,
                "random_un_type_lower": random_un_type_lower,
                "random_un_type_upper": random_un_type_upper,
                "random_un_type_number": random_un_type_number,
                "error_or_noerror": error_or_noerror}

        return self.execute_keyword(element_name, args, self.command_const.OT_GU_RANDOM_UN, **kwargs)

    def gim_ot_gu_first_lastname(self, element_name, un_type, rand_or_static, number, static, error_or_noerror,
                                 **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [un_type] - Type of Username
        [rand_or_static] - Selects the Checkbox Random Numbers or Static
        [number] - Inputs the Random Number
        [static] - Inputs the Static Value
        [error_or_noerror] - To Validate the Errored Cases.

        Select the UserName Type for Guest User under FirstNameLastName.
        """
        args = {"un_type": un_type,
                "rand_or_static": rand_or_static,
                "number": number,
                "static": static,
                "error_or_noerror": error_or_noerror}

        return self.execute_keyword(element_name, args, self.command_const.OT_GU_FIRST_LASTNAME, **kwargs)

    def gim_ot_gu_finitial_lastname(self, element_name, un_type, rand_or_static, number, static, error_or_noerror,
                                    **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [un_type] - Type of Username
        [rand_or_static] - Selects the Checkbox Random Numbers or Static
        [number] - Inputs the Random Number
        [static] - Inputs the Static Value
        [error_or_noerror] - To Validate the Error Cases.

        Select the UserName Type for Guest User for FirstInitialLastName
        """
        args = {"un_type": un_type,
                "rand_or_static": rand_or_static,
                "number": number,
                "static": static,
                "error_or_noerror": error_or_noerror}

        return self.execute_keyword(element_name, args, self.command_const.OT_GU_FINITIAL_LASTNAME, **kwargs)

    def gim_ot_gu_pwd_complexity_config(self, element_name, pwd_length, pwd_type_lower, pwd_type_upper,
                                        pwd_type_number, pwd_type_special, error_or_noerror, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [pwd_length] - Length of the Password
        [pwd_type_lower] - Selects the checkbox Lowercase
        [pwd_type_upper] - Selects the checkbox Uppercase
        [pwd_type_number] - Selects the checkbox Number
        [pwd_type_special] - Selects the checkbox Special Characters
        [error_or_noerror] - TO Validate the Error Scenarios.

        Configures the Password Complexity.
        """
        args = {"pwd_length": pwd_length,
                "pwd_type_lower": pwd_type_lower,
                "pwd_type_upper": pwd_type_upper,
                "pwd_type_number": pwd_type_number,
                "pwd_type_special": pwd_type_special,
                "error_or_noerror": error_or_noerror}

        return self.execute_keyword(element_name, args, self.command_const.OT_GU_PWD_COMPLEXITY_CONFIG, **kwargs)

    def gim_ot_validation_advanced_tab(self, element_name, time_zone_label, default_time_zone,
                                       default_label_for_ldap_prov, associated_label_ldap_groups, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [time_zone_label] - Time zone label from OT advanced tab
        [default_time_zone] - Default ime zone value from OT advanced tab
        [default_label_for_ldap_prov] - Default label for ldap provisioner from OT advanced tab
        [associated_label_ldap_groups] - Associated label for ldap groups label

        This keyword is used to validate advanced tab of OT
        """
        args = {"time_zone_label": time_zone_label,
                "default_time_zone": default_time_zone,
                "default_label_for_ldap_prov": default_label_for_ldap_prov,
                "associated_label_ldap_groups": associated_label_ldap_groups}

        return self.execute_keyword(element_name, args, self.command_const.OT_VALIDATION_ADVANCED_TAB, **kwargs)

    def gim_ot_temp_acc_validity(self, element_name, duration, time_type, err_no_err, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [duration] - Duration between 1-9999
        [time_type] - Select the time type in between minutes, hours and days.

        Configures the Temporary Account Validity settings in OT.
        """
        args = {"duration": duration,
                "time_type": time_type,
                "err_no_err": err_no_err}

        return self.execute_keyword(element_name, args, self.command_const.OT_TEMP_ACC_VALIDITY, **kwargs)

    def gim_ot_accessible_to_prov_de(self, element_name, name_option, name, limit_devices, device_limit_number,
                                     display_admin_comments, admin_comment, source, source_option,
                                     static_source_value, asset_type, asset_type_option, doe_yes_or_no, doe_option,
                                     acc_exp, device_type_group, device_type_group_option, device_types,
                                     device_type_option, account_activation_type, error_or_no, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [duration] - Duration between 1-9999
        [time_type] - Select the time type in between minutes, hours and days.

        Configures the Temporary Account Validity settings in OT for Device.
        """
        args = {"name_option": name_option,
                "name": name,
                "limit_devices": limit_devices,
                "device_limit_number": device_limit_number,
                "display_admin_comments": display_admin_comments,
                "admin_comment": admin_comment,
                "source": source,
                "source_option": source_option,
                "static_source_value": static_source_value,
                "asset_type": asset_type,
                "asset_type_option": asset_type_option,
                "doe_yes_or_no": doe_yes_or_no,
                "doe_option": doe_option,
                "acc_exp": acc_exp,
                "device_type_group": device_type_group,
                "device_type_group_option": device_type_group_option,
                "device_types": device_types,
                "device_type_option": device_type_option,
                "account_activation_type": account_activation_type,
                "error_or_no": error_or_no}

        return self.execute_keyword(element_name, args, self.command_const.OT_ACCESSIBLE_TO_PROV_DE, **kwargs)

    def gim_ot_accessible_to_prov_gu(self, element_name, sms_gateway_list, acc_exp, acc_exp_option, delete_on_expiry,
                                     doe_option, access_groups, first_last_name, first_last_name_option, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [sms_gateway_list] - Duration between 1-9999
        [acc_exp] - Select the time type in between minutes, hours and days.
        [acc_exp_option] - options to select account expiration
        [delete_on_expiry] - delete on expiry
        [doe_option] - delete on expiry yes or no option
        [access_groups] - access group
        [first_last_name] - first and last name label
        [first_last_name_option] - first and last name option

        Configures the Temporary Account Validity settings in OT for Guest User.
        """
        args = {"sms_gateway_list": sms_gateway_list,
                "acc_exp": acc_exp,
                "acc_exp_option": acc_exp_option,
                "delete_on_expiry": delete_on_expiry,
                "doe_option": doe_option,
                "access_groups": access_groups,
                "first_last_name": first_last_name,
                "first_last_name_option": first_last_name_option}

        return self.execute_keyword(element_name, args, self.command_const.OT_ACCESSIBLE_TO_PROV_GU, **kwargs)

    def gim_ot_add_ldap_group(self, element_name, check_box_status, time_zone, time_zone_name, ad_group,
                              ad_group_name, remove_group, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [check_box_status] - Expected checkbox status, True or False
        [time_zone] - if 'yes_time_zone', it will select expected time zone
        [time_zone_name] - Name of the time zone
        [ad_group] - if 'yes_ad_group', it will ad group name
        [ad_group_name] - Name of the ad group
        [remove_group] - remove the added ad group 'yes_remove_group'

        This keyword is used to validate advanced tab of OT
        """
        args = {"check_box_status": check_box_status,
                "time_zone": time_zone,
                "time_zone_name": time_zone_name,
                "ad_group": ad_group,
                "ad_group_name": ad_group_name,
                "remove_group": remove_group}

        return self.execute_keyword(element_name, args, self.command_const.OT_ADD_LDAP_GROUP, **kwargs)

    def gim_ot_sponsor_auto_approve_deny(self, element_name, ot_spon_domain, spon_response, auto_approve_deny,
                                         **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ot_spon_domain] - domain name
        [spon_response] - Sponsor approve or deny responce time
        [auto_approve_deny]- Sponsor Auto Approve or Deny the guest User .

        Adding domain to Sponsor
        """
        args = {"ot_spon_domain": ot_spon_domain,
                "spon_response": spon_response,
                "auto_approve_deny": auto_approve_deny}

        return self.execute_keyword(element_name, args, self.command_const.OT_SPONSOR_AUTO_APPROVE_DENY, **kwargs)

    def gim_ot_resend_details(self, element_name, resend_yes_no, resend_option, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [resend_yes_no] - Expected checkbox status of Resend Details, True or False
        [resend_option] - selecting among different available options as following:
                            a. Resend All Details
                            b. Resend Password

        This keyword is used to Configure Resend Details
        """
        args = {"resend_yes_no": resend_yes_no,
                "resend_option": resend_option}

        return self.execute_keyword(element_name, args, self.command_const.OT_RESEND_DETAILS, **kwargs)
