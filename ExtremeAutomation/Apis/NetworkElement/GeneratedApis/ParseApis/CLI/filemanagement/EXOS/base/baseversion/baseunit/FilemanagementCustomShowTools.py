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
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())

        local_file = "log"
        remote_file = "slot" + slot + "_syslog_" + timestamp + ".log"

        self.file_mgmt.upload_logging_to_server(self.device.name, local_file, remote_file, server_ip)

        if trm_run:
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
            src_path = py_path + remote_file
            newdest_path = dest_path + remote_file
            move(src_path, newdest_path)

        return True, True

    def move_core_files(self, output, server_ip, file_name):
        files = self.pw.get_value_by_offset(output, "Tarball Name:", 2)
        files = files.split(" ")

        py_path = None
        path_var = os.environ['PYTHONPATH'].split(os.pathsep)

        for path in path_var:
            if "SQA_ROBOT_AUTOMATION" in path:
                py_path = path
                break

        if py_path is None:
            py_path = "/home/administrator/Robot/SQA_ROBOT_AUTOMATION/"

        dest_path = os.path.join(py_path, "ExtremeAutomation/TRM_DATA/EXECUTE_GIT_Master/")

        for file_name in files:
            self.logger.log_info("Moving debug file " + file_name + " to Test Plan logging directory.")
            src_path = py_path + file_name
            ldest_path = dest_path + file_name
            move(src_path, ldest_path)

        return True, True

    def get_version_filename(self, output, version):
        primary_ver = self.pw.get_value_by_offset(output, "Primary ver:", 2)
        secondary_ver = self.pw.get_value_by_offset(output, "Secondary ver:", 2)

        if primary_ver.lower() == version.lower():
            filename = "primary"
        elif secondary_ver.lower() == version.lower():
            filename = "secondary"
        else:
            filename = None

        filename = filename
        if filename is not None:
            result = True
        else:
            result = False

        return result, filename

    def check_version_present(self, output, version):
        primary_ver = self.pw.get_value_by_offset(output, "Primary ver:", 2)
        secondary_ver = self.pw.get_value_by_offset(output, "Secondary ver:", 2)

        result = True if primary_ver.lower() == version or secondary_ver.lower() == version else False
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
            if args["config"] == config_file:
                return True, True
        return False, False
