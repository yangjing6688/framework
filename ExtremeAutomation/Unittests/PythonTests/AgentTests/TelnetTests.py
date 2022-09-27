import re
import mock
from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent import TelnetAgent
from ExtremeAutomation.Library.Device.Common.CommandObjects.CliCommandObject import CliCommandObject
from ExtremeAutomation.Library.Device.Common.PromptHandler.BasePromptHandler import BasePromptHandler


class TelnetTests(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.create_dummy_devices()

    # +-------------+
    # | Login Tests |
    # +-------------+
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_login_boss(self, mock_telnet, mock_read):
        telnet = self.__test_setup(self.boss_dev)
        mock_read.return_value = "1"
        return_val = telnet.login()
        mock_telnet.assert_called_with()
        telnet.main_session.open.assert_called_with(self.boss_dev.hostname, 23, timeout=5)
        self.assertTrue(return_val)

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_login_eos(self, mock_telnet, mock_read):
        telnet = self.__test_setup(self.eos_dev)
        mock_read.return_value = "1"
        return_val = telnet.login()
        mock_telnet.assert_called_with()
        telnet.main_session.open.assert_called_with(self.eos_dev.hostname, 23, timeout=5)
        self.assertTrue(return_val)

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_login_exos(self, mock_telnet, mock_read):
        telnet = self.__test_setup(self.exos_dev)
        mock_read.return_value = "1"
        return_val = telnet.login()
        mock_telnet.assert_called_with()
        telnet.main_session.open.assert_called_with(self.exos_dev.hostname, 23, timeout=5)
        self.assertTrue(return_val)

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_login_ecos(self, mock_telnet, mock_read):
        telnet = self.__test_setup(self.ecos_dev)
        mock_read.return_value = "1"
        return_val = telnet.login()
        mock_telnet.assert_called_with()
        telnet.main_session.open.assert_called_with(self.ecos_dev.hostname, 23, timeout=5)
        self.assertTrue(return_val)

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(TelnetAgent, "read_until_list_match")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_login_linux(self, mock_telnet, mock_read_list, mock_read):
        telnet = self.__test_setup(self.linux_dev)
        mock_read.return_value = "1"
        mock_read_list.return_value = "1"
        return_val = telnet.login()
        mock_telnet.assert_called_with()
        telnet.main_session.open.assert_called_with(self.linux_dev.hostname, 23, timeout=5)
        self.assertTrue(return_val)

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_login_extr_wireless(self, mock_telnet, mock_read):
        telnet = self.__test_setup(self.extr_wireless_dev)
        mock_read.return_value = "1"
        return_val = telnet.login()
        mock_telnet.assert_called_with()
        telnet.main_session.open.assert_called_with(self.extr_wireless_dev.hostname, 23, timeout=5)
        self.assertTrue(return_val)

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_login_zebra_wireless(self, mock_telnet, mock_read):
        telnet = self.__test_setup(self.zebra_wireless_dev)
        mock_read.return_value = "1"
        return_val = telnet.login()
        mock_telnet.assert_called_with()
        telnet.main_session.open.assert_called_with(self.zebra_wireless_dev.hostname, 23, timeout=5)
        self.assertTrue(return_val)

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(TelnetAgent, "read_until_list_match")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_login_snap_route(self, mock_telnet, mock_read_list, mock_read):
        telnet = self.__test_setup(self.snap_route_dev)
        mock_read.return_value = "1"
        mock_read_list.return_value = "1"
        return_val = telnet.login()
        mock_telnet.assert_called_with()
        telnet.main_session.open.assert_called_with(self.snap_route_dev.hostname, 23, timeout=5)
        self.assertTrue(return_val)

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_login_voss(self, mock_telnet, mock_read):
        telnet = self.__test_setup(self.voss_dev)
        mock_read.return_value = "1"
        return_val = telnet.login()
        mock_telnet.assert_called_with()
        telnet.main_session.open.assert_called_with(self.voss_dev.hostname, 23, timeout=5)
        self.assertTrue(return_val)

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_login_jets(self, mock_telnet, mock_read):
        telnet = self.__test_setup(self.jets_dev)
        mock_read.return_value = "1"
        return_val = telnet.login()
        mock_telnet.assert_called_with()
        telnet.main_session.open.assert_called_with(self.jets_dev.hostname, 23, timeout=5)
        self.assertTrue(return_val)

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_login_alpha(self, mock_telnet, mock_read):
        telnet = self.__test_setup(self.alpha_dev)
        mock_read.return_value = "1"
        return_val = telnet.login()
        mock_telnet.assert_called_with()
        telnet.main_session.open.assert_called_with(self.alpha_dev.hostname, 23, timeout=5)
        self.assertTrue(return_val)

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_login_eos_stacks(self, mock_telnet, mock_read):
        telnet = self.__test_setup(self.eos_stacks_dev)
        mock_read.return_value = "1"
        return_val = telnet.login()
        mock_telnet.assert_called_with()
        telnet.main_session.open.assert_called_with(self.eos_stacks_dev.hostname, 23, timeout=5)
        self.assertTrue(return_val)

    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_login_slx(self, mock_telnet, mock_read):
        telnet = self.__test_setup(self.slx_dev)
        mock_read.return_value = "1"
        return_val = telnet.login()
        mock_telnet.assert_called_with()
        telnet.main_session.open.assert_called_with(self.slx_dev.hostname, 23, timeout=5)
        self.assertTrue(return_val)

    # +--------------+
    # | Logout Tests |
    # +--------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_logout_boss(self, mock_telnet):
        telnet = self.__test_setup(self.boss_dev)
        telnet.main_session = mock_telnet
        return_val = telnet.logout()
        telnet.main_session.close.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(telnet.connected)
        self.assertFalse(telnet.logged_in)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_logout_eos(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.main_session = mock_telnet
        return_val = telnet.logout()
        telnet.main_session.close.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(telnet.connected)
        self.assertFalse(telnet.logged_in)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_logout_exos(self, mock_telnet):
        telnet = self.__test_setup(self.exos_dev)
        telnet.main_session = mock_telnet
        return_val = telnet.logout()
        telnet.main_session.close.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(telnet.connected)
        self.assertFalse(telnet.logged_in)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_logout_ecos(self, mock_telnet):
        telnet = self.__test_setup(self.ecos_dev)
        telnet.main_session = mock_telnet
        return_val = telnet.logout()
        telnet.main_session.close.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(telnet.connected)
        self.assertFalse(telnet.logged_in)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_logout_linux(self, mock_telnet):
        telnet = self.__test_setup(self.linux_dev)
        telnet.main_session = mock_telnet
        return_val = telnet.logout()
        telnet.main_session.close.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(telnet.connected)
        self.assertFalse(telnet.logged_in)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_logout_extr_wireless(self, mock_telnet):
        telnet = self.__test_setup(self.extr_wireless_dev)
        telnet.main_session = mock_telnet
        return_val = telnet.logout()
        telnet.main_session.close.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(telnet.connected)
        self.assertFalse(telnet.logged_in)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_logout_zebra_wireless(self, mock_telnet):
        telnet = self.__test_setup(self.zebra_wireless_dev)
        telnet.main_session = mock_telnet
        return_val = telnet.logout()
        telnet.main_session.close.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(telnet.connected)
        self.assertFalse(telnet.logged_in)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_logout_snap_route(self, mock_telnet):
        telnet = self.__test_setup(self.snap_route_dev)
        telnet.main_session = mock_telnet
        return_val = telnet.logout()
        telnet.main_session.close.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(telnet.connected)
        self.assertFalse(telnet.logged_in)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_logout_voss(self, mock_telnet):
        telnet = self.__test_setup(self.voss_dev)
        telnet.main_session = mock_telnet
        return_val = telnet.logout()
        telnet.main_session.close.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(telnet.connected)
        self.assertFalse(telnet.logged_in)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_logout_jets(self, mock_telnet):
        telnet = self.__test_setup(self.jets_dev)
        telnet.main_session = mock_telnet
        return_val = telnet.logout()
        telnet.main_session.close.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(telnet.connected)
        self.assertFalse(telnet.logged_in)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_logout_alpha(self, mock_telnet):
        telnet = self.__test_setup(self.alpha_dev)
        telnet.main_session = mock_telnet
        return_val = telnet.logout()
        telnet.main_session.close.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(telnet.connected)
        self.assertFalse(telnet.logged_in)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_logout_eos_stacks(self, mock_telnet):
        telnet = self.__test_setup(self.eos_stacks_dev)
        telnet.main_session = mock_telnet
        return_val = telnet.logout()
        telnet.main_session.close.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(telnet.connected)
        self.assertFalse(telnet.logged_in)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_logout_slx(self, mock_telnet):
        telnet = self.__test_setup(self.slx_dev)
        telnet.main_session = mock_telnet
        return_val = telnet.logout()
        telnet.main_session.close.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(telnet.connected)
        self.assertFalse(telnet.logged_in)

    # +-------------+
    # | Write Tests |
    # +-------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_write_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        return_val = telnet.write("test")
        telnet.main_session.write.assert_called_with(b"test")
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_write_not_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = False
        telnet.main_session = mock_telnet
        return_val = telnet.write("test")
        telnet.main_session.write.assert_not_called()
        self.assertIsNone(return_val)

    # +--------------------+
    # | Write Encode Tests |
    # +--------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_write_encode_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        return_val = telnet.write_encode("test")
        telnet.main_session.write.assert_called_with(telnet.cmd_encode("test").encode("ascii"))
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_write_encode_not_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = False
        telnet.main_session = mock_telnet
        return_val = telnet.write_encode("test")
        telnet.main_session.write.assert_not_called()
        self.assertIsNone(return_val)

    # +-----------------------+
    # | Write Encode Ln Tests |
    # +-----------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_write_encode_ln_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        return_val = telnet.write_encode_ln("test")
        telnet.main_session.write.assert_called_with((telnet.cmd_encode("test") + telnet.eol).encode("ascii"))
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_write_encode_ln_not_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = False
        telnet.main_session = mock_telnet
        return_val = telnet.write_encode_ln("test")
        telnet.main_session.write.assert_not_called()
        self.assertIsNone(return_val)

    # +---------------------------+
    # | Send Command Object Tests |
    # +---------------------------+
    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(TelnetAgent, "send_command_wait_for_prompt")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_object_connected_single_command(self, mock_telnet, mock_read, mock_dev):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        self.eos_dev.current_agent = telnet
        self.eos_dev.wait_for_prompt = True
        mock_dev.return_value = True, ""
        mock_read.return_value = "1"
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1"
        return_val = telnet.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(TelnetAgent, "send_command_wait_for_prompt")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_object_connected_multi_command(self, mock_telnet, mock_read, mock_dev):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        self.eos_dev.current_agent = telnet
        self.eos_dev.wait_for_prompt = True
        mock_dev.return_value = True, ""
        mock_read.side_effect = ["1", "2"]
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1||command2"
        return_val = telnet.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1||2")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(TelnetAgent, "send_command_wait_for_quiet")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_object_connected_single_command_no_wfp(self, mock_telnet, mock_read, mock_dev):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        self.eos_dev.current_agent = telnet
        self.eos_dev.wait_for_prompt = False
        mock_dev.return_value = True, ""
        mock_read.return_value = "1"
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1"
        return_val = telnet.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(TelnetAgent, "send_command_wait_for_quiet")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_object_connected_multi_command_no_wfp(self, mock_telnet, mock_read, mock_dev):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        self.eos_dev.current_agent = telnet
        self.eos_dev.wait_for_prompt = False
        mock_dev.return_value = True, ""
        mock_read.side_effect = ["1", "2"]
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1||command2"
        return_val = telnet.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1||2")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(TelnetAgent, "send_command_wait_for_confirmation")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_object_connected_single_command_with_conf(self, mock_telnet, mock_read, mock_dev):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        self.eos_dev.current_agent = telnet
        self.eos_dev.wait_for_prompt = True
        mock_dev.return_value = True, ""
        mock_read.return_value = ("1", None)
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1"
        cmd_obj.confirmation_args = "arg1"
        cmd_obj.confirmation_phrases = "phrase1"
        return_val = telnet.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(TelnetAgent, "send_command_wait_for_confirmation")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_object_connected_multi_command_with_conf(self, mock_telnet, mock_read, mock_dev):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        self.eos_dev.current_agent = telnet
        self.eos_dev.wait_for_prompt = True
        mock_dev.return_value = True, ""
        mock_read.return_value = ("1", None)
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1||command2"
        cmd_obj.confirmation_args = "arg1"
        cmd_obj.confirmation_phrases = "phrase1"
        return_val = telnet.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1||1")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(TelnetAgent, "send_command_wait_for_confirmation")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_object_connected_single_command_with_multi_conf(self, mock_telnet, mock_read, mock_dev):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        self.eos_dev.current_agent = telnet
        self.eos_dev.wait_for_prompt = True
        mock_dev.return_value = True, ""
        mock_read.side_effect = [("1", 1), ("2", None)]
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1"
        cmd_obj.confirmation_args = "arg1||arg2"
        cmd_obj.confirmation_phrases = "phrase1||phrase2"
        return_val = telnet.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1||2")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(TelnetAgent, "send_command_wait_for_confirmation")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_object_connected_multi_command_with_multi_conf(self, mock_telnet, mock_read, mock_dev):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        self.eos_dev.current_agent = telnet
        self.eos_dev.wait_for_prompt = True
        mock_dev.return_value = True, ""
        mock_read.side_effect = [("1", 1), ("2", None), ("1", None)]
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1||command2"
        cmd_obj.confirmation_args = "arg1||arg2"
        cmd_obj.confirmation_phrases = "phrase1||phrase2"
        return_val = telnet.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1||2||1")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(TelnetAgent, "send_command_wait_for_confirmation")
    @mock.patch.object(TelnetAgent, "send_command_wait_for_confirmation_or_quiet")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_object_connected_single_command_with_multi_conf_no_wfp(self, mock_telnet, mock_quiet,
                                                                                 mock_read, mock_dev):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        self.eos_dev.current_agent = telnet
        self.eos_dev.wait_for_prompt = False
        mock_dev.return_value = True, ""
        mock_read.return_value = ("1", 1)
        mock_quiet.side_effect = [("2", None), ("1", None)]
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1"
        cmd_obj.confirmation_args = "arg1||arg2"
        cmd_obj.confirmation_phrases = "phrase1||phrase2"
        return_val = telnet.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1||2")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(TelnetAgent, "send_command_wait_for_confirmation")
    @mock.patch.object(TelnetAgent, "send_command_wait_for_confirmation_or_quiet")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_object_connected_multi_command_with_multi_conf_no_wfp(self, mock_telnet, mock_quiet,
                                                                                mock_read, mock_dev):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        self.eos_dev.current_agent = telnet
        self.eos_dev.wait_for_prompt = False
        mock_dev.return_value = True, ""
        mock_read.side_effect = [("1", 1), ("2", None)]
        mock_quiet.return_value = ("2", None)
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1||command2"
        cmd_obj.confirmation_args = "arg1||arg2"
        cmd_obj.confirmation_phrases = "phrase1||phrase2"
        return_val = telnet.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1||2||2")
        self.assertFalse(return_val.error_state)

    # +------------------------+
    # | Wait Until Quiet Tests |
    # +------------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_wait_until_quiet_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        telnet.wait_for_sleep = 100
        telnet.wait_for_retries = 1
        telnet.main_session.read_very_eager.side_effect = ([b""] * 5) + [b"1"] + ([b""] * 10)
        return_val = telnet.wait_until_quiet(1000)
        self.assertAlmostEqual(telnet.main_session.read_very_eager.call_count, 10, delta=1)
        self.assertEqual(return_val, "1")

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_wait_until_quiet_not_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = False
        telnet.main_session = mock_telnet
        telnet.wait_for_sleep = 100
        telnet.wait_for_retries = 1
        self.assertRaises(EOFError, telnet.wait_until_quiet, 1000)
        telnet.main_session.read_very_eager.assert_not_called()

    # +---------------------+
    # | Wait No Parse Tests |
    # +---------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_wait_no_parse_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        telnet.main_session.read_very_eager.return_value = b"test"
        return_val = telnet.wait_no_parse(1, 9)
        telnet.main_session.read_very_eager.assert_called_with()
        self.assertEqual(telnet.main_session.read_very_eager.call_count, 10)
        self.assertEqual(return_val, "test" * 10)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_wait_no_parse_not_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = False
        telnet.main_session = mock_telnet
        telnet.main_session.read_very_eager.return_value = "test"
        self.assertRaises(EOFError, telnet.wait_no_parse, 1, 10)
        telnet.main_session.read_very_eager.assert_not_called()

    # +---------------------------------------+
    # | Wait For Confirmation or Prompt Tests |
    # +---------------------------------------+
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_wait_for_confirmation_or_prompt_connected(self, mock_telnet, mock_wait):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        mock_wait.side_effect = (["0"] * 10) + ["1"] + (["0"] * 10)
        return_val = telnet.wait_for_confirmation_or_prompt("", ["1"], 100)
        self.assertEqual(return_val, ("00000000001", 0))
        mock_wait.side_effect = (["0"] * 10) + ["2"] + (["0"] * 10)
        return_val = telnet.wait_for_confirmation_or_prompt("", ["1", "2", "3"], 100)
        self.assertEqual(return_val, ("00000000002", 1))
        mock_wait.side_effect = (["0"] * 10) + ["3"] + (["0"] * 10)
        return_val = telnet.wait_for_confirmation_or_prompt("", ["1", "2", "3"], 100)
        self.assertEqual(return_val, ("00000000003", 2))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_wait_for_confirmation_or_prompt_not_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = False
        telnet.main_session = mock_telnet
        telnet.main_session.read_very_eager.return_value = "test"
        self.assertRaises(EOFError, telnet.wait_for_confirmation_or_prompt, "", ["0", "1", "2"], 100)
        telnet.main_session.read_very_eager.assert_not_called()

    # +--------------------------------------+
    # | Wait for Regex Prompt or Quiet Tests |
    # +--------------------------------------+
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_wait_for_regex_prompt_or_quiet_connected(self, mock_telnet, mock_wait):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        mock_wait.side_effect = (["0"] * 10) + ["1", "2"] + (["0"] * 10)
        return_val = telnet.wait_for_regex_prompt_or_quiet("012", 100)
        self.assertEqual(return_val, "000000000012")

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_wait_for_regex_prompt_or_quiet_not_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = False
        telnet.main_session = mock_telnet
        telnet.main_session.read_very_eager.return_value = "test"
        self.assertRaises(EOFError, telnet.wait_for_regex_prompt_or_quiet, "012", 100)
        telnet.main_session.read_very_eager.assert_not_called()

    # +-----------------------+
    # | Wait for Prompt Tests |
    # +-----------------------+
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch.object(TelnetAgent, "_CliAgent__get_prompt_regex")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_wait_for_prompt_connected(self, mock_telnet, mock_prompt, mock_wait):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        mock_prompt.return_value = [re.compile(".*012")]
        mock_wait.side_effect = (["0"] * 10) + ["1", "2"] + (["0"] * 10)
        return_val = telnet.wait_for_prompt()
        self.assertEqual(return_val, "000000000012")

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_wait_for_prompt_not_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = False
        telnet.main_session = mock_telnet
        telnet.main_session.read_very_eager.return_value = "test"
        self.assertRaises(EOFError, telnet.wait_for_prompt)
        telnet.main_session.read_very_eager.assert_not_called()

    # +--------------------+
    # | Send Command Tests |
    # +--------------------+
    @mock.patch.object(TelnetAgent, "read_until")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_connected(self, mock_telnet, mock_read):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        mock_read.side_effect = ["1", "2", "3"]
        return_val = telnet.send_command(["command1", "command2", "command3"])
        self.assertEqual(return_val, "123")
        mock_read.side_effect = ["123"]
        return_val = telnet.send_command("command1")
        self.assertEqual(return_val, "123")

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_not_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = False
        telnet.main_session = mock_telnet
        self.assertRaises(EOFError, telnet.send_command, ["command1", "command2", "command3"])

    # +-----------------------------------+
    # | Send Command Wait for Quiet Tests |
    # +-----------------------------------+
    @mock.patch.object(TelnetAgent, "wait_until_quiet")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_wait_for_quiet_connected(self, mock_telnet, mock_wait):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        mock_wait.side_effect = ["1", "2", "3"]
        return_val = telnet.send_command_wait_for_quiet(["command1", "command2", "command3"])
        self.assertEqual(return_val, "123")

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_wait_for_quiet_not_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = False
        telnet.main_session = mock_telnet
        self.assertRaises(EOFError, telnet.send_command_wait_for_quiet, ["command1", "command2", "command3"])

    # +------------------------------------+
    # | Send Command Wait for Prompt Tests |
    # +------------------------------------+
    @mock.patch.object(TelnetAgent, "wait_for_prompt")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_wait_for_prompt_connected(self, mock_telnet, mock_wait):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        mock_wait.side_effect = ["command11", "command22", "command33"]
        return_val = telnet.send_command_wait_for_prompt(["command1", "command2", "command3"])
        self.assertEqual(return_val, "123")

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_wait_for_prompt_not_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = False
        telnet.main_session = mock_telnet
        self.assertRaises(EOFError, telnet.send_command_wait_for_prompt, ["command1", "command2", "command3"])

    # +------------------------------------------+
    # | Send Command Wait for Confirmation Tests |
    # +------------------------------------------+
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_wait_for_confirmation_connected(self, mock_telnet, mock_wait):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        mock_wait.side_effect = (["0"] * 10) + ["1"] + (["0"] * 10) + ["snapshot"]
        conf_phrase_list = ["1"]
        return_val = telnet.send_command_wait_for_confirmation("command1", conf_phrase_list)
        self.assertEqual(return_val, ("00000000001", 0))
        conf_phrase_list.pop(0)
        return_val = telnet.send_command_wait_for_confirmation("command1", conf_phrase_list)
        self.assertEqual(return_val, ("0000000000snapshot", None))
        mock_wait.side_effect = (["0"] * 10) + ["1"] + (["0"] * 10)
        return_val = telnet.send_command_wait_for_confirmation("command1", "1")
        self.assertEqual(return_val, ("00000000001", 0))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_wait_for_confirmation_not_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = False
        telnet.main_session = mock_telnet
        self.assertRaises(EOFError, telnet.send_command_wait_for_confirmation, "command1", ["1"])
        self.assertRaises(EOFError, telnet.send_command_wait_for_confirmation, "command1", "1")

    # +---------------------------------------------------+
    # | Send Command Wait for Confirmation or Quiet Tests |
    # +---------------------------------------------------+
    @mock.patch.object(TelnetAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_wait_for_confirmation_or_quiet_connected(self, mock_telnet, mock_wait):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        mock_wait.side_effect = (["0"] * 10) + ["1"] + (["0"] * 10)
        return_val = telnet.send_command_wait_for_confirmation_or_quiet("command1", ["1"])
        self.assertEqual(return_val, ("00000000001", 0))
        mock_wait.side_effect = (["0"] * 10) + ["1"] + (["0"] * 10)
        return_val = telnet.send_command_wait_for_confirmation_or_quiet("command1", "1")
        self.assertEqual(return_val, ("00000000001", 0))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_send_command_wait_for_confirmation_or_quiet_not_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = False
        telnet.main_session = mock_telnet
        self.assertRaises(EOFError, telnet.send_command_wait_for_confirmation_or_quiet, "command1", ["1"])
        self.assertRaises(EOFError, telnet.send_command_wait_for_confirmation_or_quiet, "command1", "1")

    # +------------------+
    # | Read Until Tests |
    # +------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_read_until_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        telnet.read_until("1")
        telnet.main_session.read_until.assert_called_with(b"1")

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_read_until_not_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = False
        telnet.main_session = mock_telnet
        self.assertRaises(EOFError, telnet.read_until, "1")

    # +-----------------------------+
    # | Read Until List Match Tests |
    # +-----------------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_read_until_list_match_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = True
        telnet.main_session = mock_telnet
        telnet.read_until_list_match(["1", "2", "3"])
        telnet.main_session.expect.assert_called_with([b"1", b"2", b"3"])

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent.telnetlib.Telnet")
    def test_read_until_list_match_not_connected(self, mock_telnet):
        telnet = self.__test_setup(self.eos_dev)
        telnet.connected = False
        telnet.main_session = mock_telnet
        self.assertRaises(EOFError, telnet.read_until_list_match, ["1", "2", "3"])

    # ##################################################################################################################
    #   Non-test helper functions.   ###################################################################################
    # ##################################################################################################################
    @staticmethod
    def __test_setup(device):
        telnet = TelnetAgent(device)
        telnet.prompt_snapshot = "snapshot"
        device.login_prompt = ["1"]
        device.pass_prompt = "1"
        device.main_prompt = "1"
        device.port = 23
        device.prompt_handler = BasePromptHandler(device)

        return telnet


if __name__ == '__main__':
    RobotUnitTest.main()
