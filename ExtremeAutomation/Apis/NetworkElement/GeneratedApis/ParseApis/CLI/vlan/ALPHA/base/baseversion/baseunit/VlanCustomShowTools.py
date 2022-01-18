from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.vlan.base.VlanBaseCustomShowTools import \
    VlanBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class VlanCustomShowTools(VlanBaseCustomShowTools):
    def __init__(self, device):
        super(VlanCustomShowTools, self).__init__(device)

    def check_vlan_name(self, output, args, **kwargs):
        for line in output.splitlines():
            if "VLAN Name:" in line:
                output_name = self.pw.get_value_from_string_to_eol(line, "VLAN Name:").replace("VLAN Name:", "").strip()
                result = output_name == args["name"]
                return result, {"ret_vlan_name": output_name}
        return False, False

    def check_vlan_exists(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                created_vlans = self.pw.get_value_by_index(line, 0)
                if created_vlans == args["vlan"]:
                    return True, {"ret_vlans": created_vlans}
        return False, False

    def check_port_pvid(self, output, args, **kwargs):
        port_pvid = self.pw.get_value_by_offset(output, args["port"], 1)
        pvid_split = port_pvid.split(' ')
        result = pvid_split[0] == args['pvid']
        return result, {"ret_port": pvid_split[0]}

    def check_tagged_ports(self, output, args, **kwargs):
        tagged = self.pw.get_value_by_offset(output, args["port"], 3)
        tagged_split = tagged.split(' ')
        result = tagged_split[0] == "Tagged"
        return result, {"ret_port": tagged_split[0]}

    def check_vlan_name_id(self, output, args, **kwargs):
        new_output = output.split()
        for index, item in enumerate(new_output):
            if item.lower() == args["vlan_name"].lower():
                vlan_id = new_output[index - 1]
                if vlan_id == args["vlan_id"]:
                    return True, {"ret_vlan": vlan_id}

        return False, False
