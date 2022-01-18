"""
This class outlines all the constants for the filemanagement API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(FilemanagementConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class FilemanagementConstants(ApiConstants):
    def __init__(self):
        super(FilemanagementConstants, self).__init__()
        self.CHECK_CONFIG_FILE_EXISTS = {"constant": "check_config_file_exists",
                                         "tags": ["PARSE_CLI"],
                                         "link": self.link.check_config_file_exists}
        self.CHECK_CONFIG_FILE_EXISTS_PER_SLOT = {"constant": "check_config_file_exists_per_slot",
                                                  "tags": ["PARSE_CLI"],
                                                  "link": self.link.check_config_file_exists_per_slot}
        self.CHECK_DEFAULT_BOOT_CONFIG_FILE = {"constant": "check_default_boot_config_file",
                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                               "link": self.link.check_default_boot_config_file}
        self.CHECK_PRIMARY_BACKUP_BOOT_CONFIG_FILE = {"constant": "check_primary_backup_boot_config_file",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.check_primary_backup_boot_config_file}
        self.CHECK_PRIMARY_BOOT_CONFIG_FILE = {"constant": "check_primary_boot_config_file",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.check_primary_boot_config_file}
        self.CHECK_VERSION_PRESENT = {"constant": "check_version_present",
                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                      "link": self.link.check_version_present}
        self.GET_LOGFILE_LIST = {"constant": "get_logfile_list",
                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                 "link": self.link.get_logfile_list}
        self.GET_UNUSED_IMAGENAME = {"constant": "get_unused_imagename",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.get_unused_imagename}
        self.GET_VERSION_FILENAME = {"constant": "get_version_filename",
                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                     "link": self.link.get_version_filename}
        self.MOVE_CORE_FILES = {"constant": "move_core_files",
                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                "link": self.link.move_core_files}
