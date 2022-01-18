from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.filemanagement.base.\
    FilemanagementBaseCustomShowTools import FilemanagementBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
import re


class FilemanagementCustomShowTools(FilemanagementBaseCustomShowTools):
    def __init__(self, device):
        super(FilemanagementCustomShowTools, self).__init__(device)

    def check_config_file_exists(self, output, args, **kwargs):
        files = re.findall(r"^[drwx-]+\s+\S+\s+\S+\s+\S+\s+\d+\s+\S+\s+\d+\s+\S+\s+(.*?)$", output, re.MULTILINE)

        result = False
        for file in files:
            if file.strip() == args["config"]:
                result = True
                break

        return result, {"ret_files_found": str(files)}
