from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as GroupsBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Groups(GroupsBase):
    def groups_click_add_group_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'panel[title=All Groups]#configContentPanel button[text=Add...] => '
                               '.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def groups_click_delete_group_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'panel[title=All Groups]#configContentPanel button[text=Delete] => '
                               '.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def groups_click_edit_group_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'panel[title=All Groups]#configContentPanel button[text=Edit...] => '
                               '.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def groups_click_refresh_button(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'panel[title=All Groups]#configContentPanel button[text=Refresh] => '
                               '.x-btn-inner-default-toolbar-small')

        return ui_cmd_obj

    def groups_select_group(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@class='x-grid-cell-inner ' and .='" + str(arg_dict["group_name"]) + "']")

        return ui_cmd_obj

    def groups_dialog_set_group_name(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict["group_name"], "//input[@name='groupName']")

        return ui_cmd_obj

    def groups_dialog_select_group_type(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'combo[name=groupType] => .x-form-trigger')
        self.ext_builder.click(ui_cmd_obj, 'combo[name=groupType] boundlist => :textEquals(' +
                               str(arg_dict['group_type']) + ')')

        return ui_cmd_obj

    def groups_dialog_click_create_new_group(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-blue-small' and .='Create']")

        return ui_cmd_obj

    def groups_dialog_add_ldap_user_group_entry(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Add a new entry']/span/span/span[.='Add...']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["attribute_name"], "//*[@name='attrName']")
        self.builder.enter_text(ui_cmd_obj, arg_dict["attribute_value"], "//*[@name='attrValue']")
        self.ext_builder.click(ui_cmd_obj, 'button[text=Add] => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def groups_dialog_add_location_group_entry(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//a[@data-qtip='Add a new entry']/span/span/span[.='Add...']")
        if arg_dict['ip_list'] != "Any":
            self.ext_builder.click(ui_cmd_obj, 'combo[name=switchMode] => .x-form-trigger')
            self.ext_builder.click(ui_cmd_obj, 'combo[name=switchMode] boundlist => :textEquals(List)')
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
        self.ext_builder.click(ui_cmd_obj, 'button[text=Save] => .x-btn-inner-blue-small')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def groups_dialog_save_and_close_group(self, ui_cmd_obj, arg_dict):
        self.ext_builder.click(ui_cmd_obj, 'button[text=Save & Close] => .x-btn-inner-blue-small')
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj

    def groups_delete_group(self, ui_cmd_obj, arg_dict):
        self.groups_select_group(ui_cmd_obj, arg_dict)
        self.groups_click_delete_group_button(ui_cmd_obj, arg_dict)
        self.ext_builder.click(ui_cmd_obj, '#yes => .x-btn-inner-blue-small')

        return ui_cmd_obj
