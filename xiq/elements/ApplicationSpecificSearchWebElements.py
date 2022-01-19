from xiq.defs.ApplicationSpecificSearchWebElementsDefinition import *
from common.WebElementHandler import *

class  ApplicationSpecificSearchWebElements(ApplicationSpecificSearchWebElementsDefinition):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_app_search_icon(self):
        return self.weh.get_element(self.app_specific_icon)

    def get_app_drop_down(self):
        return self.weh.get_element(self.app_drop_down)

    def get_app_text_box(self):
        return self.weh.get_element(self.app_text_box)

    def get_app_result(self):
        return self.weh.get_element(self.app_result)

    def get_warning_result(self):
        return self.weh.get_element(self.warning_result)

    def get_warning_close(self):
        return self.weh.get_element(self.warning_close)
