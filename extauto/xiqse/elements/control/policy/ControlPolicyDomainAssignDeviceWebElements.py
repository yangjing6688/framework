from common.WebElementHandler import *
from xiqse.defs.control.policy.ControlPolicyDomainAssignDeviceWebElementsDefinitions import *


class ControlPolicyDomainAssignDeviceWebElements(ControlPolicyDomainAssignDeviceWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

     # Assign Device(s) to Domain
    def get_assign_all_devices_node(self):
        """
        :return:  "All Devices node in the Assign Device(s) to Domain window"
        """
        return self.weh.get_element(self.assign_all_devices_node)

    def get_assign_find_device(self, device_ip):
        """
        :param device_ip:
        :return:  Device node in the left panel in Assign Device(s) to Domain window
        """
        return self.weh.get_template_element(self.device_els_active_template, ip=device_ip)

    def get_assign_add_button(self):
        """
        :return:  "Add button in the Assign Device(s) to Domain window"
        """
        return self.weh.get_element(self.assign_add_button)

    def get_assign_cancel_button(self):
        """
        :return:  "Cancel button in the Assign Device(s) to Domain window"
        """
        return self.weh.get_element(self.assign_cancel_button)

    def get_assign_ok_button(self):
        """
        :return:  "OK button in the Assign Device(s) to Domain window"
        """
        return self.weh.get_element(self.assign_ok_button)
    # End of Assign Device(s) to Domain
