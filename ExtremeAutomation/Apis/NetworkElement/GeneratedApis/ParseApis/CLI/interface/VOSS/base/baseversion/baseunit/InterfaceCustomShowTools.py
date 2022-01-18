from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.interface.base.InterfaceBaseCustomShowTools \
    import InterfaceBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants


def create_instance(device):
    return InterfaceCustomShowTools(device)


class InterfaceCustomShowTools(InterfaceBaseCustomShowTools):
    def __init__(self, device):
        super(InterfaceCustomShowTools, self).__init__(device)

    def check_interface_exists(self, output, args, **kwargs):

        output = output.splitlines()
        output = "\r\n".join(["vid_" + i for i in output])
        item = "vid_" + args["interface"]
        v_id = self.pw.get_value_by_offset(output, item, 0)
        v_idl = v_id.split()

        result = True if v_idl[0] == item else False

        return result, {"ret_interface": v_idl[0]}

    def check_ip_address_exists(self, output, args, **kwargs):
        ret_dict = {"ret_interface_ip": None,
                    "ret_mask": None}
        prefix_or_subnet = args["prefix_or_subnet"]
        if prefix_or_subnet is not None:
            if prefix_or_subnet.isdigit():
                prefix_or_subnet = StringUtils.mask_from_prefix(prefix_or_subnet)

            if args["ipaddr"] in output:
                mask = self.pw.get_value_by_offset(output, args["ipaddr"], 3)
                ret_dict["ret_mask"] = mask
                result = True if prefix_or_subnet == str(mask) else False
                return result, ret_dict
        else:
            self.logger.log_info("IP prefixlen/subnet not provided. Matching any instance of the IP Address.")
            result = True if args["ipaddr"] in output else False
            return result, result

        return False, False

    def check_ipv6_address_exists(self, output, args, **kwargs):
        exp_ip = StringUtils.normalize_value(args["ipaddr"], PacketConstants.IPV6_ADDRESS)
        output = output.replace("/", " ")
        ret_dict = {"ret_ipv6_addr": None,
                    "ret_prefix_len": None}
        found_ip = self.pw.get_value_by_offset(output, "UNICAST MANUAL", 0)
        found_ip = StringUtils.normalize_value(found_ip, PacketConstants.IPV6_ADDRESS)
        found_prefix = self.pw.get_value_by_offset(output, "UNICAST MANUAL", 1)
        ret_dict["ret_ipv6_addr"] = found_ip
        ret_dict["ret_prefix_len"] = found_prefix
        result = True if found_ip == exp_ip and found_prefix == args["prefix_len"] else False
        return result, ret_dict

    def check_ipv6_linklocal_exists(self, output, args, **kwargs):
        link_l = 'fe80:0000:0000:0000:' + args["ipaddr"]
        exp_ip = StringUtils.normalize_value(link_l, PacketConstants.IPV6_ADDRESS)
        output = output.replace("/", " ")
        ret_dict = {"ret_interface_ip": None,
                    "ret_prefix": None}
        found_ip = self.pw.get_value_by_offset(output, "UNICAST LINKLAYER", 0)
        found_ip = StringUtils.normalize_value(found_ip, PacketConstants.IPV6_ADDRESS)
        found_prefix = self.pw.get_value_by_offset(output, "UNICAST LINKLAYER", 1)
        ret_dict["ret_interface_ip"] = found_ip
        ret_dict["ret_prefix"] = found_prefix
        result = True if found_ip == exp_ip and found_prefix == "64" else False

        return result, ret_dict

    def check_loopback_ipv4_address(self, output, args, **kwargs):
        ip_found = self.pw.get_exact_value_by_offset(output, args["loopback_id"], 1)

        result = True if ip_found == args["ip"] else False

        return result, {"ret_loopback_ip": ip_found}

    def check_loopback_id(self, output, args, **kwargs):
        loopback_id_found = self.pw.get_exact_value_by_offset(output, args["ip"], 0)

        result = True if loopback_id_found == args["loopback_id"] else False

        return result, {"ret_loopback_id": loopback_id_found}

    def check_brouter_port_vlan(self, output, args, **kwargs):
        vlan_found = self.pw.get_exact_value_by_offset(output, args["port"], 1)

        result = True if vlan_found == args["vlan"] else False

        return result, {"ret_vlan": vlan_found}

    def check_brouter_port_ipv4(self, output, args, **kwargs):
        port_found = self.pw.get_exact_value_by_offset(output, args["ip"], 0)

        result = True if port_found == args["port"] else False

        return result, {"ret_port": port_found}

    def check_chassis_force_topology_ip_flag(self, output, args, **kwargs):
        flag_found = self.pw.get_exact_value_by_offset(output.lower(), "forcetopologyipflag", 2)

        result = True if flag_found == "true" else False

        return result, {"ret_flag": flag_found}

    def check_port_interface_name(self, output, args, **kwargs):
        port_found = self.pw.get_exact_value_by_offset(output, args["name"], 0)

        result = True if port_found == args["port"] else False

        return result, {"ret_port": port_found}

    def check_loopback_ipv6_address(self, output, args, **kwargs):
        ip_found = self.pw.get_exact_value_by_offset(output, args["loopback_id"], 1)

        result = True if ip_found == args["ipv6_addr"] else False

        return result, {"ret_ip": ip_found}

    def check_loopback_ipv6_address_exists(self, output, args, **kwargs):
        exp_ip = StringUtils.normalize_value(args["ipv6_addr"], PacketConstants.IPV6_ADDRESS)
        output = output.replace("/", " ")
        ret_dict = {"ret_interface_ip": None,
                    "ret_prefix": None}
        found_ip = self.pw.get_value_by_offset(output, "UNICAST MANUAL", 0)
        found_ip = StringUtils.normalize_value(found_ip, PacketConstants.IPV6_ADDRESS)
        found_prefix = self.pw.get_value_by_offset(output, "UNICAST MANUAL", 1)
        ret_dict["ret_interface_ip"] = found_ip
        ret_dict["ret_prefix"] = found_prefix
        result = True if found_ip == exp_ip and found_prefix == "128" else False

        return result, ret_dict

    def check_ipv6_interface_vlan_is_enabled(self, output, args, **kwargs):
        vlan = self.pw.get_value_at_location(output, column=2, name=None, row=10)
        state = self.pw.get_value_at_location(output, column=4, name=None, row=10)
        ret_dict = {"ret_vlan": vlan,
                    "ret_state": state}
        result = True if vlan == args["interface"] and state == "enable" else False

        return result, ret_dict

    def check_interface_vlan_spb_multicast_enabled(self, output, args, **kwargs):
        interface = self.pw.get_value_at_location(output, column=0, name=args["interface"], row=None)
        state = self.pw.get_value_at_location(output, column=2, name=args["interface"], row=None)
        ret_dict = {"ret_interface": interface,
                    "ret_state": state}
        result = True if interface == args["interface"] and state == "spb" else False

        return result, ret_dict

    def check_interface_vlan_vrf_spb_multicast_enabled(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        vrf_found = self.pw.get_value_by_offset(output, "VRF", 4)
        output = output.lower()
        ret_dict = {"ret_vlan": None,
                    "ret_state": None}
        if vrf_found == args["vrf_name"]:
            vlan = self.pw.get_value_at_location(output, column=0, name=args["vlan"], row=None)
            state = self.pw.get_value_at_location(output, column=2, name=args["vlan"], row=None)
            ret_dict["ret_vlan"] = vlan
            ret_dict["ret_state"] = state
            if "vlan" in vlan and "vlan" in args["vlan"] and state == "spb":
                return True, ret_dict
            elif vlan == "vlan" + args["vlan"] and state == "spb":
                return True, ret_dict

        return False, ret_dict

    def check_mac_address(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_interface_enabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
