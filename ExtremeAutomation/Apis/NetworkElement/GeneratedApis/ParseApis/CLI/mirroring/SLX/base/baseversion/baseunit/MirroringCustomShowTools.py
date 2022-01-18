from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.mirroring.base.MirroringBaseCustomShowTools \
    import MirroringBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class MirroringCustomShowTools(MirroringBaseCustomShowTools):
    def __init__(self, device):
        super(MirroringCustomShowTools, self).__init__(device)

    def check_port_mirror_exists(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_mirror_enabled(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_mirror_ingress_exists(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_mirror_egress_exists(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_port_mirror_ingress_egress_exists(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
