from xiq.defs.RSWebElementsDefinitions import *
from common.WebElementHandler import WebElementHandler


class RSWebElements(RSWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    @staticmethod
    def get_displayed_element(elements):
        """
        :param elements:
        :return:
        """
        for el in elements:
            if el.is_displayed():
                return el

    def get_default_radius_server_group_select_button(self):
        return self.weh.get_element(self.default_radius_server_group_select_button)

    def get_default_radius_server_group_dialog_rsg_rows(self):
        return self.weh.get_elements(self.default_radius_server_group_dialog_rsg_rows)

    def get_default_radius_server_group_dialog_cancel_button(self):
        return self.weh.get_element(self.default_radius_server_group_dialog_cancel_button)

    def get_default_radius_server_group_dialog_rsg_row_checkbox(self, row):
        return self.weh.get_element(self.default_radius_server_group_dialog_rsg_row_checkbox, row)

    def get_default_radius_server_group_dialog_select_button(self):
        return self.weh.get_element(self.default_radius_server_group_dialog_select_button)

    def get_default_radius_server_group_add_button(self):
        """

        :return:
        """
        return self.weh.get_element(self.default_radius_server_group_add_button)

    def get_radius_server_group_name_field(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.config_radius_server_dialog_window)
        return self.weh.get_element(self.radius_server_group_name_field, parent)

    def get_external_radius_server(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.config_radius_server_dialog_window)
        return self.weh.get_element(self.external_radius_server, parent)

    def get_radius_server_list_rows(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.config_radius_server_dialog_window)
        sub_el = self.weh.get_element(self.radius_server_list, parent)
        return self.weh.get_elements(self.radius_server_list_rows, sub_el)

    def get_radius_server_list_row_select_checkbox(self, row):
        """

        :return:
        """
        return self.weh.get_element(self.radius_server_list_row_select_checkbox, row)

    def get_radius_server_save_radius_button(self):
        parent = self.weh.get_element(self.config_radius_server_dialog_window)
        return self.weh.get_element(self.radius_server_save_radius_button, parent)

    def get_radius_server_list_add_button(self):
        return self.weh.get_element(self.radius_server_list_add_button)

    def get_new_external_radius_server_name_field(self):
        return self.weh.get_element(self.new_external_radius_server_name_field)

    def get_new_external_radius_server_ip_host_select_drop_down(self):
        parent = self.weh.get_element(self.config_radius_server_dialog_window)
        return self.weh.get_element(self.new_external_radius_server_ip_host_select_drop_down, parent)

    def get_new_external_radius_server_ip_list_items(self):
        parent = self.weh.get_elements(self.popup_elment)[0]
        return self.weh.get_element(self.new_external_radius_server_ip_list_items, parent)

    def get_new_external_radius_server_ip_list_item(self, el):
        return self.weh.get_elements(self.new_external_radius_server_ip_list_item, el)

    def get_new_external_radius_server_ip_host_add_button(self):
        return self.weh.get_element(self.new_external_radius_server_ip_host_add_button)

    def get_new_external_radius_server_ip_host_select_items(self):
        parent = self.weh.get_elements(self.popup_elment)[1]
        return self.weh.get_elements(self.new_external_radius_server_ip_host_select_items, parent)

    def get_new_external_radius_server_host_name_field(self):
        return self.weh.get_element(self.new_external_radius_server_host_name_field)

    def get_new_external_radius_server_ip_address_field(self):
        return self.weh.get_element(self.new_external_radius_server_ip_address_field)

    def get_new_external_radius_server_save_ip_button(self):
        return self.weh.get_element(self.new_external_radius_server_save_ip_button)

    def get_external_radius_server_shared_secret_field(self):
        return self.weh.get_element(self.external_radius_server_shared_secret_field)

    def get_external_radius_server_save_button(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.config_radius_server_dialog_window)
        return self.weh.get_element(self.external_radius_server_save_button, parent)

    def get_extreme_networks_radius_server(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.config_radius_server_dialog_window)
        return self.weh.get_element(self.extreme_networks_radius_server, parent)

    def get_extreme_networks_radius_server_db_scroll_button(self):
        """
        :return:
        """
        return self.weh.get_element(self.extreme_networks_radius_server_db_scroll_button)

    def get_extreme_networks_radius_server_db_drop_down_items(self):
        """
        :return:
        """
        parent = self.weh.get_element(self.extreme_networks_radius_server_db_scroll_all_items)
        return self.weh.get_elements(self.extreme_networks_radius_server_db_item, parent)

    def get_extreme_networks_radius_server_list_rows(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.config_radius_server_dialog_window)
        sub_el = self.weh.get_element(self.extreme_networks_radius_server_list, parent)
        return self.weh.get_elements(self.extreme_networks_radius_server_list_rows, sub_el)

    def get_extreme_networks_radius_server_list_row_select_checkbox(self, row):
        """

        :return:
        """
        return self.weh.get_element(self.extreme_networks_radius_server_list_row_select_checkbox, row)

    def get_user_db_active_directory_checkbox(self):
        return self.weh.get_element(self.user_db_active_directory_checkbox)

    def get_user_db_local_database_checkbox(self):
        return self.weh.get_element(self.user_db_local_database_checkbox)

    def get_user_db_ldap_database_checkbox(self):
        return self.weh.get_element(self.user_db_ldap_checkbox)

    def get_extreme_networks_radius_server_aaa_name1(self):
        parent = self.weh.get_element(self.config_radius_server_dialog_window)
        sub_el = self.weh.get_element(self.new_extreme_networks_radius_server_field_parent, parent)
        return self.weh.get_element(self.new_extreme_networks_radius_server_field, sub_el)

    def get_extreme_networks_radius_server_aaa_name(self):
        return self.weh.get_element(self.new_extreme_networks_radius_server_field)

    def get_extreme_networks_radius_server_approved_clients_tab(self):
        return self.weh.get_element(self.extreme_networks_radius_server_approved_clients_tab)

    def get_extreme_networks_radius_server_ip_host_add_button(self):
        """

        :return:
        """
        elements = self.weh.get_elements(self.extreme_networks_radius_server_ip_host_add_button)
        return self.get_displayed_element(elements)

    def get_extreme_networks_radius_server_add_button(self):
        return self.weh.get_element(self.extreme_networks_radius_server_add_button)

    def get_extreme_networks_radius_server_select_button(self):
        return self.weh.get_element(self.extreme_networks_radius_server_select_button)

    def get_extreme_networks_radius_server_shared_secret_field(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.config_radius_server_dialog_window)
        return self.weh.get_element(self.extreme_networks_radius_server_shared_secret_field, parent)

    def get_extreme_networks_radius_server_shared_secret_field1(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.config_radius_server_dialog_window)
        return self.weh.get_element(self.extreme_networks_radius_server_shared_secret_field1, parent)

    def get_extreme_networks_device_as_radius_server_list_rows(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.config_radius_server_dialog_window)
        sub_el = self.weh.get_element(self.extreme_networks_device_as_radius_server_list, parent)
        return self.weh.get_elements(self.extreme_networks_device_as_radius_server_rows, sub_el)

    def get_extreme_networks_device_as_radius_server_list_row_select_checkbox(self, row):
        """

        :return:
        """
        return self.weh.get_element(self.extreme_networks_device_as_radius_server_row_select_checkbox, row)

    def get_extreme_networks_device_as_radius_server_list_add_button(self):
        return self.weh.get_element(self.extreme_networks_device_as_radius_server_list_add_button)

    def get_extreme_networks_device_as_radius_server_shared_secret_field(self):
        """

        :return:
        """
        elements = self.weh.get_elements(self.extreme_networks_device_as_radius_server_shared_secret_field)
        return self.get_displayed_element(elements)

    def get_extreme_networks_radius_server_select_db_button(self):
        """

        :return:
        """
        elements = self.weh.get_elements(self.extreme_networks_radius_server_select_db_button)
        return self.get_displayed_element(elements)

    def get_user_group_select_button1(self):
        """

        :return:
        """
        elements = self.weh.get_elements(self.user_group_select_button)
        for el in elements:
            if el.is_displayed():
                return el

    def get_user_group_select_button(self):
        return self.weh.get_element(self.extreme_networks_radius_server_select_db_button)

    def get_user_group_select_dialog_local_db_tab(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.user_group_dialog_window)
        return self.weh.get_elements(self.user_group_select_dialog_local_db_tab)

    def get_user_group_select_dialog_usergroup_rows(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.user_group_dialog_window)
        return self.weh.get_elements(self.user_group_select_dialog_usergroup_rows, parent)

    def get_user_group_dialog_cancel_button(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.user_group_dialog_window)
        return self.weh.get_element(self.user_group_dialog_cancel_button, parent)

    def get_usergroup_dialog_usergroup_row_checkbox(self, row):
        """

        :return:
        """
        return self.weh.get_element(self.usergroup_dialog_usergroup_row_checkbox, row)

    def get_usergroup_dialog_select_button(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.user_group_dialog_window)
        return self.weh.get_element(self.usergroup_dialog_select_button, parent)

    def get_radius_server_group_delete_button(self):
        """

        :return:
        """
        parent = self.weh.get_element(self.default_radius_server_group_dialog)
        return self.weh.get_element(self.radius_server_group_delete_button, parent)

    def get_radius_server_group_delete_confirm_button(self):
        return self.weh.get_element(self.radius_server_group_delete_confirm_button)

