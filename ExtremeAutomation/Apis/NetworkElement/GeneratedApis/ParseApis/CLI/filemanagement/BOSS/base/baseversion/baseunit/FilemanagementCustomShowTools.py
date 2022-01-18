from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.filemanagement.base.\
    FilemanagementBaseCustomShowTools import FilemanagementBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return FilemanagementCustomShowTools(device)


class FilemanagementCustomShowTools(FilemanagementBaseCustomShowTools):
    def __init__(self, device):
        super(FilemanagementCustomShowTools, self).__init__(device)

    def get_version_filename(self, output, version):
        filename = self.pw.get_value_by_offset(output, version, 0)

        if filename.lower() == "primary" or filename.lower() == "secondary":
            ret_filename = filename
            result = True
        else:
            ret_filename = None
            result = False

        return result, ret_filename
