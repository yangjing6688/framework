import logging
from ansi2html.style import SCHEME as ANSI2HTML_COLOR_SCHEME
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.ConfigFileHelper import ConfigFileHelper
from ExtremeAutomation.Library.Utils.Singleton import Singleton

LOG_FORMAT = '[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s:%(lineno)s] [%(test_name)s] %(message)s'

colors_mapping = {
    logging.INFO: ANSI2HTML_COLOR_SCHEME.get("ansi2html")[5],
    logging.DEBUG: ANSI2HTML_COLOR_SCHEME.get("ansi2html")[2],
    logging.WARNING: ANSI2HTML_COLOR_SCHEME.get("ansi2html")[3],
    logging.ERROR: ANSI2HTML_COLOR_SCHEME.get("ansi2html")[1]
}


class Logging(logging.Logger, metaclass=Singleton):
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

    def get_logger(self):
        return self.logging

    @logger_not_initialised
    def configure_filter(self):
        self.logging.root.addFilter(FormatAndColorizeAndDispatchToRobot())

    @property
    def logger_level(self):
        self._logger_level = min(*[v for v in colors_mapping if isinstance(v, int)])
        return self._logger_level

    @logger_not_initialised
    def init_logger(self):
        self.old_record_factory = self.logging.getLogRecordFactory()
        self.logging.setLogRecordFactory(self.new_record_factory)

        self.setLevel(self.logger_level)
        self.configure_filter()

        self._logger_initialised = True


def _apply_html_coloring(message, color):
    return f"<div style='color: {color}'>{message}</div>"


class FormatAndColorizeAndDispatchToRobot(logging.Filter):
    def __init__(self):
        super().__init__()

    def filter(self, record):
        level_number = record.levelno
        formatted_message = self.format(record)
        colorized_message = _apply_html_coloring(formatted_message, colors_mapping.get(level_number))

        if level_number < logging.WARNING:  # WARN and ERROR already logged via log_to_file by Robot
            self.log_to_file(level_number, colorized_message)
            self.log_to_console(formatted_message)  # No support to customize colors
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
                robot = "WARN" if canonical == "WARNING" else canonical
                BuiltIn().log(message, robot, True)
            return with_html
