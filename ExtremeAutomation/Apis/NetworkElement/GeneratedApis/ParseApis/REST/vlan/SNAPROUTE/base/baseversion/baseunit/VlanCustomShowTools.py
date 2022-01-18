from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.REST.vlan.base.VlanBaseCustomShowTools import \
    VlanBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return VlanCustomShowTools(device)


class VlanCustomShowTools(VlanBaseCustomShowTools):
    def __init__(self, device):
        super(VlanCustomShowTools, self).__init__(device)

    def check_vlan_exists(self, output, args, **kwargs):
        try:
            for vlan_object in output["Objects"]:
                if str(vlan_object["Object"]["VlanId"]) == str(args["vlan"]):
                    return True, True
            return False, None
        except KeyError:
            return False, None

    def check_tagged_ports(self, output, args, **kwargs):
        try:
            result = True if args["port"] in output["Object"]["IntfList"] else False
            return result, {"ret_ports": str(output["Object"]["IntfList"])}
        except KeyError:
            return False, None

    def check_untagged_ports(self, output, args, **kwargs):
        try:
            result = True if args["port"] in output["Object"]["UntagIntfList"] else False
            return result, {"ret_ports": str(output["Object"]["UntagIntfList"])}
        except KeyError:
            return False, None

    def check_port_pvid(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
