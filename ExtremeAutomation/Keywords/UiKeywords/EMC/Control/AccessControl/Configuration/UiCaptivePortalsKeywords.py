from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.CaptiveportalsConstants import CaptiveportalsConstants


class UiCaptivePortalsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiCaptivePortalsKeywords, self).__init__()
        self.api_const = self.constants.API_CAPTIVEPORTALS
        self.command_const = CaptiveportalsConstants()

    def access_control_captive_portals_admin_click_save_button_on_administration_page(self, element_name, **kwargs):
        """Returns the result of access_control_captive_portals_admin_click_save_button_on_administration_page."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CAPTIVE_PORTALS_ADMIN_CLICK_SAVE_BUTTON_ON_ADMINISTRATION_PAGE,
                                    **kwargs)

    def access_control_captive_portals_admin_select_login_config(self, element_name, user_name, **kwargs):
        """Returns the result of access_control_captive_portals_admin_select_login_config."""
        args = {"user_name": user_name.encode('unicode_escape')}

        return self.execute_keyword(element_name, args, self.command_const.CAPTIVE_PORTALS_ADMIN_SELECT_LOGIN_CONFIG,
                                    **kwargs)

    def access_control_captive_portals_admin_verify_existence_of_login_config(self, element_name, user_name, **kwargs):
        """Returns the result of access_control_captive_portals_admin_verify_existence_of_login_config."""
        args = {"user_name": user_name.encode('unicode_escape')}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CAPTIVE_PORTALS_ADMIN_VERIFY_EXISTENCE_OF_LOGIN_CONFIG, **kwargs)

    def access_control_captive_portals_admin_click_add_login_config_button(self, element_name, **kwargs):
        """Returns the result of access_control_captive_portals_admin_click_add_login_config_button."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CAPTIVE_PORTALS_ADMIN_CLICK_ADD_LOGIN_CONFIG_BUTTON, **kwargs)

    def access_control_captive_portals_admin_click_delete_login_config_button(self, element_name, **kwargs):
        """Returns the result of access_control_captive_portals_admin_click_delete_login_config_button."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CAPTIVE_PORTALS_ADMIN_CLICK_DELETE_LOGIN_CONFIG_BUTTON, **kwargs)

    def access_control_captive_portals_admin_click_edit_login_config_button(self, element_name, **kwargs):
        """Returns the result of access_control_captive_portals_admin_click_edit_login_config_button."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CAPTIVE_PORTALS_ADMIN_CLICK_EDIT_LOGIN_CONFIG_BUTTON, **kwargs)

    def access_control_captive_portals_admin_delete_login_config(self, element_name, user_name, **kwargs):
        """Returns the result of access_control_captive_portals_admin_delete_login_config."""
        args = {"user_name": user_name}

        return self.execute_keyword(element_name, args, self.command_const.CAPTIVE_PORTALS_ADMIN_DELETE_LOGIN_CONFIG,
                                    **kwargs)

    def access_control_captive_portals_admin_select_authentication_for_login_config(self, element_name, auth_name,
                                                                                    **kwargs):
        """Returns the result of access_control_captive_portals_admin_select_authentication_for_login_config."""
        args = {"auth_name": auth_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CAPTIVE_PORTALS_ADMIN_SELECT_AUTHENTICATION_FOR_LOGIN_CONFIG,
                                    **kwargs)

    def access_control_captive_portals_admin_add_new_user_for_login_config(self, element_name, **kwargs):
        """Returns the result of access_control_captive_portals_admin_add_new_user_for_login_config."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CAPTIVE_PORTALS_ADMIN_ADD_NEW_USER_FOR_LOGIN_CONFIG, **kwargs)

    def access_control_captive_portals_admin_select_user_for_login_config(self, element_name, user_name, **kwargs):
        """Returns the result of access_control_captive_portals_admin_select_user_for_login_config."""
        args = {"user_name": user_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CAPTIVE_PORTALS_ADMIN_SELECT_USER_FOR_LOGIN_CONFIG, **kwargs)

    def access_control_captive_portals_admin_select_role_for_login_config(self, element_name, role_name, **kwargs):
        """Returns the result of access_control_captive_portals_admin_select_role_for_login_config."""
        args = {"role_name": role_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CAPTIVE_PORTALS_ADMIN_SELECT_ROLE_FOR_LOGIN_CONFIG, **kwargs)

    def access_control_captive_portals_admin_click_add_button_save_login_config(self, element_name, **kwargs):
        """Returns the result of access_control_captive_portals_admin_click_add_button_save_login_config."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CAPTIVE_PORTALS_ADMIN_CLICK_ADD_BUTTON_SAVE_LOGIN_CONFIG,
                                    **kwargs)

    def access_control_captive_portals_admin_click_save_button_save_login_config(self, element_name, **kwargs):
        """Returns the result of access_control_captive_portals_admin_click_save_button_save_login_config."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CAPTIVE_PORTALS_ADMIN_CLICK_SAVE_BUTTON_SAVE_LOGIN_CONFIG,
                                    **kwargs)

    def access_control_captive_portals_admin_fill_mandatory_user_info_on_edit_user_window(self, element_name,
                                                                                          display_name, user_name,
                                                                                          password, verify_password,
                                                                                          **kwargs):
        """Returns the result of access_control_captive_portals_admin_fill_mandatory_user_info_on_edit_user_window."""
        args = {"display_name": display_name,
                "user_name": user_name,
                "password": password,
                "verify_password": verify_password}

        return self.execute_keyword(element_name, args, self.command_const.
                                    CAPTIVE_PORTALS_ADMIN_FILL_MANDATORY_USER_INFO_ON_EDIT_USER_WINDOW, **kwargs)

    def access_control_captive_portals_admin_fill_optional_user_info_on_edit_user_window(self, element_name, first_name,
                                                                                         last_name, description,
                                                                                         **kwargs):
        """Returns the result of access_control_captive_portals_admin_fill_optional_user_info_on_edit_user_window."""
        args = {"first_name": first_name,
                "last_name": last_name,
                "description": description}

        return self.execute_keyword(element_name, args, self.command_const.
                                    CAPTIVE_PORTALS_ADMIN_FILL_OPTIONAL_USER_INFO_ON_EDIT_USER_WINDOW, **kwargs)

    def access_control_captive_portals_admin_click_ok_button_on_edit_user_window(self, element_name, **kwargs):
        """Returns the result of access_control_captive_portals_admin_click_ok_button_on_edit_user_window."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CAPTIVE_PORTALS_ADMIN_CLICK_OK_BUTTON_ON_EDIT_USER_WINDOW,
                                    **kwargs)
