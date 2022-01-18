from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.lacp.base.LacpBaseCustomShowTools import \
    LacpBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return LacpCustomShowTools(device)


class LacpCustomShowTools(LacpBaseCustomShowTools):
    def __init__(self, device):
        super(LacpCustomShowTools, self).__init__(device)

    def check_mlt_lacp_actor_admin_key(self, output, args, **kwargs):
        item = "SNMPv2-SMI::iso.2.840.10006.300.43.1.1.1.1.6." + args["oid_index"]
        result_name = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_name == args["actor_admin_key"] else False
        return result, {"ret_actor_admin_key": result_name}

    def check_mlt_lacp_actor_oper_key(self, output, args, **kwargs):
        item = "SNMPv2-SMI::iso.2.840.10006.300.43.1.1.1.1.7." + args["oid_index"]
        result_name = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_name == args["actor_oper_key"] else False
        return result, {"ret_actor_oper_key": result_name}

    def check_mlt_lacp_actor_system_priority(self, output, args, **kwargs):
        item = "SNMPv2-SMI::iso.2.840.10006.300.43.1.1.1.1.9." + args["oid_index"]
        result_name = self.pw.get_value_by_offset(output, item, 2)

        result = True if result_name == args["actor_system_priority"] else False
        return result, {"ret_actor_sys_priority": result_name}
