from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.sysinfo.base.SysinfoBaseCustomShowTools import \
    SysinfoBaseCustomShowTools
import re
# All imports above this line will be removed after generation.
# User imports must be added below.

class SysinfoCustomShowTools(SysinfoBaseCustomShowTools):
    def __init__(self, device):
        super(SysinfoCustomShowTools, self).__init__(device)

    def check_firmware_version(self, output, version, *args):
        filename = self.pw.get_value_by_offset(output, '(Primary Release)', 0)

        result = False
        if version.lower() == filename.lower():
            result = True
        return result, {"ret_version": filename}

    def get_firmware_version(self, output, *args):
        firmFull = self.pw.get_value_by_offset(output, 'APP_FS', 1)
        buildmatch = re.match("^[A-Z0-9]+\.([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)int([0-9]+)", firmFull)
        if buildmatch:
            firmware = f"{buildmatch.group(1)}.{buildmatch.group(2)}"
        else:
            firmware = None
        self.logger.log_debug(f"Firmware version: {firmware}")
        result = True if firmFull.lower() != "valuenotpresent" and firmware else False
        return result, firmware

    def store_model(self, output):
        sysname = self.pw.get_value_by_offset(output, 'SysName', 2)
        self.logger.log_debug(f"Model: {sysname}")
        result = True if sysname.lower() != "valuenotpresent" else False
        return result, sysname
