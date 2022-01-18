"""
This class outlines all the constants for the scripts API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(ScriptsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class ScriptsConstants(ApiConstants):
    def __init__(self):
        super(ScriptsConstants, self).__init__()
        self.SCRIPTS_CLICK_ADD = {"constant": "scripts_click_add",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.scripts_click_add}
        self.SCRIPTS_CLICK_DELETE = {"constant": "scripts_click_delete",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.scripts_click_delete}
        self.SCRIPTS_CLICK_EDIT = {"constant": "scripts_click_edit",
                                   "tags": ["COMMAND_SELENIUM"],
                                   "link": self.link.scripts_click_edit}
        self.SCRIPTS_CLICK_EXPORT = {"constant": "scripts_click_export",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.scripts_click_export}
        self.SCRIPTS_CLICK_IMPORT = {"constant": "scripts_click_import",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.scripts_click_import}
        self.SCRIPTS_CLICK_REFRESH = {"constant": "scripts_click_refresh",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.scripts_click_refresh}
        self.SCRIPTS_CLICK_RUN = {"constant": "scripts_click_run",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.scripts_click_run}
        self.SCRIPTS_CONFIRM_COMMAND_RESULTS_RESULTS = {"constant": "scripts_confirm_command_results_results",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scripts_confirm_command_results_results}
        self.SCRIPTS_CONFIRM_DIALOG_ADD_PERMISSIONS_SELECTED_GROUPS = {"constant": "scripts_confirm_dialog_add_permissions_selected_groups",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.scripts_confirm_dialog_add_permissions_selected_groups}
        self.SCRIPTS_CONFIRM_DIALOG_EDIT_OVERVIEW_VARIABLE = {"constant": "scripts_confirm_dialog_edit_overview_variable",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.scripts_confirm_dialog_edit_overview_variable}
        self.SCRIPTS_CONFIRM_DIALOG_EDIT_PERMISSIONS_SELECTED_GROUPS = {"constant": "scripts_confirm_dialog_edit_permissions_selected_groups",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.scripts_confirm_dialog_edit_permissions_selected_groups}
        self.SCRIPTS_CONFIRM_EXECUTE_CLI_RESULTS_PROGRESS = {"constant": "scripts_confirm_execute_cli_results_progress",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.scripts_confirm_execute_cli_results_progress}
        self.SCRIPTS_CONFIRM_EXECUTE_CLI_RESULTS_STATUS = {"constant": "scripts_confirm_execute_cli_results_status",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.scripts_confirm_execute_cli_results_status}
        self.SCRIPTS_CONFIRM_RUN_SCRIPT_DEVICE_STATUS = {"constant": "scripts_confirm_run_script_device_status",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.scripts_confirm_run_script_device_status}
        self.SCRIPTS_CONFIRM_RUN_SCRIPT_OVERALL_STATUS = {"constant": "scripts_confirm_run_script_overall_status",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.scripts_confirm_run_script_overall_status}
        self.SCRIPTS_CONFIRM_RUN_SCRIPT_RESULTS = {"constant": "scripts_confirm_run_script_results",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.scripts_confirm_run_script_results}
        self.SCRIPTS_CONFIRM_RUN_SCRIPT_RESULTS_FOR_DEVICE = {"constant": "scripts_confirm_run_script_results_for_device",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.scripts_confirm_run_script_results_for_device}
        self.SCRIPTS_CONFIRM_RUN_VERIFY_DEVICE = {"constant": "scripts_confirm_run_verify_device",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.scripts_confirm_run_verify_device}
        self.SCRIPTS_CONFIRM_RUN_VERIFY_SCRIPT_NAME = {"constant": "scripts_confirm_run_verify_script_name",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.scripts_confirm_run_verify_script_name}
        self.SCRIPTS_CONFIRM_RUN_VERIFY_TASK_INFORMATION = {"constant": "scripts_confirm_run_verify_task_information",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.scripts_confirm_run_verify_task_information}
        self.SCRIPTS_CONFIRM_RUN_VERIFY_TASK_NAME = {"constant": "scripts_confirm_run_verify_task_name",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.scripts_confirm_run_verify_task_name}
        self.SCRIPTS_CONFIRM_RUN_VERIFY_TIMEOUT = {"constant": "scripts_confirm_run_verify_timeout",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.scripts_confirm_run_verify_timeout}
        self.SCRIPTS_CONFIRM_SCRIPT_EXISTS = {"constant": "scripts_confirm_script_exists",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.scripts_confirm_script_exists}
        self.SCRIPTS_CONFIRM_TABLE_VALUE = {"constant": "scripts_confirm_table_value",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.scripts_confirm_table_value}
        self.SCRIPTS_DIALOG_ADD_CLICK_CANCEL = {"constant": "scripts_dialog_add_click_cancel",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.scripts_dialog_add_click_cancel}
        self.SCRIPTS_DIALOG_ADD_CLICK_RUN = {"constant": "scripts_dialog_add_click_run",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.scripts_dialog_add_click_run}
        self.SCRIPTS_DIALOG_ADD_CLICK_SAVE = {"constant": "scripts_dialog_add_click_save",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.scripts_dialog_add_click_save}
        self.SCRIPTS_DIALOG_ADD_CLICK_SAVE_AS = {"constant": "scripts_dialog_add_click_save_as",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.scripts_dialog_add_click_save_as}
        self.SCRIPTS_DIALOG_ADD_CONTENT_ADD_CONTENT = {"constant": "scripts_dialog_add_content_add_content",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.scripts_dialog_add_content_add_content}
        self.SCRIPTS_DIALOG_ADD_CONTENT_ADD_VARIABLE = {"constant": "scripts_dialog_add_content_add_variable",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scripts_dialog_add_content_add_variable}
        self.SCRIPTS_DIALOG_ADD_CONTENT_CLEAR_CONTENT = {"constant": "scripts_dialog_add_content_clear_content",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.scripts_dialog_add_content_clear_content}
        self.SCRIPTS_DIALOG_ADD_CONTENT_CLICK_VARIABLES = {"constant": "scripts_dialog_add_content_click_variables",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.scripts_dialog_add_content_click_variables}
        self.SCRIPTS_DIALOG_ADD_CONTENT_HIDE_LINE_NUMBERS = {"constant": "scripts_dialog_add_content_hide_line_numbers",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.scripts_dialog_add_content_hide_line_numbers}
        self.SCRIPTS_DIALOG_ADD_CONTENT_SET_CONTENT = {"constant": "scripts_dialog_add_content_set_content",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.scripts_dialog_add_content_set_content}
        self.SCRIPTS_DIALOG_ADD_CONTENT_SHOW_LINE_NUMBERS = {"constant": "scripts_dialog_add_content_show_line_numbers",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.scripts_dialog_add_content_show_line_numbers}
        self.SCRIPTS_DIALOG_ADD_PERMISSIONS_CLEAR_AUTHORIZATION_GROUPS = {"constant": "scripts_dialog_add_permissions_clear_authorization_groups",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.scripts_dialog_add_permissions_clear_authorization_groups}
        self.SCRIPTS_DIALOG_ADD_PERMISSIONS_CLEAR_MENUS = {"constant": "scripts_dialog_add_permissions_clear_menus",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.scripts_dialog_add_permissions_clear_menus}
        self.SCRIPTS_DIALOG_ADD_PERMISSIONS_CLICK_REMOVE_ALL_GROUPS = {"constant": "scripts_dialog_add_permissions_click_remove_all_groups",
                                                                       "tags": ["COMMAND_SELENIUM"],
                                                                       "link": self.link.scripts_dialog_add_permissions_click_remove_all_groups}
        self.SCRIPTS_DIALOG_ADD_PERMISSIONS_CLICK_SELECT_GROUPS = {"constant": "scripts_dialog_add_permissions_click_select_groups",
                                                                   "tags": ["COMMAND_SELENIUM"],
                                                                   "link": self.link.scripts_dialog_add_permissions_click_select_groups}
        self.SCRIPTS_DIALOG_ADD_PERMISSIONS_DEVICE_GROUP_CLICK_CANCEL = {"constant": "scripts_dialog_add_permissions_device_group_click_cancel",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.scripts_dialog_add_permissions_device_group_click_cancel}
        self.SCRIPTS_DIALOG_ADD_PERMISSIONS_DEVICE_GROUP_CLICK_OK = {"constant": "scripts_dialog_add_permissions_device_group_click_ok",
                                                                     "tags": ["COMMAND_SELENIUM"],
                                                                     "link": self.link.scripts_dialog_add_permissions_device_group_click_ok}
        self.SCRIPTS_DIALOG_ADD_PERMISSIONS_DEVICE_GROUP_EXPAND_NODE = {"constant": "scripts_dialog_add_permissions_device_group_expand_node",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.scripts_dialog_add_permissions_device_group_expand_node}
        self.SCRIPTS_DIALOG_ADD_PERMISSIONS_DEVICE_GROUP_SELECT_NODE = {"constant": "scripts_dialog_add_permissions_device_group_select_node",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.scripts_dialog_add_permissions_device_group_select_node}
        self.SCRIPTS_DIALOG_ADD_PERMISSIONS_SELECT_AUTHORIZATION_GROUPS = {"constant": "scripts_dialog_add_permissions_select_authorization_groups",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.scripts_dialog_add_permissions_select_authorization_groups}
        self.SCRIPTS_DIALOG_ADD_PERMISSIONS_SELECT_MENUS = {"constant": "scripts_dialog_add_permissions_select_menus",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.scripts_dialog_add_permissions_select_menus}
        self.SCRIPTS_DIALOG_ADD_PERMISSIONS_SET_CATEGORY = {"constant": "scripts_dialog_add_permissions_set_category",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.scripts_dialog_add_permissions_set_category}
        self.SCRIPTS_DIALOG_ADD_RUNTIME_SET_COMMENTS = {"constant": "scripts_dialog_add_runtime_set_comments",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scripts_dialog_add_runtime_set_comments}
        self.SCRIPTS_DIALOG_ADD_RUNTIME_SET_TIMEOUT = {"constant": "scripts_dialog_add_runtime_set_timeout",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.scripts_dialog_add_runtime_set_timeout}
        self.SCRIPTS_DIALOG_ADD_SELECT_TAB = {"constant": "scripts_dialog_add_select_tab",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.scripts_dialog_add_select_tab}
        self.SCRIPTS_DIALOG_COMMAND_RESULTS_CLICK_CLOSE = {"constant": "scripts_dialog_command_results_click_close",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.scripts_dialog_command_results_click_close}
        self.SCRIPTS_DIALOG_COMMAND_RESULTS_CLICK_SAVE_RESULTS = {"constant": "scripts_dialog_command_results_click_save_results",
                                                                  "tags": ["COMMAND_SELENIUM"],
                                                                  "link": self.link.scripts_dialog_command_results_click_save_results}
        self.SCRIPTS_DIALOG_CONFIRM_DELETE_CLICK_NO = {"constant": "scripts_dialog_confirm_delete_click_no",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.scripts_dialog_confirm_delete_click_no}
        self.SCRIPTS_DIALOG_CONFIRM_DELETE_CLICK_YES = {"constant": "scripts_dialog_confirm_delete_click_yes",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scripts_dialog_confirm_delete_click_yes}
        self.SCRIPTS_DIALOG_EDIT_CLICK_CANCEL = {"constant": "scripts_dialog_edit_click_cancel",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.scripts_dialog_edit_click_cancel}
        self.SCRIPTS_DIALOG_EDIT_CLICK_RUN = {"constant": "scripts_dialog_edit_click_run",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.scripts_dialog_edit_click_run}
        self.SCRIPTS_DIALOG_EDIT_CLICK_SAVE = {"constant": "scripts_dialog_edit_click_save",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.scripts_dialog_edit_click_save}
        self.SCRIPTS_DIALOG_EDIT_CLICK_SAVE_AS = {"constant": "scripts_dialog_edit_click_save_as",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.scripts_dialog_edit_click_save_as}
        self.SCRIPTS_DIALOG_EDIT_CONTENT_ADD_CONTENT = {"constant": "scripts_dialog_edit_content_add_content",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scripts_dialog_edit_content_add_content}
        self.SCRIPTS_DIALOG_EDIT_CONTENT_ADD_VARIABLE = {"constant": "scripts_dialog_edit_content_add_variable",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.scripts_dialog_edit_content_add_variable}
        self.SCRIPTS_DIALOG_EDIT_CONTENT_CLEAR_CONTENT = {"constant": "scripts_dialog_edit_content_clear_content",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.scripts_dialog_edit_content_clear_content}
        self.SCRIPTS_DIALOG_EDIT_CONTENT_CLICK_VARIABLES = {"constant": "scripts_dialog_edit_content_click_variables",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.scripts_dialog_edit_content_click_variables}
        self.SCRIPTS_DIALOG_EDIT_CONTENT_HIDE_LINE_NUMBERS = {"constant": "scripts_dialog_edit_content_hide_line_numbers",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.scripts_dialog_edit_content_hide_line_numbers}
        self.SCRIPTS_DIALOG_EDIT_CONTENT_SET_CONTENT = {"constant": "scripts_dialog_edit_content_set_content",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scripts_dialog_edit_content_set_content}
        self.SCRIPTS_DIALOG_EDIT_CONTENT_SHOW_LINE_NUMBERS = {"constant": "scripts_dialog_edit_content_show_line_numbers",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.scripts_dialog_edit_content_show_line_numbers}
        self.SCRIPTS_DIALOG_EDIT_OVERVIEW_SET_VARIABLE = {"constant": "scripts_dialog_edit_overview_set_variable",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.scripts_dialog_edit_overview_set_variable}
        self.SCRIPTS_DIALOG_EDIT_PERMISSIONS_CLEAR_AUTHORIZATION_GROUPS = {"constant": "scripts_dialog_edit_permissions_clear_authorization_groups",
                                                                           "tags": ["COMMAND_SELENIUM"],
                                                                           "link": self.link.scripts_dialog_edit_permissions_clear_authorization_groups}
        self.SCRIPTS_DIALOG_EDIT_PERMISSIONS_CLEAR_MENUS = {"constant": "scripts_dialog_edit_permissions_clear_menus",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.scripts_dialog_edit_permissions_clear_menus}
        self.SCRIPTS_DIALOG_EDIT_PERMISSIONS_CLICK_REMOVE_ALL_GROUPS = {"constant": "scripts_dialog_edit_permissions_click_remove_all_groups",
                                                                        "tags": ["COMMAND_SELENIUM"],
                                                                        "link": self.link.scripts_dialog_edit_permissions_click_remove_all_groups}
        self.SCRIPTS_DIALOG_EDIT_PERMISSIONS_CLICK_SELECT_GROUPS = {"constant": "scripts_dialog_edit_permissions_click_select_groups",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.scripts_dialog_edit_permissions_click_select_groups}
        self.SCRIPTS_DIALOG_EDIT_PERMISSIONS_DEVICE_GROUP_CLICK_CANCEL = {"constant": "scripts_dialog_edit_permissions_device_group_click_cancel",
                                                                          "tags": ["COMMAND_SELENIUM"],
                                                                          "link": self.link.scripts_dialog_edit_permissions_device_group_click_cancel}
        self.SCRIPTS_DIALOG_EDIT_PERMISSIONS_DEVICE_GROUP_CLICK_OK = {"constant": "scripts_dialog_edit_permissions_device_group_click_ok",
                                                                      "tags": ["COMMAND_SELENIUM"],
                                                                      "link": self.link.scripts_dialog_edit_permissions_device_group_click_ok}
        self.SCRIPTS_DIALOG_EDIT_PERMISSIONS_DEVICE_GROUP_EXPAND_NODE = {"constant": "scripts_dialog_edit_permissions_device_group_expand_node",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.scripts_dialog_edit_permissions_device_group_expand_node}
        self.SCRIPTS_DIALOG_EDIT_PERMISSIONS_DEVICE_GROUP_SELECT_NODE = {"constant": "scripts_dialog_edit_permissions_device_group_select_node",
                                                                         "tags": ["COMMAND_SELENIUM"],
                                                                         "link": self.link.scripts_dialog_edit_permissions_device_group_select_node}
        self.SCRIPTS_DIALOG_EDIT_PERMISSIONS_SELECT_AUTHORIZATION_GROUPS = {"constant": "scripts_dialog_edit_permissions_select_authorization_groups",
                                                                            "tags": ["COMMAND_SELENIUM"],
                                                                            "link": self.link.scripts_dialog_edit_permissions_select_authorization_groups}
        self.SCRIPTS_DIALOG_EDIT_PERMISSIONS_SELECT_MENUS = {"constant": "scripts_dialog_edit_permissions_select_menus",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.scripts_dialog_edit_permissions_select_menus}
        self.SCRIPTS_DIALOG_EDIT_PERMISSIONS_SET_CATEGORY = {"constant": "scripts_dialog_edit_permissions_set_category",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.scripts_dialog_edit_permissions_set_category}
        self.SCRIPTS_DIALOG_EDIT_RUNTIME_SET_COMMENTS = {"constant": "scripts_dialog_edit_runtime_set_comments",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.scripts_dialog_edit_runtime_set_comments}
        self.SCRIPTS_DIALOG_EDIT_RUNTIME_SET_TIMEOUT = {"constant": "scripts_dialog_edit_runtime_set_timeout",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scripts_dialog_edit_runtime_set_timeout}
        self.SCRIPTS_DIALOG_EDIT_SELECT_TAB = {"constant": "scripts_dialog_edit_select_tab",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.scripts_dialog_edit_select_tab}
        self.SCRIPTS_DIALOG_EXECUTE_CLI_CLICK_ABORT = {"constant": "scripts_dialog_execute_cli_click_abort",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.scripts_dialog_execute_cli_click_abort}
        self.SCRIPTS_DIALOG_EXECUTE_CLI_CLICK_CANCEL = {"constant": "scripts_dialog_execute_cli_click_cancel",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scripts_dialog_execute_cli_click_cancel}
        self.SCRIPTS_DIALOG_EXECUTE_CLI_CLICK_EXECUTE = {"constant": "scripts_dialog_execute_cli_click_execute",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.scripts_dialog_execute_cli_click_execute}
        self.SCRIPTS_DIALOG_EXECUTE_CLI_CLICK_SAVE_RESULTS = {"constant": "scripts_dialog_execute_cli_click_save_results",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.scripts_dialog_execute_cli_click_save_results}
        self.SCRIPTS_DIALOG_EXECUTE_CLI_CLICK_VIEW_RESULTS = {"constant": "scripts_dialog_execute_cli_click_view_results",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.scripts_dialog_execute_cli_click_view_results}
        self.SCRIPTS_DIALOG_EXECUTE_CLI_SELECT_TAB = {"constant": "scripts_dialog_execute_cli_select_tab",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.scripts_dialog_execute_cli_select_tab}
        self.SCRIPTS_DIALOG_IMPORT_CLICK_CLOSE = {"constant": "scripts_dialog_import_click_close",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.scripts_dialog_import_click_close}
        self.SCRIPTS_DIALOG_REPLACE_SCRIPT_CLICK_NO = {"constant": "scripts_dialog_replace_script_click_no",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.scripts_dialog_replace_script_click_no}
        self.SCRIPTS_DIALOG_REPLACE_SCRIPT_CLICK_YES = {"constant": "scripts_dialog_replace_script_click_yes",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scripts_dialog_replace_script_click_yes}
        self.SCRIPTS_DIALOG_RUN_CLICK_BACK = {"constant": "scripts_dialog_run_click_back",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.scripts_dialog_run_click_back}
        self.SCRIPTS_DIALOG_RUN_CLICK_CANCEL = {"constant": "scripts_dialog_run_click_cancel",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.scripts_dialog_run_click_cancel}
        self.SCRIPTS_DIALOG_RUN_CLICK_CLOSE = {"constant": "scripts_dialog_run_click_close",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.scripts_dialog_run_click_close}
        self.SCRIPTS_DIALOG_RUN_CLICK_EXECUTE_CLI = {"constant": "scripts_dialog_run_click_execute_cli",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.scripts_dialog_run_click_execute_cli}
        self.SCRIPTS_DIALOG_RUN_CLICK_FINISH = {"constant": "scripts_dialog_run_click_finish",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.scripts_dialog_run_click_finish}
        self.SCRIPTS_DIALOG_RUN_CLICK_NEXT = {"constant": "scripts_dialog_run_click_next",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.scripts_dialog_run_click_next}
        self.SCRIPTS_DIALOG_RUN_CLICK_RUN = {"constant": "scripts_dialog_run_click_run",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.scripts_dialog_run_click_run}
        self.SCRIPTS_DIALOG_RUN_COLLAPSE_DEVICE_GROUP = {"constant": "scripts_dialog_run_collapse_device_group",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.scripts_dialog_run_collapse_device_group}
        self.SCRIPTS_DIALOG_RUN_EXPAND_DEVICE_GROUP = {"constant": "scripts_dialog_run_expand_device_group",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.scripts_dialog_run_expand_device_group}
        self.SCRIPTS_DIALOG_RUN_MOVE_DEVICE_DOWN = {"constant": "scripts_dialog_run_move_device_down",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.scripts_dialog_run_move_device_down}
        self.SCRIPTS_DIALOG_RUN_MOVE_DEVICE_UP = {"constant": "scripts_dialog_run_move_device_up",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.scripts_dialog_run_move_device_up}
        self.SCRIPTS_DIALOG_RUN_RESULTS_CLICK_REFRESH = {"constant": "scripts_dialog_run_results_click_refresh",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.scripts_dialog_run_results_click_refresh}
        self.SCRIPTS_DIALOG_RUN_RESULTS_SELECT_DEVICE = {"constant": "scripts_dialog_run_results_select_device",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.scripts_dialog_run_results_select_device}
        self.SCRIPTS_DIALOG_RUN_SELECT_DEVICE = {"constant": "scripts_dialog_run_select_device",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.scripts_dialog_run_select_device}
        self.SCRIPTS_DIALOG_RUN_SELECT_DEVICE_GROUP = {"constant": "scripts_dialog_run_select_device_group",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.scripts_dialog_run_select_device_group}
        self.SCRIPTS_DIALOG_RUN_SET_RUN_NOW_NO_SAVE = {"constant": "scripts_dialog_run_set_run_now_no_save",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.scripts_dialog_run_set_run_now_no_save}
        self.SCRIPTS_DIALOG_RUN_SET_SAVE_AND_RUN_LATER = {"constant": "scripts_dialog_run_set_save_and_run_later",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.scripts_dialog_run_set_save_and_run_later}
        self.SCRIPTS_DIALOG_RUN_SET_SAVE_AND_RUN_NOW = {"constant": "scripts_dialog_run_set_save_and_run_now",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.scripts_dialog_run_set_save_and_run_now}
        self.SCRIPTS_DIALOG_RUN_SET_TIMEOUT = {"constant": "scripts_dialog_run_set_timeout",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.scripts_dialog_run_set_timeout}
        self.SCRIPTS_DIALOG_RUN_SET_VARIABLE = {"constant": "scripts_dialog_run_set_variable",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.scripts_dialog_run_set_variable}
        self.SCRIPTS_DIALOG_SAVE_CLICK_CANCEL = {"constant": "scripts_dialog_save_click_cancel",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.scripts_dialog_save_click_cancel}
        self.SCRIPTS_DIALOG_SAVE_CLICK_SAVE = {"constant": "scripts_dialog_save_click_save",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.scripts_dialog_save_click_save}
        self.SCRIPTS_DIALOG_SAVE_SET_DESCRIPTION = {"constant": "scripts_dialog_save_set_description",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.scripts_dialog_save_set_description}
        self.SCRIPTS_DIALOG_SAVE_SET_NAME = {"constant": "scripts_dialog_save_set_name",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.scripts_dialog_save_set_name}
        self.SCRIPTS_DIALOG_SAVE_SUCCESS_CLICK_OK = {"constant": "scripts_dialog_save_success_click_ok",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.scripts_dialog_save_success_click_ok}
        self.SCRIPTS_DIALOG_VARIABLES_CLEAR_SCOPE = {"constant": "scripts_dialog_variables_clear_scope",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.scripts_dialog_variables_clear_scope}
        self.SCRIPTS_DIALOG_VARIABLES_CLICK_CANCEL = {"constant": "scripts_dialog_variables_click_cancel",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.scripts_dialog_variables_click_cancel}
        self.SCRIPTS_DIALOG_VARIABLES_CLICK_INSERT = {"constant": "scripts_dialog_variables_click_insert",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.scripts_dialog_variables_click_insert}
        self.SCRIPTS_DIALOG_VARIABLES_SELECT_SCOPE = {"constant": "scripts_dialog_variables_select_scope",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.scripts_dialog_variables_select_scope}
        self.SCRIPTS_DIALOG_VARIABLES_SELECT_VARIABLES = {"constant": "scripts_dialog_variables_select_variables",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.scripts_dialog_variables_select_variables}
        self.SCRIPTS_SELECT_SCRIPT = {"constant": "scripts_select_script",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.scripts_select_script}
        self.SCRIPTS_WAIT_FOR_EXECUTE_CLI_RESULTS_PROGRESS = {"constant": "scripts_wait_for_execute_cli_results_progress",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.scripts_wait_for_execute_cli_results_progress}
        self.SCRIPTS_WAIT_FOR_EXECUTE_CLI_RESULTS_STATUS = {"constant": "scripts_wait_for_execute_cli_results_status",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.scripts_wait_for_execute_cli_results_status}
        self.SCRIPTS_WAIT_FOR_RUN_SCRIPT_DEVICE_STATUS = {"constant": "scripts_wait_for_run_script_device_status",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.scripts_wait_for_run_script_device_status}
        self.SCRIPTS_WAIT_FOR_RUN_SCRIPT_OVERALL_STATUS = {"constant": "scripts_wait_for_run_script_overall_status",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.scripts_wait_for_run_script_overall_status}
        self.SCRIPTS_WAIT_FOR_SCRIPT_ADD = {"constant": "scripts_wait_for_script_add",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.scripts_wait_for_script_add}
        self.SCRIPTS_WAIT_FOR_SCRIPT_REMOVE = {"constant": "scripts_wait_for_script_remove",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.scripts_wait_for_script_remove}
