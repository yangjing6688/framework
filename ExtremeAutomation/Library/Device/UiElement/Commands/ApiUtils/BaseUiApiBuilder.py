from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.Common.Agents.BaseSeleniumAgent import SeleniumConstants


class BaseUiApiBuilder(object):
    def __init__(self, device):
        self.device = device
        self.constants = SeleniumConstants()
        self.driver = None
        self.logger = Logger()

    def open_web_page(self, cmd_obj, browser, url, implicit_wait=None, delete_all_cookies=False, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [browser] - The browser to open the web page with.
        [url] - The URL the browser should load.

        This function opens a new browser and loads the specified url. It also maximizes the browser
        window.
        """
        args = {"browser": browser,
                "url": url,
                "implicit_wait": implicit_wait,
                "delete_all_cookies": delete_all_cookies}

        return self._add_action(cmd_obj, self.constants.ACTION_OPEN_PAGE, args, **kwargs)

    def open_new_browser_tab(self, cmd_obj, url, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.

        This function closes the browser.
        """
        args = {'url': url}
        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_OPEN_NEW_BROWSER_TAB, args, **kwargs)

    def switch_browser_tab(self, cmd_obj, title_name, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.

        This function closes the browser.
        """
        args = {'title_name': title_name}
        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_SWITCH_BROWSER_TAB, args, **kwargs)

    def close_browser_tab(self, cmd_obj, title_name=None, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.

        This function closes the browser.
        """
        args = {'title_name': title_name}
        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_CLOSE_BROWSER_TAB, args, **kwargs)

    def close_web_page(self, cmd_obj, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.

        This function closes the browser.
        """
        args = {}
        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_CLOSE_PAGE, args, **kwargs)

    def quit_web_page(self, cmd_obj, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.

        This function closes the browser.
        """
        args = {}
        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_CLOSE_PAGE, args, **kwargs)

    def click(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be clicked.

        This function clicks on the given target
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_CLICK, args, **kwargs)

    def double_click(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function double-clicks on the given target
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_DOUBLE_CLICK, args, **kwargs)

    def right_click(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be right clicked.

        This function right-clicks on the given target
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_RIGHT_CLICK, args, **kwargs)

    def mouse_down(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function will perform a mouse down action on the provided target.
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_MOUSE_DOWN, args, **kwargs)

    def mouse_up(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function will perform a mouse up action on the provided target.
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_MOUSE_UP, args, **kwargs)

    def move_to_element(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function will move the cursor to the specified target.
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_MOVE_TO_ELEMENT, args, **kwargs)

    def element_exists(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function will move the cursor to the specified target.
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_ELEMENT_EXISTS, args, **kwargs)

    def is_element_enabled(self, cmd_obj, target, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element

        This function will determine if an element is enabled and return a boolean value back
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_IS_ELEMENT_ENABLED, args,
                                **kwargs).return_data

    def is_element_selected(self, cmd_obj, target, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element

        This function will determine if an element is selected and return a boolean value back
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_IS_ELEMENT_SELECTED, args,
                                **kwargs).return_data

    def is_element_displayed(self, cmd_obj, target, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element

        This function will determine if an element is displayed is enabled and return a boolean value back
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_IS_ELEMENT_DISPLAYED, args,
                                **kwargs).return_data

    def get_text_from_element(self, cmd_obj, target, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element

        This function will determine if an element is enabled and return a boolean value back
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_GET_TEXT_FROM_ELEMENT, args,
                                **kwargs).return_data

    def get_attribute_from_element(self, cmd_obj, target, attribute, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element that the cursor should be moved to.
        [attribute] - The attribute of the element to return
        This function will get the attribute from the web element and return it
        """
        args = {"target": target,
                "attribute": attribute}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_GET_ATTRIBUTE_FROM_ELEMENT, args,
                                **kwargs).return_data

    def move_cursor_x_y(self, cmd_obj, x, y, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [x] - The amount of horizontal pixels the cursor should move.
        [y] - The amount of vertical pixels the cursor should move

        This function will move the cursor by [x, y] pixels.
        """
        args = {"x": x,
                "y": y}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_MOVE_CURSOR_X_Y, args, **kwargs)

    def find_element_by_name(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_element function and returns the webelement to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_FIND_ELEMENT_BY_NAME,
                                args, **kwargs).return_data

    def find_element_by_id(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_element function and returns the webelement to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_FIND_ELEMENT_BY_ID, args, **kwargs).return_data

    def find_element_by_xpath(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_element function and returns the webelement to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_FIND_ELEMENT_BY_XPATH, args,
                                **kwargs).return_data

    def find_element_by_link_text(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_element function and returns the webelement to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_FIND_ELEMENT_BY_LINK_TEXT,
                                args, **kwargs).return_data

    def find_element_by_partial_link_text(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_element function and returns the webelement to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_FIND_ELEMENT_BY_PARTIAL_LINK_TEXT,
                                args, **kwargs).return_data

    def find_element_by_tag_name(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_element function and returns the webelement to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_FIND_ELEMENT_BY_TAG_NAME,
                                args, **kwargs).return_data

    def find_element_by_class_name(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_element function and returns the webelement to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj,
                                self.constants.ACTION_SELENIUM_FIND_ELEMENT_BY_CLASS_NAME, args, **kwargs).return_data

    def find_element_by_css_selector(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_element function and returns the webelement to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj,
                                self.constants.ACTION_SELENIUM_FIND_ELEMENT_BY_CSS_SELECTOR, args, **kwargs).return_data

    def find_elements_by_name(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_elements function and returns all webelements to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj,
                                self.constants.ACTION_SELENIUM_FIND_ELEMENTS_BY_NAME, args, **kwargs).return_data

    def find_elements_by_id(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_elements function and returns all webelements to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj,
                                self.constants.ACTION_SELENIUM_FIND_ELEMENTS_BY_ID, args, **kwargs).return_data

    def find_elements_by_xpath(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_elements function and returns all webelements to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_FIND_ELEMENTS_BY_XPATH,
                                args, **kwargs).return_data

    def find_elements_by_link_text(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_elements function and returns all webelements to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_FIND_ELEMENTS_BY_LINK_TEXT,
                                args, **kwargs).return_data

    def find_elements_by_partial_link_text(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_elements function and returns all webelements to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_FIND_ELEMENTS_BY_PARTIAL_LINK_TEXT,
                                args, **kwargs).return_data

    def find_elements_by_tag_name(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_elements function and returns all webelements to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_FIND_ELEMENTS_BY_TAG_NAME, args,
                                **kwargs).return_data

    def find_elements_by_class_name(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_elements function and returns all webelements to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_FIND_ELEMENTS_BY_CLASS_NAME, args,
                                **kwargs).return_data

    def find_elements_by_css_selector(self, cmd_obj, target, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.

        This function calls the selenium find_elements function and returns all webelements to the user
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_FIND_ELEMENTS_BY_CSS_SELECTOR,
                                args, **kwargs).return_data

    def send_keys(self, cmd_obj, target, text, clear_existing=True, **kwargs):
        """
        [target] - The target of the element that should be clicked.
        [text] - text to send to target
        [clear_existing] - Boolean on whether or not to clear existing text

        This function will click the given target if it can be located on the page.
        """
        args = {"target": target,
                "text": text,
                "clear_existing": clear_existing}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_SEND_KEYS, args, **kwargs)

    def execute_async_script(self, cmd_obj, script, target=None, **kwargs):
        """
        [target] - The target of the element that should be clicked.
        [script] - The java script to execute

        This function will execute the java script given on the target using execute_async_script
        """
        args = {"script": script,
                "target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_EXECUTE_ASYNC_SCRIPT, args, **kwargs)

    def execute_script(self, cmd_obj, script, target=None, **kwargs):
        """
        [target] - The target of the element that should be clicked.
        [script] - The java script to execute

        This function will execute the java script given on the target using execute_script
        """
        args = {"script": script,
                "target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_EXECUTE_SCRIPT, args, **kwargs)

    def drag_and_drop(self, cmd_obj, element, target, **kwargs):
        """
        [target] - The target to drop the element
        [element] - The element to move

        This function will drag the element to the target
        """
        args = {"element": element,
                "target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_DRAG_AND_DROP, args, **kwargs)

    def drag_and_drop_by_offset(self, cmd_obj, element, x, y, **kwargs):
        """
        [element] - The element to move
        [x] - The x position
        [y] - The y position

        This function will drag the element to the x,y offset given
        """
        args = {"element": element,
                "x": x,
                "y": y}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_DRAG_AND_DROP_BY_OFFSET, args, **kwargs)

    def accept_alert(self, cmd_obj, **kwargs):
        """
        This function will switch to and accept an alert
        """
        args = {}
        return self._add_action(cmd_obj, self.constants.ACTION_ACCEPT_ALERT, args,
                                **kwargs)

    def dismiss_alert(self, cmd_obj, **kwargs):
        """
        This function will switch to and dismiss an alert
        """
        args = {}
        return self._add_action(cmd_obj, self.constants.ACTION_DISMISS_ALERT, args,
                                **kwargs)

    def get_text_from_alert(self, cmd_obj, **kwargs):
        """
        This function will grab the given text from the alert window
        """
        args = {}
        return self._add_action(cmd_obj, self.constants.ACTION_GET_TEXT_FROM_ALERT, args,
                                **kwargs).return_data

    def send_keys_to_alert(self, cmd_obj, text, **kwargs):
        """
        This function will send text to the alert window
        """
        args = {"text": text}
        return self._add_action(cmd_obj, self.constants.ACTION_SEND_KEYS_TO_ALERT, args,
                                **kwargs)

    def delay(self, cmd_obj, delay, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [delay] - The length of time in seconds to wait.

        This function will wait the specified amount of time before moving to the next step.
        """
        args = {"delay": delay}

        return self._add_action(cmd_obj, self.constants.ACTION_DELAY, args, **kwargs)

    def screen_shot(self, cmd_obj, file_name, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [file_name] - The name to save the screenshot with. If no file_name is provided the screenshot will
                      be saved with a timestamp.

        This function takes a screenshot and saves it as the specified file name.
        """
        args = {"file_name": file_name}

        return self._add_action(cmd_obj, self.constants.ACTION_SCREEN_SHOT, args, **kwargs)

    def select_and_click_multiple_elements(self, cmd_obj, start_element, end_element, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element that the cursor should click first.
        [end_element] - The target of the element that the cursor should click last.
        This function will shift click multiple web elements
        """
        args = {"target": start_element,
                "end_element": end_element}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_SELECT_AND_CLICK_MULTIPLE_ELEMENTS, args,
                                **kwargs)

    def move_cursor_out_of_element(self, cmd_obj, target, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element that the cursor should be moved away from
        This function will move the cursor out from the element that is selected
        """
        args = {"target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_MOVE_CURSOR_OUT_OF_ELEMENT, args, **kwargs)

    def windows_file_browser_enter_path_text(self, cmd_obj, window_title, path, **kwargs):
        """
        [win_title] - the title on the window to access
        [path] - the path to input into the window

        Enters a file/folder path in the windows file browser path.
        """
        args = {"win_title": window_title,
                "path": path}
        return self._add_action(cmd_obj, self.constants.ACTION_WINDOWS_FILE_BROWSER_ENTER_PATH_TEXT, args,
                                **kwargs).return_data

    def webdriver_wait_until(self, cmd_obj, target, timeout=1, retry=15, strategy=SeleniumConstants.STRATEGY_XPATH,
                             condition=SeleniumConstants.CONDITION_ELEMENT_TO_BE_CLICKABLE, ignore_outcome=False,
                             **kwargs):
        """
        Required kwargs:
        [target] - The target of the element
        [timeout] - How long for the webdriver to wait
        [retry] - How many times to retry
        [strategy] - The location strategy to use
        [condition] - The specific webdriver wait function to run
        [ignore_outcome] - Whether or not to fail the function based on the result
        This function executes the webdriver wait function based on condition
        """
        args = {"target": target,
                "timeout_ww": timeout,
                "retry": retry,
                "strategy": strategy,
                "condition": condition,
                'ignore_outcome': ignore_outcome}

        return self._add_action(cmd_obj, self.constants.ACTION_WEBDRIVER_WAIT_UNTIL, args, **kwargs).return_data

    def webdriver_wait_until_element_exists(self, cmd_obj, target, timeout=1, retry=15,
                                            strategy=SeleniumConstants.STRATEGY_XPATH,
                                            condition=SeleniumConstants.CONDITION_ELEMENT_TO_BE_CLICKABLE,
                                            exists=True, **kwargs):
        """
        Required kwargs:
        [target] - The target of the element
        [timeout] - How long for the webdriver to wait
        [retry] - How many times to retry
        [strategy] - The location strategy to use
        [condition] - The specific webdriver wait function to run
        This function executes the webdriver wait function based on condition
        """
        args = {"target": target,
                "timeout_ww": timeout,
                "retry": retry,
                "strategy": strategy,
                "condition": condition,
                'ignore_outcome': False,
                'exists': exists}
        kwargs["ignore_outcome"] = False
        return self._add_action(cmd_obj, self.constants.ACTION_SELENIUM_WEBDRIVER_WAIT_UNTIL_ELEMENT_EXISTS, args,
                                **kwargs).return_data

    # +----------------------------+
    # | Non Builder Helper Methods |
    # +----------------------------+
    def _add_action(self, cmd_obj, action, args, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [action] - The action to take.
        [args] - The arguments needed for the action.

        Takes the appropriate action based on the passed command object.
        """
        self._log_action(action, args, **kwargs)

        cmd_obj.action = action
        args.update(kwargs)
        cmd_obj.args = args
        cmd_obj = self.device.send_command_object(cmd_obj)

        # This attempts to retrieve the current driver object from the Selenium agent.
        # This only happens if the driver has not yet been set.
        if self.driver is None:
            try:
                self.driver = self.device.current_agent.driver
            except AttributeError:
                pass

        return cmd_obj

    def _log_action(self, action, args, **kwargs):
        """
        This function logs the currently running action with the following format.

        +-------------------+
        | Executing Command |
        +-------------------+
        | action: <action>  |
        | arg1: <arg1_val>  |
        | arg2: <arg2_val>  |
        | argN: <argN_val>  |
        +-------------------+

        """
        log = kwargs.get("log_action", True)

        if log:
            # This adds the line | action: <cmd_obj.action.
            message_content = ["| action: " + action]

            # This iterates over each key in the cmd_obj.args dict and adds | <key>: <val> for each key value pair.
            # Ignores "log_action" if that is present in the arg dict, as it is only used to tell the action if it
            # should log.
            message_content += ["| " + key + ": " + str(args[key]) for key in args if key not in ["log_action",
                                                                                                  "action_name"]]

            # This finds the line in the content list that is the longest, we'll use this to fill out
            # the header and footer sections.
            longest_line = max([len(i) for i in message_content])
            longest_line = longest_line if longest_line > 21 else 21

            # Define the message footer it is "+" plus "-" * <longest_line> plus "+".
            message_footer = ["+" + "-" * longest_line + "+"]

            # Defines the message header. It first adds "+-------------------+" and "| Executing Command |".
            # Then it adds "+" and "-" up until the longest line then adds another "+". Finally it fills
            # "-" until the last character which is a "+".
            message_header = ["+-------------------+", "| Executing Command |",
                              "".join([c if index != 20 else "+" for index, c in enumerate(message_footer[0])])]

            # This adds longest_line - len(line) whitespace and a "|" to each line in the content.
            message_content = [line + " " * (longest_line - len(line)) + " |" for line in message_content]

            # Join each section with a newline and log it at info level.
            self.logger.log_info("\n" + "\n".join(message_header + message_content + message_footer))
