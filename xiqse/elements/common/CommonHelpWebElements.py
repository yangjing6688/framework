from common.WebElementHandler import *
from xiqse.defs.common.CommonHelpWebElementsDefinitions import *


class CommonHelpWebElements(CommonHelpWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_help_panel(self):
        """
        :return: Gets the help panel
        """
        return self.weh.get_element(self.help_panel)

    def get_help_panel_title(self):
        """
        :return: Gets the title of the help panel
        """
        return self.weh.get_element(self.help_panel_title)
