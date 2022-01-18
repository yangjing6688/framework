from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XCA.XcaportalConstants import XcaportalConstants
from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass


class UiXcaPortalKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiXcaPortalKeywords, self).__init__()
        self.api_const = self.constants.API_XCA_PORTALS
        self.command_const = XcaportalConstants()

    def portal_click_add_to_create_new_portal(self, element_names, **kwargs):
        """Returns the result of portal_click_add_to_create_new_portal."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CLICK_ADD_TO_CREATE_NEW_PORTAL, **kwargs)

    def portal_click_portal_name_to_open_portal_settings(self, element_names, portal_name, **kwargs):
        """Returns the result of portal_click_portal_name_to_open_portal_settings."""
        args = {"portal_name": portal_name}

        return self.execute_keyword(element_names, args, self.command_const.CLICK_PORTAL_NAME_TO_OPEN_PORTAL_SETTINGS,
                                    **kwargs)

    def portal_set_portal_name(self, element_names, portal_name, **kwargs):
        """Returns the result of portal_set_portal_name."""
        args = {"portal_name": portal_name}

        return self.execute_keyword(element_names, args, self.command_const.SET_PORTAL_NAME, **kwargs)

    def portal_select_guest_portal(self, element_names, guest_portal, **kwargs):
        """Returns the result of portal_select_guest_portal."""
        args = {"guest_portal": guest_portal}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_GUEST_PORTAL, **kwargs)

    def portal_select_authenticated_portal(self, element_names, authenticated_portal, **kwargs):
        """Returns the result of portal_select_authenticated_portal."""
        args = {"authenticated_portal": authenticated_portal}

        return self.execute_keyword(element_names, args, self.command_const.SELECT_AUTHENTICATED_PORTAL, **kwargs)

    def portal_click_portal_configurations_tab(self, element_names, **kwargs):
        """Returns the result of portal_click_portal_configurations_tab."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CLICK_PORTAL_CONFIGURATIONS_TAB, **kwargs)

    def portal_click_network_settings_tab(self, element_names, **kwargs):
        """Returns the result of portal_click_network_settings_tab."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CLICK_NETWORK_SETTINGS_TAB, **kwargs)

    def portal_click_administration_tab(self, element_names, **kwargs):
        """Returns the result of portal_click_administration_tab."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CLICK_ADMINISTRATION_TAB, **kwargs)

    def portal_config_portal_network_settings(self, element_names, toggle_use_mobile_captive_portal,
                                              toggle_display_welcome_page, test_image_url, redirection, destination,
                                              **kwargs):
        """Returns the result of portal_config_portal_network_settings."""
        args = {"toggle_use_mobile_captive_portal": toggle_use_mobile_captive_portal,
                "toggle_display_welcome_page": toggle_display_welcome_page,
                "test_image_url": test_image_url,
                "redirection": redirection,
                "destination": destination}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_PORTAL_NETWORK_SETTINGS, **kwargs)

    def portal_delete_existing_portal(self, element_names, portal_name, **kwargs):
        """Returns the result of portal_delete_existing_portal."""
        args = {"portal_name": portal_name}

        return self.execute_keyword(element_names, args, self.command_const.DELETE_EXISTING_PORTAL, **kwargs)

    def portal_save_config_and_back_to_portal_page(self, element_names, **kwargs):
        """Returns the result of portal_save_config_and_back_to_portal_page."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SAVE_CONFIG_AND_BACK_TO_PORTAL_PAGE,
                                    **kwargs)

    def portal_verify_portal_exists(self, element_names, portal_name, **kwargs):
        """Returns the result of portal_verify_portal_exists."""
        args = {"portal_name": portal_name}

        return self.execute_keyword(element_names, args, self.command_const.VERIFY_PORTAL_EXISTS, **kwargs)

    def portal_verify_portal_does_not_exist(self, element_names, portal_name, **kwargs):
        """Returns the result of portal_verify_portal_does_not_exist."""
        args = {"portal_name": portal_name}

        return self.execute_keyword(element_names, args, self.command_const.VERIFY_PORTAL_DOES_NOT_EXIST, **kwargs)
