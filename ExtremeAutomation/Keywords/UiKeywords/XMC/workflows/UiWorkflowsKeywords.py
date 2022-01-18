from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XMC.WorkflowsConstants import WorkflowsConstants


class UiWorkflowsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiWorkflowsKeywords, self).__init__()
        self.api_const = self.constants.API_XMC_WORKFLOWS
        self.command_const = WorkflowsConstants()

    def expand_workflow_tree_panel_size(self, element_name, x, y, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [x]                     - Ending point of x co-ordinate
        [y]                     - Ending point of y co-ordinate

        Expand Workflows tree panel size (width)
        """
        args = {"x": x,
                "y": y
                }

        return self.execute_keyword(element_name, args, self.command_const.EXPAND_WORKFLOW_TREE_PANEL_SIZE, **kwargs)

    def expand_workflow_activity_panel_size(self, element_name, x, y, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [x]                     - Ending point of x co-ordinate
        [y]                     - Ending point of y co-ordinate

        Expand Workflows activity panel size (width)
        """
        args = {"x": x,
                "y": y
                }

        return self.execute_keyword(element_name, args, self.command_const.EXPAND_WORKFLOW_ACTIVITY_PANEL_SIZE,
                                    **kwargs)

    def collapse_all_user_workflow_items(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against

        Collapse all User Workflows items
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.COLLAPSE_ALL_USER_WORKFLOW_ITEMS, **kwargs)

    def select_workflows_tab(self, element_name, tab_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [tab_name]              - Workflows tab name

        Select workflows tab either User or System workflows
        """
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.SELECT_WORKFLOWS_TAB, **kwargs)

    def refresh_workflows(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against

        Refresh current Workflows open items
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.REFRESH_WORKFLOWS, **kwargs)

    def select_a_system_workflow(self, element_name, workflow_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [workflow_name]         - a system workflow name with absolute navigation path delimited by pipe symbol (|)

        Select a system workflow
        """
        args = {"workflow_name": workflow_name}

        return self.execute_keyword(element_name, args, self.command_const.SELECT_A_SYSTEM_WORKFLOW, **kwargs)

    def select_a_user_workflow(self, element_name, workflow_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [workflow_name]         - a user workflow name with absolute navigation path delimited by pipe symbol (|)

        Select a user workflow
        """
        args = {"workflow_name": workflow_name}

        return self.execute_keyword(element_name, args, self.command_const.SELECT_A_USER_WORKFLOW, **kwargs)

    def invoke_context_menu_for_user_workflow(self, element_name, treenodes, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [treenodes]             - User Workflows item with complete path

        Invoke popup menu for any one of the user workflows item
        """
        args = {"treenodes": treenodes}

        return self.execute_keyword(element_name, args, self.command_const.INVOKE_CONTEXT_MENU_FOR_USER_WORKFLOW,
                                    **kwargs)

    def invoke_context_menu_for_system_workflow(self, element_name, treenodes, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [treenodes]             - System Workflows item with complete path

        Invoke popup menu for any one of the system workflows item
        """
        args = {"treenodes": treenodes}

        return self.execute_keyword(element_name, args, self.command_const.INVOKE_CONTEXT_MENU_FOR_SYSTEM_WORKFLOW,
                                    **kwargs)

    def select_humburger_menu_item(self, element_name, menu_item, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [menu_item]              - menu item

        Select Humburger menu item
        """
        args = {"menu_item": menu_item}

        return self.execute_keyword(element_name, args, self.command_const.SELECT_HUMBURGER_MENU_ITEM, **kwargs)

    def create_workflow(self, element_name, wflow_name, wflow_description, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [wflow_name]            - Workflow name
        [wflow_description]     - Workflow description

        Create a new user workflow item
        """
        args = {"wflow_name": wflow_name,
                "wflow_description": wflow_description
                }

        return self.execute_keyword(element_name, args, self.command_const.CREATE_WORKFLOW, **kwargs)

    def create_workgroup(self, element_name, wgroup_name, wgroup_description, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [wflow_name]            - Workflow name
        [wgroup_description]    - Workgroup description

        Create a new user Workgroup item
        """
        args = {"wgroup_name": wgroup_name,
                "wgroup_description": wgroup_description
                }

        return self.execute_keyword(element_name, args, self.command_const.CREATE_WORKGROUP, **kwargs)

    def rename_workflow(self, element_name, wflow_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [wflow_name]            - workflow name

        Rename a user workflow item
        """
        args = {"wflow_name": wflow_name}

        return self.execute_keyword(element_name, args, self.command_const.RENAME_WORKFLOW, **kwargs)

    def rename_workgroup(self, element_name, wgroup_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [wgroup_name]           - workgroup name

        Rename a user workgroup item
        """
        args = {"wgroup_name": wgroup_name}

        return self.execute_keyword(element_name, args, self.command_const.RENAME_WORKGROUP, **kwargs)

    def save_workflow_as(self, element_name, wflow_name, wgroup_path=None, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [wflow_name]            - workflow name
        [wgroup_path]           - workgroup path

        Save workflow item as
        """
        args = {"wflow_name": wflow_name,
                "wgroup_path": wgroup_path
                }

        return self.execute_keyword(element_name, args, self.command_const.SAVE_WORKFLOW_AS, **kwargs)

    def run_workflow(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against

        Run a workflow
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.RUN_WORKFLOW, **kwargs)

    def select_a_device(self, element_name, tree_node, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [tree_node]             - a device IP

        Select and move a device
        """
        args = {"tree_node": tree_node}

        return self.execute_keyword(element_name, args, self.command_const.SELECT_A_DEVICE, **kwargs)

    def import_workflow(self, element_name, file_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [file_name]             - file name

        Import a workflow item
        """
        args = {"file_name": file_name}

        return self.execute_keyword(element_name, args, self.command_const.IMPORT_WORKFLOW, **kwargs)

    def toggle_mini_map(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against

        Toggle mini map
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.TOGGLE_MINI_MAP, **kwargs)

    def add_activity(self, element_name, name, x, y, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [name]                  - An activity name
        [x]                     - x co-ordinate
        [y]                     - y co-ordinate

        Add an activity
        """
        args = {"name": name,
                "x": x,
                "y": y
                }

        return self.execute_keyword(element_name, args, self.command_const.ADD_ACTIVITY, **kwargs)

    def delete_activity(self, element_name, name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [name]                  - An activity name

        Delete an activity
        """
        args = {"name": name}

        return self.execute_keyword(element_name, args, self.command_const.DELETE_ACTIVITY, **kwargs)

    def save_workflow(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against

        Save workflow changes
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SAVE_WORKFLOW, **kwargs)

    def collapse_workflows_tree_panel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against

        Collapse/Hide workflows tree panel view
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.COLLAPSE_WORKFLOWS_TREE_PANEL, **kwargs)

    def collapse_workflow_details_panel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against

        Collapse/Hide workflows details panel view
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.COLLAPSE_WORKFLOW_DETAILS_PANEL, **kwargs)

    def expand_workflows_tree_panel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against

        Invoke/Expand hidden workflows panel view
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.EXPAND_WORKFLOWS_TREE_PANEL, **kwargs)

    def expand_workflow_details_panel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against

        Invoke/Expand hidden workflows details panel view
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.EXPAND_WORKFLOW_DETAILS_PANEL, **kwargs)

    def verify_system_workflow_version(self, element_name, exp_version, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [exp_version]           - Expected/Current version of a workflow

        Verify a system workflow version
        """
        args = {"exp_version": exp_version}

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_SYSTEM_WORKFLOW_VERSION, **kwargs)

    def verify_workflow_control_tooltips(self, element_name, control_name, exp_tooltips, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [control_name]          - Control name
        [exp_tooltips]          - Expected tooltips for the control

        Verify a workflow control tooltips
        """
        args = {"control_name": control_name,
                "exp_tooltips": exp_tooltips
                }

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_WORKFLOW_CONTROL_TOOLTIPS, **kwargs)

    def verify_user_workflows_item_exists(self, element_name, workflow_item, flag="true", **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [workflow_item]         - A user workflow name
        [flag]                  - TRUE to check if exists
                                - FALSE to check if NOT exists

        Verify a user workflow item exists or not
        """
        args = {"workflow_item": workflow_item,
                "flag": flag
                }

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_USER_WORKFLOWS_ITEM_EXISTS, **kwargs)

    def verify_system_workflows_item_exists(self, element_name, workflow_item, flag="true", **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [workflow_item]         - A system workflow name
        [flag]                  - TRUE to check if exists
                                - FALSE to check if NOT exists

        Verify a system workflow item exists or not
        """
        args = {"workflow_item": workflow_item,
                "flag": flag
                }

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_SYSTEM_WORKFLOWS_ITEM_EXISTS,
                                    **kwargs)

    def verify_system_workflows_are_read_only(self, element_name, activity_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [activity_name]         - An activity name

        Verify a workflow mini map exists or not
        """
        args = {"activity_name": activity_name}

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_SYSTEM_WORKFLOWS_ARE_READ_ONLY,
                                    **kwargs)

    def verify_workflow_mini_map_exists(self, element_name, flag="true", **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [flag]                  - TRUE to check if exists
                                - FALSE to check if NOT exists

        Verify a workflow mini map exists or not
        """
        args = {"flag": flag}

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_WORKFLOW_MINI_MAP_EXISTS, **kwargs)

    def verify_workflow_changes_exist(self, element_name, activity_name, flag="true", **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [activity_name]         - activity name either added or removed from workflow diagram
        [flag]                  - TRUE to check if exists
                                - FALSE to check if NOT exists

        Verify workflow changes exist or not
        """
        args = {"activity_name": activity_name,
                "flag": flag
                }

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_WORKFLOW_CHANGES_EXIST, **kwargs)

    def verify_workflow_tree_panel_exists(self, element_name, flag="true", **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [flag]                  - TRUE to check if exists
                                - FALSE to check if NOT exists

        Verify a workflow tree panel exists (wide open)
        """
        args = {"flag": flag}

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_WORKFLOW_TREE_PANEL_EXISTS, **kwargs)

    def verify_workflow_details_panel_exists(self, element_name, flag="true", **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [flag]                  - TRUE to check if exists
                                - FALSE to check if NOT exists

        Verify a workflow details panel exists (wide open)
        """
        args = {"flag": flag}

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_WORKFLOW_DETAILS_PANEL_EXISTS,
                                    **kwargs)

    def verify_workflow_diagram_zoom_in(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against

        Verify a workflow diagram zoom in functionality
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_WORKFLOW_DIAGRAM_ZOOM_IN, **kwargs)

    def verify_workflow_diagram_zoom_out(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against

        Verify a workflow diagram zoom out functionality
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_WORKFLOW_DIAGRAM_ZOOM_OUT, **kwargs)

    def verify_workflow_validation_message(self, element_name, message, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [message]               - Validation message

        Verify a workflow Validation message
        """
        args = {"message": message}

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_WORKFLOW_VALIDATION_MESSAGE, **kwargs)
