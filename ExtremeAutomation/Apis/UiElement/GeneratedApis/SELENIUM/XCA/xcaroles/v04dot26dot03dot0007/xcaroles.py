from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as XcarolesBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Xcaroles(XcarolesBase):
    def edit_role_name(self, ui_cmd_obj, arg_dict):
        self.builder.enter_text(ui_cmd_obj, arg_dict['policy_role_name'], "//input[@id='name']")

        return ui_cmd_obj

    def delete_policy_role(self, ui_cmd_obj, arg_dict):
        self.click_policy_role_name_to_open_role_settings(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//button[@ng-click='$parent.showDelete()']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='delete(this)']")

        return ui_cmd_obj

    def create_network_rule_on_policy_role(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//md-icon[contains(@ng-show, 'ruleToggle.l3Rules') "
                                                            "and .='expand_more']", "aria-hidden", "false")
        if not ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//md-icon[contains(@ng-show, 'ruleToggle.l3Rules') and .='expand_more']")
        ui_cmd_obj.error_state = False
        self.builder.click(ui_cmd_obj, "//button[@ng-click='addL3Rule($event)']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['network_rule_name'], "//input[@id='ruleName']")
        if arg_dict['access_control']:
            self.builder.click(ui_cmd_obj, "//select[@id='accessControl']/option[.='" +
                               arg_dict['access_control'] + "']")
        if arg_dict['cos_profile']:
            self.builder.click(ui_cmd_obj, "//select[@ng-model='role.l3Filters[$index].cosId']/option[.='" +
                               arg_dict['cos_profile'] + "']")
        if arg_dict['protocol']:
            self.builder.click(ui_cmd_obj, "//select[@name='protocolType']/option[.='" + arg_dict['protocol'] + "']")
        if arg_dict['subnet_and_mask']:
            self.builder.click(ui_cmd_obj, "//select[@name='subnetType']/option[.='" +
                               arg_dict['subnet_and_mask'] + "']")
            if arg_dict['subnet_and_mask'] == "User Defined":
                self.builder.enter_text(ui_cmd_obj, arg_dict['subnet_ip'],
                                        "//input[@ng-model='role.l3Filters[$index].ipAddressRange']")
        if arg_dict['filter_port']:
            self.builder.click(ui_cmd_obj, "//select[@name='portType']/option[.='" + arg_dict['filter_port'] + "']")
        self.builder.click(ui_cmd_obj, "//div[@ng-show='ruleToggle.l3Rules']//tr/th[.='Name']")

        return ui_cmd_obj

    def delete_network_rule_on_policy_role(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//md-icon[contains(@ng-show, 'ruleToggle.l3Rules') "
                                                            "and .='expand_more']", "aria-hidden", "false")
        if not ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//md-icon[contains(@ng-show, 'ruleToggle.l3Rules') and .='expand_more']")
        ui_cmd_obj.error_state = False
        self.builder.click(ui_cmd_obj, "//div[@ng-show='ruleToggle.l3Rules']//div[@class='col-md-6 ng-binding' "
                                       "and normalize-space(.)='" + arg_dict['network_rule_name'] + "']")
        self.builder.click(ui_cmd_obj, "//i[@ng-click='deleteRule($event)']")
        self.builder.click(ui_cmd_obj, "//div[@ng-show='ruleToggle.l3Rules']//tr/th[.='Name']")

        return ui_cmd_obj

    def click_add_to_create_new_policy_role(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-click='$parent.onCreate()' and normalize-space(.)='Add']")
        self.builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def click_policy_role_name_to_open_role_settings(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//div[@class='ui-grid-cell-contents ng-binding ng-scope' and .='" +
                           str(arg_dict['policy_role_name']) + "']")
        self.builder.delay(ui_cmd_obj, 2000)
        self.builder.click(ui_cmd_obj, "//button[.='CONFIGURE ROLE']")

        return ui_cmd_obj

    def create_application_rule_on_policy_role(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//md-icon[contains(@ng-show, 'ruleToggle.l7Rules') "
                                                            "and .='expand_more']", "aria-hidden", "false")
        if not ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//md-icon[contains(@ng-show, 'ruleToggle.l7Rules') and .='expand_more']")
        ui_cmd_obj.error_state = False
        self.builder.click(ui_cmd_obj, "//button[@ng-click='addL7Rule($event)']")
        self.builder.find_element(ui_cmd_obj, "//h3[.='ExtremeCloud Appliance']")
        if ui_cmd_obj.error_state:
            ui_cmd_obj.error_state = False
        else:
            self.builder.click(ui_cmd_obj, "//button[@ng-click='closeDialog(true)']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['application_rule_name'], "//input[@id='ruleName']")
        if arg_dict['access_control']:
            self.builder.click(ui_cmd_obj, "//select[@id='accessControl']/option[.='" +
                               arg_dict['access_control'] + "']")
        if arg_dict['cos_profile']:
            self.builder.click(ui_cmd_obj, "//select[@ng-model='role.l7Filters[$index].cosId']/option[.='" +
                               arg_dict['cos_profile'] + "']")
        if arg_dict['application_group_name']:
            self.builder.click(ui_cmd_obj,
                               "//select[@ng-model='role.l7Filters[$index].appGroupId']/option[.='" +
                               arg_dict['application_group_name'] + "']")
        if arg_dict['application_name']:
            self.builder.click(ui_cmd_obj, "//select[@ng-model='selectApplication']/option[.='" +
                               arg_dict['application_name'] + "']")
        self.builder.click(ui_cmd_obj, "//div[@ng-show='ruleToggle.l7Rules']//tr/th[.='Name']")

        return ui_cmd_obj

    def delete_application_rule_on_policy_role(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//md-icon[contains(@ng-show, 'ruleToggle.l7Rules') "
                                                            "and .='expand_more']", "aria-hidden", "false")
        if not ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//md-icon[contains(@ng-show, 'ruleToggle.l7Rules') and .='expand_more']")
        ui_cmd_obj.error_state = False
        self.builder.click(ui_cmd_obj,
                           "//div[@ng-show='ruleToggle.l7Rules']//div[@class='col-md-6 ng-binding' "
                           "and normalize-space(.)='" + arg_dict['application_rule_name'] + "']")
        self.builder.click(ui_cmd_obj, "//i[@ng-click='deleteRule($event)']")
        self.builder.click(ui_cmd_obj, "//div[@ng-show='ruleToggle.l7Rules']//tr/th[.='Name']")

        return ui_cmd_obj

    def save_roles_settings(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//button[@ng-click='$parent.save()' and @aria-hidden='false']")
        self.builder.click(ui_cmd_obj, "//button[@ng-click='closeDialog(false)']")

        return ui_cmd_obj

    def verify_policy_role_exists(self, ui_cmd_obj, arg_dict):
        xpath = "//div[@class='ui-grid-cell-contents ng-binding ng-scope' and .='" + \
                str(arg_dict['policy_role_name']) + "']"
        self.builder.find_element(ui_cmd_obj, xpath)
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Vlan " + str(arg_dict["policy_role_name"]) + " doesn't exist.")
        else:
            self.logger.log_debug("Vlan " + str(arg_dict["policy_role_name"]) + " already exist.")

        return ui_cmd_obj

    def verify_policy_role_does_not_exist(self, ui_cmd_obj, arg_dict):
        xpath = "//div[@class='ui-grid-cell-contents ng-binding ng-scope' and .='" + \
                str(arg_dict['policy_role_name']) + "']"
        self.builder.find_element(ui_cmd_obj, xpath)
        if ui_cmd_obj.error_state:
            ui_cmd_obj.error_state = False
            self.logger.log_debug("Vlan " + str(arg_dict["policy_role_name"]) + " doesn't exist.")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_debug("Vlan " + str(arg_dict["policy_role_name"]) + " still exist.")

        return ui_cmd_obj

    def verify_network_rule_exists_on_policy_role(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//md-icon[contains(@ng-show, 'ruleToggle.l3Rules') "
                                                            "and .='expand_more']", "aria-hidden", "false")
        if not ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//md-icon[contains(@ng-show, 'ruleToggle.l3Rules') and .='expand_more']")
        ui_cmd_obj.error_state = False
        self.builder.find_element(ui_cmd_obj, "//div[@ng-show='ruleToggle.l3Rules']//div[@class='col-md-6 ng-binding' "
                                              "and normalize-space(.)='" + arg_dict['network_rule_name'] + "']")
        if ui_cmd_obj.error_state:
            self.logger.log_debug("Network rule " + str(arg_dict["network_rule_name"]) + " doesn't exist.")
        else:
            self.logger.log_debug("Network rule " + str(arg_dict["network_rule_name"]) + " already exist.")

        return ui_cmd_obj

    def verify_network_rule_does_not_exist_on_policy_role(self, ui_cmd_obj, arg_dict):
        self.builder.get_attribute_from_element_and_compare(ui_cmd_obj,
                                                            "//md-icon[contains(@ng-show, 'ruleToggle.l3Rules') "
                                                            "and .='expand_more']", "aria-hidden", "false")
        if not ui_cmd_obj.error_state:
            self.builder.click(ui_cmd_obj, "//md-icon[contains(@ng-show, 'ruleToggle.l3Rules') and .='expand_more']")
        ui_cmd_obj.error_state = False
        self.builder.find_element(ui_cmd_obj, "//div[@ng-show='ruleToggle.l3Rules']//div[@class='col-md-6 ng-binding' "
                                              "and normalize-space(.)='" + arg_dict['network_rule_name'] + "']")
        if ui_cmd_obj.error_state:
            ui_cmd_obj.error_state = False
            self.logger.log_debug("Network rule " + str(arg_dict["network_rule_name"]) + " doesn't exist.")
        else:
            ui_cmd_obj.error_state = True
            self.logger.log_debug("Network rule " + str(arg_dict["network_rule_name"]) + " still exist.")

        return ui_cmd_obj

    def create_mac_rule_on_policy_role(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcaroles, self).create_mac_rule_on_policy_role(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()

    def delete_mac_rule_on_policy_role(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Xcaroles, self).delete_mac_rule_on_policy_role(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()
