import io
import os
import re
import mock
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest


class LoggerUnitTest(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.log = Logger()
        cls.msg = "test message"

    @classmethod
    def tearDownClass(cls):
        cls.__remove_log_files()

    def setUp(self):
        self.__reset_logger()

    # +-------------------+
    # | misc logger tests |
    # +-------------------+
    def test_logger_singleton(self):
        l1 = Logger()
        l2 = Logger()

        self.assertEqual(l1, l2)

    def test_set_console_level(self):
        for level in self.log.valid_log_levels:
            self.log.console_level = level
            self.assertEqual(self.log.console_level, level)
            self.assertEqual(self.log.console_filter.level, level)

        with self.assertRaises(ValueError):
            self.log.console_level = -1

        with self.assertRaises(ValueError):
            self.log.console_level = 65535

        with self.assertRaises(ValueError):
            self.log.console_level = "a"

    def test_set_file_level(self):
        for level in self.log.valid_log_levels:
            self.log.file_level = level
            self.assertEqual(self.log.file_level, level)
            self.assertEqual(self.log.file_filter.level, level)

        with self.assertRaises(ValueError):
            self.log.file_level = -1

        with self.assertRaises(ValueError):
            self.log.file_level = 65535

        with self.assertRaises(ValueError):
            self.log.file_level = "a"

    def test_update_handlers(self):
        self.log.create_log_files = True
        self.log._Logger__update_handlers(self.log.CLI_SEND)
        self.assertEqual(len(self.log.logger.handlers), 2)
        self.assertEqual(self.log.logger.handlers[1].name, "cli_send")

        self.log._Logger__update_handlers(self.log.CLI_READ)
        self.assertEqual(len(self.log.logger.handlers), 3)
        self.assertEqual(self.log.logger.handlers[2].name, "cli_read")

        self.log._Logger__update_handlers(self.log.INFO)
        self.assertEqual(len(self.log.logger.handlers), 4)
        self.assertEqual(self.log.logger.handlers[3].name, "primary")

        self.log._Logger__update_handlers(self.log.DEBUG)
        self.assertEqual(len(self.log.logger.handlers), 4)

        self.log._Logger__update_handlers(65535)
        self.assertEqual(len(self.log.logger.handlers), 4)

    def test_check_trm_run_non_trm(self):
        log_root = self.log.root_log_path

        self.log._Logger__check_trm_run()

        self.assertEqual(self.log.root_log_path, log_root)
        self.assertIsNone(self.log.trm_guid)
        self.assertFalse(self.log.create_log_files)

    @mock.patch("ExtremeAutomation.Library.Logger.Logger.platform.platform")
    @mock.patch("ExtremeAutomation.Library.Logger.Logger.os.path.exists")
    @mock.patch("ExtremeAutomation.Library.Logger.Logger.BuiltIn.get_variables")
    def test_check_trm_run_folder_exists_windows(self, mock_robot, mock_os, mock_platform):
        mock_robot.return_value = {"environment": {"testguid": "guid1"}}
        mock_os.return_value = True
        mock_platform.return_value = "windows"

        self.log._Logger__check_trm_run()

        self.assertEqual(self.log.trm_guid, "guid1")
        self.assertEqual(self.log.root_log_path, os.path.join(r"C:\TRM_DATA", "logs", "guid1"))
        self.assertTrue(self.log.create_log_files)

    @mock.patch("ExtremeAutomation.Library.Logger.Logger.platform.platform")
    @mock.patch("ExtremeAutomation.Library.Logger.Logger.os.path.exists")
    @mock.patch("ExtremeAutomation.Library.Logger.Logger.BuiltIn.get_variables")
    def test_check_trm_run_folder_exists_linux(self, mock_robot, mock_os, mock_platform):
        mock_robot.return_value = {"environment": {"testguid": "guid2"}}
        mock_os.return_value = True
        mock_platform.return_value = "linux"

        self.log._Logger__check_trm_run()

        self.assertEqual(self.log.trm_guid, "guid2")
        self.assertEqual(self.log.root_log_path, os.path.join(r"/TRM_DATA", "logs", "guid2"))
        self.assertTrue(self.log.create_log_files)

    @mock.patch("ExtremeAutomation.Library.Logger.Logger.platform.platform")
    @mock.patch("ExtremeAutomation.Library.Logger.Logger.os.makedirs")
    @mock.patch("ExtremeAutomation.Library.Logger.Logger.os.path.exists")
    @mock.patch("ExtremeAutomation.Library.Logger.Logger.BuiltIn.get_variables")
    def test_check_trm_run_folder_not_exists_windows(self, mock_robot, mock_os, mock_make_dir, mock_platform):
        mock_robot.return_value = {"environment": {"testguid": "guid3"}}
        mock_os.return_value = False
        mock_platform.return_value = "windows"

        self.log._Logger__check_trm_run()

        self.assertEqual(self.log.trm_guid, "guid3")
        self.assertEqual(self.log.root_log_path, os.path.join(r"C:\TRM_DATA", "logs", "guid3"))
        self.assertTrue(self.log.create_log_files)
        mock_make_dir.assert_called()

    @mock.patch("ExtremeAutomation.Library.Logger.Logger.platform.platform")
    @mock.patch("ExtremeAutomation.Library.Logger.Logger.os.system")
    @mock.patch("ExtremeAutomation.Library.Logger.Logger.os.path.exists")
    @mock.patch("ExtremeAutomation.Library.Logger.Logger.BuiltIn.get_variables")
    def test_check_trm_run_folder_not_exists_linux(self, mock_robot, mock_os, mock_system, mock_platform):
        mock_robot.return_value = {"environment": {"testguid": "guid4"}}
        mock_os.return_value = False
        mock_platform.return_value = "linux"

        self.log._Logger__check_trm_run()

        self.assertEqual(self.log.trm_guid, "guid4")
        self.assertEqual(self.log.root_log_path, os.path.join(r"/TRM_DATA", "logs", "guid4"))
        self.assertTrue(self.log.create_log_files)
        mock_system.assert_called()

    def test_get_level_string(self):
        self.assertEqual(self.log.get_level_string(self.log.CRITICAL), "CRITICAL")
        self.assertEqual(self.log.get_level_string(self.log.ERROR), "ERROR")
        self.assertEqual(self.log.get_level_string(self.log.WARN), "WARNING")
        self.assertEqual(self.log.get_level_string(self.log.INFO), "INFO")
        self.assertEqual(self.log.get_level_string(self.log.CLI_SEND), "CLI_SEND")
        self.assertEqual(self.log.get_level_string(self.log.CLI_READ), "CLI_READ")
        self.assertEqual(self.log.get_level_string(self.log.DEBUG), "DEBUG")
        self.assertEqual(self.log.get_level_string(self.log.TRACE), "TRACE")
        self.assertEqual(self.log.get_level_string(self.log.ALL), "ALL")
        self.assertEqual(self.log.get_level_string(self.log.NONE), "NONE")

        with self.assertRaises(ValueError):
            self.log.get_level_string(65535)

        with self.assertRaises(ValueError):
            self.log.get_level_string(-1)

        with self.assertRaises(ValueError):
            self.log.get_level_string("a")

    def test_log_file_creation(self):
        self.assertFalse(os.path.exists(self.__get_log_path(self.log.primary_log_file)))
        self.assertFalse(os.path.exists(self.__get_log_path(self.log.cli_send_log_file)))
        self.assertFalse(os.path.exists(self.__get_log_path(self.log.cli_read_log_file)))

        self.log.create_log_files = True
        self.log.file_level = self.log.ALL

        self.log.log_info(self.msg)

        self.assertTrue(os.path.exists(self.__get_log_path(self.log.primary_log_file)))
        self.assertFalse(os.path.exists(self.__get_log_path(self.log.cli_send_log_file)))
        self.assertFalse(os.path.exists(self.__get_log_path(self.log.cli_read_log_file)))

        self.log.log_cli_send(self.msg)

        self.assertTrue(os.path.exists(self.__get_log_path(self.log.primary_log_file)))
        self.assertTrue(os.path.exists(self.__get_log_path(self.log.cli_send_log_file)))
        self.assertFalse(os.path.exists(self.__get_log_path(self.log.cli_read_log_file)))

        self.log.log_cli_read(self.msg)

        self.assertTrue(os.path.exists(self.__get_log_path(self.log.primary_log_file)))
        self.assertTrue(os.path.exists(self.__get_log_path(self.log.cli_send_log_file)))
        self.assertTrue(os.path.exists(self.__get_log_path(self.log.cli_read_log_file)))

    # +----------------------------+
    # | log_message, no file tests |
    # +----------------------------+
    def test_log_message_critical(self):
        self.log.log_message(self.msg, self.log.CRITICAL)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.CRITICAL)))

    def test_log_message_error(self):
        self.log.log_message(self.msg, self.log.ERROR)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.ERROR)))

    def test_log_message_warn(self):
        self.log.log_message(self.msg, self.log.WARN)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.WARN)))

    def test_log_message_cli_send(self):
        self.log.log_message(self.msg, self.log.CLI_SEND)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.CLI_SEND)))

    def test_log_message_cli_read(self):
        self.log.log_message(self.msg, self.log.CLI_READ)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.CLI_READ)))

    def test_log_message_info(self):
        self.log.log_message(self.msg, self.log.INFO)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.INFO)))

    def test_log_message_debug(self):
        self.log.log_message(self.msg, self.log.DEBUG)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.DEBUG)))

    def test_log_message_trace(self):
        self.log.log_message(self.msg, self.log.TRACE)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.TRACE)))

    # +------------------------------+
    # | log_message, with file tests |
    # +------------------------------+
    def test_log_message_with_file_critical(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_message(self.msg, self.log.CRITICAL)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.CRITICAL))

    def test_log_message_with_file_error(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_message(self.msg, self.log.ERROR)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.ERROR))

    def test_log_message_with_file_warn(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_message(self.msg, self.log.WARN)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.WARN))

    def test_log_message_with_file_cli_send(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_message(self.msg, self.log.CLI_SEND)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.CLI_SEND))

    def test_log_message_with_file_cli_read(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_message(self.msg, self.log.CLI_READ)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.CLI_READ))

    def test_log_message_with_file_info(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_message(self.msg, self.log.INFO)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.INFO))

    def test_log_message_with_file_debug(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_message(self.msg, self.log.DEBUG)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.DEBUG))

    def test_log_message_with_file_trace(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_message(self.msg, self.log.TRACE)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.TRACE))

    # +----------------------------+
    # | log_<level>, no file tests |
    # +----------------------------+
    def test_log_critical(self):
        self.log.log_critical(self.msg)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.CRITICAL)))

    def test_log_error(self):
        self.log.log_error(self.msg)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.ERROR)))

    def test_log_warn(self):
        self.log.log_warn(self.msg)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.WARN)))

    def test_log_cli_send(self):
        self.log.log_cli_send(self.msg)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.CLI_SEND)))

    def test_log_cli_read(self):
        self.log.log_cli_read(self.msg)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.CLI_READ)))

    def test_log_info(self):
        self.log.log_info(self.msg)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.INFO)))

    def test_log_debug(self):
        self.log.log_debug(self.msg)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.DEBUG)))

    def test_log_trace(self):
        self.log.log_trace(self.msg)
        self.assertTrue(self.__verify_msg(self.s.getvalue(), self.msg, self.log.get_level_string(self.log.TRACE)))

    # +------------------------------+
    # | log_message, with file tests |
    # +------------------------------+
    def test_log_critical_with_file(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_critical(self.msg)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.CRITICAL))

    def test_log_error_with_file(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_error(self.msg)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.ERROR))

    def test_log_warn_with_file(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_warn(self.msg)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.WARN))

    def test_log_cli_send_with_file(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_cli_send(self.msg)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.CLI_SEND))

    def test_log_cli_read_with_file(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_cli_read(self.msg)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.CLI_READ))

    def test_log_info_with_file(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_info(self.msg)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.INFO))

    def test_log_debug_with_file(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_debug(self.msg)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.DEBUG))

    def test_log_trace_with_file(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.log_trace(self.msg)
        self.assertTrue(self.__verify_file_msg(self.msg, self.log.TRACE))

    # +----------------------------+
    # | console level filter tests |
    # +----------------------------+
    def test_console_level_all(self):
        self.log.console_level = self.log.ALL
        self.__log_at_each_level(self.msg)

        return_val = [i for i in self.s.getvalue().split("\n") if i != ""]
        self.assertEqual(len(return_val), 8)

    def test_console_level_trace(self):
        self.log.console_level = self.log.TRACE
        self.__log_at_each_level(self.msg)

        return_val = [i for i in self.s.getvalue().split("\n") if i != ""]
        self.assertEqual(len(return_val), 8)

    def test_console_level_debug(self):
        self.log.console_level = self.log.DEBUG
        self.__log_at_each_level(self.msg)

        output = self.s.getvalue()
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 7)

    def test_console_level_info(self):
        self.log.console_level = self.log.INFO
        self.__log_at_each_level(self.msg)

        output = self.s.getvalue()
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE", "DEBUG"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 6)

    def test_console_level_cli_read(self):
        self.log.console_level = self.log.CLI_READ
        self.__log_at_each_level(self.msg)

        output = self.s.getvalue()
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE", "DEBUG", "INFO"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 5)

    def test_console_level_cli_send(self):
        self.log.console_level = self.log.CLI_SEND
        self.__log_at_each_level(self.msg)

        output = self.s.getvalue()
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE", "DEBUG", "INFO", "CLI_READ"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 4)

    def test_console_level_warn(self):
        self.log.console_level = self.log.WARN
        self.__log_at_each_level(self.msg)

        output = self.s.getvalue()
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE", "DEBUG", "INFO", "CLI_READ", "CLI_SEND"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 3)

    def test_console_level_error(self):
        self.log.console_level = self.log.ERROR
        self.__log_at_each_level(self.msg)

        output = self.s.getvalue()
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE", "DEBUG", "INFO", "CLI_READ", "CLI_SEND", "WARN"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 2)

    def test_console_level_critical(self):
        self.log.console_level = self.log.CRITICAL
        self.__log_at_each_level(self.msg)

        output = self.s.getvalue()
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE", "DEBUG", "INFO", "CLI_READ", "CLI_SEND", "WARN", "ERROR"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 1)

    def test_console_level_none(self):
        self.log.console_level = self.log.NONE
        self.__log_at_each_level(self.msg)

        output = self.s.getvalue()
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE", "DEBUG", "INFO", "CLI_READ", "CLI_SEND", "WARN", "ERROR", "CRITICAL"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 0)

    # +-----------------------------+
    # | log file level filter tests |
    # +-----------------------------+
    def test_file_log_level_all(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.file_level = self.log.ALL
        self.__log_at_each_level(self.msg)

        return_val = [i for i in self.__get_file_data(self.log.ALL).split("\n") if i != ""]
        self.assertEqual(len(return_val), 6)

    def test_file_log_level_trace(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.file_level = self.log.TRACE
        self.__log_at_each_level(self.msg)

        return_val = [i for i in self.__get_file_data(self.log.TRACE).split("\n") if i != ""]
        self.assertEqual(len(return_val), 6)

    def test_file_log_level_debug(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.file_level = self.log.DEBUG
        self.__log_at_each_level(self.msg)

        output = self.__get_file_data(self.log.DEBUG)
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 5)

    def test_file_log_level_info(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.file_level = self.log.INFO
        self.__log_at_each_level(self.msg)

        output = self.__get_file_data(self.log.INFO)
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE", "DEBUG"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 4)

    def test_file_log_level_cli_send(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.file_level = self.log.INFO
        self.__log_at_each_level(self.msg)

        output = self.__get_file_data(self.log.CLI_SEND)
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE", "DEBUG"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 1)

    def test_file_log_level_cli_read(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.file_level = self.log.CLI_READ
        self.__log_at_each_level(self.msg)

        output = self.__get_file_data(self.log.CLI_READ)
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE", "DEBUG", "INFO"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 1)

    def test_file_log_level_warn(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.file_level = self.log.WARN
        self.__log_at_each_level(self.msg)

        output = self.__get_file_data(self.log.WARN)
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE", "DEBUG", "INFO", "CLI_READ", "CLI_SEND"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 3)

    def test_file_log_level_error(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.file_level = self.log.ERROR
        self.__log_at_each_level(self.msg)

        output = self.__get_file_data(self.log.ERROR)
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE", "DEBUG", "INFO", "CLI_READ", "CLI_SEND", "WARN"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 2)

    def test_file_log_level_critical(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.file_level = self.log.CRITICAL
        self.__log_at_each_level(self.msg)

        output = self.__get_file_data(self.log.CRITICAL)
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE", "DEBUG", "INFO", "CLI_READ", "CLI_SEND", "WARN", "ERROR"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 1)

    def test_file_log_level_none(self):
        self.log.create_log_files = True
        self.log.console_level = self.log.NONE
        self.log.file_level = self.log.NONE
        self.__log_at_each_level(self.msg)

        output = self.__get_file_data(self.log.NONE)
        return_val = [i for i in output.split("\n") if i != ""]
        filtered_list = ["TRACE", "DEBUG", "INFO", "CLI_READ", "CLI_SEND", "WARN", "ERROR", "CRITICAL"]

        self.assertFalse(any(i in output for i in filtered_list))
        self.assertEqual(len(return_val), 0)

    # +-------------------------+
    # | non test helper methods |
    # +-------------------------+
    def __reset_logger(self):
        """
        Because the logger is a singleton it's attributes don't get reset on re-creation. This
        function resets it's attributes to their default state.
        """
        while len(self.log.logger.handlers) > 1:
            self.log.logger.handlers[-1].close()
            self.log.logger.handlers.pop()

        self.log.create_log_files = False
        self.log.file_level = self.log.ALL
        self.log.console_level = self.log.ALL
        self.s = io.StringIO()
        self.log.logger.handlers[0].stream = self.s
        self.log.root_log_path = ""
        self.log.trm_guid = None
        self.__remove_log_files()

    def __get_file_data(self, level):
        """
        This function opens one of the log files depending on the passed level. It then reads and returns all
        data found within.
        """
        if level == self.log.CLI_SEND:
            with open(self.__get_log_path(self.log.cli_send_log_file)) as log_file:
                return log_file.read()
        elif level == self.log.CLI_READ:
            with open(self.__get_log_path(self.log.cli_read_log_file)) as log_file:
                return log_file.read()
        else:
            with open(self.__get_log_path(self.log.primary_log_file)) as log_file:
                return log_file.read()

    @staticmethod
    def __verify_msg(full_msg, msg, level):
        """
        This function verifies that a given log message follows the required format.
        """
        msg_re = "^" + level + r"\s-\s\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{3}\s-\s" + msg + "$"
        if re.search(msg_re, full_msg):
            return True
        return False

    def __verify_file_msg(self, msg, level):
        """
        This function gets data from a log file and verifies the message inside follows the required format.
        """
        file_data = self.__get_file_data(level)
        return self.__verify_msg(file_data, msg, self.log.get_level_string(level))

    def __log_at_each_level(self, msg):
        """
        This writes a log message at each level.
        """
        self.log.log_critical(msg)
        self.log.log_error(msg)
        self.log.log_warn(msg)
        self.log.log_cli_send(msg)
        self.log.log_cli_read(msg)
        self.log.log_info(msg)
        self.log.log_debug(msg)
        self.log.log_trace(msg)

    def __get_log_path(self, log_file):
        """
        This creates the full path for a given log file. Using the log file and the root
        path configured in the logger object.
        """
        return os.path.join(self.log.root_log_path, log_file)

    @staticmethod
    def __remove_log_files():
        """
        This function removes all existing log files.
        """
        # Close all the file handlers.
        if len(Logger().logger.handlers) == 4:
            Logger().logger.handlers[1].close()
            Logger().logger.handlers[2].close()
            Logger().logger.handlers[3].close()

        if os.path.exists(Logger().primary_log_file):
            os.remove(Logger().primary_log_file)
        if os.path.exists(Logger().cli_send_log_file):
            os.remove(Logger().cli_send_log_file)
        if os.path.exists(Logger().cli_read_log_file):
            os.remove(Logger().cli_read_log_file)


if __name__ == '__main__':
    RobotUnitTest.main()
