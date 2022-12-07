from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.tasks.TasksWebElements import TasksWebElements


class XIQSE_Tasks(TasksWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_tasks_select_tab(self, tab_name):
        """
        - This keyword selects the specified tab of the Tasks page
        - Keyword Usage
        - ``XIQSE Tasks Select Tab    Workflow Dashboard``
        - ``XIQSE Tasks Select Tab    Scheduled Tasks``
        - ``XIQSE Tasks Select Tab    Saved Tasks``
        - ``XIQSE Tasks Select Tab    Scripts``
        - ``XIQSE Tasks Select Tab    Workflows``

        :param tab_name: name of the sub tab to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        if tab_name == "Workflow Dashboard":
            the_tab = self.get_workflow_dashboard_tab()
        elif tab_name == "Scheduled Tasks":
            the_tab = self.get_scheduled_tasks_tab()
        elif tab_name == "Saved Tasks":
            the_tab = self.get_saved_tasks_tab()
        elif tab_name == "Scripts":
            the_tab = self.get_scripts_tab()
        elif tab_name == "Workflows":
            the_tab = self.get_workflows_tab()
        else:
            the_tab = None
        if the_tab:
            self.utils.print_info(f"Selecting '{tab_name}' tab on Tasks page")
            self.auto_actions.click(the_tab)
            ret_val = 1
            sleep(2)
        else:
            self.utils.print_info(f"Unable to select tab with name '{tab_name}' on Tasks page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_tasks_select_workflow_dashboard_tab(self):
        """
        - This keyword selects the Workflow Dashboard tab of the Tasks page
        - Keyword Usage
        - ``XIQSE Tasks Select Workflow Dashboard Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_tasks_select_tab("Workflow Dashboard")

    def xiqse_tasks_select_scheduled_tasks_tab(self):
        """
        - This keyword selects the Scheduled Tasks tab of the Tasks page
        - Keyword Usage
        - ``XIQSE Tasks Select Scheduled Tasks Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_tasks_select_tab("Scheduled Tasks")

    def xiqse_tasks_select_saved_tasks_tab(self):
        """
        - This keyword selects the Saved Tasks tab of the Tasks page
        - Keyword Usage
        - ``XIQSE Tasks Select Saved Tasks Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_tasks_select_tab("Saved Tasks")

    def xiqse_tasks_select_scripts_tab(self):
        """
        - This keyword selects the Scripts tab of the Tasks page
        - Keyword Usage
        - ``XIQSE Tasks Select Scripts Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_tasks_select_tab("Scripts")

    def xiqse_tasks_select_workflows_tab(self):
        """
        - This keyword selects the Workflows tab of the Tasks page
        - Keyword Usage
        - ``XIQSE Tasks Select Workflows Tab``

        :return: 1 if action was successful, else -1
        """

        return self.xiqse_tasks_select_tab("Workflows")
