from time import sleep
from extauto.common.WebElementHandler import *
from extauto.common.AutoActions import AutoActions
from extauto.common.Utils import Utils
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.common.CommonValidation import CommonValidation


class WebElementController:
    def __init__(self):
        self.weh = WebElementHandler()
        self.auto_actions = AutoActions()
        self.utils = Utils()
        self.devices_web_elements = DevicesWebElements()
        self.common_validation = CommonValidation()

    def is_web_element_present(self, web_element):
        """
        Check to see Element is present or not.
        :param web_element: web element
        :return: 1 if element is present, -1 when element is not present
        """
        if web_element:
            self.utils.print_info("Web Element is present")
            return 1
        self.utils.print_info("Web Element is not present")
        return -1

    def action_method(self, action_method, get_web_element_method, **kwargs):
        """
            - This keyword is used to do a certain action using a web element
            - In case of Stale Reference Exception, try to get the web element again
            - Retry times = 3
        :param action_method: The action method - e.g. click, move_to_element, etc
        :param get_web_element_method: The method used to get the web element
                                        - e.g. devices_web_elements.get_refresh_devices_page
        :return: 1 if the action was done, -1 is it was unable to complete it
        """

        for retry_count in range(3):
            web_element = get_web_element_method()
            try:
                if self.is_web_element_present(web_element):
                    action_method(get_web_element_method())
                    kwargs['pass_msg'] = f"Action done successfully"
                    self.common_validation.validate(1, 1, **kwargs)
                    return 1
            except StaleElementReferenceException:
                self.utils.print_info("Retry the certain action on element '{}' for {} times".format(web_element,
                                                                                                     retry_count))
                sleep(1)
            except ElementNotInteractableException:
                self.utils.print_info(
                    "Retry the certain action on element '{}' not in view for {} times".format(web_element,
                                                                                               retry_count))
                sleep(1)
            except ElementClickInterceptedException:
                self.utils.print_info(
                    "Element '{}' is intersected by another element. Retry for {} times".format(web_element,
                                                                                                retry_count))
                sleep(1)

        kwargs['fail_msg'] = "FAIL - Unable to complete the action"
        self.common_validation.validate(-1, 1, **kwargs)
        return -1
