from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.policy.base.PolicyBaseCustomShowTools import \
    PolicyBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.Lists.IntList import IntList
from ExtremeAutomation.Library.Utils.Parsing.PolicyRule import PolicyRule
from ExtremeAutomation.Library.Utils.Parsing.PolicyProfile import PolicyProfile
from ExtremeAutomation.Library.Utils.Parsing.PolicyAdminProfile import PolicyAdminProfile
from ExtremeAutomation.Library.Utils.NumberUtils import NumberUtils


class PolicyCustomShowTools(PolicyBaseCustomShowTools):
    def __init__(self, device):
        super(PolicyCustomShowTools, self).__init__(device)

    # ##################################################################################################################
    #   Current Parser Functions   #####################################################################################
    # ##################################################################################################################
    def check_policy_state(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), 'policy is currently', 3)

        result = True if parse_result == "enabled" else False
        return result, {"ret_state": parse_result}

    def check_policy_profile_exists(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        profile_ids = []
        for profile in policy_profiles:
            if profile.profile_id == args["profile_id"]:
                profile_ids.append(profile.profile_id)
                result = True
                break
        return result, {"ret_profile_id": str(profile_ids)}

    def check_policy_profile_name(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        profile_name = None
        for profile in policy_profiles:
            if profile.profile_id == args["profile_id"]:
                profile_name = profile.profile_name
                result = profile.profile_name == args["profile_name"]
                break
        return result, {"ret_profile_name": profile_name}

    def check_policy_profile_pvid_status(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        pvid_status = None
        for profile in policy_profiles:
            if profile.profile_id == args["profile_id"]:
                pvid_status = profile.port_vid_status
                result = profile.port_vid_status == "enabled"
                break
        return result, {"ret_pvid_status": pvid_status}

    def check_policy_profile_pvid(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        pvid = None
        for profile in policy_profiles:
            if profile.profile_id == args["profile_id"]:
                pvid = profile.port_vid_override
                result = profile.port_vid_override == args["pvid"]
                break
        return result, {"ret_pvid": pvid}

    def check_policy_profile_cos_status(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        cos_status = None
        for profile in policy_profiles:
            if profile.profile_id == args["profile_id"]:
                cos_status = profile.cos_status
                result = profile.cos_status.lower() == "enabled"
                break
        return result, {"ret_cos_status": cos_status}

    def check_policy_profile_cos(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        cos = None
        for profile in policy_profiles:
            if profile.profile_id == args["profile_id"]:
                cos = profile.cos
                result = profile.cos == args["cos_value"]
                break
        return result, {"ret_cos": cos}

    def check_policy_profile_egress_vlan(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        vlan = None
        for profile in policy_profiles:
            if profile.profile_id == args["profile_id"]:
                vlan = profile.tagged_egress
                result = args["vlan"] in profile.tagged_egress
                break
        return result, {"ret_egress_vlan": vlan}

    def check_policy_profile_untagged_vlan(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        vlan = None
        for profile in policy_profiles:
            if profile.profile_id == args["profile_id"]:
                vlan = profile.untagged_egress
                result = args["vlan"] in profile.untagged_egress
                break
        return result, {"ret_untagged_vlan": vlan}

    def check_policy_profile_forbidden_vlan(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        vlan = None
        for profile in policy_profiles:
            if profile.profile_id == args["profile_id"]:
                vlan = profile.forbidden_egress
                result = args["vlan"] in profile.forbidden_egress
                break
        return result, {"ret_forbidden_vlan": vlan}

    def check_policy_profile_tci_overwrite(self, output, args, **kwargs):
        profile_list = self.__create_policy_profile_list(output)

        result = False
        tci = None
        for profile in profile_list:
            if profile.profile_id == args["profile_id"]:
                tci = profile.replace_tci_status
                result = profile.replace_tci_status.lower() == "enabled"
                break
        return result, {"ret_tci_overwrite": tci}

    def check_policy_profile_precedence(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)
        result = False
        precedence = None
        try:
            normalized_precedence_string = IntList(args["precedence_string"]).get_all()

            for profile in policy_profiles:
                if profile.profile_id == args["profile_id"]:
                    precedence = IntList(profile.rule_precedence).get_all()
                    result = precedence == normalized_precedence_string
                    break
        except ValueError:
            pass
        return result, {"ret_rule_precedence": str(precedence)}

    def check_policy_rule_ether(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False
        expected_type = args["ether_type"]
        if expected_type.startswith("0x"):
            expected_type = str(StringUtils.hex_str_to_int(expected_type))

        result = False
        found_rule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ether ii packet type":
                if rule.rule_data.lower() == expected_type.lower():
                    rule_data_verified = True
                    found_rule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No ether rule with data " + args["ether_type"] + " found.")

        return result, found_rule

    def check_policy_rule_ip6dest(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        ipv6_addr = StringUtils.collapse_ipv6_address(args["ipv6_addr"])
        rule_data = ipv6_addr if args["l4_port"] is None else ipv6_addr + "-" + args["l4_port"]
        rule_data_verified = False

        result = False
        found_rule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ipv6 destination address":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_rule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IPv6 destination rule with data " + rule_data + " found.")

        return result, found_rule

    def check_policy_rule_ipdestsocket(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        rule_data = args["ip_addr"] if args["l4_port"] is None else args["ip_addr"] + ":" + args["l4_port"]

        result = False
        found_rule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ip destination address":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_rule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IP destination socket rule with data " + rule_data + " found.")

        return result, found_rule

    def check_policy_rule_ipfrag(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)

        result = False
        found_rule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ip fragmentation":
                found_rule = rule.rule_data_dict()
                if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                   args["vlan"], args["cos"]):
                    result = True
                    break
        return result, found_rule

    def check_policy_rule_ipproto(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_rule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ip proto":
                if rule.rule_data.split()[0] == args["ip_proto"]:
                    rule_data_verified = True
                    found_rule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IP proto rule with data " + args["ip_proto"] + " found.")

        return result, found_rule

    def check_policy_rule_ipsourcesocket(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        rule_data = args["ip_addr"] if args["l4_port"] is None else args["ip_addr"] + ":" + args["l4_port"]

        result = False
        found_rule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ip source address":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_rule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IP source socket rule with data " + rule_data + " found.")

        return result, found_rule

    def check_policy_rule_iptos(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_rule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ip type of service":
                if rule.rule_data.split()[0] == args["ip_tos"]:
                    rule_data_verified = True
                    found_rule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IP TOS rule with data " + args["ip_tos"] + " found.")

        return result, found_rule

    def check_policy_rule_ipttl(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_rule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ttl":
                if rule.rule_data.split()[0] == args["ip_ttl"]:
                    rule_data_verified = True
                    found_rule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IP TTL rule with data " + args["ip_ttl"] + " found.")

        return result, found_rule

    def check_policy_rule_macdest(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        rule_data = StringUtils.normalize_mac(args["mac_addr"], "-")

        result = False
        found_rule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "mac destination address":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_rule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No MAC destination rule with data " + rule_data + " found.")

        return result, found_rule

    def check_policy_rule_macsource(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        rule_data = StringUtils.normalize_mac(args["mac_addr"], "-")

        result = False
        found_rule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "mac source address":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_rule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No MAC source rule with data " + rule_data + " found.")

        return result, found_rule

    def check_policy_rule_port(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        rule_data = args["port"]

        result = False
        found_rule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "port string":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_rule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No Port rule for port " + rule_data + " found.")

        return result, found_rule

    def check_policy_rule_tcpdestportip(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        ip_addr = args["ip_addr"]
        tcp_port = args["tcp_port"]
        if ip_addr is None:
            rule_data = tcp_port
        elif ":" in ip_addr:
            rule_data = tcp_port + "-" + ip_addr
        else:
            rule_data = tcp_port + ":" + ip_addr

        result = False
        found_rule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "tcp port destination":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_rule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No TCP destination port IP rule with data " + rule_data + " found.")

        return result, found_rule

    def check_policy_rule_tcpsourceportip(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        ip_addr = args["ip_addr"]
        tcp_port = args["tcp_port"]
        if ip_addr is None:
            rule_data = tcp_port
        elif ":" in ip_addr:
            rule_data = tcp_port + "-" + ip_addr
        else:
            rule_data = tcp_port + ":" + ip_addr

        result = False
        found_rule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "tcp port source":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_rule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No TCP source port IP rule with data " + rule_data + " found.")

        return result, found_rule

    def check_policy_rule_udpdestportip(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        ip_addr = args["ip_addr"]
        udp_port = args["udp_port"]
        if ip_addr is None:
            rule_data = udp_port
        elif ":" in ip_addr:
            rule_data = udp_port + "-" + ip_addr
        else:
            rule_data = udp_port + ":" + ip_addr

        result = False
        found_rule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "udp port destination":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_rule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No UDP destination port IP rule with data " + rule_data + " found.")

        return result, found_rule

    def check_policy_rule_udpsourceportip(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        ip_addr = args["ip_addr"]
        udp_port = args["udp_port"]
        if ip_addr is None:
            rule_data = udp_port
        elif ":" in ip_addr:
            rule_data = udp_port + "-" + ip_addr
        else:
            rule_data = udp_port + ":" + ip_addr

        result = False
        found_rule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "udp port source":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_rule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No UDP source port rule with data " + rule_data + " found.")

        return result, found_rule

    def check_policy_allowed_types(self, output, args, **kwargs):
        output_type_list = list()
        vnp = self.constants.VALUE_NOT_PRESENT

        for i in range(1, 32):
            if i < 10:
                result = True if self.pw.get_value_by_offset(output, "(0" + str(i) + ")", 0) != vnp else False
                output_type_list.append(result)
            elif i != 24 and i != 30:
                result = True if self.pw.get_value_by_offset(output, "(" + str(i) + ")", 0) != vnp else False
                output_type_list.append(result)

        result = True
        all_type_list = eval(args["all_types"])
        if len(all_type_list) == len(output_type_list):
            for i in range(len(all_type_list)):
                if all_type_list[i] != output_type_list[i]:
                    result = False
        else:
            self.logger.log_error("Lists were not the same length, check parser.")
            result = False

        return result, {"ret_allowed_types": str(output_type_list)}

    def check_policy_map_response(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), 'policy map response', 4)

        result = True if parse_result == args["attribute"] else False
        return result, {"ret_map_response": parse_result}

    def check_policy_invalid_action(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), args["action"], 0)

        result = True if parse_result == "current" else False
        return result, {"ret_action": parse_result}

    def check_policy_global_vlan_authorization_state(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), 'vlan authorization global status', 4)

        result = True if parse_result == args["state"] else False
        return result, {"ret_vlan_auth_state": parse_result}

    def check_policy_invalid_count(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output.lower(), "profiles detected", 5)

        result = True if parse_result == args["count"] else False
        return result, {"ret_invalid_count": parse_result}

    def store_policy_invalid_counter(self, output, args, **kwargs):
        """
        The following function returns True when the PI count is stored.
        """
        pi_count = self.pw.get_value_by_offset(output.lower(), "profiles detected", 5)

        self.value_storage.add_value(self.device.name, "pi_count", pi_count)
        self.logger.log_debug("Policy Invalid counter: " + pi_count)

        result = True if pi_count != self.constants.VALUE_NOT_PRESENT else False
        return result, {"ret_invalid_counter": pi_count}

    def verify_policy_invalid_count_incremented(self, output, args, **kwargs):
        """
        The following function returns True if the PI count incremented accordingly.
        """
        pi_count_new = self.pw.get_value_by_offset(output.lower(), "profiles detected", 5)
        pi_count_old = self.value_storage.get_value(self.device.name, "pi_count")
        self.logger.log_debug("Policy Invalid counter: " + pi_count_new)

        result = False
        if pi_count_new.isdigit() and pi_count_old.isdigit():
            incr_offset = int(pi_count_new) - int(pi_count_old)
            if args["increment"].isdigit():
                if int(incr_offset) == int(args["increment"]):
                    result = True

        return result, {"ret_invalid_count_old": pi_count_old,
                        "ret_invalid_count_new": pi_count_new}

    def check_port_admin_profile(self, output, args, **kwargs):
        admin_profiles = self.__create_policy_admin_profile_list(output)

        result = False
        found_rule = None
        for admin_profile in admin_profiles:
            if admin_profile.rule_type.lower() == "port string":
                if admin_profile.rule_data == args["port"]:
                    found_rule = admin_profile.rule_data_dict()
                    result = admin_profile.port == args["port"]
                    break
        return result, found_rule

    def check_mac_source_admin_profile(self, output, args, **kwargs):
        admin_profiles = self.__create_policy_admin_profile_list(output)

        result = False
        found_rule = None
        for admin_profile in admin_profiles:
            if admin_profile.rule_type.lower() == "mac source address":
                found_rule = admin_profile.rule_data_dict()
                if admin_profile.rule_data == StringUtils.normalize_mac(args["mac_addr"], "-"):
                    result = admin_profile.port == args["port"]
                    break
        return result, found_rule

    def check_policy_rule_model_access_list(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "Rule-model", 2)

        result = True if parse_result == "access-list" else False
        return result, {"ret_rule_model": parse_result}

    def check_policy_rule_model_hierarchical(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "Rule-model", 2)

        result = True if parse_result == "hierarchical" else False
        return result, {"ret_rule_model": parse_result}

    def check_policy_acl_ether(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "Ether" in line:
                resulting_line = line

        parse_result = self.pw.get_value_by_offset(resulting_line, "Ether", 2).lstrip("(").rstrip(")")
        mask = self.pw.get_value_by_offset(resulting_line, "Ether", 4).split("|")[0]
        if "x" not in args["ether"]:
            try:
                args["ether"] = NumberUtils.to_hex_value(args["ether"], False)
            except ValueError:
                self.logger.log_error("'ether' argument could not be converted to hex!")
                pass
        if args["mask"]:
            result = parse_result == args["ether"] and mask == args["mask"]
        else:
            result = parse_result == args["ether"]
        return result, {"ret_rule_data": parse_result,
                        "ret_mask": mask}

    def check_policy_acl_icmp6type(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "ICMP6Type" in line:
                resulting_line = line

        parse_result = self.pw.get_value_by_offset(resulting_line, "ICMP6Type", 1)
        if len(parse_result.split("|")) > 1:
            parse_result = parse_result.split("|")[1]
        mask = self.pw.get_value_by_offset(resulting_line, "ICMP6Type", 3).split("|")[0]
        if args["mask"]:
            result = parse_result == args["icmp6type"] and mask == args["mask"]
        else:
            result = parse_result == args["icmp6type"]
        return result, {"ret_rule_data": parse_result,
                        "ret_mask": mask}

    def check_policy_acl_icmptype(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "ICMPType" in line:
                resulting_line = line
        parse_result = self.pw.get_value_by_offset(resulting_line, "ICMPType", 1)
        mask = self.pw.get_value_by_offset(resulting_line, "ICMPType", 3)
        try:
            parse_result = parse_result.split("|")[1]
            mask = mask.split("|")[0]
        except IndexError:
            pass
        if args["mask"]:
            result = parse_result == args["icmptype"] and mask == args["mask"]
        else:
            result = parse_result == args["icmptype"]
        return result, {"ret_rule_data": parse_result,
                        "ret_mask": mask}

    def check_policy_acl_ipdestsocket(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "IPDest" in line:
                resulting_line = line

        parse_result = self.pw.get_value_by_offset(resulting_line, "IPDest", 1)
        if len(parse_result.split("|")) > 1:
            parse_result = parse_result.split("|")[1]
        mask = self.pw.get_value_by_offset(resulting_line, "IPDest", 3).split("|")[0]
        if args["mask"]:
            result = parse_result == args["ipdestsocket"] and mask == args["mask"]
        else:
            result = parse_result == args["ipdestsocket"]
        return result, {"ret_rule_data": parse_result,
                        "ret_mask": mask}

    def check_policy_acl_ipfrag(self, output, args, **kwargs):
        lines = str.splitlines(output, False)

        result = False
        for line in lines:
            if "IPFrag" in line:
                result = True
        return result, result

    def check_policy_acl_ipproto(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "IPProto" in line:
                resulting_line = line

        parse_result = self.pw.get_value_by_offset(resulting_line, "IPProto", 2).lstrip("(").rstrip(")")
        mask = self.pw.get_value_by_offset(resulting_line, "IPProto", 4).split("|")[0]
        if "x" not in args["ipproto"]:
            args["ipproto"] = NumberUtils.to_hex_value(args["ipproto"], False)
        if args["mask"]:
            result = parse_result == args["ipproto"] and mask == args["mask"]
        else:
            result = parse_result == args["ipproto"]
        return result, {"ret_rule_data": parse_result,
                        "ret_mask": mask}

    def check_policy_acl_ipsourcesocket(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "IPSource" in line:
                resulting_line = line
        parse_result = self.pw.get_value_by_offset(resulting_line, "IPSource", 1)
        mask = self.pw.get_value_by_offset(resulting_line, "IPSource", 3)
        try:
            parse_result = parse_result.split("|")[1]
            mask = mask.split("|")[0]
        except IndexError:
            pass
        if args["mask"]:
            result = parse_result == args["ipsourcesocket"] and mask == args["mask"]
        else:
            result = parse_result == args["ipsourcesocket"]
        return result, {"ret_rule_data": parse_result,
                        "ret_mask": mask}

    def check_policy_acl_iptos(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "IPTOS" in line:
                resulting_line = line

        parse_result = self.pw.get_value_by_offset(resulting_line, "IPTOS", 2).lstrip("(").rstrip(")")
        mask = self.pw.get_value_by_offset(resulting_line, "IPTOS", 4).split("|")[0]
        if "x" not in args["iptos"]:
            args["iptos"] = NumberUtils.to_hex_value(args["iptos"], False)
        if args["mask"]:
            result = parse_result == args["iptos"] and mask == args["mask"]
        else:
            result = parse_result == args["iptos"]
        return result, {"ret_rule_data": parse_result,
                        "ret_mask": mask}

    def check_policy_acl_ipttl(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "TTL" in line:
                resulting_line = line

        parse_result = self.pw.get_value_by_offset(resulting_line, "TTL", 2).lstrip("(").rstrip(")")
        mask = self.pw.get_value_by_offset(resulting_line, "TTL", 4).split("|")[0]
        if "x" not in args["ttl"]:
            args["ttl"] = NumberUtils.to_hex_value(args["ttl"], False)
        if args["mask"]:
            result = parse_result == args["ttl"] and mask == args["mask"]
        else:
            result = parse_result == args["ttl"]
        return result, {"ret_rule_data": parse_result,
                        "ret_mask": mask}

    def check_policy_acl_tcpdestportip(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "TCPDestPort" in line:
                resulting_line = line
        parse_result = self.pw.get_value_by_offset(resulting_line, "TCPDestPort", 1)
        mask = self.pw.get_value_by_offset(resulting_line, "TCPDestPort", 3)
        try:
            parse_result = parse_result.split("|")[1]
            mask = mask.split("|")[0]
        except IndexError:
            pass
        if args["mask"]:
            result = parse_result == args["tcpdestportip"] and mask == args["mask"]

        else:
            result = parse_result == args["tcpdestportip"]
        return result, {"ret_rule_data": parse_result,
                        "ret_mask": mask}

    def check_policy_acl_tcpsourceportip(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "TCPSrcPort" in line:
                resulting_line = line

        parse_result = self.pw.get_value_by_offset(resulting_line, "TCPSrcPort", 1)
        if len(parse_result.split("|")) > 1:
            parse_result = parse_result.split("|")[1]
        mask = self.pw.get_value_by_offset(resulting_line, "TCPSrcPort", 3).split("|")[0]
        if args["mask"]:
            result = parse_result == args["tcpsourceportip"] and mask == args["mask"]
        else:
            result = parse_result == args["tcpsourceportip"]
        return result, {"ret_rule_data": parse_result,
                        "ret_mask": mask}

    def check_policy_acl_udpdestportip(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "UDPDestPort" in line:
                resulting_line = line
        parse_result = self.pw.get_value_by_offset(resulting_line, "UDPDestPort", 1)
        mask = self.pw.get_value_by_offset(resulting_line, "UDPDestPort", 3)
        try:
            parse_result = parse_result.split("|")[1]
            mask = mask.split("|")[0]
        except IndexError:
            pass
        if args["mask"]:
            result = parse_result == args["udpdestportip"] and mask == args["mask"]
        else:
            result = parse_result == args["udpdestportip"]
        return result, {"ret_rule_data": parse_result,
                        "ret_mask": mask}

    def check_policy_acl_udpsourceportip(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "UDPSrcPort" in line:
                resulting_line = line

        parse_result = self.pw.get_value_by_offset(resulting_line, "UDPSrcPort", 1)
        if len(parse_result.split("|")) > 1:
            parse_result = parse_result.split("|")[1]
        mask = self.pw.get_value_by_offset(resulting_line, "UDPSrcPort", 3).split("|")[0]
        if args["mask"]:
            result = parse_result == args["udpsourceportip"] and mask == args["mask"]
        else:
            result = parse_result == args["udpsourceportip"]
        return result, {"ret_rule_data": parse_result,
                        "ret_mask": mask}

    def check_policy_acl_action_cos(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if line.count("|") == 9:
                resulting_line = line
        try:
            parse_result = resulting_line.split("|")[7].strip()
        except IndexError:
            parse_result = resulting_line
        result = True if parse_result == args["cos"] else False
        return result, {"ret_cos": parse_result}

    def check_policy_acl_action_mirror(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        parse_result = ""
        for line in lines:
            if line.count("|") == 9:
                parse_result = line
        if len(parse_result.split("|")) > 8:
            parse_result = parse_result.split("|")[8].strip()
        result = True if parse_result == args["mirror_index"] else False
        return result, {"ret_mirror": parse_result}

    def check_policy_acl_action_drop(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if line.count("|") == 9:
                resulting_line = line
        try:
            parse_result = resulting_line.split("|")[6]
        except IndexError:
            parse_result = resulting_line
        result = True if parse_result == "drop" else False
        return result, {"ret_action": parse_result}

    def check_policy_acl_action_forward(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        parse_result = ""
        for line in lines:
            if line.count("|") == 9:
                parse_result = line
        if len(parse_result.split("|")) > 6:
            parse_result = parse_result.split("|")[6]
        result = True if parse_result == "fwrd" else False
        return result, {"ret_action": parse_result}

    def check_policy_acl_action_trap_enabled(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if line.count("|") == 9:
                resulting_line = line
        try:
            parse_result = resulting_line.split("|")[5]
        except IndexError:
            parse_result = resulting_line
        result = True if "T" in parse_result else False
        return result, {"ret_trap_state": parse_result}

    def check_policy_acl_action_syslog_enabled(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        parse_result = ""
        for line in lines:
            if line.count("|") == 9:
                parse_result = line
        if len(parse_result.split("|")) > 5:
            parse_result = parse_result.split("|")[5]
        result = True if "S" in parse_result else False
        return result, {"ret_syslog_state": parse_result}

    def check_policy_acl_action_all(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        st = None
        ts = None
        vlan = None
        cos = None
        mir = None
        try:
            for line in lines:
                if line.count("|") == 9:
                    resulting_line = line
            st = resulting_line.split("|")[4].strip()
            ts = resulting_line.split("|")[5].strip()
            vlan = resulting_line.split("|")[6].strip()
            cos = resulting_line.split("|")[7].strip()
            mir = resulting_line.split("|")[8].strip()

            result = True
            if args["st"] is not None:
                if args["st"].lower() != st.lower():
                    result = False
            if args["ts"] is not None:
                if args["ts"].lower() != ts.lower():
                    result = False
            if args["vlan"] is not None:
                if args["vlan"].lower() != vlan.lower():
                    result = False
            if args["cos"] is not None:
                if args["cos"] != cos:
                    result = False
            if args["mir"] is not None:
                if args["mir"] != mir:
                    result = False
        except IndexError:
            result = False
        return result, {"ret_syslog": st,
                        "ret_trap": ts,
                        "ret_vlan": vlan,
                        "ret_cos": cos,
                        "ret_mirror": mir}

    def check_policy_acl_does_not_exist(self, output, args, **kwargs):
        if args["list_name"] in output:
            return False, False
        else:
            return True, True

    def check_policy_acl_action_set_cos(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        parse_result = ""
        for line in lines:
            if "| action set" in line:
                parse_result = line
        if len(parse_result.split("|")) > 8:
            parse_result = parse_result.split("|")[8].strip()
        result = True if parse_result == args["cos"] else False
        return result, {"ret_cos": parse_result}

    def check_policy_acl_action_set_mirror(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "| action set" in line:
                resulting_line = line
        try:
            parse_result = resulting_line.split("|")[9].strip()
        except IndexError:
            parse_result = resulting_line
        result = True if parse_result == args["mirror_index"] else False
        return result, {"ret_mirror": parse_result}

    def check_policy_acl_action_set_drop(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        parse_result = ""
        for line in lines:
            if "| action set" in line:
                parse_result = line
        if len(parse_result.split("|")) > 7:
            parse_result = parse_result.split("|")[7]
        result = True if parse_result == "drop" else False
        return result, {"ret_action": parse_result}

    def check_policy_acl_action_set_forward(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "| action set" in line:
                resulting_line = line
        try:
            parse_result = resulting_line.split("|")[7]
        except IndexError:
            parse_result = resulting_line
        result = True if parse_result == "fwrd" else False
        return result, {"ret_action": parse_result}

    def check_policy_acl_action_set_trap_enabled(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        parse_result = ""
        for line in lines:
            if "| action set" in line:
                parse_result = line
        if len(parse_result.split("|")) > 6:
            parse_result = parse_result.split("|")[6]
        result = True if "T" in parse_result else False
        return result, {"ret_trap_state": parse_result}

    def check_policy_acl_action_set_syslog_enabled(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "| action set" in line:
                resulting_line = line
        try:
            parse_result = resulting_line.split("|")[6]
        except IndexError:
            parse_result = resulting_line
        result = True if "S" in parse_result else False
        return result, {"ret_syslog_state": parse_result}

    def check_policy_acl_action_set_all(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        for line in lines:
            if "| action set" in line:
                resulting_line = line
        if len(resulting_line.split("|")) > 9:
            st = resulting_line.split("|")[5].strip()
            ts = resulting_line.split("|")[6].strip()
            vlan = resulting_line.split("|")[7].strip()
            cos = resulting_line.split("|")[8].strip()
            mir = resulting_line.split("|")[9].strip()
        else:
            st = self.constants.VALUE_NOT_PRESENT
            ts = self.constants.VALUE_NOT_PRESENT
            vlan = self.constants.VALUE_NOT_PRESENT
            cos = self.constants.VALUE_NOT_PRESENT
            mir = self.constants.VALUE_NOT_PRESENT

        result = True
        if args["st"] is not None:
            if args["st"].lower() != st.lower():
                result = False
        if args["ts"] is not None:
            if args["ts"].lower() != ts.lower():
                result = False
        if args["vlan"] is not None:
            if args["vlan"].lower() != vlan.lower():
                result = False
        if args["cos"] is not None:
            if args["cos"] != cos:
                result = False
        if args["mir"] is not None:
            if args["mir"] != mir:
                result = False
        return result, {"ret_syslog": st,
                        "ret_trap": ts,
                        "ret_vlan": vlan,
                        "ret_cos": cos,
                        "ret_mirror": mir}

    def check_policy_acl_action_set_does_not_exist(self, output, args, **kwargs):
        return True, True

    def check_policy_acl_profile_index(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, 'Access List Name', 3)
        parse_result = parse_result.lstrip(":")
        result = True if parse_result == args["list_name"] else False
        return result, {"ret_profile_index": parse_result}

    def check_policy_acl_profile_index_none(self, output, args, **kwargs):
        lines = str.splitlines(output, False)
        resulting_line = ""
        combostr = "|" + args["list_name"]
        for line in lines:
            if combostr in line:
                resulting_line = line
                break
        parse_result = resulting_line.split("|")[0].strip()
        result = True if parse_result == "" else False
        return result, {"ret_profile_index": parse_result}

    def check_policy_acl_rule_does_not_exist(self, output, args, **kwargs):
        if args["rule"] in output:
            return False, False
        else:
            return True, True

    # ##################################################################################################################
    #   Parser Helper Functions   ######################################################################################
    # ##################################################################################################################
    def __check_optional_rule_data(self, rule, mask, port_string, storage_type, vlan, cos):
        result = True

        if mask is not None:
            if rule.mask != mask:
                result = False
                self.logger.log_info("Configured rule mask " + rule.mask + " was not equal to " + mask + ".")

        if port_string is not None:
            if rule.port.lower() != port_string.lower():
                result = False
                self.logger.log_info("Configured port " + rule.port + " was not equal to " + port_string + ".")

        if storage_type is not None:
            if rule.storage_type != storage_type:
                result = False
                self.logger.log_info("Configured storage type " + rule.storage_type + " was not equal to " +
                                     storage_type + ".")

        if vlan is not None:
            if rule.vlan != vlan:
                result = False
                self.logger.log_info("Configured VLAN " + rule.vlan + " was not equal to " + vlan + ".")

        if cos is not None:
            if rule.cos != cos:
                result = False
                self.logger.log_info("Configured COS value " + rule.cos + " was not equal to " + cos + ".")

        return result

    def __create_policy_admin_profile_list(self, output):
        policy_admin_rules = list()
        output = output.split('========================================')
        output = [i for i in output if "Profile" in i]  # Remove entries that aren't admin profiles.

        for rule_block in output:
            if self.pw.get_value_by_offset(rule_block, "Profile Index", 2)[1:] == "Admin-Profile":
                rule = PolicyAdminProfile()

                rule.profile_index = "Admin-Profile"
                rule.rule_type = self.pw.get_value_range(rule_block, "Rule Type", "\r")[1:]
                rule.rule_data = self.pw.get_value_by_offset(rule_block, "Rule Data", 2)[1:]
                rule.mask = self.pw.get_value_by_offset(rule_block, "Mask", 1)[1:]
                rule.port = self.pw.get_value_by_offset_with_exclude(rule_block, "Port", 1, ":Port")[1:]
                rule.status = self.pw.get_value_by_offset(rule_block, "Status", 1)[1:]
                rule.storage_type = self.pw.get_value_by_offset(rule_block, "Storage Type", 2)[1:]
                rule.oper_pid = self.pw.get_value_by_offset(rule_block, "Operational-PID", 1)[1:]
                rule.admin_pid = self.pw.get_value_by_offset(rule_block, "Admin-PID", 1)[1:]

                policy_admin_rules.append(rule)
        return policy_admin_rules

    def __create_policy_rule_list(self, output):
        policy_rules = list()
        output = output.split("========================================")
        output = [i for i in output if "Profile" in i]  # Remove entries that aren't policy rules.

        for rule_block in output:
            if self.pw.get_value_by_offset(rule_block, "Profile Index", 2)[1:] != "Admin-Profile":
                rule = PolicyRule()

                rule.policy_id = self.pw.get_value_by_offset(rule_block, "Profile Index", 2)[1:]
                rule.rule_type = self.pw.get_value_range(rule_block, "Rule Type", "\r")[1:]
                rule.rule_data = self.pw.get_value_by_offset(rule_block, "Rule Data", 2)[1:]
                rule.rule_data_hex = (hex(int(rule.rule_data))) if str(rule.rule_data).isdigit() else None
                rule.mask = self.pw.get_value_by_offset(rule_block, "Mask", 1)[1:]
                rule.port = self.pw.get_value_by_offset_with_exclude(rule_block, "Port", 1, ":Port")[1:]
                rule.status = self.pw.get_value_by_offset(rule_block, "Status", 1)[1:]
                rule.storage_type = self.pw.get_value_by_offset(rule_block, "Storage Type", 2)[1:]
                rule.vlan = self.pw.get_value_by_offset(rule_block, "VLAN", 1)[1:]
                rule.cos = self.pw.get_value_by_offset(rule_block, "COS", 1)[1:]

                policy_rules.append(rule)
        return policy_rules

    def __create_policy_profile_list(self, output):
        policy_profiles = list()
        output = output.split("-----------------------------------------")
        output = [i for i in output if "Profile" in i]  # Remove entries that aren't policy profiles.

        for profile_block in output:
            profile = PolicyProfile()

            profile.profile_id = self.pw.get_value_by_offset(profile_block, "Profile Index", 2)[1:]
            profile.profile_name = self.pw.get_value_range(profile_block, "Profile Name", "\r")[1:]
            profile.row_status = self.pw.get_value_by_offset(profile_block, "Row Status", 2)[1:]
            profile.port_vid_status = self.pw.get_value_by_offset(profile_block, "Port VID Status", 3)[1:]
            profile.port_vid_override = self.pw.get_value_by_offset(profile_block, "Port VID Override", 3)[1:]
            profile.cos_status = self.pw.get_value_by_offset(profile_block, "CoS Status", 2)[1:]
            profile.cos = self.pw.get_value_by_offset_with_exclude(profile_block, "CoS", 1, "CoS Status")[1:]
            profile.disable_ingress_port = self.pw.get_value_by_offset(profile_block, "Disable ingress port", 3)[1:]
            profile.replace_tci_status = self.pw.get_value_by_offset(profile_block, "Replace TCI Status", 3)[1:]
            profile.tagged_egress = self.pw.get_value_by_offset(profile_block, "Tagged Egress", 2)[1:]
            profile.untagged_egress = self.pw.get_value_by_offset(profile_block, "Untagged Egress", 2)[1:]
            profile.forbidden_egress = self.pw.get_value_by_offset(profile_block, "Forbidden Egress", 2)[1:]
            profile.rule_precedence = self.pw.get_value_by_offset(profile_block, "Rule Precedence", 2)[1:]
            profile.admin_profile_usage = self.pw.get_value_by_offset(profile_block, "Admin Profile Usage", 3)[1:]
            profile.oper_profile_usage = self.pw.get_value_by_offset(profile_block, "Oper Profile Usage", 3)[1:]
            profile.dynamic_profile_usage = self.pw.get_value_by_offset(profile_block, "Dynamic Profile Usage", 3)[1:]

            policy_profiles.append(profile)
        return policy_profiles
