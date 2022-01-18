from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.XCA.xcarules.v04dot26dot03dot0007.xcarules import \
    Xcarules as XcarulesBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Xcarules(XcarulesBase):
    def save_config_and_back_to_rules_page(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-show='$parent.canSave' and @aria-hidden='false']")
        self.builder.delay(ui_cmd_obj, 2000)
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//*[@uib-tooltip='OnBoard']", "aria-expanded", "true")
        if ui_cmd_obj.error_state is True:
            ui_cmd_obj.error_state = False
            self.builder.click(ui_cmd_obj, "//*[@uib-tooltip='OnBoard']")
        self.builder.click(ui_cmd_obj, "//*[@id='side-menu-onboard']//a[contains(text(),'Rules')]")

        return ui_cmd_obj
