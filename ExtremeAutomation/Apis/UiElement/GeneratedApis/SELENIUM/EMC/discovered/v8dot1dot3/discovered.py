from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.discovered.v8dot1dot2.discovered import Discovered as \
    DiscoveredBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Discovered(DiscoveredBase):
    def discovered_select_row_by_column_value(self, ui_cmd_obj, arg_dict):
        # Map the column name to the column attribute
        self.get_column_attribute(ui_cmd_obj, arg_dict['col_name'])
        col_attr = ui_cmd_obj.return_data

        if col_attr != "":
            # Look for the specified value
            ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                               '#networkTabPanel #networkDiscoveredTab '
                                                               '#DiscoveredDevicesGrid', '[0]', col_attr,
                                                               arg_dict['col_value'])
            if ui_cmd_obj.return_data is True:
                # The value was found
                self.ext_builder.click(ui_cmd_obj,
                                       '#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid tableview => '
                                       '.x-grid-cell-inner:textEquals(' + arg_dict['col_value'] + ')')
            else:
                ui_cmd_obj.error_state = True
                self.logger.log_info("\nCould not find a row with value '" + arg_dict['col_value'] + "' in column '" +
                                     arg_dict['col_name'] + "'\n")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_info("\nUnknown column '" + arg_dict['col_name'] + "'\n")

        return ui_cmd_obj

    def discovered_add_device_select_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel tab[text=" + str(arg_dict['tab_name']) + "] => .x-tab-inner")
        return ui_cmd_obj

    def discovered_add_device_set_system_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=sysName] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "deviceDetailsPanel textfield[name=sysName] => .x-form-text")
        return ui_cmd_obj

    def discovered_add_device_set_contact(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=sysContact] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "deviceDetailsPanel textfield[name=sysContact] => .x-form-text")
        return ui_cmd_obj

    def discovered_add_device_set_location(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=sysLocation] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "deviceDetailsPanel textfield[name=sysLocation] => .x-form-text")
        return ui_cmd_obj

    def discovered_add_device_set_admin_profile(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combobox[name=profileName] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=profileName].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        return ui_cmd_obj

    def discovered_add_device_set_topology_layer(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combobox[name=topologyRole] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=topologyRole].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        return ui_cmd_obj

    def discovered_add_device_set_default_site(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=defaultSiteId] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=defaultSiteId].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['site_name']) + ")")

        if StringUtils.string_to_boolean(arg_dict['import_site'])is True:
            self.ext_builder.click(ui_cmd_obj,
                                   "messagebox[title=Import Site Configuration] #yes => .x-btn-inner-blue-small")
        else:
            self.ext_builder.click(ui_cmd_obj,
                                   "messagebox[title=Import Site Configuration] #no => .x-btn-inner-default-small")

        return ui_cmd_obj

    def discovered_add_device_set_poll_group(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combobox[name=pollGroup] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=pollGroup].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        return ui_cmd_obj

    def discovered_add_device_set_poll_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combobox[name=pollType] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=pollType].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        return ui_cmd_obj

    def discovered_add_device_set_snmp_timeout(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel numberfield[name=snmpTimeout] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "deviceDetailsPanel numberfield[name=snmpTimeout] => .x-form-text")
        return ui_cmd_obj

    def discovered_add_device_set_snmp_retries(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel numberfield[name=snmpRetry] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "deviceDetailsPanel numberfield[name=snmpRetry] => .x-form-text")
        return ui_cmd_obj

    def discovered_add_device_click_add(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[actionId=addDiscoverDevices] => .x-btn-button")
        return ui_cmd_obj

    def discovered_add_device_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[actionId=editDeviceCloseWindow] => .x-btn-button")
        return ui_cmd_obj

    def discovered_edit_device_set_default_site(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=defaultSiteId] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=defaultSiteId].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['site_name']) + ")")

        if str(arg_dict['import_site']) == "True" or str(arg_dict['import_site']) == "Yes":
            self.ext_builder.click(ui_cmd_obj,
                                   "messagebox[title=Import Site Configuration] #yes => .x-btn-inner-blue-small")
        else:
            self.ext_builder.click(ui_cmd_obj,
                                   "messagebox[title=Import Site Configuration] #no => .x-btn-inner-default-small")

        return ui_cmd_obj

    def discovered_edit_device_vlan_definition_set_always_write_to_devices(self, ui_cmd_obj, arg_dict):
        # This is no longer supported in version 8.1.3. Returns not supported.
        ui_cmd_obj.not_supported = True

        return ui_cmd_obj

    # HELPER METHODS

    def get_column_attribute(self, ui_cmd_obj, col_name):
        ui_cmd_obj.return_data = ""

        if col_name == "Connector":
            ui_cmd_obj.return_data = "connector"
        elif col_name == "Details":
            ui_cmd_obj.return_data = "details"
        elif col_name == "Type":
            ui_cmd_obj.return_data = "deviceType"
        elif col_name == "Firmware":
            ui_cmd_obj.return_data = "firmware"
        elif col_name == "First Seen":
            ui_cmd_obj.return_data = "firstSeenTime"
        elif col_name == "IP Address":
            ui_cmd_obj.return_data = "ipAddress"
        elif col_name == "Last Seen":
            ui_cmd_obj.return_data = "lastSeenTime"
        elif col_name == "Profile":
            ui_cmd_obj.return_data = "profileName"
        elif col_name == "Serial Number":
            ui_cmd_obj.return_data = "serialnumber"
        elif col_name == "Site Path":
            ui_cmd_obj.return_data = "sitePath"
        elif col_name == "Source":
            ui_cmd_obj.return_data = "source"
        elif col_name == "Status":
            ui_cmd_obj.return_data = "status"
        elif col_name == "System Description":
            ui_cmd_obj.return_data = "sysDescr"
        elif col_name == "Object ID":
            ui_cmd_obj.return_data = "sysObjectId"

        return ui_cmd_obj
