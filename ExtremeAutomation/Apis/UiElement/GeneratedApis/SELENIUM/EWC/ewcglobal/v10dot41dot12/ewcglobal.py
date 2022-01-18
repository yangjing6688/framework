from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EwcglobalBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Ewcglobal(EwcglobalBase):
    def global_authentication_check_strict_mode(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='Authentication']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@name='strict_mode']")
        checked = checkbox.get_attribute("checked")
        if not checked:
            self.builder.click(ui_cmd_obj, "//input[@name='strict_mode']")

        return ui_cmd_obj

    def global_authentication_uncheck_strict_mode(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[contains(@class, 'cnSiteLink') and .='Authentication']")
        checkbox = self.builder.driver.find_element_by_xpath("//input[@name='strict_mode']")
        checked = checkbox.get_attribute("checked")
        if checked:
            self.builder.click(ui_cmd_obj, "//input[@name='strict_mode']")

        return ui_cmd_obj

    def global_click_save_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//input[@id='save_global']")

        return ui_cmd_obj
