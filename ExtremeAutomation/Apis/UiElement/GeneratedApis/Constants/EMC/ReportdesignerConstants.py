"""
This class outlines all the constants for the reportdesigner API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(ReportdesignerConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class ReportdesignerConstants(ApiConstants):
    def __init__(self):
        super(ReportdesignerConstants, self).__init__()
        self.REPORTDESIGNER_CLICK_DELETE = {"constant": "reportdesigner_click_delete",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.reportdesigner_click_delete}
        self.REPORTDESIGNER_CLICK_EDIT = {"constant": "reportdesigner_click_edit",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.reportdesigner_click_edit}
        self.REPORTDESIGNER_CLICK_NEW = {"constant": "reportdesigner_click_new",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.reportdesigner_click_new}
        self.REPORTDESIGNER_CLICK_SAVE = {"constant": "reportdesigner_click_save",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.reportdesigner_click_save}
        self.REPORTDESIGNER_COLLAPSE_TREE_PANEL = {"constant": "reportdesigner_collapse_tree_panel",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.reportdesigner_collapse_tree_panel}
        self.REPORTDESIGNER_COMPONENTS_COLLAPSE_TREE_NODE = {"constant": "reportdesigner_components_collapse_tree_node",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.reportdesigner_components_collapse_tree_node}
        self.REPORTDESIGNER_COMPONENTS_EXPAND_TREE_NODE = {"constant": "reportdesigner_components_expand_tree_node",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.reportdesigner_components_expand_tree_node}
        self.REPORTDESIGNER_COMPONENTS_SELECT_TREE_NODE = {"constant": "reportdesigner_components_select_tree_node",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.reportdesigner_components_select_tree_node}
        self.REPORTDESIGNER_DIALOG_CONFIRM_DELETE = {"constant": "reportdesigner_dialog_confirm_delete",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.reportdesigner_dialog_confirm_delete}
        self.REPORTDESIGNER_DIALOG_NEW_CLICK_CANCEL = {"constant": "reportdesigner_dialog_new_click_cancel",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.reportdesigner_dialog_new_click_cancel}
        self.REPORTDESIGNER_DIALOG_NEW_CLICK_CUSTOM = {"constant": "reportdesigner_dialog_new_click_custom",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.reportdesigner_dialog_new_click_custom}
        self.REPORTDESIGNER_DIALOG_NEW_CLICK_OK = {"constant": "reportdesigner_dialog_new_click_ok",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.reportdesigner_dialog_new_click_ok}
        self.REPORTDESIGNER_DIALOG_NEW_CUSTOM_SET_COLUMNS = {"constant": "reportdesigner_dialog_new_custom_set_columns",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.reportdesigner_dialog_new_custom_set_columns}
        self.REPORTDESIGNER_DIALOG_NEW_CUSTOM_SET_ROWS = {"constant": "reportdesigner_dialog_new_custom_set_rows",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.reportdesigner_dialog_new_custom_set_rows}
        self.REPORTDESIGNER_DIALOG_NEW_SET_CATEGORY = {"constant": "reportdesigner_dialog_new_set_category",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.reportdesigner_dialog_new_set_category}
        self.REPORTDESIGNER_DIALOG_NEW_SET_INCLUDE_TOOLBAR = {"constant": "reportdesigner_dialog_new_set_include_toolbar",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.reportdesigner_dialog_new_set_include_toolbar}
        self.REPORTDESIGNER_DIALOG_NEW_SET_LAYOUT = {"constant": "reportdesigner_dialog_new_set_layout",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.reportdesigner_dialog_new_set_layout}
        self.REPORTDESIGNER_DIALOG_NEW_SET_MIN_HEIGHT = {"constant": "reportdesigner_dialog_new_set_min_height",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.reportdesigner_dialog_new_set_min_height}
        self.REPORTDESIGNER_DIALOG_NEW_SET_REPORT_NAME = {"constant": "reportdesigner_dialog_new_set_report_name",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.reportdesigner_dialog_new_set_report_name}
        self.REPORTDESIGNER_DRAGDROP_COMPONENT = {"constant": "reportdesigner_dragdrop_component",
                                                  "tags": ["COMMAND_SELENIUM"],
                                                  "link": self.link.reportdesigner_dragdrop_component}
        self.REPORTDESIGNER_EXPAND_TREE_PANEL = {"constant": "reportdesigner_expand_tree_panel",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.reportdesigner_expand_tree_panel}
        self.REPORTDESIGNER_MYCOMPONENTS_COLLAPSE_TREE_NODE = {"constant": "reportdesigner_mycomponents_collapse_tree_node",
                                                               "tags": ["COMMAND_SELENIUM"],
                                                               "link": self.link.reportdesigner_mycomponents_collapse_tree_node}
        self.REPORTDESIGNER_MYCOMPONENTS_EXPAND_TREE_NODE = {"constant": "reportdesigner_mycomponents_expand_tree_node",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.reportdesigner_mycomponents_expand_tree_node}
        self.REPORTDESIGNER_MYCOMPONENTS_SELECT_TREE_NODE = {"constant": "reportdesigner_mycomponents_select_tree_node",
                                                             "tags": ["COMMAND_SELENIUM"],
                                                             "link": self.link.reportdesigner_mycomponents_select_tree_node}
        self.REPORTDESIGNER_MYREPORTS_COLLAPSE_TREE_NODE = {"constant": "reportdesigner_myreports_collapse_tree_node",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.reportdesigner_myreports_collapse_tree_node}
        self.REPORTDESIGNER_MYREPORTS_EXPAND_TREE_NODE = {"constant": "reportdesigner_myreports_expand_tree_node",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.reportdesigner_myreports_expand_tree_node}
        self.REPORTDESIGNER_MYREPORTS_SELECT_TREE_NODE = {"constant": "reportdesigner_myreports_select_tree_node",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.reportdesigner_myreports_select_tree_node}
        self.REPORTDESIGNER_SELECT_TREE_PANEL = {"constant": "reportdesigner_select_tree_panel",
                                                 "tags": ["COMMAND_SELENIUM"],
                                                 "link": self.link.reportdesigner_select_tree_panel}
        self.REPORTDESIGNER_SYSTEMREPORTS_COLLAPSE_TREE_NODE = {"constant": "reportdesigner_systemreports_collapse_tree_node",
                                                                "tags": ["COMMAND_SELENIUM"],
                                                                "link": self.link.reportdesigner_systemreports_collapse_tree_node}
        self.REPORTDESIGNER_SYSTEMREPORTS_EXPAND_TREE_NODE = {"constant": "reportdesigner_systemreports_expand_tree_node",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.reportdesigner_systemreports_expand_tree_node}
        self.REPORTDESIGNER_SYSTEMREPORTS_SELECT_TREE_NODE = {"constant": "reportdesigner_systemreports_select_tree_node",
                                                              "tags": ["COMMAND_SELENIUM"],
                                                              "link": self.link.reportdesigner_systemreports_select_tree_node}
