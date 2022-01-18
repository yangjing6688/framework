from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.interface.base.InterfaceBaseCustomShowTools \
    import InterfaceBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return InterfaceCustomShowTools(device)


class InterfaceCustomShowTools(InterfaceBaseCustomShowTools):
    def __init__(self, device):
        super(InterfaceCustomShowTools, self).__init__(device)

    def check_interface_exists(self, output, args, **kwargs):
        interfaces = self.pw.get_value_by_offset(output, "Operationally", 0).split()
        intf_arg = StringUtils.eos_interface(args["interface"])

        result = True if intf_arg in interfaces else False

        return result, {"ret_interface": ', '.join(interfaces)}

    def check_loopback_exists(self, output, args, **kwargs):
        intf_arg = StringUtils.eos_interface(args["interface"], "loop")
        interfaces = self.pw.get_value_by_offset(output, "Operationally", 0).split()

        result = True if intf_arg in interfaces else False

        return result, {"ret_interface": ', '.join(interfaces)}

    def check_ip_address_exists(self, output, args, **kwargs):
        ret_dict = {"ret_interface_ip": None,
                    "ret_mask": None}
        if args["prefix_or_subnet"] is not None:
            if args["prefix_or_subnet"].isdigit():
                prefix_or_subnet = StringUtils.mask_from_prefix(args["prefix_or_subnet"])
            else:
                prefix_or_subnet = args["prefix_or_subnet"]

            interface_ip = self.pw.get_value_by_offset(output, "IP Address", 2)
            mask = self.pw.get_value_by_offset(output, "IP Address", 4)
            ret_dict["ret_interface_ip"] = interface_ip
            ret_dict["ret_interface"] = mask
            result = True if interface_ip == args["ipaddr"] and prefix_or_subnet == mask else False

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
            if output[i].find("Global unicast") > 0 and start is None:
                start = i + 1
            if output[i].find("Joined group") > 0 and start is not None:
                end = i
                break

        configured_ipv6_addrs = output[start:end]

        for addr in configured_ipv6_addrs:
            addr = addr.replace("/", "/ ").replace(",", "").replace("[", " [")
            dev_ipv6_addr = self.pw.get_value_by_offset(addr, "", 0)
            dev_prefix_len = self.pw.get_value_by_offset(addr, "", 4)
            ret_dict["ret_ipv6_addr"] = dev_ipv6_addr
            ret_dict["ret_prefix_len"] = dev_prefix_len
            if dev_ipv6_addr == ipv6_addr and dev_prefix_len == args["prefix_len"]:
                result = True
                return result, ret_dict
        result = False
        return result, ret_dict

    def check_ipv6_linklocal_exists(self, output, args, **kwargs):
        """
        This function verifies the IPv6 Link-Local address assigned to an interface.
        """
        ret_dict = {"ret_interface_ip": None,
                    "ret_prefix": None}
        output = output.replace("%", " ")
        interface_ip = self.pw.get_value_by_offset(output, "link-local address is", 6)
        ret_dict["ret_interface_ip"] = interface_ip
        result = True if interface_ip == args["ipaddr"] else False

        return result, ret_dict

    def check_mac_address(self, output, args, **kwargs):
        output_mac = self.pw.get_value_by_offset(output, "MAC-Address", 2)

        output_mac = StringUtils.normalize_mac(output_mac)
        mac = StringUtils.normalize_mac(args["mac"])

        result = True if output_mac == mac else False

        return result, {"ret_output_mac": output_mac}

    def check_interface_enabled(self, output, args, **kwargs):
        output_state = self.pw.get_value_by_offset(output, "Administratively", 5)

        result = True if output_state.lower() == "up" else False

        return result, {"ret_output_state": output_state}
