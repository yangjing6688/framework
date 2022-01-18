from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XMC.HomeConstants import HomeConstants


class UiHomeKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiHomeKeywords, self).__init__()
        self.api_const = self.constants.API_XMC_HOME
        self.command_const = HomeConstants()

    def open_operation_panel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against

        Open an operations panel
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.OPEN_OPERATION_PANEL, **kwargs)

    def close_operation_panel(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against

        Close an operations panel
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.CLOSE_OPERATION_PANEL, **kwargs)

    def wait_for_operation(self, element_name, operation_name, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [operation_name]       - An operation name which is looked for

        Wait for an operation specific status
        """
        args = {"operation_name": operation_name}

        return self.execute_keyword(element_name, args, self.command_const.WAIT_FOR_OPERATION, **kwargs)

    def verify_operation_status(self, element_name, operation_name, status_message, **kwargs):
        """
        Keyword Arguments:
        [element_names]         - List of elements the keyword will be run against
        [operation_name]        - Name of the operation status to be tracked
        [status_message]        - Operation status message to be verified

        Get an operation status and verify the same
        """
        args = {"operation_name": operation_name,
                "status_message": status_message
                }

        return self.execute_keyword(element_name, args, self.command_const.VERIFY_OPERATION_STATUS, **kwargs)
