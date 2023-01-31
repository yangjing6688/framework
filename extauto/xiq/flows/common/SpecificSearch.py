from time import sleep
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation
from extauto.xiq.elements.ApplicationSpecificSearchWebElements import ApplicationSpecificSearchWebElements
from extauto.xiq.elements.ApSpecificSearchWebElements import ApSpecificSearchWebElements


class SpecificSearch:
    def __init__(self):
        self.ap_web_elements = ApSpecificSearchWebElements()
        self.app_web_elements = ApplicationSpecificSearchWebElements()
        self.common_validation = CommonValidation()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def ap_specific_search(self, info, **kwargs):
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
                kwargs['pass_msg'] = "Information regarding AP appears in Devices Page"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = "'ap_specific_search()' -> There is no specific information about AP in" \
                                     " Devices page"
                self.common_validation.failed(**kwargs)
                return -1
        except Exception as e:
            self.utils.print_debug(e)
            kwargs['fail_msg'] = f"'ap_specific_search()' -> {e}"
            self.common_validation.fault(**kwargs)
            return -1

    def application_specific_search(self, info, **kwargs):
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
                kwargs['pass_msg'] = "Information regarding applicaton appears in Application Page"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = f"'application_specific_search()' -> Info message: '{info}' does not match the " \
                                     f"result message: '{result}'"
                self.common_validation.failed(**kwargs)
                return -1

        except Exception as e:
            self.utils.print_info(e)
            kwargs['fail_msg'] = f"'application_specific_search()' -> Error message: '{e}'"
            self.common_validation.fault(**kwargs)
            return -1

    def warning_search_close_window(self, info, **kwargs):
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
                kwargs['pass_msg'] = "Information Warning Page is available"
                self.common_validation.passed(**kwargs)
                return 1
            else:
                kwargs['fail_msg'] = f"'warning_search_close_window()' -> Info message: '{info}' does not match the" \
                                     f" result message: '{result}'"
                self.common_validation.failed(**kwargs)
                return -1
        except Exception as e:
            self.utils.print_info(e)
            kwargs['fail_msg'] = f"'warning_search_close_window()' -> Error message: '{e}'"
            self.common_validation.fault(**kwargs)
            return -1
