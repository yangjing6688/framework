from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.PolicymappingsConstants import PolicymappingsConstants


class UiPolicyMappingsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiPolicyMappingsKeywords, self).__init__()
        self.api_const = self.constants.API_POLICY_MAPPINGS
        self.command_const = PolicymappingsConstants()

    def access_control_policy_mappings_dialog_add_policy_mapping(self, element_name, mapping_name, policy_role,
                                                                 mgmt_access, **kwargs):
        """Returns the result of access_control_policy_mappings_dialog_add_policy_mapping."""
        args = {"mapping_name": mapping_name,
                "policy_role": policy_role,
                "mgmt_access": mgmt_access}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_MAPPINGS_DIALOG_ADD_POLICY_MAPPING,
                                    **kwargs)

    def access_control_policy_mappings_dialog_delete_policy_mapping(self, element_name, mapping_name, **kwargs):
        """Returns the result of access_control_policy_mappings_dialog_delete_policy_mapping."""
        args = {"mapping_name": mapping_name}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_MAPPINGS_DIALOG_DELETE_POLICY_MAPPING,
                                    **kwargs)

    def access_control_policy_mappings_navigate_to_edit_policy_mapping(self, element_name, mapping_name, **kwargs):
        """Returns the result of access_control_policy_mappings_navigate_to_edit_policy_mapping."""
        args = {"mapping_name": mapping_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_MAPPINGS_NAVIGATE_TO_EDIT_POLICY_MAPPING, **kwargs)

    def access_control_policy_mappings_click_switch_to_basic(self, element_name, **kwargs):
        """Returns the result of access_control_policy_mappings_click_switch_to_basic."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_MAPPINGS_CLICK_SWITCH_TO_BASIC,
                                    **kwargs)

    def access_control_policy_mappings_click_switch_to_advanced(self, element_name, **kwargs):
        """Returns the result of access_control_policy_mappings_click_switch_to_advanced."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_MAPPINGS_CLICK_SWITCH_TO_ADVANCED,
                                    **kwargs)

    def access_control_policy_mappings_dialog_edit_mapping_set_custom_fields(self, element_name, mapping_name, custom1,
                                                                             custom2, custom3, custom4, custom5,
                                                                             **kwargs):
        """Returns the result of access_control_policy_mappings_dialog_edit_mapping_set_custom_fields."""
        args = {"mapping_name": mapping_name,
                "custom1": custom1,
                "custom2": custom2,
                "custom3": custom3,
                "custom4": custom4,
                "custom5": custom5}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_CUSTOM_FIELDS, **kwargs)

    def access_control_policy_mappings_dialog_edit_mapping_set_filter(self, element_name, mapping_name, set_filter,
                                                                      **kwargs):
        """Returns the result of access_control_policy_mappings_dialog_edit_mapping_set_filter."""
        args = {"mapping_name": mapping_name,
                "filter": set_filter}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_FILTER, **kwargs)

    def access_control_policy_mappings_dialog_edit_mapping_set_location(self, element_name, mapping_name, location,
                                                                        **kwargs):
        """Returns the result of access_control_policy_mappings_dialog_edit_mapping_set_location."""
        args = {"mapping_name": mapping_name,
                "location": location}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_LOCATION, **kwargs)

    def access_control_policy_mappings_dialog_edit_mapping_set_login_lat_group_and_port(self, element_name,
                                                                                        mapping_name, lat_group,
                                                                                        lat_port, **kwargs):
        """Returns the result of access_control_policy_mappings_dialog_edit_mapping_set_login_lat_group_and_port."""
        args = {"mapping_name": mapping_name,
                "lat_group": lat_group,
                "lat_port": lat_port}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_LOGIN_LAT_GROUP_AND_PORT,
                                    **kwargs)

    def access_control_policy_mappings_dialog_edit_mapping_set_management_access(self, element_name, mapping_name,
                                                                                 mgmt_access, management,
                                                                                 mgmt_service_type, cli_access,
                                                                                 **kwargs):
        """Returns the result of access_control_policy_mappings_dialog_edit_mapping_set_management_access."""
        args = {"mapping_name": mapping_name,
                "mgmt_access": mgmt_access,
                "management": management,
                "mgmt_service_type": mgmt_service_type,
                "cli_access": cli_access}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_MANAGEMENT_ACCESS,
                                    **kwargs)

    def access_control_policy_mappings_dialog_edit_mapping_set_name(self, element_name, mapping_name, new_name,
                                                                    **kwargs):
        """Returns the result of access_control_policy_mappings_dialog_edit_mapping_set_name."""
        args = {"mapping_name": mapping_name,
                "new_name": new_name}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_NAME,
                                    **kwargs)

    def access_control_policy_mappings_dialog_edit_mapping_set_policy_role(self, element_name, mapping_name,
                                                                           policy_role, **kwargs):
        """Returns the result of access_control_policy_mappings_dialog_edit_mapping_set_policy_role."""
        args = {"mapping_name": mapping_name,
                "policy_role": policy_role}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_POLICY_ROLE, **kwargs)

    def access_control_policy_mappings_dialog_edit_mapping_set_port_profile(self, element_name, mapping_name,
                                                                            port_profile, **kwargs):
        """Returns the result of access_control_policy_mappings_dialog_edit_mapping_set_port_profile."""
        args = {"mapping_name": mapping_name,
                "port_profile": port_profile}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_PORT_PROFILE, **kwargs)

    def access_control_policy_mappings_dialog_edit_mapping_set_radius_attribute_lists(self, element_name, mapping_name,
                                                                                      org1, org2, org3, **kwargs):
        """Returns the result of access_control_policy_mappings_dialog_edit_mapping_set_radius_attribute_lists."""
        args = {"mapping_name": mapping_name,
                "org1": org1,
                "org2": org2,
                "org3": org3}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_RADIUS_ATTRIBUTE_LISTS,
                                    **kwargs)

    def access_control_policy_mappings_dialog_edit_mapping_set_virtual_router(self, element_name, mapping_name,
                                                                              virtual_router, **kwargs):
        """Returns the result of access_control_policy_mappings_dialog_edit_mapping_set_virtual_router."""
        args = {"mapping_name": mapping_name,
                "virtual_router": virtual_router}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_VIRTUAL_ROUTER, **kwargs)

    def access_control_policy_mappings_dialog_edit_mapping_set_vlan_name(self, element_name, mapping_name, vlan_id,
                                                                         vlan_name, **kwargs):
        """Returns the result of access_control_policy_mappings_dialog_edit_mapping_set_vlan_name."""
        args = {"mapping_name": mapping_name,
                "vlan_id": vlan_id,
                "vlan_name": vlan_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_VLAN_NAME, **kwargs)

    def access_control_policy_mappings_dialog_edit_mapping_set_vlan_egress(self, element_name, mapping_name,
                                                                           vlan_egress, vlan_egress_field, **kwargs):
        """Returns the result of access_control_policy_mappings_dialog_edit_mapping_set_vlan_egress."""
        args = {"mapping_name": mapping_name,
                "vlan_egress": vlan_egress,
                "vlan_egress_field": vlan_egress_field}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_SET_VLAN_EGRESS, **kwargs)

    def access_control_policy_mappings_select_mapping(self, element_name, mapping_name, **kwargs):
        """Returns the result of access_control_policy_mappings_select_mapping."""
        args = {"mapping_name": mapping_name}

        return self.execute_keyword(element_name, args, self.command_const.POLICY_MAPPINGS_SELECT_MAPPING, **kwargs)

    def access_control_policy_mappings_dialog_edit_mapping_click_save(self, element_name, **kwargs):
        """Returns the result of access_control_policy_mappings_dialog_edit_mapping_click_save."""
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.POLICY_MAPPINGS_DIALOG_EDIT_MAPPING_CLICK_SAVE, **kwargs)
