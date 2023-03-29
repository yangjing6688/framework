"""
Enhance and fix logging issues for Robot tests.
Most of the functionality is ported from PytestLogger.

Features:
1. Prepend console logging with:
- [Logged time] [Logged Message Level] [Source Module] [Source File:Source Line] [Test Name|SETUP|TEARDOWN].

2. Prepend HTML logging differently since the logged time is written by Robot:
- [Logged Message Level] [Source Module] [Source File:Source Line] [Test Name|SETUP|TEARDOWN].

3. Sets logging level is set to the configured run option.

4. Add the Robot's native TRACE level logging accessible via logging.trace()

5. Color HTML and console messages.

6. Fix missing new line when Robot prints start of test.

7. Prepend SETUP or TEARDOWN instead of test name according to test phase.
"""

import logging
from functools import partial, partialmethod

import robot.output.listeners
from ansi2html.style import SCHEME as ANSI2HTML_COLOR_SCHEME
from robot.libraries.BuiltIn import BuiltIn
from robot.output.logger import LOGGER as InternalRobotLogger
from extauto.common.ConfigFileHelper import ConfigFileHelper
from ExtremeAutomation.Library.Utils.Singleton import Singleton
from ExtremeAutomation.Library.Logger.Colors import Colors
from types import MethodType


CONSOLE_LOG_FORMAT = '[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s:%(lineno)s] [%(test_name)s] %(message)s'
HTML_LOG_FORMAT = '[%(levelname)s] [%(module)s] [%(funcName)s:%(lineno)s] [%(test_name)s] %(message)s'

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
                try:
                    test_name = BuiltIn().get_variable_value("${TEST NAME}")
                    if not test_name:
                        status = BuiltIn().get_variable_value("${SUITE STATUS}")
                        test_name = "TEARDOWN" if status else "SETUP"
                    record.test_name = test_name
                except Exception:
                    pass
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
    def configure_internal_robot_logger(self):
        def patch_message(_self, msg):
            """Messages about what the framework is doing, warnings, errors, ..."""
            if not _self._cache_only:
                for logger in _self:
                    test = logger
                    if hasattr(msg.message, "skipConsoleAutoPrint") and hasattr(logger, "logger") and isinstance(logger.logger, robot.output.console.verbose.VerboseOutput):
                        pass
                    else:
                        logger.message(msg)
            if _self._message_cache is not None:
                _self._message_cache.append(msg)
            if msg.level == 'ERROR':
                _self._error_occurred = True
                if _self._error_listener:
                    _self._error_listener()

        InternalRobotLogger.message = MethodType(patch_message, InternalRobotLogger)

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

        self.configure_internal_robot_logger()

        self._logger_initialised = True


def _apply_html_coloring(message, color):
    return f"<div style='color: {color}'>{message}</div>"


def _apply_terminal_coloring(message, color):
    return f"{color}{message}{terminal_colors_mapping['reset']}"


class FormatAndColorizeAndDispatchToRobot(logging.Filter):
    def __init__(self, level):
        self.level = level
        self.currentTest = None
        super().__init__()

    def filter(self, record):
        level_number = record.levelno
        if level_number < self.level:
            return False
        console_formatted_message = self.console_format(record)
        html_formatted_message = self.html_format(record)
        html_colorized = _apply_html_coloring(html_formatted_message, html_colors_mapping.get(level_number))
        terminal_colorized = _apply_terminal_coloring(console_formatted_message, terminal_colors_mapping.get(level_number))

        self.log_to_file(level_number, html_colorized)
        self.log_to_console(level_number, terminal_colorized)
        return False

    def console_format(self, record):
        class Formatter(logging.Formatter):
            def format(cls, record):
                cls._style._fmt = f"{CONSOLE_LOG_FORMAT}"
                return super().format(record)

        return Formatter().format(record)

    def html_format(self, record):
        class Formatter(logging.Formatter):
            def format(cls, record):
                cls._style._fmt = f"{HTML_LOG_FORMAT}"
                return super().format(record)

        return Formatter().format(record)

    def log_to_file(self, level_number, message):
        self.Dispatch()[level_number](message)

    def log_to_console(self, level_number, message):
        stream = "STDOUT" if level_number < logging.WARNING else "STDERR"

        if stream == "STDOUT" and self.is_first_message():
            BuiltIn().log_to_console("")

        BuiltIn().log_to_console(message, stream)

    def is_first_message(self):
        test_name = BuiltIn().get_variable_value("${TEST NAME}")
        if self.currentTest != test_name:
            self.currentTest = test_name
            return True
        return False

    class Dispatch(object):
        def __getitem__(self, level_number):
            def with_html(message):
                canonical = logging.getLevelName(level_number)
                robot_level = "WARN" if canonical == "WARNING" else canonical  # Robot usage is --loglevel WARN
                flagged_message = FlaggedMessage(message)
                BuiltIn().log(flagged_message, robot_level, True)
            return with_html


class FlaggedMessage(str):
    def __new__(cls, content):
        cls.skipConsoleAutoPrint = True
        return str.__new__(cls, content)

