from a3.defs.A3WebElementsDefs import *
from common.AutoActions import *
from common.WebElementHandler import *


class A3WebElements(A3WebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_grid_rows(self):
        """
        :return: all the rows in the a3 devices grid
        """
        grid_rows = self.weh.get_elements(self.a3_devices_page_grid_rows)
        rows = []
        for row in grid_rows:
            if row.is_displayed():
                rows.append(row)
        return rows

    def get_refresh_a3_devices_page(self):
        refresh_icon = self.weh.get_element(self.a3_devices_page_refresh_button)
        return refresh_icon

    def get_status_cell(self, row):
        el = self.weh.get_element(self.devices_a3_status_green, row)
        return el.get_attribute("class")

    def get_a3_device_row_cells(self):
        return self.weh.get_elements(self.a3_device_row_cells)

    def get_a3_device_expanded_status(self):
        return self.weh.get_element(self.a3_device_expanded_status)

    def get_a3_device_row_cells_with_row(self, row):
        """
        :return: device row cell elements
        """
        return self.weh.get_element(self.a3_device_row_cells, row)

    def get_a3_device_expanded_button(self, row):
        elements = self.weh.get_elements(self.a3_device_expanded_button, row)
        print(len(elements))
        for el in elements:
            if el.is_displayed():
                return el

    def get_a3_device_host_name_cell(self, row):
        return self.weh.get_element(self.a3_device_host_name_cell, parent=row)

    def get_a3_node_grid_rows(self):
        """
        :return: all the rows in the a3 devices grid
        """
        grid_rows = self.weh.get_elements(self.a3_nodes__grid_rows)
        rows = []
        for row in grid_rows:
            if row.is_displayed():
                rows.append(row)
        return rows

    def get_go_to_a3_button(self, row):
        elements = self.weh.get_elements(self.go_to_a3_button, row)
        print(len(elements))
        for el in elements:
            if el.is_displayed():
                return el

    def get_a3_login_username_field(self):
        return self.weh.get_element(self.a3_login_username_field)

    def get_a3_login_password_field(self):
        return self.weh.get_element(self.a3_login_password_field)

    def get_a3_login_button(self):
        return self.weh.get_element(self.a3_login_button)

    def get_a3_node_go_to_a3_button(self, row):
        elements = self.weh.get_elements(self.a3_node_go_to_a3_button, parent=row)
        print(len(elements))
        for el in elements:
            if el.is_displayed():
                return el

    def get_a3_unlink_page_text(self):
        return self.weh.get_element(self.a3_unlink_page_text)

    def select_auth_source_menu(self):
            return self.weh.get_element(self.auth_source_ui)

    def select_conn_profile_menu(self):
        return self.weh.get_element(self.conn_profile_menu)

    def select_device_ui(self):
        return self.weh.get_element(self.device_ui)

    def get_radius_audit_log_ui(self):
        return self.weh.get_element(self.radius_audit_log_ui)

    def get_clients_search_ui(self):
        return self.weh.get_element(self.clients_search_ui)

    def get_realms_ui(self):
        return self.weh.get_element(self.realm_ui)

    def get_conn_profile_test_ui(self):
        return self.weh.get_element(self.conn_profile_test)

    def get_policies_access_control(self):
        return self.weh.get_element(self.policies_tab)

    def get_roles(self):
        return self.weh.get_element(self.roles)

    def get_role_button(self):
        return self.weh.get_element(self.role_button)

    def get_ad_domains(self):
        return self.weh.get_element(self.ad_domain)

    def get_system_configuration(self):
        return self.weh.get_element(self.system_config_tab)

    def get_cloud(self):
        return self.weh.get_element(self.cloud_integration)

    def cloud_host(self):
        return self.weh.get_element(self.cloud_host_input)

    def get_ssh_option_ui(self):
        return self.weh.get_element(self.ssh_option_ui)

    def get_ssh_button(self):
        ssh_btn = self.weh.get_element(self.ssh_selector)
        return ssh_btn

    def get_ssh_duration(self):
        return self.weh.get_element(self.input_drop_down_options)

    def get_backup(self):
        return self.weh.get_element(self.backup_menu)

    def get_log_ui(self):
        return self.weh.get_element(self.log_ui)

    def get_auth_source_menu(self):
        return self.weh.get_element(self.auth_source_ui)



