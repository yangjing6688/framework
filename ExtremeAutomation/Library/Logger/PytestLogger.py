import imp
import sys

from functools import partial, partialmethod

from ExtremeAutomation.Library.Logger.Colors import Colors
from ExtremeAutomation.Library.Utils.Singleton import Singleton


LOG_FORMAT = '[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s:%(lineno)s] [%(test_name)s] %(message)s'
STEP_LOG_LEVEL = 5
CLI_LOG_LEVEL = 6
logging = imp.load_module("logging_module", *imp.find_module("logging"))


class PytestLogger(metaclass=Singleton):
    
    def __init__(self, pytest_config={}):
        
        logging.STEP = STEP_LOG_LEVEL
        logging.CLI = CLI_LOG_LEVEL
        logging.addLevelName(logging.STEP, 'STEP')
        logging.addLevelName(logging.CLI, 'CLI')
        logging.Logger.step = partialmethod(logging.Logger.log, logging.STEP)
        logging.Logger.cli = partialmethod(logging.Logger.log, logging.CLI)
        logging.step = partial(logging.log, logging.STEP)
        logging.cli = partial(logging.log, logging.CLI)
        self.logging = logging
        self.pytest_config = pytest_config

        colors_mapping = {
            "reset": Colors.Fg.RESET,
            logging.STEP: Colors.Fg.CYAN,
            logging.CLI: Colors.Fg.BLUE,
            logging.INFO: Colors.Fg.MAGENTA,
            logging.DEBUG: Colors.Fg.GREEN,
            logging.WARNING: Colors.Fg.YELLOW,
            logging.CRITICAL: Colors.Fg.RED,
            logging.ERROR: Colors.Fg.RED
        }

        old_factory = logging.getLogRecordFactory()

        def record_factory(*args, **kwargs):
            record = old_factory(*args, **kwargs)
            record.test_name = pytest_config.get("${TEST_NAME}", "SETUP")
            return record

        logging.setLogRecordFactory(record_factory)

        class Formatter(logging.Formatter):
            def format(cls, record):
                cls._style._fmt = f"{colors_mapping[record.levelno]}{LOG_FORMAT}{colors_mapping['reset']}"
                return super().format(record)

        logger = logging.getLogger(__name__)
        logger.setLevel(STEP_LOG_LEVEL)

        s_handler = logging.StreamHandler(sys.stdout)
        s_handler.setFormatter(Formatter())
        s_handler.setLevel(STEP_LOG_LEVEL)
        logger.addHandler(s_handler)
        self.logger = logger

