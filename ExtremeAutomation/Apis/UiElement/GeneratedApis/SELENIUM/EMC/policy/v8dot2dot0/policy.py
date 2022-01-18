from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.EMC.policy.v8dot1dot3.policy import Policy as PolicyBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Policy(PolicyBase):
    def policy_expand_tree_panel_roles_services(self, ui_cmd_obj, arg_dict):
        self.expand_tree_panel(ui_cmd_obj, "#policyTree", "Roles/Services")
        return ui_cmd_obj

    def policy_expand_tree_panel_class_of_service(self, ui_cmd_obj, arg_dict):
        self.expand_tree_panel(ui_cmd_obj, "#cosTree", "Class of Service")
        return ui_cmd_obj

    def policy_expand_tree_panel_vlans(self, ui_cmd_obj, arg_dict):
        self.expand_tree_panel(ui_cmd_obj, "#vlanTree", "VLANs")
        return ui_cmd_obj

    def policy_expand_tree_panel_network_resources(self, ui_cmd_obj, arg_dict):
        self.expand_tree_panel(ui_cmd_obj, "#nrTree", "Network Resources")
        return ui_cmd_obj

    def policy_expand_tree_panel_devices_port_groups(self, ui_cmd_obj, arg_dict):
        self.expand_tree_panel(ui_cmd_obj, "#devicePortTreesPanel", "Devices/Port Groups")
        return ui_cmd_obj

    def expand_tree_panel(self, ui_cmd_obj, tree_id, header_name):
        component_id = '#policyNavTab #PolicyDomainView #policyDomainViewNavigationTrees #policyTreesPanel ' + tree_id

        # Only expand the tree panel if it isn't already expanded
        self.ext_builder.component_query(ui_cmd_obj, component_id, '[0].collapsed')
        if ui_cmd_obj.return_data is not False:
            self.ext_builder.click(ui_cmd_obj, component_id + ' tool => .x-tool-tool-el')
        else:
            self.logger.log_info("\nTree panel '" + header_name + "' is already expanded.\n")

        return ui_cmd_obj
