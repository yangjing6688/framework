from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.interface.base.InterfaceBaseCustomShowTools \
    import InterfaceBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
import re


def create_instance(device):
    return InterfaceCustomShowTools(device)


class InterfaceCustomShowTools(InterfaceBaseCustomShowTools):
    def __init__(self, device):
        super(InterfaceCustomShowTools, self).__init__(device)

    def check_interface_exists(self, output, args, **kwargs):
        vlan_exos = StringUtils.exos_vlan_string(args["interface"])

        output = output.replace("show " + args["intf"] + " " + vlan_exos, "")
        interface_status = self.pw.get_value_by_offset(output, "VLAN Interface", 4)
        interface_status2 = vlan_exos in output

        result = True if (interface_status == vlan_exos) or (interface_status2 is True) else False

        return result, {"ret_interface": interface_status}

    def check_loopback_exists(self, output, args, **kwargs):
        interface = " " + args["interface"] + " "
        vid_from_output = re.findall("(" + interface + r")[^\/]", output)

        result = False
        if len(vid_from_output) == 1:
            vid_from_output = vid_from_output[0].replace(" ", "")
            result = vid_from_output == args["interface"]

        return result, {"ret_interface": str(vid_from_output)}

    def check_ip_address_exists(self, output, args, **kwargs):
        ret_dict = {"ret_interface_ip": None,
                    "ret_mask": None}
        if args["prefix_or_subnet"] is not None:
            if args["prefix_or_subnet"].isdigit():
                ip_addr = args["ipaddr"] + "/" + args["prefix_or_subnet"]
            else:
                ip_addr = args["ipaddr"] + "/" + StringUtils.prefix_len(args["prefix_or_subnet"])

            interface_ip = self.pw.get_value_by_offset(output, "Primary IP:", 2)
            ret_dict["ret_interface_ip"] = interface_ip
            result = True if interface_ip == ip_addr else False
            return result, ret_dict

        else:
            self.logger.log_info("IP prefixlen/subnet not provided. Matching any instance of the IP Address.")
            result = True if args["ipaddr"] in output else False
            return result, result

    def check_ipv6_address_exists(self, output, args, **kwargs):
        output = output.splitlines()
        start = None
        end = None
        ret_dict = {"ret_ipv6_addr": None,
                    "ret_prefix_len": None}
        ipv6_addr = StringUtils.collapse_ipv6_address(args["ipaddr"])

        for i in range(len(output)):
            if output[i].find("IPv6:") > 0 and start is None:
                start = i
            if output[i].find("STPD:") > 0 and start is not None:
                end = i
                break

        configured_ipv6_addrs = output[start:end]

        for addr in configured_ipv6_addrs:
            addr = addr.replace("/", " / ").replace("IPv6:", "")
            dev_ipv6_addr = self.pw.get_value_by_offset(addr, "", 0)
            dev_prefix_len = self.pw.get_value_by_offset(addr, "", 2)
            ret_dict["ret_ipv6_addr"] = dev_ipv6_addr
            ret_dict["ret_prefix_len"] = dev_prefix_len
            if dev_ipv6_addr == ipv6_addr and dev_prefix_len == args["prefix_len"]:
                result = True
                return result, ret_dict
        result = False
        return result, ret_dict

    def check_ipv6_linklocal_exists(self, output, args, **kwargs):
        ret_dict = {"ret_interface_ip": None,
                    "ret_prefix": None}
        interface_ip = self.pw.get_value_by_offset(output, "IPv6:", 1)
        ip_addr = args["ipaddr"] + "/" + args["prefix_len"]
        ret_dict["ret_interface_ip"] = interface_ip
        result = True if interface_ip == ip_addr else False

        return result, ret_dict

    def check_interface_enabled(self, output, args, **kwargs):
        output_state = self.pw.get_value_by_offset(output, "Admin State:", 2)

        result = True if output_state.lower() == "enabled" else False

        return result, {"ret_output_state": output_state}

    def check_mac_address(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
