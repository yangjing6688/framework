from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.EnginesConstants import EnginesConstants


class UiEnginesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEnginesKeywords, self).__init__()
        self.api_const = self.constants.API_ENGINES
        self.command_const = EnginesConstants()

    def access_control_engines_dialog_add_access_control_engine(self, element_name, engine_group, ip_address,
                                                                engine_name, profile, **kwargs):
        """Returns the result of access_control_engines_dialog_add_access_control_engine."""
        args = {"engine_group": engine_group,
                "ip_address": ip_address,
                "engine_name": engine_name,
                "profile": profile}

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_DIALOG_ADD_ACCESS_CONTROL_ENGINE,
                                    **kwargs)

    def access_control_engines_dialog_delete_access_control_engine(self, element_name, engine_name, **kwargs):
        """Returns the result of access_control_engines_dialog_delete_access_control_engine."""
        args = {"engine_name": engine_name}

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_DIALOG_DELETE_ACCESS_CONTROL_ENGINE,
                                    **kwargs)

    def access_control_engines_dialog_add_switch(self, element_name, device_type, engine_group, switch_ip,
                                                 primary_engine_name, primary_engine_ip, **kwargs):
        """Returns the result of access_control_engines_dialog_add_switch."""
        args = {"device_type": device_type,
                "engine_group": engine_group,
                "switch_ip": switch_ip,
                "primary_engine_name": primary_engine_name,
                "primary_engine_ip": primary_engine_ip}

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_DIALOG_ADD_SWITCH, **kwargs)

    def access_control_engines_dialog_delete_switch(self, element_name, engine_group, switch_ip, **kwargs):
        """Returns the result of access_control_engines_dialog_delete_switch."""
        args = {"engine_group": engine_group,
                "switch_ip": switch_ip}

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_DIALOG_DELETE_SWITCH, **kwargs)

    def access_control_engines_dialog_edit_switch_set_switch_type(self, element_name, switch_type, **kwargs):
        """Returns the result of access_control_engines_dialog_edit_switch_set_switch_type."""
        args = {"switch_type": switch_type}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_DIALOG_EDIT_SWITCH_SET_SWITCH_TYPE, **kwargs)

    def access_control_engines_dialog_edit_switch_set_primary_engine(self, element_name, primary_engine_name,
                                                                     primary_engine_ip, **kwargs):
        """Returns the result of access_control_engines_dialog_edit_switch_set_primary_engine."""
        args = {"primary_engine_name": primary_engine_name,
                "primary_engine_ip": primary_engine_ip}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_DIALOG_EDIT_SWITCH_SET_PRIMARY_ENGINE, **kwargs)

    def access_control_engines_dialog_edit_switch_set_secondary_engine(self, element_name, secondary_engine_name,
                                                                       secondary_engine_ip, **kwargs):
        """Returns the result of access_control_engines_dialog_edit_switch_set_secondary_engine."""
        args = {"secondary_engine_name": secondary_engine_name,
                "secondary_engine_ip": secondary_engine_ip}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_DIALOG_EDIT_SWITCH_SET_SECONDARY_ENGINE, **kwargs)

    def access_control_engines_dialog_edit_switch_set_auth_access_type(self, element_name, access_type, **kwargs):
        """Returns the result of access_control_engines_dialog_edit_switch_set_auth_access_type."""
        args = {"access_type": access_type}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_DIALOG_EDIT_SWITCH_SET_AUTH_ACCESS_TYPE, **kwargs)

    def access_control_engines_dialog_edit_switch_set_virtual_router_name(self, element_name, vr_name, **kwargs):
        """Returns the result of access_control_engines_dialog_edit_switch_set_virtual_router_name."""
        args = {"vr_name": vr_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_DIALOG_EDIT_SWITCH_SET_VIRTUAL_ROUTER_NAME, **kwargs)

    def access_control_engines_dialog_edit_switch_set_radius_attr_to_send(self, element_name, attributes_to_send,
                                                                          **kwargs):
        """Returns the result of access_control_engines_dialog_edit_switch_set_radius_attr_to_send."""
        args = {"attributes_to_send": attributes_to_send}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_DIALOG_EDIT_SWITCH_SET_RADIUS_ATTR_TO_SEND, **kwargs)

    def access_control_engines_dialog_edit_switch_set_radius_accounting(self, element_name, radius_accounting,
                                                                        **kwargs):
        """Returns the result of access_control_engines_dialog_edit_switch_set_radius_accounting."""
        args = {"radius_accounting": radius_accounting}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_DIALOG_EDIT_SWITCH_SET_RADIUS_ACCOUNTING, **kwargs)

    def access_control_engines_dialog_edit_switch_set_radius_mgmt_server_1(self, element_name, mgmt_server, **kwargs):
        """Returns the result of access_control_engines_dialog_edit_switch_set_radius_mgmt_server_1."""
        args = {"mgmt_server": mgmt_server}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_DIALOG_EDIT_SWITCH_SET_RADIUS_MGMT_SERVER_1, **kwargs)

    def access_control_engines_dialog_edit_switch_set_radius_mgmt_server_2(self, element_name, mgmt_server, **kwargs):
        """Returns the result of access_control_engines_dialog_edit_switch_set_radius_mgmt_server_2."""
        args = {"mgmt_server": mgmt_server}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_DIALOG_EDIT_SWITCH_SET_RADIUS_MGMT_SERVER_2, **kwargs)

    def access_control_engines_dialog_edit_switch_set_network_radius_server(self, element_name, network_server,
                                                                            **kwargs):
        """Returns the result of access_control_engines_dialog_edit_switch_set_network_radius_server."""
        args = {"network_server": network_server}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_DIALOG_EDIT_SWITCH_SET_NETWORK_RADIUS_SERVER, **kwargs)

    def access_control_engines_dialog_edit_switch_set_policy_domain(self, element_name, domain_name, **kwargs):
        """Returns the result of access_control_engines_dialog_edit_switch_set_policy_domain."""
        args = {"domain_name": domain_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_DIALOG_EDIT_SWITCH_SET_POLICY_DOMAIN, **kwargs)

    def access_control_engines_dialog_edit_switch_click_save(self, element_name, device_type, **kwargs):
        """Returns the result of access_control_engines_dialog_edit_switch_click_save."""
        args = {"device_type": device_type}

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_DIALOG_EDIT_SWITCH_CLICK_SAVE,
                                    **kwargs)

    def access_control_engines_navigate_to_edit_switch(self, element_name, engine_group, switch_ip, **kwargs):
        """Returns the result of access_control_engines_navigate_to_edit_switch."""
        args = {"engine_group": engine_group,
                "switch_ip": switch_ip}

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_NAVIGATE_TO_EDIT_SWITCH, **kwargs)

    def access_control_engines_open_advanced_settings_dialog(self, element_name, **kwargs):
        """Returns the result of access_control_engines_open_advanced_settings_dialog."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_OPEN_ADVANCED_SETTINGS_DIALOG,
                                    **kwargs)

    def access_control_engines_advanced_switch_settings_dialog_select_ip_subnet(self, element_name, ip_subnet,
                                                                                **kwargs):
        """Returns the result of access_control_engines_advanced_switch_settings_dialog_select_ip_subnet."""
        args = {"ip_subnet": ip_subnet}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_ADVANCED_SWITCH_SETTINGS_DIALOG_SELECT_IP_SUBNET,
                                    **kwargs)

    def access_control_engines_advanced_switch_settings_dialog_enter_shared_security(self, element_name, shared_secret,
                                                                                     **kwargs):
        """Returns the result of access_control_engines_advanced_switch_settings_dialog_enter_shared_security."""
        args = {"shared_secret": shared_secret}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_ADVANCED_SWITCH_SETTINGS_DIALOG_ENTER_SHARED_SECURITY,
                                    **kwargs)

    def access_control_engines_advanced_switch_settings_dialog_select_reauth_type(self, element_name, reauth_type,
                                                                                  **kwargs):
        """Returns the result of access_control_engines_advanced_switch_settings_dialog_select_reauth_type."""
        args = {"reauth_type": reauth_type}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_ADVANCED_SWITCH_SETTINGS_DIALOG_SELECT_REAUTH_TYPE,
                                    **kwargs)

    def access_control_engines_advanced_switch_settings_dialog_check_enable_port_link_control(self, element_name,
                                                                                              port_link, **kwargs):
        """
        Returns the result of
        access_control_engines_advanced_switch_settings_dialog_check_enable_port_link_control.
        """
        args = {"port_link": port_link}

        return self.execute_keyword(element_name, args, self.command_const.
                                    ENGINES_ADVANCED_SWITCH_SETTINGS_DIALOG_CHECK_ENABLE_PORT_LINK_CONTROL, **kwargs)

    def access_control_engines_advanced_switch_settings_dialog_save_settings(self, element_name, **kwargs):
        """Returns the result of access_control_engines_advanced_switch_settings_dialog_save_settings."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_ADVANCED_SWITCH_SETTINGS_DIALOG_SAVE_SETTINGS, **kwargs)

    def access_control_engines_advanced_switch_settings_dialog_cancel_settings(self, element_name, **kwargs):
        """Returns the result of access_control_engines_advanced_switch_settings_dialog_cancel_settings."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_ADVANCED_SWITCH_SETTINGS_DIALOG_CANCEL_SETTINGS,
                                    **kwargs)

    def access_control_engines_add_engine_properties(self, element_name, primary_engine_name, primary_engine_ip,
                                                     property_name, property_value, **kwargs):
        """Returns the result of access_control_engines_add_engine_properties."""
        args = {"primary_engine_name": primary_engine_name,
                "primary_engine_ip": primary_engine_ip,
                "property_name": property_name,
                "property_value": property_value}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_ADD_ENGINE_PROPERTIES,
                                    **kwargs)

    def access_control_engines_remove_engine_properties(self, element_name, primary_engine_name, primary_engine_ip,
                                                        property_name, **kwargs):
        """Returns the result of access_control_engines_remove_engine_properties."""
        args = {"primary_engine_name": primary_engine_name,
                "primary_engine_ip": primary_engine_ip,
                "property_name": property_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ENGINES_REMOVE_ENGINE_PROPERTIES,
                                    **kwargs)

    def access_control_engines_gim_default_validation_gim_tab(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Validation of Guest And IOT Manager tab from xmc
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_GIM_DEFAULT_VALIDATION_GIM_TAB,
                                    **kwargs)

    def access_control_engines_gim_default_buttons_validation(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.

        Validation of Add, Edit and Delete buttons from Guest And IOT Manager tab from xmc
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_GIM_DEFAULT_BUTTONS_VALIDATION,
                                    **kwargs)

    def access_control_engines_gim_add_gim_ip(self, element_name, ip_address, secret, delete_row, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ip_address]  - IP address of the GIM
        [secret]  - RADIUS Secret
        [delete_row] - deleting row, if none it will not delete it

        Adding of GIM IP to xmc
        """
        args = {"ip_address": ip_address,
                "secret": secret,
                "delete_row": delete_row
                }

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_GIM_ADD_GIM_IP, **kwargs)

    def access_control_engines_gim_edit_gim_ip(self, element_name, ip_address, edit_secret, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ip_address]  - IP address of the GIM
        [edit_secret]  - New secret

        Editing  newly added GIM details with secret key
        """
        args = {"ip_address": ip_address,
                "edit_secret": edit_secret
                }

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_GIM_EDIT_GIM_IP, **kwargs)

    def access_control_engines_gim_delete_gim_ip(self, element_name, ip_address, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ip_address]  - IP address of the GIM

        Deleting newly added GIM ip
        """
        args = {"ip_address": ip_address
                }

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_GIM_DELETE_GIM_IP, **kwargs)

    def access_control_engines_gim_default_validation_details_tab(self, element_name, gim_conf_text, domain_name,
                                                                  lpr_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [gim_conf_text] - Text present in GIM Panel from Details tab
        [domain_name] - Name of the Domain
        [lpr_name] - Name of the Local Password Repo

        Validation of Guest and IOT Manager panel from Details tab
        """
        args = {"gim_conf_text": gim_conf_text,
                "domain_name": domain_name,
                "lpr_name": lpr_name
                }

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_GIM_DEFAULT_VALIDATION_DETAILS_TAB,
                                    **kwargs)

    def access_control_engines_gim_add_domain(self, element_name, domain_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [domain_name]  - Name of the newly created domain

        Adding of new custom domain and map to the default LPR
        """
        args = {"domain_name": domain_name
                }

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_GIM_ADD_DOMAIN, **kwargs)

    def access_control_engines_gim_map_domain_lpr_none(self, element_name, domain_name, lpr_name, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [domain_name]  - Name of the Domain to select
        [lpr_name]  -   Name of LPR or None

        Mapping of Domain to None Local Password Repo
        """
        args = {"domain_name": domain_name,
                "lpr_name": lpr_name
                }

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_MAP_DOMAIN_LPR_NONE, **kwargs)

    def access_control_engines_gim_duplicate_ip(self, element_name, ip_address, secret, **kwargs):
        """
        Keyword Arguments:
        [element_name] - The UI element(s) the keyword should be run against.
        [ip_address]  - IP address of the GIM
        [secret]  - RADIUS Secret

        Adding of GIM IP to xmc
        """
        args = {"ip_address": ip_address,
                "secret": secret
                }

        return self.execute_keyword(element_name, args, self.command_const.ENGINES_GIM_DUPLICATE_IP, **kwargs)
