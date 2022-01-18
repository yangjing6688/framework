from common.WebElementHandler import *
from xiqse.defs.tasks.TasksWebElementsDefinitions import *


class TasksWebElements(TasksWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_workflow_dashboard_tab(self):
        """
        :return: Workflow Dashboard Tab on the Tasks page
        """
        return self.weh.get_element(self.workflow_dashboard_tab)

    def get_scheduled_tasks_tab(self):
        """
        :return: Scheduled Tasks Tab on the Tasks page
        """
        return self.weh.get_element(self.scheduled_tasks_tab)

    def get_saved_tasks_tab(self):
        """
        :return: Saved Tasks Tab on the Tasks page
        """
        return self.weh.get_element(self.saved_tasks_tab)

    def get_scripts_tab(self):
        """
        :return: Scripts Tab on the Tasks page
        """
        return self.weh.get_element(self.scripts_tab)

    def get_workflows_tab(self):
        """
        :return: Workflows Tab on the Tasks page
        """
        return self.weh.get_element(self.workflows_tab)
