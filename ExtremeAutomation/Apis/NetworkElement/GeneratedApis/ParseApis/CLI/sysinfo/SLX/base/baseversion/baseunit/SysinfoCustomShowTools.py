from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.sysinfo.base.SysinfoBaseCustomShowTools import \
    SysinfoBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class SysinfoCustomShowTools(SysinfoBaseCustomShowTools):
    def __init__(self, device):
        super(SysinfoCustomShowTools, self).__init__(device)

    def get_firmware_version(self, output, args, **kwargs):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_firmware_version(self, output, version, **kwargs):
        firmware = self.pw.get_value_by_offset(output, "Firmware name:", 2)

        result = False
        if firmware.lower() == version.lower():
            result = True
        return result, {"ret_version": firmware}
