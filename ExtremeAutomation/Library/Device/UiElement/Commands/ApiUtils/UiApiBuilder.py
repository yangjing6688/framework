from ExtremeAutomation.Library.Device.Common.Agents.BaseSeleniumAgent import SeleniumConstants
from ExtremeAutomation.Library.Device.UiElement.Commands.ApiUtils.BaseUiApiBuilder import BaseUiApiBuilder


class UiApiBuilder(BaseUiApiBuilder):
    def __init__(self, device):
        super(UiApiBuilder, self).__init__(device)

    def open_web_page(self, cmd_obj, browser, url, implicit_wait=None, delete_all_cookies=False, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [browser] - The browser to open the web page with.
        [url] - The URL the browser should load.

        This function opens a new browser and loads the specified url. It also maximizes the browser
        window.
        """
        return super(UiApiBuilder, self).open_web_page(cmd_obj, browser, url, implicit_wait, delete_all_cookies,
                                                       **kwargs)

    def delay(self, cmd_obj, delay, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [delay] - The length of time in seconds to wait.

        This function will wait the specified amount of time before moving to the next step.
        """
        return super(UiApiBuilder, self).delay(cmd_obj, delay, **kwargs)

    def screen_shot(self, cmd_obj, file_name, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [file_name] - The name to save the screenshot with. If no file_name is provided the screenshot will
                      be saved with a timestamp.

        This function takes a screenshot and saves it as the specified file name.
        """
        return super(UiApiBuilder, self).screen_shot(cmd_obj, file_name, **kwargs)

    def move_cursor_x_y(self, cmd_obj, x, y, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [x] - The amount of horizontal pixels the cursor should move.
        [y] - The amount of vertical pixels the cursor should move

        This function will move the cursor by [x, y] pixels.
        """
        return super(UiApiBuilder, self).move_cursor_x_y(cmd_obj, x, y, **kwargs)

    def document_query(self, cmd_obj, target, args="", **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.

        Example:
        The following call
        self.add_document_query("grid[stateId=AlarmDefinitions]", "[0]")

        Would result in the following component query.
        document.querySelector("grid[stateId=AlarmDefinitions]")[0]

        This function will perform a querySelector query with the given target and arguments. The return_data
        attribute of ui_cmd_obj will be set to the returned value.
        """
        args = {"target": target,
                "args": args}

        return self._add_action(cmd_obj, self.constants.ACTION_DOCUMENT_QUERY, args, **kwargs)

    def windows_file_browser_enter_path_text(self, cmd_obj, window_title, path, **kwargs):
        """
        Enters a file/folder path in the windows file browser path.
        """
        return super(UiApiBuilder, self).windows_file_browser_enter_path_text(cmd_obj, window_title, path, **kwargs)

    def execute_async_script(self, cmd_obj, script, return_val=None, **kwargs):
        """
        This calls the parent class's execute_async_script method
        """
        return super(UiApiBuilder, self).execute_async_script(cmd_obj, script, return_val)

    def execute_script(self, cmd_obj, script, return_val=None, **kwargs):
        """
        This calls the parent class's execute_script method
        """
        return super(UiApiBuilder, self).execute_script(cmd_obj, script, return_val)

    def click_boundlist_item(self, cmd_obj, target, item, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - the target
        [item] - the item to locate
        [strategy] - the strategy to use to locate the element
        This function closes the browser.
        """
        args = {"target": target,
                "item": item,
                "strategy": strategy}
        return self._add_action(cmd_obj, self.constants.ACTION_CLICK_BOUNDLIST_ITEM, args, **kwargs)

    def close_web_page(self, cmd_obj, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.

        This function closes the browser.
        """
        args = {}
        self._add_action(cmd_obj, self.constants.ACTION_CLOSE_PAGE, args, **kwargs)

    def click(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be clicked.
        [strategy] - The element location strategy to use.

        This function will perform a click action on the provided target.
        """
        args = {"target": target,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_CLICK, args, **kwargs)

    def double_click(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.
        [strategy] - The element location strategy to use.

        This function will perform a double click action on the provided target.
        """
        args = {"target": target,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_DOUBLE_CLICK, args, **kwargs)

    def right_click(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.
        [strategy] - The element location strategy to use.

        This function will perform a right click action on the provided target.
        """
        args = {"target": target,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_RIGHT_CLICK, args, **kwargs)

    def mouse_down(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.
        [strategy] - The element location strategy to use.

        This function will perform a mouse down action on the provided target.
        """
        args = {"target": target,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_MOUSE_DOWN, args, **kwargs)

    def mouse_up(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.
        [strategy] - The element location strategy to use.

        This function will perform a mouse up action on the provided target.
        """
        args = {"target": target,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_MOUSE_UP, args, **kwargs)

    def move_cursor(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target that should be double clicked.
        [strategy] - The element location strategy to use.

        This function will move the cursor to the specified target.
        """
        args = {"target": target,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_MOVE_CURSOR, args, **kwargs)

    def enter_text(self, cmd_obj, text, target, strategy=SeleniumConstants.STRATEGY_XPATH, clear_existing=True,
                   **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target where the text should be typed.
        [text] - The text to type into the given target.
        [strategy] - The element location strategy to use.
        [clear_existing] - Whether or not the existing text should be cleared from the target.

        This function will enter the provided text into the specified target.
        """
        args = {"target": target,
                "text": text,
                "strategy": strategy,
                "clear_existing": clear_existing}

        return self._add_action(cmd_obj, self.constants.ACTION_TYPE, args, **kwargs)

    def enter_text_no_target(self, cmd_obj, text, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [text] - The text to type into the given target.

        This function will enter the provided text into whichever element is currently active.
        """
        args = {"text": text}

        return self._add_action(cmd_obj, self.constants.ACTION_TYPE, args, **kwargs)

    def find_element(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target of the component query.
        [strategy] - The element location strategy to use.

        This function returns the selenium element that is located with the provided <target> and <strategy>.
        """
        args = {"target": target,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_FIND_ELEMENT, args, **kwargs).return_data

    def find_elements(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_ELEMENTS_XPATH, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target of the component query.
        [strategy] - The element location strategy to use.

        This function returns the selenium element that is located with the provided <target> and <strategy>.
        """
        args = {"target": target,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_FIND_ELEMENTS, args, **kwargs).return_data

    def get_text_from_element_and_compare(self, cmd_obj, target, text, strategy=SeleniumConstants.STRATEGY_XPATH,
                                          **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target of the component query.
        [strategy] - The element location strategy to use.
        [text] - The given text to compare against

        This function compares given text{text} against the web element text
        """
        args = {"target": target,
                "text": text,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_GET_TEXT_FROM_ELEMENT_AND_COMPARE, args,
                                **kwargs).return_data

    def get_attribute_from_element_and_compare(self, cmd_obj, target, attribute, value,
                                               strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target of the component query.
        [strategy] - The element location strategy to use.
        [text] - The given text to compare against

        This function compares given text{text} against the web element text

        """
        args = {"target": target,
                "value": value,
                "strategy": strategy,
                "attribute": attribute}

        return self._add_action(cmd_obj, self.constants.ACTION_GET_ATTRIBUTE_FROM_ELEMENT_AND_COMPARE, args,
                                **kwargs).return_data

    def is_element_enabled(self, cmd_obj, target, enabled=True, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element

        This function will determine if an element is enabled and return a boolean value back
        """
        args = {"target": target,
                "enabled": enabled,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_IS_ELEMENT_ENABLED, args,
                                **kwargs).return_data

    def is_element_selected(self, cmd_obj, target, selected=True, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element

        This function will determine if an element is selected and return a boolean value back
        """
        args = {"target": target,
                "selected": selected,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_IS_ELEMENT_SELECTED, args,
                                **kwargs).return_data

    def is_element_displayed(self, cmd_obj, target, displayed=True,
                             strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element

        This function will determine if an element is displayed is enabled and return a boolean value back
        """
        args = {"target": target,
                "displayed": displayed,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_IS_ELEMENT_DISPLAYED, args,
                                **kwargs).return_data

    def get_text_from_element(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element

        This function will determine if an element is enabled and return a boolean value back
        """
        args = {"target": target,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_GET_TEXT_FROM_ELEMENT, args,
                                **kwargs).return_data

    def get_attribute_from_element(self, cmd_obj, target, attribute, strategy=SeleniumConstants.STRATEGY_XPATH,
                                   **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that the cursor should be moved to.
        [attribute] - The attribute of the element to return
        This function will get the attribute from the web element and return it
        """
        args = {"target": target,
                "attribute": attribute,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_GET_ATTRIBUTE_FROM_ELEMENT, args, **kwargs).return_data

    def element_exists(self, cmd_obj, target, exists=True, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        [cmd_obj] - An instance of a UiCommandObject.
        [target] - The target of the component query.
        [strategy] - The element location strategy to use.
        [text] - The given text to compare against

        This function compares given text{text} against the web element text

        """
        args = {"target": target,
                "exists": exists,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_ELEMENT_EXISTS, args, **kwargs).return_data

    def get_length_of_find_elements(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that the cursor should be moved to.
        This function will return the length of find_elements
        """
        args = {"target": target,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_GET_LENGTH_OF_FIND_ELEMENTS, args, **kwargs).return_data

    def wait_for_document_ready(self, cmd_obj, state="complete", retry='30', target=None, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that the cursor should be moved to.
        This function will return the length of find_elements
        """
        args = {"script": "return document.readyState;",
                "state": state,
                "retry": retry,
                "target": target}

        return self._add_action(cmd_obj, self.constants.ACTION_WAIT_FOR_DOCUMENT_READY, args, **kwargs)

    def select_and_click_multiple_elements(self, cmd_obj, start_element, end_element,
                                           strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that the cursor should click first.
        [end_element] - The target of the element that the cursor should click last.
        This function will shift click multiple web elements
        """
        args = {"target": start_element,
                "end_element": end_element,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_SELECT_AND_CLICK_MULTIPLE_ELEMENTS, args, **kwargs)

    def move_cursor_out_of_element(self, cmd_obj, target, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        Required kwargs:
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target of the element that the cursor should be moved away from
        This function will move the cursor out from the element that is selected
        """
        args = {"target": target,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_MOVE_CURSOR_OUT_OF_ELEMENT, args, **kwargs)

    def drag_and_drop(self, cmd_obj, element, target, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [target] - The target to drop the element
        [element] - The element to move

        This function will drag the element to the target
        """
        args = {"element": element,
                "target": target,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_DRAG_AND_DROP, args,
                                **kwargs)

    def drag_and_drop_by_offset(self, cmd_obj, element, x, y, strategy=SeleniumConstants.STRATEGY_XPATH, **kwargs):
        """
        [strategy] - The element location strategy to use. Constants can be found in SeleniumConstants.
        [element] - The element to move
        [x] - The x position
        [y] - The y position

        This function will drag the element to the x,y offset given
        """
        args = {"element": element,
                "x": x,
                "y": y,
                "strategy": strategy}

        return self._add_action(cmd_obj, self.constants.ACTION_DRAG_AND_DROP_BY_OFFSET, args,
                                **kwargs)

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
        kwargs['ignore_outcome'] = False

        return self._add_action(cmd_obj, self.constants.ACTION_WEBDRIVER_WAIT_UNTIL_ELEMENT_EXISTS, args,
                                **kwargs).return_data
