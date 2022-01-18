from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.OpspanelConstants import OpspanelConstants


class UiOpsPanelKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiOpsPanelKeywords, self).__init__()
        self.api_const = self.constants.API_OPSPANEL
        self.command_const = OpspanelConstants()

    def opspanel_click_operations(self, element_name, **kwargs):
        """Returns the result of opspanel_click_operations."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.OPSPANEL_CLICK_OPERATIONS, **kwargs)

    def opspanel_clear_all(self, element_name, **kwargs):
        """Returns the result of opspanel_clear_all."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.OPSPANEL_CLICK_CLEAR_ALL, **kwargs)

    def opspanel_confirm_type_exists(self, element_name, operation_type, exists, **kwargs):
        """Returns the result of opspanel_confirm_type_exists."""
        args = {'operation_type': operation_type,
                'exists': exists}

        return self.execute_keyword(element_name, args, self.command_const.OPSPANEL_CONFIRM_TYPE_EXISTS, **kwargs)

    def opspanel_confirm_result_exists(self, element_name, msg_result, exists, **kwargs):
        """Returns the result of opspanel_confirm_result_exists."""
        args = {'msg_result': msg_result,
                'exists': exists}

        return self.execute_keyword(element_name, args, self.command_const.OPSPANEL_CONFIRM_RESULT_EXISTS, **kwargs)

    def opspanel_confirm_message_exists(self, element_name, message, exists, max_wait=0, **kwargs):
        """Returns the result of opspanel_confirm_message_exists."""
        args = {'message': message,
                'exists': exists,
                'max_wait': max_wait}

        return self.execute_keyword(element_name, args, self.command_const.OPSPANEL_CONFIRM_MESSAGE_EXISTS, **kwargs)

    def opspanel_confirm_target_exists(self, element_name, target, exists, **kwargs):
        """Returns the result of opspanel_confirm_target_exists."""
        args = {'target': target,
                'exists': exists}

        return self.execute_keyword(element_name, args, self.command_const.OPSPANEL_CONFIRM_TARGET_EXISTS, **kwargs)

    def opspanel_confirm_all_parameters_exist(self, element_name, event_type=None, event_target=None, event_result=None,
                                              event_message=None, exists=True, max_attempts=0, **kwargs):
        """Returns the result of opspanel_confirm_all_parameters_exist."""
        args = {'event_type': event_type,
                'event_target': event_target,
                'event_result': event_result,
                'event_message': event_message,
                'exists': exists,
                'max_attempts': max_attempts}

        return self.execute_keyword(element_name, args, self.command_const.OPSPANEL_CONFIRM_ALL_PARAMETERS_EXIST,
                                    **kwargs)
