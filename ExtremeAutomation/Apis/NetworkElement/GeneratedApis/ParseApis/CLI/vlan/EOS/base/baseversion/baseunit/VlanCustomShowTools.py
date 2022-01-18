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
        output = output.replace("VLAN Type", "VType")
        created_vlans = self.pw.get_value_by_offset_with_exclude(output, "VLAN", 2, "Name").split()
        if not isinstance(created_vlans, list):
            created_vlans = [created_vlans]

        result = True if args["vlan"] in created_vlans else False

        return result, {"ret_vlans": ', '.join(created_vlans)}

    def check_untagged_ports(self, output, args, **kwargs):
        output = output.replace(":\r\n", ": ")
        untagged_ports = self.pw.get_value_by_offset(output, "Untagged Ports", 2)

        result = self.it.compare_port_values(untagged_ports, args["port"], self.inspect_constants.FOUNDIN)

        return result, {"ret_port": untagged_ports}

    def check_static_untagged_ports(self, output, args, **kwargs):
        output = output.replace(":\r\n", ": ")
        untagged_ports = self.pw.get_value_by_offset(output, "Untagged Ports", 2)

        result = self.it.compare_port_values(untagged_ports, args["port"], self.inspect_constants.FOUNDIN)

        return result, {"ret_port": untagged_ports}

    def check_untagged_operational_ports(self, output, args, **kwargs):
        output = output.replace(":\r\n", ": ")
        untagged_ports = self.pw.get_value_by_offset(output, "Untagged Ports", 2)

        result = self.it.compare_port_values(untagged_ports, args["port"], self.inspect_constants.FOUNDIN)

        return result, {"ret_port": untagged_ports}

    def check_tagged_ports(self, output, args, **kwargs):
        output = output.replace(":\r\n", ": ")
        output = output.replace("Forbidden Egress Ports", "Forbidden")
        output = output.replace("Untagged Ports", "Untagged")
        tagged_ports = self.pw.get_value_by_offset(output, "Egress Ports", 2)
        untagged_ports = self.pw.get_value_by_offset(output, "Untagged", 1)
        ret_dict = {"ret_untagged_ports": untagged_ports,
                    "ret_tagged_ports": tagged_ports}
        # Checks that the port is in the Egress Port section and NOT in the untagged port section.
        result = (self.it.compare_port_values(tagged_ports, args["port"], self.inspect_constants.FOUNDIN) and
                  self.it.compare_port_values(untagged_ports, args["port"], self.inspect_constants.NOTFOUNDIN))

        return result, ret_dict

    def check_tagged_operational_ports(self, output, args, **kwargs):
        output = output.replace(":\r\n", ": ")
        output = output.replace("Forbidden Egress Ports", "Forbidden")
        output = output.replace("Untagged Ports", "Untagged")
        tagged_ports = self.pw.get_value_by_offset(output, "Egress Ports", 2)
        untagged_ports = self.pw.get_value_by_offset(output, "Untagged", 1)
        ret_dict = {"ret_untagged_ports": untagged_ports,
                    "ret_tagged_ports": tagged_ports}
        # Checks that the port is in the Egress Port section and NOT in the untagged port section.
        result = (self.it.compare_port_values(tagged_ports, args["port"], self.inspect_constants.FOUNDIN) and
                  self.it.compare_port_values(untagged_ports, args["port"], self.inspect_constants.NOTFOUNDIN))

        return result, ret_dict

    def check_forbidden_ports(self, output, args, **kwargs):
        output = output.replace(":\r\n", ": ")
        forbidden_ports = self.pw.get_value_by_offset(output, "Forbidden Egress Ports", 3)
        result = self.it.compare_port_values(forbidden_ports, args["port"], self.inspect_constants.FOUNDIN)

        return result, {"ret_port": forbidden_ports}

    def check_vlan_state(self, output, args, **kwargs):
        state = self.pw.get_value_by_offset(output, "Status", 5)

        result = True if state.lower() == "enabled" else False

        return result, {"ret_state": state}

    def check_vlan_description(self, output, args, **kwargs):
        new_out = self.pw.get_eol_value(output, "Name       : ")[0]
        output_name = self.pw.get_value_from_string_to_eol(new_out, "Name       : ")

        result = True if str(output_name) == str(args["description"]) else False

        return result, {"ret_name": str(output_name)}

    def check_port_pvid(self, output, args, **kwargs):
        conf_pvid = self.pw.get_value_by_offset(output, "set to", 4)

        result = True if conf_pvid == args["pvid"] else False

        return result, {"ret_pvid": conf_pvid}

    def get_vlan_tag(self, output, args, **kwargs):
        configured_tag = self.pw.get_value_by_offset(output, "FID", 2)

        result = True if args["tag"] == configured_tag else False

        return result, {"ret_tag": configured_tag}

    def check_vlan_on_port_tagged_egress(self, output, args, **kwargs):
        output = output.replace(" ", "")
        result = args["port"] + args["vlan"] + "tagged" + "static" in output

        return result, result

    def check_vlan_on_port_untagged_egress(self, output, args, **kwargs):
        output = output.replace(" ", "")
        result = args["port"] + args["vlan"] + "untagged" + "static" in output

        return result, result

    def check_vman_exists(self, output, args, **kwargs):
        output = output.replace("VLAN Type", "VType")
        created_vlans = self.pw.get_value_by_offset_with_exclude(output, "VLAN", 2, "Name").split()
        if not isinstance(created_vlans, list):
            created_vlans = [created_vlans]

        result = True if args["vman"] in created_vlans else False

        return result, {"ret_vmans": ', '.join(created_vlans)}

    def check_vlan_name(self, output, args, **kwargs):
        mod_output = output.replace(":", "")

        for line in mod_output.splitlines():
            if "Name" in line:
                output_name = self.pw.get_value_from_string_to_eol(line, "Name").replace("Name", "").strip()
                result = output_name == args["name"]
                return result, {"ret_name": output_name}
        return False, False

    def check_vlan_name_id(self, output, args, **kwargs):
        index = 0
        output = output.replace(":", '')
        new_output = output.split()
        for item in new_output:
            if item.lower() == args["vlan_name"].lower():
                vlan_id = new_output[index - 2]
                if vlan_id == args["vlan_id"]:
                    return True, {"ret_vlan": vlan_id}
                else:
                    index = index + 1
            else:
                index = index + 1

        return False, False
