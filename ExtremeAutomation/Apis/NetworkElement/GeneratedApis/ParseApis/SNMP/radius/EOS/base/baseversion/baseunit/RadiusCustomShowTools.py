from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.radius.base.RadiusBaseCustomShowTools import \
    RadiusBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return RadiusCustomShowTools(device)


class RadiusCustomShowTools(RadiusBaseCustomShowTools):
    def __init__(self, device):
        super(RadiusCustomShowTools, self).__init__(device)

    def check_radius_server_exists(self, output, args, **kwargs):
        server_ip = 'SNMPv2-SMI::enterprises.5624.1.2.4.1.5.1.3.' + str(args["index"])
        expected_address = StringUtils.ipaddr_to_pure_hex(args["addr"])
        found_ip = self.pw.get_value_by_offset(output, server_ip, 2)
        result = found_ip == expected_address
        return result, {"ret_ip": found_ip}

    def check_radius_server_status(self, output, args, **kwargs):
        server_ip = 'SNMPv2-SMI::enterprises.5624.1.2.4.1.5.1.3.' + str(args["index"])
        server_status = 'SNMPv2-SMI::enterprises.5624.1.2.4.1.5.1.8.' + str(args["index"])
        expected_address = StringUtils.ipaddr_to_pure_hex(args["addr"])

        found_ip = self.pw.get_value_by_offset(output, server_ip, 2)
        found_status = self.pw.get_value_by_offset(output, server_status, 2)
        result = found_ip == expected_address and found_status == "1"
        return result, {"ret_ip": found_ip,
                        "ret_status": found_status}
