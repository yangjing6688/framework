from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.filemanagement.base.\
    FilemanagementBaseCustomShowTools import FilemanagementBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.
import os
import time
from shutil import move
from ExtremeAutomation.Keywords.NetworkElementKeywords.StaticKeywords.NetworkElementFileManagementUtilsKeywords \
    import NetworkElementFileManagementUtilsKeywords

class FilemanagementCustomShowTools(FilemanagementBaseCustomShowTools):
    def __init__(self, device):
        super(FilemanagementCustomShowTools, self).__init__(device)
        self.file_mgmt = NetworkElementFileManagementUtilsKeywords()

    def get_logfile_list(self, output, slot, server_ip, trm_run):
        current_log = self.pw.get_value_by_offset(output, "current", 5)
        if current_log == "current.log":
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())

            local_file = "slot" + slot + "/logs/current.log"
            remote_file = "slot" + slot + "_current_" + timestamp + ".log"

            self.file_mgmt.upload_logging_to_server(self.device.name, local_file, remote_file, server_ip)

            if trm_run is True:
                py_path = None
                path_var = os.environ['PYTHONPATH'].split(os.pathsep)
                for path in path_var:
                    if "SQA_ROBOT_AUTOMATION" in path:
                        py_path = path
                        break

                if py_path is None:
                    py_path = "/home/administrator/Robot/SQA_ROBOT_AUTOMATION/"

                dest_path = os.path.join(py_path, "ExtremeAutomation/TRM_DATA/EXECUTE_GIT_Master/")

                self.logger.log_info("Moving log file " + remote_file + " to Test Plan logging directory.")
                src_path = os.path.join(py_path, remote_file)
                newdest_path = os.path.join(dest_path, remote_file)
                move(src_path, newdest_path)

            return True, None
        else:
            return False, None

    def move_core_files(self, output, server_ip, file_name):
        py_path = None
        path_var = os.environ['PYTHONPATH'].split(os.pathsep)

        for path in path_var:
            if "SQA_ROBOT_AUTOMATION" in path:
                py_path = path
                break

        if py_path is None:
            py_path = "/home/administrator/Robot/SQA_ROBOT_AUTOMATION/"

        self.logger.log_info("Moving debug file " + file_name + " to Test Plan logging directory.")
        dest_path = os.path.join(py_path, "ExtremeAutomation/TRM_DATA/EXECUTE_GIT_Master/")
        src_path = py_path + file_name
        ldest_path = dest_path + file_name
        move(src_path, ldest_path)

        return True, None

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
            result = False

        return result, filename

    def get_unused_imagename(self, output):
        filename_list = self.pw.get_value_by_offset(output, "Filename:", 1).split(" ")

        result = False
        ret_imagename = None
        if not len(filename_list) < 3:
            for filename in filename_list:
                if self.pw.get_value_by_offset(output, filename, 2) == "valueNotPresent":
                    result = True
                    ret_imagename = filename
                    break

        return result, ret_imagename

    def check_version_present(self, output, version):
        version_list = self.pw.get_value_by_offset(output, "Version:", 1).split(" ")

        result = False
        for cli_version in version_list:
            if cli_version.lower() == version.lower():
                result = True
        return result, result

    def check_config_file_exists(self, output, args, **kwargs):
        formats = [".conf", ".cfg", ".config"]

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
        formats = [".conf", ".cfg", ".config"]

        config_files = []
        for filename in output.split():
            for ending in formats:
                if ending in filename:
                    config_files.append(filename)

        for config_file in config_files:
            if args["config"] in config_file:
                return True, True
        return False, False
