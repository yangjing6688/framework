from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.sysinfo.base.SysinfoBaseCustomShowTools import \
    SysinfoBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class SysinfoCustomShowTools(SysinfoBaseCustomShowTools):
    def __init__(self, device):
        super(SysinfoCustomShowTools, self).__init__(device)

    def check_firmware_version(self, output, version, *args):
        filename_list = self.pw.get_eol_value(output, "Filename:")
        version_list = self.pw.get_value_by_offset(output, "Version:", 1).split(" ")

        result = False
        output_version = None
        for i, versions in enumerate(version_list):
            if "Active" in filename_list[i]:
                output_version = version_list[i]
                if output_version.lower() == version.lower():
                    result = True
        return result, {"ret_version": output_version}

    def get_firmware_version(self, output, *args):
        filename_list = self.pw.get_eol_value(output, "Filename:")
        version_list = self.pw.get_value_by_offset(output, "Version:", 1).split(" ")
        firmware = "unknown"

        for i, versions in enumerate(version_list):
            if "Active" in filename_list[i]:
                firmware = version_list[i]
                break

        result = True if firmware != "unknown" else False
        return result, firmware
