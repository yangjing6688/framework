import mock
from ExtremeAutomation.Keywords.FailureException import FailureException
from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Library.Device.NetworkElement.NetworkElement import NetworkElement
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.fdb.EXOS.base.baseversion.baseunit.\
    FdbCustomShowTools import FdbCustomShowTools
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.vlan.EXOS.base.baseversion.baseunit.\
    VlanCustomShowTools import VlanCustomShowTools


class ExecuteKeywordUnitTest(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        # Create a test device and set the required attributes.
        cls.dev_name = "test_dev"
        cls.dev = NetworkElement(NetworkElementConstants.OS_EXOS,
                                 NetworkElementConstants.PLATFORM_BASE,
                                 NetworkElementConstants.UNIT_BASE,
                                 NetworkElementConstants.VERSION_BASE)
        cls.dev.hostname = "1.1.1.1"
        cls.dev.connection_method = "telnet"
        cls.dev.port = "21"

        # Create an instance of the network element keyword base class.
        # Add the device to the collection and set the api constant.
        cls.net_elem_base = NetworkElementKeywordBaseClass()
        cls.net_elem_base.device_collection.add_device(cls.dev_name, cls.dev)
        cls.net_elem_base.api_const = cls.net_elem_base.constants.API_VLAN

    # +-----------------------+
    # | Execute Keyword Tests |
    # +-----------------------+
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_default(self, mock_login, mock_send):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True

        result = self.net_elem_base.execute_keyword(self.dev_name, {"vlan": "123"}, "set_vlan_create")

        self.assertTrue(result[0].test_result)
        self.assertEqual(result[0].cmd_obj.command, "create vlan 123")

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_override_api_const(self, mock_login, mock_send):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True

        result = self.net_elem_base.execute_keyword(self.dev_name, {"agetime": "123"}, "set_mac_agetime",
                                                    command_api_const="fdb")

        self.assertTrue(result[0].test_result)
        self.assertEqual(result[0].cmd_obj.command, "configure fdb agingtime 123")

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_cli_error(self, mock_login, mock_send):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True

        self.assertRaises(FailureException, self.net_elem_base.execute_keyword,
                          self.dev_name, {"vlan": "123"}, "set_vlan_create")

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_ignore_cli_feedback_true_bool(self, mock_login, mock_send):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True

        result = self.net_elem_base.execute_keyword(self.dev_name, {"vlan": "123"}, "set_vlan_create",
                                                    ignore_cli_feedback=True)

        self.assertTrue(result[0].test_result)

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_ignore_cli_feedback_true_str(self, mock_login, mock_send):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True

        result = self.net_elem_base.execute_keyword(self.dev_name, {"vlan": "123"}, "set_vlan_create",
                                                    ignore_cli_feedback="True")

        self.assertTrue(result[0].test_result)

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_ignore_cli_feedback_false_bool(self, mock_login, mock_send):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True

        self.assertRaises(FailureException, self.net_elem_base.execute_keyword,
                          self.dev_name, {"vlan": "123"}, "set_vlan_create", ignore_cli_feedback=False)

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_ignore_cli_feedback_false_str(self, mock_login, mock_send):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True

        self.assertRaises(FailureException, self.net_elem_base.execute_keyword,
                          self.dev_name, {"vlan": "123"}, "set_vlan_create", ignore_cli_feedback="False")

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_expect_error_true_bool(self, mock_login, mock_send):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True

        result = self.net_elem_base.execute_keyword(self.dev_name, {"vlan": "123"}, "set_vlan_create",
                                                    expect_error=True)

        self.assertTrue(result[0].test_result)

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_expect_error_true_str(self, mock_login, mock_send):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True

        result = self.net_elem_base.execute_keyword(self.dev_name, {"vlan": "123"}, "set_vlan_create",
                                                    expect_error="True")

        self.assertTrue(result[0].test_result)

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_expect_error_false_bool(self, mock_login, mock_send):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True

        self.assertRaises(FailureException, self.net_elem_base.execute_keyword,
                          self.dev_name, {"vlan": "123"}, "set_vlan_create", expect_error=False)

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_expect_error_false_str(self, mock_login, mock_send):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True

        self.assertRaises(FailureException, self.net_elem_base.execute_keyword,
                          self.dev_name, {"vlan": "123"}, "set_vlan_create", expect_error="False")

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_expect_error_true_bool_no_error(self, mock_login, mock_send):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True

        self.assertRaises(FailureException, self.net_elem_base.execute_keyword, self.dev_name, {"vlan": "123"},
                          "set_vlan_create", expect_error=True)

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_expect_error_true_str_no_error(self, mock_login, mock_send):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True

        self.assertRaises(FailureException, self.net_elem_base.execute_keyword, self.dev_name, {"vlan": "123"},
                          "set_vlan_create", expect_error="True")

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_expect_error_false_bool_no_error(self, mock_login, mock_send):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True

        result = self.net_elem_base.execute_keyword(self.dev_name, {"vlan": "123"}, "set_vlan_create",
                                                    expect_error=False)

        self.assertTrue(result[0].test_result)

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_expect_error_false_str_no_error(self, mock_login, mock_send):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True

        result = self.net_elem_base.execute_keyword(self.dev_name, {"vlan": "123"}, "set_vlan_create",
                                                    expect_error="False")

        self.assertTrue(result[0].test_result)

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_keyword_ignore_cli_feedback_and_expect_error(self, mock_login, mock_send):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True

        self.assertRaises(ValueError, self.net_elem_base.execute_keyword, self.dev_name, {"vlan": "123"},
                          "set_vlan_create", ignore_cli_feedback=True, expect_error=True)

    # +------------------------------+
    # | Execute Verify Keyword Tests |
    # +------------------------------+
    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_default_pass_true(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True
        mock_parse.return_value = True

        result = self.net_elem_base.execute_verify_keyword(self.dev_name, {"vlan": "123"}, "set_vlan_create",
                                                           "check_vlan_exists", True, "pass", "fail")

        self.assertTrue(result[0].test_result)
        self.assertEqual(result[0].cmd_obj.command, "create vlan 123")

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_default_pass_false(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True
        mock_parse.return_value = False

        result = self.net_elem_base.execute_verify_keyword(self.dev_name, {"vlan": "123"}, "set_vlan_create",
                                                           "check_vlan_exists", False, "pass", "fail")

        self.assertTrue(result[0].test_result)
        self.assertEqual(result[0].cmd_obj.command, "create vlan 123")

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_default_fail_true(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True
        mock_parse.return_value = False

        self.assertRaises(FailureException, self.net_elem_base.execute_verify_keyword, self.dev_name, {"vlan": "123"},
                          "set_vlan_create", "check_vlan_exists", True, "pass", "fail")

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_default_fail_false(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True
        mock_parse.return_value = True

        self.assertRaises(FailureException, self.net_elem_base.execute_verify_keyword, self.dev_name, {"vlan": "123"},
                          "set_vlan_create", "check_vlan_exists", False, "pass", "fail")

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_override_cmd_const(self, mock_login, mock_send):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True

        result = self.net_elem_base.execute_verify_keyword(self.dev_name, {"agetime": "123"},
                                                           "set_mac_agetime", "check_fdb_agetime", True,
                                                           "pass", "fail", command_api_const="fdb")

        self.assertTrue(result[0].test_result)
        self.assertEqual(result[0].cmd_obj.command, "configure fdb agingtime 123")
        self.assertEqual(result[0].pass_string, "Pass, but only due to the fact that the method is not supported")

    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_override_parse_const(self, mock_login, mock_send):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True

        result = self.net_elem_base.execute_verify_keyword(self.dev_name, {"agetime": "123"}, "set_mac_agetime",
                                                           "check_fdb_agetime", True, "pass", "fail",
                                                           parse_api_const="fdb")

        self.assertTrue(result[0].test_result)
        self.assertTrue(result[0].cmd_obj.not_supported)
        self.assertIsNone(result[0].cmd_obj.command)
        self.assertEqual(result[0].pass_string, "Pass, but only due to the fact that the method is not supported")

    @mock.patch.object(FdbCustomShowTools, "check_fdb_agetime")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_override_both_const(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True
        mock_parse.return_value = True

        result = self.net_elem_base.execute_verify_keyword(self.dev_name, {"agetime": "123"}, "set_mac_agetime",
                                                           "check_fdb_agetime", True, "pass", "fail",
                                                           command_api_const="fdb", parse_api_const="fdb")

        self.assertTrue(result[0].test_result)
        self.assertEqual(result[0].cmd_obj.command, "configure fdb agingtime 123")

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_cli_error_true(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True
        mock_parse.return_value = True

        self.assertRaises(FailureException, self.net_elem_base.execute_verify_keyword, self.dev_name,
                          {"vlan": "123"}, "set_vlan_create", "check_vlan_exists", True, "pass", "fail")

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_ignore_cli_feedback_true_bool(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True
        mock_parse.return_value = True

        result = self.net_elem_base.execute_verify_keyword(self.dev_name, {"vlan": "123"}, "set_vlan_create",
                                                           "check_vlan_exists", True, "pass", "fail",
                                                           ignore_cli_feedback=True)

        self.assertTrue(result[0].test_result)
        self.assertEqual(result[0].cmd_obj.command, "create vlan 123")

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_ignore_cli_feedback_true_str(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True
        mock_parse.return_value = True

        result = self.net_elem_base.execute_verify_keyword(self.dev_name, {"vlan": "123"}, "set_vlan_create",
                                                           "check_vlan_exists", True, "pass", "fail",
                                                           ignore_cli_feedback="True")

        self.assertTrue(result[0].test_result)
        self.assertEqual(result[0].cmd_obj.command, "create vlan 123")

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_ignore_cli_feedback_false_bool(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True
        mock_parse.return_value = True

        self.assertRaises(FailureException, self.net_elem_base.execute_verify_keyword, self.dev_name, {"vlan": "123"},
                          "set_vlan_create", "check_vlan_exists", True, "pass", "fail", ignore_cli_feedback=False)

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_ignore_cli_feedback_false_str(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True
        mock_parse.return_value = True

        self.assertRaises(FailureException, self.net_elem_base.execute_verify_keyword, self.dev_name, {"vlan": "123"},
                          "set_vlan_create", "check_vlan_exists", True, "pass", "fail", ignore_cli_feedback="False")

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_expect_error_true_cmd_true_parse_true(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True
        mock_parse.return_value = True

        self.assertRaises(FailureException, self.net_elem_base.execute_verify_keyword, self.dev_name, {"vlan": "123"},
                          "set_vlan_create", "check_vlan_exists", True, "pass", "fail", expect_error=True)

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_expect_error_true_cmd_true_parse_false(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True
        mock_parse.return_value = False

        result = self.net_elem_base.execute_verify_keyword(self.dev_name, {"vlan": "123"}, "set_vlan_create",
                                                           "check_vlan_exists", True, "pass", "fail",
                                                           expect_error=True)

        self.assertTrue(result[0].test_result)
        self.assertEqual(result[0].cmd_obj.command, "create vlan 123")

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_expect_error_true_cmd_false_parse_true(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True
        mock_parse.return_value = True

        result = self.net_elem_base.execute_verify_keyword(self.dev_name, {"vlan": "123"}, "set_vlan_create",
                                                           "check_vlan_exists", True, "pass", "fail",
                                                           expect_error=True)

        self.assertTrue(result[0].test_result)
        self.assertEqual(result[0].cmd_obj.command, "create vlan 123")

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_expect_error_true_cmd_false_parse_false(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True
        mock_parse.return_value = False

        result = self.net_elem_base.execute_verify_keyword(self.dev_name, {"vlan": "123"}, "set_vlan_create",
                                                           "check_vlan_exists", True, "pass", "fail",
                                                           expect_error=True)

        self.assertTrue(result[0].test_result)
        self.assertEqual(result[0].cmd_obj.command, "create vlan 123")

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_expect_error_false_cmd_true_parse_true(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True
        mock_parse.return_value = True

        result = self.net_elem_base.execute_verify_keyword(self.dev_name, {"vlan": "123"}, "set_vlan_create",
                                                           "check_vlan_exists", True, "pass", "fail",
                                                           expect_error=False)

        self.assertTrue(result[0].test_result)
        self.assertEqual(result[0].cmd_obj.command, "create vlan 123")

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_expect_error_false_cmd_true_parse_false(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True
        mock_parse.return_value = False

        self.assertRaises(FailureException, self.net_elem_base.execute_verify_keyword, self.dev_name, {"vlan": "123"},
                          "set_vlan_create", "check_vlan_exists", True, "pass", "fail", expect_error=False)

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_expect_error_false_cmd_false_parse_true(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True
        mock_parse.return_value = True

        self.assertRaises(FailureException, self.net_elem_base.execute_verify_keyword, self.dev_name, {"vlan": "123"},
                          "set_vlan_create", "check_vlan_exists", True, "pass", "fail", expect_error=False)

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_expect_error_false_cmd_false_parse_false(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = self.set_cli_error
        mock_login.return_value = True
        mock_parse.return_value = False

        self.assertRaises(FailureException, self.net_elem_base.execute_verify_keyword, self.dev_name, {"vlan": "123"},
                          "set_vlan_create", "check_vlan_exists", True, "pass", "fail", expect_error=False)

    @mock.patch.object(VlanCustomShowTools, "check_vlan_exists")
    @mock.patch.object(NetworkElement, "send_command_object")
    @mock.patch.object(NetworkElement, "login")
    def test_execute_verify_keyword_ignore_cli_feedback_and_expect_error(self, mock_login, mock_send, mock_parse):
        mock_send.side_effect = lambda x: x
        mock_login.return_value = True
        mock_parse.return_value = True

        self.assertRaises(ValueError, self.net_elem_base.execute_verify_keyword, self.dev_name, {"vlan": "123"},
                          "set_vlan_create", "check_vlan_exists", True, "pass", "fail", ignore_cli_feedback=True,
                          expect_error=True)

    # +------------------+
    # | Helper Functions |
    # +------------------+
    @staticmethod
    def set_cli_error(cmd_obj):
        cmd_obj.error_state = True
        cmd_obj.error_text = "error"
        return cmd_obj


if __name__ == '__main__':
    RobotUnitTest.main()
