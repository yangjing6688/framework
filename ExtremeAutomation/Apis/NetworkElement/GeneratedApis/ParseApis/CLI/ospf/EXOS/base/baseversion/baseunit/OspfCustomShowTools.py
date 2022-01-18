from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.ospf.base.OspfBaseCustomShowTools import \
    OspfBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return OspfCustomShowTools(device)


class OspfCustomShowTools(OspfBaseCustomShowTools):
    def __init__(self, device):
        super(OspfCustomShowTools, self).__init__(device)

    def verify_ospf_globally_enabled(self, output, args, **kwargs):
        ospf_output = self.pw.get_value_by_offset(output, "OSPF", 2)

        result = True if ospf_output.lower() == "enabled" else False
        return result, {"ret_state": ospf_output}

    def verify_ospf_globally_disabled(self, output, args, **kwargs):
        ospf_output = self.pw.get_value_by_offset(output, "OSPF", 2)

        result = True if ospf_output.lower() == "disabled" else False
        return result, {"ret_state": ospf_output}

    def verify_ospf_router_id(self, output, args, **kwargs):
        ospf_output = self.pw.get_value_by_offset(output, "RouterId", 2)

        result = True if ospf_output.lower() == args["router_id"] else False
        return result, {"ret_router_id": ospf_output}

    def verify_ospf_router_id_is_removed(self, output, args, **kwargs):
        ospf_output = self.pw.get_value_by_offset(output, "RouterId", 2)

        result = True if ospf_output.lower() == "0.0.0.0" else False
        return result, {"ret_router_id": ospf_output}

    def verify_ospf_neighbor_exists(self, output, args, **kwargs):
        result = False
        router_id = None
        if args["neighbor_ip"] in output:
            router_id = self.pw.get_value_by_offset(output, args["neighbor_ip"], 0)
            result = args["neighbor_id"] == router_id
        return result, {"ret_neighbor_id": router_id}

    def verify_ospf_neighbor_adjacency_full(self, output, args, **kwargs):
        result = False
        state = None
        if args["neighbor_ip"] in output:
            router_id = self.pw.get_value_by_offset(output, args["neighbor_ip"], 0)
            if args["neighbor_id"] == router_id:
                state = self.pw.get_value_by_offset(output, args["neighbor_ip"], 2)
                result = state.upper() == "FULL"
        return result, {"ret_neighbor_state": state}

    def verify_ospf_interface_authentication(self, output, args, **kwargs):
        result = False
        auth_output_value = self.pw.get_value_by_offset(output, "Authentication:", 1)
        keyid_output_value = self.pw.get_value_by_offset(output, "Key Id:", 4)
        if auth_output_value == "MD5" and keyid_output_value == args["keyid"]:
            result = True
        return result, {"ret_auth_type": auth_output_value,
                        "ret_key_id": keyid_output_value}

    def verify_ospf_interface_authentication_none(self, output, args, **kwargs):
        auth_output_value = self.pw.get_value_by_offset(output, "Authentication:", 1)

        result = True if auth_output_value == "NONE" else False
        return result, {"ret_auth_type": auth_output_value}

    def verify_ospf_metric_table_100G(self, output, args, **kwargs):
        cost_output_value = self.pw.get_value_by_offset(output, "100000M Cost (100G)", 9)

        result = True if cost_output_value == args["cost"] else False
        return result, {"ret_cost": cost_output_value}

    def verify_ospf_metric_table_100M(self, output, args, **kwargs):
        cost_output_value = self.pw.get_value_by_offset(output, "100M Cost", 7)

        result = True if cost_output_value == args["cost"] else False
        return result, {"ret_cost": cost_output_value}

    def verify_ospf_metric_table_10G(self, output, args, **kwargs):
        cost_output_value = self.pw.get_value_by_offset(output, "10000M Cost (10G)", 9)

        result = True if cost_output_value == args["cost"] else False
        return result, {"ret_cost": cost_output_value}

    def verify_ospf_metric_table_10M(self, output, args, **kwargs):
        cost_output_value = self.pw.get_value_by_offset(output, "10M Cost", 3)

        result = True if cost_output_value == args["cost"] else False
        return result, {"ret_cost": cost_output_value}

    def verify_ospf_metric_table_1G(self, output, args, **kwargs):
        cost_output_value = self.pw.get_value_by_offset(output, "1000M Cost (1G)", 4)

        result = True if cost_output_value == args["cost"] else False
        return result, {"ret_cost": cost_output_value}

    def verify_ospf_metric_table_2_5G(self, output, args, **kwargs):
        cost_output_value = self.pw.get_value_by_offset(output, "2500M Cost (2.5G)", 9)

        result = True if cost_output_value == args["cost"] else False
        return result, {"ret_cost": cost_output_value}

    def verify_ospf_metric_table_25G(self, output, args, **kwargs):
        cost_output_value = self.pw.get_value_by_offset(output, "25000M Cost (25G)", 4)

        result = True if cost_output_value == args["cost"] else False
        return result, {"ret_cost": cost_output_value}

    def verify_ospf_metric_table_40G(self, output, args, **kwargs):
        cost_output_value = self.pw.get_value_by_offset(output, "40000M Cost (40G)", 9)

        result = True if cost_output_value == args["cost"] else False
        return result, {"ret_cost": cost_output_value}

    def verify_ospf_metric_table_50G(self, output, args, **kwargs):
        cost_output_value = self.pw.get_value_by_offset(output, "50000M Cost (50G)", 4)

        result = True if cost_output_value == args["cost"] else False
        return result, {"ret_cost": cost_output_value}

    def verify_ospf_metric_table_5G(self, output, args, **kwargs):
        cost_output_value = self.pw.get_value_by_offset(output, "5000M Cost (5G)", 4)

        result = True if cost_output_value == args["cost"] else False
        return result, {"ret_cost": cost_output_value}

    def verify_ospf_enabled_on_vlan(self, output, args, **kwargs):
        vlan_state = self.pw.get_value_by_offset(output, "OSPF: ", 5)

        result = True if vlan_state == "ENABLED" else False
        return result, {"ret_vlan_state": vlan_state}

    def verify_ospf_disabled_on_vlan(self, output, args, **kwargs):
        vlan_state = self.pw.get_value_by_offset(output, "OSPF: ", 5)

        result = True if vlan_state == "DISABLED" else False
        return result, {"ret_vlan_state": vlan_state}
