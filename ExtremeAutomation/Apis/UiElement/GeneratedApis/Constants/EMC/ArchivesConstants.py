"""
This class outlines all the constants for the archives API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(ArchivesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class ArchivesConstants(ApiConstants):
    def __init__(self):
        super(ArchivesConstants, self).__init__()
        self.ARCHIVES_CLICK_CREATE = {"constant": "archives_click_create",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.archives_click_create}
        self.ARCHIVES_CLICK_REFRESH = {"constant": "archives_click_refresh",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.archives_click_refresh}
        self.ARCHIVES_CONFIRM_ARCHIVE_CONTAINS_DEVICES = {"constant": "archives_confirm_archive_contains_devices",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.archives_confirm_archive_contains_devices}
        self.ARCHIVES_CONFIRM_ARCHIVE_EXISTS = {"constant": "archives_confirm_archive_exists",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.archives_confirm_archive_exists}
        self.ARCHIVES_CONFIRM_ARCHIVE_VERSION_ABORTED = {"constant": "archives_confirm_archive_version_aborted",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.archives_confirm_archive_version_aborted}
        self.ARCHIVES_CONFIRM_ARCHIVE_VERSION_COUNT = {"constant": "archives_confirm_archive_version_count",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.archives_confirm_archive_version_count}
        self.ARCHIVES_CONFIRM_ARCHIVE_VERSION_SUCCESS = {"constant": "archives_confirm_archive_version_success",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.archives_confirm_archive_version_success}
        self.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_ABORT_ON_FAILURE = {"constant": "archives_confirm_details_archive_abort_on_failure",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.archives_confirm_details_archive_abort_on_failure}
        self.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_CAPACITY_PLANNING = {"constant": "archives_confirm_details_archive_capacity_planning",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.archives_confirm_details_archive_capacity_planning}
        self.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_CONFIGURATION_DATA = {"constant": "archives_confirm_details_archive_configuration_data",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.archives_confirm_details_archive_configuration_data}
        self.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_DATE = {"constant": "archives_confirm_details_archive_date",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.archives_confirm_details_archive_date}
        self.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_DESCRIPTION = {"constant": "archives_confirm_details_archive_description",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.archives_confirm_details_archive_description}
        self.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_DESCRIPTION_CONTAINS = {"constant": "archives_confirm_details_archive_description_contains",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.archives_confirm_details_archive_description_contains}
        self.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_FREQUENCY = {"constant": "archives_confirm_details_archive_frequency",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.archives_confirm_details_archive_frequency}
        self.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_IPS_ENABLED = {"constant": "archives_confirm_details_archive_ips_enabled",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.archives_confirm_details_archive_ips_enabled}
        self.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_MAX_VERSIONS_UNLIMITED = {"constant": "archives_confirm_details_archive_max_versions_unlimited",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.archives_confirm_details_archive_max_versions_unlimited}
        self.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_MAX_VERSIONS_VALUE = {"constant": "archives_confirm_details_archive_max_versions_value",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.archives_confirm_details_archive_max_versions_value}
        self.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_NAME = {"constant": "archives_confirm_details_archive_name",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.archives_confirm_details_archive_name}
        self.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_PROCESS_GROUPS = {"constant": "archives_confirm_details_archive_process_groups",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.archives_confirm_details_archive_process_groups}
        self.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_REGIME = {"constant": "archives_confirm_details_archive_regime",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.archives_confirm_details_archive_regime}
        self.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_RUN_GOVERNANCE = {"constant": "archives_confirm_details_archive_run_governance",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.archives_confirm_details_archive_run_governance}
        self.ARCHIVES_CONFIRM_DETAILS_ARCHIVE_START_TIME = {"constant": "archives_confirm_details_archive_start_time",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.archives_confirm_details_archive_start_time}
        self.ARCHIVES_CONFIRM_DETAILS_DEVICE_DESCRIPTION = {"constant": "archives_confirm_details_device_description",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.archives_confirm_details_device_description}
        self.ARCHIVES_CONFIRM_DETAILS_DEVICE_DESCRIPTION_CONTAINS = {"constant": "archives_confirm_details_device_description_contains",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.archives_confirm_details_device_description_contains}
        self.ARCHIVES_CONFIRM_DETAILS_VERSION_ABORTED_COUNT = {"constant": "archives_confirm_details_version_aborted_count",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.archives_confirm_details_version_aborted_count}
        self.ARCHIVES_CONFIRM_DETAILS_VERSION_DESCRIPTION = {"constant": "archives_confirm_details_version_description",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.archives_confirm_details_version_description}
        self.ARCHIVES_CONFIRM_DETAILS_VERSION_DESCRIPTION_CONTAINS = {"constant": "archives_confirm_details_version_description_contains",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.archives_confirm_details_version_description_contains}
        self.ARCHIVES_CONFIRM_DETAILS_VERSION_DEVICE_COUNT = {"constant": "archives_confirm_details_version_device_count",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.archives_confirm_details_version_device_count}
        self.ARCHIVES_CONFIRM_DETAILS_VERSION_DIFFERENT_COUNT = {"constant": "archives_confirm_details_version_different_count",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.archives_confirm_details_version_different_count}
        self.ARCHIVES_CONFIRM_DETAILS_VERSION_FAILED_COUNT = {"constant": "archives_confirm_details_version_failed_count",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.archives_confirm_details_version_failed_count}
        self.ARCHIVES_CONFIRM_DETAILS_VERSION_LOCKED = {"constant": "archives_confirm_details_version_locked",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.archives_confirm_details_version_locked}
        self.ARCHIVES_CONFIRM_DETAILS_VERSION_SUCCESS_COUNT = {"constant": "archives_confirm_details_version_success_count",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.archives_confirm_details_version_success_count}
        self.ARCHIVES_DETAILS_ARCHIVE_CLICK_CONFIGURE_DEVICES = {"constant": "archives_details_archive_click_configure_devices",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.archives_details_archive_click_configure_devices}
        self.ARCHIVES_DETAILS_ARCHIVE_SELECT_REGIME = {"constant": "archives_details_archive_select_regime",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.archives_details_archive_select_regime}
        self.ARCHIVES_DETAILS_ARCHIVE_SET_ABORT_ON_FAILURE = {"constant": "archives_details_archive_set_abort_on_failure",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.archives_details_archive_set_abort_on_failure}
        self.ARCHIVES_DETAILS_ARCHIVE_SET_ARCHIVE_CAPACITY_PLANNING_DATA = {"constant": "archives_details_archive_set_archive_capacity_planning_data",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.archives_details_archive_set_archive_capacity_planning_data}
        self.ARCHIVES_DETAILS_ARCHIVE_SET_ARCHIVE_CONFIGURATION_DATA = {"constant": "archives_details_archive_set_archive_configuration_data",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.archives_details_archive_set_archive_configuration_data}
        self.ARCHIVES_DETAILS_ARCHIVE_SET_DATE = {"constant": "archives_details_archive_set_date",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.archives_details_archive_set_date}
        self.ARCHIVES_DETAILS_ARCHIVE_SET_DESCRIPTION = {"constant": "archives_details_archive_set_description",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.archives_details_archive_set_description}
        self.ARCHIVES_DETAILS_ARCHIVE_SET_FREQUENCY = {"constant": "archives_details_archive_set_frequency",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.archives_details_archive_set_frequency}
        self.ARCHIVES_DETAILS_ARCHIVE_SET_IPS_DISABLED = {"constant": "archives_details_archive_set_ips_disabled",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.archives_details_archive_set_ips_disabled}
        self.ARCHIVES_DETAILS_ARCHIVE_SET_IPS_ENABLED = {"constant": "archives_details_archive_set_ips_enabled",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.archives_details_archive_set_ips_enabled}
        self.ARCHIVES_DETAILS_ARCHIVE_SET_MAX_VERSIONS_UNLIMITED = {"constant": "archives_details_archive_set_max_versions_unlimited",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.archives_details_archive_set_max_versions_unlimited}
        self.ARCHIVES_DETAILS_ARCHIVE_SET_MAX_VERSIONS_VALUE = {"constant": "archives_details_archive_set_max_versions_value",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.archives_details_archive_set_max_versions_value}
        self.ARCHIVES_DETAILS_ARCHIVE_SET_PROCESS_GROUPS = {"constant": "archives_details_archive_set_process_groups",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.archives_details_archive_set_process_groups}
        self.ARCHIVES_DETAILS_ARCHIVE_SET_RUN_GOVERNANCE = {"constant": "archives_details_archive_set_run_governance",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.archives_details_archive_set_run_governance}
        self.ARCHIVES_DETAILS_ARCHIVE_SET_START_TIME = {"constant": "archives_details_archive_set_start_time",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.archives_details_archive_set_start_time}
        self.ARCHIVES_DETAILS_CLICK_SAVE = {"constant": "archives_details_click_save",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.archives_details_click_save}
        self.ARCHIVES_DETAILS_DEVICE_SET_MEMO = {"constant": "archives_details_device_set_memo",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.archives_details_device_set_memo}
        self.ARCHIVES_DETAILS_SELECT_TAB = {"constant": "archives_details_select_tab",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.archives_details_select_tab}
        self.ARCHIVES_DETAILS_VERSION_SET_DESCRIPTION = {"constant": "archives_details_version_set_description",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.archives_details_version_set_description}
        self.ARCHIVES_DETAILS_VERSION_SET_LOCKED = {"constant": "archives_details_version_set_locked",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.archives_details_version_set_locked}
        self.ARCHIVES_DIALOG_CONFIGURE_DEVICES_ADD_ARCHIVE_MEMBER_DEVICE = {"constant": "archives_dialog_configure_devices_add_archive_member_device",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.archives_dialog_configure_devices_add_archive_member_device}
        self.ARCHIVES_DIALOG_CONFIGURE_DEVICES_ADD_ARCHIVE_MEMBER_GROUP = {"constant": "archives_dialog_configure_devices_add_archive_member_group",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.archives_dialog_configure_devices_add_archive_member_group}
        self.ARCHIVES_DIALOG_CONFIGURE_DEVICES_CLICK_CANCEL = {"constant": "archives_dialog_configure_devices_click_cancel",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.archives_dialog_configure_devices_click_cancel}
        self.ARCHIVES_DIALOG_CONFIGURE_DEVICES_CLICK_OK = {"constant": "archives_dialog_configure_devices_click_ok",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.archives_dialog_configure_devices_click_ok}
        self.ARCHIVES_DIALOG_CONFIGURE_DEVICES_REMOVE_ARCHIVE_MEMBER_DEVICE = {"constant": "archives_dialog_configure_devices_remove_archive_member_device",
                                                                               "tags": ["COMMAND_SELENIUM"],
                                                                               "link": self.link.archives_dialog_configure_devices_remove_archive_member_device}
        self.ARCHIVES_DIALOG_CONFIGURE_DEVICES_REMOVE_ARCHIVE_MEMBER_GROUP = {"constant": "archives_dialog_configure_devices_remove_archive_member_group",
                                                                              "tags": ["COMMAND_SELENIUM"],
                                                                              "link": self.link.archives_dialog_configure_devices_remove_archive_member_group}
        self.ARCHIVES_DIALOG_CONFIRM_DELETE_ARCHIVE_CLICK_NO = {"constant": "archives_dialog_confirm_delete_archive_click_no",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.archives_dialog_confirm_delete_archive_click_no}
        self.ARCHIVES_DIALOG_CONFIRM_DELETE_ARCHIVE_CLICK_YES = {"constant": "archives_dialog_confirm_delete_archive_click_yes",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.archives_dialog_confirm_delete_archive_click_yes}
        self.ARCHIVES_DIALOG_CONFIRM_DELETE_DEVICE_CLICK_NO = {"constant": "archives_dialog_confirm_delete_device_click_no",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.archives_dialog_confirm_delete_device_click_no}
        self.ARCHIVES_DIALOG_CONFIRM_DELETE_DEVICE_CLICK_YES = {"constant": "archives_dialog_confirm_delete_device_click_yes",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.archives_dialog_confirm_delete_device_click_yes}
        self.ARCHIVES_DIALOG_CONFIRM_DELETE_VERSION_CLICK_NO = {"constant": "archives_dialog_confirm_delete_version_click_no",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.archives_dialog_confirm_delete_version_click_no}
        self.ARCHIVES_DIALOG_CONFIRM_DELETE_VERSION_CLICK_YES = {"constant": "archives_dialog_confirm_delete_version_click_yes",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.archives_dialog_confirm_delete_version_click_yes}
        self.ARCHIVES_DIALOG_CREATE_ADD_ARCHIVE_MEMBER_DEVICE = {"constant": "archives_dialog_create_add_archive_member_device",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.archives_dialog_create_add_archive_member_device}
        self.ARCHIVES_DIALOG_CREATE_ADD_ARCHIVE_MEMBER_GROUP = {"constant": "archives_dialog_create_add_archive_member_group",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.archives_dialog_create_add_archive_member_group}
        self.ARCHIVES_DIALOG_CREATE_CLICK_CANCEL = {"constant": "archives_dialog_create_click_cancel",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.archives_dialog_create_click_cancel}
        self.ARCHIVES_DIALOG_CREATE_CLICK_FINISH = {"constant": "archives_dialog_create_click_finish",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.archives_dialog_create_click_finish}
        self.ARCHIVES_DIALOG_CREATE_CLICK_NEXT = {"constant": "archives_dialog_create_click_next",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.archives_dialog_create_click_next}
        self.ARCHIVES_DIALOG_CREATE_CLICK_PREVIOUS = {"constant": "archives_dialog_create_click_previous",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.archives_dialog_create_click_previous}
        self.ARCHIVES_DIALOG_CREATE_REMOVE_ARCHIVE_MEMBER_DEVICE = {"constant": "archives_dialog_create_remove_archive_member_device",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.archives_dialog_create_remove_archive_member_device}
        self.ARCHIVES_DIALOG_CREATE_REMOVE_ARCHIVE_MEMBER_GROUP = {"constant": "archives_dialog_create_remove_archive_member_group",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.archives_dialog_create_remove_archive_member_group}
        self.ARCHIVES_DIALOG_CREATE_SET_ABORT_ON_FAILURE = {"constant": "archives_dialog_create_set_abort_on_failure",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.archives_dialog_create_set_abort_on_failure}
        self.ARCHIVES_DIALOG_CREATE_SET_ARCHIVE_CAPACITY_PLANNING_DATA = {"constant": "archives_dialog_create_set_archive_capacity_planning_data",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.archives_dialog_create_set_archive_capacity_planning_data}
        self.ARCHIVES_DIALOG_CREATE_SET_ARCHIVE_CONFIGURATION_DATA = {"constant": "archives_dialog_create_set_archive_configuration_data",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.archives_dialog_create_set_archive_configuration_data}
        self.ARCHIVES_DIALOG_CREATE_SET_DATE = {"constant": "archives_dialog_create_set_date",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.archives_dialog_create_set_date}
        self.ARCHIVES_DIALOG_CREATE_SET_DESCRIPTION = {"constant": "archives_dialog_create_set_description",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.archives_dialog_create_set_description}
        self.ARCHIVES_DIALOG_CREATE_SET_FREQUENCY = {"constant": "archives_dialog_create_set_frequency",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.archives_dialog_create_set_frequency}
        self.ARCHIVES_DIALOG_CREATE_SET_IPS_DISABLED = {"constant": "archives_dialog_create_set_ips_disabled",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.archives_dialog_create_set_ips_disabled}
        self.ARCHIVES_DIALOG_CREATE_SET_IP_SORT_ASCENDING = {"constant": "archives_dialog_create_set_ip_sort_ascending",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.archives_dialog_create_set_ip_sort_ascending}
        self.ARCHIVES_DIALOG_CREATE_SET_IP_SORT_DESCENDING = {"constant": "archives_dialog_create_set_ip_sort_descending",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.archives_dialog_create_set_ip_sort_descending}
        self.ARCHIVES_DIALOG_CREATE_SET_MAX_VERSIONS_UNLIMITED = {"constant": "archives_dialog_create_set_max_versions_unlimited",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.archives_dialog_create_set_max_versions_unlimited}
        self.ARCHIVES_DIALOG_CREATE_SET_MAX_VERSIONS_VALUE = {"constant": "archives_dialog_create_set_max_versions_value",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.archives_dialog_create_set_max_versions_value}
        self.ARCHIVES_DIALOG_CREATE_SET_NAME = {"constant": "archives_dialog_create_set_name",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.archives_dialog_create_set_name}
        self.ARCHIVES_DIALOG_CREATE_SET_PROCESS_GROUPS = {"constant": "archives_dialog_create_set_process_groups",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.archives_dialog_create_set_process_groups}
        self.ARCHIVES_DIALOG_CREATE_SET_START_TIME = {"constant": "archives_dialog_create_set_start_time",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.archives_dialog_create_set_start_time}
        self.ARCHIVES_DIALOG_RENAME_CLICK_CANCEL = {"constant": "archives_dialog_rename_click_cancel",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.archives_dialog_rename_click_cancel}
        self.ARCHIVES_DIALOG_RENAME_CLICK_OK = {"constant": "archives_dialog_rename_click_ok",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.archives_dialog_rename_click_ok}
        self.ARCHIVES_DIALOG_RENAME_SET_NAME = {"constant": "archives_dialog_rename_set_name",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.archives_dialog_rename_set_name}
        self.ARCHIVES_DIALOG_VIEW_CONFIG_CLICK_CLOSE = {"constant": "archives_dialog_view_config_click_close",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.archives_dialog_view_config_click_close}
        self.ARCHIVES_DIALOG_VIEW_CONFIG_FILE_FIND = {"constant": "archives_dialog_view_config_file_find",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.archives_dialog_view_config_file_find}
        self.ARCHIVES_DIALOG_VIEW_CONFIG_FILE_FIND_IN_NAMED_BLOCK = {"constant": "archives_dialog_view_config_file_find_in_named_block",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.archives_dialog_view_config_file_find_in_named_block}
        self.ARCHIVES_DIALOG_VIEW_CONFIG_FILE_LINE_CONTAINS = {"constant": "archives_dialog_view_config_file_line_contains",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.archives_dialog_view_config_file_line_contains}
        self.ARCHIVES_TABLE_DELETE_ARCHIVE = {"constant": "archives_table_delete_archive",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.archives_table_delete_archive}
        self.ARCHIVES_TABLE_DELETE_NEWEST_ARCHIVE_VERSION = {"constant": "archives_table_delete_newest_archive_version",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.archives_table_delete_newest_archive_version}
        self.ARCHIVES_TABLE_DELETE_NEWEST_ARCHIVE_VERSION_DEVICE = {"constant": "archives_table_delete_newest_archive_version_device",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.archives_table_delete_newest_archive_version_device}
        self.ARCHIVES_TABLE_DELETE_OLDEST_ARCHIVE_VERSION = {"constant": "archives_table_delete_oldest_archive_version",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.archives_table_delete_oldest_archive_version}
        self.ARCHIVES_TABLE_DELETE_OLDEST_ARCHIVE_VERSION_DEVICE = {"constant": "archives_table_delete_oldest_archive_version_device",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.archives_table_delete_oldest_archive_version_device}
        self.ARCHIVES_TABLE_LOCK_NEWEST_ARCHIVE_VERSION = {"constant": "archives_table_lock_newest_archive_version",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.archives_table_lock_newest_archive_version}
        self.ARCHIVES_TABLE_LOCK_OLDEST_ARCHIVE_VERSION = {"constant": "archives_table_lock_oldest_archive_version",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.archives_table_lock_oldest_archive_version}
        self.ARCHIVES_TABLE_RENAME_ARCHIVE = {"constant": "archives_table_rename_archive",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.archives_table_rename_archive}
        self.ARCHIVES_TABLE_RESTORE_NEWEST_ARCHIVE_VERSION = {"constant": "archives_table_restore_newest_archive_version",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.archives_table_restore_newest_archive_version}
        self.ARCHIVES_TABLE_RESTORE_NEWEST_ARCHIVE_VERSION_DEVICE = {"constant": "archives_table_restore_newest_archive_version_device",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.archives_table_restore_newest_archive_version_device}
        self.ARCHIVES_TABLE_RESTORE_OLDEST_ARCHIVE_VERSION = {"constant": "archives_table_restore_oldest_archive_version",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.archives_table_restore_oldest_archive_version}
        self.ARCHIVES_TABLE_RESTORE_OLDEST_ARCHIVE_VERSION_DEVICE = {"constant": "archives_table_restore_oldest_archive_version_device",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.archives_table_restore_oldest_archive_version_device}
        self.ARCHIVES_TABLE_SELECT_ARCHIVE = {"constant": "archives_table_select_archive",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.archives_table_select_archive}
        self.ARCHIVES_TABLE_STAMP_NEW_VERSION = {"constant": "archives_table_stamp_new_version",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.archives_table_stamp_new_version}
        self.ARCHIVES_TABLE_UNLOCK_NEWEST_ARCHIVE_VERSION = {"constant": "archives_table_unlock_newest_archive_version",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.archives_table_unlock_newest_archive_version}
        self.ARCHIVES_TABLE_UNLOCK_OLDEST_ARCHIVE_VERSION = {"constant": "archives_table_unlock_oldest_archive_version",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.archives_table_unlock_oldest_archive_version}
        self.ARCHIVES_TREE_COLLAPSE_NEWEST_ARCHIVE_VERSION = {"constant": "archives_tree_collapse_newest_archive_version",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.archives_tree_collapse_newest_archive_version}
        self.ARCHIVES_TREE_COLLAPSE_NODE = {"constant": "archives_tree_collapse_node",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.archives_tree_collapse_node}
        self.ARCHIVES_TREE_COLLAPSE_OLDEST_ARCHIVE_VERSION = {"constant": "archives_tree_collapse_oldest_archive_version",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.archives_tree_collapse_oldest_archive_version}
        self.ARCHIVES_TREE_CREATE = {"constant": "archives_tree_create",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.archives_tree_create}
        self.ARCHIVES_TREE_DELETE_ARCHIVE = {"constant": "archives_tree_delete_archive",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.archives_tree_delete_archive}
        self.ARCHIVES_TREE_DELETE_NEWEST_ARCHIVE_VERSION = {"constant": "archives_tree_delete_newest_archive_version",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.archives_tree_delete_newest_archive_version}
        self.ARCHIVES_TREE_DELETE_NEWEST_ARCHIVE_VERSION_DEVICE = {"constant": "archives_tree_delete_newest_archive_version_device",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.archives_tree_delete_newest_archive_version_device}
        self.ARCHIVES_TREE_DELETE_OLDEST_ARCHIVE_VERSION = {"constant": "archives_tree_delete_oldest_archive_version",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.archives_tree_delete_oldest_archive_version}
        self.ARCHIVES_TREE_DELETE_OLDEST_ARCHIVE_VERSION_DEVICE = {"constant": "archives_tree_delete_oldest_archive_version_device",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.archives_tree_delete_oldest_archive_version_device}
        self.ARCHIVES_TREE_EXPAND_NEWEST_ARCHIVE_VERSION = {"constant": "archives_tree_expand_newest_archive_version",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.archives_tree_expand_newest_archive_version}
        self.ARCHIVES_TREE_EXPAND_NODE = {"constant": "archives_tree_expand_node",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.archives_tree_expand_node}
        self.ARCHIVES_TREE_EXPAND_OLDEST_ARCHIVE_VERSION = {"constant": "archives_tree_expand_oldest_archive_version",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.archives_tree_expand_oldest_archive_version}
        self.ARCHIVES_TREE_LOCK_NEWEST_ARCHIVE_VERSION = {"constant": "archives_tree_lock_newest_archive_version",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.archives_tree_lock_newest_archive_version}
        self.ARCHIVES_TREE_LOCK_OLDEST_ARCHIVE_VERSION = {"constant": "archives_tree_lock_oldest_archive_version",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.archives_tree_lock_oldest_archive_version}
        self.ARCHIVES_TREE_REFRESH = {"constant": "archives_tree_refresh",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.archives_tree_refresh}
        self.ARCHIVES_TREE_RENAME_ARCHIVE = {"constant": "archives_tree_rename_archive",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.archives_tree_rename_archive}
        self.ARCHIVES_TREE_RESTORE_NEWEST_ARCHIVE_VERSION = {"constant": "archives_tree_restore_newest_archive_version",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.archives_tree_restore_newest_archive_version}
        self.ARCHIVES_TREE_RESTORE_NEWEST_ARCHIVE_VERSION_DEVICE = {"constant": "archives_tree_restore_newest_archive_version_device",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.archives_tree_restore_newest_archive_version_device}
        self.ARCHIVES_TREE_RESTORE_OLDEST_ARCHIVE_VERSION = {"constant": "archives_tree_restore_oldest_archive_version",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.archives_tree_restore_oldest_archive_version}
        self.ARCHIVES_TREE_RESTORE_OLDEST_ARCHIVE_VERSION_DEVICE = {"constant": "archives_tree_restore_oldest_archive_version_device",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.archives_tree_restore_oldest_archive_version_device}
        self.ARCHIVES_TREE_SELECT_NEWEST_ARCHIVE_VERSION = {"constant": "archives_tree_select_newest_archive_version",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.archives_tree_select_newest_archive_version}
        self.ARCHIVES_TREE_SELECT_NODE = {"constant": "archives_tree_select_node",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.archives_tree_select_node}
        self.ARCHIVES_TREE_SELECT_OLDEST_ARCHIVE_VERSION = {"constant": "archives_tree_select_oldest_archive_version",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.archives_tree_select_oldest_archive_version}
        self.ARCHIVES_TREE_STAMP_NEW_VERSION = {"constant": "archives_tree_stamp_new_version",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.archives_tree_stamp_new_version}
        self.ARCHIVES_TREE_UNLOCK_NEWEST_ARCHIVE_VERSION = {"constant": "archives_tree_unlock_newest_archive_version",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.archives_tree_unlock_newest_archive_version}
        self.ARCHIVES_TREE_UNLOCK_OLDEST_ARCHIVE_VERSION = {"constant": "archives_tree_unlock_oldest_archive_version",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.archives_tree_unlock_oldest_archive_version}
        self.ARCHIVES_TREE_VIEW_CONFIG_FILE = {"constant": "archives_tree_view_config_file",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.archives_tree_view_config_file}
