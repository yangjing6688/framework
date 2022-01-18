from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.vrf.base.VrfBaseCustomShowTools import \
    VrfBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class VrfCustomShowTools(VrfBaseCustomShowTools):
    def __init__(self, device):
        super(VrfCustomShowTools, self).__init__(device)

    def verify_vrf_trap_enabled(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        state = self.pw.get_exact_value_by_offset(output, args["vrf_name"], 5)

        result = True if state == "enable" else False
        return result, {"ret_state": state}

    def verify_vrf_max_routes(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        max_routes = self.pw.get_exact_value_by_offset(output, args["vrf_name"], 3)

        result = True if max_routes == args["num_max_routes"] else False
        return result, {"ret_max_routes": max_routes}

    def verify_vrf_ipv6_max_routes(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        ipv6_max_routes = self.pw.get_exact_value_by_offset(output, args["vrf_name"], 3)

        result = True if ipv6_max_routes == args["num_max_routes"] else False
        return result, {"ret_max_routes": ipv6_max_routes}

    def verify_vrf_max_routes_trap_enabled(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        state = self.pw.get_exact_value_by_offset(output, args["vrf_name"], 4)

        result = True if state == "enable" else False
        return result, {"ret_trap_state": state}

    def verify_vrf_ipv6_max_routes_trap_enabled(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        state = self.pw.get_exact_value_by_offset(output, args["vrf_name"], 4)

        result = True if state == "enable" else False
        return result, {"ret_trap_state": state}

    def verify_vrf_name(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        name_found = self.pw.get_value_by_offset(output, args["vrf_name"], 0)

        result = True if name_found == args["vrf_name"] else False
        return result, {"ret_name": name_found}

    def verify_vrf_vrfid(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        name_found = self.pw.get_exact_value_by_offset(output, args["vrf_name"], 0)
        vrfid_found = self.pw.get_exact_value_by_offset(output, args["vrf_name"], 1)

        result = True if name_found == args["vrf_name"] and vrfid_found == args["vrfid"] else False
        return result, {"ret_vrf": name_found,
                        "ret_id": vrfid_found}

    def verify_vrf_name_and_vrfid(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        name_found = self.pw.get_exact_value_by_offset(output, args["vrf_name"], 0)
        vrfid_found = self.pw.get_exact_value_by_offset(output, args["vrf_name"], 1)

        result = True if name_found == args["vrf_name"] and vrfid_found == args["vrfid"] else False
        return result, {"ret_vrf": name_found,
                        "ret_id": vrfid_found}

    def verify_vrf_is_assigned_to_interface_vlan(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        name_found = self.pw.get_exact_value_by_offset(output, args["vrf_name"], 1)
        vlan_found = self.pw.get_exact_value_by_offset(output, args["vrf_name"], 0)

        result = True if name_found == args["vrf_name"] and vlan_found == args["vlan"] else False
        return result, {"ret_vrf": name_found,
                        "ret_vlan": vlan_found}

    def verify_router_vrf_ipvpn_is_set(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        name_found = self.pw.get_value_by_offset(output, args["vrf_name"], 3)

        result = True if name_found == args["vrf_name"] else False
        return result, {"ret_vrf": name_found}

    def verify_router_vrf_isid_is_set(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        isid_found = self.pw.get_exact_value_by_offset(output, "i-sid", 2)

        result = True if isid_found == args["i_sid"] else False
        return result, {"ret_isid": isid_found}

    def verify_router_vrf_isis_redistribute_direct(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        output_1 = output.split()
        try:
            index_1 = output_1.index(args["vrf_name"])
            vrf_found = str(output_1[index_1])
        except ValueError:
            vrf_found = "valueNotPresent"
        redistribute = self.pw.get_exact_value_by_offset(output, "loc", 0)

        result = True if vrf_found == args["vrf_name"] and redistribute == "loc" else False
        return result, {"ret_vrf": vrf_found,
                        "ret_redistribute": redistribute}

    def verify_router_vrf_isis_redistribute_direct_enabled(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        output_1 = output.split()
        try:
            index_1 = output_1.index(args["vrf_name"])
            vrf_found = str(output_1[index_1])
        except ValueError:
            vrf_found = "valueNotPresent"
        enabled = self.pw.get_exact_value_by_offset(output, "loc", 4)

        result = True if vrf_found == args["vrf_name"] and enabled == "true" else False
        return result, {"ret_vrf": vrf_found,
                        "ret_state": enabled}

    def verify_router_vrf_ipvpn_is_enabled(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        output_1 = output.split()
        try:
            index_1 = output_1.index('enabled')
            state = str(output_1[index_1])
        except ValueError:
            state = "valueNotPresent"

        result = True if state == "enabled" else False
        return result, {"ret_state": state}

    def verify_vrf_iproute(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_vrf_mvpn_enabled(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        vrf_found = self.pw.is_exact_string_present_in_output(output, args["vrf_name"])
        state = self.pw.get_value_by_offset(output, "enable", 2)

        result = vrf_found and state == "enabled"
        return result, {"ret_state": state}

    def verify_vrf_mvpn_disabled(self, output, args, **kwargs):
        output = output.lower()
        output = output.replace("\n", " ")
        parse_result = self.pw.get_exact_value_by_offset(output, "vrf", 3)
        if "valueNotPresent" in parse_result:
            return True, None
        elif self.pw.is_exact_string_present_in_output(output, "no mvpn enabled vrf exists"):
            return True, None
        elif parse_result == args["vrf_name"]:
            return False, None
        else:
            return False, None

    def verify_vrf_mvpn_fwd_cache_timeout(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
