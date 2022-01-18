from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.spbm.base.SpbmBaseCustomShowTools import \
    SpbmBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return SpbmCustomShowTools(device)


class SpbmCustomShowTools(SpbmBaseCustomShowTools):
    def __init__(self, device):
        super(SpbmCustomShowTools, self).__init__(device)

    def check_spbm_ethertype(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.78.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["integer_ethertype"] else False
        return result, {"ret_ethertype": parse_result}

    def verify_spbm_enabled(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.78.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}

    def verify_spbm_ip_enabled(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.4.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}

    def verify_spbm_ipv6_enabled(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.4.1.14." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}

    def verify_spbm_lsdb_trap_enabled(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.4.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}

    def verify_isis_spbm_instance_id(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.4.1.2." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "0" else False
        return result, {"ret_id": parse_result}

    def verify_isis_spbm_nick_name(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.4.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        name_arg = StringUtils().normalize_hex_string_to_0x_hex_expression(args["nickname"])

        result = True if parse_result == name_arg else False
        return result, {"ret_nickname": parse_result}

    def verify_isis_spbm_bvid(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.4.1.4." + args["oid_index"]
        final_hex = self.pw.get_value_by_offset(output, item, 2)
        if final_hex.startswith("0x"):
            final_hex = final_hex[2:]
            final_hex = list(final_hex)
            final_hex = ["8"] + final_hex
            final_hex = "".join(final_hex)
            d_bin = bin(int(final_hex, 16))[2:]
            d_bin = d_bin[3:]
            vlans = [i for i in range(len(d_bin)) if d_bin.startswith('1', i)]
            vlans = map(str, vlans)
            found_vlans = "\r\n".join(vlans)

            result = True if args["bvid"] in found_vlans else False
            return result, {"ret_bvids": str(found_vlans)}
        else:
            return False, None

    def verify_isis_spbm_multicast_enabled(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.4.1.12." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}

    def verify_isis_spbm_smlt_virtual_bmac(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.4.1.10." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        bmac_arg = StringUtils().normalize_hex_string_to_0x_hex_expression(args["bmac"])

        result = True if parse_result == bmac_arg else False
        return result, {"ret_bmac": parse_result}

    def verify_isis_spbm_smlt_peer_system_id(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.4.1.11." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        sysid_arg = StringUtils().normalize_hex_string_to_0x_hex_expression(args["peer_sys_id"])

        result = True if parse_result == sysid_arg else False
        return result, {"ret_sys_id": parse_result}

    def check_isis_spbm_instance_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.5.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "0" else False
        return result, {"ret_instance": parse_result}

    def check_isis_spbm_admin_status_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.5.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_status": parse_result}

    def check_isis_spbm_oper_status_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.2.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_status": parse_result}

    def check_isis_spbm_adjacencies_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.2.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["total_adj"] else False
        return result, {"ret_adj_on_port": parse_result}

    def check_isis_spbm_up_adjacencies_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.2.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["up_adj"] else False
        return result, {"ret_adj_on_port": parse_result}

    def check_isis_spbm_l1_metric_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.5.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["l1_metric"] else False
        return result, {"ret_l1_metric": parse_result}

    def check_isis_spbm_type_broadcast_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.5.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_type": parse_result}

    def check_isis_spbm_type_point_to_point_on_port(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.5.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "2" else False
        return result, {"ret_type": parse_result}

    def check_isis_spbm_instance_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.5.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "0" else False
        return result, {"ret_instance": parse_result}

    def check_isis_spbm_admin_status_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.5.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_status": parse_result}

    def check_isis_spbm_oper_status_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.2.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_status": parse_result}

    def check_isis_spbm_adjacencies_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.2.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["total_adj"] else False
        return result, {"ret_adj_on_mlt": parse_result}

    def check_isis_spbm_up_adjacencies_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.2.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["up_adj"] else False
        return result, {"ret_adj_on_mlt": parse_result}

    def check_isis_spbm_l1_metric_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.5.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["l1_metric"] else False
        return result, {"ret_l1_metric": parse_result}

    def check_isis_spbm_type_broadcast_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.5.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_type": parse_result}

    def check_isis_spbm_type_point_to_point_on_mlt(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.5.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "2" else False
        return result, {"ret_type": parse_result}

    def check_isis_spbm_smlt_split_beb_primary(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.4.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_beb_primary": parse_result}

    def check_isis_spbm_smlt_split_beb_secondary(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.4.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "2" else False
        return result, {"ret_beb_secondary": parse_result}

    def check_isis_spbm_unicast_fib_host_name(self, output, args, **kwargs):
        da_index = StringUtils().hex_str_to_dotted_decimal(args["da"].lower())
        sysid_index = StringUtils().hex_str_to_dotted_decimal(args["sysid"].lower())

        item = "SNMPv2-SMI::enterprises.2272.1.63.13.1.5." + sysid_index + "." + args["bvlan"] + "." + da_index
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["hostname"] else False
        return result, {"ret_hostname": parse_result}

    def check_isis_spbm_unicast_fib_cost(self, output, args, **kwargs):
        da_index = StringUtils().hex_str_to_dotted_decimal(args["da"].lower())
        sysid_index = StringUtils().hex_str_to_dotted_decimal(args["sysid"].lower())

        item = "SNMPv2-SMI::enterprises.2272.1.63.13.1.6." + sysid_index + "." + args["bvlan"] + "." + da_index
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["cost"] else False
        return result, {"ret_cost": parse_result}

    def check_isis_spbm_unicast_fib_outgoing_interface(self, output, args, **kwargs):
        da_index = StringUtils().hex_str_to_dotted_decimal(args["da"].lower())
        sysid_index = StringUtils().hex_str_to_dotted_decimal(args["sysid"].lower())
        item = "SNMPv2-SMI::enterprises.2272.1.63.13.1.4." + sysid_index + "." + args["bvlan"] + "." + da_index
        parse_result = self.pw.get_value_by_offset(output, item, 2)
        if parse_result == "111":
            parse_result = "cpp"

        result = True if parse_result == args["port_num_index"] else False
        return result, {"ret_interface": parse_result}

    def check_isis_spbm_multicast_fwd_cache_timeout(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.4.1.13." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["timeout"] else False
        return result, {"ret_timeout": parse_result}

    def check_isis_spbm_multicast_fib_isid(self, output, args, **kwargs):
        da_index = StringUtils().hex_str_to_dotted_decimal(args["da"].lower())
        sysid_index = StringUtils().hex_str_to_dotted_decimal(args["sysid"].lower())
        item = "SNMPv2-SMI::enterprises.2272.1.63.14.1.4." + sysid_index + "." + args["bvlan"] + "." + da_index
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["isid"] else False
        return result, {"ret_isid": parse_result}

    def check_isis_spbm_multicast_fib_type(self, output, args, **kwargs):
        da_index = StringUtils().hex_str_to_dotted_decimal(args["da"].lower())
        sysid_index = StringUtils().hex_str_to_dotted_decimal(args["sysid"].lower())
        item = "SNMPv2-SMI::enterprises.2272.1.63.14.1.6." + sysid_index + "." + args["bvlan"] + "." + da_index
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["fib_type"] else False
        return result, {"ret_type": parse_result}

    def check_isis_spbm_multicast_fib_host_name(self, output, args, **kwargs):
        da_index = StringUtils().hex_str_to_dotted_decimal(args["da"].lower())
        sysid_index = StringUtils().hex_str_to_dotted_decimal(args["sysid"].lower())
        item = "SNMPv2-SMI::enterprises.2272.1.63.14.1.8." + sysid_index + "." + args["bvlan"] + "." + da_index
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["hostname"] else False
        return result, {"ret_hostname": parse_result}

    def check_isis_spbm_multicast_fib_out_ports(self, output, args, **kwargs):
        da_index = StringUtils().hex_str_to_dotted_decimal(args["da"].lower())
        sysid_index = StringUtils().hex_str_to_dotted_decimal(args["sysid"].lower())
        item = "SNMPv2-SMI::enterprises.2272.1.63.14.1.9." + sysid_index + "." + args["bvlan"] + "." + da_index
        final_hex = self.pw.get_value_by_offset(output, item, 2)
        final_hex = final_hex[2:]
        final_hex = list(final_hex)
        final_hex[0] = '8'
        final_hex = "".join(final_hex)
        d_bin = bin(int(final_hex, 16))[2:]
        ports = [i for i in range(len(d_bin)) if d_bin.startswith('1', i)]
        ports.pop(0)
        ports = map(str, ports)
        found_ports = "\r\n".join(ports)

        result = True if args["port_index"] in found_ports else False
        return result, {"ret_ports": str(found_ports)}

    def check_isis_spbm_multicast_fib_out_mlts(self, output, args, **kwargs):
        da_index = StringUtils().hex_str_to_dotted_decimal(args["da"].lower())
        sysid_index = StringUtils().hex_str_to_dotted_decimal(args["sysid"].lower())
        item = "SNMPv2-SMI::enterprises.2272.1.63.14.1.10." + sysid_index + "." + args["bvlan"] + "." + da_index
        final_hex = self.pw.get_value_by_offset(output, item, 2)
        if final_hex.startswith("0x"):
            final_hex = final_hex[2:]
            final_hex = list(final_hex)
            final_hex = ['8'] + final_hex
            final_hex = "".join(final_hex)
            d_bin = bin(int(final_hex, 16))[2:]
            nd_bin = d_bin[3:]
            mlts = [i for i in range(len(nd_bin)) if nd_bin.startswith('1', i)]
            mlts = map(str, mlts)
            found_mlts = "\r\n".join(mlts)
        else:
            found_mlts = "0"

        result = True if args["mlt_id"] in found_mlts else False
        return result, {"ret_mlts": str(found_mlts)}

    def check_isis_spbm_multicast_fib_in_ports(self, output, args, **kwargs):
        da_index = StringUtils().hex_str_to_dotted_decimal(args["da"].lower())
        sysid_index = StringUtils().hex_str_to_dotted_decimal(args["sysid"].lower())
        item = "SNMPv2-SMI::enterprises.2272.1.63.14.1.11." + sysid_index + "." + args["bvlan"] + "." + da_index
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["port_index"] else False
        return result, {"ret_port": parse_result}

    def check_isis_spbm_multicast_fib_in_mlts(self, output, args, **kwargs):
        da_index = StringUtils().hex_str_to_dotted_decimal(args["da"].lower())
        sysid_index = StringUtils().hex_str_to_dotted_decimal(args["sysid"].lower())
        item = "SNMPv2-SMI::enterprises.2272.1.63.14.1.11." + sysid_index + "." + args["bvlan"] + "." + da_index
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["mlt_index"] else False
        return result, {"ret_mlt": parse_result}

    def check_isis_spbm_instance_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.5.1.3." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "0" else False
        return result, {"ret_instance": parse_result}

    def check_isis_spbm_admin_status_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.5.1.4." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_status": parse_result}

    def check_isis_spbm_oper_status_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.2.1.8." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_status": parse_result}

    def check_isis_spbm_adjacencies_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.2.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["total_adj"] else False
        return result, {"ret_adj_on_logical": parse_result}

    def check_isis_spbm_up_adjacencies_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.2.1.9." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["up_adj"] else False
        return result, {"ret_adj_on_logical": parse_result}

    def check_isis_spbm_l1_metric_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.5.1.7." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == args["l1_metric"] else False
        return result, {"ret_l1_metric": parse_result}

    def check_isis_spbm_type_broadcast_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.5.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_type": parse_result}

    def check_isis_spbm_type_point_to_point_on_logical_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.63.5.1.5." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == "2" else False
        return result, {"ret_type": parse_result}

    def check_isis_spbm_ip_unicast_fib_entry_exists(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                new1 = line.replace("SNMPv2-SMI::enterprises.2272.1.63.21.1.", "").replace(" ", "").\
                    replace("=", ".").split(".")
                if new1[3] == "4":
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "/" + new1[8]
                    expected_dest = args["dest"]
                else:
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "." + new1[8] + "." + \
                        new1[9] + "." + new1[10] + "." + new1[11] + "." + new1[12] + "." + new1[13] + "." + \
                        new1[14] + "." + new1[15] + "." + new1[16] + "." + new1[17] + "." + new1[18] + "." + \
                        new1[19] + "." + new1[20]

                    temp_ipv6_mask = args["dest"].split("/")
                    ipv6addr = StringUtils().ipv6_to_dec(temp_ipv6_mask[0])
                    ipv6mask = temp_ipv6_mask[1]
                    expected_dest = ipv6addr + "." + ipv6mask

                found_nh_beb = new1[-1]
                found_bvlan = new1[-2]

                if found_dest == expected_dest and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"]:
                    return True, {"ret_dest": found_dest,
                                  "ret_nh_beb": found_nh_beb,
                                  "ret_bvlan": found_bvlan}

        return False, None

    def check_isis_spbm_ip_unicast_fib_spbm_cost(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                new1 = line.replace("SNMPv2-SMI::enterprises.2272.1.63.21.1.", "").replace(" ", "").\
                    replace("=", ".").split(".")

                if new1[3] == "4":
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "/" + new1[8]
                    expected_dest = args["dest"]
                else:
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "." + new1[8] + "." + \
                        new1[9] + "." + new1[10] + "." + new1[11] + "." + new1[12] + "." + new1[13] + "." + \
                        new1[14] + "." + new1[15] + "." + new1[16] + "." + new1[17] + "." + new1[18] + "." + \
                        new1[19] + "." + new1[20]

                    temp_ipv6_mask = args["dest"].split("/")
                    ipv6addr = StringUtils().ipv6_to_dec(temp_ipv6_mask[0])
                    ipv6mask = temp_ipv6_mask[1]
                    expected_dest = ipv6addr + "." + ipv6mask

                found_nh_beb = new1[-1]
                found_bvlan = new1[-2]
                if found_dest == expected_dest and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"]:
                    g = line.replace(" ", "").split("=")[0]
                    nl = list(g)
                    nl[39] = '12'
                    item = ''.join(nl)
                    parse_result = self.pw.get_value_by_offset(output, item, 2)

                    result = True if parse_result == args["spbm_cost"] else False
                    return result, {"ret_cost": parse_result}

        return False, None

    def check_isis_spbm_ip_unicast_fib_prefix_cost(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                new1 = line.replace("SNMPv2-SMI::enterprises.2272.1.63.21.1.", "").replace(" ", "").\
                    replace("=", ".").split(".")
                if new1[3] == "4":
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "/" + new1[8]
                    expected_dest = args["dest"]
                else:
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "." + new1[8] + "." + \
                        new1[9] + "." + new1[10] + "." + new1[11] + "." + new1[12] + "." + new1[13] + "." + \
                        new1[14] + "." + new1[15] + "." + new1[16] + "." + new1[17] + "." + new1[18] + "." + \
                        new1[19] + "." + new1[20]

                    temp_ipv6_mask = args["dest"].split("/")
                    ipv6addr = StringUtils().ipv6_to_dec(temp_ipv6_mask[0])
                    ipv6mask = temp_ipv6_mask[1]
                    expected_dest = ipv6addr + "." + ipv6mask

                found_nh_beb = new1[-1]
                found_bvlan = new1[-2]
                if found_dest == expected_dest and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"]:
                    g = line.replace(" ", "").split("=")[0]
                    nl = list(g)
                    nl[39] = '11'
                    item = ''.join(nl)
                    parse_result = self.pw.get_value_by_offset(output, item, 2)

                    result = True if parse_result == args["prefix_cost"] else False
                    return result, {"ret_cost": parse_result}

        return False, None

    def check_isis_spbm_ip_unicast_fib_ip_route_preference(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                new1 = line.replace("SNMPv2-SMI::enterprises.2272.1.63.21.1.", "").replace(" ", "").\
                    replace("=", ".").split(".")
                if new1[3] == "4":
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "/" + new1[8]
                    expected_dest = args["dest"]
                else:
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "." + new1[8] + "." + \
                        new1[9] + "." + new1[10] + "." + new1[11] + "." + new1[12] + "." + new1[13] + "." + \
                        new1[14] + "." + new1[15] + "." + new1[16] + "." + new1[17] + "." + new1[18] + "." + \
                        new1[19] + "." + new1[20]

                    temp_ipv6_mask = args["dest"].split("/")
                    ipv6addr = StringUtils().ipv6_to_dec(temp_ipv6_mask[0])
                    ipv6mask = temp_ipv6_mask[1]
                    expected_dest = ipv6addr + "." + ipv6mask

                found_nh_beb = new1[-1]
                found_bvlan = new1[-2]
                if found_dest == expected_dest and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"]:
                    g = line.replace(" ", "").split("=")[0]
                    nl = list(g)
                    nl[39] = '13'
                    item = ''.join(nl)
                    parse_result = self.pw.get_value_by_offset(output, item, 2)

                    result = True if parse_result == args["ip_route_pref"] else False
                    return result, {"ret_preference": parse_result}

        return False, None

    def check_isis_spbm_ip_unicast_fib_destination_isid(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                new1 = line.replace("SNMPv2-SMI::enterprises.2272.1.63.21.1.", "").replace(" ", "").\
                    replace("=", ".").split(".")
                if new1[3] == "4":
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "/" + new1[8]
                    expected_dest = args["dest"]
                else:
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "." + new1[8] + "." + \
                        new1[9] + "." + new1[10] + "." + new1[11] + "." + new1[12] + "." + new1[13] + "." + \
                        new1[14] + "." + new1[15] + "." + new1[16] + "." + new1[17] + "." + new1[18] + "." + \
                        new1[19] + "." + new1[20]

                    temp_ipv6_mask = args["dest"].split("/")
                    ipv6addr = StringUtils().ipv6_to_dec(temp_ipv6_mask[0])
                    ipv6mask = temp_ipv6_mask[1]
                    expected_dest = ipv6addr + "." + ipv6mask

                found_nh_beb = new1[-1]
                found_bvlan = new1[-2]
                found_dest_isid = new1[-3]

                if found_dest == expected_dest and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"] \
                        and found_dest_isid == args["dest_isid"]:
                    return True, {"ret_dest": found_dest,
                                  "ret_nh_beb": found_nh_beb,
                                  "ret_bvlan": found_bvlan}

        return False, None

    def check_isis_spbm_ip_unicast_fib_nh_mac(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                new1 = line.replace("SNMPv2-SMI::enterprises.2272.1.63.21.1.", "").replace(" ", "").\
                    replace("=", ".").split(".")
                if new1[3] == "4":
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "/" + new1[8]
                    expected_dest = args["dest"]
                else:
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "." + new1[8] + "." + \
                        new1[9] + "." + new1[10] + "." + new1[11] + "." + new1[12] + "." + new1[13] + "." + \
                        new1[14] + "." + new1[15] + "." + new1[16] + "." + new1[17] + "." + new1[18] + "." + \
                        new1[19] + "." + new1[20]

                    temp_ipv6_mask = args["dest"].split("/")
                    ipv6addr = StringUtils().ipv6_to_dec(temp_ipv6_mask[0])
                    ipv6mask = temp_ipv6_mask[1]
                    expected_dest = ipv6addr + "." + ipv6mask

                found_bvlan = new1[-2]
                found_nh_bmac = \
                    new1[-9] + "." + new1[-8] + "." + new1[-7] + "." + new1[-6] + "." + new1[-5] + "." + new1[-4]
                found_nh_bmac = StringUtils().dec_to_mac(found_nh_bmac)

                if found_dest == expected_dest and found_nh_bmac == args["nh_bmac"] and found_nh_bmac == \
                        args["nh_bmac"] and found_bvlan == args["bvlan"]:
                    return True, {"ret_dest": found_dest,
                                  "ret_nh_bmac": found_nh_bmac,
                                  "ret_bvlan": found_bvlan}

        return False, None

    def check_isis_spbm_ip_unicast_fib_out_port(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                new1 = line.replace("SNMPv2-SMI::enterprises.2272.1.63.21.1.", "").replace(" ", "").\
                    replace("=", ".").split(".")
                if new1[3] == "4":
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "/" + new1[8]
                    expected_dest = args["dest"]
                else:
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "." + new1[8] + "." + \
                        new1[9] + "." + new1[10] + "." + new1[11] + "." + new1[12] + "." + new1[13] + "." + \
                        new1[14] + "." + new1[15] + "." + new1[16] + "." + new1[17] + "." + new1[18] + "." + \
                        new1[19] + "." + new1[20]

                    temp_ipv6_mask = args["dest"].split("/")
                    ipv6addr = StringUtils().ipv6_to_dec(temp_ipv6_mask[0])
                    ipv6mask = temp_ipv6_mask[1]
                    expected_dest = ipv6addr + "." + ipv6mask

                found_nh_beb = new1[-1]
                found_bvlan = new1[-2]
                if found_dest == expected_dest and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"]:
                    g = line.replace(" ", "").split("=")[0]
                    nl = list(g)
                    nl[39] = '10'
                    item = ''.join(nl)
                    parse_result = self.pw.get_value_by_offset(output, item, 2)

                    result = True if parse_result == args["port_if_index"] else False
                    return result, {"ret_port": parse_result}

        return False, None

    def check_isis_spbm_ip_unicast_fib_out_logical_interface(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                new1 = line.replace("SNMPv2-SMI::enterprises.2272.1.63.21.1.", "").replace(" ", "").\
                    replace("=", ".").split(".")
                if new1[3] == "4":
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "/" + new1[8]
                    expected_dest = args["dest"]
                else:
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "." + new1[8] + "." + \
                        new1[9] + "." + new1[10] + "." + new1[11] + "." + new1[12] + "." + new1[13] + "." + \
                        new1[14] + "." + new1[15] + "." + new1[16] + "." + new1[17] + "." + new1[18] + "." + \
                        new1[19] + "." + new1[20]

                    temp_ipv6_mask = args["dest"].split("/")
                    ipv6addr = StringUtils().ipv6_to_dec(temp_ipv6_mask[0])
                    ipv6mask = temp_ipv6_mask[1]
                    expected_dest = ipv6addr + "." + ipv6mask

                found_nh_beb = new1[-1]
                found_bvlan = new1[-2]
                if found_dest == expected_dest and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"]:
                    g = line.replace(" ", "").split("=")[0]
                    nl = list(g)
                    nl[39] = '10'
                    item = ''.join(nl)
                    parse_result = self.pw.get_value_by_offset(output, item, 2)

                    result = True if parse_result == args["logical_if_index"] else False
                    return result, {"ret_logical_intf": parse_result}

        return False, None

    def check_isis_spbm_ip_unicast_fib_vrf_isid(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                new1 = line.replace("SNMPv2-SMI::enterprises.2272.1.63.21.1.", "").replace(" ", "").\
                    replace("=", ".").split(".")
                if new1[3] == "4":
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "/" + new1[8]
                    expected_dest = args["dest"]
                else:
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "." + new1[8] + "." + \
                        new1[9] + "." + new1[10] + "." + new1[11] + "." + new1[12] + "." + new1[13] + "." + \
                        new1[14] + "." + new1[15] + "." + new1[16] + "." + new1[17] + "." + new1[18] + "." + \
                        new1[19] + "." + new1[20]

                    temp_ipv6_mask = args["dest"].split("/")
                    ipv6addr = StringUtils().ipv6_to_dec(temp_ipv6_mask[0])
                    ipv6mask = temp_ipv6_mask[1]
                    expected_dest = ipv6addr + "." + ipv6mask

                found_nh_beb = new1[-1]
                found_bvlan = new1[-2]
                if found_dest == expected_dest and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"]:
                    g = line.replace(" ", "").split("=")[0]
                    nl = list(g)
                    nl[39] = '8'
                    item = ''.join(nl)
                    parse_result = self.pw.get_value_by_offset(output, item, 2)

                    result = True if parse_result == args["vrf_isid"] else False
                    return result, {"ret_isid": parse_result}

        return False, None

    def check_isis_spbm_ip_unicast_fib_prefix_type_internal(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                new1 = line.replace("SNMPv2-SMI::enterprises.2272.1.63.21.1.", "").replace(" ", "").\
                    replace("=", ".").split(".")
                if new1[3] == "4":
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "/" + new1[8]
                    expected_dest = args["dest"]
                else:
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "." + new1[8] + "." + \
                        new1[9] + "." + new1[10] + "." + new1[11] + "." + new1[12] + "." + new1[13] + "." + \
                        new1[14] + "." + new1[15] + "." + new1[16] + "." + new1[17] + "." + new1[18] + "." + \
                        new1[19] + "." + new1[20]

                    temp_ipv6_mask = args["dest"].split("/")
                    ipv6addr = StringUtils().ipv6_to_dec(temp_ipv6_mask[0])
                    ipv6mask = temp_ipv6_mask[1]
                    expected_dest = ipv6addr + "." + ipv6mask

                found_nh_beb = new1[-1]
                found_bvlan = new1[-2]
                if found_dest == expected_dest and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"]:
                    g = line.replace(" ", "").split("=")[0]
                    nl = list(g)
                    nl[39] = '14'
                    item = ''.join(nl)
                    parse_result = self.pw.get_value_by_offset(output, item, 2)

                    result = True if parse_result == "1" else False
                    return result, {"ret_type": parse_result}

        return False, None

    def check_isis_spbm_ip_unicast_fib_prefix_type_external(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                new1 = line.replace("SNMPv2-SMI::enterprises.2272.1.63.21.1.", "").replace(" ", "").\
                    replace("=", ".").split(".")
                if new1[3] == "4":
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "/" + new1[8]
                    expected_dest = args["dest"]
                else:
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "." + new1[8] + "." + \
                        new1[9] + "." + new1[10] + "." + new1[11] + "." + new1[12] + "." + new1[13] + "." + \
                        new1[14] + "." + new1[15] + "." + new1[16] + "." + new1[17] + "." + new1[18] + "." + \
                        new1[19] + "." + new1[20]

                    temp_ipv6_mask = args["dest"].split("/")
                    ipv6addr = StringUtils().ipv6_to_dec(temp_ipv6_mask[0])
                    ipv6mask = temp_ipv6_mask[1]
                    expected_dest = ipv6addr + "." + ipv6mask

                found_nh_beb = new1[-1]
                found_bvlan = new1[-2]
                if found_dest == expected_dest and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"]:
                    g = line.replace(" ", "").split("=")[0]
                    nl = list(g)
                    nl[39] = '14'
                    item = ''.join(nl)
                    parse_result = self.pw.get_value_by_offset(output, item, 2)

                    result = True if parse_result == "2" else False
                    return result, {"ret_type": parse_result}

        return False, None

    def check_isis_spbm_ip_unicast_fib_dest_network(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                new1 = line.replace("SNMPv2-SMI::enterprises.2272.1.63.21.1.", "").replace(" ", "").\
                    replace("=", ".").split(".")
                if new1[3] == "4":
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "/" + new1[8]
                    expected_dest = args["dest"]
                else:
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "." + new1[8] + "." + \
                        new1[9] + "." + new1[10] + "." + new1[11] + "." + new1[12] + "." + new1[13] + "." + \
                        new1[14] + "." + new1[15] + "." + new1[16] + "." + new1[17] + "." + new1[18] + "." + \
                        new1[19] + "." + new1[20]

                    temp_ipv6_mask = args["dest"].split("/")
                    ipv6addr = StringUtils().ipv6_to_dec(temp_ipv6_mask[0])
                    ipv6mask = temp_ipv6_mask[1]
                    expected_dest = ipv6addr + "." + ipv6mask

                found_nh_beb = new1[-1]
                found_bvlan = new1[-2]

                if found_dest == expected_dest and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"]:
                    return True, {"ret_dest": found_dest,
                                  "ret_nh_beb": found_nh_beb,
                                  "ret_bvlan": found_bvlan}

        return False, None

    def check_isis_spbm_ip_unicast_fib_bvlan(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                new1 = line.replace("SNMPv2-SMI::enterprises.2272.1.63.21.1.", "").replace(" ", "").\
                    replace("=", ".").split(".")
                if new1[3] == "4":
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "/" + new1[8]
                    expected_dest = args["dest"]
                else:
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "." + new1[8] + "." + \
                        new1[9] + "." + new1[10] + "." + new1[11] + "." + new1[12] + "." + new1[13] + "." + \
                        new1[14] + "." + new1[15] + "." + new1[16] + "." + new1[17] + "." + new1[18] + "." + \
                        new1[19] + "." + new1[20]

                    temp_ipv6_mask = args["dest"].split("/")
                    ipv6addr = StringUtils().ipv6_to_dec(temp_ipv6_mask[0])
                    ipv6mask = temp_ipv6_mask[1]
                    expected_dest = ipv6addr + "." + ipv6mask

                found_nh_beb = new1[-1]
                found_bvlan = new1[-2]

                if found_dest == expected_dest and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"]:
                    return True, {"ret_dest": found_dest,
                                  "ret_nh_beb": found_nh_beb,
                                  "ret_bvlan": found_bvlan}

        return False, None

    def check_isis_spbm_ip_unicast_fib_prefix_type(self, output, args, **kwargs):
        for line in output.splitlines():
            if len(line) > 1:
                new1 = line.replace("SNMPv2-SMI::enterprises.2272.1.63.21.1.", "").replace(" ", "").\
                    replace("=", ".").split(".")
                if new1[3] == "4":
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "/" + new1[8]
                    expected_dest = args["dest"]
                else:
                    found_dest = new1[4] + "." + new1[5] + "." + new1[6] + "." + new1[7] + "." + new1[8] + "." + \
                        new1[9] + "." + new1[10] + "." + new1[11] + "." + new1[12] + "." + new1[13] + "." + \
                        new1[14] + "." + new1[15] + "." + new1[16] + "." + new1[17] + "." + new1[18] + "." + \
                        new1[19] + "." + new1[20]

                    temp_ipv6_mask = args["dest"].split("/")
                    ipv6addr = StringUtils().ipv6_to_dec(temp_ipv6_mask[0])
                    ipv6mask = temp_ipv6_mask[1]
                    expected_dest = ipv6addr + "." + ipv6mask

                found_nh_beb = new1[-1]
                found_bvlan = new1[-2]
                if found_dest == expected_dest and found_nh_beb == args["nh_beb"] and found_bvlan == args["bvlan"]:
                    g = line.replace(" ", "").split("=")[0]
                    nl = list(g)
                    nl[39] = '14'
                    item = ''.join(nl)
                    parse_result = self.pw.get_value_by_offset(output, item, 2)

                    p_type = args["prefix_type"].lower()
                    if p_type == "internal":
                        p = "1"
                    elif p_type == "external":
                        p = "2"
                    else:
                        return False, {"ret_type": parse_result}

                    result = True if parse_result == p else False
                    return result, {"ret_type": parse_result}

        return False, None
