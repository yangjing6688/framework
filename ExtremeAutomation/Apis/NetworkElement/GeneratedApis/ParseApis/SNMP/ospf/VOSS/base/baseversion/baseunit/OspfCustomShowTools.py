from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.ospf.base.OspfBaseCustomShowTools import \
    OspfBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return OspfCustomShowTools(device)


class OspfCustomShowTools(OspfBaseCustomShowTools):
    def __init__(self, device):
        super(OspfCustomShowTools, self).__init__(device)

    def verify_ospf_globally_enabled(self, output, args, **kwargs):
        item = "SNMPv2-SMI::mib-2.14.1.2." + args["oid_index"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_state": parse_result}

    def verify_ospf_globally_disabled(self, output, args, **kwargs):
        item = "SNMPv2-SMI::mib-2.14.1.2." + args["oid_index"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if parse_result == "2" else False
        return result, {"ret_state": parse_result}

    def verify_ospf_enabled_on_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.8.1.1.1.6." + args["oid_index"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_interface_state": parse_result}

    def verify_ospf_disabled_on_interface(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.8.1.1.1.6." + args["oid_index"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if parse_result == "2" else False
        return result, {"ret_interface_state": parse_result}

    def verify_ospf_enabled_on_vlan(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.8.1.1.1.6." + args["voss_oid_index"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if parse_result == "1" else False
        return result, {"ret_vlan_state": parse_result}

    def verify_ospf_disabled_on_vlan(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.8.1.1.1.6." + args["voss_oid_index"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if parse_result == "2" else False
        return result, {"ret_vlan_state": parse_result}

    def verify_ospf_router_id(self, output, args, **kwargs):
        item = "SNMPv2-SMI::mib-2.14.1.1." + args["oid_index"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if parse_result == args["router_id"] else False
        return result, {"ret_router_id": parse_result}

    def verify_ospf_router_id_is_removed(self, output, args, **kwargs):
        item = "SNMPv2-SMI::mib-2.14.1.1." + args["oid_index"]
        parse_result = self.pw.get_exact_value_by_offset(output, item, 2)

        result = True if parse_result == "0.0.0.0" else False
        return result, {"ret_router_id": parse_result}
