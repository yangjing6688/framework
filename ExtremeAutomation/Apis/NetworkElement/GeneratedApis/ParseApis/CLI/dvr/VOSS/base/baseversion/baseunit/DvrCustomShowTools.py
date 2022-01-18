from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.dvr.base.DvrBaseCustomShowTools import \
    DvrBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class DvrCustomShowTools(DvrBaseCustomShowTools):
    def __init__(self, device):
        super(DvrCustomShowTools, self).__init__(device)

    def verify_dvr_domain_controller_exists(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_dvr_domain_controller_inject_default_route_all_is_disabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_dvr_domain_controller_inject_default_route_is_disabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_dvr_leaf_id_is_set(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_dvr_leaf_virtual_ist_local_and_peer_ip_is_set(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_interface_vlan_dvr_gateway_ipv4_is_set(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_dvr_on_interface_is_enabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_dvr_redistribute_direct_is_enabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_dvr_redistribute_direct_is_disabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_dvr_redistribute_static_is_enabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_dvr_redistribute_static_is_disabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_dvr_redistribute_direct_metric_is_set(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def verify_dvr_redistribute_static_metric_is_set(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
