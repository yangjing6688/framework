from common.WebElementHandler import *
from xiqse.defs.admin.options.AdminOptionsWebElementsDefinitions import *


class AdminOptionsWebElements(AdminOptionsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_save_options_button(self):
        """
        :return: Save button on the Administration> Options page
        """
        return self.weh.get_element(self.save_options_button)

    def get_confirm_save_warning_dialog(self):
        """
        :return: Save Warnings dialog on the Options page
        """
        return self.weh.get_element(self.save_warning_dialog)

    def get_confirm_save_yes_btn(self):
        """
        :return: Yes button in the Save Warnings dialog on the Options page
        """
        return self.weh.get_element(self.save_warning_yes_button)

    def get_restore_default_options_button(self):
        """
        :return: Restore Defaults button on the Administration> Options page
        """
        return self.weh.get_element(self.restore_default_options_button)

    def get_reset_options_button(self):
        """
        :return: Reset button on the Administration> Options page
        """
        return self.weh.get_element(self.reset_options_button)

    def get_site_engine_general_option(self):
        """
        :return: Site Engine - General option in the tree on the Administration> Options page
        """
        return self.weh.get_element(self.site_engine_general_option)

    def get_xiq_connection_option(self):
        """
        :return: XIQ Connection option in the tree on the Administration> Options page
        """
        return self.weh.get_element(self.xiq_connection_option)

    def get_xiq_connection_enable_sharing_checkbox(self):
        """
        :return: Enable Sharing check button on the Administration> Options page for the XIQ Connection option
        """
        return self.weh.get_element(self.xiq_connection_enable_sharing_checkbox)

    def get_xiqse_serial_number_label(self):
        """
        :return: XIQ-SE Serial Number label on the Administration> Options page for the XIQ Connection option
        """
        return self.weh.get_element(self.xiqse_serial_number_label)

    def get_web_server_option(self):
        """
        :return: Web Server option in the tree on the Administration> Options page
        """
        return self.weh.get_element(self.web_server_option)

    def get_web_server_session_timeout_value(self):
        """
        :return: Web Server HTTP Session Timeout value on the Administration> Options page
        """
        return self.weh.get_element(self.web_server_session_timeout_value)

    def get_web_server_session_timeout_units_dropdown(self):
        """
        :return: Web Server HTTP Session Timeout units dropdown on the Administration> Options page
        """
        return self.weh.get_element(self.web_server_session_timeout_units_dropdown)

    def get_device_tree_name_format_dropdown_trigger(self):
        """
        :return: Site Engine - General: Device Tree Name Format dropdown trigger arrow on the Administration> Options page
        """
        return self.weh.get_element(self.device_tree_name_format_dropdown_trigger)

    def get_device_tree_name_format_dropdown(self):
        """
        :return: Site Engine - General: Device Tree Name Format dropdown field on the Administration> Options page
        """
        return self.weh.get_element(self.device_tree_name_format_dropdown)
