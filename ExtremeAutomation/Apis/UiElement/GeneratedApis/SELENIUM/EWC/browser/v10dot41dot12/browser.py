from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as BrowserBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Browser(BrowserBase):
    def login(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict["username"], "//input[@name='loginID']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["password"], "//input[@name='loginPwd']")
        self.builder.click(ui_cmd_obj, "//button[.='Login']")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def open_web_page(self, ui_cmd_obj, arg_dict):
        self.builder.open_web_page(ui_cmd_obj, arg_dict["browser"], arg_dict["url"])

        return ui_cmd_obj

    def close_web_page(self, ui_cmd_obj, arg_dict):
        self.builder.close_web_page(ui_cmd_obj)

        return ui_cmd_obj
