from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.filemanagement.base.\
    FilemanagementBaseCustomShowTools import FilemanagementBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class FilemanagementCustomShowTools(FilemanagementBaseCustomShowTools):
    def __init__(self, device):
        super(FilemanagementCustomShowTools, self).__init__(device)

    def get_version_filename(self, output, version, **kwargs):
        filename = self.pw.get_value_by_offset(output, version, 1)

        if filename.lower() == "pri" or filename.lower() == "sec":
            if filename.lower() == "pri":
                filename = "primary"
                result = True
            else:
                filename = "secondary"
                result = True
        else:
            filename = None
            result = False

        return result, filename
