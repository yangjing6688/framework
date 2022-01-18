from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as DiscoveredBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Discovered(DiscoveredBase):

    def click_clear_selected(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid '
                               'button[actionId=clearDiscoveredAction] => .x-btn-button')
        return ui_cmd_obj

    def discovered_select_device_in_table(self, ui_cmd_obj, arg_dict):
        # Look for the specified device
        ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                           '#networkTabPanel #networkDiscoveredTab '
                                                           '#DiscoveredDevicesGrid', '[0]', 'ipAddress',
                                                           arg_dict['device_ip'])
        if ui_cmd_obj.return_data is True:
            # The ipAddress was found
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid tableview => '
                                   '.x-grid-cell-inner:textEquals(' + arg_dict['device_ip'] + ')')
        else:
            # If the device wasn't found by the ipAddress attribute, check the connectedIpAddress attribute
            ui_cmd_obj = self.ext_builder.is_item_in_component(ui_cmd_obj,
                                                               '#networkTabPanel #networkDiscoveredTab '
                                                               '#DiscoveredDevicesGrid', '[0]', 'connectedIpAddress',
                                                               arg_dict['device_ip'])
            if ui_cmd_obj.return_data is True:
                # The IP will have an asterisk (*) appended if it is "connectedIpAddress"
                self.ext_builder.click(ui_cmd_obj,
                                       '#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid tableview => '
                                       '.x-grid-cell-inner:textEquals(' + arg_dict['device_ip'] + '*)')
            else:
                self.logger.log_info("\nCould not find a device with IP '" + arg_dict['device_ip'] + "'\n")

        return ui_cmd_obj

    def discovered_wait_for_device_add(self, ui_cmd_obj, arg_dict):
        self.ext_builder.wait_for_item_in_table(ui_cmd_obj,
                                                '#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid '
                                                'gridview', '[0]', 'connectedIpAddress', arg_dict['device_ip'], None,
                                                True, arg_dict['timeout'])
        return ui_cmd_obj

    def discovered_wait_for_device_remove(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid "
                               "button[iconCls=x-tbar-loading][tooltip=Refresh] => .x-btn-icon-el")
        return ui_cmd_obj

    def discovered_click_clear_selected(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid "
                               "button[actionId=clearDiscoveredAction] => .x-btn-button")
        return ui_cmd_obj

    def discovered_click_clear_all_devices(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid "
                               "button[actionId=clearAllProcessedAction] => .x-btn-button")
        return ui_cmd_obj

    def discovered_click_pre_register_device(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid "
                               "button[actionId=addPreApprovedDevicesAction] => .x-btn-button")
        return ui_cmd_obj

    def discovered_click_add_devices(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid "
                               "button[actionId=addDevicesAction] => .x-btn-button")
        return ui_cmd_obj

    def discovered_click_edit_devices(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid "
                               "button[actionId=editDevicesAction] => .x-btn-button")
        return ui_cmd_obj

    def discovered_refresh_table(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid "
                               "button[iconCls=x-tbar-loading][tooltip=Refresh] => .x-btn-icon-el")
        return ui_cmd_obj

    def discovered_modify_table_refresh_time(self, ui_cmd_obj, arg_dict):
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     "#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid "
                                     "button[text=Refresh Off] => .x-btn-wrap")
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid menuitem[text=" +
                               arg_dict['time_string'] + "] => .x-menu-item-text")
        return ui_cmd_obj

    def discovered_reset_table(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid button[text=Reset] => "
                               ".x-btn-inner-default-toolbar-small")
        return ui_cmd_obj

    def discovered_pre_register_device_set_default_site(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#preRegAddPanel panel[name=preRegAddForm] combobox[name=preRegSite] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "combobox[name=preRegSite].getPicker() => .x-boundlist-item:contains(" +
                               str(arg_dict['default_site']) + ")")
        return ui_cmd_obj

    def discovered_pre_register_device_set_ip_address(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#preRegAddPanel panel[name=preRegAddForm] textfield[name=preRegIpAddress] => "
                               ".x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['ip_address']),
                                    "#preRegAddPanel panel[name=preRegAddForm] textfield[name=preRegIpAddress] => "
                                    ".x-form-text")

        return ui_cmd_obj

    def discovered_pre_register_device_set_serial_numbers(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#preRegAddPanel panel[name=preRegAddForm] textareafield[name=preRegSerials] => "
                               ".x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['serial_nums']),
                                    "#preRegAddPanel panel[name=preRegAddForm] textareafield[name=preRegSerials] => "
                                    ".x-form-text")
        return ui_cmd_obj

    def discovered_pre_register_device_next(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[actionId=preRegNextButton] => .x-btn-button")
        return ui_cmd_obj

    def discovered_pre_register_device_previous(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[actionId=preRegPrevButton] => .x-btn-button")
        return ui_cmd_obj

    def discovered_pre_register_device_create(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[actionId=preRegCreateButton] => .x-btn-button")
        return ui_cmd_obj

    def discovered_pre_register_device_cancel(self, ui_cmd_obj, arg_dict):
        return ui_cmd_obj

    def discovered_edit_device_select_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel tab[text=" + str(arg_dict['tab_name']) + "] => .x-tab-inner")
        return ui_cmd_obj

    def discovered_edit_device_set_system_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=sysName] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['sys_name']),
                                    "deviceDetailsPanel textfield[name=sysName] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_set_contact(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=sysContact] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['contact']),
                                    "deviceDetailsPanel textfield[name=sysContact] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_set_location(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=sysLocation] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['location']),
                                    "deviceDetailsPanel textfield[name=sysLocation] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_set_admin_profile(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combobox[name=profileName] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=profileName].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['profile']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_topology_layer(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combobox[name=topologyRole] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=topologyRole].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['topology_layer']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_remove_from_service(self, ui_cmd_obj, arg_dict):
        return ui_cmd_obj

    def discovered_edit_device_set_default_site(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=defaultSiteId] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=defaultSiteId].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['site_name']) + ")")

        if str(arg_dict['import_site']) == "True" or str(arg_dict['import_site']) == "Yes":
            self.ext_builder.click(ui_cmd_obj, "messagebox[title=Import Site] #yes => .x-btn-inner-blue-small")
        else:
            self.ext_builder.click(ui_cmd_obj, "messagebox[title=Import Site] #no => .x-btn-inner-default-small")

        return ui_cmd_obj

    def discovered_edit_device_set_poll_group(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combobox[name=pollGroup] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=pollGroup].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['poll_group']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_poll_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combobox[name=pollType] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combobox[name=pollType].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['poll_type']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_snmp_timeout(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel numberfield[name=snmpTimeout] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['snmp_timeout']),
                                    "deviceDetailsPanel numberfield[name=snmpTimeout] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_set_snmp_retries(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel numberfield[name=snmpRetry] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['snmp_retries']),
                                    "deviceDetailsPanel numberfield[name=snmpRetry] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_set_replacement_serial_number(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel textfield[name=replacementSerialNumber] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['serial_num']),
                                    "deviceDetailsPanel textfield[name=replacementSerialNumber] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_trap_receiver(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceNewAddPanel[title=Add Device Actions] "
                                                      "checkbox[name=addTrapServer]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceNewAddPanel[title=Add Device Actions] checkbox[name=addTrapServer] => "
                                   ".x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_syslog_receiver(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceNewAddPanel[title=Add Device Actions] "
                                                      "checkbox[name=addSyslogServer]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceNewAddPanel[title=Add Device Actions] checkbox[name=addSyslogServer] => "
                                   ".x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_set_enable_collection(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceNewAddPanel[title=Add Device Actions] "
                                                      "checkbox[name=enableCollection]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceNewAddPanel[title=Add Device Actions] checkbox[name=enableCollection] => "
                                   ".x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_to_archive(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceNewAddPanel[title=Add Device Actions] "
                                                      "checkbox[name=addToSiteArchive]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceNewAddPanel[title=Add Device Actions] checkbox[name=addToSiteArchive] => "
                                   ".x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_to_map(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceNewAddPanel[title=Add Device Actions] "
                                                      "checkbox[name=addToSiteMap]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceNewAddPanel[title=Add Device Actions] checkbox[name=addToSiteMap] => "
                                   ".x-form-cb-input")
            if StringUtils.string_to_boolean(arg_dict["the_value"]) is True:
                self.ext_builder.click(ui_cmd_obj,
                                       "deviceNewAddPanel[title=Add Device Actions] combo[name=mapId] => "
                                       ".x-form-trigger")
                self.ext_builder.click(ui_cmd_obj,
                                       "deviceNewAddPanel[title=Add Device Actions] combo[name=mapId].getPicker() => "
                                       ".x-boundlist-item:contains(" + str(arg_dict['map_name']) + ")")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_to_policy_domain(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceNewAddPanel[title=Add Device Actions] "
                                                      "checkbox[name=addToPolicyDomain]", "[0].rawValue")

        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["add_to_domain"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceNewAddPanel[title=Add Device Actions] checkbox[name=addToPolicyDomain] => "
                                   ".x-form-cb-input")
            if StringUtils.string_to_boolean(arg_dict["add_to_domain"]) is True:
                self.ext_builder.click(ui_cmd_obj,
                                       "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Policy] "
                                       "combobox[name=policyDomain] => .x-form-trigger")
                self.ext_builder.click(ui_cmd_obj,
                                       "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Policy] "
                                       "combobox[name=policyDomain].getPicker() => .x-boundlist-item:contains(" +
                                       str(arg_dict['domain_name']) + ")")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_to_access_control_group(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceNewAddPanel[title=Add Device Actions] "
                                                      "checkbox[name=addToNacGroup]", "[0].rawValue")

        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["add_to_access_control"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceNewAddPanel[title=Add Device Actions] checkbox[name=addToNacGroup] => "
                                   ".x-form-cb-input")
            if StringUtils.string_to_boolean(arg_dict["add_to_access_control"]):
                self.ext_builder.click(ui_cmd_obj,
                                       "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                                       "combobox[name=nacApplianceGroup] => .x-form-trigger")
                self.ext_builder.click(ui_cmd_obj,
                                       "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                                       "combobox[name=nacApplianceGroup].getPicker() => .x-boundlist-item:contains(" +
                                       str(arg_dict['access_control_group']) + ")")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_engine_group_(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Discovered, self).discovered_edit_device_set_edit_access_control_engine_group_(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def discovered_edit_device_set_edit_access_control_switch_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=switchType] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=switchType].getPicker() => .x-boundlist-item:contains(" +
                               str(arg_dict['switch_type']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_primary_engine(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=primaryGateway] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=primaryGateway].getPicker() => .x-boundlist-item:contains(" +
                               str(arg_dict['primary_gateway']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_secondary_engine(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=secondaryGateway] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=secondaryGateway].getPicker() => .x-boundlist-item:contains(" +
                               str(arg_dict['secondary_gateway']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_auth_access_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=authAccessType] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=authAccessType].getPicker() => .x-boundlist-item:contains(" +
                               str(arg_dict['auth_access_type']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_virtual_router_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "textfield[name=vrName]=> .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['virtual_router']),
                                    "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                                    "textfield[name=vrName]")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_radius_attrs_to_send(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=attributesToSend] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=attributesToSend].getPicker() => .x-boundlist-item:contains(" +
                               str(arg_dict['attr_to_send']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_radius_accounting(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=radiusAccounting] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=radiusAccounting].getPicker() => .x-boundlist-item:contains(" +
                               str(arg_dict['radius_accounting']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_mgmt_radius_server_1(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=managementRadiusServer1] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=managementRadiusServer1].getPicker() => .x-boundlist-item:contains(" +
                               str(arg_dict['radius_server_1']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_mgmt_radius_server_2(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=managementRadiusServer2] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=managementRadiusServer2].getPicker() => .x-boundlist-item:contains(" +
                               str(arg_dict['radius_server_2']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_network_radius_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=networkRadiusServer] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=networkRadiusServer].getPicker() => .x-boundlist-item:contains(" +
                               str(arg_dict['network_radius_server']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_policy_enforcement_point_1(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=policyEnforcementPoint1] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=policyEnforcementPoint1].getPicker() => .x-boundlist-item:contains(" +
                               str(arg_dict['policy_enforcement_point_1']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_policy_enforcement_point_2(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=policyEnforcementPoint2] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[name=editDeviceDataWindow] panel[title=Access Control] "
                               "combobox[name=policyEnforcementPoint2].getPicker() => .x-boundlist-item:contains(" +
                               str(arg_dict['policy_enforcement_point_2']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_enable_auth_using_port_template(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceNewAddPanel[title=Add Device Actions] "
                                                      "checkbox[name=addEnableAuthOnAccess]", "[0].rawValue")

        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["enable_auth_using_port_template"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceNewAddPanel[title=Add Device Actions] checkbox[name=addEnableAuthOnAccess] "
                                   "=> .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_advanced_settings_open(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               r"deviceNewAddPanel[title=Add Device Actions] button[text=Advanced Settings\.\.\.] => "
                               r".x-btn-inner-gray-small")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_advanced_settings_save(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[text=OK] => .x-btn-button")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_advanced_settings_ip_subnet(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "combo[name=ipSubnet] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "combo[name=ipSubnet] boundlist => :textEquals(" +
                               str(arg_dict['ip_subnet']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_advanced_settings_shared_secret(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "passwordfield[name=sharedSecret] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['shared_secret']),
                                    "passwordfield[name=sharedSecret] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_advanced_settings_reauth_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "combo[name=switchReauthConfig] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "combo[name=switchReauthConfig] boundlist => :textEquals(" +
                               str(arg_dict['switch_reauth_config']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_set_edit_access_control_advanced_settings_enable_port_link(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=togglePortLink]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj, "checkbox[name=togglePortLink] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_set_nickname(self, ui_cmd_obj, arg_dict):
        # self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=nickname] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['nickname']),
                                    "deviceDetailsPanel textfield[name=nickname] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_set_asset_tag(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=assetTag] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['asset_tag']),
                                    "deviceDetailsPanel textfield[name=assetTag] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_set_user_data(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel textfield[name=" + "userData" +
                               str(arg_dict['the_field']) + "] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['user_data']),
                                    "deviceDetailsPanel textfield[name=" + "userData" +
                                    str(arg_dict['the_field']) + "] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_set_note(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textarea[name=note] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_note']),
                                    "deviceDetailsPanel textarea[name=note] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_vlan_definition_add(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel #deviceVlanGrid button[text=Add] => .x-btn-button")
        return ui_cmd_obj

    def discovered_edit_device_vlan_definition_edit(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel #deviceVlanGrid button[text=Edit] => .x-btn-button")
        return ui_cmd_obj

    def discovered_edit_device_vlan_definition_delete(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel #deviceVlanGrid button[text=Delete] => .x-btn-button")
        return ui_cmd_obj

    def discovered_edit_device_vlan_definition_update(self, ui_cmd_obj, arg_dict):
        type_string = "[RETURN]"
        self.ext_builder.enter_text(ui_cmd_obj, str(type_string),
                                    "textfield[name=deviceDetailsVlanName] => .x-form-text",
                                    clear_existing=False)
        return ui_cmd_obj

    def discovered_edit_device_vlan_definition_set_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "textfield[name=deviceDetailsVlanName] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "textfield[name=deviceDetailsVlanName] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_vlan_definition_set_vid(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "textfield[name=deviceDetailsVid] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "textfield[name=deviceDetailsVid] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_vlan_definition_set_always_write_to_devices(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=deviceDetailsWrite]",
                                                      "[0].value")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj, "checkbox[name=deviceDetailsWrite] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_vlan_definition_select_row(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("Selecting VLAN Name " + str(arg_dict['vlan_name']))
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel #deviceVlanGrid gridview => .x-grid-cell-inner:textEquals(" +
                               str(arg_dict['vlan_name']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_ztp_set_configure_device(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceZtpPlusPanel[title=ZTP+ Device Settings] "
                                                      "checkbox[name=ztpConfigEnable]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   r"deviceZtpPlusPanel[title=ZTP\+ Device Settings] checkbox[name=ztpConfigEnable] => "
                                   r".x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_ztp_set_serial_number(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=serialNumber] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "deviceDetailsPanel textfield[name=serialNumber] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_ztp_set_ip_address_subnet(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=ipAddress] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "deviceDetailsPanel textfield[name=ipAddress] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_ztp_set_gateway_address(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=gateway] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "deviceDetailsPanel textfield[name=gateway] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_ztp_set_management_interface(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combo[name=mgmtInterface] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "deviceDetailsPanel combo[name=mgmtInterface].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_ztp_set_domain_name(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=ztpDomainName] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "deviceDetailsPanel textfield[name=ztpDomainName] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_ztp_set_dns_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=dnsServer] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "deviceDetailsPanel textfield[name=dnsServer] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_ztp_set_ntp_server(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel textfield[name=ntpServer] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "deviceDetailsPanel textfield[name=ntpServer] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_ztp_set_lacp(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceZtpPlusPanel[title=ZTP+ Device Settings] "
                                                      "checkbox[name=lacp]", "[0].rawValue")
        if ui_cmd_obj.return_data is False and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is True:
            self.ext_builder.click(ui_cmd_obj,
                                   r"deviceZtpPlusPanel[title=ZTP\+ Device Settings] checkbox[name=lacp] => "
                                   r".x-form-cb-input")
            self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combo[name=lacpLogging] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=lacpLogging].getPicker() => "
                                   ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is True:
            self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combo[name=lacpLogging] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=lacpLogging].getPicker() => "
                                   ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is False:
            self.ext_builder.click(ui_cmd_obj, r"deviceZtpPlusPanel[title=ZTP\+ Device Settings] checkbox[name=lacp] =>"
                                               r" .x-form-cb-input")
        return ui_cmd_obj

    def discovered_edit_device_ztp_set_lldp(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceZtpPlusPanel[title=ZTP+ Device Settings] "
                                                      "checkbox[name=lldp]", "[0].rawValue")
        if ui_cmd_obj.return_data is False and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is True:
            self.ext_builder.click(ui_cmd_obj,
                                   r"deviceZtpPlusPanel[title=ZTP\+ Device Settings] checkbox[name=lldp] => "
                                   r".x-form-cb-input")
            self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combo[name=lldpLogging] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=lldpLogging].getPicker() => "
                                   ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is True:
            self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combo[name=lldpLogging] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=lldpLogging].getPicker() => "
                                   ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is False:
            self.ext_builder.click(ui_cmd_obj,
                                   r"deviceZtpPlusPanel[title=ZTP\+ Device Settings] checkbox[name=lldp] => "
                                   r".x-form-cb-input")
        return ui_cmd_obj

    def discovered_edit_device_ztp_set_mstp(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceZtpPlusPanel[title=ZTP+ Device Settings] "
                                                      "checkbox[name=spanningTree]", "[0].rawValue")
        if ui_cmd_obj.return_data is False and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is True:
            self.ext_builder.click(ui_cmd_obj,
                                   r"deviceZtpPlusPanel[title=ZTP\+ Device Settings] checkbox[name=spanningTree] => "
                                   r".x-form-cb-input")
            self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combo[name=spanningTreeLogging] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=spanningTreeLogging].getPicker() => "
                                   ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is True:
            self.ext_builder.click(ui_cmd_obj, "deviceDetailsPanel combo[name=spanningTreeLogging] => "
                                               ".x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=spanningTreeLogging].getPicker() => "
                                   ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is False:
            self.ext_builder.click(ui_cmd_obj,
                                   r"deviceZtpPlusPanel[title=ZTP\+ Device Settings] checkbox[name=spanningTree] => "
                                   r".x-form-cb-input")
        return ui_cmd_obj

    def discovered_edit_device_ztp_set_mvrp(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceZtpPlusPanel[title=ZTP+ Device Settings] "
                                                      "checkbox[name=mvrp]", "[0].rawValue")
        if ui_cmd_obj.return_data is False and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is True:
            self.ext_builder.click(ui_cmd_obj,
                                   r"deviceZtpPlusPanel[title=ZTP\+ Device Settings] checkbox[name=mvrp] => "
                                   r".x-form-cb-input")
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=mvrpLogging] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=mvrpLogging].getPicker() => "
                                   ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is True:
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=mvrpLogging] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=mvrpLogging].getPicker() => "
                                   ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is False:
            self.ext_builder.click(ui_cmd_obj,
                                   r"deviceZtpPlusPanel[title=ZTP\+ Device Settings] checkbox[name=mvrp] => "
                                   r".x-form-cb-input")
        return ui_cmd_obj

    def discovered_edit_device_ztp_set_poe(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceZtpPlusPanel[title=ZTP+ Device Settings] "
                                                      "checkbox[name=poe]", "[0].rawValue")

        if ui_cmd_obj.return_data is False and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is True:
            self.ext_builder.click(ui_cmd_obj,
                                   r"deviceZtpPlusPanel[title=ZTP\+ Device Settings] checkbox[name=poe] => "
                                   r".x-form-cb-input")
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=poeLogging] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=poeLogging].getPicker() => "
                                   ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is True:
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=poeLogging] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=poeLogging].getPicker() => "
                                   ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is False:
            self.ext_builder.click(ui_cmd_obj,
                                   r"deviceZtpPlusPanel[title=ZTP\+ Device Settings] checkbox[name=poe] => "
                                   r".x-form-cb-input")
        return ui_cmd_obj

    def discovered_edit_device_ztp_set_xvlan(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "deviceZtpPlusPanel[title=ZTP+ Device Settings] "
                                                      "checkbox[name=vxlan]", "[0].rawValue")
        if ui_cmd_obj.return_data is False and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is True:
            self.ext_builder.click(ui_cmd_obj,
                                   r"deviceZtpPlusPanel[title=ZTP\+ Device Settings] checkbox[name=vxlan] => "
                                   r".x-form-cb-input")
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=vxlanLogging] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=vxlanLogging].getPicker() => "
                                   ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is True:
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=vxlanLogging] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "deviceDetailsPanel combo[name=vxlanLogging].getPicker() => "
                                   ".x-boundlist-item:contains(" + str(arg_dict['the_value']) + ")")
        elif ui_cmd_obj.return_data is True and StringUtils.string_to_boolean(arg_dict["is_enabled"]) is False:
            self.ext_builder.click(ui_cmd_obj,
                                   r"deviceZtpPlusPanel[title=ZTP\+ Device Settings] checkbox[name=vxlan] => "
                                   r".x-form-cb-input")
        return ui_cmd_obj

    def discovered_edit_device_ports_select_port(self, ui_cmd_obj, arg_dict):
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     'deviceDetailsPanel gridcolumn[dataIndex=deviceDetailsPortNumber] => '
                                     '.x-column-header-text')
        self.ext_builder.double_click(ui_cmd_obj,
                                      "editDeviceDataWindow[title=Configure Device] "
                                      "deviceDetailPortsPanel[name=deviceDetailPortsPanel] tableview => "
                                      ".x-grid-cell-inner:textEquals(" + str(arg_dict['port_name']) + ")")
        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "editDeviceDataWindow[title=Configure Device] "
                               "deviceDetailPortsPanel[name=deviceDetailPortsPanel] button[actionId=deviceEditPort] => "
                               ".x-btn-inner-default-toolbar-small")
        return ui_cmd_obj

    def discovered_edit_device_ports_row_editor_update(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text_no_target(ui_cmd_obj, "[RETURN]")
        return ui_cmd_obj

    def discovered_edit_device_ports_row_editor_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "roweditorbuttons [itemId=cancel] => .x-btn-inner-default-small")
        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_alias(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "textfield[name=deviceDetailsPortAlias] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_nickname(self, ui_cmd_obj, arg_dict):
        # self.ext_builder.click(ui_cmd_obj,"textfield[name=deviceDetailsPortNickname]= >.x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "textfield[name=deviceDetailsPortNickname] => .x-form-text")
        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_enabled(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "checkbox[name =deviceDetailsPortAdminState]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj, "checkbox[name =deviceDetailsPortAdminState] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_auto_negotiation(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name =deviceDetailsPortAutoNegotiation]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   "checkbox[name =deviceDetailsPortAutoNegotiation] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")

        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_speed(self, ui_cmd_obj, arg_dict):
        if StringUtils.string_to_boolean(arg_dict["auto_neg_value"]) is False:
            self.ext_builder.click(ui_cmd_obj, "combo[name=deviceDetailsPortConfigSpeed] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "combo[name=deviceDetailsPortConfigSpeed] boundlist => :textEquals(" +
                                   str(arg_dict["the_value"]) + ")")
        else:
            self.ext_builder.click(ui_cmd_obj, "combo[name=deviceDetailsPortConfigSpeed] => .x-form-clear-trigger")
            self.ext_builder.click(ui_cmd_obj, "combo[name=deviceDetailsPortConfigSpeed] => .x-form-trigger")
            values = str(arg_dict["the_value"]).split(",")
            for value in values:
                self.ext_builder.click(ui_cmd_obj,
                                       "combo[name=deviceDetailsPortConfigSpeed] boundlist => "
                                       ":textEquals(" + str(value) + ")")

        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_duplex(self, ui_cmd_obj, arg_dict):
        if StringUtils.string_to_boolean(arg_dict["auto_neg_value"]) is False:
            self.ext_builder.click(ui_cmd_obj, "combo[name=deviceDetailsPortDuplex] => .x-form-trigger")
            self.ext_builder.click(ui_cmd_obj,
                                   "combo[name=deviceDetailsPortDuplex] boundlist => "
                                   ":textEquals(" + str(arg_dict["the_value"]) + ")")
        else:
            self.ext_builder.click(ui_cmd_obj, "combo[name=deviceDetailsPortDuplex] => .x-form-clear-trigger")
            self.ext_builder.click(ui_cmd_obj, "combo[name=deviceDetailsPortDuplex] => .x-form-trigger")
            values = str(arg_dict["the_value"]).split(",")
            for value in values:
                self.ext_builder.click(ui_cmd_obj,
                                       "combo[name=deviceDetailsPortDuplex] boundlist => "
                                       ":textEquals(" + str(value) + ")")
        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "combo[name=deviceDetailsRole] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "combo[name=deviceDetailsRole] boundlist => "
                               ":textEquals(" + str(arg_dict["the_value"]) + ")")
        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_pvid(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "combo[name=devicePortPvidEditor] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj,
                               "combo[name=devicePortPvidEditor].getPicker() => "
                               ".x-boundlist-item:contains(" + str(arg_dict["the_value"]) + ")")
        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_lag(self, ui_cmd_obj, arg_dict):
        iteration = 0
        self.ext_builder.click(ui_cmd_obj,
                               "selectActionField[dataIndex=deviceLagMembership] => .fa-ellipsis-h")

        self.ext_builder.click(ui_cmd_obj,
                               "selectPortActionDialog[title=Select LAG Ports] checkcolumn => "
                               ".x-column-header-checkbox")
        self.ext_builder.click(ui_cmd_obj,
                               "selectPortActionDialog[title=Select LAG Ports] checkcolumn => "
                               ".x-column-header-checkbox")
        values = str(arg_dict["the_value"]).split(",")
        for value in values:
            self.ext_builder.component_query(
                ui_cmd_obj, 'selectPortActionDialog[title=Select LAG Ports] gridview', '[0].store.data.length')
            length = ui_cmd_obj.return_data
            while iteration < length:
                self.ext_builder.component_query(ui_cmd_obj, 'selectPortActionDialog[title=Select LAG Ports] gridview',
                                                 '[0].store.data.items[' + str(iteration) + '].data.portName')
                if value == ui_cmd_obj.return_data:
                    location_in_table = iteration
                    self.ext_builder.component_query(ui_cmd_obj,
                                                     'selectPortActionDialog[title=Select LAG Ports] gridview',
                                                     '[0].body.dom.childNodes[' + str(location_in_table) + '].id')
                    self.ext_builder.click(ui_cmd_obj, '#' + str(ui_cmd_obj.return_data) + ' > tbody > tr > td')
                    break
                else:
                    iteration += 1

        self.ext_builder.click(ui_cmd_obj, ">>selectPortActionDialog[title=Select LAG Ports] button[text=OK]")
        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_authentication(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "multicombo[name=deviceAuthType] => .x-form-clear-trigger")
        self.ext_builder.click(ui_cmd_obj, "multicombo[name=deviceAuthType] => .x-form-arrow-trigger")
        auth_values = str(arg_dict["the_value"]).split(",")
        for value in auth_values:
            self.ext_builder.click(ui_cmd_obj,
                                   "multicombo[name=deviceAuthType].getPicker() => "
                                   ".x-boundlist-item:contains(" + str(value) + ")")

        # type_string = "[ESCAPE]"
        # self.ext_builder.type(ui_cmd_obj, str(type_string),
        #                                   "textfield[name=deviceAuthType] => .x-form-text",
        #                                   clear_existing=False)
        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_tagged(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "vlanmulticombobox[dataIndex=tagged] => .x-form-clear-trigger")
        self.ext_builder.click(ui_cmd_obj, "vlanmulticombobox[dataIndex=tagged] => .x-form-arrow-trigger")
        values = str(arg_dict["the_value"]).split(",")
        for value in values:
            self.ext_builder.click(ui_cmd_obj,
                                   "vlanmulticombobox[dataIndex=tagged].getPicker() => "
                                   ".x-boundlist-item:contains(" + str(value) + ")")
        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_untagged(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "vlanmulticombobox[dataIndex=untagged] => .x-form-clear-trigger")
        self.ext_builder.click(ui_cmd_obj, "vlanmulticombobox[dataIndex=untagged] => .x-form-arrow-trigger")
        values = str(arg_dict["the_value"]).split(",")
        for value in values:
            self.ext_builder.click(ui_cmd_obj,
                                   "vlanmulticombobox[dataIndex=untagged].getPicker() => "
                                   ".x-boundlist-item:contains(" + str(value) + ")")
        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_node_alias(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=deviceDetailsPortNodeAlias]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj, "checkbox[name=deviceDetailsPortNodeAlias] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_span_guard(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=deviceDetailsPortSpanGuard]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj, "checkbox[name=deviceDetailsPortSpanGuard] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_loop_protect(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=deviceDetailsPortLoopProtect]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj, "checkbox[name=deviceDetailsPortLoopProtect] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_ports_edit_row_mvrp(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=deviceDetailsPortMvrp]",
                                                      "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj, "checkbox[name=deviceDetailsPortMvrp] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")
        return ui_cmd_obj

    def discovered_edit_device_ports_show_columns(self, ui_cmd_obj, arg_dict):
        # Open the column menu
        self.ext_builder.move_cursor(ui_cmd_obj,
                                     'deviceDetailsPanel gridcolumn[dataIndex=deviceDetailsPortNumber] => '
                                     '.x-column-header-text')
        self.ext_builder.click(ui_cmd_obj,
                               'deviceDetailsPanel gridcolumn[dataIndex=deviceDetailsPortNumber] => '
                               '.x-column-header-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               'editDeviceDataWindow grid[name=deviceDetailPortsGrid] menu #columnItem => '
                               '.x-menu-item-text')

        # Make sure the menu exists
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      'editDeviceDataWindow grid[name=deviceDetailPortsGrid] '
                                                      'menu #columnItem', '[0].menu')

        if ui_cmd_obj.return_data is not None:
            # Make sure the menu contains items
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          'editDeviceDataWindow grid[name=deviceDetailPortsGrid] menu '
                                                          '#columnItem', '[0].menu.items.length')
            menu_count = int(ui_cmd_obj.return_data)
            if menu_count != 0:
                # Loop through each of the column names in the comma-separated list and toggle each column
                # checkbox appropriately
                columns = arg_dict['col_list'].split(',')
                for col_name in columns:
                    menu_count += 1

                    # Loop through the items, searching for the node to act on
                    menu_index = 0
                    for x in range(0, menu_count):
                        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                                      'editDeviceDataWindow '
                                                                      'grid[name=deviceDetailPortsGrid] menu '
                                                                      '#columnItem', '[0].menu.items.items[' +
                                                                      str(menu_index) + '].text')
                        if ui_cmd_obj.return_data == col_name:
                            # Check the current selection state of the node
                            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                                          'editDeviceDataWindow '
                                                                          'grid[name=deviceDetailPortsGrid] menu '
                                                                          '#columnItem', '[0].menu.items.items[' +
                                                                          str(menu_index) + '].checked')
                            if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['show_col']):
                                self.ext_builder.click(ui_cmd_obj,
                                                       'editDeviceDataWindow grid[name=deviceDetailPortsGrid] menu '
                                                       '#columnItem menucheckitem[text=' + col_name + '] => '
                                                       '.x-menu-item-icon')
                            else:
                                self.logger.log_info(
                                    "\nColumn '" + col_name + "' is already at desired selection state (" +
                                    arg_dict['show_col'] + ").\n")
                            break
                        else:
                            menu_index += 1
            else:
                self.logger.log_info("\nColumn menu is empty.\n")
                ui_cmd_obj.error_state = True
        else:
            self.logger.log_info("\nCould not find column menu.\n")
            ui_cmd_obj.error_state = True

        # Close the column menu
        self.ext_builder.click(ui_cmd_obj,
                               'editDeviceDataWindow[title=Configure Device] '
                               'deviceDetailPortsPanel[name=deviceDetailPortsPanel] toolbar => .x-box-inner')

        return ui_cmd_obj

    def discovered_edit_device_click_save(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[actionId=editDeviceData] => .x-btn-button")
        return ui_cmd_obj

    def discovered_edit_device_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[actionId=editDeviceCloseWindow] => .x-btn-button")
        return ui_cmd_obj

    def discovered_confirm_device_ip_exists(self, ui_cmd_obj, arg_dict):
        row_index = self.discovered_get_discovered_table_row_index(ui_cmd_obj, "connectedIpAddress",
                                                                   str(arg_dict["ip_address"]))
        self.logger.log_info("connectedIpAddress " + str(row_index))
        if row_index == -1:
            row_index = self.discovered_get_discovered_table_row_index(ui_cmd_obj, "ipAddress",
                                                                       str(arg_dict["ip_address"]))
            self.logger.log_info("ipAddress " + str(row_index))
            if row_index == -1:
                ui_cmd_obj.error_state = True
                self.logger.log_info("Confirmed IP Address: " + str(arg_dict["ip_address"]) +
                                     " does not exist within the discovered table.")
            else:
                ui_cmd_obj.error_state = False
                self.logger.log_info("Confirmed IP Address: " + str(arg_dict["ip_address"]) +
                                     " does exist within the discovered table at row index: " + str(row_index))
        else:
            ui_cmd_obj.error_state = False
            self.logger.log_info("Confirmed IP Address: " + str(arg_dict["ip_address"]) +
                                 " does exist within the discovered table at row index: " + str(row_index))

        return ui_cmd_obj

    def discovered_confirm_device_ip_profile(self, ui_cmd_obj, arg_dict):
        row_index = self.discovered_get_discovered_table_row_index(ui_cmd_obj, "connectedIpAddress",
                                                                   str(arg_dict["ip_address"]))
        self.logger.log_info("connectedIpAddress " + str(row_index))
        profile_name = ""
        if row_index == -1:
            row_index = self.discovered_get_discovered_table_row_index(ui_cmd_obj, "ipAddress",
                                                                       str(arg_dict["ip_address"]))
            self.logger.log_info("ipAddress " + str(row_index))
            if row_index == -1:
                ui_cmd_obj.error_state = True
            else:
                profile_name = self.discovered_get_discovered_table(ui_cmd_obj, row_index, "profileName")
        else:
            profile_name = self.discovered_get_discovered_table(ui_cmd_obj, row_index, "profileName")

        if profile_name == str(arg_dict["profile_name"]):
            self.logger.log_info("Confirmed Profile: " + arg_dict['profile_name'] + " matches profile: " +
                                 profile_name + " within the discovered table for IP Address: " +
                                 str(arg_dict["ip_address"]))
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_info("Confirmed Profile: " + arg_dict['profile_name'] + " does not match profile: " +
                                 profile_name + " within the discovered table for IP Address: " +
                                 str(arg_dict["ip_address"]))
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def discovered_confirm_device_ip_status(self, ui_cmd_obj, arg_dict):
        row_index = self.discovered_get_discovered_table_row_index(ui_cmd_obj, "connectedIpAddress",
                                                                   str(arg_dict["ip_address"]))
        self.logger.log_info("connectedIpAddress " + str(row_index))
        status = ""
        if row_index == -1:
            row_index = self.discovered_get_discovered_table_row_index(ui_cmd_obj, "ipAddress",
                                                                       str(arg_dict["ip_address"]))
            self.logger.log_info("ipAddress " + str(row_index))
            if row_index == -1:
                ui_cmd_obj. ui_cmd_obj.error_state = True
            else:
                status = self.discovered_get_discovered_table(ui_cmd_obj, row_index, "status")
        else:
            status = self.discovered_get_discovered_table(ui_cmd_obj, row_index, "status")

        if status == str(arg_dict["status"]):
            self.logger.log_info("Confirmed Status: " + arg_dict['status'] + " matches status: " + status +
                                 " within the discovered table for IP Address: " + str(arg_dict["ip_address"]))
            ui_cmd_obj.error_state = False
        else:
            self.logger.log_info("Confirmed Status: " + arg_dict['status'] + " does not match status: " + status +
                                 " within the discovered table for IP Address: " + str(arg_dict["ip_address"]))
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def discovery_get_device_port_auto_negotiation_value(self, ui_cmd_obj, arg_dict):
        row_index = self.discovered_get_discovered_table_row_index(
            ui_cmd_obj, "deviceDetailsPortNumber", "5")
        # str(arg_dict["port_id"])
        self.logger.log_info("deviceDetailsPortNumber " + str(row_index))
        if row_index == -1:
            ui_cmd_obj.error_state = True
            # self.logger.log_info(
            #     "Confirmed Port ID: " + str(arg_dict["port_id"]) + " does not exist within the Device Ports table.")
        else:
            ui_cmd_obj.return_data = str(
                self.devices_get_table(ui_cmd_obj,
                                       'deviceDetailPortsPanel[name=deviceDetailPortsPanel] gridview{isVisible()}',
                                       row_index, "deviceDetailsPortAutoNegotiation"))
        return ui_cmd_obj

    def discovered_get_discovered_table(self, ui_cmd_obj, row_index, column_name):
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid tableview',
                                         '[0].store.data.items[' + str(row_index) + '].data.' + column_name)
        return ui_cmd_obj.return_data

    def discovered_get_discovered_table_row_index(self, ui_cmd_obj, column_name, the_value):
        self.logger.log_info("The value to look for: " + the_value + ".")
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid tableview',
                                         '[0].store.data.items.length')
        item_count = int(ui_cmd_obj.return_data)
        self.logger.log_info("The table contains : " + str(item_count) + " rows.")
        item_index = 0
        for item_index in range(0, item_count):
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid tableview',
                                             '[0].store.data.items[' + str(item_index) + '].data.' + column_name)
            self.logger.log_info("The table row contains : " + str(ui_cmd_obj.return_data) + " in column: " +
                                 column_name)
            if str(ui_cmd_obj.return_data) == str(the_value):
                self.logger.log_info("The row index returned: " + str(item_index + 1))
                break
            else:
                item_index = -1
        return item_index

    def discovered_edit_device_edit(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[actionId=addDiscoverDevices] => .x-btn-button")
        return ui_cmd_obj
