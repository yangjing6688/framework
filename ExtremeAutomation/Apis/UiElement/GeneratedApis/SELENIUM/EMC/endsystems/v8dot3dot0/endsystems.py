from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.endsystems.v8dot2dot1.endsystems import Endsystems as \
    EndsystemsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Endsystems(EndsystemsBase):
    def endsystems_delete_device_by_mac_address(self, ui_cmd_obj, arg_dict):
        self.endsystems_select_device_by_mac_address(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj, "#endSystemsNavTab endSystemsGrid button[text=Tools] =>"
                                           ".x-btn-inner-default-toolbar-small")
        self.ext_builder.click(ui_cmd_obj, "#endSystemsNavTab menuitem[text=Delete] => .x-menu-item-text")

        if bool(arg_dict["is_force_delete"]):
            self.builder.click(ui_cmd_obj, "//label[.='Force Delete of End-System']/../span/input[@type='checkbox']")

        self.ext_builder.click(ui_cmd_obj, "#deleteEndSystemsPanel #deleteEndSystemsButton "
                                           "=> .x-btn-inner-blue-small")

        return ui_cmd_obj
