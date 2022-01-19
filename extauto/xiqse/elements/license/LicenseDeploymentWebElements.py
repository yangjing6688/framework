from extauto.common.WebElementHandler import *
from xiqse.defs.license.LicenseDeploymentWebElementsDefinitions import LicenseDeploymentWebElementsDefinitions


class LicenseDeploymentWebElements(LicenseDeploymentWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_info_label(self):
        """
        :return: Gets the "Select the deployment..." information label
        """
        return self.weh.get_element(self.info_label)

    def get_onboard_radio(self):
        """
        :return: Gets the "Onboard to ExtremeCloud IQ" radio button
        """
        return self.weh.get_element(self.onboard_radio)

    def get_airgap_radio(self):
        """
        :return: Gets the "Enter entitlement(s) for air gapped ExtremeCloud IQ - Site Engine" radio button
        """
        return self.weh.get_element(self.airgap_radio)

    def get_next_button(self):
        """
        :return: Gets the Next button
        """
        return self.weh.get_element(self.next_button)
