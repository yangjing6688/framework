from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.pim.base.PimBaseCustomShowTools import \
    PimBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return PimCustomShowTools(device)


class PimCustomShowTools(PimBaseCustomShowTools):
    def __init__(self, device):
        super(PimCustomShowTools, self).__init__(device)

    def check_pim_state(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        pim_state = self.pw.get_value_by_offset(output, "PimStat", 2)

        result = True if pim_state == "enabled" else False
        return result, {"ret_state": pim_state}

    def check_pim_interface_state(self, output, args, **kwargs):
        interface = self.pw.get_value_at_location(output, column=0, name=None, row=7)
        interface_state = self.pw.get_value_at_location(output, column=1, name=None, row=7)

        result = True if interface == args["interface"] and interface_state == args["state"] else False
        return result, {"ret_enabled_interfaces": interface,
                        "ret_interface_state": interface_state}

    def check_pim_bsr(self, output, args, **kwargs):
        candidate_bsr_address = args["ip_address"]
        output = output.replace("\n", "\r\n")
        pim_bsr = self.pw.get_value_by_offset(output.lower(), "current bsr address", 3)

        result = True if candidate_bsr_address == pim_bsr else False
        return result, {"ret_bsr": pim_bsr}

    def check_pim_bsr_priority(self, output, args, **kwargs):
        current_bsr_priority = args["priority"]
        output = output.replace("\n", "\r\n")
        bsr_priority_found = self.pw.get_value_by_offset(output.lower(), "current bsr priority", 3)

        result = True if current_bsr_priority == bsr_priority_found else False
        return result, {"ret_bsr_priority": bsr_priority_found}

    def check_pim_candidate_bsr_priority_on_vlan(self, output, args, **kwargs):
        vlan = self.pw.get_value_at_location(output, column=0, name=None, row=13)
        priority = self.pw.get_value_at_location(output, column=1, name=None, row=13)

        result = True if vlan == args["vlan"] and priority == args["priority"] else False
        return result, {"ret_bsr_priority": priority,
                        "ret_vlan": vlan}

    def check_pim_candidate_bsr_priority_on_interface(self, output, args, **kwargs):
        interface = self.pw.get_value_at_location(output, column=0, name=None, row=13)
        priority = self.pw.get_value_at_location(output, column=1, name=None, row=13)

        result = True if interface == args["interface"] and priority == args["priority"] else False
        return result, {"ret_interface": interface,
                        "ret_priority": priority}

    def check_pim_candidate_rp_ip(self, output, args, **kwargs):
        candidate_rp_address = args["ip"]
        pim_candidate_rp_ip_found = self.pw.get_value_at_location(output, column=2, name=args["ip"], row=11)

        result = True if pim_candidate_rp_ip_found == candidate_rp_address else False
        return result, {"ret_rp_ip": pim_candidate_rp_ip_found}

    def check_pim_candidate_rp_ip_group_mask(self, output, args, **kwargs):
        candidate_rp_ip = args["ip"]
        candidate_rp_group = args["mcast_group_address"]
        candidate_rp_mask = args["mask"]
        pim_rp_ip_found = self.pw.get_value_at_location(output, column=2, name=args["ip"], row=11)
        pim_rp_group_found = self.pw.get_value_at_location(output, column=0, name=args["mcast_group_address"], row=11)
        pim_rp_mask_found = self.pw.get_value_at_location(output, column=1, name=args["mask"], row=11)

        result = (pim_rp_ip_found == candidate_rp_ip and
                  pim_rp_group_found == candidate_rp_group and
                  pim_rp_mask_found == candidate_rp_mask)
        return result, {"ret_rp_ip": pim_rp_ip_found,
                        "ret_rp_group": pim_rp_group_found,
                        "ret_rp_mask": pim_rp_mask_found}

    def check_pim_mode(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        pim_mode = self.pw.get_value_by_offset(output, "Mode", 2)

        result = True if pim_mode == args["pim_mode"] else False
        return result, {"ret_mode": pim_mode}

    def check_pim_static_rp(self, output, args, **kwargs):
        pim_static_mode = self.pw.get_value_at_location(output, column=2, name="sparse", row=8)

        result = True if pim_static_mode == "enabled" else False
        return result, {"ret_static_rp_mode": pim_static_mode}

    def check_pim_type_sparse(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        pim_mode = self.pw.get_value_by_offset(output, "Mode", 2)

        result = True if pim_mode == "sparse" else False
        return result, {"ret_mode": pim_mode}

    def check_pim_type_ssm(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        pim_mode = self.pw.get_value_by_offset(output, "Mode", 2)

        result = True if pim_mode == "ssm" else False
        return result, {"ret_mode": pim_mode}

    def check_pim_vlan_state(self, output, args, **kwargs):
        vlan = self.pw.get_value_at_location(output, column=0, name=None, row=13)
        state = self.pw.get_value_at_location(output, column=1, name=None, row=13)

        result = True if vlan == args["vlan"] and state == "enable" else False
        return result, {"ret_state": state}

    def check_pim_opertype(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
