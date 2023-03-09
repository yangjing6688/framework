import imp
import sys
import pytest

from functools import partial, partialmethod
from pytest_testconfig import config
from ExtremeAutomation.Library.Logger.Colors import Colors
from ExtremeAutomation.Library.Utils.Singleton import Singleton


LOG_FORMAT = '[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s:%(lineno)s] [%(test_name)s] %(message)s'
logging = imp.load_module("logging_module", *imp.find_module("logging"))

new_log_levels = {
    "STEP": 
        {
            "log_level_value": 5,
            "log_color": Colors.Fg.CYAN
        },
    "CLI": 
        {
            "log_level_value": 6,
            "log_color": Colors.Fg.BLUE
        },
    "TRACE": 
        {
            "log_level_value": 7,
            "log_color": Colors.Fg.GREEN
        }
}

colors_mapping = {
    "reset": Colors.Fg.RESET,
    logging.INFO: Colors.Fg.MAGENTA,
    logging.DEBUG: Colors.Fg.GREEN,
    logging.WARNING: Colors.Fg.YELLOW,
    logging.CRITICAL: Colors.Fg.RED,
    logging.ERROR: Colors.Fg.RED
}


class PytestLogger(logging.Logger, metaclass=Singleton):
    
    def __init__(self, pytest_config=config):
        
        super().__init__(__name__)

        self.pytest_config = pytest_config
        self.logging = logging
        self._new_record_factory = None
        self._formatter_cls = None
        self._stream_handler = None
        self._logger_level = None
        self._logger_initialised = False
    
        self.init_logger()

    @property
    def new_record_factory(self):
        if not self._new_record_factory:
            def record_factory(*args, **kwargs):
                record = self.old_record_factory(*args, **kwargs)
                record.test_name = self.pytest_config.get("${TEST_NAME}", "SETUP")
                return record
            self._new_record_factory = record_factory
        return self._new_record_factory

    @property
    def formatter_cls(self):
        if not self._formatter_cls:
            class Formatter(self.logging.Formatter):
                def format(cls, record):
                    cls._style._fmt = f"{colors_mapping[record.levelno]}{LOG_FORMAT}{colors_mapping['reset']}"
                    return super().format(record)
            self._formatter_cls = Formatter
        return self._formatter_cls

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
            setattr(self.logging.Logger, level_name.lower(), partialmethod(self.logging.Logger.log, getattr(self.logging, level_name)))
            setattr(self.logging, level_name.lower(), partial(self.logging.log, getattr(self.logging, level_name)))
            colors_mapping[getattr(self.logging, level_name)] = log_info["log_color"]
    
    @property
    def stream_handler(self):
        if not self._stream_handler:
            self._stream_handler = self.logging.StreamHandler(sys.stdout)
        return self._stream_handler

    @logger_not_initialised
    def configure_stream_handler(self):
        self.stream_handler.setFormatter(self.formatter_cls())
        self.stream_handler.setLevel(self.logger_level)
        self.addHandler(self.stream_handler)

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
        self.configure_stream_handler()
        
        self._logger_initialised = True

    def fail(self, message):
        self.error(message)
        pytest.fail(f"{Colors.Fg.RED}{message}{Colors.Fg.RESET}")
