from common.WebElementHandler import *
from xiqse.defs.license.LicenseCommonWebElementsDefinitions import LicenseCommonWebElementsDefinitions


class LicenseCommonWebElements(LicenseCommonWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_welcome_title(self):
        """
        :return: Gets the "Welcome to ExtremeCloud IQ - Site Engine" title
        """
        return self.weh.get_element(self.welcome_title)

    def get_copyright_label(self):
        """
        :return: Gets the Copyright label
        """
        return self.weh.get_element(self.copyright_label)
