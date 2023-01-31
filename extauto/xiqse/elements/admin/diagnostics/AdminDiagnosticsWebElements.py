from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.admin.diagnostics.AdminDiagnosticsWebElementsDefinitions import AdminDiagnosticsWebElementsDefinitions


class AdminDiagnosticsWebElements(AdminDiagnosticsWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_level_dropdown(self):
        """
        :return: Gets the Level dropdown on the Administration> Diagnostics page
        """
        return self.weh.get_element(self.level_dropdown)

    def get_level_advanced_choice(self):
        """
        :return: Gets the "Advanced" choice from the Level dropdown on the Administration> Diagnostics page
        """
        return self.weh.get_element(self.level_advanced_choice)

    def get_level_basic_choice(self):
        """
        :return: Gets the "Basic" choice from the Level dropdown on the Administration> Diagnostics page
        """
        return self.weh.get_element(self.level_basic_choice)

    def get_level_diagnostic_choice(self):
        """
        :return: Gets the "Diagnostic" choice from the Level dropdown on the Administration> Diagnostics page
        """
        return self.weh.get_element(self.level_diagnostic_choice)

    def get_server_tree_node(self):
        """
        :return: 'Server' tree node on the Administration> Diagnostics page
        """
        return self.weh.get_element(self.server_tree_node)

    def get_server_tree_node_collapsed(self):
        """
        :return: Collapsed 'Server' tree node on the Administration> Diagnostics page
        """
        return self.weh.get_element(self.server_tree_node_collapsed)

    def get_server_tree_node_expanded(self):
        """
        :return: Expanded 'Server' tree node on the Administration> Diagnostics page
        """
        return self.weh.get_element(self.server_tree_node_expanded)

    def get_server_log_tree_node(self):
        """
        :return: 'Server Log' tree node on the Administration> Diagnostics page under the Server node
        """
        return self.weh.get_element(self.server_log_tree_node)

    def get_server_log_panel_title(self):
        """
        :return: 'Server Log' panel title on the Administration> Diagnostics page under the Server node
        """
        return self.weh.get_element(self.server_log_panel_title)

    def get_server_log_clear_button(self):
        """
        :return: 'Clear' button in the Server Log view on the Administration> Diagnostics page
        """
        return self.weh.get_element(self.server_log_clear_button)

    def get_server_log_refresh_button(self):
        """
        :return: 'Refresh' button in the Server Log view on the Administration> Diagnostics page
        """
        return self.weh.get_element(self.server_log_refresh_button)

    def get_server_log_contents(self):
        """
        :return: Contents of the Server Log view on the Administration> Diagnostics page
        """
        return self.weh.get_element(self.server_log_contents)

    def get_system_tree_node(self):
        """
        :return: 'System' tree node on the Administration> Diagnostics page
        """
        return self.weh.get_element(self.system_tree_node)

    def get_system_tree_node_collapsed(self):
        """
        :return: Collapsed 'System' tree node on the Administration> Diagnostics page
        """
        return self.weh.get_element(self.system_tree_node_collapsed)

    def get_system_tree_node_expanded(self):
        """
        :return: Expanded 'System' tree node on the Administration> Diagnostics page
        """
        return self.weh.get_element(self.system_tree_node_expanded)

    def get_xiq_device_message_details_tree_node(self):
        """
        :return: 'XIQ Device Message Details' tree node on the Administration> Diagnostics page under the System node
        """
        return self.weh.get_element(self.xiq_device_message_details_tree_node)

    def get_xiq_device_message_details_ip_address_column_header(self):
        """
        :return: 'IP Address' column header on the Administration> Diagnostics> System> XIQ Device Message Details page
        """
        return self.weh.get_element(self.xiq_device_message_details_ip_address_column_header)

    def get_xiq_device_message_details_title(self):
        """
        :return: Title of the Administration> Diagnostics> System> XIQ Device Message Details page
        """
        return self.weh.get_element(self.xiq_device_message_details_title)

    def get_xiq_device_message_details_table_rows(self):
        """
        :return: All the rows in the XIQ Device Message Details table
        """
        return self.weh.get_elements(self.xiq_device_message_details_table_rows)

    def get_xiq_device_message_details_last_update_time_col(self):
        """
        :return: Last Update Time column in the XIQ Device Message Details table
        """
        return self.weh.get_element(self.xiq_device_message_details_last_update_time_col)

    def get_xiq_device_message_details_onboard_status_col(self):
        """
        :return: Onboard Status column's ID in the XIQ Device Message Details table
        """
        return self.weh.get_element(self.xiq_device_message_details_onboard_status_col)

    def get_xiq_device_message_details_column(self, col_id, row):
        """
        :param col_id:  identifier of the column to retrieve
        :param row:     row to obtain the data for
        :return: Column value for the specified column ID and row in the XIQ Device Message Details table
        """
        return self.weh.get_template_element(self.xiq_device_message_details_column, parent=row, element_id=col_id)

    def get_xiq_device_message_details_refresh_button(self):
        """
        :return: Refresh button for the XIQ Device Message Details table
        """
        return self.weh.get_element(self.xiq_device_message_details_refresh_button)

    def get_xiq_device_message_details_displaying_rows_label(self):
        """
        :return: "Displaying ## rows" label for the XIQ Device Message Details table
        """
        return self.weh.get_element(self.xiq_device_message_details_displaying_rows_label)

    def get_xiq_device_message_details_search_button(self):
        """
        :return: Search button for the XIQ Device Message Details table when the search box is closed;
                 this button opens the search panel
        """
        return self.weh.get_element(self.xiq_device_message_details_search_button)

    def get_xiq_device_message_details_search_text_field(self):
        """
        :return: Search text field for the XIQ Device Message Details table
        """
        return self.weh.get_element(self.xiq_device_message_details_search_text_field)

    def get_xiq_device_message_details_perform_search_button(self):
        """
        :return: Search button for the XIQ Device Message Details table when the search box is expanded;
                 this button initiates the search
        """
        return self.weh.get_element(self.xiq_device_message_details_perform_search_button)

    def get_xiq_device_message_details_search_clear_button(self):
        """
        :return: Clear button for the search field in the XIQ Device Message Details table
        """
        return self.weh.get_element(self.xiq_device_message_details_search_clear_button)

    def get_xiq_device_message_details_show_xiq_messages_button(self):
        """
        :return: Show XIQ Messages button for the XIQ Device Message Details table
        """
        return self.weh.get_element(self.xiq_device_message_details_show_xiq_messages_button)

    def get_show_xiq_messages_dialog_title(self):
        """
        :return: Title of the 'Show XIQ Messages' dialog
        """
        return self.weh.get_element(self.show_xiq_messages_dialog_title)

    def get_show_xiq_messages_dialog_content(self):
        """
        :return: Content of the 'Show XIQ Messages' dialog
        """
        return self.weh.get_element(self.show_xiq_messages_dialog_content)

    def get_show_xiq_messages_dialog_close_button(self):
        """
        :return: Close button for the 'Show XIQ Messages' dialog
        """
        return self.weh.get_element(self.show_xiq_messages_dialog_close_button)

    def get_xiq_device_message_details_auto_onboard_xiqse_button(self):
        """
        :return: Auto Onboard XIQ-SE button in the XIQ Device Message Details view
        """
        return self.weh.get_element(self.xiq_device_message_details_auto_onboard_xiqse_button)

    def get_auto_onboard_xiqse_dialog_title(self):
        """
        :return: 'Auto Onboard XIQ-SE to XIQ' dialog's title
        """
        return self.weh.get_element(self.auto_onboard_xiqse_dialog_title)

    def get_auto_onboard_xiqse_dialog_email_field(self):
        """
        :return: 'Auto Onboard XIQ-SE to XIQ' dialog's email field
        """
        return self.weh.get_element(self.auto_onboard_xiqse_dialog_email_field)

    def get_auto_onboard_xiqse_dialog_password_field(self):
        """
        :return: 'Auto Onboard XIQ-SE to XIQ' dialog's password field
        """
        return self.weh.get_element(self.auto_onboard_xiqse_dialog_password_field)

    def get_auto_onboard_xiqse_dialog_submit_button(self):
        """
        :return: 'Auto Onboard XIQ-SE to XIQ' dialog's submit button
        """
        return self.weh.get_element(self.auto_onboard_xiqse_dialog_submit_button)

    def get_auto_onboard_xiqse_dialog_confirm_ok(self):
        """
        :return: OK button in the confirmation dialog for 'Auto Onboard XIQ-SE to XIQ'
        """
        return self.weh.get_element(self.auto_onboard_xiqse_dialog_confirm_ok)

    def get_auto_onboard_xiqse_dialog_confirm_cancel(self):
        """
        :return: Cancel button in the confirmation dialog for 'Auto Onboard XIQ-SE to XIQ'
        """
        return self.weh.get_element(self.auto_onboard_xiqse_dialog_confirm_cancel)
