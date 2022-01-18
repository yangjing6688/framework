from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.REST.vlan.base.VlanBaseCustomShowTools import \
    VlanBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return VlanCustomShowTools(device)


class VlanCustomShowTools(VlanBaseCustomShowTools):
    def __init__(self, device):
        super(VlanCustomShowTools, self).__init__(device)

    def check_vlan_exists(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)

        vlan_int_list = list()

        # create a list of vlan integers
        if isinstance(args['vlan'], list):
            for arg in args['vlan']:
                vlan_int_list.append(int(arg))
        else:
            vlan_int_list = [int(args["vlan"])]

        found_vlan_list = list()

        for vlan in output['openconfig-vlan:vlans']['vlan']:
            if int(vlan['config']['vlan-id']) in vlan_int_list:
                found_vlan_list.append(int(vlan['config']['vlan-id']))

        self.logger.log_info("VLANs to find: " + str(vlan_int_list))
        self.logger.log_info("VLANs found: " + str(found_vlan_list))

        result = True if vlan_int_list == found_vlan_list else False
        return result, {"ret_vlans": str(found_vlan_list)}

    def check_untagged_ports(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)

        untagged_ports = output["result"][1]["vlanProc"]["untaggedPorts"]

        result = self.it.compare_port_values(untagged_ports, args["port"], self.inspect_constants.FOUNDIN)
        return result, {"ret_ports": str(untagged_ports)}

    def check_tagged_ports(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)

        tagged_ports = output["result"][1]["vlanProc"]["taggedPorts"]

        result = self.it.compare_port_values(tagged_ports, args["port"], self.inspect_constants.FOUNDIN)
        return result, {"ret_ports": str(tagged_ports)}

    def check_vlan_state(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)

        state = output["result"][1]["vlanProc"]["adminState"]
        state = "enabled" if state == 1 else "disabled"

        result = True if state.lower() == "enabled" else False
        return result, {"ret_state": state}

    def get_vlan_tag(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)

        configured_tag = str(output["result"][1]["vlanProc"]["tag"])

        result = True if args["tag"] == configured_tag else False
        return result, {"ret_tag": configured_tag}

    def get_vlan_ipv4(self, output, args, **kwargs):
        output = StringUtils.format_json_output(output)

        configured_ip = output["result"][1]["vlanProc"]["ipAddress"]

        result = True if args["ip"] == configured_ip else False
        return result, {"ret_ip": configured_ip}
