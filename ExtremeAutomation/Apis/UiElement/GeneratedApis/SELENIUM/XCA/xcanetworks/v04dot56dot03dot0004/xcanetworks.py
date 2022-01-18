from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.XCA.xcanetworks.v04dot36dot01dot0097.xcanetworks import \
    Xcanetworks as XcanetworksBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Xcanetworks(XcanetworksBase):
    def save_settings_and_back_to_networks_page(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-show='$parent.canSave' and @aria-hidden='false']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='closeDialog(false)']")
        self.builder.delay(ui_cmd_obj, 2000)
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//*[@uib-tooltip='Configure']", "aria-expanded", "true")
        if ui_cmd_obj.error_state:
            ui_cmd_obj.error_state = False
            self.builder.click(ui_cmd_obj, "//*[@uib-tooltip='Configure']")
        self.builder.click(ui_cmd_obj, "//*[@id='side-menu-configure']//*[@uib-tooltip='Networks']")
        self.builder.click(ui_cmd_obj, "//*[@href='#/networks/configure' and @uib-tooltip='WLANs']")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj
