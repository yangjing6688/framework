from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.filemanagement.base.\
    FilemanagementBaseCustomShowTools import FilemanagementBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return FilemanagementCustomShowTools(device)


class FilemanagementCustomShowTools(FilemanagementBaseCustomShowTools):
    def __init__(self, device):
        super(FilemanagementCustomShowTools, self).__init__(device)

    def check_default_boot_config_file(self, output, args, **kwargs):
        item = "SNMPv2-SMI::enterprises.2272.1.1.32." + args["oid_index"]
        parse_result = self.pw.get_value_by_offset(output, item, 2)

        result = True if parse_result == str(args["config"]) else False
        return result, {"ret_config": parse_result}
