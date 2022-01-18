from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.policy.base.PolicyBaseCustomShowTools import \
    PolicyBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.Lists.IntList import IntList
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.Parsing.PolicyRule import PolicyRule
from ExtremeAutomation.Library.Utils.Parsing.PolicyProfile import PolicyProfile
from ExtremeAutomation.Library.Utils.Parsing.PolicyAdminProfile import PolicyAdminProfile


def create_instance(device):
    return PolicyCustomShowTools(device)


class PolicyCustomShowTools(PolicyBaseCustomShowTools):
    def __init__(self, device):
        super(PolicyCustomShowTools, self).__init__(device)

    # ##################################################################################################################
    #   Current Parser Functions   #####################################################################################
    # ##################################################################################################################
    def check_policy_profile_exists(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        profile_ids = []
        for profile in policy_profiles:
            profile_ids.append(profile.profile_id)
            result = profile.profile_id == args["profile_id"]
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
        return result, {"ret_tagged_vlan": vlan}

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
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        tci = None
        for profile in policy_profiles:
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
                    precedence = profile.rule_precedence
                    result = IntList(profile.rule_precedence).get_all() == normalized_precedence_string
                    break
        except ValueError:
            pass
        return result, {"ret_rule_precedence": precedence}

    def check_policy_profile_mirror_dest(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        mirror = None
        for profile in policy_profiles:
            if profile.profile_id == args["profile_id"]:
                mirror = profile.mirror
                result = profile.mirror == args["mirror_index"]
                break
        return result, {"ret_mirror": mirror}

    def check_policy_profile_syslog(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        syslog = None
        for profile in policy_profiles:
            if profile.profile_id == args["profile_id"]:
                syslog = profile.syslog_on_use
                result = profile.syslog_on_use.lower() == "enable"
                break
        return result, {"ret_syslog": syslog}

    def check_policy_profile_trap(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        trap = None
        for profile in policy_profiles:
            if profile.profile_id == args["profile_id"]:
                trap = profile.trap_on_use
                result = profile.trap_on_use == "enable"
                break
        return result, {"ret_trap_status": trap}

    def check_policy_profile_disable_port(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        action = None
        for profile in policy_profiles:
            if profile.profile_id == args["profile_id"]:
                action = profile.disable_ingress_port
                result = profile.disable_ingress_port == "enable"
                break
        return result, {"ret_action": action}

    def check_policy_profile_fst(self, output, args, **kwargs):
        policy_profiles = self.__create_policy_profile_list(output)

        result = False
        fst = None
        for profile in policy_profiles:
            if profile.profile_id == args["profile_id"]:
                fst = profile.fst_class_index
                result = profile.fst_class_index == args["fst_index"]
                break
        return result, {"ret_fst_index": fst}

    def check_policy_profile_web_redirect(self, output, args, **kwargs):
        policy_profile = self.__create_policy_profile_list(output)

        result = False
        redirect = None
        for profile in policy_profile:
            if profile.profile_id == args["profile_id"]:
                redirect = profile.web_redirect_index
                result = profile.web_redirect_index == args["web_redirect_index"]
                break
        return result, {"ret_web_redirect": redirect}

    def check_policy_rule_application(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "application layer":
                if rule.rule_data == args["application"].upper() + "-" + args["application_type"].lower():
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No application rule with data " + args["application"].upper() + "-" +
                                 args["application_type"].lower() + " found.")

        return result, found_fule

    def check_policy_rule_ether(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ether ii packet type":
                if rule.rule_data.lower() == args["ether_type"].lower():
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No ether rule with data " + args["ether_type"] + " found.")

        return result, found_fule

    def check_policy_rule_icmp6type(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        icmp6_type = args["icmp6_type"]
        icmp6_code = args["icmp6_code"]

        if "0x" in icmp6_type:
            icmp6_type = str(int(icmp6_type, 16))
        if "0x" in icmp6_code:
            icmp6_code = str(int(icmp6_code, 16))

        rule_data = icmp6_type + "." + icmp6_code

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "icmpv6 packet type":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No ICMPv6 type rule with data " + rule_data + " found.")

        return result, found_fule

    def check_policy_rule_icmptype(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        icmp_type = args["icmp_type"]
        icmp_code = args["icmp_code"]

        if "0x" in icmp_type:
            icmp_type = str(int(icmp_type, 16))
        if "0x" in icmp_code:
            icmp_code = str(int(icmp_code, 16))

        rule_data = icmp_type + "." + icmp_code

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "icmp packet type":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No ICMP type rule with data " + rule_data + " found.")

        return result, found_fule

    def check_policy_rule_ip6dest(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        ipv6_addr = StringUtils.collapse_ipv6_address(args["ipv6_addr"])
        rule_data = ipv6_addr if args["l4_port"] is None else ipv6_addr + "-" + args["l4_port"]
        rule_data_verified = False

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ipv6 destination address":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IPv6 destination rule with data " + rule_data + " found.")

        return result, found_fule

    def check_policy_rule_ip6flowlabel(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ipv6 flow label":
                if rule.rule_data == args["ipv6_flow_label"]:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IPv6 flow label rule with data " + args["ipv6_flow_label"] + " found.")

        return result, found_fule

    def check_policy_rule_ip6source(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        ipv6_addr = StringUtils.collapse_ipv6_address(args["ipv6_addr"])
        rule_data = ipv6_addr if args["l4_port"] is None else ipv6_addr + "-" + args["l4_port"]
        rule_data_verified = False

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ipv6 source address":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IPv6 source rule with data " + rule_data + " found.")

        return result, found_fule

    def check_policy_rule_ipdestsocket(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        rule_data = args["ip_addr"] if args["l4_port"] is None else args["ip_addr"] + ":" + args["l4_port"]

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ip destination address":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IP destination socket rule with data " + rule_data + " found.")

        return result, found_fule

    def check_policy_rule_ipfrag(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ip fragmentation":
                found_fule = rule.rule_data_dict()
                if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                   args["vlan"], args["cos"], args["tci_overwrite"],
                                                   args["mirror_destination"], args["syslog"], args["trap"],
                                                   args["disable_port"], args["quarantine_profile"]):
                    result = True
                    break
        return result, found_fule

    def check_policy_rule_ipproto(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ip proto":
                if rule.rule_data.split()[0] == args["ip_proto"]:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IP proto rule with data " + args["ip_proto"] + " found.")

        return result, found_fule

    def check_policy_rule_ipsourcesocket(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        rule_data = args["ip_addr"] if args["l4_port"] is None else args["ip_addr"] + ":" + args["l4_port"]

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ip source address":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IP source socket rule with data " + rule_data + " found.")

        return result, found_fule

    def check_policy_rule_iptos(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ip type of service":
                if rule.rule_data.split()[0] == args["ip_tos"]:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IP TOS rule with data " + args["ip_tos"] + " found.")

        return result, found_fule

    def check_policy_rule_ipttl(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ttl":
                if rule.rule_data.split()[0] == args["ip_ttl"]:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IP TTL rule with data " + args["ip_ttl"] + " found.")

        return result, found_fule

    def check_policy_rule_ipxclass(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ipx transmission control":
                if rule.rule_data.split()[0] == args["ipx_class"]:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IPX class rule with data " + args["ipx_class"] + " found.")

        return result, found_fule

    def check_policy_rule_ipxdest(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        rule_data = "0x" + ("0" * (8 - len(args["ipx_dest"].replace("0x", "")))) + args["ipx_dest"].replace("0x", "")

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ipx destination address":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IPX destination rule with data " + rule_data + " found.")

        return result, found_fule

    def check_policy_rule_ipxdestsocket(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ipx destination socket":
                if rule.rule_data.split()[0] == args["ipx_dest_socket"]:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IPX destination socket rule with data " + args["ipx_dest_socket"] + " found.")

        return result, found_fule

    def check_policy_rule_ipxsource(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        rule_data = "0x" + ("0" * (8 - len(args["ipx_source"].replace("0x", "")))) + \
                    args["ipx_source"].replace("0x", "")

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ipx source address":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IPX source rule with data " + rule_data + " found.")

        return result, found_fule

    def check_policy_rule_ipxsourcesocket(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ipx source socket":
                if rule.rule_data.split()[0] == args["ipx_source_socket"]:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IPX source socket rule with data " + args["ipx_source_socket"] + " found.")

        return result, found_fule

    def check_policy_rule_ipxtype(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "ipx type field":
                if rule.rule_data.split()[0] == args["ipx_type"]:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No IPX type rule with data " + args["ipx_type"] + " found.")

        return result, found_fule

    def check_policy_rule_llcdsapssap(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "llc dsap/ssap/ctrl":
                if rule.rule_data == args["llc_dsap_ssap"]:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No LLC DSAP SSAP rule with data " + args["llc_dsap_ssap"] + " found.")

        return result, found_fule

    def check_policy_rule_macdest(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        rule_data = StringUtils.normalize_mac(args["mac_addr"], "-")

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "mac destination address":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No MAC destination rule with data " + rule_data + " found.")

        return result, found_fule

    def check_policy_rule_macsource(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        rule_data = StringUtils.normalize_mac(args["mac_addr"], "-")

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "mac source address":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No MAC source rule with data " + rule_data + " found.")

        return result, found_fule

    def check_policy_rule_port(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "port string":
                if rule.rule_data == args["port"]:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No port rule with data " + args["port"] + " found.")

        return result, found_fule

    def check_policy_rule_tci(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        tci_value = args["tci_value"]
        if "0x" in tci_value:
            tci_value = str(int(tci_value, 16))

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "replace tci":
                if rule.rule_data.split()[0] == tci_value:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No TCI rule with data " + tci_value + " found.")

        return result, found_fule

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
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "tcp port destination":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No TCP destination port IP rule with data " + rule_data + " found.")

        return result, found_fule

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
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "tcp port source":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No TCP source port IP rule with data " + rule_data + " found.")

        return result, found_fule

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
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "udp port destination":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No UDP destination port IP rule with data " + rule_data + " found.")

        return result, found_fule

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
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "udp port source":
                if rule.rule_data == rule_data:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No UDP source port IP rule with data " + rule_data + " found.")

        return result, found_fule

    def check_policy_rule_vlantag(self, output, args, **kwargs):
        policy_rules = self.__create_policy_rule_list(output)
        rule_data_verified = False

        result = False
        found_fule = None
        for rule in policy_rules:
            if rule.rule_type.lower() == "vlan tag":
                if rule.rule_data.split()[0] == args["vlan_tag"]:
                    rule_data_verified = True
                    found_fule = rule.rule_data_dict()
                    if self.__check_optional_rule_data(rule, args["mask"], args["port_string"], args["storage_type"],
                                                       args["vlan"], args["cos"], args["tci_overwrite"],
                                                       args["mirror_destination"], args["syslog"], args["trap"],
                                                       args["disable_port"], args["quarantine_profile"]):
                        result = True
                        break

        if not rule_data_verified:
            self.logger.log_info("No VLAN tag rule with data " + args["vlan_tag"] + " found.")

        return result, found_fule

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

        return result, {"ret_allowed_types": output_type_list}

    def check_port_admin_profile(self, output, args, **kwargs):
        admin_profiles = self.__create_policy_admin_profile_list(output)

        result = False
        found_rule = None
        for admin_profile in admin_profiles:
            if admin_profile.rule_type.lower() == "port string":
                found_rule = admin_profile.rule_data_dict()
                if admin_profile.rule_data == args["port"] and admin_profile.port == args["port"]:
                    result = True
                    break
        return result, found_rule

    def check_mac_source_admin_profile(self, output, args, **kwargs):
        admin_profiles = self.__create_policy_admin_profile_list(output)

        result = False
        found_rule = None
        for admin_profile in admin_profiles:
            if admin_profile.rule_type.lower() == "mac source address":
                found_rule = admin_profile.rule_data_dict()
                if admin_profile.rule_data == StringUtils.normalize_mac(args["mac_addr"], "-") and \
                        admin_profile.port == args["port"]:
                    result = True
                    break
        return result, found_rule

    # ##################################################################################################################
    #   Parser Helper Functions   ######################################################################################
    # ##################################################################################################################

    def __check_optional_rule_data(self, rule, mask, port_string, storage_type, vlan, cos, tci_overwrite,
                                   mirror_destination, syslog, trap, disable_port, quarantine_profile):
        result = True

        if mask is not None:
            if rule.mask != mask:
                result = False
                self.logger.log_info("Configured rule mask " + rule.mask + " was not equal to " + mask + ".")

        if port_string is not None:
            if rule.port != port_string:
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

        if tci_overwrite is not None:
            if rule.replace_tci_status != tci_overwrite:
                result = False
                self.logger.log_info("Configured TCI overwrite status " + rule.replace_tci_status +
                                     " was not equal to " + tci_overwrite + ".")

        if mirror_destination is not None:
            if rule.mirror != mirror_destination:
                result = False
                self.logger.log_info("Configured mirror destination " + rule.mirror + " was not equal to " +
                                     mirror_destination + ".")

        if syslog is not None:
            if rule.audit_syslog_status != syslog:
                result = False
                self.logger.log_info("Configured syslog status " + rule.audit_syslog_status + " was not equal to " +
                                     syslog + ".")

        if trap is not None:
            if rule.audit_trap_status != trap:
                result = False
                self.logger.log_info("Configured trap status " + rule.audit_trap_status + " was not equal to " +
                                     trap + ".")

        if disable_port is not None:
            if rule.disable_port_status != disable_port:
                result = False
                self.logger.log_info("Configured disable port status " + rule.disable_port_status +
                                     " was not equal to " + disable_port + ".")

        if quarantine_profile is not None:
            if rule.quarantine_profile != quarantine_profile:
                result = False
                self.logger.log_info("Configured quarantine profile " + rule.quarantine_profile +
                                     " was not equal to " + quarantine_profile + ".")

        return result

    def __create_policy_admin_profile_list(self, output):
        policy_admin_rules = list()
        output = output.split('========================================')
        output = [i for i in output if "Profile" in i]  # Remove list entries that aren't admin profiles.

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
        policy_rules = []
        output = output.split('========================================')
        output = [i for i in output if "Profile" in i]  # Remove list entries that aren't policy rules.

        for rule_block in output:
            rule = PolicyRule()

            rule.policy_id = self.pw.get_value_by_offset(rule_block, "Profile Index", 2)[1:]
            rule.rule_type = self.pw.get_value_range(rule_block, "Rule Type", "\r")[1:]
            rule.rule_data = self.pw.get_value_by_offset(rule_block, "Rule Data", 2)[1:]
            rule.rule_data_hex = (hex(int(rule.rule_data))) if str(rule.rule_data).isdigit() else None
            rule.mask = self.pw.get_value_by_offset(rule_block, "Mask", 1)[1:]
            rule.port = self.pw.get_value_by_offset_with_exclude(rule_block, "Port", 1, ":Port")[1:]
            rule.status = self.pw.get_value_by_offset(rule_block, "Status", 1)[1:].split()[0]
            rule.storage_type = self.pw.get_value_by_offset(rule_block, "Storage Type", 2)[1:]
            rule.vlan = self.pw.get_value_by_offset_with_exclude(rule_block, "VLAN", 1, ":VLAN")[1:]
            rule.cos = self.pw.get_value_by_offset(rule_block, "CoS", 1)[1:]
            rule.mirror = self.pw.get_value_by_offset(rule_block, "Mirror", 1)[1:]
            rule.quarantine_profile = self.pw.get_value_by_offset(rule_block, "Quarantine Profile", 2)[1:]
            rule.audit_syslog_status = self.pw.get_value_by_offset(rule_block, "Audit Syslog Status", 3)[1:]
            rule.audit_trap_status = self.pw.get_value_by_offset(rule_block, "Audit Trap Status", 3)[1:]
            rule.disable_port = self.pw.get_value_by_offset(rule_block, "Disable Port Status", 3)[1:]
            rule.replace_tci_status = self.pw.get_value_by_offset(rule_block, "Replace TCI Status", 3)[1:]

            policy_rules.append(rule)
        return policy_rules

    def __create_policy_profile_list(self, output):
        policy_profiles = []
        output = output.split('-----------------------------------------')
        output = [i for i in output if "Profile" in i]  # Remove list entries that aren't policy profiles.

        for profile_block in output:
            profile = PolicyProfile()

            profile.profile_id = self.pw.get_value_by_offset(profile_block, "Profile Index", 2)[1:]
            profile.profile_name = self.pw.get_value_range(profile_block, "Profile Name", "\r")[1:]
            profile.row_status = self.pw.get_value_by_offset(profile_block, "Row Status", 2)[1:]
            profile.port_vid_status = self.pw.get_value_by_offset(profile_block, "Port VID Status", 3)[1:]
            profile.port_vid_override = self.pw.get_value_by_offset(profile_block, "Port VID Override", 3)[1:]
            profile.cos_status = self.pw.get_value_by_offset(profile_block, "CoS Status", 2)[1:]
            profile.cos = self.pw.get_value_by_offset_with_exclude(profile_block, "CoS", 1, "CoS Status")[1:]
            profile.mirror = self.pw.get_value_by_offset(profile_block, "Mirror", 1)[1:]
            profile.fst_class_index = self.pw.get_value_by_offset(profile_block, "FST Class Index", 3)[1:]
            profile.web_redirect_index = self.pw.get_value_by_offset(profile_block, "Web Redirect Index", 4)[1:]
            profile.syslog_on_use = self.pw.get_value_by_offset(profile_block, "Syslog on use", 3)[1:]
            profile.trap_on_use = self.pw.get_value_by_offset(profile_block, "Trap on use", 3)[1:]
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
