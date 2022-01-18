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
        self.COPY_FILE = {"constant": "copy_file",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.copy_file}
        self.COPY_FILE_FROM_SERVER = {"constant": "copy_file_from_server",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.copy_file_from_server}
        self.DELETE_FILE = {"constant": "delete_file",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.delete_file}
        self.DELETE_FILE_ON_SLOT = {"constant": "delete_file_on_slot",
                                    "tags": ["COMMAND_CLI"],
                                    "link": self.link.delete_file_on_slot}
        self.GENERATE_SUPPORT_FILE = {"constant": "generate_support_file",
                                      "tags": ["COMMAND_CLI"],
                                      "link": self.link.generate_support_file}
        self.SAVE_CONFIG_TO_FILE = {"constant": "save_config_to_file",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.save_config_to_file}
        self.SAVE_CONFIG_TO_PRIMARY = {"constant": "save_config_to_primary",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.save_config_to_primary}
        self.SAVE_CONFIG_TO_SECONDARY = {"constant": "save_config_to_secondary",
                                         "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                         "link": self.link.save_config_to_secondary}
        self.SAVE_CURRENT_CONFIG = {"constant": "save_current_config",
                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                    "link": self.link.save_current_config}
        self.SET_SYSTEM_CONFIG = {"constant": "set_system_config",
                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                  "link": self.link.set_system_config}
        self.SET_SYSTEM_TO_BACKUP_CONFIG = {"constant": "set_system_to_backup_config",
                                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                            "link": self.link.set_system_to_backup_config}
        self.SET_SYSTEM_TO_PRIMARY_CONFIG = {"constant": "set_system_to_primary_config",
                                             "tags": ["COMMAND_CLI"],
                                             "link": self.link.set_system_to_primary_config}
        self.SHOW_CONFIG_FILES = {"constant": "show_config_files",
                                  "tags": ["COMMAND_CLI"],
                                  "link": self.link.show_config_files}
        self.SHOW_CONFIG_FILES_PER_SLOT = {"constant": "show_config_files_per_slot",
                                           "tags": ["COMMAND_CLI"],
                                           "link": self.link.show_config_files_per_slot}
        self.SHOW_DEFAULT_BOOT_CONFIG_FILE = {"constant": "show_default_boot_config_file",
                                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                              "link": self.link.show_default_boot_config_file}
        self.SHOW_LOGGING_FILES = {"constant": "show_logging_files",
                                   "tags": ["COMMAND_CLI"],
                                   "link": self.link.show_logging_files}
        self.UPLOAD_CORE_FILE = {"constant": "upload_core_file",
                                 "tags": ["COMMAND_CLI"],
                                 "link": self.link.upload_core_file}
        self.UPLOAD_FILE = {"constant": "upload_file",
                            "tags": ["COMMAND_CLI"],
                            "link": self.link.upload_file}
