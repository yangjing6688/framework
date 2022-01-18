from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.REST.sysinfo.base.SysinfoBaseCustomShowTools import \
    SysinfoBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


def create_instance(device):
    return SysinfoCustomShowTools(device)


class SysinfoCustomShowTools(SysinfoBaseCustomShowTools):
    def __init__(self, device):
        super(SysinfoCustomShowTools, self).__init__(device)

    def check_firmware_version(self, output, version):
        output = StringUtils.format_json_output(output)

        output = StringUtils.format_json_output(output)
        output = output["result"][0]["CLIoutput"]
        output = output.replace("\n", "\r\n")

        image = self.pw.get_value_by_offset(output, "IMG:", 9)

        result = True if version.lower() == image.lower() else False
        return result, {"ret_version": version}

    def check_installed_xmods(self, output, xmod_file_name):
        output = StringUtils.format_json_output(output)

        output = StringUtils.format_json_output(output)
        output = output["result"][0]["CLIoutput"]
        output = output.replace("\n", "\r\n")

        if len(xmod_file_name) <= 5 or xmod_file_name[len(xmod_file_name) - 5:len(xmod_file_name)] != ".xmod":
            xmod_file_name += ".xmod"

        output = output.lower()
        all_xmods = self.pw.get_value_by_offset(output, ".xmod ", 9)
        all_xmods = all_xmods.split(" ")

        result = True if xmod_file_name.lower() in all_xmods else False
        return result, {"ret_xmods": str(all_xmods)}
