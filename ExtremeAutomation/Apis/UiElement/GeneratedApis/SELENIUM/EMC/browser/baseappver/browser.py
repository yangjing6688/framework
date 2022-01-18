from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as BrowserBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from selenium.common.exceptions import WebDriverException


class Browser(BrowserBase):
    def login(self, ui_cmd_obj, arg_dict):
        attempts = 0
        max_attempts = 3
        self.base_login(ui_cmd_obj, arg_dict)
        try:
            self.builder.find_element(ui_cmd_obj, "//span[contains(@class, "
                                                  "'x-btn-inner x-btn-inner-extr-nav-toolbar-button-small') "
                                                  "and text() = 'Network']")
            if ui_cmd_obj.error_state is True or ui_cmd_obj.return_text.text != "Network":
                while attempts < max_attempts:
                    ui_cmd_obj.error_state = False
                    current_url = self.builder.driver.current_url
                    self.builder.close_web_page(ui_cmd_obj)
                    self.ext_builder.delay(ui_cmd_obj, 5000)
                    self.builder.open_web_page(ui_cmd_obj, arg_dict["browser"], current_url)
                    self.ext_builder.delay(ui_cmd_obj, 1000)
                    self.base_login(ui_cmd_obj, arg_dict)
                    self.builder.find_element(ui_cmd_obj, "//span[contains(@class, "
                                                          "'x-btn-inner x-btn-inner-extr-nav-toolbar-button-small') "
                                                          "and text() = 'Network']")
                    if ui_cmd_obj.error_state is True or ui_cmd_obj.return_text.text != "Network":
                        attempts += 1
                    else:
                        return ui_cmd_obj
                return ui_cmd_obj
            else:
                return ui_cmd_obj
        except WebDriverException:
            ui_cmd_obj.error_state = True
            return ui_cmd_obj

    def open_web_page(self, ui_cmd_obj, arg_dict):
        attempts = 0
        max_attempts = 3
        self.builder.open_web_page(ui_cmd_obj, arg_dict["browser"], arg_dict["url"])
        try:
            self.builder.find_element(ui_cmd_obj, "//*[contains(@name,'j_username')]")
            if ui_cmd_obj.error_state is True:
                while attempts < max_attempts:
                    ui_cmd_obj.error_state = False
                    self.builder.close_web_page(ui_cmd_obj)
                    self.ext_builder.delay(ui_cmd_obj, 5000)
                    self.builder.open_web_page(ui_cmd_obj, arg_dict["browser"], arg_dict["url"])
                    self.ext_builder.delay(ui_cmd_obj, 1000)
                    self.builder.find_element(ui_cmd_obj, "//*[contains(@name,'j_username')]")
                    if ui_cmd_obj.error_state is True:
                        attempts += 1
                    else:
                        return ui_cmd_obj
                return ui_cmd_obj
            else:
                return ui_cmd_obj
        except WebDriverException:
            ui_cmd_obj.error_state = True
            return ui_cmd_obj

    def close_web_page(self, ui_cmd_obj, arg_dict):
        self.builder.close_web_page(ui_cmd_obj)

        return ui_cmd_obj

    def base_login(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict["username"], "input[name=j_username]")
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict["password"], "input[name=j_password]")
        self.ext_builder.click(ui_cmd_obj, "button[type=submit]", wait_for_page_load=True)
        self.ext_builder.delay(ui_cmd_obj, 7000)
        return ui_cmd_obj
