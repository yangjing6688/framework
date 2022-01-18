from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.nd.base.NdBaseCustomShowTools import \
    NdBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants


def create_instance(device):
    return NdCustomShowTools(device)


class NdCustomShowTools(NdBaseCustomShowTools):
    def __init__(self, device):
        super(NdCustomShowTools, self).__init__(device)

    def check_nd_entry_exists(self, output, args, **kwargs):
        exp_ip = StringUtils.normalize_value(args["ipv6_addr"], PacketConstants.IPV6_ADDRESS)
        exp_mac = StringUtils.normalize_mac(args["hw_addr"])
        output = output.replace("/", "")
        out1 = output.split()[:-1]
        found_ip = None
        found_mac = None
        ret_dict = {"ret_ipv6_entries": None,
                    "ret_mac_entries": None,
                    "ret_interfaces": None}
        for i, j in enumerate(out1):
            if exp_ip == StringUtils.normalize_value(j, PacketConstants.IPV6_ADDRESS):
                found_ip = StringUtils.normalize_value(j, PacketConstants.IPV6_ADDRESS)
                k = i + 6
                if exp_mac == StringUtils.normalize_mac(out1[k]):
                    found_mac = StringUtils.normalize_mac(out1[k])
        ret_dict["ret_ipv6_entries"] = found_ip
        ret_dict["ret_mac_entries"] = found_mac
        result = True if found_ip == exp_ip and found_mac == exp_mac else False

        return result, ret_dict
