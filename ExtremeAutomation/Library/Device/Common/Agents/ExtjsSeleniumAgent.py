import re
import time
from ExtremeAutomation.Library.Device.Common.Agents.BaseSeleniumAgent import WebDriverException, Constants, \
    StaleElementReferenceException, JavascriptException
from ExtremeAutomation.Library.Device.Common.Agents.SeleniumAgent import SeleniumAgent
from selenium.common.exceptions import TimeoutException


class ExtjsSeleniumAgent(SeleniumAgent):
    def __init__(self, device):
        super(ExtjsSeleniumAgent, self).__init__(device)
        self.ext_constants = ExtjsSeleniumConstants()
        self.ext_actions = [getattr(self.ext_constants, i) for i in dir(self.ext_constants) if i.startswith("ACTION_")]
        self.valid_actions += self.ext_actions

    def find_element(self, target, strategy):
        """
        Function Args:
        [target] - The target of the element to attempt to find.
        [strategy] - The strategy to locate the element with.

        This function will check if the strategy is siesta, if it is it will use the function for finding
        siesta elements, otherwise it will use the find element function in the parent class.
        """
        if strategy == self.constants.STRATEGY_SIESTA:
            element = self.find_element_siesta(target)
            self.scroll_element_into_view(element)
            return element
        else:
            return super(ExtjsSeleniumAgent, self).find_element(target, strategy)

    def execute_async_script(self, **kwargs):
        """
        Call the super of execute_async_script
        """
        return super(ExtjsSeleniumAgent, self).selenium_execute_async_script(**kwargs)

    def execute_script(self, **kwargs):
        """
        Call the super of execute_script
        """
        return super(ExtjsSeleniumAgent, self).selenium_execute_script(**kwargs)

    def formatted_execute_async_script(self, script, return_val):
        """
        This function converts the provided script into a script that will work
        with execute_async_script.
        """
        js = """
             var callback = arguments[arguments.length - 1];

             {0}

             callback({1});
             """
        return self.driver.execute_async_script(self.format_js(js, script, return_val))

    def document_ready(self):
        """
        This waits until the document ready state is "complete". It will wait up to a minute for this.
        If the timeout expires a TimeoutException is raised.
        """
        timeout = 60 * 1000  # 1 minute in milliseconds.
        start = time.time()

        while time.time() - start < timeout:
            if self.formatted_execute_async_script("var state = document.readyState;", "state") == "complete":
                return True
        raise TimeoutException("Page state was not complete within " + str(timeout * 1000) + " seconds.")

    def document_query(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the document query.
        [args] - Any additional args that should be passed to the document query.

        Example:
        The following call
        self.add_document_query("grid[stateId=AlarmDefinitions]", "[0]")

        Would result in the following component query.
        self.execute_async_script('return document.querySelector('grid[stateId=AlarmDefinitions]')[0]')

        This function will perform a querySelector query with the given target and arguments and return the value.
        """
        target = self._check_kwargs(kwargs, "target")
        args = kwargs.get("args", "")

        return self.formatted_execute_async_script("var res = document.querySelector('" + str(target) + "')" +
                                                   args + ";", "res")

    def find_element_siesta(self, target):
        """
        Function Args:
        [target] - The siesta target of the element to attempt to find.
        [timeout] - The amount of time in seconds this function should search for the specified target.

        This function accepts a siesta identifier string and attempts to find the element on the current page.
        The supported identifiers are as follows.
          >> - If the string starts with >> it is considered a component query by siesta. To emulate this with
               selenium a component query that returns the element's ID is attempted first. Then the ID is used
               to find the element.
          => - If the string contains => it is considered a composite query. A composite query is made up of a
               component query and a CSS selector. First a component query returning the element's ID is attempted
               once the ID is retrieved it is added to the CSS selector and searched for using full CSS selector.
             - Finally if none of the above strings are found it is treated as a normal CSS selector.

        If the element was not found within timeout seconds then None is returned, otherwise the element is returned.
        """
        if target.startswith(">>"):
            _id = self.get_id_via_cq(target[2::])
            return self.driver.find_element_by_id(_id)
        elif "=>" in target:
            return self.find_element_composite_query(target)
        else:
            return self.find_element(target, self.constants.STRATEGY_CSS_SELECTOR)

    def find_element_composite_query(self, target):
        """
        Function Args:
        [target] - The siesta target string.

        This function attempts to emulate a siesta composite query. The target is first broken into two parts.
        The first being a component query, the second being a CSS selector. The component query attempts to find
        the ID of the target which is then appended to the CSS selector.

        This function also handles a few of the built in pseudo-selectors that siesta supports.
          :textEquals - This is emulated by using an x-path.
          :contains - This is emulated by using the contains function of jQuery.
          :nth-of-type - This is emulated by using the nth-of-type function of jQuery.

        This function returns the element if it is found.
        """
        current_element = None
        cq_target, css_target = target.split("=>")
        cq_len = self.get_cq_array_length(cq_target)

        for i in range(0, cq_len):
            _id = self.get_id_via_cq(cq_target, i)
            self.logger.log_trace("Found ID: " + _id)
            full_css_selector = ["#" + _id]
            current_element = None
            split_css = self.split_css_selector(css_target)

            for index, selector in enumerate(split_css):
                if ":textEquals" in selector:
                    if 1 > len(split_css) != index:
                        raise ValueError(":textEquals was not the last item in the composite query.")

                    select_text = self.get_pseudo_selector_target(":textEquals", css_target)
                    full_css_selector.append(selector.split(":")[0])
                    js = self.text_equals_js(" ".join(full_css_selector), select_text)
                    current_element = self.formatted_execute_async_script(js, "result")

                    if current_element is None:
                        if r"\.\.\." in select_text:
                            select_text = select_text.replace(r"\.\.\.", "...")
                        xpath = "//*[@id='" + _id + "']//*[.='" + select_text + "']"
                        current_element = self.driver.find_element_by_xpath(xpath)
                elif ":contains" in selector or ":nth-of-type" in selector:
                    full_css_selector.append(selector)
                elif ":" in selector:
                    raise ValueError(selector + " is not a recognized siesta pseudo selector.")
                else:
                    full_css_selector.append(selector)

            if current_element is None:
                js = "var item = jQuery('" + " ".join(full_css_selector) + "').get(0);"
                self.logger.log_trace("Attempting jQuery: " + js)
                current_element = self.formatted_execute_async_script(js, "item")
            if current_element is not None:
                break

        return current_element

    def get_id_via_cq(self, target, index=0):
        """
        Function Args:
        [target] - The target of the component query.
        [index] - The element within the returned array to get the ID of.

        This function returns the ID of the given target. This is mostly used to find elements using a component query.
        """
        function_re = r"\..*\(\)"
        args = "[" + str(index) + "]"

        for match in re.findall(function_re, target):
            args += match
            target = target.replace(match, "")

        args += ".id"

        return self.component_query(target=target, args=args)

    def get_cq_array_length(self, target):
        """
        Function Args:
        [target] - The target of the component query.

        This function returns the ID of the given target. This is mostly used to find elements using a component query.
        """
        function_re = r"\..*\(\)"

        for match in re.findall(function_re, target):
            target = target.replace(match, "")

        args = ".length"

        return int(self.component_query(target=target, args=args))

    @staticmethod
    def split_css_selector(css_selector):
        """
        This function will return a list of each CSS selector in a given css selector string.

        For example:
            This string ".x-grid-item:nth-of-type(2) .x-grid-cell-inner:textEquals(AC Power Recovered)"
            would return [".x-grid-item:nth-of-type(2)", ".x-grid-cell-inner:textEquals(AC Power Recovered)"]
        """
        norm_css_selector = css_selector.strip()
        split_selector = []
        current_str = ""
        num_parens = 0
        for index, char in enumerate(norm_css_selector):
            if char == " ":
                if num_parens == 0:
                    split_selector.append(current_str)
                    current_str = ""
                else:
                    current_str += char
            else:
                if char == "(":
                    num_parens += 1
                elif char == ")":
                    num_parens -= 1
                current_str += char

            if index == len(norm_css_selector) - 1:
                split_selector.append(current_str)

        return split_selector

    @staticmethod
    def get_pseudo_selector_target(selector_type, css_selector):
        """
        This function will return the target string for a given pseudo selector.

        For example:
            :textEquals(some_text) would return "some_text"
        """
        end_index = len(css_selector) - 1
        start_index = css_selector.find("(", css_selector.find(selector_type)) + 1
        for index, c in enumerate(css_selector[::-1]):
            if c == ")":
                end_index = end_index - index
                break

        return css_selector[start_index: end_index]

    def wait_for_load_masks(self, timeout=60):
        """
        This function checks for any element that starts with an id of "loadmask".
        It then verifies that none of the elements are displayed. It will wait up
        to <timeout> seconds for all elements to be hidden before failing. Returns
        True if all elements are hidden otherwise False is returned.
        """
        try:
            load_mask_elements = self.driver.find_elements_by_css_selector("[id^=loadmask]")
        except AttributeError:
            # The driver hasn't been created yet, this is probably being called
            # by open_web_page, no load masks can be present, return True.
            return True

        start = time.time()

        while len(load_mask_elements) > 0 and time.time() - start < timeout:
            tmp_elem_list = []
            for elem in load_mask_elements:
                try:
                    load_mask_id = elem.get_attribute("id")
                    if not self.component_query(target="[id=" + load_mask_id + "]", args="[0].hidden"):
                        tmp_elem_list.append(elem)
                except (StaleElementReferenceException, JavascriptException):
                    # The element is stale or doesn't have a .hidden attr, don't add it to the tmp list.
                    pass
            load_mask_elements = tmp_elem_list

        if len(load_mask_elements) != 0:
            return False
        return True

    # +---------------+
    # | ExtJS Actions |
    # +---------------+
    def component_query(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.

        Example:
        The following call
        self.component_query("grid[stateId=AlarmDefinitions]", "[0]")

        Would result in the following component query.
        self.execute_async_script('return Ext.ComponentQuery.query('grid[stateId=AlarmDefinitions]')[0]')

        This function will perform a component query with the given target and arguments. If the query returns
        a valid value it will be returned. There is a limit to how much information can be returned by a component
        query. In some cases the object may have too much information to return.
        """
        target, args = self._check_kwargs(kwargs, "target", "args")

        try:
            if self.document_ready():
                return self.formatted_execute_async_script("var res = Ext.ComponentQuery.query('" +
                                                           target + "')" + args + ";", "res")
        except WebDriverException as e:
            object_too_big_errors = ["too much recursion",
                                     "cyclic object value",
                                     "Maximum call stack size exceeded"]
            if any(err in e.msg for err in object_too_big_errors):
                return "Component query returned a value that could not be converted by selenium."
            raise e

    def get_component_index(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [key] - The key within the component to search for.
        [val] - The value the key should have configured.
        [exact_match] - A boolean flag that determines whether <table_val> must match the configured value exactly
                        or only needs to be found in the beginning of a the string. This value is defaulted to True.

        Example:
        The following call
        self.get_component_index("grid[stateId=AlarmDefinitions]", "[0]", "name", "AP Radio OnOff")

        Would result in the following component query.
        Ext.ComponentQuery.query("grid[stateId=AlarmDefinitions]")[0]

        This function returns the index if the key value pair is found within the component. It returns -1 if
        it is not found.
        """
        target, args, key, val, exact_match = self._check_kwargs(kwargs, "target", "args", "key", "val", "exact_match")

        if not exact_match:
            exact_match = "false"
        else:
            exact_match = "true"

        args = args + ".store.find('" + key + "', '" + val + "', undefined, undefined, undefined, " + exact_match + ")"
        return self.component_query(target=target, args=args, log_action=False)

    def get_menu_index(self, **kwargs):
        """
        Required kwargs:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [text] - The text that should be present in the component query return value.
        [exact_match] - Whether or not the text returned has to match exactly or simply exist
                        within the returned string.

        This function returns hte index if the text is found within the component. It returns -1 if no match
        is found.
        """
        target, args, text, exact_match = self._check_kwargs(kwargs, "target", "args", "text", "exact_match")

        js = self.menu_item_index_js(target, args, text, exact_match)
        return self.formatted_execute_async_script(js, "index")

    # +----------------------------------+
    # | Functions that return javascript |
    # +----------------------------------+
    def text_equals_js(self, css_selector, match_text):
        """
        Function Args:
        [css_selector] - The CSS selector string to provide to the jQuery function.
        [match_text] - This is the text that should be present in the returned element.

        This function returns the javascript to emulate the siesta textEquals pseudo selector.
        """
        js = """
             var jq_result = jQuery('{0}');
             var result;

             for (i = 0; i < jq_result.length; i++) {
             if (jq_result.get(i).innerText.trim() == '{1}') {
                     result = jq_result.get(i);
                     break
                 }
             }
             """
        return self.format_js(js, css_selector, match_text)

    def menu_item_index_js(self, target, args, match_text, exact_match):
        """
        Function Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [match_text] - The text that should be present in the component query return value.
        [exact_match] - Whether or not the text returned has to match exactly or simply exist
                        within the returned string.

        This function returns the javascript code to identify an items index within a component.
        """
        if not exact_match:
            exact_match = "false"
        else:
            exact_match = "true"

        js = """
             var exact_match = {3};
             var num_items = Ext.ComponentQuery.query('{0}'){1}.menu.items.items.length;
             var index = -1;

             if (num_items > 0) {
                 for (i = 0; i < num_items; i++) {
                     var item_name = Ext.ComponentQuery.query('{0}'){1}.menu.items.items[i.toString()].text;
                     if (exact_match === true) {
                         if (item_name === "{2}") {
                             index = i;
                         }
                     }
                     else {
                         if (item_name.indexOf("{2}") === 0) {
                             index = i;
                         }
                     }
                 }
             }
             """

        return self.format_js(js, target, args, match_text, exact_match)

    @staticmethod
    def format_js(js, *args):
        """
        Function Args:
        [js] - The javascript text to perform the replacement on.
        [*args] - The strings to substitute into <js>.

        This function behaves similarly to the python built-in str.format() function.
        It replaces each occurrence of {#} with the corresponding arg. The only difference
        being that it also replaces \n with "". This allows the javascript function to
        preserve formatting/readability and proper execution through selenium (normally newlines
        cause issues, so they are removed).
        """
        new_js = js

        for index, arg in enumerate(args):
            new_js = new_js.replace("{" + str(index) + "}", arg)

        return new_js.replace("\n", "")


class ExtjsSeleniumConstants(Constants):
    ACTION_COMPONENT_QUERY = "component_query"
    ACTION_GET_COMPONENT_INDEX = "get_component_index"
    ACTION_GET_MENU_INDEX = "get_menu_index"

    COMPONENT_TYPE_TABLE = "table"
    COMPONENT_TYPE_TREE = "tree"
    COMPONENT_TYPE_COMBO = "combo"
    COMPONENT_TYPE_MENU = "menu"
