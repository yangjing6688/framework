from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.sites.v8dot1dot3.sites import Sites as SitesBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Sites(SitesBase):
    def sites_rename_site(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton => .fa')
        self.ext_builder.click(ui_cmd_obj, r'#networkTabPanel #networkDevicesTab #DeviceTreeActionButton '
                               r'#deviceTreeMenuMap menuitem[text=Maps\/Sites] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton #deviceTreeMenuMap '
                               'menuitem[text=Rename Site...] => .x-menu-item-text')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['site_name'], '#mapCreationRenameWindow '
                                    'textfield[fieldLabel=Name] => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#mapCreationRenameWindow button[text=OK] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def sites_validate_all_site_summary_parameters(self, ui_cmd_obj, arg_dict):
        match = True
        self.ext_builder.component_query(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                         'siteSummaryGrid[title=Site Summary] gridview', '[0].store.data.length')
        table_length = ui_cmd_obj.return_data
        table_start = 0
        while table_start < table_length:
            self.ext_builder.component_query(ui_cmd_obj, '#networkTabPanel #networkDevicesTab '
                                             '#devicesTreeContextTabPanel siteSummaryGrid[title=Site Summary] gridview',
                                             '[0].store.data.items[' + str(table_start) + '].data.location')
            if ui_cmd_obj.return_data == arg_dict['site_path']:
                self.ext_builder.component_query(ui_cmd_obj, '#networkTabPanel #networkDevicesTab '
                                                 '#devicesTreeContextTabPanel siteSummaryGrid[title=Site Summary] '
                                                             'gridview',
                                                 '[0].store.data.items[' + str(table_start) + '].data.seedsSummary')
                if ui_cmd_obj.return_data != arg_dict['seed_address']:
                    match = False
                self.ext_builder.component_query(ui_cmd_obj,
                                                 '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                 'siteSummaryGrid[title=Site Summary] gridview',
                                                 '[0].store.data.items[' +
                                                 str(table_start) + '].data.subnetsSummary')
                if ui_cmd_obj.return_data != arg_dict['subnet_address']:
                    match = False
                self.ext_builder.component_query(ui_cmd_obj,
                                                 '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                 'siteSummaryGrid[title=Site Summary]'
                                                 ' gridview',
                                                 '[0].store.data.items[' + str(table_start) + '].data.rangesSummary')

                if ui_cmd_obj.return_text != arg_dict['address_range']:
                    match = False
                self.ext_builder.component_query(ui_cmd_obj,
                                                 '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                 'siteSummaryGrid[title=Site Summary] gridview',
                                                 '[0].store.data.items[' + str(table_start) + '].data.vlanSummary')

                if ui_cmd_obj.return_data != arg_dict['vlan_summary']:
                    match = False
                self.ext_builder.component_query(ui_cmd_obj,
                                                 '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                 'siteSummaryGrid[title=Site Summary] gridview',
                                                 '[0].store.data.items[' + str(table_start) + '].data.ztpSummary')

                if ui_cmd_obj.return_data != arg_dict['ztp_summary']:
                    match = False
                self.ext_builder.component_query(ui_cmd_obj,
                                                 '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                 'siteSummaryGrid[title=Site Summary] gridview',
                                                 '[0].store.data.items[' + str(table_start) + '].data.policySummary')

                if ui_cmd_obj.return_data != arg_dict['policy_summary']:
                    match = False
                self.ext_builder.component_query(ui_cmd_obj,
                                                 '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                                 'siteSummaryGrid[title=Site Summary] gridview',
                                                 '[0].store.data.items[' + str(table_start) +
                                                 '].data.identityAndAccessSummary')

                if ui_cmd_obj.return_data != arg_dict['access_control']:
                    match = False

                if match is False:
                    ui_cmd_obj.error_state = True
                    return ui_cmd_obj
                else:
                    return ui_cmd_obj

            else:
                table_start += 1
        ui_cmd_obj.error_state = True
        return ui_cmd_obj

    def sites_confirm_sites_menu_exists(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, '#activeContextMenu', '[0]')
        if ui_cmd_obj.return_data is None:

            self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton => .fa')
            # self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton '
            #                                    '#deviceTreeMenuMap menuitem[text=Maps\/Sites] => .x-menu-item-text')
            # self.ext_builder.click(ui_cmd_obj,
            #                        '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton #deviceTreeMenuMap '
            #                        'menuitem[text=Rename Site...] => .x-menu-item-text')
            #
            # # Context menu has not been built yet, so display it then hide it so we can query the menu picks
            # self.ext_builder.click(ui_cmd_obj,
            #                        '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
            #                        '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
            # self.ext_builder.click(ui_cmd_obj,
            #                        '#activeContextMenu{isVisible()} menuitem[text=Maps] => '
            #                        '.x-menu-item-text')
        self.ext_builder.component_query(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton '
                                         '#deviceTreeMenuMap menuitem[text=' + arg_dict["menu_name"] + ']',
                                         '[0].hidden')
        # Check if the specified menu is present - the query returns True if the menu is HIDDEN

        # Pass or fail the test, based on what was expected (query info is true if the menu is HIDDEN)
        if ui_cmd_obj.return_data == 'Component query returned a value that could not be converted by selenium.':
            ui_cmd_obj.return_data = True
        if ui_cmd_obj.return_data is not StringUtils.string_to_boolean(arg_dict["exists"]):
            # PASS
            ui_cmd_obj.error_state = False
        else:
            # FAIL
            ui_cmd_obj.error_state = True

        return ui_cmd_obj
