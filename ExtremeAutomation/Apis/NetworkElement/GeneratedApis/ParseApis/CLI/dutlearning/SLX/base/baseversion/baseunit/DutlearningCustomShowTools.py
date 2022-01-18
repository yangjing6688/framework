from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.dutlearning.base.DutlearningBaseCustomShowTools \
    import DutlearningBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class DutlearningCustomShowTools(DutlearningBaseCustomShowTools):
    def __init__(self, device):
        super(DutlearningCustomShowTools, self).__init__(device)

    def gather_unit_info(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def gather_chassis_info(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def gather_port_info(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def gather_system_info(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def gather_license_info(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
