import time
from selenium.webdriver.common.action_chains import ActionChains
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Device.Common.Agents.BaseSeleniumAgent import BaseSeleniumAgent
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class SeleniumAgent(BaseSeleniumAgent):
    def __init__(self, device):
        super(SeleniumAgent, self).__init__(device)
        self.driver = None

    def close_web_page(self, **kwargs):
        """
        Required kwargs:
        None

        This function will close the browser and browser driver.
        """
        self.driver.close()
        time.sleep(5)
        self.driver.quit()
        time.sleep(5)
        self.driver = None

    def click(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that should be clicked.

        This function will click the given target if it can be located on the page.
        """
        strategy, target = self._check_kwargs(kwargs, "strategy", "target")

        action_target = self.find_element(target, strategy)

        if not self.check_modifier_keys(**kwargs):
            action_target.click()
        else:
            action_chain = ActionChains(self.driver)
            action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.click, action_target)
            action_chain.perform()

    def click_boundlist_item(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that should be double clicked.
        [boundslist_item] - The text of the item in the bounds list to match on
        This function will double click the given target if it can be located on the page.
        """
        strategy, target, boundlist_item = self._check_kwargs(kwargs, "strategy", "target", "boundlist_item")
        list_items = self.find_elements(target, strategy)
        for list_item in list_items:
            if list_item.text == boundlist_item:
                list_item.click()

    def double_click(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that should be double clicked.

        This function will double click the given target if it can be located on the page.
        """
        strategy, target = self._check_kwargs(kwargs, "strategy", "target")

        action_target = self.find_element(target, strategy)

        action_chain = ActionChains(self.driver)
        action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.double_click, action_target)
        action_chain.perform()

    def right_click(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that should be right clicked.

        This function will right click the given target if it can be located on the page.
        """
        strategy, target = self._check_kwargs(kwargs, "strategy", "target")

        action_target = self.find_element(target, strategy)

        action_chain = ActionChains(self.driver)
        action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.context_click, action_target)
        action_chain.perform()

    def mouse_down(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that should be clicked and held.

        This function will hold a mouse click down on the given target if it can be located on the page.
        """
        strategy, target = self._check_kwargs(kwargs, "strategy", "target")

        action_target = self.find_element(target, strategy)

        action_chain = ActionChains(self.driver)
        action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.click_and_hold, action_target)
        action_chain.perform()

    def mouse_up(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that the mouse button should be released on.

        This function will release the mouse button on the given target if it can be located on the page.
        """
        strategy, target = self._check_kwargs(kwargs, "strategy", "target")

        action_target = self.find_element(target, strategy)

        action_chain = ActionChains(self.driver)
        action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.release, action_target)
        action_chain.perform()

    def move_cursor(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that the cursor should be moved to.

        This function will move the mouse cursor to the given target if it can be located on the page.
        """
        strategy, target = self._check_kwargs(kwargs, "strategy", "target")

        action_target = self.find_element(target, strategy)

        action_chain = ActionChains(self.driver)
        action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.move_to_element, action_target)
        action_chain.perform()

    def move_cursor_out_of_element(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that the cursor should be moved to.

        This function will move the mouse cursor to the given target if it can be located on the page.
        """
        strategy, target = self._check_kwargs(kwargs, "strategy", "target")

        action_target = self.find_element(target, strategy)

        size = action_target.size
        x = (size['width'] / 2) + 1
        y = (size['height'] / 2) + 1

        action_chain = ActionChains(self.driver)
        action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.move_to_element, action_target)
        action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.move_by_offset, [x, y])
        action_chain.perform()

    def get_text_from_element_and_compare(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element
        [text] - The text to compare to

        This function will find the element and use the selenium method text. Once the text is received we compare
        against the text the user expects
        """
        strategy, target, text = self._check_kwargs(kwargs, "strategy", "target", "text")
        try:
            action_target = self.find_element(target, strategy)
            compare_to_text = action_target.text
            self.logger.log_info("Expected Web Element Text =" + text)
            self.logger.log_info("Web Element Text =" + compare_to_text)
            if compare_to_text != text:
                self.logger.log_info("Expected Web Element Text and Web Element Text were NOT equal")
                return self.constants.FAILURE_GET_TEXT_FROM_ELEMENT_AND_COMPARE
            self.logger.log_info("Expected Web Element Text and Web Element Text were equal")
        except AttributeError:
            return self.constants.FAILURE_GET_TEXT_FROM_ELEMENT_AND_COMPARE

    def get_attribute_from_element_and_compare(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element
        [text] - The text/value to compare to
        [attribute] - the attribute of the web elemeent to get

        This function will find the element and use the selenium method get_attribute with the attribute the user wants.
        Once the text/value is received we compare against the text/value the user expects
        """
        strategy, target, value, attribute = self._check_kwargs(kwargs, "strategy", "target", "value", "attribute")
        try:
            action_target = self.find_element(target, strategy)
            compare_to_attribute = action_target.get_attribute(attribute)
            self.logger.log_info("Attribute To Find =" + attribute)
            self.logger.log_info("Expected Web Element " + attribute + " =" + value)
            self.logger.log_info("Web Element " + attribute + " =" + compare_to_attribute)
            if compare_to_attribute != value:
                self.logger.log_info("Expected Web Element " + attribute + " and Web Element " +
                                     attribute + " were NOT equal")
                return self.constants.FAILURE_GET_ATTRIBUTE_FROM_ELEMENT_AND_COMPARE
            self.logger.log_info("Expected Web Element " + attribute + " and Web Element " +
                                 attribute + " were equal")
        except AttributeError:
            self.logger.log_info("Attribute Error")
            return self.constants.FAILURE_GET_ATTRIBUTE_FROM_ELEMENT_AND_COMPARE

    def element_exists(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element
        [exists] - Whether the element should exist or not

        This function will find the element and determine whether it should exists or not based upon
        the users input
        """
        strategy, target, exists = self._check_kwargs(kwargs, "strategy", "target", "exists")
        try:
            action_target = self.find_element(target, strategy)
            if action_target is not None and not StringUtils.string_to_boolean(exists):
                self.logger.log_info("Web Element Does NOT Exist")
                return self.constants.FAILURE_ELEMENT_EXISTS
            self.logger.log_info("Web Element Does Exist")
        except self.common_exceptions:
            if not StringUtils.string_to_boolean(exists):
                self.logger.log_info("Web Element Does NOT Exist")
                return self.constants.FAILURE_ELEMENT_EXISTS
            self.logger.log_info("Web Element Does Exist")

    def is_element_enabled(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element

        This function will determine if an element is enabled and return a boolean value back
        """
        strategy, target, enabled = self._check_kwargs(kwargs, "strategy", "target", "enabled")
        try:
            web_obj = self.find_element(target, strategy)
            self.logger.log_info("Enabled Arg Is Set To:" + enabled)
            is_enabled = web_obj.is_enabled()
            self.logger.log_info("Web Element Is Enabled:" + is_enabled)
            if is_enabled is not None and not StringUtils.string_to_boolean(enabled):

                return self.constants.FAILURE_IS_ELEMENT_ENABLED
        except self.common_exceptions:
            if not StringUtils.string_to_boolean(enabled):
                return self.constants.FAILURE_IS_ELEMENT_ENABLED

    def is_element_selected(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element

        This function will determine if an element is selected and return a boolean value back
        """
        strategy, target, selected = self._check_kwargs(kwargs, "strategy", "target", "selected")
        try:
            web_obj = self.find_element(target, strategy)
            self.logger.log_info("Selected Arg Is Set To:" + selected)
            is_selected = web_obj.is_selected()
            self.logger.log_info("Web Element Is Selected:" + is_selected)
            if web_obj.is_selected() is not None and not StringUtils.string_to_boolean(selected):
                return self.constants.FAILURE_IS_ELEMENT_SELECTED
        except self.common_exceptions:
            if not StringUtils.string_to_boolean(selected):
                return self.constants.FAILURE_IS_ELEMENT_SELECTED

    def is_element_displayed(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element

        This function will determine if an element is displayed is enabled and return a boolean value back
        """
        strategy, target, displayed = self._check_kwargs(kwargs, "strategy", "target", "displayed")
        try:
            web_obj = self.find_element(target, strategy)
            self.logger.log_info("Displayed Arg Is Set To:" + displayed)
            is_displayed = web_obj.is_displayed()
            self.logger.log_info("Web Element Is Displayed:" + is_displayed)
            if web_obj.is_displayed() is not None and not StringUtils.string_to_boolean(displayed):
                return self.constants.FAILURE_IS_ELEMENT_DISPLAYED
        except self.common_exceptions:
            if not StringUtils.string_to_boolean(displayed):
                return self.constants.FAILURE_IS_ELEMENT_DISPLAYED

    def get_text_from_element(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element

        This function will determine if an element is enabled and return a boolean value back
        """
        strategy, target = self._check_kwargs(kwargs, "strategy", "target")
        try:
            web_obj = self.find_element(target, strategy)
            return web_obj.text
        except AttributeError:
            self.logger.log_info("Caught Attribute Error Exception")
            return self.constants.FAILURE_GET_TEXT_FROM_ELEMENT

    def get_attribute_from_element(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that the cursor should be moved to.
        [attribute] - The attribute of the element to return
        This function will get the attribute from the web element and return it
        """
        strategy, target, attribute = self._check_kwargs(kwargs, "strategy", "target", "attribute")
        try:
            web_obj = self.find_element(target, strategy)
            return web_obj.get_attribute(attribute)
        except AttributeError:
            self.logger.log_info("Caught Attribute Error Exception")
            return self.constants.FAILURE_GET_ATTRIBUTE_FROM_ELEMENT

    def execute_async_script(self, **kwargs):
        """
        This calls the parent class's execute_async_script method
        """
        return super(SeleniumAgent, self).selenium_execute_async_script(**kwargs)

    def execute_script(self, **kwargs):
        """
        This calls the parent class's execute_script method
        """
        return super(SeleniumAgent, self).selenium_execute_script(**kwargs)

    def enter_text(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that text should be entered into.
        [text] - The text that should be entered.

        Optional kwargs:
        [clear_existing] - A boolean representing whether or not the existing text should be removed before
                           entering the specified text. Enabled by default.

        This function will enter the given text into the target if it it can be located on the page.
        """
        text = self._check_kwargs(kwargs, "text")
        text = self.check_special_keys(text)
        target = kwargs.get("target", None)
        strategy = kwargs.get("strategy", None)
        clear_existing = kwargs.get("clear_existing", True)

        if target is not None and strategy is not None:
            action_target = self.find_element(target, strategy)
        else:
            action_target = None

        if not self.check_modifier_keys(**kwargs):
            if action_target is not None:
                if clear_existing:
                    action_target.clear()
                action_target.send_keys(text)
            else:
                action_chain = ActionChains(self.driver)
                action_chain.send_keys(text).perform()
        else:
            action_chain = ActionChains(self.driver)
            if target is not None:
                action_args = [action_target, text]
                self.get_modifier_keys(action_chain, kwargs, action_chain.send_keys_to_element, action_args).perform()
            else:
                self.get_modifier_keys(action_chain, kwargs, action_chain.send_keys, text).perform()

    def get_length_of_find_elements(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that should be double clicked.

        This function will return the length of find_elements to the user
        """
        strategy, target = self._check_kwargs(kwargs, "strategy", "target")

        action_target = self.find_elements(target, strategy)

        return len(action_target)

    def wait_for_document_ready(self, **kwargs):
        """
        This waits until the document ready state is "complete". It will wait up to a minute for this.
        If the timeout expires a TimeoutException is raised.
        """
        expected_state, retry = self._check_kwargs(kwargs, "state", "retry")
        return_state = self.execute_script(**kwargs)
        if expected_state.lower() == return_state.lower():
            return
        self.logger.log_info("Page state was not 'Complete'. Trying again...")
        raise TimeoutException

    def select_and_click_multiple_elements(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that the cursor should click first.
        [end_element] - The target of the element that the cursor should click last.
        This function will first find the web elements then shift click multiple web elements
        """
        strategy, start_element, end_element = self._check_kwargs(kwargs, "strategy", "target", "end_element")
        target = self.find_element(start_element, strategy)
        end_element = self.find_element(end_element, strategy)
        action_chain = ActionChains(self.driver)
        action_chain.click(target)
        action_chain.key_down(Keys.SHIFT)
        action_chain.click(end_element)
        action_chain.key_up(Keys.SHIFT)
        action_chain.perform()

    def drag_and_drop(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target to drop the element
        [element] - The element to move

        This function will drag the element to the target
        """
        strategy, element, target = self._check_kwargs(kwargs, "strategy", "element", "target")
        source_element = self.find_element(element, strategy)
        dest_element = self.find_element(target, strategy)
        action_chain = ActionChains(self.driver)
        action_chain.drag_and_drop(source_element, dest_element)
        action_chain.perform()

    def drag_and_drop_by_offset(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [element] - The element to move
        [x] - The x position
        [y] - The y position

        This function will drag the element to the x,y offset given
        """
        strategy, element, x, y = self._check_kwargs(kwargs, "strategy", "element", "x", "y")
        source_element = self.find_element(element, strategy)
        action_chain = ActionChains(self.driver)
        action_chain.drag_and_drop_by_offset(source_element, x, y)
        action_chain.perform()

    def webdriver_wait_until_element_exists(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element
        [exists] - Whether the element should exist or not

        This function will return True/False and attempt to find the element and determine whether it should exists
        or not based upon the users input. This function will also manipulate the cmd_obj.error_state
        """
        exists = self._check_kwargs(kwargs, "exists")

        target = self.webdriver_wait_until(**kwargs)
        action_target = target
        if action_target is self.constants.FAILURE_WEBDRIVER_WAIT_UNTIL_FAILURE \
                and StringUtils.string_to_boolean(exists):
            return self.constants.FAILURE_WEBDRIVER_WAIT_UNTIL_ELEMENT_EXISTS_FAILURE
        elif action_target is self.constants.FAILURE_WEBDRIVER_WAIT_UNTIL_FAILURE \
                and not StringUtils.string_to_boolean(exists):
            return True
        return True
