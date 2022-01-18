from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as SitesBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Sites(SitesBase):

    def sites_create_site(self, ui_cmd_obj, arg_dict):
        # Access the menu to create the map
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton => .fa')
        self.ext_builder.click(ui_cmd_obj, r'#networkTabPanel #networkDevicesTab #DeviceTreeActionButton{isVisible()} '
                                           r'menuitem[text=Maps\/Sites] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton{isVisible()} '
                                           'menuitem[text=Create Site...] => .x-menu-item-text')

        # Populate the dialog
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['site_name'], '#mapCreationWindow #mapName => .x-form-text')

        # Handle the case where the OK button is disabled
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#mapCreationWindow #mapCreateOkButton', '[0].disabled')

        # If OK is disabled click Cancel/Close;  otherwise, click OK
        if ui_cmd_obj.return_data is True:
            # Check if there was an error
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "#mapCreationWindow #mapName",
                                                          "[0].lastActiveError")
            if "already exists" in ui_cmd_obj.return_data:
                # PASS
                self.logger.log_info("\nA site with name '" + str(arg_dict['site_name']) + "' already exists.\n")
                ui_cmd_obj.error_state = False
            else:
                # FAIL
                self.logger.log_info("\nCould not create site: '" + ui_cmd_obj.return_data + "'.\n")
                ui_cmd_obj.error_state = True

            # Click Cancel
            self.ext_builder.click(ui_cmd_obj, '#mapCreationWindow button[text=Cancel] => .x-btn-inner-default-small')
        else:
            # Click OK
            self.ext_builder.click(ui_cmd_obj, '#mapCreationWindow #mapCreateOkButton => .x-btn-inner-blue-small')

        # TO DO: switch to wait for
        self.logger.log_info("\nTO DO: wait for the site to be added to the tree\n")
        self.ext_builder.delay(ui_cmd_obj, "3000")

        return ui_cmd_obj

    def sites_delete_site(self, ui_cmd_obj, arg_dict):
        # Select the specified map in the tree
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab treeview => '
                                           '.x-tree-node-text span:textEquals(' + arg_dict['site_name'] + ')')

        # Access the menu to delete the map
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton => .fa')
        self.ext_builder.click(ui_cmd_obj, r'#networkTabPanel #networkDevicesTab #DeviceTreeActionButton{isVisible()} '
                                           r'menuitem[text=Maps\/Sites] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton{isVisible()} '
                                           'menuitem[text=Delete Site] => .x-menu-item-text')

        # Confirm the delete
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def sites_select_sub_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'tab[text=' + str(arg_dict['tab_name']) + '] => .x-tab-inner')

        return ui_cmd_obj

    def sites_configure_addresses_click_add(self, ui_cmd_obj, arg_dict):
        # Click the Add toolbar button
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'grid[name=discoverAddressesGrid] button[text=Add] => '
                               '.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def sites_configure_addresses_click_delete(self, ui_cmd_obj, arg_dict):
        # Handle the case where the button is disabled
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                      'grid[name=discoverAddressesGrid] '
                                                      'button[actionId=removeDiscoverAddress]', '[0].disabled')

        # If the Delete toolbar button is enabled, click it;  otherwise, report the error
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   'grid[name=discoverAddressesGrid] button[actionId=removeDiscoverAddress] => '
                                   '.x-btn-inner-default-toolbar-small')
        else:
            self.logger.log_info("\nThe 'Delete' button in the Addresses panel is disabled.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def sites_configure_addresses_select_address(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'grid[name=discoverAddressesGrid] => '
                               ':textEquals(' + str(arg_dict['the_value']) + ')')
        return ui_cmd_obj

    def sites_configure_addresses_set_enabled(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_addresses_set_enabled(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_profiles_click_add(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_profiles_click_add(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_profiles_click_edit(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_profiles_click_edit(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_profiles_click_delete(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_profiles_click_delete(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_profiles_select_profile(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_profiles_select_profile(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_profiles_set_accept(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("\nTO DO: accept comma-separated list of profiles\n")
        # Set the state of the check button if it isn't already at the desired state

        # Figure out how many items are in the profiles table
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                      '#deviceProfilesGridId tableview', '[0].store.data.items.length')
        item_count = int(ui_cmd_obj.return_data)
        item_count += 1

        # Loop through the profile table items, searching for the node to act on
        for item_index in range(0, item_count):
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#networkTabPanel #networkDevicesTab '
                                                          '#devicesTreeContextTabPanel #deviceProfilesGridId tableview',
                                                          '[0].store.data.items[' + str(item_index) + '].data.name')
            if ui_cmd_obj.return_data == arg_dict['the_profile']:
                # Check the current checked state of the node
                ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                              '#networkTabPanel #networkDevicesTab '
                                                              '#devicesTreeContextTabPanel #deviceProfilesGridId '
                                                              'tableview', '[0].store.data.items[' +
                                                              str(item_index) + '].data.acceptProfile')
                node_checked = ui_cmd_obj.return_data

                if node_checked is not StringUtils.string_to_boolean(arg_dict["btn_state"]):
                    self.ext_builder.click(ui_cmd_obj,
                                           '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                           '#deviceProfilesGridId tableview => '
                                           '.x-grid-item:contains(' + str(arg_dict['the_profile']) + ') '
                                           '.x-grid-cell-acceptColumn .x-grid-checkcolumn')
                else:
                    self.logger.log_info("\nProfile '" + arg_dict['the_profile'] + "' is already at desired state.\n")
                break

        return ui_cmd_obj

    def sites_configure_profiles_set_reject(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_profiles_set_reject(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_actions_set_automatically_add_devices(self, ui_cmd_obj, arg_dict):
        # Determine the current selection state of the check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                                      "checkbox[name=addToNetSight]", "[0].rawValue")

        # Only click the check button if it is not currently in the correct state
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["btn_state"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   'checkbox[name=addToNetSight] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Automatically Add Devices' check button already at desired value.\n")

        return ui_cmd_obj

    def sites_configure_actions_set_add_trap_receiver(self, ui_cmd_obj, arg_dict):
        # Determine the current selection state of the check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                                      "checkbox[name=addTrapServer]", "[0].rawValue")

        # Only click the check button if it is not currently in the correct state
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["btn_state"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   'checkbox[name=addTrapServer] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Add Trap Receiver' check button already at desired value.\n")

        return ui_cmd_obj

    def sites_configure_actions_set_add_syslog_receiver(self, ui_cmd_obj, arg_dict):
        # Determine the current selection state of the check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                                      "checkbox[name=addSyslogServer]", "[0].rawValue")

        # Only click the check button if it is not currently in the correct state
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["btn_state"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   'checkbox[name=addSyslogServer] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Add Syslog Receiver' check button already at desired value.\n")

        return ui_cmd_obj

    def sites_configure_actions_set_enable_collection(self, ui_cmd_obj, arg_dict):
        # Determine the current selection state of the check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                                      "checkbox[name=enableCollection]", "[0].rawValue")

        # Only click the check button if it is not currently in the correct state
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["btn_state"]):
            self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                               'checkbox[name=enableCollection] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Enable Collection' check button already at desired value.\n")

        return ui_cmd_obj

    def sites_configure_actions_set_add_to_archive(self, ui_cmd_obj, arg_dict):
        # Determine the current selection state of the check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                                      "checkbox[name=addToSiteArchive]", "[0].rawValue")

        # Only click the check button if it is not currently in the correct state
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["btn_state"]):
            self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                               'checkbox[name=addToSiteArchive] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Add to Archive' check button already at desired value.\n")

        return ui_cmd_obj

    def sites_configure_actions_set_add_to_map(self, ui_cmd_obj, arg_dict):
        # Make sure the check button is enabled (it will be disabled if no maps exist)
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                                      "checkbox[name=addToSiteMap]", "[0].disabled")
        # If the button is not disabled, we can continue
        if ui_cmd_obj.return_data is False:
            # Determine the current selection state of the check button
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          "#networkTabPanel #networkDevicesTab "
                                                          "#devicesTreeContextTabPanel checkbox[name=addToSiteMap]",
                                                          "[0].rawValue")

            # Only click the check button if it is not currently in the correct state
            if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["btn_state"]):
                self.ext_builder.click(ui_cmd_obj,
                                       '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                       'checkbox[name=addToSiteMap] => .x-form-cb-input')
            else:
                self.logger.log_info("\n'Add to Map' check button already at desired value.\n")
        else:
            self.logger.log_info("\n'Add to Map' check button is disabled.\n")
            # Fail the test if the check button was being set to True
            # (if being set to False, it doesn't matter that the button is disabled)
            if StringUtils.string_to_boolean(arg_dict["btn_state"]) is True:
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def sites_configure_actions_set_map(self, ui_cmd_obj, arg_dict):
        # Make sure the field is not hidden (it will be hidden if no maps exist or if the Add to Map check button
        # is deselected)
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                                      "combo[name=mapId]", "[0].hidden")

        # If the field is visible, we can make the selection
        if ui_cmd_obj.return_data is False:
            self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                               'combo[name=mapId] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                               'combo[name=mapId] boundlist => '
                                               '.x-boundlist-item:contains(' + arg_dict['map_name'] + ')')
        else:
            self.logger.log_info("\nMap selection field is not displayed - could not select map '" +
                                 arg_dict['map_name'] + "'.\n")
            ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def sites_configure_actions_set_add_device_to_policy_domain(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_actions_set_add_device_to_policy_domain(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_actions_set_policy_domain(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_actions_set_policy_domain(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_actions_set_add_device_to_access_control_engine_group(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_actions_set_add_device_to_access_control_engine_group(ui_cmd_obj,
                                                                                                     arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_actions_set_access_control_engine_group(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_actions_set_access_control_engine_group(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_actions_set_enable_authentication_using_port_template(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_actions_set_enable_authentication_using_port_template(ui_cmd_obj,
                                                                                                     arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_vlan_select_vlan(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_vlan_select_vlan(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_vlan_click_add(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_vlan_click_add(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_vlan_click_edit(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_vlan_click_edit(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_vlan_click_delete(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_vlan_click_delete(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_vlan_row_click_update(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_vlan_row_click_update(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_vlan_row_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_vlan_row_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_vlan_row_set_name(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_vlan_row_set_name(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_vlan_row_set_vid(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_vlan_row_set_vid(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_vlan_row_set_always_write_to_devices(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_vlan_row_set_always_write_to_devices(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_ports_select_port_configuration(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'form[title=Port Templates] gridview => .x-grid-cell-inner:textEquals(' +
                               arg_dict['port_config'] + ')')

        return ui_cmd_obj

    def sites_configure_ports_click_edit(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'button[actionId=editPortTemplateAction] => .x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def sites_configure_ports_row_click_update(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text_no_target(ui_cmd_obj, "[RETURN]")
        return ui_cmd_obj

    def sites_configure_ports_row_click_cancel(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_ports_row_click_cancel(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_ports_row_set_pvid(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_ports_row_set_pvid(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_ports_row_set_policy(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_ports_row_set_policy(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_ports_row_set_authentication(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_ports_row_set_authentication(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_ports_row_set_tagged(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_ports_row_set_tagged(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_ports_row_set_untagged(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_ports_row_set_untagged(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_ports_row_set_node_alias(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_ports_row_set_node_alias(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_ports_row_set_span_guard(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_ports_row_set_span_guard(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_ports_row_set_loop_protect(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_ports_row_set_loop_protect(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_ports_row_set_mvrp(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_ports_row_set_mvrp(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_ports_row_set_auto_negotiation(self, ui_cmd_obj, arg_dict):
        # Determine the current selection state of the check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, "checkbox[name=portAutoNegotiation]", "[0].rawValue")
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj, "checkbox[name=portAutoNegotiation] => .x-form-cb-input")
        else:
            self.logger.log_info("\nCheck button already at desired state.\n")

        return ui_cmd_obj

    def sites_configure_ports_row_set_collection(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            super(Sites, self).sites_configure_ports_row_set_collection(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def sites_configure_ports_show_columns(self, ui_cmd_obj, arg_dict):
        # Open the column menu
        self.ext_builder.move_cursor(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                 'gridcolumn[text=Configuration] => .x-column-header-text-inner')
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                           'gridcolumn[text=Configuration] => .x-column-header-trigger')
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                           'form[title=Port Templates] menu #columnItem => .x-menu-item-link')

        # Make sure the menu exists
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                      'form[title=Port Templates] menu #columnItem', '[0].menu')

        if ui_cmd_obj.return_data is not None:
            # Make sure the menu contains items
            ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                          '#networkTabPanel #networkDevicesTab '
                                                          '#devicesTreeContextTabPanel form[title=Port Templates] menu '
                                                          '#columnItem', '[0].menu.items.length')
            menu_count = int(ui_cmd_obj.return_data)
            if menu_count != 0:
                # Loop through each of the column names in the comma-separated list and toggle each column checkbox
                # appropriately
                columns = arg_dict['col_list'].split(',')
                for col_name in columns:
                    menu_count += 1

                    # Loop through the items, searching for the node to act on
                    menu_index = 0
                    for x in range(0, menu_count):
                        ui_cmd_obj = self.ext_builder.component_query(
                            ui_cmd_obj,
                            '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                            'form[title=Port Templates] menu #columnItem',
                            '[0].menu.items.items[' + str(menu_index) + '].text')
                        if ui_cmd_obj.return_data == col_name:
                            # Check the current selection state of the node
                            ui_cmd_obj = self.ext_builder.component_query(
                                ui_cmd_obj,
                                '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                'form[title=Port Templates] menu #columnItem',
                                '[0].menu.items.items[' + str(menu_index) + '].checked')
                            if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict['show_col']):
                                self.ext_builder.click(ui_cmd_obj,
                                                       '#networkTabPanel #networkDevicesTab '
                                                       '#devicesTreeContextTabPanel form[title=Port Templates] menu '
                                                       '#columnItem menucheckitem[text=' + col_name + '] => '
                                                       '.x-menu-item-icon')
                            else:
                                self.logger.log_info("\nColumn '" + col_name + "' is already at desired selection "
                                                     "state (" + arg_dict['show_col'] + ").\n")
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
        self.ext_builder.click(ui_cmd_obj, '>>#networkTabPanel #networkDevicesTab treeview')

        return ui_cmd_obj

    def sites_configure_ztp_set_configure_device(self, ui_cmd_obj, arg_dict):
        # Determine the current selection state of the check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                                      "checkbox[name=ztpConfigEnable]", "[0].rawValue")

        # Only click the check button if it is not currently in the correct state
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   'checkbox[name=ztpConfigEnable] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Configure Device' check button already at desired value.\n")

        return ui_cmd_obj

    def sites_configure_ztp_set_use_discovered_ip(self, ui_cmd_obj, arg_dict):
        # Determine the current selection state of the check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                                      "checkbox[name=ztpUseDiscoveredIp]", "[0].rawValue")

        # Only click the check button if it is not currently in the correct state
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   'checkbox[name=ztpUseDiscoveredIp] => .x-form-cb-input')
        else:
            self.logger.log_info("\n'Use Discovered IP' check button already at desired value.\n")

        return ui_cmd_obj

    def sites_configure_ztp_set_gateway_address(self, ui_cmd_obj, arg_dict):
        # Enter the Gateway Address
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                    "textfield[name=gateway] => .x-form-text")

        return ui_cmd_obj

    def sites_configure_ztp_set_management_interface(self, ui_cmd_obj, arg_dict):
        # Select the Management Interface
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=mgmtInterface] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=mgmtInterface] boundlist => :textEquals(' + arg_dict['the_value'] + ')')

        return ui_cmd_obj

    def sites_configure_ztp_set_domain_name(self, ui_cmd_obj, arg_dict):
        # Enter the Domain Name
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                    "textfield[name=ztpDomainName] => .x-form-text")

        return ui_cmd_obj

    def sites_configure_ztp_set_dns_server(self, ui_cmd_obj, arg_dict):
        # Enter the DNS Server
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                    "textfield[name=dnsServer] => .x-form-text")

        return ui_cmd_obj

    def sites_configure_ztp_set_ntp_server(self, ui_cmd_obj, arg_dict):
        # Enter the DNS Server
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                    "textfield[name=ntpServer] => .x-form-text")

        return ui_cmd_obj

    def sites_configure_ztp_set_starting_ip_address(self, ui_cmd_obj, arg_dict):
        # Enter the Starting IP
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']),
                                    "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                    "textfield[name=ztpDefaultSubnet] => .x-form-text")

        return ui_cmd_obj

    def sites_configure_ztp_set_admin_profile(self, ui_cmd_obj, arg_dict):
        # Select the Admin Profile
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=ztpProfile] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=ztpProfile] boundlist => :textEquals(' + arg_dict['the_value'] + ')')

        return ui_cmd_obj

    def sites_configure_ztp_set_poll_group(self, ui_cmd_obj, arg_dict):
        # Select the Poll Group
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=ztpPollGroup] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=ztpPollGroup] boundlist => :textEquals(' + arg_dict['the_value'] + ')')

        return ui_cmd_obj

    def sites_configure_ztp_set_poll_type(self, ui_cmd_obj, arg_dict):
        # Select the Poll Type
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=ztpMonitorType] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=ztpMonitorType] boundlist => :textEquals(' + arg_dict['the_value'] + ')')

        return ui_cmd_obj

    def sites_configure_ztp_set_lacp_enabled(self, ui_cmd_obj, arg_dict):
        # Determine the current selection state of the check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                                      "checkbox[name=lacp]", "[0].rawValue")

        # Only click the check button if it is not currently in the correct state
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   'checkbox[name=lacp] => .x-form-cb-input')
        else:
            self.logger.log_info("\nLACP 'Enabled' check button already at desired value.\n")

        return ui_cmd_obj

    def sites_configure_ztp_set_lacp_type(self, ui_cmd_obj, arg_dict):
        # Select the LACP Type
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=lacpLogging] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=lacpLogging] boundlist => :textEquals(' + arg_dict['the_value'] + ')')

        return ui_cmd_obj

    def sites_configure_ztp_set_lldp_enabled(self, ui_cmd_obj, arg_dict):
        # Determine the current selection state of the check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                                      "checkbox[name=lldp]", "[0].rawValue")

        # Only click the check button if it is not currently in the correct state
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   'checkbox[name=lldp] => .x-form-cb-input')
        else:
            self.logger.log_info("\nLLDP 'Enabled' check button already at desired value.\n")

        return ui_cmd_obj

    def sites_configure_ztp_set_lldp_type(self, ui_cmd_obj, arg_dict):
        # Select the LLDP Type
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=lldpLogging] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=lldpLogging] boundlist => :textEquals(' + arg_dict['the_value'] + ')')

        return ui_cmd_obj

    def sites_configure_ztp_set_mstp_enabled(self, ui_cmd_obj, arg_dict):
        # Determine the current selection state of the check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                                      "checkbox[name=spanningTree]", "[0].rawValue")

        # Only click the check button if it is not currently in the correct state
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   'checkbox[name=spanningTree] => .x-form-cb-input')
        else:
            self.logger.log_info("\nMSTP 'Enabled' check button already at desired value.\n")

        return ui_cmd_obj

    def sites_configure_ztp_set_mstp_type(self, ui_cmd_obj, arg_dict):
        # Select the MSTP Type
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=spanningTreeLogging] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=spanningTreeLogging] boundlist => :textEquals(' + arg_dict['the_value'] +
                               ')')

        return ui_cmd_obj

    def sites_configure_ztp_set_mvrp_enabled(self, ui_cmd_obj, arg_dict):
        # Determine the current selection state of the check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                                      "checkbox[name=mvrp]", "[0].rawValue")

        # Only click the check button if it is not currently in the correct state
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   'checkbox[name=mvrp] => .x-form-cb-input')
        else:
            self.logger.log_info("\nMVRP 'Enabled' check button already at desired value.\n")

        return ui_cmd_obj

    def sites_configure_ztp_set_mvrp_type(self, ui_cmd_obj, arg_dict):
        # Select the MVRP Type
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=mvrpLogging] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=mvrpLogging] boundlist => :textEquals(' + arg_dict['the_value'] + ')')

        return ui_cmd_obj

    def sites_configure_ztp_set_poe_enabled(self, ui_cmd_obj, arg_dict):
        # Determine the current selection state of the check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                                      "checkbox[name=poe]", "[0].rawValue")

        # Only click the check button if it is not currently in the correct state
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   'checkbox[name=poe] => .x-form-cb-input')
        else:
            self.logger.log_info("\nPOE 'Enabled' check button already at desired value.\n")

        return ui_cmd_obj

    def sites_configure_ztp_set_poe_type(self, ui_cmd_obj, arg_dict):
        # Select the POE Type
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=poeLogging] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=poeLogging] boundlist => :textEquals(' + arg_dict['the_value'] + ')')

        return ui_cmd_obj

    def sites_configure_ztp_set_vxlan_enabled(self, ui_cmd_obj, arg_dict):
        # Determine the current selection state of the check button
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj,
                                                      "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                                                      "checkbox[name=vxlan]", "[0].rawValue")

        # Only click the check button if it is not currently in the correct state
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["the_value"]):
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   'checkbox[name=vxlan] => .x-form-cb-input')
        else:
            self.logger.log_info("\nVXLAN 'Enabled' check button already at desired value.\n")

        return ui_cmd_obj

    def sites_configure_ztp_set_vxlan_type(self, ui_cmd_obj, arg_dict):
        # Select the VXLAN Type
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=vxlanLogging] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'combo[name=vxlanLogging] boundlist => :textEquals(' + arg_dict['the_value'] + ')')

        return ui_cmd_obj

    def sites_configure_click_cancel(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("\nTO DO: make sure button is enabled.\n")
        # Click the Cancel button
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                               "button[actionId=editSiteCancel] => .x-btn-inner-default-small")

        return ui_cmd_obj

    def sites_configure_click_configure_devices(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("\nTO DO: make sure button is enabled.\n")
        # Click the Configure Devices button
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                               "button[actionId=editSiteDevices] => .x-btn-inner-default-small")

        return ui_cmd_obj

    def sites_configure_click_discover(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("\nTO DO: make sure button is enabled.\n")
        # Click the Discover button
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                               "button[actionId=discover] => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def sites_configure_click_save(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("\nTO DO: make sure button is enabled.\n")
        # Click the Save button
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                               "button[actionId=editSiteSave] => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def sites_configure_click_scheduler(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("\nTO DO: make sure button is enabled.\n")
        # Click the Configure Devices button
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel "
                               "button[actionId=doSiteScheduler] => .x-btn-inner-default-small")

        return ui_cmd_obj

    def sites_dialog_address_set_type(self, ui_cmd_obj, arg_dict):
        # Select the Discovery Type
        self.ext_builder.click(ui_cmd_obj, '#addressTypeCombo => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, '#addressTypeCombo boundlist => :textEquals(' + arg_dict['the_value'] + ')')

        return ui_cmd_obj

    def sites_dialog_address_set_subnet(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']), '#addressSubnetField => .x-form-text')

        return ui_cmd_obj

    def sites_dialog_address_set_seed_address(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']), '#addressSeedField => .x-form-text')

        return ui_cmd_obj

    def sites_dialog_address_set_start_address(self, ui_cmd_obj, arg_dict):
        # Enter the Start Address
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']), "#addressStartField => .x-form-text")

        return ui_cmd_obj

    def sites_dialog_address_set_end_address(self, ui_cmd_obj, arg_dict):
        # Enter the End Address
        self.ext_builder.enter_text(ui_cmd_obj, str(arg_dict['the_value']), "#addressEndField => .x-form-text")

        return ui_cmd_obj

    def sites_dialog_address_click_ok(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("\nTO DO: check enabled state of button\n")
        self.ext_builder.click(ui_cmd_obj, "#addAddressOkBtn => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def sites_dialog_address_click_cancel(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "window[title=Add Address] button[text=Cancel] => .x-btn-inner-default-small")

        return ui_cmd_obj

    def sites_confirm_site_exists(self, ui_cmd_obj, arg_dict):
        # Look for the map in the tree
        self.ext_builder.component_query(ui_cmd_obj,
                                         '#networkTabPanel #networkDevicesTab treeview', '[0].store.data.length')
        item_count = int(ui_cmd_obj.return_data)
        item_count += 1

        # Assume we won't find the map
        found_item = False

        # Loop through the table and see if the specified site exists
        item_index = 0
        for x in range(0, item_count):
            self.ext_builder.component_query(ui_cmd_obj,
                                             '#networkTabPanel #networkDevicesTab treeview',
                                             '[0].store.data.items[' + str(item_index) + '].data.name')
            if ui_cmd_obj.return_data == arg_dict['site_name']:
                self.logger.log_info("\nFound site '" + arg_dict['site_name'] + "' at index " + str(item_index) + "\n")
                found_item = True
                break
            else:
                item_index += 1

        # Determine if we passed or failed the test, depending on what we expected (exists/not)
        if found_item is StringUtils.string_to_boolean(arg_dict["exists"]):
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        return ui_cmd_obj
