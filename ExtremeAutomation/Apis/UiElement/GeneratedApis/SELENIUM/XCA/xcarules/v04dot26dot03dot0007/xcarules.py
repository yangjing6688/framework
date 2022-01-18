from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as XcarulesBase
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class Xcarules(XcarulesBase):
    def click_add_to_create_new_rule(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-click='$parent.onCreate()']")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def click_rule_name_to_open_rule_settings(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcarules, self).click_rule_name_to_open_rule_settings(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def click_rule_name_to_move_up(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcarules, self).click_rule_name_to_move_up(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def click_rule_name_to_move_down(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcarules, self).click_rule_name_to_move_down(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def config_rule_name_and_enabled(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict["rule_name"], "//input[@id='name']")
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//md-checkbox[@id='ruleEnabled']", "aria-checked", "true")
        if StringUtils.string_to_boolean(arg_dict['rule_enabled']) is ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//md-checkbox[@id='ruleEnabled']")
        ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def config_rule_conditions(self, ui_cmd_obj, arg_dict):
        if arg_dict["user_group"] is not None:
            self.builder.click(ui_cmd_obj,
                               "//div/label[.='User Group']/..//following-sibling::div//option[@label='" +
                               str(arg_dict["user_group"]) + "']")
        if arg_dict["end_sys_group"] is not None:
            self.builder.click(ui_cmd_obj,
                               "//div/label[.='End-System Group']/..//following-sibling::div//option[@label='" +
                               str(arg_dict["end_sys_group"]) + "']")
        if arg_dict["device_type_group"] is not None:
            self.builder.click(ui_cmd_obj,
                               "//div/label[.='Device Type Group']/..//following-sibling::div//option[@label='" +
                               str(arg_dict["device_type_group"]) + "']")
        if arg_dict["location_group"] is not None:
            self.builder.click(ui_cmd_obj,
                               "//div/label[.='Location Group']/..//following-sibling::div//option[@label='" +
                               str(arg_dict["location_group"]) + "']")

        return ui_cmd_obj

    def config_rule_actions(self, ui_cmd_obj, arg_dict):
        if arg_dict["accept_policy_name"] is not None:
            self.builder.click(ui_cmd_obj,
                               "//div/label[.='Accept Policy']/..//following-sibling::div//option[@label='" +
                               str(arg_dict["accept_policy_name"]) + "']")
        if arg_dict["portal_name"] is not None:
            self.builder.click(ui_cmd_obj,
                               "//div/label[.='Portal']/..//following-sibling::div//option[@label='" +
                               str(arg_dict["portal_name"]) + "']")

        return ui_cmd_obj

    def save_config_and_back_to_rules_page(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-show='$parent.canSave' and @aria-disabled='false']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='setBack()']")

        return ui_cmd_obj

    def delete_rule_in_rules_page(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//tr[@ng-repeat='rule in rules']//td[.='" + str(arg_dict["rule_name"]) + "']")
        self.builder.click(ui_cmd_obj, "//i[@ng-click='confirmDeleteRule()' and @role='button']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='deleteRule(this, rule)']")

        return ui_cmd_obj

    def delete_rule_in_config_page(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcarules, self).delete_rule_in_config_page(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def verify_control_rule_exists(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//tr[@ng-repeat='rule in rules']//td[.='" +
                                  str(arg_dict["rule_name"]) + "']")
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Rule " + str(arg_dict["rule_name"]) + " doesn't exist.")
        else:
            self.logger.log_debug("Rule " + str(arg_dict["rule_name"]) + " already exist.")

        return ui_cmd_obj

    def verify_control_rule_does_not_exist(self, ui_cmd_obj, arg_dict):
        self.builder.find_element(ui_cmd_obj, "//tr[@ng-repeat='rule in rules']//td[.='" +
                                  str(arg_dict["rule_name"]) + "']")
        if ui_cmd_obj.error_state:
            ui_cmd_obj.error_state = False
            self.logger.log_debug("Rule " + str(arg_dict["rule_name"]) + " doesn't exist.")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_debug("Rule " + str(arg_dict["rule_name"]) + " still exist.")

        return ui_cmd_obj
