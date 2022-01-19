from extauto.common.WebElementHandler import *
from xiqse.defs.common.CommonErrorWebElementsDefinitions import *


class CommonErrorWebElements(CommonErrorWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_connection_lost_error_dialog(self):
        """
        :return: "Connection to server lost" error dialog
        """
        return self.weh.get_element(self.connection_lost_error_dialog)

    def get_session_terminated_dialog(self):
        """
        :return: "Session Terminated" dialog
        """
        return self.weh.get_element(self.session_terminated_dialog)

    def get_message_box_ok_button(self):
        """
        :return: OK button for the message box
        """
        return self.weh.get_element(self.message_box_ok_button)

    def get_message_box_yes_button(self):
        """
        :return: Yes button for the message box
        """
        return self.weh.get_element(self.message_box_yes_button)
