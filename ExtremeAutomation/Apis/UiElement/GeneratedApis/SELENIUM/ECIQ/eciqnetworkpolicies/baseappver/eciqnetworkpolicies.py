from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as EciqnetworkpoliciesBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Eciqnetworkpolicies(EciqnetworkpoliciesBase):
    def network_policies_click_add_network_policy_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[contains(@class,'policy-add-btn') and @data-dojo-attach-point='listAdd']")

        return ui_cmd_obj

    def network_policies_click_express_policy_setup_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[contains(@class,'policy-add-btn') "
                                       "and @data-dojo-attach-point='listAddPackage']")

        return ui_cmd_obj

    def network_policies_delete_network_policy(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@data-dojo-attach-point='policyName' and .='" +
                           arg_dict['network_policy_name'] + "']/../../div/span[@data-dojo-attach-point='delEl']")
        self.builder.click(ui_cmd_obj, "//button[@data-dojo-attach-point='yesBtn']")

        return ui_cmd_obj

    def network_policies_dialog_add_network_policy_name(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict['network_policy_name'], "//*[@data-dojo-attach-point='policyName' "
                                                                             "and @placeholder='Network Policy Name']")

        return ui_cmd_obj

    def network_policies_dialog_add_network_policy_description(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict['network_policy_desc'],
                                "//*[@data-dojo-attach-point='policyDesc']")

        return ui_cmd_obj

    def network_policies_dialog_check_routing_policy_type_checkbox(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element(ui_cmd_obj, "//*[@type='checkbox' and "
                                                            "@data-dojo-attach-point='branchRoutingCheckbox']",
                                                            "checked")
        if "true" in str(arg_dict["status"]).lower() and not bool(ui_cmd_obj.return_data):
            self.builder.click(ui_cmd_obj, "//*[@type='checkbox' and @data-dojo-attach-point='branchRoutingCheckbox']")
        elif "false" in str(arg_dict["status"]).lower() and bool(ui_cmd_obj.return_data):
            self.builder.click(ui_cmd_obj, "//*[@type='checkbox' and @data-dojo-attach-point='branchRoutingCheckbox']")

        return ui_cmd_obj

    def network_policies_dialog_check_switches_policy_type_checkbox(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element(ui_cmd_obj, "//*[@type='checkbox' and "
                                                            "@data-dojo-attach-point='switchesCheckbox']", "checked")
        if "true" in str(arg_dict["status"]).lower() and not bool(ui_cmd_obj.return_data):
            self.builder.click(ui_cmd_obj, "//*[@type='checkbox' and @data-dojo-attach-point='switchesCheckbox']")
        elif "false" in str(arg_dict["status"]).lower() and bool(ui_cmd_obj.return_data):
            self.builder.click(ui_cmd_obj, "//*[@type='checkbox' and @data-dojo-attach-point='switchesCheckbox']")

        return ui_cmd_obj

    def network_policies_dialog_check_wireless_policy_type_checkbox(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element(ui_cmd_obj, "//*[@type='checkbox' and "
                                                            "@data-dojo-attach-point='wirelessCheckbox']", "checked")
        if "true" in str(arg_dict["status"]).lower() and not bool(ui_cmd_obj.return_data):
            self.builder.click(ui_cmd_obj, "//*[@type='checkbox' and @data-dojo-attach-point='wirelessCheckbox']")
        elif "false" in str(arg_dict["status"]).lower() and bool(ui_cmd_obj.return_data):
            self.builder.click(ui_cmd_obj, "//*[@type='checkbox' and @data-dojo-attach-point='wirelessCheckbox']")

        return ui_cmd_obj

    def network_policies_dialog_click_exit_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@data-dojo-attach-point='exitBtn']")

        return ui_cmd_obj

    def network_policies_dialog_click_next_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@data-dojo-attach-point='nextBtn' and .='Next']")

        return ui_cmd_obj

    def network_policies_dialog_click_save_button(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@data-dojo-attach-point='saveButton']")

        return ui_cmd_obj

    def network_policies_dialog_click_tab_header(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[@class='wiz-item-des' and .='" + arg_dict['tab_name'] + "']")

        return ui_cmd_obj

    def network_policies_select_policy(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//*[@data-dojo-attach-point='btnCard']")
        self.builder.click(ui_cmd_obj, "//*[@data-dojo-attach-point='policyName' and .='" +
                           arg_dict['network_policy_name'] + "']")

        return ui_cmd_obj
