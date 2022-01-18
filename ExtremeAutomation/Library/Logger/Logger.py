import os
import sys
import inspect
import logging
import platform
from logging.handlers import RotatingFileHandler
from ExtremeAutomation.Library.Utils.Singleton import Singleton


class Logger(object, metaclass=Singleton):
    # +------------------+
    # | Logger Constants |
    # +------------------+

    # Logging defined log levels
    CRITICAL = logging.CRITICAL
    ERROR = logging.ERROR
    WARN = logging.WARN
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET

    # Custom log levels.
    NONE = 99
    CLI_SEND = 22
    CLI_READ = 21
    TRACE = 5
    ALL = 1

    # Logger name
    MAIN_LOGGER = "pytest"

    def __init__(self):
        self.trm_guid = None
        self.root_log_path = ""
        self.primary_log_file = "atg.rlog"
        self.cli_send_log_file = "atg_cli_send.rlog"
        self.cli_read_log_file = "atg_cli_read.rlog"
        self.max_log_size = 400000
        self.backup_count = 10
        self.create_log_files = False
        self._console_level = self.DEBUG
        self._file_level = self.INFO
        self.file_filter = FileFilter(self.file_level)
        self.console_filter = LogFilter(self.console_level)
        self.logger = logging.getLogger(self.MAIN_LOGGER)
        self.logger.setLevel(self.INFO)
        self.log_formatter = logging.Formatter("%(levelname)s - %(asctime)s - %(message)s")
        self.__init_logger()
        # self.__check_trm_run()

        self.valid_log_levels = [self.ALL,
                                 self.CRITICAL,
                                 self.ERROR,
                                 self.WARN,
                                 self.CLI_SEND,
                                 self.CLI_READ,
                                 self.INFO,
                                 self.DEBUG,
                                 self.TRACE,
                                 self.NONE]

    @property
    def console_level(self):
        """
        Property function for the private attribute console_level.
        """
        return self._console_level

    @console_level.setter
    def console_level(self, level):
        """
        Setter function for the private attribute console_level. When console level is set
        the console filter level is also set to the passed level.
        """
        if level in self.valid_log_levels:
            self._console_level = level
            self.console_filter.level = level
        else:
            raise ValueError(str(level) + " is not a valid level")

    @property
    def file_level(self):
        """
        Property function for the private attribute log_level.
        """
        return self._file_level

    @file_level.setter
    def file_level(self, level):
        """
        Setter function for the private attribute log_level. When log_level is set the log filter
        level is also set to the passed level.
        """
        if level in self.valid_log_levels:
            self._file_level = level
            self.file_filter.level = level
        else:
            raise ValueError(str(level) + " is not a valid log level")

    def __init_logger(self):
        """
        This function applies the required config to the logger. To start we only need to add
        a handler to send messages to stdout and to configure our custom log levels.
        """
        # Add a handler to send log messages to stdout.
        handler = logging.StreamHandler(sys.__stdout__)
        handler.setFormatter(self.log_formatter)
        handler.addFilter(self.console_filter)
        self.logger.addHandler(handler)

        # Add 3 custom logging levels, CLI_SEND, CLI_READ, and TRACE.
        logging.addLevelName(self.CLI_SEND, "CLI_SEND")
        logging.addLevelName(self.CLI_READ, "CLI_READ")
        logging.addLevelName(self.TRACE, "TRACE")

    def __update_handlers(self, level):
        """
        This function updates the file handlers as needed. By default none of the file handlers are created.
        We only create them when they are used the first time (if create_log_files is enabled). If a new
        file handler is needed we first check to make sure it has not already been added. If it exists do
        nothing otherwise add the new handler.
        """
        if self.create_log_files:
            if level == self.CLI_SEND and "cli_send" not in [i.name for i in self.logger.handlers]:
                self.__add_file_handler("cli_send", self.cli_send_log_file, CliFilter(self.CLI_SEND))
            elif level == self.CLI_READ and "cli_read" not in [i.name for i in self.logger.handlers]:
                self.__add_file_handler("cli_read", self.cli_read_log_file, CliFilter(self.CLI_READ))
            elif "primary" not in [i.name for i in self.logger.handlers]:
                self.__add_file_handler("primary", self.primary_log_file, self.file_filter)

    def __add_file_handler(self, name, log_file, _filter):
        """
        This function creates a handler using the passed log_file. Then is configures
        the formatter for the handler and adds it to the given logger.
        """
        log_file_path = os.path.join(self.root_log_path, log_file)
        handler = RotatingFileHandler(log_file_path, maxBytes=self.max_log_size, backupCount=self.backup_count)
        handler.name = name
        handler.setFormatter(self.log_formatter)
        handler.addFilter(_filter)
        self.logger.addHandler(handler)

    # def __check_trm_run(self):
    #     """
    #     This checks if we are doing a TRM run by trying to grab the testguid from the robot variable dictionary.
    #     If we are unable to grab either the variables dict or the test guid we know that this is not a TRM run.
    #     If it is we set the TRM paths, create TRM dirs, and set create_log_files to True.
    #     """
    #     try:
    #         var_dict = BuiltIn().get_variables(True)
    #         self.trm_guid = var_dict["environment"]["testguid"]
    #         self.__set_trm_paths()
    #         self.__create_trm_folders()
    #         self.create_log_files = True
    #     except (RobotNotRunningError, KeyError):
    #         # This is not a TRM run, nothing special needs to be done.
    #         pass

    # def __set_trm_paths(self):
    #     r"""
    #     This function will set the log paths based on the current OS.

    #     If windows is used the path is C:\TRM_DATA\logs\<guid>\
    #     Otherwise it uses /TRM_DATA/logs/<guid>/
    #     """
    #     if "windows" in platform.platform().lower():
    #         self.root_log_path = os.path.join(r"C:\TRM_DATA", "logs", self.trm_guid)
    #     else:
    #         self.root_log_path = os.path.join("/TRM_DATA", "logs", self.trm_guid)

    # def __create_trm_folders(self):
    #     """
    #     This function checks to the see if the TRM_DATA/logs/ folders exists on the given OS.
    #     If TRM_DATA does not exist it creates it and the logs folder. If only the logs folder
    #     is missing is creates that. Otherwise it creates nothing.
    #     """
    #     # First check if the full root path directory exists, if it doesn't see if the parent
    #     # folder exists.
    #     if not os.path.exists(os.path.dirname(self.root_log_path)):
    #         # Check if the parent folder exists, if it doesn't create it.
    #         parent_dir = os.path.join(os.path.dirname(self.root_log_path), "..")
    #         if not os.path.exists(parent_dir):
    #             self.__make_dir(parent_dir)

    #         # Create the root log path after checking if the parent directory exists.
    #         self.__make_dir(self.root_log_path)

    @staticmethod
    def __make_dir(path):
        """
        This function creates a directory with the given path on either Windows or Linux.
        """
        if "windows" in platform.platform().lower():
            os.makedirs(path)
        else:
            os.system("sudo mkdir " + path)
            os.system("sudo chmod 777 " + path)

    def log_message(self, msg, level):
        """
        This function accepts a message to log and level to log the message at.

        This function will call the update_handlers function which creates the file
        handlers as needed.

        If the level is not known a ValueError will be raised.
        """
        if not isinstance(msg, str):
            msg = str(msg)

        if level in [self.INFO,
                     self.WARN,
                     self.ERROR,
                     self.DEBUG,
                     self.TRACE,
                     self.CRITICAL,
                     self.CLI_SEND,
                     self.CLI_READ]:
            self.__update_handlers(level)
            print(self.format_message(msg))
            # self.logger.log(level, self.format_message(msg))
        else:
            raise ValueError("Unknown log type.")

    def log_cli_send(self, msg):
        """
        Logs the given msg at CLI send level.
        """
        self.log_message(msg, self.CLI_SEND)

    def log_cli_read(self, msg):
        """
        Logs the given msg at CLI read level.
        """
        self.log_message(msg, self.CLI_READ)

    def log_info(self, msg):
        """
        Logs the given msg at the info level.
        """
        self.log_message(msg, self.INFO)

    def log_warn(self, msg):
        """
        Logs the given msg at the warning level.
        """
        self.log_message(msg, self.WARN)

    def log_error(self, msg):
        """
        Logs the given msg at the error level.
        """
        self.log_message(msg, self.ERROR)

    def log_debug(self, msg):
        """
        Logs the given msg at the debug level.
        """
        self.log_message(msg, self.DEBUG)

    def log_trace(self, msg):
        """
        Logs the given msg at the trace level.
        """
        self.log_message(msg, self.TRACE)

    def log_critical(self, msg):
        """
        Logs the given msg at critical level.
        """
        self.log_message(msg, self.CRITICAL)

    def log_unimplemented_method(self):
        """
        Logs an unimplemented method
        """
        self.log_unsupported("method not implemented")
    
    def log_unsupported(self, msg):
        """
        Logs a method as unsupported.
        """
        curframe = inspect.stack()
        formatted_lines = []
        b_started_logging = False
        for s in curframe:
            path_name = str(s[1]).lower()
            current_frame = s[0]
            args, _, _, values = inspect.getargvalues(current_frame)
            if not b_started_logging and "logger" in path_name:
                b_started_logging = True
            # stop when you get to the unittest or jetbrain calls. Probably needs something for robot keywords
            elif b_started_logging and ("\\unittest\\" in path_name or "jetbrain" in path_name):
                break
            # don't log until back out of the logger and managedobject call
            elif b_started_logging and "logger" not in path_name and "managedobject" not in path_name:
                temp_values = {}
                for (key, val) in values.items():
                    # look for arg = self
                    if "object at" in str(val):
                        temp_values[key] = key
                str_args = ', '.join("%s" % val for (key, val) in temp_values.items() if key != "self")
                formatted_lines.append(str(s[3]) + "(" + str_args + ") @ line " + str(s[2]) + " in file " +
                                       str(s[1]) + " ")
        index = 1
        ret_string = ""
        for line in formatted_lines:
            ret_string += str(msg).upper() + " stack[" + str(index) + "]::" + str(line) + "\n"
            index += 1
            self.log_debug(ret_string)

    def get_level_string(self, level):
        """
        This function is used to get the string representation of a given log level.
        """
        levels = {self.CRITICAL: "CRITICAL",
                  self.ERROR: "ERROR",
                  self.WARN: "WARNING",
                  self.INFO: "INFO",
                  self.CLI_SEND: "CLI_SEND",
                  self.CLI_READ: "CLI_READ",
                  self.DEBUG: "DEBUG",
                  self.TRACE: "TRACE",
                  self.ALL: "ALL",
                  self.NOTSET: "NOTSET",
                  self.NONE: "NONE"}

        if level in levels:
            return levels[level]
        raise ValueError(str(level) + " is not a valid log level")

    @staticmethod
    def format_message(msg):
        """
        This function checks to see if the first character in the message is a new line. If it
        is indent the message. This makes reading multi-line messages easier.
        """
        if msg.startswith("\n"):
            msg = msg.replace("\n", "\n    ")
        return msg


class LogFilter(logging.Filter):
    def __init__(self, level):
        super(LogFilter, self).__init__()
        self.level = level

    def filter(self, record):  # noqa: A003
        """
        This filter is used by the console logger. It checks to make sure the level is at or above the
        currently configured level.
        """
        return record.levelno >= self.level


class FileFilter(LogFilter):
    def filter(self, record):  # noqa: A003
        """
        This filter is used by the rotating file handler. It filters out any CLI_READ/CLI_SEND messages
        as they are already logged to the CLI_SEND/READ log files. It also filters out messages
        that are below it's currently configured log level by calling it's parent class's filter method.
        """
        if record.levelno not in [Logger.CLI_SEND, Logger.CLI_READ]:
            return super(FileFilter, self).filter(record)
        return False


class CliFilter(LogFilter):
    def filter(self, record):  # noqa: A003
        """
        This is the filter used by CLI_SEND and CLI_READ. It filters out all messages that are not
        the configured level.
        """
        return record.levelno == self.level
    
    
