from a3.defs.AuthSourcesWebElementDefs import *
from common.AutoActions import *
from common.WebElementHandler import *


class AuthSourcesWebElements(AuthSourcesWebElementDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_auth_source_menu(self):
        return self.weh.get_element(self.auth_source_ui)

