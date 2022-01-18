"""
This class outlines all the constants for the options API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(OptionsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class OptionsConstants(ApiConstants):
    def __init__(self):
        super(OptionsConstants, self).__init__()
        self.OPTIONS_COLLAPSE_OPTION = {"constant": "options_collapse_option",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.options_collapse_option}
        self.OPTIONS_EXPAND_OPTION = {"constant": "options_expand_option",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.options_expand_option}
        self.OPTIONS_RESET = {"constant": "options_reset",
                              "tags": ["COMMAND_SELENIUM"],
                              "link": self.link.options_reset}
        self.OPTIONS_RESTORE_DEFAULTS = {"constant": "options_restore_defaults",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.options_restore_defaults}
        self.OPTIONS_SAVE = {"constant": "options_save",
                             "tags": ["COMMAND_SELENIUM"],
                             "link": self.link.options_save}
        self.OPTIONS_SELECT_OPTION = {"constant": "options_select_option",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.options_select_option}
        self.OPTIONS_SET_ACCESS_CONTROL_COLLECTION_POLL_RATE = {"constant": "options_set_access_control_collection_poll_rate",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.options_set_access_control_collection_poll_rate}
        self.OPTIONS_SET_DB_BACKUP_FILE_PATH = {"constant": "options_set_db_backup_file_path",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.options_set_db_backup_file_path}
        self.OPTIONS_SET_DB_BACKUP_INCLUDE_ADDITIONAL_DATA = {"constant": "options_set_db_backup_include_additional_data",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.options_set_db_backup_include_additional_data}
        self.OPTIONS_SET_DB_BACKUP_SCHEDULE_FILE_FORMAT = {"constant": "options_set_db_backup_schedule_file_format",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.options_set_db_backup_schedule_file_format}
        self.OPTIONS_SET_DB_BACKUP_SCHEDULE_LIMIT_BACKUPS = {"constant": "options_set_db_backup_schedule_limit_backups",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.options_set_db_backup_schedule_limit_backups}
        self.OPTIONS_SET_DB_BACKUP_SCHEDULE_OCCURRENCE = {"constant": "options_set_db_backup_schedule_occurrence",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.options_set_db_backup_schedule_occurrence}
        self.OPTIONS_SET_DEVICE_COLLECTION_POLL_RATE = {"constant": "options_set_device_collection_poll_rate",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.options_set_device_collection_poll_rate}
        self.OPTIONS_SET_DEVICE_TREE_NAME_FORMAT = {"constant": "options_set_device_tree_name_format",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.options_set_device_tree_name_format}
        self.OPTIONS_SET_EXTREME_NETWORKS_UPDATES_CREDENTIALS = {"constant": "options_set_extreme_networks_updates_credentials",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.options_set_extreme_networks_updates_credentials}
        self.OPTIONS_SET_FTP_FILE_TRANSFER = {"constant": "options_set_ftp_file_transfer",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.options_set_ftp_file_transfer}
        self.OPTIONS_SET_INTERFACE_COLLECTION_POLL_RATE = {"constant": "options_set_interface_collection_poll_rate",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.options_set_interface_collection_poll_rate}
        self.OPTIONS_SET_SCP_FILE_TRANSFER = {"constant": "options_set_scp_file_transfer",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.options_set_scp_file_transfer}
        self.OPTIONS_SET_SFTP_FILE_TRANSFER = {"constant": "options_set_sftp_file_transfer",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.options_set_sftp_file_transfer}
        self.OPTIONS_SET_SITE_SHOW_VLAN_UNTAGGED = {"constant": "options_set_site_show_vlan_untagged",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.options_set_site_show_vlan_untagged}
        self.OPTIONS_SET_STATUS_POLLING_DEFAULT_GROUP = {"constant": "options_set_status_polling_default_group",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.options_set_status_polling_default_group}
        self.OPTIONS_SET_STATUS_POLLING_POLL_GROUP_1 = {"constant": "options_set_status_polling_poll_group_1",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.options_set_status_polling_poll_group_1}
        self.OPTIONS_SET_STATUS_POLLING_POLL_GROUP_2 = {"constant": "options_set_status_polling_poll_group_2",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.options_set_status_polling_poll_group_2}
        self.OPTIONS_SET_STATUS_POLLING_POLL_GROUP_3 = {"constant": "options_set_status_polling_poll_group_3",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.options_set_status_polling_poll_group_3}
        self.OPTIONS_SET_SYSLOG_ENGINE_DELAY_START = {"constant": "options_set_syslog_engine_delay_start",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.options_set_syslog_engine_delay_start}
        self.OPTIONS_SET_TFTP_FILE_TRANSFER = {"constant": "options_set_tftp_file_transfer",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.options_set_tftp_file_transfer}
        self.OPTIONS_SET_TRAP_ENGINE_DELAY_START = {"constant": "options_set_trap_engine_delay_start",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.options_set_trap_engine_delay_start}
        self.OPTIONS_SET_TRAP_SNMPV1_CREDENTIAL_NAME = {"constant": "options_set_trap_snmpv1_credential_name",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.options_set_trap_snmpv1_credential_name}
        self.OPTIONS_SET_TRAP_SNMPV2_CREDENTIAL_NAME = {"constant": "options_set_trap_snmpv2_credential_name",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.options_set_trap_snmpv2_credential_name}
        self.OPTIONS_SET_TRAP_SNMPV3_CREDENTIAL_NAME = {"constant": "options_set_trap_snmpv3_credential_name",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.options_set_trap_snmpv3_credential_name}
        self.OPTIONS_SET_WEB_SERVER_TIMEOUT = {"constant": "options_set_web_server_timeout",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.options_set_web_server_timeout}
        self.OPTIONS_SET_WIRELESS_COLLECTION_ACCESS_POINT_POLL_RATE = {"constant": "options_set_wireless_collection_access_point_poll_rate",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.options_set_wireless_collection_access_point_poll_rate}
        self.OPTIONS_SET_WIRELESS_COLLECTION_CONTROLLER_POLL_RATE = {"constant": "options_set_wireless_collection_controller_poll_rate",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.options_set_wireless_collection_controller_poll_rate}
        self.OPTIONS_SITE_SET_LENGTH_OF_SNMP_TIMEOUT = {"constant": "options_site_set_length_of_snmp_timeout",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.options_site_set_length_of_snmp_timeout}
        self.OPTIONS_SITE_SET_NUMBER_OF_SNMP_RETRIES = {"constant": "options_site_set_number_of_snmp_retries",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.options_site_set_number_of_snmp_retries}
