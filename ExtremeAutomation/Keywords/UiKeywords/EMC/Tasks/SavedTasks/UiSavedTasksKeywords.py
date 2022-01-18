from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.SavedtasksConstants import SavedtasksConstants


class UiSavedTasksKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiSavedTasksKeywords, self).__init__()
        self.api_const = self.constants.API_SAVED_TASKS
        self.command_const = SavedtasksConstants()

    def savedtasks_select_task(self, element_name, task_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [task_name] -     Name of the task to select

        Selects the specified saved task.
        """
        args = {"task_name": task_name}

        return self.execute_keyword(element_name, args, self.command_const.SAVEDTASKS_SELECT_TASK, **kwargs)

    def savedtasks_click_edit(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Edit toolbar button.  Assumes the task to edit is already selected.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SAVEDTASKS_CLICK_EDIT, **kwargs)

    def savedtasks_click_save_as(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Save As toolbar button.  Assumes the task to copy is already selected.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SAVEDTASKS_CLICK_SAVE_AS, **kwargs)

    def savedtasks_click_run(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Run toolbar button.  Assumes the task to run is already selected.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SAVEDTASKS_CLICK_RUN, **kwargs)

    def savedtasks_click_delete(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Delete toolbar button.  Assumes the task to delete is already selected.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SAVEDTASKS_CLICK_DELETE, **kwargs)

    def savedtasks_click_refresh(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Refresh toolbar button.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SAVEDTASKS_CLICK_REFRESH, **kwargs)

    def savedtasks_dialog_confirm_delete_click_yes(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Yes in the Confirm Delete dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SAVEDTASKS_DIALOG_CONFIRM_DELETE_CLICK_YES,
                                    **kwargs)

    def savedtasks_dialog_confirm_delete_click_no(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks No in the Confirm Delete dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SAVEDTASKS_DIALOG_CONFIRM_DELETE_CLICK_NO,
                                    **kwargs)

    def savedtasks_confirm_task_exists(self, element_name, task_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [task_name] -     Name of the task to look for
        [exists] -        Indicates whether the task is expected to be found or not (True/False)

        Confirms if the specified task exists or not.
        """
        args = {"task_name": task_name,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.SAVEDTASKS_CONFIRM_TASK_EXISTS, **kwargs)

    def savedtasks_wait_for_task_add(self, element_name, task_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [task_name] -     Name of the task to wait for

        Waits for the specified task to appear in the Saved Tasks table.
        """
        args = {"task_name": task_name}

        return self.execute_keyword(element_name, args, self.command_const.SAVEDTASKS_WAIT_FOR_TASK_ADD, **kwargs)

    def savedtasks_wait_for_task_remove(self, element_name, task_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [task_name] -     Name of the task to wait for

        Waits for the specified task to be removed from the Saved Tasks table.
        """
        args = {"task_name": task_name}

        return self.execute_keyword(element_name, args, self.command_const.SAVEDTASKS_WAIT_FOR_TASK_REMOVE, **kwargs)
