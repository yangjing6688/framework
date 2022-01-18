import os
import re
import time
import logging
from urllib.error import URLError
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.remote_connection import LOGGER as SELENIUM_LOGGER
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, JavascriptException, \
    InvalidElementStateException, WebDriverException, ElementClickInterceptedException, NoSuchWindowException, \
    TimeoutException
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Utils.Constants.Constants import Constants
from ExtremeAutomation.Library.Device.Common.Agents.LoginManagementAgent import LoginManagementAgent
from selenium.webdriver.chrome.options import Options
from robot.api import logger
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

try:
    import autoit
    from autoit import AutoItError
except ImportError:
    AutoItError = ImportError
    pass


class BaseSeleniumAgent(LoginManagementAgent):
    def __init__(self, device):
        super(BaseSeleniumAgent, self).__init__(device)
        self.driver = None
        self.select = None
        self.constants = SeleniumConstants()
        self.valid_actions = [getattr(self.constants, i) for i in dir(self.constants) if i.startswith("ACTION_")]
        self.valid_browsers = [getattr(self.constants, i) for i in dir(self.constants) if i.startswith("BROWSER_")]
        self.default_action_retry_delay = 1   # Time in seconds to wait after a failed action before retrying.
        self.default_action_timeout = 15      # Time in seconds to wait before failing an action.
        self.default_inter_action_delay = .5  # Time in seconds to wait between each successful action.

        # This flag indicates whether a screen shot should be taken
        # when an action fails to execute.
        self.action_screen_shot = StringUtils.string_to_boolean(device.agent_kwargs.get("action_screen_shot", True))
        self.failure_list = [self.constants.FAILURE_GET_ATTRIBUTE_FROM_ELEMENT_AND_COMPARE,
                             self.constants.FAILURE_GET_ATTRIBUTE_FROM_ELEMENT,
                             self.constants.FAILURE_GET_TEXT_FROM_ELEMENT,
                             self.constants.FAILURE_IS_ELEMENT_ENABLED,
                             self.constants.FAILURE_ELEMENT_EXISTS,
                             self.constants.FAILURE_IS_ELEMENT_DISPLAYED,
                             self.constants.FAILURE_GET_TEXT_FROM_ELEMENT_AND_COMPARE,
                             self.constants.FAILURE_IS_ELEMENT_SELECTED,
                             self.constants.FAILURE_SELENIUM_GET_TEXT_FROM_ELEMENT,
                             self.constants.FAILURE_SELENIUM_WINDOWS_FILE_BROWSER_ENTER_PATH_TEXT,
                             self.constants.FAILURE_SELENIUM_IS_ELEMENT_SELECTED,
                             self.constants.FAILURE_SELENIUM_IS_ELEMENT_DISPLAYED,
                             self.constants.FAILURE_SELENIUM_IS_ELEMENT_ENABLED,
                             self.constants.FAILURE_SELENIUM_GET_ATTRIBUTE_FROM_ELEMENT,
                             self.constants.FAILURE_WEBDRIVER_WAIT_UNTIL_FAILURE,
                             self.constants.FAILURE_WEBDRIVER_WAIT_UNTIL_ELEMENT_EXISTS_FAILURE
                             ]
        self.common_exceptions = (AttributeError,
                                  URLError,
                                  WebDriverException,
                                  JavascriptException,
                                  NoSuchElementException,
                                  InvalidElementStateException,
                                  StaleElementReferenceException,
                                  ElementClickInterceptedException,
                                  AutoItError,
                                  NoSuchWindowException,
                                  TimeoutException)

    def send_command_object(self, cmd_obj, **kwargs):
        """
        Function Args:
        [cmd_obj] - A UiCommandObject instance.

        This functions grabs the needed information from the UI command object and executes the specified action.
        """
        if cmd_obj.action in self.valid_actions:
            self.take_action(cmd_obj)
            self.delay(delay=self.default_inter_action_delay, ms=False)
            return cmd_obj
        raise ValueError(cmd_obj.action + " is not a supported action.")

    def take_action(self, cmd_obj):
        """
        Function Args:
        [cmd_obj] - A UiCommandObject instance.

        This function will take the action according to the information in the command object. It will parse any
        arguments and pass them to the required action.
        """
        retries = 1
        if 'retry' in cmd_obj.args:
            retry_count = int(cmd_obj.args['retry']) + 1
        else:
            retry_count = self.get_retry_count(self.default_action_timeout)
        if "timeout" in cmd_obj.args:
            action_retry_delay = int(cmd_obj.args['timeout'])
        else:
            action_retry_delay = self.default_action_retry_delay

        action = getattr(self, cmd_obj.action)

        if cmd_obj.args.get("wait_for_load_mask", True):
            if not self.wait_for_load_masks():
                cmd_obj.set_error_state("Load mask(s) was present for more than 60 seconds.")
                self.__take_failure_screen_shot("load_mask_timeout")
                self.logger.log_info("Load mask present for more than 60 seconds, refreshing page.")
                self.driver.refresh()

        while retries <= retry_count:
            try:
                cmd_obj.return_data = action(**cmd_obj.args)
                if cmd_obj.return_data in self.failure_list:
                    cmd_obj.error_state = True
                elif cmd_obj.return_data == self.constants.WEBDRIVER_WAIT_UNTIL_IGNORE_FAILURE:
                    cmd_obj.return_data = False
                    return cmd_obj
                break
            except self.common_exceptions as e:
                self.logger.log_trace("Caught exception, retrying...")
                self.logger.log_trace(e)
                self.delay(delay=action_retry_delay, ms=False)
                retries += 1
        if retries >= retry_count or cmd_obj.return_data in self.failure_list:
            if cmd_obj.return_data in self.failure_list:
                self.logger.log_trace(cmd_obj.return_data)
                if cmd_obj.return_data == self.constants.FAILURE_WEBDRIVER_WAIT_UNTIL_ELEMENT_EXISTS_FAILURE:
                    cmd_obj.return_data = False
            else:
                self.logger.log_trace("Unable to locate element.")
            if not cmd_obj.error_state:
                cmd_obj.error_state = True
                cmd_obj.error_text = "Unable to perform action."

            if self.action_screen_shot:
                action_name = cmd_obj.args.get("action_name", cmd_obj.action)
                self.__take_failure_screen_shot(action_name)

        return cmd_obj

    def find_element_by_name(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_element(target, SeleniumConstants.STRATEGY_NAME)

    def find_element_by_id(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_element(target, SeleniumConstants.STRATEGY_ID)

    def find_element_by_xpath(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_element(target, SeleniumConstants.STRATEGY_XPATH)

    def find_element_by_link_text(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_element(target, SeleniumConstants.STRATEGY_LINK_TEXT)

    def find_element_by_partial_link_text(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_element(target, SeleniumConstants.STRATEGY_PARTIAL_LINK_TEXT)

    def find_element_by_tag_name(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_element(target, SeleniumConstants.STRATEGY_TAG_NAME)

    def find_element_by_class_name(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_element(target, SeleniumConstants.STRATEGY_CLASS_NAME)

    def find_element_by_css_selector(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_element(target, SeleniumConstants.STRATEGY_CSS_SELECTOR)

    def find_elements_by_name(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_elements(target, SeleniumConstants.STRATEGY_ELEMENTS_NAME)

    def find_elements_by_id(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_elements(target, SeleniumConstants.STRATEGY_ELEMENTS_ID)

    def find_elements_by_xpath(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_elements(target, SeleniumConstants.STRATEGY_ELEMENTS_XPATH)

    def find_elements_by_link_text(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_elements(target, SeleniumConstants.STRATEGY_ELEMENTS_LINK_TEXT)

    def find_elements_by_partial_link_text(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_elements(target, SeleniumConstants.STRATEGY_ELEMENTS_PARTIAL_LINK_TEXT)

    def find_elements_by_tag_name(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_elements(target, SeleniumConstants.STRATEGY_ELEMENTS_TAG_NAME)

    def find_elements_by_class_name(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_elements(target, SeleniumConstants.STRATEGY_ELEMENTS_CLASS_NAME)

    def find_elements_by_css_selector(self, target):
        """
        Required kwargs:
        [target] - The target of the element
        This function simply calls the generic find_element function with specific strategy
        """
        return self.find_elements(target, SeleniumConstants.STRATEGY_ELEMENTS_CSS_SELECTOR)

    # +--------------------------------------------------+
    # | BASE FIND ELEMENT FUNCTION TO FUNNEL ALL THROUGH |
    # +--------------------------------------------------+

    def find_element(self, target, strategy):
        """
        Function Args:
        [target] - The string identifying the component to search for.
        [strategy] - The strategy to use to find the element. Supported strategies can be found in SeleniumConstants.
                     For example, class, id, xpath, and css selector are some of the methods that can be used.

        Attempts to locate the element at <target> using <strategy>.
        """
        if strategy in self.strategies:
            element = self.strategies[strategy](target)
            self.scroll_element_into_view(element)
            return element
        else:
            if strategy == self.constants.STRATEGY_SIESTA:
                err_str = "Cannot use strategy SIESTA with \"selenium\", use \"ext_selenium instead\"."
            else:
                err_str = strategy + " is not a valid element location strategy."
            raise ValueError(err_str)

    def find_elements(self, target, strategy):
        """
        Function Args:
        [target] - The string identifying the component to search for.
        [strategy] - The strategy to use to find the element. Supported strategies can be found in SeleniumConstants.
                     For example, class, id, xpath, and css selector are some of the methods that can be used.

        Attempts to locate the element at <target> using <strategy>.
        """
        if strategy in self.strategies:
            element = self.strategies[strategy](target)
            if not isinstance(element, list):
                self.scroll_element_into_view(element)
            return element
        else:
            if strategy == self.constants.STRATEGY_SIESTA:
                err_str = "Cannot use strategy SIESTA with \"selenium\", use \"ext_selenium instead\"."
            else:
                err_str = strategy + " is not a valid element location strategy."
            raise ValueError(err_str)

    def wait_for_load_masks(self, **kwargs):
        """
        This always returns True for selenium. There shouldn't be any load masks in a non-ext page.
        """
        return True

    # +------------------+
    # | Selenium actions |
    # +------------------+
    def open_web_page(self, **kwargs):
        """
        Required kwargs:
        [browser] - The type of browser to open. There are constants in SeleniumConstants for supported browsers.
        [url] - The URL the browser should open.

        This function will create the needed web driver and open the corresponding URL.
        """
        browser, url, implicit_wait, delete_all_cookies = self._check_kwargs(kwargs, "browser", "url", "implicit_wait",
                                                                             "delete_all_cookies")

        if StringUtils.string_to_boolean(self.device.remote) is False:
            remote = False
        else:
            if self.device.hostname != "127.0.0.1":
                remote = True
            else:
                remote = True if self.device.port == "4444" else False

        if browser in self.valid_browsers:
            if not self.debug:
                # Change the selenium logger log level so that the robot reports
                # are not polluted with unneeded selenium messages. Enable debug attr
                # enable these messages.
                SELENIUM_LOGGER.setLevel(logging.WARNING)
            if self.driver is None:
                self.driver = self.create_browser_driver(browser, remote)
                self.check_open_web_page_implicit_wait(implicit_wait)
                self.driver.get(url)
                self.check_open_web_page_delete_all_cookies(delete_all_cookies)
                self.driver.maximize_window()
                self.strategies = {
                    self.constants.STRATEGY_ID: self.driver.find_element_by_id,
                    self.constants.STRATEGY_NAME: self.driver.find_element_by_name,
                    self.constants.STRATEGY_XPATH: self.driver.find_element_by_xpath,
                    self.constants.STRATEGY_LINK_TEXT: self.driver.find_element_by_link_text,
                    self.constants.STRATEGY_PARTIAL_LINK_TEXT: self.driver.find_element_by_partial_link_text,
                    self.constants.STRATEGY_TAG_NAME: self.driver.find_element_by_tag_name,
                    self.constants.STRATEGY_CLASS_NAME: self.driver.find_element_by_class_name,
                    self.constants.STRATEGY_CSS_SELECTOR: self.driver.find_element_by_css_selector,
                    self.constants.STRATEGY_ELEMENTS_XPATH: self.driver.find_elements_by_xpath,
                    self.constants.STRATEGY_ELEMENTS_ID: self.driver.find_elements_by_id,
                    self.constants.STRATEGY_ELEMENTS_NAME: self.driver.find_elements_by_name,
                    self.constants.STRATEGY_ELEMENTS_LINK_TEXT: self.driver.find_elements_by_link_text,
                    self.constants.STRATEGY_ELEMENTS_PARTIAL_LINK_TEXT: self.driver.find_elements_by_partial_link_text,
                    self.constants.STRATEGY_ELEMENTS_TAG_NAME: self.driver.find_elements_by_tag_name,
                    self.constants.STRATEGY_ELEMENTS_CLASS_NAME: self.driver.find_elements_by_class_name,
                    self.constants.STRATEGY_ELEMENTS_CSS_SELECTOR: self.driver.find_elements_by_css_selector
                }

            else:
                self.check_open_web_page_implicit_wait(implicit_wait)
                self.check_open_web_page_delete_all_cookies(delete_all_cookies)
                self.driver.get(url)
        else:
            raise ValueError(browser + " is not a supported browser type.")

    def selenium_double_click(self, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that should be double clicked.

        This function will double click the given target if it can be located on the page.
        """
        target = self._check_kwargs(kwargs, "target")

        action_target = target

        action_chain = ActionChains(self.driver)
        action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.double_click, action_target)
        action_chain.perform()

    def selenium_right_click(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element that should be right clicked.

        This function will right click the given target if it can be located on the page.
        """
        target = self._check_kwargs(kwargs, "target")

        action_target = target

        action_chain = ActionChains(self.driver)
        action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.context_click, action_target)
        action_chain.perform()

    def selenium_close_web_page(self, **kwargs):
        """
        Required kwargs:
        None

        This function will close the browser and browser driver.
        """
        self.driver.close()

        self.driver = None

    def selenium_quit_web_page(self, **kwargs):
        """
        Required kwargs:
        None

        This function will close the browser and browser driver.
        """
        self.driver.quit()

        self.driver = None

    def selenium_click(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element that should be clicked.

        This function will click the given target if it can be located on the page.
        """
        target = self._check_kwargs(kwargs, "target")

        action_target = target
        action_target.click()

    def send_keys(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element that should be clicked.
        [text] - text to send to target
        [clear_existing] - Boolean on whether or not to clear existing text
        This function will click the given target if it can be located on the page.
        """
        action_target, text, clear_existing = self._check_kwargs(kwargs, "target", "text", "clear_existing")
        bool_clear_existing = StringUtils.string_to_boolean(clear_existing)
        if bool_clear_existing:
            self.logger.log_info("Clear Existing Is Set To:" + str(clear_existing))
            action_target.clear()
        action_target.send_keys(text)

    def selenium_mouse_down(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element that should be clicked and held.

        This function will hold a mouse click down on the given target if it can be located on the page.
        """
        target = self._check_kwargs(kwargs, "target")

        action_target = target

        action_chain = ActionChains(self.driver)
        action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.click_and_hold, action_target)
        action_chain.perform()

    def selenium_mouse_up(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element that the mouse button should be released on.

        This function will release the mouse button on the given target if it can be located on the page.
        """
        target = self._check_kwargs(kwargs, "target")

        action_target = target

        action_chain = ActionChains(self.driver)
        action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.release, action_target)
        action_chain.perform()

    def selenium_move_to_element(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element that the cursor should be moved to.

        This function will move the mouse cursor to the given target if it can be located on the page.
        """
        target = self._check_kwargs(kwargs, "target")

        action_target = target

        action_chain = ActionChains(self.driver)
        action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.move_to_element, action_target)
        action_chain.perform()

    def selenium_move_cursor_out_of_element(self, **kwargs):
        """
        Required kwargs:.
        [target] - The target of the element that the cursor should be moved to.

        This function will move the mouse cursor to the given target if it can be located on the page.
        """
        target = self._check_kwargs(kwargs, "target")

        action_target = target
        size = action_target.size
        x = (size['width'] / 2) + 1
        y = (size['height'] / 2) + 1

        action_chain = ActionChains(self.driver)
        action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.move_to_element, action_target)
        action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.move_by_offset, [x, y])
        action_chain.perform()

    def selenium_move_cursor_x_y(self, **kwargs):
        """
        Required kwargs:
        [x] - The number of pixels the mouse should move horizontally.
        [y] - the number of pixels the mouse should move vertically.

        This function will move the mouse cursor to the given target if it can be located on the page.
        """
        x, y = self._check_kwargs(kwargs, "x", "y")

        action_chain = ActionChains(self.driver)
        action_chain = self.get_modifier_keys(action_chain, kwargs, action_chain.move_by_offset, [x, y])
        action_chain.perform()

    def selenium_element_exists(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element
        [exists] - Whether the element should exist or not

        This function will find the element and determine whether it should exists or not based upon
        the users input
        """
        target = self._check_kwargs(kwargs, "target")
        try:
            action_target = target
            if action_target is not None:
                return True
            return False
        except self.common_exceptions:
            return False

    def selenium_is_element_enabled(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element

        This function will determine if an element is enabled and return a boolean value back
        """
        target = self._check_kwargs(kwargs, "target")
        try:
            return target.is_enabled()
        except AttributeError:
            return self.constants.FAILURE_SELENIUM_IS_ELEMENT_ENABLED

    def selenium_is_element_selected(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element

        This function will determine if an element is selected and return a boolean value back
        """
        target = self._check_kwargs(kwargs, "target")
        try:
            return target.is_selected()
        except AttributeError:
            return self.constants.FAILURE_SELENIUM_IS_ELEMENT_SELECTED

    def selenium_is_element_displayed(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element

        This function will determine if an element is displayed is enabled and return a boolean value back
        """
        target = self._check_kwargs(kwargs, "target")
        try:
            return target.is_displayed()
        except AttributeError:
            return self.constants.FAILURE_IS_ELEMENT_DISPLAYED

    def selenium_get_text_from_element(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element

        This function will determine if an element is enabled and return a boolean value back
        """
        target = self._check_kwargs(kwargs, "target")
        try:
            return target.text
        except AttributeError:
            return self.constants.FAILURE_GET_TEXT_FROM_ELEMENT

    def windows_file_browser_enter_path_text(self, **kwargs):
        """
        Required kwargs:
        [win_title] - The associated text with the window title
        [path] - The path of the file to enter into the text field

        This function will add text to a windows explorer window.
        """
        win_title, path = self._check_kwargs(kwargs, "win_title", "path")
        try:
            autoit.auto_it_set_option("WinTitleMatchMode", 1)
            autoit.win_wait(win_title, 3)
            autoit.control_send(win_title, "Edit1", path + "{Enter}")
            try:
                autoit.win_wait(win_title, 3)
                autoit.win_close(win_title)
                autoit.win_wait(win_title, 3)
                autoit.win_close(win_title)
                return self.constants.FAILURE_SELENIUM_WINDOWS_FILE_BROWSER_ENTER_PATH_TEXT
            except self.common_exceptions:
                pass
        except self.common_exceptions:
            return self.constants.FAILURE_SELENIUM_WINDOWS_FILE_BROWSER_ENTER_PATH_TEXT

    def selenium_get_attribute_from_element(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element that the cursor should be moved to.
        [attribute] - The attribute of the element to return
        This function will get the attribute from the web element and return it
        """
        target, attribute = self._check_kwargs(kwargs, "target", "attribute")
        try:
            return target.get_attribute(attribute)
        except AttributeError:
            return self.constants.FAILURE_SELENIUM_GET_ATTRIBUTE_FROM_ELEMENT

    def selenium_execute_async_script(self, **kwargs):
        """
        This function converts the provided script into a script that will work
        with execute_async_script.
        """
        script, target = self._check_kwargs(kwargs, "script", "target")

        if target is None:
            return self.driver.execute_async_script(script)
        return self.driver.execute_async_script(script, target)

    def selenium_execute_script(self, **kwargs):
        """
        This function converts the provided script into a script that will work
        with execute_async_script.
        """
        script, target = self._check_kwargs(kwargs, "script", "target")

        if target is None:
            return self.driver.execute_script(script)
        return self.driver.execute_script(script, target)

    def delay(self, **kwargs):
        """
        Required kwargs:
        [delay] - The amount of time to wait.

        Optional kwargs:
        [ms] - A boolean flag indicating whether or not [delay] is in milliseconds or seconds. Default is milliseconds.

        Pauses the driver for <delay> seconds.
        """
        delay = self._check_kwargs(kwargs, "delay")
        ms = kwargs.get("ms", True)

        if ms:
            delay = int(delay) / 1000

        time.sleep(delay)

    def screen_shot(self, **kwargs):
        """
        Required kwargs:
        [file_name] - The name of the file the screen shot should be saved under.

        This function will take a screenshot and save it under the given file name.
        """
        base_file = self._check_kwargs(kwargs, "file_name")
        file_name = base_file.replace(" ", "_")
        try:
            guid = BuiltIn().get_variables(True)["environment"]["testguid"]
            file_name = os.path.join("/TRM_DATA/logs/", guid, "screenshots", file_name)
        except (RobotNotRunningError, KeyError):
            pass
        folder = os.path.dirname(file_name)
        if folder != "":
            if not os.path.isdir(folder) and not os.path.isfile(folder):
                os.makedirs(folder)
        try:
            result = self.driver.save_screenshot(file_name)
            if 'screenshots' in file_name:
                new_file = file_name.split("screenshots")
                file_name = r'.\screenshots' + str(new_file[1])
            try:
                logger.info('<a href="%s"><img src="%s" height="%s" width="%s"></a>' %
                            (file_name, file_name, '100', '600'), html=True)
                message_footer = ["+" + "-" * (len(file_name) + 31) + "+"]
                self.logger.log_info(message_footer[0])
                self.logger.log_info("|  Taking Failure Screenshot: " + file_name + "  |")
                self.logger.log_info(message_footer[0])
            except (RobotNotRunningError, KeyError):
                pass
            if not result:
                self.logger.log_info("Unable to take screenshot with name " + file_name + ".\n" +
                                     "Verify the file name is valid.")
            return result
        except AttributeError:
            self.logger.log_info("The selenium driver has not been created yet, unable to take screenshot.")
            return False

    def selenium_drag_and_drop(self, **kwargs):
        """
        Required kwargs:
        [target] - The target to drop the element
        [element] - The element to move

        This function will drag the element to the target
        """
        element, target = self._check_kwargs(kwargs, "element", "target")
        source_element = element
        dest_element = target
        action_chain = ActionChains(self.driver)
        action_chain.drag_and_drop(source_element, dest_element)
        action_chain.perform()

    def selenium_drag_and_drop_by_offset(self, **kwargs):
        """
        Required kwargs:
        [element] - The element to move
        [x] - The x position
        [y] - The y position

        This function will drag the element to the x,y offset given
        """
        element, x, y = self._check_kwargs(kwargs, "element", "x", "y")
        source_element = element
        action_chain = ActionChains(self.driver)
        action_chain.drag_and_drop_by_offset(source_element, x, y)
        action_chain.perform()

    def accept_alert(self, **kwargs):
        """
        This function will switch to and accept an alert
        """
        alert = self.driver.switch_to.alert()
        alert.accept()

    def dismiss_alert(self, **kwargs):
        """
        This function will switch to and dismiss an alert
        """
        alert = self.driver.switch_to.alert()
        alert.dismiss()

    def get_text_from_alert(self, **kwargs):
        """
        This function will grab the given text from the alert window
        """
        alert = self.driver.switch_to.alert()
        return alert.getText()

    def send_keys_to_alert(self, **kwargs):
        """
        This function will send text to the alert window
        """
        text = self._check_kwargs(kwargs, "text")
        alert = self.driver.switch_to.alert()
        return alert.sendKeys(text)

    def switch_to_frame(self, **kwargs):
        """
        This function will switch to and dismiss an alert
        """
        frame_ref = self._check_kwargs(kwargs, "frame")
        frame = self.driver.switch_to.frame(frame_ref)
        return frame

    def selenium_select_and_click_multiple_elements(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element that the cursor should click first.
        [end_element] - The target of the element that the cursor should click last.
        This function will shift click multiple web elements
        """
        target, end_element = self._check_kwargs(kwargs, "target", "end_element")
        action_chain = ActionChains(self.driver)
        action_chain.click(target)
        action_chain.key_down(Keys.SHIFT)
        action_chain.click(end_element)
        action_chain.key_up(Keys.SHIFT)
        action_chain.perform()

    def selenium_open_new_browser_tab(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element that the cursor should be moved to.

        This function will move the mouse cursor to the given target if it can be located on the page.
        """
        url = self._check_kwargs(kwargs, "url")

        self.driver.execute_script("window.open('');")
        self.base_browser_tab_selection('')
        self.driver.get(url)

    def selenium_close_browser_tab(self, **kwargs):
        """
        Required kwargs:
        [title_name] - The self.driver.title of the window to close.

        This function will move the mouse cursor to the given target if it can be located on the page.
        """
        check_title = self._check_kwargs(kwargs, "title_name")
        if check_title is not None:
            self.base_browser_tab_selection(check_title)
        if len(self.driver.window_handles) > 1:
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.logger.log_info("Closing Tab and setting window handle to 0. "
                                 "Use switch tab if handle 0 is not the correct window")
        else:
            self.logger.log_info("One tab remaining not closing. Use Close Web Page")

    def selenium_switch_browser_tab(self, **kwargs):
        """
        Required kwargs:
        [title_name] - The self.driver.title of the window to switch to
        This function will switch the browser tab to the "title_name" tab provided
        """
        check_title = self._check_kwargs(kwargs, "title_name")
        self.base_browser_tab_selection(check_title)

    # +---------------------------+
    # | Driver Creation Functions |
    # +---------------------------+
    def create_browser_driver(self, browser, remote):
        """
        Function Args:
        [browser] - The type of browser that should be used. Supported browsers can be found in SeleniumConstants.
        [remote] - A boolean indicating whether or not that driver should be opened locally or remotely.

        Creates the needed browser driver.
        """
        if browser == self.constants.BROWSER_FIREFOX:
            return self.create_firefox_driver(remote)
        elif browser == self.constants.BROWSER_CHROME:
            return self.create_chrome_driver(remote)

    def create_firefox_driver(self, remote):
        """
        Function Args:
        [remote] - A boolean indicating whether or not that driver should be opened locally or remotely.

        Creates an instance of the firefox web driver locally or remotely.
        """
        capabilities = webdriver.DesiredCapabilities().FIREFOX
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True

        if remote:
            remote_ip = "http://" + self.device.hostname + ":" + self.device.port + "/wd/hub"
            return webdriver.Remote(command_executor=remote_ip, desired_capabilities=capabilities)
        else:
            profile = webdriver.FirefoxProfile()
            profile.accept_untrusted_certs = True
            profile.assume_untrusted_cert_issuer = False
            return webdriver.Firefox(profile, capabilities=capabilities)

    def create_chrome_driver(self, remote):
        """
        Function Args:
        [remote] - A boolean indicating whether or not that driver should be opened locally or remotely.

        Creates an instance of the chrome web driver locally or remotely.
        """
        if remote:
            remote_ip = "http://" + self.device.hostname + ":" + self.device.port + "/wd/hub"
            capabilities = webdriver.DesiredCapabilities().CHROME
            return webdriver.Remote(command_executor=remote_ip, desired_capabilities=capabilities)
        else:
            _chrome_options = Options()
            _chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            _chrome_options.add_experimental_option('useAutomationExtension', False)
            return webdriver.Chrome(chrome_options=_chrome_options)

    # +----------------------------------+
    # | WEBDRIVER WAIT FUNCTIONS         |
    # +----------------------------------+
    def selenium_webdriver_wait_until_element_exists(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element
        [exists] - Whether the element should exist or not

        This function will return True/False and find the element and determine whether it should exists or not
        based upon the users input
        """
        exists = self._check_kwargs(kwargs, "exists")
        target = self.webdriver_wait_until(**kwargs)
        action_target = target
        if action_target is SeleniumConstants.FAILURE_WEBDRIVER_WAIT_UNTIL_FAILURE \
                and StringUtils.string_to_boolean(exists):
            return False
        elif action_target is SeleniumConstants.FAILURE_WEBDRIVER_WAIT_UNTIL_FAILURE \
                and not StringUtils.string_to_boolean(exists):
            return True
        return True

    def webdriver_wait_until(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element
        [timeout] - How long for the webdriver to wait
        [retry] - How many times to retry
        [strategy] - The location strategy to use
        [condition] - The specific webdriver wait function to run
        This function is the main webdriver wait function that will handle retries as well as handle if the end user
        decides to ignore the outcome(will not fail the keyword regardless of the result)
        """
        target, timeout, retry, strategy, condition, ignore_outcome = \
            self._check_kwargs(kwargs, "target", 'timeout_ww', 'retry', 'strategy', 'condition', 'ignore_outcome')
        retries = 0
        return_target = None
        while retries <= retry:
            try:
                return_target = self.base_web_driver_logic(**kwargs)
                return return_target
            except self.common_exceptions:
                self.logger.log_info("Caught exception in webdriver_wait, retrying...")
                retries += 1
        if retries > retry:
            if StringUtils.string_to_boolean(ignore_outcome) is False:
                return SeleniumConstants.FAILURE_WEBDRIVER_WAIT_UNTIL_FAILURE
            else:
                return SeleniumConstants.WEBDRIVER_WAIT_UNTIL_IGNORE_FAILURE
        else:
            return return_target

    def base_web_driver_logic(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element
        [timeout] - How long for the webdriver to wait
        [retry] - How many times to retry
        [strategy] - The location strategy to use
        [condition] - The specific webdriver wait function to run
        This function determines which webdriver wait function to execute based upon the
        condition and strategy
        """
        target, timeout, retry, strategy, condition = \
            self._check_kwargs(kwargs, "target", 'timeout_ww', 'retry', 'strategy', 'condition')
        wait = self.base_web_driver_wait(int(timeout))

        if condition == self.constants.CONDITION_TITLE_CONTAINS:
            return wait.until(expected_conditions.title_contains(target))

        elif strategy == self.constants.STRATEGY_NAME:
            if condition == self.constants.CONDITION_ELEMENT_TO_BE_CLICKABLE:
                return wait.until(expected_conditions.element_to_be_clickable((By.NAME, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ALL_ELEMENTS_LOCATED:
                return wait.until(expected_conditions.presence_of_all_elements_located((By.NAME, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ELEMENT_LOCATED:
                return wait.until(expected_conditions.presence_of_element_located((By.NAME, target)))
            elif condition == self.constants.CONDITION_INVISIBILITY_OF_ELEMENT:
                return wait.until(expected_conditions.invisibility_of_element((By.NAME, target)))

        elif strategy == self.constants.STRATEGY_XPATH:
            if condition == self.constants.CONDITION_ELEMENT_TO_BE_CLICKABLE:
                return wait.until(expected_conditions.element_to_be_clickable((By.XPATH, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ALL_ELEMENTS_LOCATED:
                return wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ELEMENT_LOCATED:
                return wait.until(expected_conditions.presence_of_element_located((By.XPATH, target)))
            elif condition == self.constants.CONDITION_INVISIBILITY_OF_ELEMENT:
                return wait.until(expected_conditions.invisibility_of_element((By.XPATH, target)))

        elif strategy == self.constants.STRATEGY_TAG_NAME:
            if condition == self.constants.CONDITION_ELEMENT_TO_BE_CLICKABLE:
                return wait.until(expected_conditions.element_to_be_clickable((By.TAG_NAME, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ALL_ELEMENTS_LOCATED:
                return wait.until(expected_conditions.presence_of_all_elements_located((By.TAG_NAME, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ELEMENT_LOCATED:
                return wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, target)))
            elif condition == self.constants.CONDITION_INVISIBILITY_OF_ELEMENT:
                return wait.until(expected_conditions.invisibility_of_element((By.TAG_NAME, target)))

        elif strategy == self.constants.STRATEGY_CLASS_NAME:
            if condition == self.constants.CONDITION_ELEMENT_TO_BE_CLICKABLE:
                return wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ALL_ELEMENTS_LOCATED:
                return wait.until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ELEMENT_LOCATED:
                return wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, target)))
            elif condition == self.constants.CONDITION_INVISIBILITY_OF_ELEMENT:
                return wait.until(expected_conditions.invisibility_of_element((By.CLASS_NAME, target)))

        elif strategy == self.constants.STRATEGY_PARTIAL_LINK_TEXT:
            if condition == self.constants.CONDITION_ELEMENT_TO_BE_CLICKABLE:
                return wait.until(expected_conditions.element_to_be_clickable((By.PARTIAL_LINK_TEXT, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ALL_ELEMENTS_LOCATED:
                return wait.until(expected_conditions.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ELEMENT_LOCATED:
                return wait.until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, target)))
            elif condition == self.constants.CONDITION_INVISIBILITY_OF_ELEMENT:
                return wait.until(expected_conditions.invisibility_of_element((By.PARTIAL_LINK_TEXT, target)))

        elif strategy == self.constants.STRATEGY_ID:
            if condition == self.constants.CONDITION_ELEMENT_TO_BE_CLICKABLE:
                return wait.until(expected_conditions.element_to_be_clickable((By.ID, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ALL_ELEMENTS_LOCATED:
                return wait.until(expected_conditions.presence_of_all_elements_located((By.ID, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ELEMENT_LOCATED:
                return wait.until(expected_conditions.presence_of_element_located((By.ID, target)))
            elif condition == self.constants.CONDITION_INVISIBILITY_OF_ELEMENT:
                return wait.until(expected_conditions.invisibility_of_element((By.ID, target)))

        elif strategy == self.constants.STRATEGY_LINK_TEXT:
            if condition == self.constants.CONDITION_ELEMENT_TO_BE_CLICKABLE:
                return wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ALL_ELEMENTS_LOCATED:
                return wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ELEMENT_LOCATED:
                return wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, target)))
            elif condition == self.constants.CONDITION_INVISIBILITY_OF_ELEMENT:
                return wait.until(expected_conditions.invisibility_of_element((By.LINK_TEXT, target)))

        elif strategy == self.constants.STRATEGY_CSS_SELECTOR:
            if condition == self.constants.CONDITION_ELEMENT_TO_BE_CLICKABLE:
                return wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ALL_ELEMENTS_LOCATED:
                return wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, target)))
            elif condition == self.constants.CONDITION_PRESENCE_OF_ELEMENT_LOCATED:
                return wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, target)))
            elif condition == self.constants.CONDITION_INVISIBILITY_OF_ELEMENT:
                return wait.until(expected_conditions.invisibility_of_element((By.CSS_SELECTOR, target)))

        else:
            self.logger.log_info("Condition or Strategy did not match")

    # +------------------+
    # | Helper Functions |
    # +------------------+

    def base_web_driver_wait(self, timeout):
        """
        Function Args:
        [timeout] - amount of time for the webdriver wait timeout.

        Returns base webdriver wait call given timeout
        """
        return WebDriverWait(self.driver, timeout)

    def base_browser_tab_selection(self, check_title):
        """
        Function Args:
        [check_title] - The title of the browser tab to select

        Switches to the correct browser tab based on title
        """
        item = 0
        while item < len(self.driver.window_handles):
            self.driver.switch_to.window(self.driver.window_handles[item])
            if self.driver.title.lower() == check_title.lower():
                return self.driver.switch_to.window(self.driver.window_handles[item])
            else:
                item += 1

    def __take_failure_screen_shot(self, action_name):
        """
        Function Args:
        [action_name] - The action name to attach to file name.

        """
        time_stamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S')
        file_name = time_stamp + "_" + action_name + ".png"

        self.screen_shot(file_name=file_name)

    def check_open_web_page_implicit_wait(self, implicit_wait):
        """
        Function Args:
        [implicit_wait] - The time to wait for DOM

        """
        if implicit_wait is not None:
            self.logger.log_info("Implicit wait value set to: " + str(implicit_wait))
            self.driver.implicitly_wait(int(implicit_wait))

    def check_open_web_page_delete_all_cookies(self, delete_all_cookies):
        """
        Function Args:
        [delete_all_cookies] - Boolean value to determine whether or not to clear cookies

        """
        if StringUtils.string_to_boolean(delete_all_cookies) is True:
            self.logger.log_info("Deleting all cookies")
            self.driver.delete_all_cookies()

    @staticmethod
    def check_special_keys(text):
        """
        Function Args:
        [text] - The text to check  for special keys.

        This function checks the given text for any instances of [<special_key>} and attempts to replace
        it with the matching Keys object.
        """
        special_key_regex = r"\[[A-Z]*\]"

        for match in re.findall(special_key_regex, text):
            special_key = match.strip("[]")

            try:
                # Try to replace [<match>] in the text with the corresponding Keys.<special_key>.
                text = text.replace(match, getattr(Keys, special_key))
            except AttributeError:
                # Couldn't find a matching Keys.<special_key>, don't change text.
                pass

        return text

    @staticmethod
    def check_modifier_keys(**kwargs):
        """
        This function checks for the existence of "shift", "ctrl", or "alt" in the passed kwargs.
        If any of them are present and set to to True, True is returned.
        """
        shift = kwargs.get("shift", False)
        ctrl = kwargs.get("ctrl", False)
        alt = kwargs.get("alt", False)

        if shift or ctrl or alt:
            return True
        return False

    def scroll_element_into_view(self, target):
        """
        Function Args:
        [target] - The selenium target that should be scrolled into view.

        Scrolls the given target into view if it isn't already in view.
        """
        if target is not None:
            if not target.is_displayed():
                self.driver.execute_script("arguments[0].scrollIntoView(true);", target)

    def get_retry_count(self, timeout=None):
        """
        Optional Arguments:
        [timeout] - Used to override the default action retry delay.

        Returns the number of retries to take before stopping the find element search.

        Returns <timeout> / <retry_delay>
        """
        if timeout is None:
            timeout = self.default_action_timeout

        return int(timeout / self.default_action_retry_delay)

    @staticmethod
    def get_modifier_keys(action_chain, modifier_dict, action, action_args):
        """
        Function Args:
        [action_chain] - An empty action chain.
        [modifier_dict] - This should be a dictionary that contains a string key for each modifier and a boolean
                          value indicating whether or not that key should be pressed.
        [action] - An action chain action to perform after all modifier keys are held.
        [action_args] - A list of arguments that should be passed to the action.

        This function figures out which modifier keys should be held and creates an action chain that holds
        the needed keys, performs the needed action, finally releases the held modifier keys.
        """
        # These are the currently supported modifier keys. If new keys are needed they should be added here.
        valid_options = ["shift", "ctrl", "alt"]
        key_map = {"shift": Keys.SHIFT,
                   "ctrl": Keys.CONTROL,
                   "alt": Keys.ALT}

        # Convert action args to a list if it is something other than a list.
        action_args = [action_args] if not isinstance(action_args, list) else action_args

        def __get_modifier_keys(_valid_options, _action_chain, current_index):
            # This checks to see if we are still adding key_down actions or if we should start
            # adding the corresponding key_up action.
            if current_index < len(_valid_options):

                # Get the current modifier key from the valid_options list using current_index. Then
                # check the kwargs dict to see if that modifier key's value is True.
                if modifier_dict.get(_valid_options[current_index], False):

                    # Add the key_down action for the current modifier key.
                    # Ex: If shift is the current key the call would be _action_chain.key_down(Keys.SHIFT)
                    _action_chain.key_down(key_map[_valid_options[current_index]])

                # Next call __get_modifier_keys again and increment the index by 1. This will check the
                # next modifier key in the valid_options list.
                _action_chain = __get_modifier_keys(_valid_options, _action_chain, current_index + 1)

                # On the way "out" of the recursive calls add the needed key_up actions. This does the same
                # check as before and only adds key_up if the current modifier key is set to True in the kwargs
                # dict.
                if modifier_dict.get(_valid_options[current_index], False):
                    _action_chain.key_up(key_map[_valid_options[current_index]])

                    # For Chrome, when sending keys to an element we need to add a second key_up otherwise
                    # the modifier key will remain pressed.
                    if "send_keys_to_element" in repr(action):
                        _action_chain.key_up(key_map[_valid_options[current_index]])
                return _action_chain
            else:
                # This takes the action_chain action and adds it to the chain.
                action(*action_args)
                return _action_chain

        if len(modifier_dict) == 0:
            action(*action_args)
            return action_chain
        return __get_modifier_keys(valid_options, action_chain, 0)

    @staticmethod
    def _check_kwargs(kwargs, *keys):
        """
        This function parses the kwargs looking for the passed keys. If any of the passed args are
        not present in the kwargs and exception is raised. Otherwise a list of corresponding values
        are returned.
        """
        missing_kwargs = []
        found_kwargs = []
        for key in keys:
            if key not in kwargs:
                missing_kwargs.append(key)
            else:
                found_kwargs.append(kwargs[key])

        if len(missing_kwargs) > 0:
            raise ValueError(", ".join(missing_kwargs) + " are required arguments.")
        if len(found_kwargs) == 1:
            return found_kwargs[0]
        return found_kwargs

    # +----------------------+
    # | Javascript Utilities |
    # +----------------------+

    def login(self):
        """
        Login function, not needed for selenium. Sets logged_in to True.
        """
        self.logged_in = True

    def connect(self):
        """
        Connect function, not needed for selenium. Sets connected to True.
        """
        self.connected = True

    def disconnect(self):
        """
        Disconnect function, not needed for selenium. Sets connected to False.
        """
        self.connected = False

    def logout(self):
        """
        Logout function, not needed for selenium. Sets logged_in to False.
        """
        self.logged_in = False


class SeleniumConstants(Constants):
    # Supported browsers.
    BROWSER_CHROME = "chrome"
    BROWSER_FIREFOX = "firefox"

    # Available Actions.
    ACTION_OPEN_PAGE = "open_web_page"
    ACTION_CLOSE_PAGE = "close_web_page"
    ACTION_SELENIUM_CLOSE_PAGE = "selenium_close_web_page"
    ACTION_SELENIUM_OPEN_NEW_BROWSER_TAB = "selenium_open_new_browser_tab"
    ACTION_SELENIUM_SWITCH_BROWSER_TAB = "selenium_switch_browser_tab"
    ACTION_SELENIUM_CLOSE_BROWSER_TAB = "selenium_close_browser_tab"
    ACTION_SELENIUM_QUIT_PAGE = "selenium_quit_web_page"
    ACTION_CLICK = "click"
    ACTION_CLICK_BOUNDLIST_ITEM = "click_boundlist_item"
    ACTION_SELENIUM_CLICK = "selenium_click"
    ACTION_DOUBLE_CLICK = "double_click"
    ACTION_SELENIUM_DOUBLE_CLICK = "selenium_double_click"
    ACTION_RIGHT_CLICK = "right_click"
    ACTION_SELENIUM_RIGHT_CLICK = "selenium_right_click"
    ACTION_MOUSE_DOWN = "mouse_down"
    ACTION_SELENIUM_MOUSE_DOWN = "selenium_mouse_down"
    ACTION_MOUSE_UP = "mouse_up"
    ACTION_SELENIUM_MOUSE_UP = "selenium_mouse_up"
    ACTION_SELENIUM_MOVE_CURSOR_X_Y = "selenium_move_cursor_x_y"
    ACTION_MOVE_CURSOR = "move_cursor"
    ACTION_SELENIUM_MOVE_TO_ELEMENT = "selenium_move_to_element"
    ACTION_MOVE_CURSOR_OUT_OF_ELEMENT = "move_cursor_out_of_element"
    ACTION_SELENIUM_MOVE_CURSOR_OUT_OF_ELEMENT = "selenium_move_cursor_out_of_element"
    ACTION_TYPE = "enter_text"
    ACTION_DELAY = "delay"
    ACTION_SCREEN_SHOT = "screen_shot"
    ACTION_DOCUMENT_QUERY = "document_query"
    ACTION_FIND_ELEMENT = "find_element"
    ACTION_FIND_ELEMENTS = "find_elements"
    ACTION_GET_TEXT_FROM_ELEMENT_AND_COMPARE = "get_text_from_element_and_compare"
    ACTION_GET_ATTRIBUTE_FROM_ELEMENT_AND_COMPARE = "get_attribute_from_element_and_compare"
    ACTION_DRAG_AND_DROP = "drag_and_drop"
    ACTION_SELENIUM_WEBDRIVER_WAIT_UNTIL_ELEMENT_EXISTS = "selenium_webdriver_wait_until_element_exists"
    ACTION_WEBDRIVER_WAIT_UNTIL_ELEMENT_EXISTS = "webdriver_wait_until_element_exists"
    ACTION_SELENIUM_DRAG_AND_DROP = "selenium_drag_and_drop"
    ACTION_SELENIUM_DRAG_AND_DROP_BY_OFFSET = "selenium_drag_and_drop_by_offset"
    ACTION_DRAG_AND_DROP_BY_OFFSET = "drag_and_drop_by_offset"
    ACTION_SELECT_AND_CLICK_MULTIPLE_ELEMENTS = "select_and_click_multiple_elements"
    ACTION_ACCEPT_ALERT = "accept_alert"
    ACTION_DISMISS_ALERT = "dismiss_alert"
    ACTION_GET_TEXT_FROM_ALERT = "get_text_from_alert"
    ACTION_SEND_KEYS_TO_ALERT = "send_keys_to_alert"
    ACTION_ELEMENT_EXISTS = "element_exists"
    ACTION_SELENIUM_ELEMENT_EXISTS = "selenium_element_exists"
    ACTION_IS_ELEMENT_ENABLED = "is_element_enabled"
    ACTION_SELENIUM_IS_ELEMENT_ENABLED = "selenium_is_element_enabled"
    ACTION_IS_ELEMENT_SELECTED = "is_element_selected"
    ACTION_SELENIUM_IS_ELEMENT_SELECTED = "selenium_is_element_selected"
    ACTION_IS_ELEMENT_DISPLAYED = "is_element_displayed"
    ACTION_SELENIUM_IS_ELEMENT_DISPLAYED = "selenium_is_element_displayed"
    ACTION_GET_TEXT_FROM_ELEMENT = "get_text_from_element"
    ACTION_SELENIUM_GET_TEXT_FROM_ELEMENT = "selenium_get_text_from_element"
    ACTION_GET_ATTRIBUTE_FROM_ELEMENT = "get_attribute_from_element"
    ACTION_GET_LENGTH_OF_FIND_ELEMENTS = "get_length_of_find_elements"
    ACTION_WAIT_FOR_DOCUMENT_READY = "wait_for_document_ready"
    ACTION_SELENIUM_GET_ATTRIBUTE_FROM_ELEMENT = "selenium_get_attribute_from_element"
    ACTION_SELECT_VISIBLE_TEXT = "select_element"
    ACTION_WINDOWS_FILE_BROWSER_ENTER_PATH_TEXT = "windows_file_browser_enter_path_text"
    ACTION_SELENIUM_SELECT_AND_CLICK_MULTIPLE_ELEMENTS = "selenium_select_and_click_multiple_elements"
    ACTION_SELENIUM_FIND_ELEMENT_BY_NAME = "find_element_by_name"
    ACTION_SELENIUM_FIND_ELEMENT_BY_ID = "find_element_by_id"
    ACTION_SELENIUM_FIND_ELEMENT_BY_XPATH = "find_element_by_xpath"
    ACTION_SELENIUM_FIND_ELEMENT_BY_LINK_TEXT = "find_element_by_link_text"
    ACTION_SELENIUM_FIND_ELEMENT_BY_PARTIAL_LINK_TEXT = "find_element_by_partial_link_text"
    ACTION_SELENIUM_FIND_ELEMENT_BY_TAG_NAME = "find_element_by_tag_name"
    ACTION_SELENIUM_FIND_ELEMENT_BY_CLASS_NAME = "find_element_by_class_name"
    ACTION_SELENIUM_FIND_ELEMENT_BY_CSS_SELECTOR = "find_element_by_css_selector"
    ACTION_SELENIUM_FIND_ELEMENTS_BY_NAME = "find_elements_by_name"
    ACTION_SELENIUM_FIND_ELEMENTS_BY_ID = "find_elements_by_id"
    ACTION_SELENIUM_FIND_ELEMENTS_BY_XPATH = "find_elements_by_xpath"
    ACTION_SELENIUM_FIND_ELEMENTS_BY_LINK_TEXT = "find_elements_by_link_text"
    ACTION_SELENIUM_FIND_ELEMENTS_BY_PARTIAL_LINK_TEXT = "find_elements_by_partial_link_text"
    ACTION_SELENIUM_FIND_ELEMENTS_BY_TAG_NAME = "find_elements_by_tag_name"
    ACTION_SELENIUM_FIND_ELEMENTS_BY_CLASS_NAME = "find_elements_by_class_name"
    ACTION_SELENIUM_FIND_ELEMENTS_BY_CSS_SELECTOR = "find_elements_by_css_selector"
    ACTION_SELENIUM_SEND_KEYS = "send_keys"
    ACTION_SELENIUM_EXECUTE_ASYNC_SCRIPT = "selenium_execute_async_script"
    ACTION_SELENIUM_EXECUTE_SCRIPT = "selenium_execute_script"
    ACTION_WEBDRIVER_WAIT_UNTIL = "webdriver_wait_until"
    CONDITION_ELEMENT_TO_BE_CLICKABLE = "element_to_be_clickable"
    CONDITION_PRESENCE_OF_ALL_ELEMENTS_LOCATED = "presence_of_all_elements_located"
    CONDITION_INVISIBILITY_OF_ELEMENT = "invisibility_of_element"
    CONDITION_PRESENCE_OF_ELEMENT_LOCATED = "presence_of_element_located"
    CONDITION_TITLE_CONTAINS = "title_contains"
    # Available element location strategies.
    STRATEGY_ID = "id"
    STRATEGY_NAME = "name"
    STRATEGY_XPATH = "xpath"
    STRATEGY_LINK_TEXT = "link_text"
    STRATEGY_PARTIAL_LINK_TEXT = "partial_link_text"
    STRATEGY_TAG_NAME = "tag_name"
    STRATEGY_CLASS_NAME = "class_name"
    STRATEGY_CSS_SELECTOR = "css_selector"
    STRATEGY_ELEMENTS_ID = "elements_by_id"
    STRATEGY_ELEMENTS_NAME = "elements_by_name"
    STRATEGY_ELEMENTS_LINK_TEXT = "elements_by_link_text"
    STRATEGY_ELEMENTS_PARTIAL_LINK_TEXT = "elements_by_partial_link_text"
    STRATEGY_ELEMENTS_TAG_NAME = "elements_by_tag_name"
    STRATEGY_ELEMENTS_CLASS_NAME = "elements_by_class_name"
    STRATEGY_ELEMENTS_CSS_SELECTOR = "elements_by_css_selector"
    STRATEGY_ELEMENTS_XPATH = "elements_by_xpath"
    STRATEGY_SIESTA = "siesta"
    STRATEGY_STRICT_SELENIUM = "strict_selenium"
    # Failure Constants
    FAILURE_SELENIUM_WINDOWS_FILE_BROWSER_ENTER_PATH_TEXT = "failure:selenium_windows_file_browser_enter_path_text"
    FAILURE_SELENIUM_GET_TEXT_FROM_ELEMENT = "failure:selenium_get_text_from_element"
    FAILURE_SELENIUM_GET_ATTRIBUTE_FROM_ELEMENT = "failure:selenium_get_attribute_from_element"
    FAILURE_SELENIUM_IS_ELEMENT_SELECTED = "failure:selenium_is_element_selected"
    FAILURE_SELENIUM_IS_ELEMENT_DISPLAYED = "failure:selenium_is_element_displayed"
    FAILURE_SELENIUM_IS_ELEMENT_ENABLED = "failure:selenium_is_element_enabled"
    FAILURE_ELEMENT_EXISTS = "failure:element_exists"
    FAILURE_IS_ELEMENT_ENABLED = "failure:is_element_enabled"
    FAILURE_IS_ELEMENT_SELECTED = "failure:is_element_selected"
    FAILURE_IS_ELEMENT_DISPLAYED = "failure:is_element_displayed"
    FAILURE_GET_TEXT_FROM_ELEMENT = "failure:get_text_from_element"
    FAILURE_GET_ATTRIBUTE_FROM_ELEMENT = "failure:get_attribute_from_element"
    FAILURE_GET_ATTRIBUTE_FROM_ELEMENT_AND_COMPARE = "failure:get_attribute_from_element_and_compare"
    FAILURE_GET_TEXT_FROM_ELEMENT_AND_COMPARE = "failure:get_text_from_element_and_compare"
    FAILURE_WEBDRIVER_WAIT_UNTIL_FAILURE = "failure:webdriver_wait_until_failure"
    FAILURE_WEBDRIVER_WAIT_UNTIL_ELEMENT_EXISTS_FAILURE = "failure:webdriver_wait_until_element_exists_failure"
    WEBDRIVER_WAIT_UNTIL_IGNORE_FAILURE = "webdriver_wait_until_ignore_failure"
