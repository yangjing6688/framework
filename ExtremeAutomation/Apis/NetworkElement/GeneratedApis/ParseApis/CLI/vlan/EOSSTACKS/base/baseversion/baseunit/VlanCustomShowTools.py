from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.vlan.base.VlanBaseCustomShowTools import \
    VlanBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class VlanCustomShowTools(VlanBaseCustomShowTools):
    def __init__(self, device):
        super(VlanCustomShowTools, self).__init__(device)

    def check_vlan_name(self, output, args, **kwargs):
        mod_output = output.replace(":", "")

        for line in mod_output.splitlines():
            if "NAME" in line:
                output_name = self.pw.get_value_from_string_to_eol(line, "NAME").replace("NAME", "").strip()
                result = output_name == args["name"]
                return result, {"ret_name": output_name}
        return False, False

    def check_vlan_exists(self, output, args, **kwargs):
        output = output.replace("VLAN Type", "VType")
        created_vlans = self.pw.get_value_by_offset_with_exclude(output, "VLAN", 2, "Name").split()

        result = args["vlan"] in created_vlans

        return result, {"ret_vlan": ', '.join(created_vlans)}

    def check_port_pvid(self, output, args, **kwargs):
        conf_pvid = self.pw.get_value_by_offset(output, "set to", 4)

        result = conf_pvid == args["pvid"]

        return result, {"ret_pvid": conf_pvid}

    def check_tagged_ports(self, output, args, **kwargs):

        output = output.replace(":\r\n", ": ")
        output = output.replace("Forbidden Egress Ports", "Forbidden")
        output = output.replace("Untagged ports", "Untagged")
        tagged_ports = self.pw.get_value_by_offset(output, "Egress Ports", 2)
        untagged_ports = self.pw.get_value_by_offset(output, "Untagged", 1)
        ret_dict = {"ret_untagged_ports": untagged_ports,
                    "ret_tagged_ports": tagged_ports}
        # Checks that the port is in the Egress Port section and NOT in the untagged port section.
        result = (self.it.compare_port_values(tagged_ports, args["port"], self.inspect_constants.FOUNDIN) and
                  self.it.compare_port_values(untagged_ports, args["port"], self.inspect_constants.NOTFOUNDIN))

        return result, ret_dict

    def check_vlan_name_id(self, output, args, **kwargs):
        new_output = output.split()
        for index, item in enumerate(new_output):
            if item.lower() == args["vlan_name"].lower():
                vlan_id = new_output[index - 2]
                if vlan_id == args["vlan_id"]:
                    return True, {"ret_vlan": vlan_id}

        return False, False
