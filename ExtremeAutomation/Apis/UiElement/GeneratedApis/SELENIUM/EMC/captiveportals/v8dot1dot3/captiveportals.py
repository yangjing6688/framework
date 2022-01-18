from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as CaptiveportalsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Captiveportals(CaptiveportalsBase):
    def captive_portals_admin_click_save_button_on_administration_page(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "//span[contains(@class, 'x-btn-inner-blue-small') and .='Save']",
                               strategy=self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def captive_portals_admin_select_login_config(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         "#nacConfigCenterPanel panel[title=Administration]#configContentPanel "
                                         "gridview", '[0].store.data.items.length')
        end_index = ui_cmd_obj.return_data
        self.logger.log_debug("End index is " + str(end_index))
        if not end_index:
            ui_cmd_obj.error_state = True
            return ui_cmd_obj
        index = 0
        while index < end_index:
            self.ext_builder.component_query(ui_cmd_obj,
                                             "#nacConfigCenterPanel panel[title=Administration]#configContentPanel "
                                             "gridview", '[0].store.data.items[' + str(index) + '].data.user')

            if arg_dict['user_name'] in ui_cmd_obj.return_data:
                index += 1
                self.ext_builder.click(ui_cmd_obj,
                                       "#nacConfigCenterPanel panel[title=Administration]#configContentPanel "
                                       "gridview => .x-grid-item:nth-of-type(" +
                                       str(index) + ") .x-grid-cell-first .x-grid-cell-inner")
                break
            elif ui_cmd_obj.return_data != u'':
                index += 1
            else:
                ui_cmd_obj.error_state = True
                break

        return ui_cmd_obj

    def captive_portals_admin_verify_existence_of_login_config(self, ui_cmd_obj, arg_dict):
        self.ext_builder.component_query(ui_cmd_obj,
                                         "#nacConfigCenterPanel panel[title=Administration]#configContentPanel "
                                         "gridview", '[0].store.data.items.length')
        max_index = max(range(int(ui_cmd_obj.return_data)))
        for index in range(int(ui_cmd_obj.return_data)):
            self.ext_builder.component_query(ui_cmd_obj,
                                             "#nacConfigCenterPanel panel[title=Administration]#configContentPanel "
                                             "gridview", '[0].store.data.items[' + str(index) + '].data.user')
            if arg_dict['user_name'] == str(ui_cmd_obj.return_data):
                self.logger.log_debug("Administrative login configuration with username: " +
                                      str(arg_dict["user_name"]) + " is displayed in the grid.")
                break
            elif index is max_index:
                self.logger.log_debug("Administrative login configuration with username: " +
                                      str(arg_dict["user_name"]) + " is NOT displayed in the grid.")

        return ui_cmd_obj

    def captive_portals_admin_click_add_login_config_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               r"#nacConfigTab #nacConfigCenterPanel panel[title=Administration]#configContentPanel "
                               r"button[text=Add\.\.\.] => .x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def captive_portals_admin_click_delete_login_config_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#nacConfigTab #nacConfigCenterPanel panel[title=Administration]#configContentPanel "
                               "button[text=Delete] => .x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def captive_portals_admin_click_edit_login_config_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "#configContentPanel button[iconCls=edit] => .x-btn-inner-default-toolbar-small")

        return ui_cmd_obj

    def captive_portals_admin_delete_login_config(self, ui_cmd_obj, arg_dict):
        self.captive_portals_admin_select_login_config(ui_cmd_obj, arg_dict)
        self.captive_portals_admin_click_delete_login_config_button(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj, "#yes => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def captive_portals_admin_select_authentication_for_login_config(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "combo[name=auth] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "combo[name=auth] boundlist => :textEquals(" + arg_dict["auth_name"] + ")")

        return ui_cmd_obj

    def captive_portals_admin_add_new_user_for_login_config(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "localPasswordRepoUserCombo[name=user] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, r"localPasswordRepoUserCombo[name=user] boundlist => "
                                           r"div:textEquals(New\.\.\.)")

        return ui_cmd_obj

    def captive_portals_admin_select_user_for_login_config(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "localPasswordRepoUserCombo[name=user] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "localPasswordRepoUserCombo[name=user] boundlist => div:textEquals(" +
                               arg_dict["user_name"] + ")")

        return ui_cmd_obj

    def captive_portals_admin_select_role_for_login_config(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "roleCombo[name=role] => .x-form-trigger")
        self.ext_builder.click(ui_cmd_obj, "roleCombo[name=role] boundlist => div:textEquals(" +
                               arg_dict["role_name"] + ")")

        return ui_cmd_obj

    def captive_portals_admin_click_add_button_save_login_config(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "button[text=Add] => .x-btn-inner-blue-small")

        return ui_cmd_obj

    def captive_portals_admin_click_save_button_save_login_config(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj,
                               "portalAdminAddEditRoleDialog[title=Edit Login Configuration] button[text=Save] => "
                               ".x-btn-inner-blue-small")

        return ui_cmd_obj

    def captive_portals_admin_fill_mandatory_user_info_on_edit_user_window(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['display_name'], "textfield[name=displayName] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['user_name'], "textfield[name=username] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['password'], "passwordfield[name=pass] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['verify_password'], "passwordfield[name=pass_verify] => "
                                                                             ".x-form-text")

        return ui_cmd_obj

    def captive_portals_admin_fill_optional_user_info_on_edit_user_window(self, ui_cmd_obj, arg_dict):
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['first_name'], "textfield[name=firstName] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['last_name'], "textfield[name=lastName] => .x-form-text")
        self.ext_builder.enter_text(ui_cmd_obj, arg_dict['description'], "textfield[name=desc] => .x-form-text")

        return ui_cmd_obj

    def captive_portals_admin_click_ok_button_on_edit_user_window(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, "localPasswordRepoEditDialog[title=Edit User] button[text=OK] => "
                                           ".x-btn-inner-blue-small")

        return ui_cmd_obj
