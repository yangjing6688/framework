from time import sleep
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.elements.ApplicationSpecificSearchWebElements import ApplicationSpecificSearchWebElements
from extauto.xiq.elements.ApSpecificSearchWebElements import ApSpecificSearchWebElements


class SpecificSearch:
    def __init__(self):
        self.ap_web_elements = ApSpecificSearchWebElements()
        self.app_web_elements = ApplicationSpecificSearchWebElements()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def ap_specific_search(self, info):
        """
        - searches information specific to AP in Devices page
        :return: 1 if successfully Search information about specific AP else -1
        """
        try:
            self.utils.print_info("Entering AP info in search:", info)
            sleep(5)
            self.auto_actions.send_keys(self.ap_web_elements.get_ap_specific_textbox(), info)
            sleep(3)
            self.auto_actions.click_reference(self.ap_web_elements.get_ap_specific_searchicon)
            popup1 = self.ap_web_elements.get_result_list()
            popup2 = self.ap_web_elements.get_result_even_row(popup1)
            matches = popup2.text
            lst = matches.splitlines()
            self.utils.print_info("lst: ", lst)
            if info in lst:
                return 1
            else:
                return -1
        except Exception as e:
            self.utils.print_debug(e)
            return -1

    def application_specific_search(self, info):
        """
        - searches information specific to application in Application page
         :return: 1 if successfully Search information about specific Application else -1
        """
        try:
            self.utils.print_info("Entering application info to search : ", info)
            sleep(5)
            self.auto_actions.click_reference(self.app_web_elements.get_app_search_icon)
            sleep(5)
            self.auto_actions.click_reference(self.app_web_elements.get_app_drop_down)
            sleep(5)
            self.auto_actions.send_keys(self.app_web_elements.get_app_text_box(), info)
            self.utils.print_info("results : ", self.app_web_elements.get_app_result().text)
            result = self.app_web_elements.get_app_result().text
            if info == result:
                return 1
            else:
                return -1

        except Exception as e:
            self.utils.print_info(e)
            return -1

    def warning_search_close_window(self, info):
        """
        - searches information specific to warning page
         :return: 1 if successfully Search information about specific Application else -1
        """
        try:
            self.utils.print_info("Search for: ", info)
            sleep(5)
            result = self.app_web_elements.get_warning_result().text
            if info == result:
                self.auto_actions.click_reference(self.app_web_elements.get_warning_close)
                sleep(5)
                return 1
            else:
                return -1
        except Exception as e:
            self.utils.print_info(e)
            return -1
