from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.license.LicenseAgreementWebElementsDefinitions import LicenseAgreementWebElementsDefinitions


class LicenseAgreementWebElements(LicenseAgreementWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_license_agreement_title(self):
        """
        :return: Gets the "License Agreement" title
        """
        return self.weh.get_element(self.license_agreement_title)

    def get_license_agreement_text_box(self):
        """
        :return: Gets the license agreement text box
        """
        return self.weh.get_element(self.license_agreement_text_box)

    def get_license_accept_checkbox(self):
        """
        :return: Gets the "I accept the License Agreement" checkbox
        """
        return self.weh.get_element(self.license_accept_checkbox)

    def get_license_next_button(self):
        """
        :return: Gets the Next button
        """
        return self.weh.get_element(self.license_next_button)
