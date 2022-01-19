__author__ = "ExtremeNetworks"
__version__ = "1.0.1"

from common.tools.remote.captiveportal.CPWebElements import CPWebElements


class CaptivePortal(CPWebElements):
    def __init__(self):
        super().__init__()

    def accept_user_acceptance_page1(self):
        """
        accept the user acceptance button on the user acceptance page to get access to the network
        :return:
        """
        accept_button = self.get_acceptance_button()
        accept_button.click()
        page_title = self.get_page_title
        print(page_title)
        if "Secure Internet Portal" in page_title:
            return 1
