from xiqse.defs.control.access_control.ControlAccessControlAddRemoveWebElementsDefinitions import *
from extauto.common.AutoActions import *
from extauto.common.WebElementHandler import *

class ControlAccessControlAddRemoveWebElements(ControlAccessControlAddRemoveWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def get_add_nac_appliance_tb_button(self):
        """
        :return: 'Add' button in the Add Device dialog toolbar
        """
        return self.weh.get_element(self.add_nac_appliance_tb_button)

    def get_id_for_ip_field(self):
        """
        :return: 'ID' for IP Address Field in the Add Device dialog
        """
        return self.weh.get_element(self.id_for_ip_field)

    def get_ip_field(self):
        """
        :return: 'IP Address' text field in the Add Device dialog
        """
        return self.weh.get_element(self.ip_field)

    def get_add_checkbox(self):
        """
        :return: Checkbox area in the Add Device dialog
        """
        return self.weh.get_element(self.add_checkbox)

    def get_add_button_dialog(self):
        """
        :return: Add Button in the Add Device dialog
        """
        return self.weh.get_element(self.add_button_dialog)

    def get_cancel_button_dialog(self):
        """
        :return: Cancel Button in the Add Device dialog
        """
        return self.weh.get_element(self.cancel_button_dialog)

    def get_save_ok_button(self):
        """
        :return: Okay Button in the dialog
        """
        return self.weh.get_element(self.save_ok_button)

    def get_save_successful(self):
        """
        :return: Save Button in the dialog
        """
        return self.weh.get_element(self.save_successful)

    def get_delete_nac_checkbox(self):
        """
        :return: Checkbox in a NAC delete dialog
        """
        return self.weh.get_element(self.delete_nac_checkbox)