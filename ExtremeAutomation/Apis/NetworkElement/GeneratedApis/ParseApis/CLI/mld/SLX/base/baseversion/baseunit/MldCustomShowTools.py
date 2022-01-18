from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.mld.base.MldBaseCustomShowTools import \
    MldBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class MldCustomShowTools(MldBaseCustomShowTools):
    def __init__(self, device):
        super(MldCustomShowTools, self).__init__(device)

    def check_mld_state(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_mld_version(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_mld_snooping_state(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_mld_snooping_querier_state(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_mld_snooping_fast_leave(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_mld_snooping_last_member_query_count(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_mld_snooping_last_member_query_interval(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_mld_snooping_robustness_variable(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_mld_snooping_startup_query_count(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_mld_snooping_startup_query_interval(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_mld_snooping_mrouter(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
