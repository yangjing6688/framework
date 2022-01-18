"""
This class outlines all the constants for the firmware API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(FirmwareConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class FirmwareConstants(ApiConstants):
    def __init__(self):
        super(FirmwareConstants, self).__init__()
        self.FIRMWARE_CONFIRM_CONFIG_FW_MENU_ENABLED = {"constant": "firmware_confirm_config_fw_menu_enabled",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.firmware_confirm_config_fw_menu_enabled}
        self.FIRMWARE_CONFIRM_CONFIG_FW_MENU_EXISTS = {"constant": "firmware_confirm_config_fw_menu_exists",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.firmware_confirm_config_fw_menu_exists}
        self.FIRMWARE_CONFIRM_UPGRADE_SUCCESS = {"constant": "firmware_confirm_upgrade_success",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.firmware_confirm_upgrade_success}
        self.FIRMWARE_DIALOG_ASSIGN_IMAGE_CLICK_CANCEL = {"constant": "firmware_dialog_assign_image_click_cancel",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.firmware_dialog_assign_image_click_cancel}
        self.FIRMWARE_DIALOG_ASSIGN_IMAGE_CLICK_OK = {"constant": "firmware_dialog_assign_image_click_ok",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.firmware_dialog_assign_image_click_ok}
        self.FIRMWARE_DIALOG_ASSIGN_IMAGE_CLICK_REFRESH = {"constant": "firmware_dialog_assign_image_click_refresh",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.firmware_dialog_assign_image_click_refresh}
        self.FIRMWARE_DIALOG_ASSIGN_IMAGE_SELECT_IMAGE = {"constant": "firmware_dialog_assign_image_select_image",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.firmware_dialog_assign_image_select_image}
        self.FIRMWARE_DIALOG_ASSIGN_IMAGE_SET_BOOTPROM_DOWNLOAD = {"constant": "firmware_dialog_assign_image_set_bootprom_download",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.firmware_dialog_assign_image_set_bootprom_download}
        self.FIRMWARE_DIALOG_ASSIGN_IMAGE_SET_SHOW_ALL_IMAGES = {"constant": "firmware_dialog_assign_image_set_show_all_images",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.firmware_dialog_assign_image_set_show_all_images}
        self.FIRMWARE_DIALOG_COMPARE_LAST_CONFIGS_CLICK_OK = {"constant": "firmware_dialog_compare_last_configs_click_ok",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.firmware_dialog_compare_last_configs_click_ok}
        self.FIRMWARE_DIALOG_CONFIGURATION_CLICK_CANCEL = {"constant": "firmware_dialog_configuration_click_cancel",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.firmware_dialog_configuration_click_cancel}
        self.FIRMWARE_DIALOG_CONFIGURATION_CLICK_OK = {"constant": "firmware_dialog_configuration_click_ok",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.firmware_dialog_configuration_click_ok}
        self.FIRMWARE_DIALOG_CONFIGURATION_CLICK_VIEW = {"constant": "firmware_dialog_configuration_click_view",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.firmware_dialog_configuration_click_view}
        self.FIRMWARE_DIALOG_CONFIGURATION_SET_CONFIGURATION_MIB = {"constant": "firmware_dialog_configuration_set_configuration_mib",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.firmware_dialog_configuration_set_configuration_mib}
        self.FIRMWARE_DIALOG_CONFIGURATION_SET_FILE_TRANSFER_MODE = {"constant": "firmware_dialog_configuration_set_file_transfer_mode",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.firmware_dialog_configuration_set_file_transfer_mode}
        self.FIRMWARE_DIALOG_CONFIGURATION_SET_FIRMWARE_MIB = {"constant": "firmware_dialog_configuration_set_firmware_mib",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.firmware_dialog_configuration_set_firmware_mib}
        self.FIRMWARE_DIALOG_CONFIGURATION_SET_SCRIPT_FILE_NAME = {"constant": "firmware_dialog_configuration_set_script_file_name",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.firmware_dialog_configuration_set_script_file_name}
        self.FIRMWARE_DIALOG_CONFIGURATION_SET_SERVER = {"constant": "firmware_dialog_configuration_set_server",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.firmware_dialog_configuration_set_server}
        self.FIRMWARE_DIALOG_CONFIGURATION_VIEW_CLICK_OK = {"constant": "firmware_dialog_configuration_view_click_ok",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.firmware_dialog_configuration_view_click_ok}
        self.FIRMWARE_DIALOG_CURRENT_FIRMWARE_RELEASES_CLICK_OK = {"constant": "firmware_dialog_current_firmware_releases_click_ok",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.firmware_dialog_current_firmware_releases_click_ok}
        self.FIRMWARE_DIALOG_RESTART_CLICK_ABORT = {"constant": "firmware_dialog_restart_click_abort",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.firmware_dialog_restart_click_abort}
        self.FIRMWARE_DIALOG_RESTART_CLICK_CANCEL = {"constant": "firmware_dialog_restart_click_cancel",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.firmware_dialog_restart_click_cancel}
        self.FIRMWARE_DIALOG_RESTART_CLICK_REFRESH = {"constant": "firmware_dialog_restart_click_refresh",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.firmware_dialog_restart_click_refresh}
        self.FIRMWARE_DIALOG_RESTART_CLICK_START = {"constant": "firmware_dialog_restart_click_start",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.firmware_dialog_restart_click_start}
        self.FIRMWARE_DIALOG_RESTART_CONFIRM_TIMED_RESTART_SUPPORTED = {"constant": "firmware_dialog_restart_confirm_timed_restart_supported",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.firmware_dialog_restart_confirm_timed_restart_supported}
        self.FIRMWARE_DIALOG_RESTART_SET_DEVICE_SELECTED = {"constant": "firmware_dialog_restart_set_device_selected",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.firmware_dialog_restart_set_device_selected}
        self.FIRMWARE_DIALOG_RESTART_SET_RESTART_TIME = {"constant": "firmware_dialog_restart_set_restart_time",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.firmware_dialog_restart_set_restart_time}
        self.FIRMWARE_DIALOG_RESTART_SET_SHOW_DEVICES_NOT_SUPPORTING_TIMED_RESTART = {"constant": "firmware_dialog_restart_set_show_devices_not_supporting_timed_restart",
                                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                                      "link": self.link.firmware_dialog_restart_set_show_devices_not_supporting_timed_restart}
        self.FIRMWARE_DIALOG_RESTORE_CLICK_CANCEL = {"constant": "firmware_dialog_restore_click_cancel",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.firmware_dialog_restore_click_cancel}
        self.FIRMWARE_DIALOG_RESTORE_CLICK_START = {"constant": "firmware_dialog_restore_click_start",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.firmware_dialog_restore_click_start}
        self.FIRMWARE_DIALOG_RESTORE_SELECT_CONFIGURATION_TO_CLONE = {"constant": "firmware_dialog_restore_select_configuration_to_clone",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.firmware_dialog_restore_select_configuration_to_clone}
        self.FIRMWARE_DIALOG_RESTORE_SELECT_CONFIGURATION_TO_CLONE_NEWEST = {"constant": "firmware_dialog_restore_select_configuration_to_clone_newest",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.firmware_dialog_restore_select_configuration_to_clone_newest}
        self.FIRMWARE_DIALOG_RESTORE_SELECT_CONFIGURATION_TO_CLONE_OLDEST = {"constant": "firmware_dialog_restore_select_configuration_to_clone_oldest",
                                                                             "tags": ["COMMAND_SELENIUM"],
                                                                             "link": self.link.firmware_dialog_restore_select_configuration_to_clone_oldest}
        self.FIRMWARE_DIALOG_RESTORE_SELECT_CONFIGURATION_TO_RESTORE = {"constant": "firmware_dialog_restore_select_configuration_to_restore",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.firmware_dialog_restore_select_configuration_to_restore}
        self.FIRMWARE_DIALOG_RESTORE_SELECT_CONFIGURATION_TO_RESTORE_NEWEST = {"constant": "firmware_dialog_restore_select_configuration_to_restore_newest",
                                                                               "tags": ["COMMAND_SELENIUM"],
                                                                               "link": self.link.firmware_dialog_restore_select_configuration_to_restore_newest}
        self.FIRMWARE_DIALOG_RESTORE_SELECT_CONFIGURATION_TO_RESTORE_OLDEST = {"constant": "firmware_dialog_restore_select_configuration_to_restore_oldest",
                                                                               "tags": ["COMMAND_SELENIUM"],
                                                                               "link": self.link.firmware_dialog_restore_select_configuration_to_restore_oldest}
        self.FIRMWARE_DIALOG_RESTORE_SELECT_PROFILE = {"constant": "firmware_dialog_restore_select_profile",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.firmware_dialog_restore_select_profile}
        self.FIRMWARE_DIALOG_RESTORE_SELECT_SOURCE_DEVICE = {"constant": "firmware_dialog_restore_select_source_device",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.firmware_dialog_restore_select_source_device}
        self.FIRMWARE_DIALOG_RESTORE_SELECT_TAB = {"constant": "firmware_dialog_restore_select_tab",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.firmware_dialog_restore_select_tab}
        self.FIRMWARE_DIALOG_RESTORE_SELECT_TEMPLATE = {"constant": "firmware_dialog_restore_select_template",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.firmware_dialog_restore_select_template}
        self.FIRMWARE_DIALOG_SERIAL_NUMBERS_CLICK_CANCEL = {"constant": "firmware_dialog_serial_numbers_click_cancel",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.firmware_dialog_serial_numbers_click_cancel}
        self.FIRMWARE_DIALOG_SERIAL_NUMBERS_CLICK_EXPORT_TO_FILE = {"constant": "firmware_dialog_serial_numbers_click_export_to_file",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.firmware_dialog_serial_numbers_click_export_to_file}
        self.FIRMWARE_DIALOG_SERIAL_NUMBERS_CLICK_REGISTER = {"constant": "firmware_dialog_serial_numbers_click_register",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.firmware_dialog_serial_numbers_click_register}
        self.FIRMWARE_DIALOG_SERIAL_NUMBERS_REGISTER_CLICK_CANCEL = {"constant": "firmware_dialog_serial_numbers_register_click_cancel",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.firmware_dialog_serial_numbers_register_click_cancel}
        self.FIRMWARE_DIALOG_SERIAL_NUMBERS_REGISTER_CLICK_REGISTER = {"constant": "firmware_dialog_serial_numbers_register_click_register",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.firmware_dialog_serial_numbers_register_click_register}
        self.FIRMWARE_DIALOG_SERIAL_NUMBERS_REGISTER_SET_REFRESH = {"constant": "firmware_dialog_serial_numbers_register_set_refresh",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.firmware_dialog_serial_numbers_register_set_refresh}
        self.FIRMWARE_DIALOG_UPGRADE_CLICK_ASSIGN_IMAGE = {"constant": "firmware_dialog_upgrade_click_assign_image",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.firmware_dialog_upgrade_click_assign_image}
        self.FIRMWARE_DIALOG_UPGRADE_CLICK_CANCEL = {"constant": "firmware_dialog_upgrade_click_cancel",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.firmware_dialog_upgrade_click_cancel}
        self.FIRMWARE_DIALOG_UPGRADE_CLICK_CLOSE = {"constant": "firmware_dialog_upgrade_click_close",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.firmware_dialog_upgrade_click_close}
        self.FIRMWARE_DIALOG_UPGRADE_CLICK_SCHEDULE = {"constant": "firmware_dialog_upgrade_click_schedule",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.firmware_dialog_upgrade_click_schedule}
        self.FIRMWARE_DIALOG_UPGRADE_CLICK_SET_CONFIGURATION = {"constant": "firmware_dialog_upgrade_click_set_configuration",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.firmware_dialog_upgrade_click_set_configuration}
        self.FIRMWARE_DIALOG_UPGRADE_CLICK_START = {"constant": "firmware_dialog_upgrade_click_start",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.firmware_dialog_upgrade_click_start}
        self.FIRMWARE_DIALOG_UPGRADE_CONFIRM_START_CLICK_NO = {"constant": "firmware_dialog_upgrade_confirm_start_click_no",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.firmware_dialog_upgrade_confirm_start_click_no}
        self.FIRMWARE_DIALOG_UPGRADE_CONFIRM_START_CLICK_YES = {"constant": "firmware_dialog_upgrade_confirm_start_click_yes",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.firmware_dialog_upgrade_confirm_start_click_yes}
        self.FIRMWARE_DIALOG_UPGRADE_SELECT_DEVICES = {"constant": "firmware_dialog_upgrade_select_devices",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.firmware_dialog_upgrade_select_devices}
        self.FIRMWARE_DIALOG_UPGRADE_SET_DEVICE_UPGRADE_GROUP_SIZE = {"constant": "firmware_dialog_upgrade_set_device_upgrade_group_size",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.firmware_dialog_upgrade_set_device_upgrade_group_size}
        self.FIRMWARE_DIALOG_UPGRADE_SET_RESTART_DEVICES_AFTER_UPGRADE = {"constant": "firmware_dialog_upgrade_set_restart_devices_after_upgrade",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.firmware_dialog_upgrade_set_restart_devices_after_upgrade}
        self.FIRMWARE_DIALOG_UPGRADE_SET_SCHEDULE_ABORT_ON_FAILURE = {"constant": "firmware_dialog_upgrade_set_schedule_abort_on_failure",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.firmware_dialog_upgrade_set_schedule_abort_on_failure}
        self.FIRMWARE_DIALOG_UPGRADE_SET_SCHEDULE_DATE_TIME = {"constant": "firmware_dialog_upgrade_set_schedule_date_time",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.firmware_dialog_upgrade_set_schedule_date_time}
        self.FIRMWARE_DIALOG_UPGRADE_SET_SCHEDULE_NAME = {"constant": "firmware_dialog_upgrade_set_schedule_name",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.firmware_dialog_upgrade_set_schedule_name}
        self.FIRMWARE_DIALOG_UPGRADE_SET_SCHEDULE_UPGRADE = {"constant": "firmware_dialog_upgrade_set_schedule_upgrade",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.firmware_dialog_upgrade_set_schedule_upgrade}
        self.FIRMWARE_DIALOG_UPGRADE_WAIT_FOR_COMPLETION = {"constant": "firmware_dialog_upgrade_wait_for_completion",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.firmware_dialog_upgrade_wait_for_completion}
        self.FIRMWARE_MENU_BACKUP_CONFIGURATION = {"constant": "firmware_menu_backup_configuration",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.firmware_menu_backup_configuration}
        self.FIRMWARE_MENU_CHECK_FOR_UPDATES = {"constant": "firmware_menu_check_for_updates",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.firmware_menu_check_for_updates}
        self.FIRMWARE_MENU_COMPARE_LAST_CONFIGURATIONS = {"constant": "firmware_menu_compare_last_configurations",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.firmware_menu_compare_last_configurations}
        self.FIRMWARE_MENU_REGISTER_EXPORT_SERIAL_NUMBERS = {"constant": "firmware_menu_register_export_serial_numbers",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.firmware_menu_register_export_serial_numbers}
        self.FIRMWARE_MENU_RESTART_DEVICE = {"constant": "firmware_menu_restart_device",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.firmware_menu_restart_device}
        self.FIRMWARE_MENU_RESTORE_CONFIGURATION = {"constant": "firmware_menu_restore_configuration",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.firmware_menu_restore_configuration}
        self.FIRMWARE_MENU_SET_CONFIGURATION = {"constant": "firmware_menu_set_configuration",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.firmware_menu_set_configuration}
        self.FIRMWARE_MENU_UPGRADE_FIRMWARE = {"constant": "firmware_menu_upgrade_firmware",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.firmware_menu_upgrade_firmware}
        self.FIRMWARE_MENU_VIEW_AVAILABLE_RELEASES = {"constant": "firmware_menu_view_available_releases",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.firmware_menu_view_available_releases}
        self.FIRMWARE_TAB_DELETE_ALL_IMAGES_FROM_TABLE = {"constant": "firmware_tab_delete_all_images_from_table",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.firmware_tab_delete_all_images_from_table}
        self.FIRMWARE_TAB_DIALOG_CONFIRM_DELETE_IMAGE_CLICK_CANCEL = {"constant": "firmware_tab_dialog_confirm_delete_image_click_cancel",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.firmware_tab_dialog_confirm_delete_image_click_cancel}
        self.FIRMWARE_TAB_DIALOG_CONFIRM_DELETE_IMAGE_CLICK_OK = {"constant": "firmware_tab_dialog_confirm_delete_image_click_ok",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.firmware_tab_dialog_confirm_delete_image_click_ok}
        self.FIRMWARE_TAB_DIALOG_CONFIRM_DELETE_IMAGE_SET_DELETE_FROM_SERVER = {"constant": "firmware_tab_dialog_confirm_delete_image_set_delete_from_server",
                                                                                "tags": ["COMMAND_SELENIUM"],
                                                                                "link": self.link.firmware_tab_dialog_confirm_delete_image_set_delete_from_server}
        self.FIRMWARE_TAB_MENU_DELETE_IMAGE_TABLE = {"constant": "firmware_tab_menu_delete_image_table",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.firmware_tab_menu_delete_image_table}
        self.FIRMWARE_TAB_MENU_DELETE_IMAGE_TREE = {"constant": "firmware_tab_menu_delete_image_tree",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.firmware_tab_menu_delete_image_tree}
        self.FIRMWARE_TAB_MENU_SET_AS_REFERENCE_IMAGE_TABLE = {"constant": "firmware_tab_menu_set_as_reference_image_table",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.firmware_tab_menu_set_as_reference_image_table}
        self.FIRMWARE_TAB_MENU_SET_AS_REFERENCE_IMAGE_TREE = {"constant": "firmware_tab_menu_set_as_reference_image_tree",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.firmware_tab_menu_set_as_reference_image_tree}
        self.FIRMWARE_TAB_MENU_UNSET_AS_REFERENCE_IMAGE_TABLE = {"constant": "firmware_tab_menu_unset_as_reference_image_table",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.firmware_tab_menu_unset_as_reference_image_table}
        self.FIRMWARE_TAB_MENU_UNSET_AS_REFERENCE_IMAGE_TREE = {"constant": "firmware_tab_menu_unset_as_reference_image_tree",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.firmware_tab_menu_unset_as_reference_image_tree}
        self.FIRMWARE_TAB_TABLE_SELECT_ALL_IMAGES = {"constant": "firmware_tab_table_select_all_images",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.firmware_tab_table_select_all_images}
        self.FIRMWARE_TAB_TABLE_SELECT_IMAGE = {"constant": "firmware_tab_table_select_image",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.firmware_tab_table_select_image}
        self.FIRMWARE_TAB_TREE_EXPAND_NODE = {"constant": "firmware_tab_tree_expand_node",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.firmware_tab_tree_expand_node}
        self.FIRMWARE_TAB_TREE_REFRESH = {"constant": "firmware_tab_tree_refresh",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.firmware_tab_tree_refresh}
        self.FIRMWARE_TAB_TREE_SELECT_NODE = {"constant": "firmware_tab_tree_select_node",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.firmware_tab_tree_select_node}
        self.FIRMWARE_TAB_TREE_UPLOAD_FILE = {"constant": "firmware_tab_tree_upload_file",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.firmware_tab_tree_upload_file}
