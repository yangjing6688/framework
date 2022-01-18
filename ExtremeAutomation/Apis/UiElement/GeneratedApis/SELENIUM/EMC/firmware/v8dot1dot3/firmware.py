from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.firmware.v8dot1dot1.firmware import Firmware as \
    FirmwareBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Firmware(FirmwareBase):
    def firmware_tab_tree_expand_node(self, ui_cmd_obj, arg_dict):
        self.ext_builder.expand_tree_node(ui_cmd_obj,
                                          '#networkTabPanel #networkFirmwareTab firmwareTree treeview',
                                          '[0]', 'text', arg_dict['node_name'], exact_match=False)
        return ui_cmd_obj

    def firmware_tab_menu_set_as_reference_image_tree(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu of the tree
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkFirmwareTab firmwareTree => '
                                     '.x-tree-node-text:contains(' + str(arg_dict["image_name"]) + ')')
        self.ext_builder.click(ui_cmd_obj, 'menuitem[text=Set as Reference Image] => .x-menu-item-text')

        return ui_cmd_obj

    def firmware_tab_menu_unset_as_reference_image_tree(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu of the tree
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkFirmwareTab firmwareTree => '
                                     '.x-tree-node-text:contains(' + str(arg_dict["image_name"]) + ')')
        self.ext_builder.click(ui_cmd_obj, 'menuitem[text=Unset as Reference Image] => .x-menu-item-text')

        return ui_cmd_obj

    def firmware_tab_menu_delete_image_tree(self, ui_cmd_obj, arg_dict):
        # Access the menu pick from the context menu of the tree
        self.ext_builder.right_click(ui_cmd_obj,
                                     '#networkTabPanel #networkFirmwareTab firmwareTree => '
                                     '.x-tree-node-text:contains(' + str(arg_dict["image_name"]) + ')')
        self.ext_builder.click(ui_cmd_obj, 'menuitem[text=Delete Image] => .x-menu-item-text')

        return ui_cmd_obj
