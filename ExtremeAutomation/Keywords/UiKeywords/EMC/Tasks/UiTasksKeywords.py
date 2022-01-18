from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.TasksConstants import TasksConstants


class UiTasksKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiTasksKeywords, self).__init__()
        self.api_const = self.constants.API_TASKS
        self.command_const = TasksConstants()

    def tasks_select_sub_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [tab_name] -      Name of the sub tab to select

        Selects the specified sub tab of the main Tasks tab.
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.TASKS_SELECT_SUB_TAB, **kwargs)
