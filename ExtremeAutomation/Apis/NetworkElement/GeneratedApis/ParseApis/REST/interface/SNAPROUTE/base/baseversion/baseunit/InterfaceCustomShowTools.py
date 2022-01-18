from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.REST.interface.base.InterfaceBaseCustomShowTools \
    import InterfaceBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return InterfaceCustomShowTools(device)


class InterfaceCustomShowTools(InterfaceBaseCustomShowTools):
    def __init__(self, device):
        super(InterfaceCustomShowTools, self).__init__(device)

    def check_ip_address_exists(self, output, ip, prefix):
        try:
            dev_ip, dev_prefix = output["Object"]["IpAddr"].split("/")

            if dev_ip == ip:
                if dev_prefix == prefix:
                    return True, {"ret_ip": dev_ip,
                                  "ret_prefix": dev_prefix}
            return False, {"ret_ip": dev_ip,
                           "ret_prefix": dev_prefix}
        except KeyError:
            return False, None

    def check_interface_exists(self, output, int_type, interface, *args):
        if interface.isdigit():
            interface = "vlan" + interface

        try:
            for obj in output["Objects"]:
                if obj["Object"]["IntfRef"] == interface:
                    return True, True
        except KeyError:
            return False, None

        return False, None
