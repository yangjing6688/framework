from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.admin.options.AdminOptionsWebElementsDefinitions import AdminOptionsWebElementsDefinitions


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

    def get_alarm_event_option(self):
        """
        :return: Alarm/Event Logs and Tables option in the tree on the Administration> Options page
        """
        return self.weh.get_element(self.alarm_event_option)

    def get_alarm_event_search_scope_client_checkbox(self):
        """
        :return: Event Search Scope Client checkbox on the Administration> Options page
        """
        return self.weh.get_element(self.event_search_scope_client_checkbox)

    def get_alarm_event_search_scope_event_checkbox(self):
        """
        :return: Event Search Scope Event checkbox on the Administration> Options page
        """
        return self.weh.get_element(self.event_search_scope_event_checkbox)

    def get_alarm_event_search_scope_source_host_name_checkbox(self):
        """
        :return: Event Search Scope Source Host Name checkbox on the Administration> Options page
        """
        return self.weh.get_element(self.event_search_scope_source_host_name_checkbox)

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

    def get_inventory_manager_option(self):
        """
        :return: Inventory Manager option in the tree on the Administration> Options page
        """
        return self.weh.get_element(self.inventory_manager_option)

    def get_scp_login_information_anonymous_checkbox(self):
        """
        :return: Anonymous check button on the Administration> Options> Inventory Manager> File Transfer> SCP Server Properties option
        """
        return self.weh.get_element(self.scp_login_information_anonymous_checkbox)

    def get_scp_login_information_username(self):
        """
        :return: The 'Username" field in the Administration> Options> Inventory Manager> File Transfer> SCP Server Properties> Username field
        """
        return self.weh.get_element(self.scp_login_information_username)

    def get_scp_login_information_password(self):
        """
        :return: The'Password" field in the Administration> Options> Inventory Manager> File Transfer> SCP Server Properties> Password field
        """
        return self.weh.get_element(self.scp_login_information_password)

    def get_sftp_login_information_anonymous_checkbox(self):
        """
        :return: Anonymous check button on the Administration> Options> Inventory Manager> File Transfer> SFTP Server Properties option
        """
        return self.weh.get_element(self.sftp_login_information_anonymous_checkbox)

    def get_sftp_login_information_username(self):
        """
        :return: The 'Username" field in the Administration> Options> Inventory Manager> File Transfer> SFTP Server Properties> Username field
        """
        return self.weh.get_element(self.sftp_login_information_username)

    def get_sftp_login_information_password(self):
        """
        :return: The'Password" field in the Administration> Options> Inventory Manager> File Transfer> SFTP Server Properties> Password field
        """
        return self.weh.get_element(self.sftp_login_information_password)

    def get_status_polling_option(self):
        """
        :return: Status Polling option in the tree on the Administration> Options page
        """
        return self.weh.get_element(self.status_polling_option)

    def get_status_polling_group_2_interval_value(self):
        """
        :return: Status Polling Group 2 Interval field on the Administration> Options page
        """
        return self.weh.get_element(self.status_polling_group_2_interval_value)

    def get_syslog_option(self):
        """
        :return: Syslog option in the tree on the Administration> Options page
        """
        return self.weh.get_element(self.syslog_option)

    def get_syslog_delay_engine_start_value(self):
        """
        :return: Syslog Delay Engine Start element in Admin-Options-Syslog
        """
        return self.weh.get_element(self.syslog_delay_engine_start_value)

    def get_trap_option(self):
        """
        :return: Trap option in the tree on the Administration> Options page
        """
        return self.weh.get_element(self.trap_option)

    def get_trap_delay_engine_start_value(self):
        """
        :return: Trap Delay Engine Start element in Admin-Options-Syslog
        """
        return self.weh.get_element(self.trap_delay_engine_start_value)
