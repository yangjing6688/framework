from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.XCA.xcanetworks.v04dot26dot03dot0007.xcanetworks import \
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

        return ui_cmd_obj

    def delete_network(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@class='ui-grid-cell-contents ng-binding ng-scope' and .='" +
                           str(arg_dict['network_name']) + "']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='$parent.showDelete()']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='delete(this)']")

        return ui_cmd_obj
