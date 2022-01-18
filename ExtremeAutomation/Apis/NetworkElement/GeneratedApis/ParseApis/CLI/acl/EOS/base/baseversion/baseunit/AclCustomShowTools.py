from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.acl.base.AclBaseCustomShowTools import \
    AclBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return AclCustomShowTools(device)


class AclCustomShowTools(AclBaseCustomShowTools):
    def __init__(self, device):
        super(AclCustomShowTools, self).__init__(device)

    def check_ipv4_acl_exists(self, output, args, **kwargs):
        dev_acl_name = self.pw.get_value_by_offset(output, "Standard IP access list", 4).split()

        return True if args["acl_name"] in dev_acl_name else False, {"ret_acl_names": str(dev_acl_name)}

    def check_ipv6_acl_exists(self, output, args, **kwargs):
        dev_acl_name = self.pw.get_value_by_offset(output, "Standard IPv6 access list", 4).split()

        return True if args["acl_name"] in dev_acl_name else False, {"ret_acl_names": str(dev_acl_name)}
