from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.maps.v8dot1dot3.maps import Maps as MapsBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Maps(MapsBase):
    def maps_select_map(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab deviceTree[title=Tree View] treeview '
                               '=> .x-tree-node-text span:textEquals(' + arg_dict['map_name'] + ')')
        return ui_cmd_obj

    def maps_edit_map(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton => .fa')
        self.ext_builder.click(ui_cmd_obj, r'#networkTabPanel #networkDevicesTab #DeviceTreeActionButton '
                               r'#deviceTreeMenuMap menuitem[text=Maps\/Sites] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #DeviceTreeActionButton '
                               '#deviceTreeMenuMap menuitem[text=Edit Map] => .x-menu-item-text')
        return ui_cmd_obj

    def maps_rename_map(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#mapPropertyMenuButton2 => .x-btn-inner-default-toolbar-small')
        self.ext_builder.click(ui_cmd_obj, '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               '#mapPropertyMenuButton2 #showPropertiesAction => .x-menu-item-text')
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['map_name'], '#mapPropertiesWindow #mapPropertiesInnerForm '
                                    'textfield[fieldLabel=Name] => .x-form-text')
        self.ext_builder.click(ui_cmd_obj, '#mapPropertiesWindow button[text=Save] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def maps_confirm_maps_menu_exists(self, ui_cmd_obj, arg_dict):
        # Check if the context menu has been built yet
        ui_cmd_obj = self.ext_builder.component_query(ui_cmd_obj, '#activeContextMenu', '[0]')
        if ui_cmd_obj.return_data is None:
            # Context menu has not been built yet, so display it then hide it so we can query the menu picks
            self.ext_builder.click(ui_cmd_obj,
                                   '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                                   '#networkPrimaryDeviceGrid button[iconCls=fa fa-bars] => .fa')
            self.ext_builder.click(ui_cmd_obj,
                                   '#activeContextMenu{isVisible()} menuitem[text=Maps] => '
                                   '.x-menu-item-text')

        # Check if the specified menu is present - the query returns True if the menu is HIDDEN
        self.ext_builder.component_query(ui_cmd_obj, '#activeContextMenu menuitem[text=' + arg_dict["menu_name"] + ']',
                                         '[0].hidden')

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
