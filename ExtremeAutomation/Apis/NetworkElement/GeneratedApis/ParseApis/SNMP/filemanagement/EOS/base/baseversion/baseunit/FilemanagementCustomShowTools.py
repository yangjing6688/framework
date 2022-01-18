from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.SNMP.filemanagement.base.\
    FilemanagementBaseCustomShowTools import FilemanagementBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return FilemanagementCustomShowTools(device)


class FilemanagementCustomShowTools(FilemanagementBaseCustomShowTools):
    def __init__(self, device):
        super(FilemanagementCustomShowTools, self).__init__(device)

    def get_logfile_list(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def move_core_files(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def get_version_filename(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def get_unused_imagename(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None

    def check_version_present(self, *args):
        return self.cmd_obj_constants.METHOD_NOT_SUPPORTED, None
