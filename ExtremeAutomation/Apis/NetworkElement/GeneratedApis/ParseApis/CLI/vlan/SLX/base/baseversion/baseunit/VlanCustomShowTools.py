from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.vlan.base.VlanBaseCustomShowTools import \
    VlanBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
import re


class VlanCustomShowTools(VlanBaseCustomShowTools):
    def __init__(self, device):
        super(VlanCustomShowTools, self).__init__(device)

    def check_vlan_exists(self, output, args, **kwargs):
        vlan_list = re.findall(r"[^\w ](\d)\s+", output)
        result = args["vlan"] in vlan_list

        return result, {"ret_vlans": str(vlan_list)}

    def check_untagged_ports(self, output, args, **kwargs):
        port_string = "Eth " + args["port"]
        egress = self.pw.get_value_by_offset(output, port_string, 2)

        result = egress.strip(",").lower() == "untagged"
        return result, {"ret_egress_type": egress.strip(",")}

    def check_tagged_ports(self, output, args, **kwargs):
        port_string = "Eth " + args["port"]
        egress = self.pw.get_value_by_offset(output, port_string, 2)

        result = egress.strip(",").lower() == "tagged"
        return result, {"ret_egress_type": egress.strip(",")}

    def check_vlan_name(self, output, args, **kwargs):
        output_name = self.pw.get_value_by_offset(output, "Name:", 3)

        result = output_name == args["name"]
        return result, {"ret_name": output_name}
