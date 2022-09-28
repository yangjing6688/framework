import imp
import sys

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

        self.configure_new_logging_levels()

        self.logger_level = min(*[v for v in colors_mapping if isinstance(v, int)]) 
        self.old_record_factory = logging.getLogRecordFactory()
        logging.setLogRecordFactory(self.new_record_factory)

        self.setLevel(self.logger_level)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(self.formatter_cls())
        stream_handler.setLevel(self.logger_level)
        self.addHandler(stream_handler)

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
            class Formatter(logging.Formatter):
                def format(cls, record):
                    cls._style._fmt = f"{colors_mapping[record.levelno]}{LOG_FORMAT}{colors_mapping['reset']}"
                    return super().format(record)
            self._formatter_cls = Formatter
        return self._formatter_cls

    def configure_new_logging_levels(self):
        for level_name, log_info in new_log_levels.items():
            setattr(self.logging, level_name, log_info["log_level_value"])
            self.logging.addLevelName(getattr(self.logging, level_name), level_name)
            setattr(self.logging.Logger, level_name.lower(), partialmethod(self.logging.Logger.log, getattr(self.logging, level_name)))
            setattr(self.logging, level_name.lower(), partial(self.logging.log, getattr(self.logging, level_name)))
            colors_mapping[getattr(self.logging, level_name)] = log_info["log_color"]
