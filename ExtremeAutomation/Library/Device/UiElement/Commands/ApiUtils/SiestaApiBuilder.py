import platform
import datetime
from ExtremeAutomation.Library.Logger.Logger import Logger
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError


class SiestaApiBuilder(object):
    """
    This class defines all the supported actions that can be taken using the Siesta agent.

    Supported actions:
     - click
     - double click
     - right click
     - type
     - delay
     - component query
     - move cursor
     - screenshot

    All action functions can be passed named arguments in addition to their required/optional arguments.

    Supported Keyword Arguments (kwargs):
     - shift: Holds the shift key while taking action.
     - ctrl: Holds the ctrl key while taking action.
     - alt: Holds the alt key while taking action.
    """

    CLEAR_MODE_ALT = "alternate"  # Uses CTRL + A, backspace to clear existing text.
    COMPONENT_TYPE_TABLE = "table"
    COMPONENT_TYPE_TREE = "tree"
    COMPONENT_TYPE_MENU = "menu"
    COMPONENT_TYPE_COMBO = "combo"
    ACTION_CLICK = "click"
    ACTION_DOUBLE_CLICK = "doubleclick"
    ACTION_RIGHTCLICK = "rightclick"
    ACTION_MOUSE_DOWN = "mouseDown"
    ACTION_MOUSE_UP = "mouseUp"
    ACTION_TYPE = "type"
    ACTION_DELAY = "delay"
    ACTION_WAIT_FOR = "waitFor"
    ACTION_COMPONENT_QUERY = "componentquery"
    ACTION_QUERY_SELECTOR = "queryselector"
    ACTION_MOVE_CURSOR = "moveCursorTo"
    ACTION_SCREEN_SHOT = "screenshot"
    ACTION_EMC_UTIL = "emc_util"
    ACTION_EMC_UTIL_WAIT_FOR = "emc_util_wait_for"

    def __init__(self, ui_element):
        self.commands = []
        self.ui_element = ui_element
        self.logger = Logger()

    def add_click_command(self, ui_cmd_obj, target, timeout=None, wait_for_page_load=False, **kwargs):
        """
        [target] - The target that should be clicked.
        [timeout] - The length of time in milliseconds before the action is considered failing.
        [wait_for_page_Load] - A boolean that indicates whether or not to wait for the page to load
                               before moving on.

        This function will perform a click action on the provided target.
        """
        return self._add_command(ui_cmd_obj, self.ACTION_CLICK, target=target, timeout=timeout,
                                 wait_for_page_load=wait_for_page_load, **kwargs)

    def add_double_click_command(self, ui_cmd_obj, target, timeout=None, **kwargs):
        """
        [target] - The target that should be double clicked.
        [timeout] - The length of time in milliseconds before the action is considered failing.

        This function will perform a double click action on the provided target.
        """
        return self._add_command(ui_cmd_obj, self.ACTION_DOUBLE_CLICK, target=target, timeout=timeout, **kwargs)

    def add_right_click_command(self, ui_cmd_obj, target, timeout=None, **kwargs):
        """
        [target] - The target that should be right clicked.
        [timeout] - The length of time in milliseconds before the action is considered failing.

        This function will perform a right click action on the provided target.
        """
        return self._add_command(ui_cmd_obj, self.ACTION_RIGHTCLICK, target=target, timeout=timeout, **kwargs)

    def add_mouse_down_command(self, ui_cmd_obj, target, timeout=None, **kwargs):
        """
        [target] - The target that the mouse down action should be performed against.
        [timeout] - The length of time in milliseconds before the action is considered failing.

        This function will perform a mouse down action on the provided target.
        """
        return self._add_command(ui_cmd_obj, self.ACTION_MOUSE_DOWN, target=target, timeout=timeout, **kwargs)

    def add_mouse_up_command(self, ui_cmd_obj, target, timeout=None, **kwargs):
        """
        [target] - The target that the mouse up action should be performed against.
        [timeout] - The length of time in milliseconds before the action is considered failing.

        This function will perform a mouse up action on the provided target.
        """
        return self._add_command(ui_cmd_obj, self.ACTION_MOUSE_UP, target=target, timeout=timeout, **kwargs)

    def add_type_command(self, ui_cmd_obj, text, target=None, clear_existing=True, timeout=None, **kwargs):
        """
        [text] - The text to type into the given target.
        [target] - The target where the text should be typed.
        [clear_existing] - Whether or not the existing text should be cleared from the target.
        [timeout] - The length of time in milliseconds before the action is considered failing.

        This function will enter the provided text into the specified target.
        """
        return self._add_command(ui_cmd_obj, self.ACTION_TYPE, text=text, target=target,
                                 clear_existing=clear_existing, timeout=timeout, **kwargs)

    def add_delay_command(self, ui_cmd_obj, delay_in_ms, **kwargs):
        """
        [delay_in_ms] - The length of time in milliseconds to wait.

        This function will wait the specified amount of time before moving to the next step.
        """
        return self._add_command(ui_cmd_obj, self.ACTION_DELAY, delay=delay_in_ms, **kwargs)

    def add_component_query(self, ui_cmd_obj, target, args, timeout=None, **kwargs):
        """
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [timeout] - The length of time in milliseconds before the action is considered failing.

        Example:
        The following call
        self.add_component_query("grid[stateId=AlarmDefinitions]", "[0]")

        Would result in the following component query.
        Ext.ComponentQuery.query("grid[stateId=AlarmDefinitions]")[0]

        This function will perform a component query with the given target and arguments. If a string, boolean, int,
        float, or None (null) is returned by the component query the query_info attribute of ui_cmd_obj will be set to
        the returned value.
        """
        return self._add_command(ui_cmd_obj, self.ACTION_COMPONENT_QUERY, target=target, args=args, timeout=timeout,
                                 **kwargs)

    def add_document_query(self, ui_cmd_obj, target, args=None, timeout=None, **kwargs):
        """
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [timeout] - The length of time in milliseconds before the action is considered failing.

        Example:
        The following call
        self.add_document_query("grid[stateId=AlarmDefinitions]", "[0]")

        Would result in the following component query.
        document.querySelector("grid[stateId=AlarmDefinitions]")[0]

        This function will perform a querySelector query with the given target and arguments. If a string, boolean, int,
        float, or None (null) is returned by the document query the query_info attribute of ui_cmd_obj will be set to
        the returned value.
        """
        return self._add_command(ui_cmd_obj, self.ACTION_QUERY_SELECTOR, target=target, args=args, timeout=timeout,
                                 **kwargs)

    def add_move_cursor_command(self, ui_cmd_obj, target, timeout=None, **kwargs):
        """
        [target] - The target that the mouse cursor should be moved to. The target can either be set to a string or
        a list with two integers representing how far the cursor should move from the current location.
            Example: target="<siesta_target>" - Would move the cursor to <siesta_element>
                     target=[100, -100] - Would move the cursor right 100 pixels and up 100 pixels.
        [timeout] - The length of time in milliseconds before the action is considered failing.

        This function will move the cursor to the specified target.
        """
        return self._add_command(ui_cmd_obj, self.ACTION_MOVE_CURSOR, target=target, timeout=timeout, **kwargs)

    def add_screenshot_command(self, ui_cmd_obj, file_name=None, **kwargs):
        """
        [file_name] - The name to save the screenshot with. If no file_name is provided the screenshot will
                      be saved with a timestamp.

        This function takes a screenshot and saves it as the specified file name.
        """
        return self._add_command(ui_cmd_obj, self.ACTION_SCREEN_SHOT, file_name=file_name, **kwargs)

    def get_component_index(self, ui_cmd_obj, target, args, key=None, val=None, exact_match=True,
                            component_type=COMPONENT_TYPE_TABLE):
        """
        Args:
        [target] - The target of the component query.
        [args] - The args that should be appended to end of the component query.
        [key] - The key within the component to search for.
        [val] - The value the key should have configured.
        [exact_match] - A boolean flag that determines whether <table_val> must match the configured value exactly
                        or only needs to be found in the beginning of a the string. This value is defaulted to True.
        [component_type] - The type of component being inspected. The default is TABLE. Other supported values are
                           TREE, COMBO, and MENU.

                           The following arguments are required for each type.
                               - TABLE [target, args, key, val, exact_match]
                               - TREE [target, args, key, val, exact_match]
                               - COMBO [target, args, key, val, exact_match]
                               - MENU [target, args, val, exact_match]

        Example:
        The following call
        self.get_component_index("grid[stateId=AlarmDefinitions]", "[0]", "name", "AP Radio OnOff")

        Would result in the following component query.
        Ext.ComponentQuery.query("grid[stateId=AlarmDefinitions]")[0]

        This function returns the index if the key value pair is found within the component. It returns -1 if
        it is not found.
        """
        if not isinstance(exact_match, bool):
            exact_match = True

        if component_type in [self.COMPONENT_TYPE_TABLE,
                              self.COMPONENT_TYPE_COMBO,
                              self.COMPONENT_TYPE_TREE]:
            function_name = "find_component_index"
            util_args = [target, args, key, val, str(exact_match)]
        elif component_type == self.COMPONENT_TYPE_MENU:
            function_name = "find_menu_index"
            util_args = [target, args, val, str(exact_match)]
        else:
            raise ValueError("Invalid component type provided.")

        return self._add_command(ui_cmd_obj, self.ACTION_EMC_UTIL, function_name=function_name,
                                 function_args=util_args)

    def __get_data(self):
        return_data = {"data": self.commands}
        self.commands = []

        return return_data

    def _add_command(self, ui_cmd_obj, cmd_type, **kwargs):
        command = {"action": cmd_type}

        if "target" in kwargs:
            if isinstance(kwargs["target"], list):
                if len(kwargs["target"]) != 2:
                    raise ValueError("List must have only 2 entries.")
                if not isinstance(kwargs["target"][0], int) or not isinstance(kwargs["target"][1], int):
                    raise ValueError("List entries must be ints.")
                command["by"] = kwargs["target"]
            else:
                command["target"] = kwargs["target"]

        if "text" in kwargs:
            command["text"] = kwargs["text"]

        if "delay" in kwargs:
            command["delay"] = int(kwargs["delay"])

        if "options" in kwargs:
            command["options"] = kwargs["options"]

        if "args" in kwargs:
            if kwargs["args"] is not None:
                command["args"] = kwargs["args"]
            else:
                command["args"] = ""

        if "function_name" in kwargs:
            command["function_name"] = kwargs["function_name"]

        if "function_args" in kwargs:
            command["function_args"] = kwargs["function_args"]

        if "file_name" in kwargs:
            if kwargs["file_name"] is None:
                file_name = self.__get_time_stamp() + ".png"
            else:
                file_name = kwargs["file_name"].replace(" ", "_") + "-" + self.__get_time_stamp() + ".png"

            if "windows" in platform.platform().lower():
                command["file_name"] = "C:/Automation/screenshots/" + file_name
            else:
                if self.ui_element.connection_method.lower() == "siestatoselenium":
                    try:
                        variables_dict = BuiltIn().get_variables(no_decoration=True)
                        test_guid = variables_dict["environment"]["testguid"]
                        # This is temporary until we finalize linux behavior.
                        command["file_name"] = "/TRM_DATA/logs/" + test_guid + "/screenshots/" + file_name
                    except RobotNotRunningError:
                        command["file_name"] = "/TRM_DATA/logs/screenshots/" + file_name
                else:
                    command["file_name"] = "C:/Automation/screenshots/" + file_name

        if "timeout" in kwargs:
            if kwargs["timeout"] is not None and str(kwargs["timeout"]).isdigit():
                command["timeout"] = int(kwargs["timeout"])

        if "clear_existing" in kwargs:
            if kwargs["clear_existing"] == self.CLEAR_MODE_ALT:
                if "target" in kwargs:
                    self.__add_clear_existing(ui_cmd_obj, kwargs["target"])
                command["clear_existing"] = False
            else:
                command["clear_existing"] = kwargs["clear_existing"]

        if "wait_for_page_load" in kwargs:
            if kwargs["wait_for_page_load"]:
                command["action"] = self.ACTION_WAIT_FOR
                command["trigger"] = cmd_type

        for option in ["shift", "ctrl", "alt"]:
            if option in kwargs:
                if "options" in command:
                    command["options"][option + "Key"] = kwargs[option]
                else:
                    command["options"] = {option + "Key": kwargs[option]}

        self.commands.append(command)
        ui_cmd_obj.data = self.__get_data()
        self.__log_command(ui_cmd_obj.data)

        return self.ui_element.send_command_object(ui_cmd_obj)

    def __add_clear_existing(self, ui_cmd_obj, target):
        text1 = "a"
        text2 = "[BACKSPACE]"
        option1 = {"ctrlKey": True}

        self._add_command(ui_cmd_obj, self.ACTION_TYPE, target=target, text=text1, options=option1)
        self._add_command(ui_cmd_obj, self.ACTION_TYPE, target=target, text=text2)

    def __log_command(self, data):
        data = data["data"][0]
        message_content = ["| " + key + " = " + str(data[key]) for key in data]
        longest_line = max([len(i) for i in message_content])
        message_footer = "+" + "-" * longest_line + "+"
        message_header = ["+-------------------+",
                          "| Executing Command |",
                          "".join([c if index != 20 else "+" for index, c in enumerate(message_footer)])]
        message_content = [line + " " * (longest_line - len(line)) + " |" for line in message_content]
        message = message_header + message_content + [message_footer]
        self.logger.log_info("\n".join(message))

    @staticmethod
    def __get_time_stamp():
        now = datetime.datetime.now()

        month = ("0" + str(now.month))[-2:]
        day = ("0" + str(now.day))[-2:]
        hour = ("0" + str(now.hour))[-2:]
        minute = ("0" + str(now.minute))[-2:]
        second = ("0" + str(now.second))[-2:]

        return hour + "-" + minute + "-" + second + "-" + str(now.year) + "-" + month + "-" + day
