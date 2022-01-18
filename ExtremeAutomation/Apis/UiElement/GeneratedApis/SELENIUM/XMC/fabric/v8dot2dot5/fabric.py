# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.XMC.webapp.baseappver.webapp \
    import Webapp as FabricBase


class Fabric(FabricBase):
    def launch_fabric_manager(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "div[id^='deviceTree']>div>div>div>a",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        # self.builder.driver.find_element_by_css_selector("div[id^='deviceTree']>div>div>div>a").click()
        self._click_link_text(ui_cmd_obj, "View")
        self._wait_for(ui_cmd_obj, 1)
        self._click_link_text(ui_cmd_obj, "Fabric")
        self._wait_for_loading(ui_cmd_obj, 30)

        return ui_cmd_obj
