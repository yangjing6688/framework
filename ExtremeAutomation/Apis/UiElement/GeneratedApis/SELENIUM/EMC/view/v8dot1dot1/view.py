from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as ViewBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class View(ViewBase):
    def view_select_tab(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, '>>#leftNavToolbar button[text=' + str(arg_dict['tab_name']) + ']')

        return ui_cmd_obj

    def view_menu_about(self, ui_cmd_obj, arg_dict):
        # Access the view context menu
        self.ext_builder.click(ui_cmd_obj, 'button[iconCls=fa fa-bg fa-bars] => .fa')

        # Select "About" from the view context menu
        self.ext_builder.click(ui_cmd_obj, 'menuitem[text=About] => .x-menu-item-text')

        return ui_cmd_obj

    def view_menu_logout(self, ui_cmd_obj, arg_dict):
        attempts = 0
        max_attempts = 3
        # Access the view context menu
        while attempts < max_attempts:
            self.ext_builder.click(ui_cmd_obj, 'button[iconCls=fa fa-bg fa-bars] => .fa')

            # Select "Logout" from the view context menu
            self.ext_builder.click(ui_cmd_obj, 'menuitem[text=Logout] => .x-menu-item-text')

            # Wait for the user to be logged out (login page is displayed)
            self.ext_builder.wait_for_user_log_out(ui_cmd_obj, '[name=loginform]')

            if ui_cmd_obj.error_state is True:
                attempts += 1
                ui_cmd_obj.error_state = False
            else:
                return ui_cmd_obj
        return ui_cmd_obj

    def view_confirm_logged_in(self, ui_cmd_obj, arg_dict):
        self.ext_builder.document_query(ui_cmd_obj, "#envelope .errorString", "")
        if ui_cmd_obj.return_data is None:
            self.logger.log_info("User Successfully Logged In")
            if arg_dict["logged_in"] == "True":
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True
        else:
            self.logger.log_info("User Did Not Log In Successfully")
            if arg_dict["logged_in"] == "True":
                ui_cmd_obj.error_state = True
            else:
                ui_cmd_obj.error_state = False

        return ui_cmd_obj
