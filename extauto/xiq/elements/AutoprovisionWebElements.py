from extauto.xiq.defs.APPElementDefs import *
from extauto.common.WebElementHandler import *


class AutoprovisionWebElements(APPElementDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_auto_provisioning_button(self):
        return self.weh.get_element(self.auto_provisioning_button)

    def get_auto_provisioning_add_button(self):
        return self.weh.get_element(self.auto_provisioning_add_button)

    def get_auto_provisioning_edit_button(self):
        return self.weh.get_element(self. auto_provisioning_edit_button)

    def get_auto_provisioning_name(self):
        return self.weh.get_element(self.auto_provisioning_name)

    def get_auto_provision_desc(self):
        return self.weh.get_element(self.auto_provisioning_desc)

    def get_auto_provision_serial(self):
        return self.weh.get_element(self.auto_provisioning_serial)

    def get_auto_provision_serial_assign_devices_list(self):
        return self.weh.get_element(self.auto_provisioning_serial_assign_devices_list)

    def get_auto_provision_serial_assign_devices_select_all(self):
        return self.weh.get_element(self.auto_provisioning_serial_assign_devices_select_all)

    def get_auto_provision_serial_assign_devices_select_few(self):
        return self.weh.get_element(self.auto_provisioning_serial_assign_devices_select_few)

    def get_auto_provision_serial_assign_devices_deselect_all(self):
        return self.weh.get_element(self.auto_provisioning_serial_assign_devices_deselect_all)

    def get_auto_provision_serial_assign_devices_deselect_few(self):
        return self.weh.get_element(self.auto_provisioning_serial_assign_devices_deselect_few)

    def get_auto_provision_serial_assign_devices_manual_enter(self):
        return self.weh.get_element(self.auto_provisioning_serial_assign_devices_manual_enter)

    def get_auto_provisioning_IP(self):
        return self.weh.get_element(self.auto_provisioning_IP)

    def get_auto_provisioning_ip_cancel_button(self):
        return self.weh.get_element(self.auto_provisioning_ip_cancel_button)

    def get_auto_provisioning_ip_save_button(self):
        return self.weh.get_element(self.auto_provisioning_ip_save_button)

    def get_auto_provisioning_network_policy(self):
        return self.weh.get_element(self.auto_provisioning_network_policy_dropdown)

    def get_auto_provisioning_network_policy_list(self):
        return self.weh.get_elements(self. auto_provisioning_network_policy_list)

    def get_auto_provisioning_device_function(self):
        return self.weh.get_element(self.auto_provisioning_device_function_dropdown)

    def get_auto_provisioning_device_function_list(self):
        return self.weh.get_elements(self.auto_provisioning_device_function_list)

    def get_auto_provisioning_device_model(self):
        return self.weh.get_element(self.auto_provisioning_device_model_dropdown)

    def get_auto_provisioning_device_model_dropdown_list(self):
        return self.weh.get_elements(self.auto_provisioning_device_model_dropdown_list)

    def get_auto_provisioning_device_model_dropdown_list_SR22_23(self):
        return self.weh.get_elements(self.auto_provisioning_device_model_dropdown_list_SR22_23)

    def get_auto_provisioning_device_model_dropdown_switch_SR22_23(self):
        return self.weh.get_element(self.auto_provisioning_device_model_dropdown_switch_SR22_23)

    def get_auto_provisioning_device_model_dropdown_switch_SR20_21(self):
        return self.weh.get_element(self.auto_provisioning_device_model_dropdown_switch_SR20_21)

    def get_auto_provisioning_device_model_dropdown_switch_dell(self):
        return self.weh.get_element(self.auto_provisioning_device_model_dropdown_switch_dell)

    def get_auto_provisioning_country_code(self):
        return self.weh.get_element(self.auto_provisioning_country_code_dropdown)

    def get_auto_provisioning_country_code_list(self):
        return self.weh.get_elements(self.auto_provisioning_country_code_list)

    def get_auto_provisioning_assign_location_button(self):
        return self.weh.get_element(self.auto_provisioning_assign_location_button)

    def get_auto_provisioning_assign_location_search_box(self):
        return self.weh.get_element(self.auto_provisioning_assign_location_search_box)

    def get_auto_provisioning_assign_location_select_button(self):
        return self.weh.get_element(self.auto_provisioning_assign_location_select_button)

    def get_auto_provisioning_assign_location_cancel_button(self):
        return self.weh.get_element(self.auto_provisioning_assign_location_cancel_button)

    def get_auto_provisioning_loation_ip_subnet_add_button(self):
        return self.weh.get_element(self.auto_provisioning_loation_ip_subnet_add_button)

    def get_auto_provisioning_loation_ip_subnet_delete_button(self):
        return self.weh.get_element(self.auto_provisioning_loation_ip_subnet_delete_button)

    def get_auto_provisioning_enable_upload_auth(self):
        return self.weh.get_element(self.auto_provisioning_enable_Upload_Auth)

    def get_auto_provisioning_enable_Upload_Auto(self):
        return self.weh.get_element(self.auto_provisioning_enable_Upload_Auto)

    def get_auto_provisioning_Upload_Auth_golden_version(self):
        return self.weh.get_element(self.auto_provisioning_Upload_Auth_golden_version)

    def get_auto_provisioning_Upload_Auth_latest_version(self):
        return self.weh.get_element(self.auto_provisioning_Upload_Auth_latest_version)

    def get_auto_provisioning_enable_Reboot(self):
        return self.weh.get_element(self.auto_provisioning_enable_Reboot)

    def get_auto_provisioning_enable_device_credential(self):
        return self.weh.get_element(self.auto_provisioning_enable_Credential)

    def get_app_device_credential_root_admin_name(self):
        return self.weh.get_element(self.auto_provisioning_device_credential_root_admin_name)

    def get_app_device_credential_root_admin_password(self):
        return self.weh.get_element(self.auto_provisioning_device_credential_root_admin_password)

    def get_app_device_credential_readonly_admin_name(self):
        return self.weh.get_element(self.auto_provisioning_device_credential_readonly_admin_name)

    def get_app_device_credential_readonly_admin_password(self):
        return self.weh.get_element(self.auto_provisioning_device_credential_readonly_admin_password)

    def get_auto_provisioning_enable_Capwap(self):
        return self.weh.get_element(self.auto_provisioning_enableCapwap)

    def get_app_capwap_primary_server_input(self):
        return self.weh.get_element(self.auto_provisioning_capwap_primary_server_input)

    def get_auto_provisioning_capwap_primary_server_add(self):
        return self.weh.get_element(self.auto_provisioning_capwap_primary_server_add)

    def get_app_capwap_add_ip_addr(self):
        return self.weh.get_element(self.uto_provisioning_capwap_add_ip_addr)

    def get_app_capwap_add_hostname(self):
        return self.weh.get_element(self.auto_provisioning_capwap_add_hostname)

    def get_app_capwap_add_ip_name(self):
        return self.weh.get_element(self.auto_provisioning_capwap_add_ip_name)

    def get_app_capwap_add_ip_IPaddr(self):
        return self.weh.get_element(self.auto_provisioning_capwap_add_ip_IPaddr)

    def get_app_capwap_add_cancel_button(self):
        return self.weh.get_element(self.auto_provisioning_capwap_add_cancel_button)

    def get_app_capwap_add_save_button(self):
        return self.weh.get_element(self.auto_provisioning_capwap_add_save_button)

    def get_app_capwap_add_hostname_name(self):
        return self.weh.get_element(self.auto_provisioning_capwap_add_hostname_name)

    def get_app_capwap_add_hostname_hostname(self):
        return self.weh.get_element(self.auto_provisioning_capwap_add_hostname_hostname)

    def get_auto_provisioning_capwap_primary_server_edit(self):
        return self.weh.get_element(self.auto_provisioning_capwap_primary_server_edit)

    def get_auto_provisioning_capwap_backup_server_input(self):
        return self.weh.get_element(self.auto_provisioning_capwap_backup_server_input)

    def get_auto_provisioning_capwap_backup_server_add(self):
        return self.weh.get_element(self.auto_provisioning_capwap_backup_server_add)

    def get_auto_provisioning_capwap_backup_server_edit(self):
        return self.weh.get_element(self.auto_provisioning_capwap_backup_server_edit)

    def get_app_capwap_shared_key_passphrase(self):
        return self.weh.get_element(self.auto_provisioning_capwap_shared_key_passphrase)

    def get_auto_provisioning_save_button(self):
        return self.weh.get_element(self.auto_provisioning_save_button)

    def get_auto_provisioning_cancel_button(self):
        return self.weh.get_element(self.auto_provisioning_cancel_button)

    def get_auto_provision_grid_rows(self):
        grid = self.weh.get_element(self.auto_provision_grid)
        return self.weh.get_elements(self.auto_provision_grid_rows, parent=grid)

    def get_auto_provisioning_grid_header(self):
        return self.weh.get_element(self.auto_provisioning_grid_header)

    def get_auto_provision_enable(self, row):
        return self.weh.get_element(self.auto_provision_enable, parent=row)

    def get_common_object_grid_row_cells(self, row, field='ace-switch ace-switch-7 J-item-enable'):
        cells = self.weh.get_elements(self.common_object_grid_row_cells, row)
        for cell in cells:
            if field in cell.get_attribute("class"):
                return cell

    def get_auto_provisioning_check_box(self, row=None):
        return self.weh.get_element(self.auto_provisioning_check_box, parent=row)

    def get_auto_provisioning_alert_yes(self):
        return self.weh.get_element(self.auto_provisioning_alert_yes)

    def get_auto_provisioning_delete_button(self):
        return self.weh.get_element(self.auto_provisioning_delete_button)

    def get_auto_provisioning_select_all_check_box(self):
        return self.weh.get_element(self.auto_provisioning_select_all_check_box)