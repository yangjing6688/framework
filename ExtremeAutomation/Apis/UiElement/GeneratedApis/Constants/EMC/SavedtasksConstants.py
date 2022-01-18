"""
This class outlines all the constants for the savedtasks API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(SavedtasksConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class SavedtasksConstants(ApiConstants):
    def __init__(self):
        super(SavedtasksConstants, self).__init__()
        self.SAVEDTASKS_CLICK_DELETE = {"constant": "savedtasks_click_delete",
                                        "tags": ["COMMAND_SELENIUM"],
                                        "link": self.link.savedtasks_click_delete}
        self.SAVEDTASKS_CLICK_EDIT = {"constant": "savedtasks_click_edit",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.savedtasks_click_edit}
        self.SAVEDTASKS_CLICK_REFRESH = {"constant": "savedtasks_click_refresh",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.savedtasks_click_refresh}
        self.SAVEDTASKS_CLICK_RUN = {"constant": "savedtasks_click_run",
                                     "tags": ["COMMAND_SELENIUM"],
                                     "link": self.link.savedtasks_click_run}
        self.SAVEDTASKS_CLICK_SAVE_AS = {"constant": "savedtasks_click_save_as",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.savedtasks_click_save_as}
        self.SAVEDTASKS_CONFIRM_TASK_EXISTS = {"constant": "savedtasks_confirm_task_exists",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.savedtasks_confirm_task_exists}
        self.SAVEDTASKS_DIALOG_CONFIRM_DELETE_CLICK_NO = {"constant": "savedtasks_dialog_confirm_delete_click_no",
                                                          "tags": ["COMMAND_SELENIUM"],
                                                          "link": self.link.savedtasks_dialog_confirm_delete_click_no}
        self.SAVEDTASKS_DIALOG_CONFIRM_DELETE_CLICK_YES = {"constant": "savedtasks_dialog_confirm_delete_click_yes",
                                                           "tags": ["COMMAND_SELENIUM"],
                                                           "link": self.link.savedtasks_dialog_confirm_delete_click_yes}
        self.SAVEDTASKS_SELECT_TASK = {"constant": "savedtasks_select_task",
                                       "tags": ["COMMAND_SELENIUM"],
                                       "link": self.link.savedtasks_select_task}
        self.SAVEDTASKS_WAIT_FOR_TASK_ADD = {"constant": "savedtasks_wait_for_task_add",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.savedtasks_wait_for_task_add}
        self.SAVEDTASKS_WAIT_FOR_TASK_REMOVE = {"constant": "savedtasks_wait_for_task_remove",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.savedtasks_wait_for_task_remove}
