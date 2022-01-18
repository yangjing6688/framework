from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.ConfigurationsConstants import ConfigurationsConstants


class UiConfigurationsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiConfigurationsKeywords, self).__init__()
        self.api_const = self.constants.API_CONFIGS
        self.command_const = ConfigurationsConstants()

    def access_control_configs_aaa_default_check_authenticate_for(self, element_name, status, **kwargs):
        """Returns the result of access_control_configs_aaa_."""
        args = {"status": status}

        return self.execute_keyword(element_name, args, self.command_const.CONFIGS_AAA_DEFAULT_CHECK_AUTHENTICATE_FOR,
                                    **kwargs)

    def access_control_configs_aaa_default_select_authenticate_method(self, element_name, auth_methods, **kwargs):
        """Returns the result of access_control_configs_aaa_."""
        args = {"auth_methods": auth_methods}

        return self.execute_keyword(element_name, args, self.command_const.CONFIGS_AAA_DEFAULT_SELECT_AUTH_METHODS,
                                    **kwargs)

    def access_control_configs_aaa_default_select_primary_radius_server(self, element_name, ip_address, **kwargs):
        """Returns the result of access_control_configs_aaa_."""
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CONFIGS_AAA_DEFAULT_SELECT_PRIMARY_RADIUS_SERVER, **kwargs)

    def access_control_configs_aaa_default_select_backup_radius_server(self, element_name, ip_address, **kwargs):
        """Returns the result of access_control_configs_aaa_."""
        args = {"ip_address": ip_address}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CONFIGS_AAA_DEFAULT_SELECT_BACKUP_RADIUS_SERVER, **kwargs)

    def access_control_configs_aaa_default_select_select_ldap_configuration(self, element_name, config_name, **kwargs):
        """Returns the result of access_control_configs_aaa_."""
        args = {"config_name": config_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CONFIGS_AAA_DEFAULT_SELECT_LDAP_CONFIGURATION, **kwargs)

    def access_control_configs_aaa_default_select_local_password_repository(self, element_name, repo_name, **kwargs):
        """Returns the result of access_control_configs_aaa_."""
        args = {"repo_name": repo_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CONFIGS_AAA_DEFAULT_SELECT_LOCAL_PASSWORD_REPOSITORY, **kwargs)

    def access_control_configs_aaa_default_save_aaa_default(self, element_name, **kwargs):
        """Returns the result of access_control_configs_aaa_."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.CONFIGS_AAA_DEFAULT_SAVE_AAA_DEFAULT,
                                    **kwargs)

    def access_control_configs_aaa_default_cancel_aaa_default(self, element_name, **kwargs):
        """Returns the result of access_control_configs_aaa_."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.CONFIGS_AAA_DEFAULT_CANCEL_AAA_DEFAULT,
                                    **kwargs)

    def access_control_configs_click_add_access_control_configuration_button(self, element_name, **kwargs):
        """Returns the result of access_control_configs_click_add_access_control_configuration_button."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CONFIGS_CLICK_ADD_ACCESS_CONTROL_CONFIGURATION_BUTTON, **kwargs)

    def access_control_configs_click_delete_access_control_configuration_button(self, element_name, **kwargs):
        """Returns the result of access_control_configs_click_delete_access_control_configuration_button."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CONFIGS_CLICK_DELETE_ACCESS_CONTROL_CONFIGURATION_BUTTON,
                                    **kwargs)

    def access_control_configs_click_edit_access_control_configuration_button(self, element_name, **kwargs):
        """Returns the result of access_control_configs_click_edit_access_control_configuration_button."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CONFIGS_CLICK_EDIT_ACCESS_CONTROL_CONFIGURATION_BUTTON, **kwargs)

    def access_control_configs_click_select_aaa_configuration_button(self, element_name, **kwargs):
        """Returns the result of access_control_configs_click_select_aaa_configuration_button."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CONFIGS_CLICK_SELECT_AAA_CONFIGURATION_BUTTON, **kwargs)

    def access_control_configs_select_aaa_configuration_dialog_select_aaa_configuration(self, element_name,
                                                                                        aaa_configuration, **kwargs):
        """Returns the result of access_control_configs_select_aaa_configuration_dialog_select_aaa_configuration."""
        args = {"aaa_configuration": aaa_configuration}

        return self.execute_keyword(element_name, args,
                                    self.command_const.CONFIGS_SELECT_AAA_CONFIGURATION_DIALOG_SELECT_AAA_CONFIGURATION,
                                    **kwargs)

    def access_control_configs_select_access_control_configuration(self, element_name, access_control_configuration,
                                                                   **kwargs):
        """Returns the result of access_control_configs_select_access_control_configuration."""
        args = {"access_control_configuration": access_control_configuration}

        return self.execute_keyword(element_name, args, self.command_const.CONFIGS_SELECT_ACCESS_CONTROL_CONFIGURATION,
                                    **kwargs)

    def access_control_configs_add_access_control_configuration(self, element_name, access_control_configuration,
                                                                **kwargs):
        """Returns the result of access_control_configs_add_access_control_configuration."""
        args = {"access_control_configuration": access_control_configuration}

        return self.execute_keyword(element_name, args, self.command_const.CONFIGS_ADD_ACCESS_CONTROL_CONFIGURATION,
                                    **kwargs)

    def access_control_configs_delete_access_control_configuration(self, element_name, access_control_configuration,
                                                                   **kwargs):
        """Returns the result of access_control_configs_delete_access_control_configuration."""
        args = {"access_control_configuration": access_control_configuration}

        return self.execute_keyword(element_name, args, self.command_const.CONFIGS_DELETE_ACCESS_CONTROL_CONFIGURATION,
                                    **kwargs)

    def access_control_configs_rules_click_add_rule_button(self, element_name, **kwargs):
        """Returns the result of access_control_configs_rules_click_add_rule_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.CONFIGS_RULES_CLICK_ADD_RULE_BUTTON,
                                    **kwargs)

    def access_control_configs_rules_click_delete_rule_button(self, element_name, **kwargs):
        """Returns the result of access_control_configs_rules_click_delete_rule_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.CONFIGS_RULES_CLICK_DELETE_RULE_BUTTON,
                                    **kwargs)

    def access_control_configs_rules_click_edit_rule_button(self, element_name, **kwargs):
        """Returns the result of access_control_configs_rules_click_edit_rule_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.CONFIGS_RULES_CLICK_EDIT_RULE_BUTTON,
                                    **kwargs)

    def access_control_configs_rules_click_refresh_button(self, element_name, **kwargs):
        """Returns the result of access_control_configs_rules_click_refresh_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.CONFIGS_RULES_CLICK_REFRESH_BUTTON,
                                    **kwargs)

    def access_control_configs_rules_select_rule(self, element_name, rule_name, **kwargs):
        """Returns the result of access_control_configs_rules_select_rule."""
        args = {"rule_name": rule_name}

        return self.execute_keyword(element_name, args, self.command_const.CONFIGS_RULES_SELECT_RULE, **kwargs)

    def access_control_configs_rules_dialog_add_rule(self, element_name, rule_name, authentication_method, user_group,
                                                     endsystem_group, device_type_group, location_group, time_group,
                                                     nac_profile, **kwargs):
        """Returns the result of access_control_configs_rules_dialog_add_rule."""
        args = {"rule_name": rule_name,
                "authentication_method": authentication_method,
                "user_group": user_group,
                "endsystem_group": endsystem_group,
                "device_type_group": device_type_group,
                "location_group": location_group,
                "time_group": time_group,
                "nac_profile": nac_profile}

        return self.execute_keyword(element_name, args, self.command_const.CONFIGS_RULES_DIALOG_ADD_RULE, **kwargs)

    def access_control_configs_rules_dialog_delete_rule(self, element_name, rule_name, **kwargs):
        """Returns the result of access_control_configs_rules_dialog_delete_rule."""
        args = {"rule_name": rule_name}

        return self.execute_keyword(element_name, args, self.command_const.CONFIGS_RULES_DIALOG_DELETE_RULE, **kwargs)

    def access_control_configs_rules_dialog_enable_rule(self, element_name, rule_name, rule_enabled, **kwargs):
        """Returns the result of access_control_configs_rules_dialog_enable_rule."""
        args = {"rule_name": rule_name,
                "rule_enabled": rule_enabled}

        return self.execute_keyword(element_name, args, self.command_const.CONFIGS_RULES_DIALOG_ENABLE_RULE, **kwargs)
