from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.license.LicenseAgreementWebElements import LicenseAgreementWebElements
from xiqse.elements.license.LicenseCommonWebElements import LicenseCommonWebElements


class XIQSE_LicenseAgreement(LicenseAgreementWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.common_els = LicenseCommonWebElements()

    def xiqse_confirm_license_agreement_page_displayed(self):
        """
        - This keyword confirms the License Agreement page is being displayed.
        - Keyword Usage
        - ``XIQSE Confirm License Agreement Page Displayed``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        welcome_title = self.common_els.get_welcome_title()
        license_title = self.get_license_agreement_title()
        license_text = self.get_license_agreement_text_box()
        accept_check = self.get_license_accept_checkbox()
        copyright_label = self.common_els.get_copyright_label()
        if welcome_title and license_title and license_text and accept_check and copyright_label:
            self.utils.print_info("License Agreement page is properly displayed")
            ret_val = 1
        else:
            self.utils.print_info("License Agreement page is not properly displayed")
            if not welcome_title:
                self.utils.print_info("  Unable to find 'Welcome to Extreme Cloud IQ - Site Engine' title")
            if not license_title:
                self.utils.print_info("  Unable to find 'License Agreement' title")
            if not license_text:
                self.utils.print_info("  Unable to find License Agreement text box")
            if not accept_check:
                self.utils.print_info("  Unable to find 'I accept the License Agreement' checkbox")
            if not copyright_label:
                self.utils.print_info("  Unable to find copyright label")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_confirm_accept_license_agreement_checkbox_deselected(self):
        """
        - This keyword confirms the checkbox to select the license agreement is deselected.
        - Keyword Usage
        - ``XIQSE Confirm Accept License Agreement Checkbox Deselected``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        accept_check = self.get_license_accept_checkbox()
        if accept_check:
            if not accept_check.is_selected():
                self.utils.print_info("Accept License Agreement checkbox is deselected")
                ret_val = 1
            else:
                self.utils.print_info("Accept License Agreement checkbox is selected")
        else:
            self.utils.print_info("Unable to find 'I accept the License Agreement' checkbox")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_confirm_accept_license_agreement_checkbox_selected(self):
        """
        - This keyword confirms the checkbox to select the license agreement is selected.
        - Keyword Usage
        - ``XIQSE Confirm Accept License Agreement Checkbox Selected``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        accept_check = self.get_license_accept_checkbox()
        if accept_check:
            if accept_check.is_selected():
                self.utils.print_info("Accept License Agreement checkbox is selected")
                ret_val = 1
            else:
                self.utils.print_info("Accept License Agreement checkbox is deselected")
        else:
            self.utils.print_info("Unable to find 'I accept the License Agreement' checkbox")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_confirm_license_agreement_next_button_disabled(self):
        """
        - This keyword confirms the Next button is disabled.
        - Keyword Usage
        - ``XIQSE Confirm License Agreement Next Button Disabled``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        next_button = self.get_license_next_button()
        if next_button:
            if next_button.get_attribute("disabled"):
                self.utils.print_info("License Agreement 'Next' button is disabled")
                ret_val = 1
            else:
                self.utils.print_info("License Agreement 'Next' button is enabled")
        else:
            self.utils.print_info("Unable to find License Agreement 'Next' button")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_confirm_license_agreement_next_button_enabled(self):
        """
        - This keyword confirms the Next button is enabled.
        - Keyword Usage
        - ``XIQSE Confirm License Agreement Next Button Enabled``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        next_button = self.get_license_next_button()
        if next_button:
            if not next_button.get_attribute("disabled"):
                self.utils.print_info("License Agreement 'Next' button is enabled")
                ret_val = 1
            else:
                self.utils.print_info("License Agreement 'Next' button is disabled")
        else:
            self.utils.print_info("Unable to find License Agreement 'Next' button")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_accept_license_agreement(self):
        """
        - This keyword selects the "I accept the License Agreement" checkbox.
        - Keyword Usage
        - ``XIQSE Accept License Agreement``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        accept_check = self.get_license_accept_checkbox()
        if accept_check:
            self.utils.print_info("Selecting the check box to accept the license agreement")
            self.auto_actions.enable_check_box(accept_check)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'I accept the License Agreement' checkbox")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_decline_license_agreement(self):
        """
        - This keyword deselects the "I accept the License Agreement" checkbox.
        - Keyword Usage
        - ``XIQSE Decline License Agreement``

        :return: 1 if action successful, else -1
        """
        ret_val = -1
        accept_check = self.get_license_accept_checkbox()
        if accept_check:
            self.utils.print_info("Deselecting the check box to decline the license agreement")
            self.auto_actions.disable_check_box(accept_check)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'I accept the License Agreement' checkbox")

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_accept_license_agreement_and_click_next(self):
        """
        - This keyword selects the "I accept the License Agreement" checkbox and clicks Next.
        - Keyword Usage
        - ``XIQSE Accept License Agreement and Click Next``

        :return: 1 if action successful, else -1
        """
        ret_val = self.xiqse_accept_license_agreement()
        if ret_val == 1:
            next_button = self.get_license_next_button()
            if next_button:
                if not next_button.get_attribute("disabled"):
                    self.utils.print_info("Clicking License Agreement 'Next' button")
                    self.auto_actions.click(next_button)
                else:
                    self.utils.print_info("License Agreement 'Next' button is disabled")
                    ret_val = -1
            else:
                self.utils.print_info("Unable to find License Agreement 'Next' button")
                ret_val = -1

        if ret_val == -1:
            self.screen.save_screen_shot()

        return ret_val
