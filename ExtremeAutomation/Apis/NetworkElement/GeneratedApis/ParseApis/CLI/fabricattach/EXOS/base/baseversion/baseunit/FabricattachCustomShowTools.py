from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.fabricattach.base.\
    FabricattachBaseCustomShowTools import FabricattachBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return FabricattachCustomShowTools(device)


class FabricattachCustomShowTools(FabricattachBaseCustomShowTools):
    def __init__(self, device):
        super(FabricattachCustomShowTools, self).__init__(device)

    def check_fa_neighbors(self, output, args, **kwargs):
        output = output.replace("\n", "\r\n")
        neighbor_found = self.pw.get_value_by_offset(output, "server", 0)

        result = True if neighbor_found == args["neighbor"] else False
        return result, {"ret_fa_neighbor": neighbor_found}

    def check_fa_service_state(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        service_state = self.pw.get_value_by_offset(output, "service", 2)

        result = True if service_state == "enabled" else False
        return result, {"ret_service_state": service_state}

    def check_fa_element_type(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        element_type = self.pw.get_value_by_offset(output, "element", 2)

        result = True if element_type == "proxy" else False
        return result, {"ret_element_type": element_type}

    def check_fa_zero_touch_status(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fa_auto_provision_setting(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fa_provision_mode(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fa_client_proxy_status(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        proxy_status = self.pw.get_value_by_offset(output, "client", 3)

        result = True if proxy_status == "enabled" else False
        return result, {"ret_proxy_status": proxy_status}

    def check_fa_standalone_proxy_status(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fa_agent_timeout(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        timeout = self.pw.get_value_by_offset(output, "timeout", 2)

        result = True if timeout == args["timeout"] else False
        return result, {"ret_agent_timeout": timeout}

    def check_fa_extended_logging_status(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fa_primary_server_id(self, output, args, **kwargs):
        output = output.lower().replace("\n", "\r\n")
        server_id = self.pw.get_value_by_offset(output, "id", 3)

        result = True if server_id == args["server_id"] else False
        return result, {"ret_server_id": server_id}

    def check_fa_server_description(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fa_elements_system_id(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fa_elements_port(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fa_elements_type(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fa_elements_mgmt_vlan(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fa_elements_tag(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fa_elements_auto_provision(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fa_port_stats_disc_elem_received(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fa_port_stats_disc_elem_expired(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fa_port_stats_elem_deleted(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_fa_port_stats_disc_auth_failed(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
