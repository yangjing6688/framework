from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as DfndrbrowserBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Dfndrbrowser(DfndrbrowserBase):
    def dfndr_browser_login(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict["username"], 'username', self.builder.constants.STRATEGY_ID)
        self.builder.click(ui_cmd_obj, "//input[@type='password']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["password"], "//input[@type='password']")
        self.builder.click(ui_cmd_obj, "//button[@id='loginButton' or @type='submit']")
        self.wait_for_page_load_completely(ui_cmd_obj)

        return ui_cmd_obj

    def dfndr_browser_open_web_page(self, ui_cmd_obj, arg_dict):
        self.builder.open_web_page(ui_cmd_obj, arg_dict["browser"], arg_dict["url"])
        self.wait_for_page_load_completely(ui_cmd_obj)

        return ui_cmd_obj

    def dfndr_browser_logout(self, ui_cmd_obj, arg_dict):
        if arg_dict['app_name'] == "defender":
            self.logger.log_info("defender")
            self.builder.click(ui_cmd_obj, "//button[@class='mat-button ng-star-inserted']")
            self.builder.click(ui_cmd_obj, "//span[text()='Logout']")
            self.wait_for_page_load_completely(ui_cmd_obj)
        if arg_dict['app_name'] == "xca":
            self.logger.log_info("xca")
            self.builder.click(ui_cmd_obj, "//a[contains(text(),'admin')]")
            self.builder.click(ui_cmd_obj, "//a[contains(text(),'Logout')]")
            self.wait_for_page_load_completely(ui_cmd_obj)

        return ui_cmd_obj

    def dfndr_browser_close_web_page(self, ui_cmd_obj, arg_dict):
        self.builder.close_web_page(ui_cmd_obj)

        return ui_cmd_obj

    def dfndr_browser_only_url(self, ui_cmd_obj, arg_dict):
        self.builder.driver.get(arg_dict['url'])

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
