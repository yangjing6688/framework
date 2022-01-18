from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.filemanagement.base.\
    FilemanagementBaseCustomShowTools import FilemanagementBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class FilemanagementCustomShowTools(FilemanagementBaseCustomShowTools):
    def __init__(self, device):
        super(FilemanagementCustomShowTools, self).__init__(device)

    def get_version_filename(self, output, version):
        filename_list = self.pw.get_value_by_offset(output, "Filename:", 1).split(" ")
        version_list = self.pw.get_value_by_offset(output, "Version:", 1).split(" ")

        filename = None
        for i, versions in enumerate(version_list):
            if version.lower() == versions.lower():
                filename = filename_list[i]

        if filename is not None:
            result = True
        else:
            filename = None
            result = False

        return result, filename
