from xiqse.defs.control.access_control.ControlAccessControlCommonWebElementsDefinitions import *
from common.AutoActions import *
from common.WebElementHandler import *

class ControlAccessControlCommonWebElements(ControlAccessControlCommonWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def get_element_field(self, element_id):
        """
        :return: Once you find element using id, you can return element
        """
        return self.weh.get_template_element(self.element_field, element_name=element_id)

    def get_click_innerel_button(self, button):
        """
        :return: Using btnInnerEl and Text, click on the button
        """
        return self.weh.get_template_element(self.click_innerel_button, element_name=button)

    def select_tab_panel(self, tab):
        """
        :return: Using panel and btn and Text, select tabs in the right panel
        """
        return self.weh.get_template_element(self.tab_panel, element_name=tab)
