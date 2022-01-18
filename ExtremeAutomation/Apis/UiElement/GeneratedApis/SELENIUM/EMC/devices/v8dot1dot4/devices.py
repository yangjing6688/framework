from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.devices.v8dot1dot3.devices import Devices as \
    DevicesBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Devices(DevicesBase):
    def devices_device_view_enable_port(self, ui_cmd_obj, arg_dict):
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel portTreePanel treeview => .x-tree-node-text:textEquals(' +
                                     str(arg_dict['port_name']) + ')')

        self.ext_builder.click(ui_cmd_obj, '#portTreeMenu{isVisible()} menuitem[text=Enable Port] => .x-menu-item-text')

        return ui_cmd_obj

    def devices_device_view_disable_port(self, ui_cmd_obj, arg_dict):
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel portTreePanel treeview => .x-tree-node-text:textEquals(' +
                                     str(arg_dict['port_name']) + ')')

        self.ext_builder.click(ui_cmd_obj,
                               '#portTreeMenu{isVisible()} menuitem[text=Disable Port] => .x-menu-item-text')

        return ui_cmd_obj

    def devices_maps_add_to_map(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               '#networkTabPanel #networkDevicesTab #devicesTreeContextTabPanel '
                               'deviceGrid[viewId=DeviceTable] button[iconCls=fa fa-bars] => .fa')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Maps] => .x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, '#activeContextMenu{isVisible()} menuitem[text=Add To Map...] => '
                               '.x-menu-item-text')
        self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Map] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combo[fieldLabel=Map] boundlist => '
                               ':textEquals(' + arg_dict['map_path'] + ')')
        self.ext_builder.click(ui_cmd_obj, 'mapSelectionWindow[title=Add To Map] button[text=OK] => .x-btn-button')

        return ui_cmd_obj
