from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.arp.base.ArpBaseCustomShowTools import \
    ArpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return ArpCustomShowTools(device)


class ArpCustomShowTools(ArpBaseCustomShowTools):
    def __init__(self, device):
        super(ArpCustomShowTools, self).__init__(device)

    def verify_arp_entry_exists(self, output, ip_arg, mac_arg, int_arg):
        words = [w.replace('.', ' ', 1) for w in (output.replace('SNMPv2-SMI::mib-2.4.22.1.2.', "")).split('\r\n')]
        out2 = '\r\n'.join([w.replace('0x', '', 1) for w in words])

        ipaddr = self.pw.get_value_by_offset(out2, ip_arg, 1)
        macaddr = self.pw.get_value_by_offset(out2, ip_arg, 3)

        if ipaddr == self.constants.VALUE_NOT_PRESENT:
            return False, None

        macaddr = StringUtils.normalize_mac(macaddr)
        mac_arg = StringUtils.normalize_mac(mac_arg)

        result = ipaddr == ip_arg and macaddr == mac_arg

        return result, {"ret_ip": ipaddr,
                        "ret_mac": macaddr}
