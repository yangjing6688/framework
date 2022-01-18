from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EciqbrowserBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Eciqbrowser(EciqbrowserBase):
    def login(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict["username"], "//input[@name='username']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["password"], "//input[@name='password']")
        self.builder.click(ui_cmd_obj, "//input[@class='blue-button']", wait_for_page_load=True)
        self.builder.delay(ui_cmd_obj, 7000)
        return ui_cmd_obj

    def open_web_page(self, ui_cmd_obj, arg_dict):
        self.builder.open_web_page(ui_cmd_obj, arg_dict["browser"], arg_dict["url"])
        return ui_cmd_obj

    def close_web_page(self, ui_cmd_obj, arg_dict):
        self.builder.close_web_page(ui_cmd_obj)

        return ui_cmd_obj

    def click_do_not_show_again_checkbox(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@class='dijitReset dijitCheckBoxInput']")

        return ui_cmd_obj

    def click_close_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@data-dojo-attach-point='containerNode' and .='Close']")

        return ui_cmd_obj

    def bypass_certificate_popup(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//*[contains(@class,'certificate-expiration-warning')]")
        if ui_cmd_obj.error_state is True:
            ui_cmd_obj.error_state = False
        else:
            self.click_do_not_show_again_checkbox(ui_cmd_obj, arg_dict)
            self.click_close_button(ui_cmd_obj, arg_dict)

        return ui_cmd_obj
