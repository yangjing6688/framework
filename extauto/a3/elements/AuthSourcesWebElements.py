from a3.defs.AuthSourcesWebElementDefs import AuthSourcesWebElementDefs
from common.AutoActions import AutoActions
from common.WebElementHandler import WebElementHandler


class AuthSourcesWebElements(AuthSourcesWebElementDefs):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()

    def get_auth_source_menu(self):
        return self.weh.get_element(self.auth_source_ui)

    def get_auth_source_button(self):
        return self.weh.get_element(self.auth_source_button)
