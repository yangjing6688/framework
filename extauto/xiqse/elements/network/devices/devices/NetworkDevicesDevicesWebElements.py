from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.network.devices.devices.NetworkDevicesDevicesWebElementsDefinitions import NetworkDevicesDevicesWebElementsDefinitions


class NetworkDevicesDevicesWebElements(NetworkDevicesDevicesWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_devices_table(self):
        """
        :return: The devices table
        """
        return self.weh.get_element(self.devices_table)

    def get_table_rows(self):
        """
        :return: All the rows in the devices table
        """
        return self.weh.get_elements(self.devices_table_rows)

    def get_device_menu_tb_button(self):
        """
        :return: Device menu toolbar button
        """
        return self.weh.get_element(self.device_menu_tb_button)

    def get_add_device_tb_button(self):
        """
        :return: "Add Device..." toolbar button
        """
        return self.weh.get_element(self.add_device_tb_button)

    def get_more_actions_menu_item(self):
        """
        :return: 'More Actions' menu item under the Devices Menu toolbar button
        """
        return self.weh.get_element(self.more_actions_menu_item)

    def get_delete_device_menu_item(self):
        """
        :return: 'Delete Device' menu item under the More Actions menu of the Devices Menu toolbar button
        """
        return self.weh.get_element(self.delete_device_menu_item)

    def get_set_device_profile_menu_item(self):
        """
        :return: 'Set Device Profile...' menu item under the More Actions menu of the Devices Menu toolbar button
        """
        return self.weh.get_element(self.set_device_profile_menu_item)

    def get_configure_menu_item(self):
        """
        :return: 'Configure...' menu item under the Devices Menu toolbar button
        """
        return self.weh.get_element(self.configure_menu_item)

    def get_upgrade_firmware_menu_item(self):
        """
        :return: 'Upgrade Firmware...' menu item under the Devices Menu toolbar button
        """
        return self.weh.get_element(self.upgrade_firmware_menu_item)

    def get_devices_status_column_header(self):
        """
        :return: 'Status' column header of the Devices table
        """
        return self.weh.get_element(self.devices_table_status_column_header)

    def get_device_status_cell_value(self, row):
        """
        :param row: row to return the data for
        :return: 'Status' cell for the specified row in the Devices table
        """
        el = self.weh.get_element(self.devices_table_status_cell, row)
        if el:
            return el.get_attribute("data-qtip")
        else:
            return None

    def get_device_column_by_name(self, col_name):
        """
        :param col_name: name of the column to return
        :return: Column for the specified column name in the Devices table, else -1
        """
        return self.weh.get_template_element(self.devices_table_column_by_name, element_name=col_name)

    def get_device_column_value(self, col_id, row):
        """
        :param col_id: ID of the column to return the value of
        :param row:    row to return the value for
        :return: Column value for the specified column id of the specified row in the Devices table
        """
        return self.weh.get_template_element(self.devices_table_column_value, parent=row, element_id=col_id)

    def get_table_displaying_label(self):
        """
        :return: 'Displaying X - Y of Z' label for the table
        """
        return self.weh.get_element(self.table_displaying_label)

    def get_table_row_at_index(self, row_index):
        """
        :param row_index:  index of row to return (0-based)
        :return:           table row at specified index
        """
        return self.weh.get_template_element(self.devices_table_row_by_index, element_index=row_index)

    def get_archives_menu_item(self):
        """
        :return: 'Archives' menu item under the Devices Menu toolbar button
        """
        return self.weh.get_element(self.archives_menu_item)

    def get_backup_configuration_menu_item(self):
        """
        :return: 'Backup Configuration' menu item under the Archives menu of the Devices Menu toolbar button
        """
        return self.weh.get_element(self.backup_configuration_menu_item)

    def get_restore_configuration_menu_item(self):
        """
        :return: 'Restore Configuration' menu item under the Archives menu of the Devices Menu toolbar button
        """
        return self.weh.get_element(self.restore_configuration_menu_item)

    def get_rediscover_device_menu_item(self):
        """
        :return: 'Rediscover Device' menu item under the Devices Menu toolbar button
        """
        return self.weh.get_element(self.rediscover_device_menu_item)

    def get_rediscover_confirm_button_yes_item(self):
        """
        :return: 'Rediscover Device' confirmation dialog Yes button
        """
        return self.weh.get_element(self.rediscover_device_confirmation_item)

    def get_restart_device_menu_item(self):
        """
        :return: 'Restart Device' menu item under the More Actions menu of the Devices Menu toolbar button
        """
        return self.weh.get_element(self.restart_device_menu_item)

    def get_register_trap_receiver_menu_item(self):
        """
        :return: 'Register Trap Receiver' menu item under the More Actions menu of the Devices Menu toolbar button
        """
        return self.weh.get_element(self.register_trap_receiver_menu_item)

    def get_unregister_trap_receiver_menu_item(self):
        """
        :return: 'Unregister Trap Receiver' menu item under the More Actions menu of the Devices Menu toolbar button
        """
        return self.weh.get_element(self.unregister_trap_receiver_menu_item)

    def get_register_syslog_receiver_menu_item(self):
        """
        :return: 'Register Syslog Receiver' menu item under the More Actions menu of the Devices Menu toolbar button
        """
        return self.weh.get_element(self.register_syslog_receiver_menu_item)

    def get_unregister_syslog_receiver_menu_item(self):
        """
        :return: 'Unregister Syslog Receiver' menu item under the More Actions menu of the Devices Menu toolbar button
        """
        return self.weh.get_element(self.unregister_syslog_receiver_menu_item)

    def get_search_open_button(self):
        """
        :return: Button to open the Search panel on the Network> Devices page
        """
        return self.weh.get_element(self.search_open_button)

    def get_search_text_field(self):
        """
        :return: Search field on the Network> Devices page
        """
        return self.weh.get_element(self.search_text_field)

    def get_search_trigger_button(self):
        """
        :return: Button to perform the Search on the Network> Devices page
        """
        return self.weh.get_element(self.search_trigger_button)

    def get_search_clear_button(self):
        """
        :return: Button to clear the Search field on the Network> Devices page
        """
        return self.weh.get_element(self.search_clear_button)
