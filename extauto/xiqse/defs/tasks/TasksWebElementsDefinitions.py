

class TasksWebElementsDefinitions:

    workflow_dashboard_tab = \
        {
            'DESC': 'Tasks> Workflow Dashboard Tab',
            'XPATH': '//span[text()="Workflow Dashboard" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    scheduled_tasks_tab = \
        {
            'DESC': 'Tasks> Scheduled Tasks Tab',
            'XPATH': '//span[text()="Scheduled Tasks" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    saved_tasks_tab = \
        {
            'DESC': 'Tasks> Saved Tasks Tab',
            'XPATH': '//span[text()="Saved Tasks" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    scripts_tab = \
        {
            'DESC': 'Tasks> Scripts Tab',
            'XPATH': '//span[text()="Scripts" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    workflows_tab = \
        {
            'DESC': 'Tasks> Workflows Tab',
            'XPATH': '//span[text()="Workflows" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }
