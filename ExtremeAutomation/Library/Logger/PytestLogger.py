import imp
import sys

from functools import partial, partialmethod

from pytest_testconfig import config
from ExtremeAutomation.Library.Logger.Colors import Colors
from ExtremeAutomation.Library.Utils.Singleton import Singleton


LOG_FORMAT = '[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s:%(lineno)s] [%(test_name)s] %(message)s'
STEP_LOG_LEVEL = 5
CLI_LOG_LEVEL = 6

logging = imp.load_module("logging_module", *imp.find_module("logging"))


class PytestLogger(logging.Logger, metaclass=Singleton):
    
    def __init__(self, pytest_config=config):
        
        super().__init__(__name__)
        self.pytest_config = pytest_config
        self.logging = logging
        self.logging.STEP = STEP_LOG_LEVEL
        self.logging.CLI = CLI_LOG_LEVEL
        self.logging.addLevelName(logging.STEP, 'STEP')
        self.logging.addLevelName(logging.CLI, 'CLI')
        self.logging.Logger.step = partialmethod(logging.Logger.log, logging.STEP)
        self.logging.Logger.cli = partialmethod(logging.Logger.log, logging.CLI)
        self.logging.step = partial(logging.log, logging.STEP)
        self.logging.cli = partial(logging.log, logging.CLI)

        self.old_record_factory = logging.getLogRecordFactory()
        logging.setLogRecordFactory(self.new_record_factory)

        self.setLevel(min(STEP_LOG_LEVEL, CLI_LOG_LEVEL))

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(self.formatter_cls())
        stream_handler.setLevel(min(STEP_LOG_LEVEL, CLI_LOG_LEVEL))
        self.addHandler(stream_handler)

    @property
    def colors_mapping(self):
        return {
            "reset": Colors.Fg.RESET,
            logging.STEP: Colors.Fg.CYAN,
            logging.CLI: Colors.Fg.BLUE,
            logging.INFO: Colors.Fg.MAGENTA,
            logging.DEBUG: Colors.Fg.GREEN,
            logging.WARNING: Colors.Fg.YELLOW,
            logging.CRITICAL: Colors.Fg.RED,
            logging.ERROR: Colors.Fg.RED
        }

    @property
    def new_record_factory(self):
        def record_factory(*args, **kwargs):
            record = self.old_record_factory(*args, **kwargs)
            record.test_name = self.pytest_config.get("${TEST_NAME}", "SETUP")
            return record
        return record_factory

    @property
    def formatter_cls(self):
        class Formatter(logging.Formatter):
            def format(cls, record):
                cls._style._fmt = f"{self.colors_mapping[record.levelno]}{LOG_FORMAT}{self.colors_mapping['reset']}"
                return super().format(record)
        return Formatter
