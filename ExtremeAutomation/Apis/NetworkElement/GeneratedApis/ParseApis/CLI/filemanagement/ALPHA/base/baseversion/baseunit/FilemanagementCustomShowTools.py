from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.filemanagement.base.\
    FilemanagementBaseCustomShowTools import FilemanagementBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return FilemanagementCustomShowTools(device)


class FilemanagementCustomShowTools(FilemanagementBaseCustomShowTools):
    def __init__(self, device):
        super(FilemanagementCustomShowTools, self).__init__(device)

    def get_version_filename(self, output, version, **kwargs):
        active_image = self.pw.get_value_by_offset(output, version, 1)
        backup_image = self.pw.get_value_by_offset(output, version, 2)

        filename = None

        if active_image == version:
            result = True
            filename = "active"
        elif backup_image == version:
            result = True
            filename = "backup"
        else:
            result = False

        return result, filename

    def check_config_file_exists(self, output, args, **kwargs):
        formats = [".cfg", ".config"]

        config_files = []
        for filename in output.split():
            for ending in formats:
                if ending in filename:
                    config_files.append(filename)

        for config_file in config_files:
            if args["config"] in config_file:
                return True, True
        return False, False
