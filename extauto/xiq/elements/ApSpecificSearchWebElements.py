from extauto.xiq.defs.ApSpecificSearchWebElementsDefinition import *
from extauto.common.WebElementHandler import *


class ApSpecificSearchWebElements(ApSpecificSearchWebElementsDefinition):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_ap_specific_searchicon(self):
        return self.weh.get_element(self.ap_specific_searchicon)

    def get_ap_specific_textbox(self):
        return self.weh.get_element(self.ap_specific_textbox)

    def get_result_list(self):
        return self.weh.get_element(self.ap_result_list)

    def get_result_even_row(self, popup):
        return self.weh.get_element(self.ap_result_even_row, parent=popup)
