import logging
from ansi2html.style import SCHEME as ansi2html_color_scheme
from functools import partial, partialmethod
from robot.api import logger as robot_logger
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.ConfigFileHelper import ConfigFileHelper
from ExtremeAutomation.Library.Utils.Singleton import Singleton

LOG_FORMAT = '[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s:%(lineno)s] [%(test_name)s] %(message)s'

new_log_levels = {
    "STEP":
        {
            "log_level_value": 5,
            "log_color": ansi2html_color_scheme.get("ansi2html")[6]
        },
    "CLI":
        {
            "log_level_value": 6,
            "log_color": ansi2html_color_scheme.get("ansi2html")[4]
        },
    "TRACE":
        {
            "log_level_value": 7,
            "log_color": ansi2html_color_scheme.get("ansi2html")[2]
        }
}

colors_mapping = {
    logging.INFO: ansi2html_color_scheme.get("ansi2html")[5],
    logging.DEBUG: ansi2html_color_scheme.get("ansi2html")[2],
    logging.WARNING: ansi2html_color_scheme.get("ansi2html")[3],
    logging.CRITICAL: ansi2html_color_scheme.get("ansi2html")[1],
    logging.ERROR: ansi2html_color_scheme.get("ansi2html")[1]
}

method_mapping = {
    logging.INFO: robot_logger.info,
    logging.DEBUG: robot_logger.debug,
    logging.WARNING: robot_logger.warn,
    logging.CRITICAL: robot_logger.error,
    logging.ERROR: robot_logger.error,
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

    @logger_not_initialised
    def configure_new_logging_levels(self):
        for level_name, log_info in new_log_levels.items():
            setattr(self.logging, level_name, log_info["log_level_value"])
            self.logging.addLevelName(getattr(self.logging, level_name), level_name)
            setattr(self.logging.Logger, level_name.lower(),
                    partialmethod(self.logging.Logger.log, getattr(self.logging, level_name)))
            setattr(self.logging, level_name.lower(), partial(self.logging.log, getattr(self.logging, level_name)))
            colors_mapping[getattr(self.logging, level_name)] = log_info["log_color"]
        method_mapping.update({
            logging.STEP: robot_logger.trace,
            logging.CLI: robot_logger.trace,
            logging.TRACE: robot_logger.trace
        })

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
        self.configure_new_logging_levels()

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
        self.log(level_number, colorized_message)
        return False

    def format(self, record):
        class Formatter(logging.Formatter):
            def format(cls, record):
                cls._style._fmt = f"{LOG_FORMAT}"
                return super().format(record)

        return Formatter().format(record)

    def log(self, level_number, message):
        self.Dispatch()[level_number](message)

    class Dispatch(object):
        def __getitem__(self, level_number):
            def with_html(message):
                method_mapping.get(level_number)(message, html=True)
            return with_html
