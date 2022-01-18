from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.PolicyConstants import PolicyConstants


class UiPolicyKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiPolicyKeywords, self).__init__()
        self.api_const = self.constants.API_POLICY
        self.cmd = PolicyConstants()

    def click_emc_policy_tab(self, element_name, **kwargs):
        """Returns the result of click_emc_policy_tab."""
        return self.execute_keyword(element_name, {}, self.cmd.CLICK_EMC_POLICY_TAB, **kwargs)

    def click_emc_control_menu(self, element_name, **kwargs):
        """Returns the result of click_emc_control_menu."""
        return self.execute_keyword(element_name, {}, self.cmd.CLICK_EMC_CONTROL_MENU, **kwargs)

    def policy_expand_tree_panel_roles_services(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Expands the Roles/Services tree panel.
        """
        return self.execute_keyword(element_name, {}, self.cmd.POLICY_EXPAND_TREE_PANEL_ROLES_SERVICES, **kwargs)

    def policy_expand_tree_panel_class_of_service(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Expands the Roles/Services tree panel.
        """
        return self.execute_keyword(element_name, {}, self.cmd.POLICY_EXPAND_TREE_PANEL_CLASS_OF_SERVICE, **kwargs)

    def policy_expand_tree_panel_vlans(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Expands the Roles/Services tree panel.
        """
        return self.execute_keyword(element_name, {}, self.cmd.POLICY_EXPAND_TREE_PANEL_VLANS, **kwargs)

    def policy_expand_tree_panel_network_resources(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Expands the Roles/Services tree panel.
        """
        return self.execute_keyword(element_name, {}, self.cmd.POLICY_EXPAND_TREE_PANEL_NETWORK_RESOURCES, **kwargs)

    def policy_expand_tree_panel_devices_port_groups(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Expands the Roles/Services tree panel.
        """
        return self.execute_keyword(element_name, {}, self.cmd.POLICY_EXPAND_TREE_PANEL_DEVICES_PORT_GROUPS, **kwargs)

    def policy_create_role(self, element_name, role_name, **kwargs):
        """Returns the result of policy_create_role."""
        args = {"role_name": role_name}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_CREATE_ROLE, **kwargs)

    def policy_delete_role(self, element_name, role_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [role_name] -     Name of the role to delete

        Deletes the specified role.
        """
        args = {"role_name": role_name}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_DELETE_ROLE, **kwargs)

    def policy_delete_service(self, element_name, service_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [service_name] -  Name of the service to delete

        Deletes the specified service.
        """
        args = {"service_name": service_name}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_DELETE_SERVICE, **kwargs)

    def policy_open_domain(self, element_name, domain_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [domain_name] -   Name of the policy domain to open

        Opens the specified policy domain.
        """
        args = {"domain_name": domain_name}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_OPEN_DOMAIN, **kwargs)

    def policy_save_domain(self, element_name, **kwargs):
        """Returns the result of policy_save_domain."""
        return self.execute_keyword(element_name, {}, self.cmd.POLICY_SAVE_DOMAIN, **kwargs)

    def policy_enforce_domain(self, element_name, **kwargs):
        """Returns the result of policy_enforce_domain."""
        return self.execute_keyword(element_name, {}, self.cmd.POLICY_ENFORCE_DOMAIN, **kwargs)

    def policy_add_device_to_domain_menu(self, element_name, device_ip, **kwargs):
        """Returns the result of policy_add_device_to_domain_menu."""
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_ADD_DEVICE_TO_DOMAIN_MENU, **kwargs)

    def click_devices_tab(self, element_name, **kwargs):
        """Returns the result of click_devices_tab."""
        return self.execute_keyword(element_name, {}, self.cmd.CLICK_DEVICES_TAB, **kwargs)

    def policy_add_device_to_domain(self, element_name, device_ip, **kwargs):
        """Returns the result of policy_add_device_to_domain."""
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_ADD_DEVICE_TO_DOMAIN, **kwargs)

    def policy_add_ports_to_domain(self, element_name, device_ip, port_group_name, ports, **kwargs):
        """Returns the result of policy_add_ports_to_domain."""
        args = {"device_ip": device_ip,
                "ports": ports,
                "port_group_name": port_group_name}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_ADD_PORTS_TO_DOMAIN, **kwargs)

    def remove_device_from_domain(self, element_name, device_ip, **kwargs):
        """Returns the result of remove_device_from_domain."""
        args = {"device_ip": device_ip}

        return self.execute_keyword(element_name, args, self.cmd.REMOVE_DEVICE_FROM_DOMAIN, **kwargs)

    def policy_create_local_service(self, element_name, service_name, **kwargs):
        """Returns the result of policy_create_local_service."""
        args = {"service_name": service_name}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_CREATE_LOCAL_SERVICE, **kwargs)

    def policy_delete_local_service(self, element_name, service_name, **kwargs):
        """Returns the result of policy_delete_local_service."""
        args = {"service_name": service_name}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_DELETE_LOCAL_SERVICE, **kwargs)

    def policy_create_rule(self, element_name, rule_name, service_name, **kwargs):
        """Returns the result of policy_create_rule."""
        args = {"rule_name": rule_name,
                "service_name": service_name}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_CREATE_RULE, **kwargs)

    def policy_add_service_to_role(self, element_name, service_name, role_name, **kwargs):
        """Returns the result of policy_add_service_to_role."""
        args = {"service_name": service_name,
                "role_name": role_name}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_ADD_SERVICE_TO_ROLE, **kwargs)

    def expand_policy_role_tree(self, element_name, **kwargs):
        """Returns the result of expand_policy_role_tree."""
        args = {"heading": 'Roles'}

        return self.execute_keyword(element_name, args, self.cmd.EXPAND_TREE, **kwargs)

    def edit_policy_rule_tci_overwrite(self, element_name, rule_name, status, **kwargs):
        """Returns the result of edit_policy_rule_tci_overwrite."""
        args = {"status": status,
                "rule_name": rule_name}

        return self.execute_keyword(element_name, args, self.cmd.EDIT_POLICY_RULE_TCI_OVERWRITE, **kwargs)

    def edit_policy_rule_access_control(self, element_name, rule_name, status, **kwargs):
        """Returns the result of edit_policy_rule_access_control."""
        args = {"status": status,
                "rule_name": rule_name}

        return self.execute_keyword(element_name, args, self.cmd.EDIT_POLICY_RULE_ACCESS_CONTROL, **kwargs)

    def edit_policy_rule_traffic_layer_type(self, element_name, rule_name, layer_type, traffic_type, **kwargs):
        """Returns the result of edit_policy_rule_traffic_layer_type."""
        args = {"layer_type": layer_type,
                "rule_name": rule_name,
                "traffic_type": traffic_type}

        return self.execute_keyword(element_name, args, self.cmd.EDIT_POLICY_RULE_TRAFFIC_LAYER_TYPE, **kwargs)

    def policy_rule_set_application_group(self, element_name, rule_name, application_group, **kwargs):
        """Returns the result of policy_rule_set_application_group."""
        args = {"rule_name": rule_name,
                "application_group": application_group}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_SET_APPLICATION_GROUP, **kwargs)

    def policy_rule_set_application(self, element_name, rule_name, application, **kwargs):
        """Returns the result of policy_rule_set_application."""
        args = {"rule_name": rule_name,
                "application": application}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_SET_APPLICATION, **kwargs)

    def edit_policy_rule_well_known_value(self, element_name, rule_name, well_known_value, **kwargs):
        """Returns the result of edit_policy_rule_well_known_value."""
        args = {"rule_name": rule_name,
                "well_known_value": well_known_value}

        return self.execute_keyword(element_name, args, self.cmd.EDIT_POLICY_RULE_WELL_KNOWN_VALUE, **kwargs)

    def edit_policy_rule_single_value(self, element_name, rule_name, single_value, **kwargs):
        """Returns the result of edit_policy_rule_single_value."""
        args = {"rule_name": rule_name,
                "single_value": single_value}

        return self.execute_keyword(element_name, args, self.cmd.EDIT_POLICY_RULE_SINGLE_VALUE_DATA, **kwargs)

    def edit_policy_rule_traffic_type(self, element_name, rule_name, traffic_type, **kwargs):
        """Returns the result of edit_policy_rule_traffic_type."""
        args = {"rule_name": rule_name,
                "traffic_type": traffic_type}

        return self.execute_keyword(element_name, args, self.cmd.EDIT_POLICY_RULE_TRAFFIC_TYPE, **kwargs)

    def set_rule_cos(self, element_name, rule_name, cos_value, **kwargs):
        """Returns the result of set_rule_cos."""
        args = {"rule_name": rule_name,
                "cos_value": cos_value}

        return self.execute_keyword(element_name, args, self.cmd.SET_RULE_COS, **kwargs)

    def edit_policy_rule(self, element_name, rule_name, service_name, layer_type, traffic_type, well_known_value,
                         application_group, application, status, cos_value, single_value, **kwargs):
        """Returns the result of edit_policy_rule."""
        args = {"layer_type": layer_type,
                "status": status,
                "application": application,
                "service_name": service_name,
                "application_group": application_group,
                "rule_name": rule_name,
                "well_known_value": well_known_value,
                "cos_value": cos_value,
                "traffic_type": traffic_type,
                "single_value": single_value}

        return self.execute_keyword(element_name, args, self.cmd.EDIT_POLICY_RULE, **kwargs)

    def verify_vlan_tree_panel(self, element_name, **kwargs):
        """Returns the result of verify_vlan_tree_panel."""
        return self.execute_keyword(element_name, {}, self.cmd.VERIFY_VLAN_TREE_PANEL, **kwargs)

    def policy_rule_navigate_to_rule_name(self, element_name, service_name, rule_name, **kwargs):
        """Returns the result of policy_rule_navigate_to_rule_name."""
        args = {"rule_name": rule_name,
                "service_name": service_name}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_NAVIGATE_TO_RULE_NAME, **kwargs)

    def policy_rule_set_cos(self, element_name, cos_value, **kwargs):
        """Returns the result of policy_rule_set_cos."""
        args = {"cos_value": cos_value}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_SET_COS, **kwargs)

    def policy_rule_set_access_control(self, element_name, access_control_value, **kwargs):
        """Returns the result of policy_rule_set_access_control."""
        args = {"access_control_value": access_control_value}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_SET_ACCESS_CONTROL, **kwargs)

    def policy_rule_traffic_description_click_edit(self, element_name, remove_traffic_description, **kwargs):
        """Returns the result of policy_rule_traffic_description_click_edit."""
        args = {"remove_traffic_description": remove_traffic_description}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_TRAFFIC_DESCRIPTION_CLICK_EDIT, **kwargs)

    def policy_rule_set_traffic_layer_type(self, element_name, layer_type, **kwargs):
        """Returns the result of policy_rule_set_traffic_layer_type."""
        args = {"layer_type": layer_type}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_SET_TRAFFIC_LAYER_TYPE, **kwargs)

    def policy_rule_set_traffic_type(self, element_name, traffic_type, **kwargs):
        """Returns the result of policy_rule_set_traffic_type."""
        args = {"traffic_type": traffic_type}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_SET_TRAFFIC_TYPE, **kwargs)

    def policy_rule_set_well_known_value(self, element_name, well_known_value, **kwargs):
        """Returns the result of policy_rule_set_well_known_value."""
        args = {"well_known_value": well_known_value}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_SET_WELL_KNOWN_VALUE, **kwargs)

    def policy_rule_set_single_value(self, element_name, single_value, **kwargs):
        """Returns the result of policy_rule_set_single_value."""
        args = {"single_value": single_value}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_SET_SINGLE_VALUE, **kwargs)

    def policy_rule_set_range_value(self, element_name, start_value, end_value, **kwargs):
        """Returns the result of policy_rule_set_range_value."""
        args = {"start_value": start_value, 'end_value': end_value}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_SET_RANGE_VALUE, **kwargs)

    def policy_rule_edit_traffic_description_click_ok(self, element_name, **kwargs):
        """Returns the result of policy_rule_edit_traffic_description_click_ok."""
        return self.execute_keyword(element_name, {}, self.cmd.POLICY_RULE_EDIT_TRAFFIC_DESCRIPTION_CLICK_OK, **kwargs)

    def policy_rule_ip_tos_dialog_click_edit(self, element_name, **kwargs):
        """Returns the result of policy_rule_ip_tos_dialog_click_edit."""
        return self.execute_keyword(element_name, {}, self.cmd.POLICY_RULE_IP_TOS_DIALOG_CLICK_EDIT, **kwargs)

    def policy_rule_ip_tos_dialog_click_ok(self, element_name, **kwargs):
        """Returns the result of policy_rule_ip_tos_dialog_click_ok."""
        return self.execute_keyword(element_name, {}, self.cmd.POLICY_RULE_IP_TOS_DIALOG_CLICK_OK, **kwargs)

    def policy_rule_set_dscp(self, element_name, well_known, dscp_value, **kwargs):
        """Returns the result of policy_rule_set_dscp."""
        args = {"dscp_value": dscp_value,
                "well_known": well_known}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_SET_DSCP, **kwargs)

    def policy_rule_set_tos(self, element_name, precedence_value, delay_sensitive_value, high_throughput_value,
                            high_reliability_value, explicit_congestion_value, **kwargs):
        """Returns the result of policy_rule_set_tos."""
        args = {"explicit_congestion_value": explicit_congestion_value,
                "precedence_value": precedence_value,
                "delay_sensitive_value": delay_sensitive_value,
                "high_throughput_value": high_throughput_value,
                "high_reliability_value": high_reliability_value}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_SET_TOS, **kwargs)

    def policy_rule_set_tos_hex(self, element_name, hex_value, **kwargs):
        """Returns the result of policy_rule_set_tos_hex."""
        args = {"hex_value": hex_value}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_SET_TOS_HEX, **kwargs)

    def policy_rule_set_tos_mask(self, element_name, mask_value, **kwargs):
        """Returns the result of policy_rule_set_tos_mask."""
        args = {"mask_value": mask_value}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_SET_TOS_MASK, **kwargs)

    def policy_rule_set_advanced_value(self, element_name, advanced_value, **kwargs):
        """Returns the result of policy_rule_set_advanced_value."""
        args = {"advanced_value": advanced_value}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_RULE_SET_ADVANCED_VALUE, **kwargs)

    def policy_confirm_device_in_domain(self, element_name, device_ip, domain_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the device to look for
        [domain_name] -   Name of the policy domain to look in
        [exists] -        Indicates whether or not the device group is expected to exist (True/False)

        Verifies whether or not the specified device exists in the specified domain.
        Passes/fails the test based on the expected value, as indicated by the "exists" argument.
        """
        args = {"device_ip": device_ip,
                "domain_name": domain_name,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_CONFIRM_DEVICE_IN_DOMAIN, **kwargs)

    def policy_confirm_device_in_current_domain(self, element_name, device_ip, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [device_ip] -     IP address of the device to look for
        [exists] -        Indicates whether or not the device group is expected to exist (True/False)

        Verifies whether or not the specified device exists in the current domain.
        Passes/fails the test based on the expected value, as indicated by the "exists" argument.
        """
        args = {"device_ip": device_ip,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_CONFIRM_DEVICE_IN_CURRENT_DOMAIN, **kwargs)

    def policy_role_default_actions_click_show_all(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Show All" button which shows all the default actions available
        for a policy role.
        """
        return self.execute_keyword(element_name, {}, self.cmd.POLICY_ROLE_DEFAULT_ACTIONS_CLICK_SHOW_ALL, **kwargs)

    def policy_role_navigate_to_role_name(self, element_name, role_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [role_name] -     Name of policy role to click on

        Navigates to the specified policy role and clicks on it
        """
        args = {"role_name": role_name}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_ROLE_NAVIGATE_TO_ROLE_NAME, **kwargs)

    def policy_role_set_access_control(self, element_name, access_control_value, **kwargs):
        """Returns the result of policy_role_set_access_control."""
        args = {"access_control_value": access_control_value}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_ROLE_SET_ACCESS_CONTROL, **kwargs)

    def policy_role_set_cos(self, element_name, cos_name, **kwargs):
        """Returns the result of policy_role_set_cos."""
        args = {"cos_name": cos_name}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_ROLE_SET_COS, **kwargs)

    def policy_role_edit_tci_overwrite(self, element_name, tci_overwrite, **kwargs):
        """Returns the result of policy_role_edit_tci_overwrite."""
        args = {"tci_overwrite": tci_overwrite}

        return self.execute_keyword(element_name, args, self.cmd.POLICY_ROLE_EDIT_TCI_OVERWRITE, **kwargs)
