import logging
from functools import partial, partialmethod
from ansi2html.style import SCHEME as ANSI2HTML_COLOR_SCHEME
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.ConfigFileHelper import ConfigFileHelper
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from ExtremeAutomation.Library.Logger.Colors import Colors


LOG_FORMAT = '[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s:%(lineno)s] [%(test_name)s] %(message)s'

new_log_levels = {
    "TRACE":
        {
            "log_level_value": 7,
            "terminal_log_color": Colors.Fg.GREEN,
            "html_log_color": ANSI2HTML_COLOR_SCHEME.get("ansi2html")[3]
        }
}

terminal_colors_mapping = {
    "reset": Colors.Fg.RESET,
    logging.INFO: Colors.Fg.MAGENTA,
    logging.DEBUG: Colors.Fg.GREEN,
    logging.WARNING: Colors.Fg.YELLOW,
    logging.ERROR: Colors.Fg.RED
}

html_colors_mapping = {
    logging.INFO: ANSI2HTML_COLOR_SCHEME.get("ansi2html")[5],
    logging.DEBUG: ANSI2HTML_COLOR_SCHEME.get("ansi2html")[2],
    logging.WARNING: ANSI2HTML_COLOR_SCHEME.get("ansi2html")[3],
    logging.ERROR: ANSI2HTML_COLOR_SCHEME.get("ansi2html")[1]
}


class RobotLogger(logging.Logger, metaclass=Singleton):
    def __init__(self):
        super().__init__(__name__)
        self.logging = logging
        self._new_record_factory = None
        self._logger_level = None
        self._logger_initialised = False

        self.cfgHelp = ConfigFileHelper()
        self.cfgHelp.checkConfigRefresh()

        self.init_logger()

    @property
    def new_record_factory(self):
        if not self._new_record_factory:
            def record_factory(*args, **kwargs):
                record = self.old_record_factory(*args, **kwargs)
                record.test_name = BuiltIn().get_variable_value("${TEST NAME}")
                return record

            self._new_record_factory = record_factory
        return self._new_record_factory

    def logger_not_initialised(func):
        def wrapped_func(self, *args, **kwargs):
            if not self._logger_initialised:
                func(self, *args, **kwargs)

        return wrapped_func

    @logger_not_initialised
    def configure_new_logging_levels(self):
        for level_name, log_info in new_log_levels.items():
            setattr(self.logging, level_name, log_info["log_level_value"])
            self.logging.addLevelName(getattr(self.logging, level_name), level_name)
            setattr(self.logging.Logger, level_name.lower(),
                    partialmethod(self.logging.Logger.log, getattr(self.logging, level_name)))
            setattr(self.logging, level_name.lower(), partial(self.logging.log, getattr(self.logging, level_name)))
            terminal_colors_mapping[getattr(self.logging, level_name)] = log_info["terminal_log_color"]
            html_colors_mapping[getattr(self.logging, level_name)] = log_info["html_log_color"]

    @logger_not_initialised
    def configure_filter(self):
        test = self.level
        self.addFilter(FormatAndColorizeAndDispatchToRobot(self.level))

    @property
    def logger_level(self):
        robot_level = BuiltIn().get_variable_value("${LOG_LEVEL}")
        if str(robot_level) == "TRACE":
            return logging.DEBUG // 2
        return robot_level

    @logger_not_initialised
    def init_logger(self):
        self.configure_new_logging_levels()

        self.old_record_factory = self.logging.getLogRecordFactory()
        self.logging.setLogRecordFactory(self.new_record_factory)

        self.setLevel(self.logger_level)
        self.configure_filter()

        self._logger_initialised = True


def _apply_html_coloring(message, color):
    return f"<div style='color: {color}'>{message}</div>"

def _apply_terminal_coloring(message, color):
    return f"{color}{message}{terminal_colors_mapping['reset']}"


class FormatAndColorizeAndDispatchToRobot(logging.Filter):
    def __init__(self, level):
        self.level = level
        super().__init__()

    def filter(self, record):
        level_number = record.levelno
        if level_number < self.level:
            return False
        formatted_message = self.format(record)
        html_colorized = _apply_html_coloring(formatted_message, html_colors_mapping.get(level_number))
        terminal_colorized = _apply_terminal_coloring(formatted_message, terminal_colors_mapping.get(level_number))

        if level_number < logging.WARNING:  # WARN and ERROR already logged via log_to_file by Robot
            self.log_to_file(level_number, html_colorized)
            self.log_to_console(terminal_colorized)
        else:
            self.log_to_file(level_number, formatted_message)  # Prevent html data to be printed to console
        return False

    def format(self, record):
        class Formatter(logging.Formatter):
            def format(cls, record):
                cls._style._fmt = f"{LOG_FORMAT}"
                return super().format(record)

        return Formatter().format(record)

    def log_to_file(self, level_number, message):
        self.Dispatch()[level_number](message)

    def log_to_console(self, message):
        BuiltIn().log_to_console(message)

    class Dispatch(object):
        def __getitem__(self, level_number):
            def with_html(message):
                canonical = logging.getLevelName(level_number)
                robot = "WARN" if canonical == "WARNING" else canonical  # Robot usage is --loglevel WARN
                BuiltIn().log(message, robot, True)
            return with_html
