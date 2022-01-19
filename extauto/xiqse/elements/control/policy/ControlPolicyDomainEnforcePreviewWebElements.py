from extauto.common.WebElementHandler import *
from xiqse.defs.control.policy.ControlPolicyDomainEnforcePreviewWebElementsDefinitions import *


class ControlPolicyDomainEnforcePreviewWebElements(ControlPolicyDomainEnforcePreviewWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    # Enforce Preview window
    def get_enforce_preview_enforce_button(self):
        """
         :return:  "'Enforce' button in the Enforce Preview window"
         """
        return self.weh.get_element(self.enforce_preview_enforce_button)

    def get_enforce_preview_cancel_button(self):
        """
         :return:  "'Cancel' button in the Enforce Preview window"
         """
        return self.weh.get_element(self.enforce_preview_cancel_button)

    def get_enforce_preview_close_button(self):
        """
         :return:  "'Close' button in the Enforce Preview window"
         """
        return self.weh.get_element(self.enforce_preview_close_button)

    def get_enforce_preview_check_device_present(self, device_ip):
        """
         :return:  "'1' if the device is present in the Enforce Preview window"
         """
        return self.weh.get_template_elements(self.enforce_preview_device, ip=device_ip)

    def get_show_on_enforce_checkbox(self):
        """
         :return:  "setting for the 'show on enforce' checkbox in the Enforce Preview window"
         """
        return self.weh.get_element(self.show_on_enforce_checkbox)

    # end of Enforce Preview window