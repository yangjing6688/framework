from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.discovered.v8dot2dot4.discovered import Discovered as \
    DiscoveredBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Discovered(DiscoveredBase):
    def discovered_click_edit_devices(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid button[text=Configure "
                               r"Devices\.\.\.]=> .x-btn-inner-default-toolbar-small")
        return ui_cmd_obj

    def discovered_click_clear_selected(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid button[text=Clear "
                               "Selected]=> .x-btn-inner-default-toolbar-small")
        return ui_cmd_obj

    def discovered_click_clear_all_devices(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid button[text=Clear "
                               "All Devices]=> .x-btn-inner-default-toolbar-small")
        return ui_cmd_obj

    def discovered_click_pre_register_device(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid button[text=Pre-Register "
                               r"Device\.\.\.]=> .x-btn-inner-default-toolbar-small")
        return ui_cmd_obj

    def discovered_click_add_devices(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#networkTabPanel #networkDiscoveredTab #DiscoveredDevicesGrid button[text=Add "
                               r"Devices\.\.\.]=> .x-btn-inner-default-toolbar-small")
        return ui_cmd_obj
