from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.filemanagement.base.\
    FilemanagementBaseCustomShowTools import FilemanagementBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return FilemanagementCustomShowTools(device)


class FilemanagementCustomShowTools(FilemanagementBaseCustomShowTools):
    def __init__(self, device):
        super(FilemanagementCustomShowTools, self).__init__(device)

    def check_default_boot_config_file(self, output, args, **kwargs):
        output = output.replace('"', '')
        parse_result = self.pw.get_value_by_offset(output, "choice primary config-file", 3)

        result = True if args["config"] == parse_result else False
        return result, {"ret_default_boot_file": parse_result}

    def check_config_file_exists(self, output, args, **kwargs):
        formats = [".conf", ".cfg", ".config", ".tgz"]

        config_files = []
        for filename in output.split():
            for ending in formats:
                if ending in filename:
                    config_files.append(filename)

        for config_file in config_files:
            if args["config"] in config_file:
                return True, True
        return False, False

    def check_config_file_exists_per_slot(self, output, args, **kwargs):
        formats = [".conf", ".cfg", ".config", ".tgz"]

        config_files = []
        for filename in output.split():
            for ending in formats:
                if ending in filename:
                    config_files.append(filename)

        for config_file in config_files:
            if args["config"] in config_file:
                return True, True
        return False, False

    def get_version_filename(self, output, version):
        filename_list = self.pw.get_value_by_offset(output, "VOSS", 0).splitlines()
        new_filename_list = filename_list[0].split(' ')

        filename = None
        result = False
        for item in new_filename_list:
            if item.lower() == version.lower():
                filename = item
                result = True
                break

        return result, filename

    def check_primary_boot_config_file(self, output, args, **kwargs):
        output = output.replace('"', '')
        parse_result = self.pw.get_value_by_offset(output, "choice primary config-file", 3)

        result = True if args["config"] == parse_result else False
        return result, {"ret_primary_boot_file": parse_result}

    def check_primary_backup_boot_config_file(self, output, args, **kwargs):
        output = output.replace('"', '')
        parse_result = self.pw.get_value_by_offset(output, "choice primary backup-config-file", 3)

        result = True if args["config"] == parse_result else False
        return result, {"ret_backup_boot_file": parse_result}
