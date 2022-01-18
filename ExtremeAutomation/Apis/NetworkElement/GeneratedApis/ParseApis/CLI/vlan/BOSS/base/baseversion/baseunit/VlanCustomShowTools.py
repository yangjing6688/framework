from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.vlan.base.VlanBaseCustomShowTools import \
    VlanBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class VlanCustomShowTools(VlanBaseCustomShowTools):
    def __init__(self, device):
        super(VlanCustomShowTools, self).__init__(device)

    def check_vlan_name(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        vlan_name = self.pw.get_value_by_offset(output, args["vlan"], 1).split(' ')
        next_after_name = self.pw.get_value_by_offset(output, args["vlan"], 2).split(' ')
        if "#" in next_after_name[0]:
            vlan_name = vlan_name[0] + " " + next_after_name[0]
        else:
            vlan_name = vlan_name[0]

        result = vlan_name == args["name"]

        return result, {"ret_vlan_name": vlan_name}

    def check_vlan_exists(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        vlan_name = self.pw.get_value_by_offset(output, args["vlan"], 0)

        result = vlan_name == args["vlan"]

        return result, {"ret_vlans": vlan_name}
