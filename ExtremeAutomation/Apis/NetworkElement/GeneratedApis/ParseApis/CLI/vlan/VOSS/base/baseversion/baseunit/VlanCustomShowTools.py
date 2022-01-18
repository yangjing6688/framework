from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.vlan.base.VlanBaseCustomShowTools import \
    VlanBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return VlanCustomShowTools(device)


class VlanCustomShowTools(VlanBaseCustomShowTools):
    def __init__(self, device):
        super(VlanCustomShowTools, self).__init__(device)

    def check_vlan_exists(self, output, args, **kwargs):
        result = self.pw.is_exact_string_present_in_output(output, args["vlan"])
        return result, result

    def check_untagged_ports(self, output, args, **kwargs):
        port_obj = self.it.get_port_parser_obj(args["port"])
        vlan_members = ""
        for port in port_obj.port_list:
            vlan_members = self.pw.get_value_by_offset(output, port + " ", 5).split(",")
            vlan_default = self.pw.get_value_by_offset(output, port + " ", 4)
            vlan_untag = self.pw.get_value_by_offset(output, port + " ", 7)

            if str(args["vlan"]) not in vlan_members:
                return False, {"ret_port": ', '.join(vlan_members)}
            elif vlan_default != str(args["vlan"]):
                return False, {"ret_port": vlan_members}
            elif vlan_untag.lower() != "enable":
                return False, {"ret_port": vlan_untag}
        return True, {"ret_port": ', '.join(vlan_members)}

    def check_tagged_ports(self, output, args, **kwargs):
        port_obj = self.it.get_port_parser_obj(args["port"])
        ret_dict = {"ret_untagged_ports": None,
                    "ret_tagged_ports": None}
        for port in port_obj.port_list:
            vlan_members = self.pw.get_value_by_offset(output, port + " ", 5).split(",")
            vlan_tagging = self.pw.get_value_by_offset(output, port + " ", 1)
            vlan_untag = self.pw.get_value_by_offset(output, port + " ", 9)
            ret_dict["ret_untagged_ports"] = vlan_untag
            ret_dict["ret_tagged_ports"] = vlan_tagging
            if vlan_tagging.lower() != "enable" or args['vlan'] not in vlan_members or args['vlan'] == vlan_untag:
                return False, ret_dict
        return True, ret_dict

    def check_vlan_name(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        vlan_name = self.pw.get_value_by_offset(output, args["vlan"], 2)

        if vlan_name == args["name"]:
            return True, {"ret_name": vlan_name}
        else:
            return False, {"ret_name": vlan_name}

    def check_vlan_isid(self, output, args, **kwargs):
        parse_result = self.pw.get_exact_value_by_offset(output, args["vlan"], 1)

        result = True if parse_result == args["i_sid"] else False

        return result, {"ret_isid": parse_result}

    def check_port_is_member_of_default_vlan(self, output, args, **kwargs):
        result = []
        port = ""
        for line in output.splitlines():
            if len(line) > 1:
                if line.split()[0] == "1":
                    result = line.split()[1]
                    port = line.split()[1]
                    break
        result = True if args["port"] in result else False

        return result, {"ret_port": port}

    def verify_port_encapsulation_dot1q_is_set(self, output, args, **kwargs):
        port_obj = self.it.get_port_parser_obj(args["port"])
        port1 = ""
        for port in port_obj.port_list:
            result = ""
            for line in output.splitlines():
                if len(line) > 1:
                    if line.split()[0] == port:
                        result = line.split()[5]
                        port1 = line.split()[5]
                        break
            if result != "Tagged":
                return False, {"ret_port": result}
        return True, {"ret_port": port1}

    def check_port_is_member_of_vlan(self, output, args, **kwargs):
        port_found = self.pw.get_exact_value_by_offset(output, args["vlan"], 1)

        result = self.it.compare_port_values(port_found, args["port"], self.inspect_constants.FOUNDIN)

        return result, {"ret_port": port_found}

    def check_port_pvid(self, output, args, **kwargs):
        port_obj = self.it.get_port_parser_obj(args["port"])
        pvid = str(args["pvid"])
        vlans = ""
        for port in port_obj.port_list:
            vlan_members = self.pw.get_value_by_offset(output, port + " ", 5).split(",")
            vlan_default = self.pw.get_value_by_offset(output, port + " ", 4)
            vlans = vlan_members
            if pvid == "0":
                if vlan_default != pvid:
                    return False, {"ret_pvid": vlan_default}
            else:
                if pvid not in vlan_members or vlan_default != pvid:
                    return False, {"ret_pvid": ', '.join(vlan_members)}
        return True, {"ret_pvid": ', '.join(vlans)}

    def check_vlan_name_id(self, output, args, **kwargs):
        vlan_id = self.pw.get_value_by_offset(output, args["vlan_name"], 0)
        if vlan_id == args["vlan_id"]:
            return True, {"ret_vlan": vlan_id}
        else:
            return False, {"ret_vlan": vlan_id}
