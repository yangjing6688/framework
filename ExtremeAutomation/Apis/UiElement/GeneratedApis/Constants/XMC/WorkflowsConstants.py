"""
This class outlines all the constants for the workflows API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(WorkflowsConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class WorkflowsConstants(ApiConstants):
    def __init__(self):
        super(WorkflowsConstants, self).__init__()
        self.ADD_ACTIVITY = {"constant": "add_activity",
                             "tags": ["COMMAND_SELENIUM"],
                             "link": self.link.add_activity}
        self.COLLAPSE_ALL_USER_WORKFLOW_ITEMS = {"constant": "collapse_all_user_workflow_items",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.collapse_all_user_workflow_items}
        self.COLLAPSE_WORKFLOWS_TREE_PANEL = {"constant": "collapse_workflows_tree_panel",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.collapse_workflows_tree_panel}
        self.COLLAPSE_WORKFLOW_DETAILS_PANEL = {"constant": "collapse_workflow_Details_panel",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.collapse_workflow_Details_panel}
        self.CREATE_WORKFLOW = {"constant": "create_workflow",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.create_workflow}
        self.CREATE_WORKGROUP = {"constant": "create_workgroup",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.create_workgroup}
        self.DELETE_ACTIVITY = {"constant": "delete_activity",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.delete_activity}
        self.EXPAND_WORKFLOWS_TREE_PANEL = {"constant": "expand_workflows_tree_panel",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.expand_workflows_tree_panel}
        self.EXPAND_WORKFLOW_ACTIVITY_PANEL_SIZE = {"constant": "expand_workflow_activity_panel_size",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.expand_workflow_activity_panel_size}
        self.EXPAND_WORKFLOW_DETAILS_PANEL = {"constant": "expand_workflow_details_panel",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.expand_workflow_details_panel}
        self.EXPAND_WORKFLOW_TREE_PANEL_SIZE = {"constant": "expand_workflow_tree_panel_size",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.expand_workflow_tree_panel_size}
        self.IMPORT_WORKFLOW = {"constant": "import_workflow",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.import_workflow}
        self.INVOKE_CONTEXT_MENU_FOR_SYSTEM_WORKFLOW = {"constant": "invoke_context_menu_for_system_workflow",
                                                        "tags": ["COMMAND_SELENIUM"],
                                                        "link": self.link.invoke_context_menu_for_system_workflow}
        self.INVOKE_CONTEXT_MENU_FOR_USER_WORKFLOW = {"constant": "invoke_context_menu_for_user_workflow",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.invoke_context_menu_for_user_workflow}
        self.REFRESH_WORKFLOWS = {"constant": "refresh_workflows",
                                  "tags": ["COMMAND_SELENIUM"],
                                  "link": self.link.refresh_workflows}
        self.RENAME_WORKFLOW = {"constant": "rename_workflow",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.rename_workflow}
        self.RENAME_WORKGROUP = {"constant": "rename_workgroup",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.rename_workgroup}
        self.RUN_WORKFLOW = {"constant": "run_workflow",
                             "tags": ["COMMAND_SELENIUM"],
                             "link": self.link.run_workflow}
        self.SAVE_WORKFLOW = {"constant": "save_workflow",
                              "tags": ["COMMAND_SELENIUM"],
                              "link": self.link.save_workflow}
        self.SAVE_WORKFLOW_AS = {"constant": "save_workflow_as",
                                 "tags": ["COMMAND_SELENIUM"],
                                 "link": self.link.save_workflow_as}
        self.SELECT_A_DEVICE = {"constant": "select_a_device",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.select_a_device}
        self.SELECT_A_SYSTEM_WORKFLOW = {"constant": "select_a_system_workflow",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.select_a_system_workflow}
        self.SELECT_A_USER_WORKFLOW = {"constant": "select_a_user_workflow",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.select_a_user_workflow}
        self.SELECT_HUMBURGER_MENU_ITEM = {"constant": "select_humburger_menu_item",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.select_humburger_menu_item}
        self.SELECT_WORKFLOWS_TAB = {"constant": "select_workflows_tab",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.select_workflows_tab}
        self.TOGGLE_MINI_MAP = {"constant": "toggle_mini_map",
                                "tags": ["COMMAND_SELENIUM"],
                                "link": self.link.toggle_mini_map}
        self.VERIFY_SYSTEM_WORKFLOWS_ARE_READ_ONLY = {"constant": "verify_system_workflows_are_read_only",
                                                      "tags": ["COMMAND_SELENIUM"],
                                                      "link": self.link.verify_system_workflows_are_read_only}
        self.VERIFY_SYSTEM_WORKFLOWS_ITEM_EXISTS = {"constant": "verify_system_workflows_item_exists",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.verify_system_workflows_item_exists}
        self.VERIFY_SYSTEM_WORKFLOW_VERSION = {"constant": "verify_system_workflow_version",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.verify_system_workflow_version}
        self.VERIFY_USER_WORKFLOWS_ITEM_EXISTS = {"constant": "verify_user_workflows_item_exists",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.verify_user_workflows_item_exists}
        self.VERIFY_WORKFLOW_CHANGES_EXIST = {"constant": "verify_workflow_changes_exist",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.verify_workflow_changes_exist}
        self.VERIFY_WORKFLOW_CONTROL_TOOLTIPS = {"constant": "verify_workflow_control_tooltips",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.verify_workflow_control_tooltips}
        self.VERIFY_WORKFLOW_DETAILS_PANEL_EXISTS = {"constant": "verify_workflow_details_panel_exists",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.verify_workflow_details_panel_exists}
        self.VERIFY_WORKFLOW_DIAGRAM_ZOOM_IN = {"constant": "verify_workflow_diagram_zoom_in",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.verify_workflow_diagram_zoom_in}
        self.VERIFY_WORKFLOW_DIAGRAM_ZOOM_OUT = {"constant": "verify_workflow_diagram_zoom_out",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.verify_workflow_diagram_zoom_out}
        self.VERIFY_WORKFLOW_MINI_MAP_EXISTS = {"constant": "verify_workflow_mini_map_exists",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.verify_workflow_mini_map_exists}
        self.VERIFY_WORKFLOW_TREE_PANEL_EXISTS = {"constant": "verify_workflow_tree_panel_exists",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.verify_workflow_tree_panel_exists}
        self.VERIFY_WORKFLOW_VALIDATION_MESSAGE = {"constant": "verify_workflow_validation_message",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.verify_workflow_validation_message}
