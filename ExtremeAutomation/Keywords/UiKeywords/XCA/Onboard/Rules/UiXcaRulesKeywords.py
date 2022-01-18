from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XCA.XcarulesConstants import XcarulesConstants


class UiXcaRulesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiXcaRulesKeywords, self).__init__()
        self.api_const = self.constants.API_XCA_RULES
        self.command_const = XcarulesConstants()

    def rules_click_add_to_create_new_rule(self, element_names, **kwargs):
        """Returns the result of rules_click_add_to_create_new_rule."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CLICK_ADD_TO_CREATE_NEW_RULE, **kwargs)

    def rules_config_rule_name_and_enabled(self, element_names, rule_name, rule_enabled, **kwargs):
        """Returns the result of rules_config_rule_name_and_enabled."""
        args = {"rule_name": rule_name,
                "rule_enabled": rule_enabled}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_RULE_NAME_AND_ENABLED, **kwargs)

    def rules_config_rule_conditions(self, element_names, user_group, end_sys_group, device_type_group, location_group,
                                     **kwargs):
        """

        :param element_names:
        :param user_group: Pass None type data if not applicable.
        :param end_sys_group: Pass None type data if not applicable.
        :param device_type_group: Pass None type data if not applicable.
        :param location_group: Pass None type data if not applicable.
        :return:
        """
        args = {"user_group": user_group,
                "end_sys_group": end_sys_group,
                "device_type_group": device_type_group,
                "location_group": location_group}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_RULE_CONDITIONS, **kwargs)

    def rules_config_rule_actions(self, element_names, accept_policy_name, portal_name, **kwargs):
        """

        :param element_names:
        :param accept_policy_name: Pass None type data if not applicable.
        :param portal_name: Pass None type data if not applicable.
        :return:
        """
        args = {"accept_policy_name": accept_policy_name,
                "portal_name": portal_name}

        return self.execute_keyword(element_names, args, self.command_const.CONFIG_RULE_ACTIONS, **kwargs)

    def rules_save_config_and_back_to_rules_page(self, element_names, **kwargs):
        """Returns the result of rules_save_config_and_back_to_rules_page."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SAVE_CONFIG_AND_BACK_TO_RULES_PAGE,
                                    **kwargs)

    def rules_delete_rule_in_rules_page(self, element_names, rule_name, **kwargs):
        """Returns the result of rules_delete_rule_in_rules_page."""
        args = {"rule_name": rule_name}

        return self.execute_keyword(element_names, args, self.command_const.DELETE_RULE_IN_RULES_PAGE, **kwargs)

    def rules_delete_rule_in_config_page(self, element_names, rule_name, **kwargs):
        """Returns the result of rules_delete_rule_in_config_page."""
        args = {"rule_name": rule_name}

        return self.execute_keyword(element_names, args, self.command_const.DELETE_RULE_IN_CONFIG_PAGE, **kwargs)

    def rules_verify_control_rule_exists(self, element_names, rule_name, **kwargs):
        """Returns the result of rules_verify_control_rule_exists."""
        args = {"rule_name": rule_name}

        return self.execute_keyword(element_names, args, self.command_const.VERIFY_CONTROL_RULE_EXISTS, **kwargs)

    def rules_verify_control_rule_does_not_exist(self, element_names, rule_name, **kwargs):
        """Returns the result of rules_verify_control_rule_does_not_exist."""
        args = {"rule_name": rule_name}

        return self.execute_keyword(element_names, args, self.command_const.VERIFY_CONTROL_RULE_DOES_NOT_EXIST,
                                    **kwargs)
