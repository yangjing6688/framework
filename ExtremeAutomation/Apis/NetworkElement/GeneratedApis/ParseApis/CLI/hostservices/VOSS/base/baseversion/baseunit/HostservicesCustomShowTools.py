from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.hostservices.base.\
    HostservicesBaseCustomShowTools import HostservicesBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return HostservicesCustomShowTools(device)


class HostservicesCustomShowTools(HostservicesBaseCustomShowTools):
    def __init__(self, device):
        super(HostservicesCustomShowTools, self).__init__(device)

    def verify_sys_force_topology_ip_flag_is_enabled(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "ForceTopologyIpFlag", 2)

        result = True if parse_result == "true" else False
        return result, {"ret_ForceTopologyIpFlag": parse_result}

    def verify_autotopology_nmm_table_entries(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_sys_clipid_topology_ip(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "clipId-topology-ip", 2)

        result = True if parse_result == args["clip_id"] else False
        return result, {"ret_clipId-topology-ip": parse_result}

    def verify_sys_force_topology_ip_flag_is_disabled(self, output, args, **kwargs):
        parse_result = self.pw.get_value_by_offset(output, "ForceTopologyIpFlag", 2)

        result = True if parse_result == "false" else False
        return result, {"ret_ForceTopologyIpFlag": parse_result}
