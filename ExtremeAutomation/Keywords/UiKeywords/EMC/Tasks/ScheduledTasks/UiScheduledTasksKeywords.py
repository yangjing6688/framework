from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.ScheduledtasksConstants import ScheduledtasksConstants


class UiScheduledTasksKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiScheduledTasksKeywords, self).__init__()
        self.api_const = self.constants.API_SCHEDULED_TASKS
        self.command_const = ScheduledtasksConstants()

    def scheduledtasks_select_task(self, element_name, task_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [task_name] -     Name of the task to select

        Selects the specified scheduled task.
        """
        args = {"task_name": task_name}

        return self.execute_keyword(element_name, args, self.command_const.SCHEDULEDTASKS_SELECT_TASK, **kwargs)

    def scheduledtasks_click_add(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Add toolbar button.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCHEDULEDTASKS_CLICK_ADD, **kwargs)

    def scheduledtasks_click_edit(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Edit toolbar button.  Assumes the task to edit is already selected.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCHEDULEDTASKS_CLICK_EDIT, **kwargs)

    def scheduledtasks_click_copy(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Copy toolbar button.  Assumes the task to copy is already selected.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCHEDULEDTASKS_CLICK_COPY, **kwargs)

    def scheduledtasks_click_delete(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Delete toolbar button.  Assumes the task to delete is already selected.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCHEDULEDTASKS_CLICK_DELETE, **kwargs)

    def scheduledtasks_click_run(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Run toolbar button.  Assumes the task to run is already selected.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCHEDULEDTASKS_CLICK_RUN, **kwargs)

    def scheduledtasks_click_refresh(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Refresh toolbar button.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCHEDULEDTASKS_CLICK_REFRESH, **kwargs)

    def scheduledtasks_click_disable(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the Disable toolbar button.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCHEDULEDTASKS_CLICK_DISABLE, **kwargs)

    def scheduledtasks_click_smtp(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the SMTP toolbar button.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SCHEDULEDTASKS_CLICK_SMTP, **kwargs)

    def scheduledtasks_dialog_confirm_delete_click_yes(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks Yes in the Confirm Delete dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCHEDULEDTASKS_DIALOG_CONFIRM_DELETE_CLICK_YES, **kwargs)

    def scheduledtasks_dialog_confirm_delete_click_no(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks No in the Confirm Delete dialog.
        """
        args = {}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SCHEDULEDTASKS_DIALOG_CONFIRM_DELETE_CLICK_NO, **kwargs)

    def scheduledtasks_confirm_task_exists(self, element_name, task_name, exists, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [task_name] -     Name of the task to look for
        [exists] -        Indicates whether the task is expected to be found or not (True/False)

        Confirms if the specified task exists or not.
        """
        args = {"task_name": task_name,
                "exists": exists}

        return self.execute_keyword(element_name, args, self.command_const.SCHEDULEDTASKS_CONFIRM_TASK_EXISTS, **kwargs)

    def scheduledtasks_wait_for_task_add(self, element_name, task_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [task_name] -     Name of the task to wait for

        Waits for the specified task to appear in the Scheduled Tasks table.
        """
        args = {"task_name": task_name}

        return self.execute_keyword(element_name, args, self.command_const.SCHEDULEDTASKS_WAIT_FOR_TASK_ADD, **kwargs)

    def scheduledtasks_wait_for_task_remove(self, element_name, task_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [task_name] -     Name of the task to wait for

        Waits for the specified task to be removed from the Scheduled Tasks table.
        """
        args = {"task_name": task_name}

        return self.execute_keyword(element_name, args, self.command_const.SCHEDULEDTASKS_WAIT_FOR_TASK_REMOVE,
                                    **kwargs)
