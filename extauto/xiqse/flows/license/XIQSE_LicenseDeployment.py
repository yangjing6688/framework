from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.license.LicenseDeploymentWebElements import LicenseDeploymentWebElements
from xiqse.elements.license.LicenseCommonWebElements import LicenseCommonWebElements


class XIQSE_LicenseDeployment(LicenseDeploymentWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.common_els = LicenseCommonWebElements()

    def xiqse_is_license_deployment_page_displayed(self):
        """
         - This keyword checks if the License Deployment page is being displayed.
         - Keyword Usage
          - ``XIQSE Is License Deployment Page Displayed``

        :return: 1 if page is displayed, else -1
        """
        ret_val = -1
        info_label = self.get_info_label()
        if info_label:
            self.utils.print_info("License Deployment page is displayed")
            ret_val = 1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_confirm_license_deployment_page_displayed(self):
        """
         - This keyword confirms the License Deployment page is being displayed.
         - Keyword Usage
          - ``XIQSE Confirm License Deployment Page Displayed``

        :return: 1 if page properly displayed, else -1
        """
        ret_val = -1
        welcome_title = self.common_els.get_welcome_title()
        info_label = self.get_info_label()
        onboard_radio = self.get_onboard_radio()
        airgap_radio = self.get_airgap_radio()
        next_button = self.get_next_button()
        copyright_label = self.common_els.get_copyright_label()
        if welcome_title and info_label and onboard_radio and airgap_radio and next_button and copyright_label:
            self.utils.print_info("License Deployment page is properly displayed")
            ret_val = 1
        else:
            self.utils.print_info("License Deployment page is not properly displayed")
            if not welcome_title:
                self.utils.print_info("  Unable to find 'Welcome to Extreme Cloud IQ - Site Engine' title")
            if not info_label:
                self.utils.print_info("  Unable to find 'Select the deployment model...' label")
            if not onboard_radio:
                self.utils.print_info("  Unable to find Onboard radio button")
            if not airgap_radio:
                self.utils.print_info("  Unable to find Air Gap radio button")
            if not next_button:
                self.utils.print_info("  Unable to find Next button")
            if not copyright_label:
                self.utils.print_info("  Unable to find copyright label")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_confirm_license_deployment_onboard_radio_selected(self):
        """
         - This keyword confirms the Onboard to ExtremeCloud IQ radio button is selected.
         - Keyword Usage
          - ``XIQSE Confirm Onboard Radio Selected``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        onboard_radio = self.get_onboard_radio()
        if onboard_radio:
            if onboard_radio.is_selected():
                self.utils.print_info("Onboard radio button is selected")
                ret_val = 1
            else:
                self.utils.print_info("Onboard radio button is not selected")
        else:
            self.utils.print_info("Unable to find Onboard radio button")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_confirm_license_deployment_airgap_radio_selected(self):
        """
         - This keyword confirms the Airgap radio button is selected.
         - Keyword Usage
          - ``XIQSE Confirm Airgap Radio Selected``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        airgap_radio = self.get_airgap_radio()
        if airgap_radio:
            if airgap_radio.is_selected():
                self.utils.print_info("Airgap radio button is selected")
                ret_val = 1
            else:
                self.utils.print_info("Airgap radio button is not selected")
        else:
            self.utils.print_info("Unable to find Airgap radio button")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_license_deployment_select_onboard_radio(self):
        """
         - This keyword selects the Onboard radio button on the license deployment page.
         - Keyword Usage
          - ``XIQSE License Deployment Select Onboard Radio``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        onboard_radio = self.get_onboard_radio()
        if onboard_radio:
            self.utils.print_info("Selecting the Onboard radio button")
            self.auto_actions.select_radio_button(onboard_radio)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find Onboard radio button")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_license_deployment_select_airgap_radio(self):
        """
         - This keyword selects the Airgap radio button on the license deployment page.
         - Keyword Usage
          - ``XIQSE License Deployment Select Airgap Radio``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        airgap_radio = self.get_airgap_radio()
        if airgap_radio:
            self.utils.print_info("Selecting the Airgap radio button")
            self.auto_actions.select_radio_button(airgap_radio)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find Airgap radio button")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_license_deployment_click_next(self):
        """
         - This keyword clicks the Next button on the license deployment page.
         - Keyword Usage
          - ``XIQSE License Deployment Click Next``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        next_button = self.get_next_button()
        if next_button:
            self.utils.print_info("Clicking Next")
            self.auto_actions.click(next_button)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find Next button")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val
