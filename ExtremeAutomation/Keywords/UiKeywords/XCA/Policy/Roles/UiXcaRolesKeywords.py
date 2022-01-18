from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XCA.XcarolesConstants import XcarolesConstants
from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass


class UiXcaRolesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiXcaRolesKeywords, self).__init__()
        self.api_const = self.constants.API_XCA_ROLES
        self.command_const = XcarolesConstants()

    def roles_edit_role_name(self, element_names, policy_role_name, **kwargs):
        """Returns the result of roles_edit_role_name."""
        args = {"policy_role_name": policy_role_name}

        return self.execute_keyword(element_names, args, self.command_const.EDIT_ROLE_NAME, **kwargs)

    def roles_delete_policy_role(self, element_names, policy_role_name, **kwargs):
        """Returns the result of roles_delete_policy_role."""
        args = {"policy_role_name": policy_role_name}

        return self.execute_keyword(element_names, args, self.command_const.DELETE_POLICY_ROLE, **kwargs)

    def roles_create_network_rule_on_policy_role(self, element_names, network_rule_name, access_control, cos_profile,
                                                 protocol, subnet_and_mask, subnet_ip, filter_port, **kwargs):
        """Returns the result of roles_create_network_rule_on_policy_role."""
        args = {"network_rule_name": network_rule_name,
                "access_control": access_control,
                "cos_profile": cos_profile,
                "protocol": protocol,
                "subnet_and_mask": subnet_and_mask,
                "subnet_ip": subnet_ip,
                "filter_port": filter_port}

        return self.execute_keyword(element_names, args, self.command_const.CREATE_NETWORK_RULE_ON_POLICY_ROLE,
                                    **kwargs)

    def roles_delete_network_rule_on_policy_role(self, element_names, network_rule_name, **kwargs):
        """Returns the result of roles_delete_network_rule_on_policy_role."""
        args = {"network_rule_name": network_rule_name}

        return self.execute_keyword(element_names, args, self.command_const.DELETE_NETWORK_RULE_ON_POLICY_ROLE,
                                    **kwargs)

    def roles_create_mac_rule_on_policy_role(self, element_names, **kwargs):
        """Returns the result of roles_create_mac_rule_on_policy_role."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CREATE_MAC_RULE_ON_POLICY_ROLE, **kwargs)

    def roles_delete_mac_rule_on_policy_role(self, element_names, **kwargs):
        """Returns the result of roles_delete_mac_rule_on_policy_role."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.DELETE_MAC_RULE_ON_POLICY_ROLE, **kwargs)

    def roles_create_application_rule_on_policy_role(self, element_names, application_rule_name, access_control,
                                                     cos_profile, application_group_name, application_name, **kwargs):
        """Returns the result of roles_create_application_rule_on_policy_role."""
        args = {"application_rule_name": application_rule_name,
                "access_control": access_control,
                "cos_profile": cos_profile,
                "application_group_name": application_group_name,
                "application_name": application_name}

        return self.execute_keyword(element_names, args, self.command_const.CREATE_APPLICATION_RULE_ON_POLICY_ROLE,
                                    **kwargs)

    def roles_delete_application_rule_on_policy_role(self, element_names, application_rule_name, **kwargs):
        """Returns the result of roles_delete_application_rule_on_policy_role."""
        args = {"application_rule_name": application_rule_name}

        return self.execute_keyword(element_names, args, self.command_const.DELETE_APPLICATION_RULE_ON_POLICY_ROLE,
                                    **kwargs)

    def roles_click_add_to_create_new_policy_role(self, element_names, **kwargs):
        """Returns the result of roles_click_add_to_create_new_policy_role."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.CLICK_ADD_TO_CREATE_NEW_POLICY_ROLE,
                                    **kwargs)

    def roles_save_roles_settings(self, element_names, **kwargs):
        """Returns the result of roles_save_roles_settings."""
        args = {}

        return self.execute_keyword(element_names, args, self.command_const.SAVE_ROLES_SETTINGS,
                                    **kwargs)

    def roles_click_policy_role_name_to_open_role_settings(self, element_names, policy_role_name, **kwargs):
        """Returns the result of roles_click_policy_role_name_to_open_role_settings."""
        args = {"policy_role_name": policy_role_name}

        return self.execute_keyword(element_names, args,
                                    self.command_const.CLICK_POLICY_ROLE_NAME_TO_OPEN_ROLE_SETTINGS, **kwargs)

    def roles_verify_policy_role_exists(self, element_names, policy_role_name, **kwargs):
        """Returns the result of roles_verify_policy_role_exists."""
        args = {"policy_role_name": policy_role_name}

        return self.execute_keyword(element_names, args, self.command_const.VERIFY_POLICY_ROLE_EXISTS, **kwargs)

    def roles_verify_policy_role_does_not_exist(self, element_names, policy_role_name, **kwargs):
        """Returns the result of roles_verify_policy_role_does_not_exist."""
        args = {"policy_role_name": policy_role_name}

        return self.execute_keyword(element_names, args, self.command_const.VERIFY_POLICY_ROLE_DOES_NOT_EXIST, **kwargs)

    def roles_verify_network_rule_exists_on_policy_role(self, element_names, network_rule_name, **kwargs):
        """Returns the result of roles_verify_network_rule_exists_on_policy_role."""
        args = {"network_rule_name": network_rule_name}

        return self.execute_keyword(element_names, args, self.command_const.VERIFY_NETWORK_RULE_EXISTS_ON_POLICY_ROLE,
                                    **kwargs)

    def roles_verify_network_rule_does_not_exist_on_policy_role(self, element_names, network_rule_name,
                                                                **kwargs):
        """Returns the result of roles_verify_network_rule_does_not_exist_on_policy_role."""
        args = {"network_rule_name": network_rule_name}

        return self.execute_keyword(element_names, args,
                                    self.command_const.VERIFY_NETWORK_RULE_DOES_NOT_EXIST_ON_POLICY_ROLE, **kwargs)
