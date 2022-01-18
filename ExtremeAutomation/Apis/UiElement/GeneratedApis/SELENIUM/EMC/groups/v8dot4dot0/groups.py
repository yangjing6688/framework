from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.groups.v8dot3dot0.groups import Groups as GroupsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Groups(GroupsBase):
    def groups_click_add_group_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Add a new group']")

        return ui_cmd_obj

    def groups_click_delete_group_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Delete selected group(s)']")

        return ui_cmd_obj

    def groups_click_edit_group_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Edit selected group']")

        return ui_cmd_obj

    def groups_click_refresh_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Reload the table']")

        return ui_cmd_obj

    def groups_dialog_set_group_name(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict["group_name"],
                                "//input[@placeholder='A unique name for this group...']")

        return ui_cmd_obj

    def groups_dialog_select_group_type(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj,
                           "//span[contains(@class, 'x-form-item-label-inner') and .='Type:']/../following-sibling::"
                           "div//div[contains(@class, 'x-form-arrow-trigger-default') and contains(@id, 'combo-')]")
        self.builder.click(ui_cmd_obj, "//li[contains(@class, 'x-boundlist-item') and .='" +
                           str(arg_dict['group_type']) + "']")

        return ui_cmd_obj

    def groups_dialog_add_location_group_entry(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Add a new entry']/span/span/span[.='Add...']")
        if arg_dict['ip_list'] != "Any":
            self.builder.click(ui_cmd_obj,
                               "//span[@class='x-form-item-label-text' and .='Switches:']/../../following-sibling::div"
                               "//div[contains(@class, 'x-form-arrow-trigger-default')]")
            self.builder.click(ui_cmd_obj, "//li[contains(@class, 'x-boundlist-item') and .='List']")
            self.builder.enter_text(ui_cmd_obj, arg_dict["ip_list"], "//*[@name='switchValue']")
        if arg_dict['intf_type'] == "Wired":
            self.ext_builder.click(ui_cmd_obj, 'combo[name=locationType] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'combo[name=locationType] boundlist => :textEquals(Wired)')
            if arg_dict['port_or_ssid_list'] != "Any":
                self.builder.enter_text(ui_cmd_obj, arg_dict["port_or_ssid_list"], "//*[@name='portValue']")
        if arg_dict['intf_type'] == "Wireless":
            self.ext_builder.click(ui_cmd_obj, 'combo[name=locationType] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'combo[name=locationType] boundlist => :textEquals(Wireless)')
            if arg_dict['port_or_ssid_list'] != "Any":
                self.builder.enter_text(ui_cmd_obj, arg_dict["port_or_ssid_list"], "//*[@name='portValue']")
            if arg_dict['ap_list'] != "Any":
                self.builder.enter_text(ui_cmd_obj, arg_dict['ap_list'], "//*[@name='apValue']")
        self.ext_builder.click(ui_cmd_obj, 'button[text=Add] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def groups_dialog_save_group_entry(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span/span/span[.='Save']")

        return ui_cmd_obj
