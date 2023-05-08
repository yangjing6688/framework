from time import sleep
from extauto.common.Utils import Utils
from extauto.common.CommonValidation import CommonValidation


class WebElementController:
    def __init__(self):
        self.utils = Utils()
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

    def action_method(self, action_method, get_web_element_method, retry_times=10, **kwargs):
        """
        - This keyword is used to do a certain action using a web element
        - In case of Stale Reference Exception, try to get the web element again
        - Retry times = 10

        :param action_method: The action method - e.g. click, move_to_element, etc
        :param get_web_element_method: The method used to get the web element
                                        - e.g. devices_web_elements.get_refresh_devices_page
        :return: 1 if the action was done, -1 is it was unable to complete it
        """

        # Validate parameters
        if not callable(action_method):
            kwargs['fail_msg'] = "action_method is not a callable function"
            self.common_validation.fault(**kwargs)
        if not callable(get_web_element_method):
            kwargs['fail_msg'] = "get_web_element_method is not a callable function"
            self.common_validation.fault(**kwargs)
        if not isinstance(retry_times, int):
            kwargs['fail_msg'] = "retry_times is not an int"
            self.common_validation.fault(**kwargs)

        # Try to complete the requested action after getting the webelement retry_times times
        for retry_count in range(retry_times):
            web_element = get_web_element_method()
            try:
                if self.is_web_element_present(web_element):
                    action_method(web_element)
                    return 1
                else:
                    method_name = str(get_web_element_method)
                    self.utils.print_info(f"web_element returned from: {method_name} is not present")
            except Exception as e:
                self.utils.print_info(f"Exception on action for an element: '{e}'")

            self.utils.print_info(f"Retrying the action on element: '{web_element}' Attempt number: {retry_count+1} of {retry_times}")
            sleep(5)

        action_method_name = str(action_method)
        kwargs['fail_msg'] = f"FAIL - Unable to complete the action {action_method_name}"
        self.common_validation.fault(**kwargs)
        return -1
