from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.sysinfo.base.SysinfoBaseCustomShowTools import \
    SysinfoBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class SysinfoCustomShowTools(SysinfoBaseCustomShowTools):
    def __init__(self, device):
        super(SysinfoCustomShowTools, self).__init__(device)

    def check_firmware_version(self, output, version, **kwargs):
        firmware = self.pw.get_value_by_offset(output, "Installed software:", 3).strip("SW:")

        result = False
        if firmware.lower() == version.lower():
            result = True
        return result, {"ret_version": firmware}

    def get_firmware_version(self, output, *args):
        firmware = self.pw.get_value_by_offset(output, "Installed software:", 3).strip("SW:")

        result = True if firmware.lower() != "valuenotpresent" else False
        return result, firmware
