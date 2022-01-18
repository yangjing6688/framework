from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as GimbrowserBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Gimbrowser(GimbrowserBase):
    def browser_login(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict["username"], 'username', self.builder.constants.STRATEGY_NAME)
        self.builder.click(ui_cmd_obj, 'password', self.builder.constants.STRATEGY_NAME)
        self.builder.enter_text(ui_cmd_obj, arg_dict["password"], 'password',
                                self.builder.constants.STRATEGY_NAME)
        self.builder.click(ui_cmd_obj, "//button[@type='submit']")
        self.wait_for_page_load_completely(ui_cmd_obj)

        return ui_cmd_obj

    def browser_open_web_page(self, ui_cmd_obj, arg_dict):
        self.builder.open_web_page(ui_cmd_obj, arg_dict["browser"], arg_dict["url"], implicit_wait=6)
        self.wait_for_page_load_completely(ui_cmd_obj)

        return ui_cmd_obj

    def browser_logout(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@role='presentation']/div[@role='presentation']/"
                           "div[@role='presentation']/div/a[2]")
        self.builder.click(ui_cmd_obj, "//a/span[text()='Logout']")
        self.wait_for_page_load_completely(ui_cmd_obj)

        return ui_cmd_obj

    def browser_close_web_page(self, ui_cmd_obj, arg_dict):
        self.builder.close_web_page(ui_cmd_obj)

        return ui_cmd_obj

    def browser_only_url(self, ui_cmd_obj, arg_dict):
        self.builder.open_web_page(ui_cmd_obj, arg_dict["browser"], arg_dict["url"], implicit_wait=3,
                                   delete_all_cookies=True)
        self.wait_for_page_load_completely(ui_cmd_obj)

        return ui_cmd_obj

    def wait_for_page_load_completely(self, ui_cmd_obj):
        self.logger.log_info("waiting for the page to load...")
        for x in range(1, 25):
            self.base_builder.delay(ui_cmd_obj, 250)
            self.base_builder.execute_script(ui_cmd_obj, "return document.readyState;")
            self.logger.log_info("page readyState:  " + str(ui_cmd_obj.return_data))
            if ui_cmd_obj.return_data == "complete":
                self.logger.log_info("page loaded completely: ")
                break

        return ui_cmd_obj
