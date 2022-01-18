import re
import mock
from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Library.Device.Common.Agents.SshAgent import SshAgent
from ExtremeAutomation.Library.Device.Common.CommandObjects.CliCommandObject import CliCommandObject
from ExtremeAutomation.Library.Device.Common.PromptHandler.BasePromptHandler import BasePromptHandler


class SshTests(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.create_dummy_devices()

    # +-------------+
    # | Login Tests |
    # +-------------+
    @mock.patch.object(SshAgent, "read_until")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_login_boss(self, mock_ssh, mock_read):
        ssh = self.__test_setup(self.boss_dev)
        mock_read.return_value = ""
        return_val = ssh.login()

        kwargs = {"device_type": "terminal_server",
                  "ip": self.boss_dev.hostname,
                  "password": self.boss_dev.password,
                  "port": self.boss_dev.port,
                  "username": self.boss_dev.username,
                  "timeout": 30,
                  "keepalive": 3}

        mock_ssh.assert_called_with(**kwargs)
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_login_eos(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        return_val = ssh.login()

        kwargs = {"device_type": "terminal_server",
                  "ip": self.eos_dev.hostname,
                  "password": self.eos_dev.password,
                  "port": self.eos_dev.port,
                  "username": self.eos_dev.username,
                  "timeout": 30,
                  "keepalive": 3}

        mock_ssh.assert_called_with(**kwargs)
        self.assertTrue(return_val)

    @mock.patch.object(SshAgent, "read_until")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_login_exos(self, mock_ssh, mock_read):
        ssh = self.__test_setup(self.exos_dev)
        mock_read.return_value = ""
        return_val = ssh.login()

        kwargs = {"device_type": "extreme",
                  "ip": self.exos_dev.hostname,
                  "password": self.exos_dev.password,
                  "port": self.exos_dev.port,
                  "username": self.exos_dev.username,
                  "timeout": 30,
                  "keepalive": 3}

        mock_ssh.assert_called_with(**kwargs)
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_login_ecos(self, mock_ssh):
        ssh = self.__test_setup(self.ecos_dev)
        return_val = ssh.login()

        kwargs = {"device_type": "cisco_ios",
                  "ip": self.ecos_dev.hostname,
                  "password": self.ecos_dev.password,
                  "port": self.ecos_dev.port,
                  "username": self.ecos_dev.username,
                  "timeout": 30,
                  "keepalive": 3}

        mock_ssh.assert_called_with(**kwargs)
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_login_linux(self, mock_ssh):
        ssh = self.__test_setup(self.linux_dev)
        return_val = ssh.login()

        kwargs = {"device_type": "ovs_linux",
                  "ip": self.linux_dev.hostname,
                  "password": self.linux_dev.password,
                  "port": self.linux_dev.port,
                  "username": self.linux_dev.username,
                  "timeout": 30,
                  "keepalive": 3}

        mock_ssh.assert_called_with(**kwargs)
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_login_extr_wireless(self, mock_ssh):
        ssh = self.__test_setup(self.extr_wireless_dev)
        return_val = ssh.login()

        kwargs = {"device_type": "cisco_ios",
                  "ip": self.extr_wireless_dev.hostname,
                  "password": self.extr_wireless_dev.password,
                  "port": self.extr_wireless_dev.port,
                  "username": self.extr_wireless_dev.username,
                  "timeout": 30,
                  "keepalive": 3}

        mock_ssh.assert_called_with(**kwargs)
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_login_zebra_wireless(self, mock_ssh):
        ssh = self.__test_setup(self.zebra_wireless_dev)
        return_val = ssh.login()

        kwargs = {"device_type": "cisco_ios",
                  "ip": self.zebra_wireless_dev.hostname,
                  "password": self.zebra_wireless_dev.password,
                  "port": self.zebra_wireless_dev.port,
                  "username": self.zebra_wireless_dev.username,
                  "timeout": 30,
                  "keepalive": 3}

        mock_ssh.assert_called_with(**kwargs)
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_login_snap_route(self, mock_ssh):
        ssh = self.__test_setup(self.snap_route_dev)
        return_val = ssh.login()

        kwargs = {"device_type": "ovs_linux",
                  "ip": self.snap_route_dev.hostname,
                  "password": self.snap_route_dev.password,
                  "port": self.snap_route_dev.port,
                  "username": self.snap_route_dev.username,
                  "timeout": 30,
                  "keepalive": 3}

        mock_ssh.assert_called_with(**kwargs)
        self.assertTrue(return_val)

    @mock.patch.object(SshAgent, "read_until")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_login_voss(self, mock_ssh, mock_read):
        ssh = self.__test_setup(self.voss_dev)
        mock_read.return_value = ""
        return_val = ssh.login()

        kwargs = {"device_type": "avaya_vsp",
                  "ip": self.voss_dev.hostname,
                  "password": self.voss_dev.password,
                  "port": self.voss_dev.port,
                  "username": self.voss_dev.username,
                  "timeout": 30,
                  "keepalive": 3}

        mock_ssh.assert_called_with(**kwargs)
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_login_jets(self, mock_ssh):
        ssh = self.__test_setup(self.jets_dev)
        return_val = ssh.login()

        kwargs = {"device_type": "terminal_server",
                  "ip": self.jets_dev.hostname,
                  "password": self.jets_dev.password,
                  "port": self.jets_dev.port,
                  "username": self.jets_dev.username,
                  "timeout": 30,
                  "keepalive": 3}

        mock_ssh.assert_called_with(**kwargs)
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_login_alpha(self, mock_ssh):
        ssh = self.__test_setup(self.alpha_dev)
        return_val = ssh.login()

        kwargs = {"device_type": "cisco_ios",
                  "ip": self.alpha_dev.hostname,
                  "password": self.alpha_dev.password,
                  "port": self.alpha_dev.port,
                  "username": self.alpha_dev.username,
                  "timeout": 30,
                  "keepalive": 3}

        mock_ssh.assert_called_with(**kwargs)
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_login_eos_stacks(self, mock_ssh):
        ssh = self.__test_setup(self.eos_stacks_dev)
        return_val = ssh.login()

        kwargs = {"device_type": "cisco_ios",
                  "ip": self.eos_stacks_dev.hostname,
                  "password": self.eos_stacks_dev.password,
                  "port": self.eos_stacks_dev.port,
                  "username": self.eos_stacks_dev.username,
                  "timeout": 30,
                  "keepalive": 3}

        mock_ssh.assert_called_with(**kwargs)
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_login_slx(self, mock_ssh):
        ssh = self.__test_setup(self.slx_dev)
        return_val = ssh.login()

        kwargs = {"device_type": "terminal_server",
                  "ip": self.slx_dev.hostname,
                  "password": self.slx_dev.password,
                  "port": self.slx_dev.port,
                  "username": self.slx_dev.username,
                  "timeout": 30,
                  "keepalive": 3}

        mock_ssh.assert_called_with(**kwargs)
        self.assertTrue(return_val)

    # +--------------+
    # | Logout Tests |
    # +--------------+
    @mock.patch.object(SshAgent, "read_until")
    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_logout_boss(self, mock_ssh, mock_wait, mock_read):
        ssh = self.__test_setup(self.boss_dev)
        ssh.main_session = mock_ssh
        mock_read.return_value = ""
        mock_wait.return_value = ""
        return_val = ssh.logout()
        ssh.main_session.disconnect.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(ssh.connected)
        self.assertFalse(ssh.logged_in)

    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_logout_eos(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.eos_dev)
        ssh.main_session = mock_ssh
        mock_wait.return_value = ""
        return_val = ssh.logout()
        ssh.main_session.disconnect.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(ssh.connected)
        self.assertFalse(ssh.logged_in)

    @mock.patch.object(SshAgent, "read_until")
    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_logout_exos(self, mock_ssh, mock_wait, mock_read):
        ssh = self.__test_setup(self.exos_dev)
        ssh.main_session = mock_ssh
        mock_read.return_value = ""
        mock_wait.return_value = ""
        return_val = ssh.logout()
        ssh.main_session.disconnect.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(ssh.connected)
        self.assertFalse(ssh.logged_in)

    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_logout_ecos(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.ecos_dev)
        ssh.main_session = mock_ssh
        mock_wait.return_value = ""
        return_val = ssh.logout()
        ssh.main_session.disconnect.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(ssh.connected)
        self.assertFalse(ssh.logged_in)

    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_logout_linux(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.linux_dev)
        ssh.main_session = mock_ssh
        mock_wait.return_value = ""
        return_val = ssh.logout()
        ssh.main_session.disconnect.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(ssh.connected)
        self.assertFalse(ssh.logged_in)

    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_logout_extr_wireless(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.extr_wireless_dev)
        ssh.main_session = mock_ssh
        mock_wait.return_value = ""
        return_val = ssh.logout()
        ssh.main_session.disconnect.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(ssh.connected)
        self.assertFalse(ssh.logged_in)

    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_logout_zebra_wireless(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.zebra_wireless_dev)
        ssh.main_session = mock_ssh
        mock_wait.return_value = ""
        return_val = ssh.logout()
        ssh.main_session.disconnect.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(ssh.connected)
        self.assertFalse(ssh.logged_in)

    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_logout_snap_route(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.snap_route_dev)
        ssh.main_session = mock_ssh
        mock_wait.return_value = ""
        return_val = ssh.logout()
        ssh.main_session.disconnect.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(ssh.connected)
        self.assertFalse(ssh.logged_in)

    @mock.patch.object(SshAgent, "read_until")
    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_logout_voss(self, mock_ssh, mock_wait, mock_read):
        ssh = self.__test_setup(self.voss_dev)
        ssh.main_session = mock_ssh
        mock_read.return_value = ""
        mock_wait.return_value = ""
        return_val = ssh.logout()
        ssh.main_session.disconnect.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(ssh.connected)
        self.assertFalse(ssh.logged_in)

    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_logout_jets(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.jets_dev)
        ssh.main_session = mock_ssh
        mock_wait.return_value = ""
        return_val = ssh.logout()
        ssh.main_session.disconnect.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(ssh.connected)
        self.assertFalse(ssh.logged_in)

    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_logout_alpha(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.alpha_dev)
        ssh.main_session = mock_ssh
        mock_wait.return_value = ""
        return_val = ssh.logout()
        ssh.main_session.disconnect.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(ssh.connected)
        self.assertFalse(ssh.logged_in)

    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_logout_eos_stacks(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.eos_stacks_dev)
        ssh.main_session = mock_ssh
        mock_wait.return_value = ""
        return_val = ssh.logout()
        ssh.main_session.disconnect.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(ssh.connected)
        self.assertFalse(ssh.logged_in)

    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_logout_slx(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.slx_dev)
        ssh.main_session = mock_ssh
        mock_wait.return_value = ""
        return_val = ssh.logout()
        ssh.main_session.disconnect.assert_called()
        self.assertIsNone(return_val)
        self.assertFalse(ssh.connected)
        self.assertFalse(ssh.logged_in)

    # +-------------+
    # | Write Tests |
    # +-------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_write_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        return_val = ssh.write("test")
        ssh.main_session.remote_conn.sendall.assert_called_with("test")
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_write_not_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = False
        ssh.main_session = mock_ssh
        return_val = ssh.write("test")
        ssh.main_session.remote_conn.sendall.assert_not_called()
        self.assertIsNone(return_val)

    # +--------------------+
    # | Write Encode Tests |
    # +--------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_write_encode_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        return_val = ssh.write_encode("test")
        ssh.main_session.remote_conn.sendall.assert_called_with(ssh.cmd_encode("test"))
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_write_encode_not_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = False
        ssh.main_session = mock_ssh
        return_val = ssh.write_encode("test")
        ssh.main_session.remote_conn.sendall.assert_not_called()
        self.assertIsNone(return_val)

    # +-----------------------+
    # | Write Encode Ln Tests |
    # +-----------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_write_encode_ln_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        return_val = ssh.write_encode_ln("test")
        ssh.main_session.remote_conn.sendall.assert_called_with(ssh.cmd_encode("test") + ssh.eol)
        self.assertTrue(return_val)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_write_encode_ln_not_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = False
        ssh.main_session = mock_ssh
        return_val = ssh.write_encode_ln("test")
        ssh.main_session.remote_conn.sendall.assert_not_called()
        self.assertIsNone(return_val)

    # +---------------------------+
    # | Send Command Object Tests |
    # +---------------------------+
    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(SshAgent, "send_command_wait_for_prompt")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_object_connected_single_command(self, mock_ssh, mock_read, mock_dev):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        self.eos_dev.current_agent = ssh
        self.eos_dev.wait_for_prompt = True
        mock_dev.return_value = True, ""
        mock_read.return_value = "1"
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1"
        return_val = ssh.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(SshAgent, "send_command_wait_for_prompt")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_object_connected_multi_command(self, mock_ssh, mock_read, mock_dev):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        self.eos_dev.current_agent = ssh
        self.eos_dev.wait_for_prompt = True
        mock_dev.return_value = True, ""
        mock_read.side_effect = ["1", "2"]
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1||command2"
        return_val = ssh.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1||2")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(SshAgent, "send_command_wait_for_quiet")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_object_connected_single_command_no_wfp(self, mock_ssh, mock_read, mock_dev):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        self.eos_dev.current_agent = ssh
        self.eos_dev.wait_for_prompt = False
        mock_dev.return_value = True, ""
        mock_read.return_value = "1"
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1"
        return_val = ssh.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(SshAgent, "send_command_wait_for_quiet")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_object_connected_multi_command_no_wfp(self, mock_ssh, mock_read, mock_dev):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        self.eos_dev.current_agent = ssh
        self.eos_dev.wait_for_prompt = False
        mock_dev.return_value = True, ""
        mock_read.side_effect = ["1", "2"]
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1||command2"
        return_val = ssh.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1||2")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(SshAgent, "send_command_wait_for_confirmation")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_object_connected_single_command_with_conf(self, mock_ssh, mock_read, mock_dev):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        self.eos_dev.current_agent = ssh
        self.eos_dev.wait_for_prompt = True
        mock_dev.return_value = True, ""
        mock_read.return_value = ("1", None)
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1"
        cmd_obj.confirmation_args = "arg1"
        cmd_obj.confirmation_phrases = "phrase1"
        return_val = ssh.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(SshAgent, "send_command_wait_for_confirmation")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_object_connected_multi_command_with_conf(self, mock_ssh, mock_read, mock_dev):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        self.eos_dev.current_agent = ssh
        self.eos_dev.wait_for_prompt = True
        mock_dev.return_value = True, ""
        mock_read.return_value = ("1", None)
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1||command2"
        cmd_obj.confirmation_args = "arg1"
        cmd_obj.confirmation_phrases = "phrase1"
        return_val = ssh.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1||1")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(SshAgent, "send_command_wait_for_confirmation")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_object_connected_single_command_with_multi_conf(self, mock_ssh, mock_read, mock_dev):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        self.eos_dev.current_agent = ssh
        self.eos_dev.wait_for_prompt = True
        mock_dev.return_value = True, ""
        mock_read.side_effect = [("1", 1), ("2", None)]
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1"
        cmd_obj.confirmation_args = "arg1||arg2"
        cmd_obj.confirmation_phrases = "phrase1||phrase2"
        return_val = ssh.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1||2")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(SshAgent, "send_command_wait_for_confirmation")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_object_connected_multi_command_with_multi_conf(self, mock_ssh, mock_read, mock_dev):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        self.eos_dev.current_agent = ssh
        self.eos_dev.wait_for_prompt = True
        mock_dev.return_value = True, ""
        mock_read.side_effect = [("1", 1), ("2", None), ("1", None)]
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1||command2"
        cmd_obj.confirmation_args = "arg1||arg2"
        cmd_obj.confirmation_phrases = "phrase1||phrase2"
        return_val = ssh.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1||2||1")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(SshAgent, "send_command_wait_for_confirmation")
    @mock.patch.object(SshAgent, "send_command_wait_for_confirmation_or_quiet")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_object_connected_single_command_with_multi_conf_no_wfp(self, mock_ssh, mock_quiet,
                                                                                 mock_read, mock_dev):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        self.eos_dev.current_agent = ssh
        self.eos_dev.wait_for_prompt = False
        mock_dev.return_value = True, ""
        mock_read.return_value = ("1", 1)
        mock_quiet.side_effect = [("2", None), ("1", None)]
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1"
        cmd_obj.confirmation_args = "arg1||arg2"
        cmd_obj.confirmation_phrases = "phrase1||phrase2"
        return_val = ssh.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1||2")
        self.assertFalse(return_val.error_state)

    @mock.patch.object(BasePromptHandler, "change_prompt")
    @mock.patch.object(SshAgent, "send_command_wait_for_confirmation")
    @mock.patch.object(SshAgent, "send_command_wait_for_confirmation_or_quiet")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_object_connected_multi_command_with_multi_conf_no_wfp(self, mock_ssh, mock_quiet,
                                                                                mock_read, mock_dev):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        self.eos_dev.current_agent = ssh
        self.eos_dev.wait_for_prompt = False
        mock_dev.return_value = True, ""
        mock_read.side_effect = [("1", 1), ("2", None)]
        mock_quiet.return_value = ("2", None)
        cmd_obj = CliCommandObject()
        cmd_obj.command = "command1||command2"
        cmd_obj.confirmation_args = "arg1||arg2"
        cmd_obj.confirmation_phrases = "phrase1||phrase2"
        return_val = ssh.send_command_object(cmd_obj)
        self.assertEqual(return_val.command, cmd_obj.command)
        self.assertEqual(return_val.return_text, "1||2||2")
        self.assertFalse(return_val.error_state)

    # +------------------------+
    # | Wait Until Quiet Tests |
    # +------------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_wait_until_quiet_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        ssh.wait_for_sleep = 100
        ssh.wait_for_retries = 1
        ssh.main_session.remote_conn.recv.side_effect = ([b""] * 5) + [b"1"] + ([b""] * 10)
        return_val = ssh.wait_until_quiet(1000)
        self.assertAlmostEqual(ssh.main_session.remote_conn.recv.call_count, 10, delta=1)
        self.assertEqual(return_val, "1")

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_wait_until_quiet_not_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = False
        ssh.main_session = mock_ssh
        ssh.wait_for_sleep = 100
        ssh.wait_for_retries = 1
        ssh.main_session.remote_conn.recv.side_effect = ([""] * 5) + ["1"] + ([""] * 10)
        self.assertRaises(EOFError, ssh.wait_until_quiet, 1000)
        ssh.main_session.remote_conn.recv.assert_not_called()

    # +---------------------+
    # | Wait No Parse Tests |
    # +---------------------+
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_wait_no_parse_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        ssh.main_session.remote_conn.recv.return_value = b"test"
        return_val = ssh.wait_no_parse(1, 9)
        ssh.main_session.remote_conn.recv.assert_called_with(65535)
        self.assertEqual(ssh.main_session.remote_conn.recv.call_count, 10)
        self.assertEqual(return_val, "test" * 10)

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_wait_no_parse_not_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = False
        ssh.main_session = mock_ssh
        ssh.main_session.remote_conn.recv.return_value = b"test"
        self.assertRaises(EOFError, ssh.wait_no_parse, 1, 10)
        ssh.main_session.remote_conn.recv.assert_not_called()

    # +---------------------------------------+
    # | Wait For Confirmation or Prompt Tests |
    # +---------------------------------------+
    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_wait_for_confirmation_or_prompt_connected(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        mock_wait.side_effect = (["0"] * 10) + ["1"] + (["0"] * 10)
        return_val = ssh.wait_for_confirmation_or_prompt("", ["1"], 100)
        self.assertEqual(return_val, ("00000000001", 0))
        mock_wait.side_effect = (["0"] * 10) + ["2"] + (["0"] * 10)
        return_val = ssh.wait_for_confirmation_or_prompt("", ["1", "2", "3"], 100)
        self.assertEqual(return_val, ("00000000002", 1))
        mock_wait.side_effect = (["0"] * 10) + ["3"] + (["0"] * 10)
        return_val = ssh.wait_for_confirmation_or_prompt("", ["1", "2", "3"], 100)
        self.assertEqual(return_val, ("00000000003", 2))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_wait_for_confirmation_or_prompt_not_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = False
        ssh.main_session = mock_ssh
        ssh.main_session.remote_conn.recv.return_value = "test"
        self.assertRaises(EOFError, ssh.wait_for_confirmation_or_prompt, "", ["0", "1", "2"], 100)
        ssh.main_session.remote_conn.recv.assert_not_called()

    # +--------------------------------------+
    # | Wait for Regex Prompt or Quiet Tests |
    # +--------------------------------------+
    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_wait_for_regex_prompt_or_quiet_connected(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        mock_wait.side_effect = (["0"] * 10) + ["1", "2"] + (["0"] * 10)
        return_val = ssh.wait_for_regex_prompt_or_quiet("012", 100)
        self.assertEqual(return_val, "000000000012")

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_wait_for_regex_prompt_or_quiet_not_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = False
        ssh.main_session = mock_ssh
        ssh.main_session.remote_conn.recv.return_value = "test"
        self.assertRaises(EOFError, ssh.wait_for_regex_prompt_or_quiet, "012", 100)
        ssh.main_session.remote_conn.recv.assert_not_called()

    # +-----------------------+
    # | Wait for Prompt Tests |
    # +-----------------------+
    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch.object(SshAgent, "_CliAgent__get_prompt_regex")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_wait_for_prompt_connected(self, mock_ssh, mock_prompt, mock_wait):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        mock_prompt.return_value = [re.compile(".*012")]
        mock_wait.side_effect = (["0"] * 10) + ["1", "2"] + (["0"] * 10)
        return_val = ssh.wait_for_prompt()
        self.assertEqual(return_val, "000000000012")

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_wait_for_prompt_not_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = False
        ssh.main_session = mock_ssh
        ssh.main_session.remote_conn.recv.return_value = "test"
        self.assertRaises(EOFError, ssh.wait_for_prompt)
        ssh.main_session.remote_conn.recv.assert_not_called()

    # +--------------------+
    # | Send Command Tests |
    # +--------------------+
    @mock.patch.object(SshAgent, "read_until")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_connected(self, mock_ssh, mock_read):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        mock_read.side_effect = ["1", "2", "3"]
        return_val = ssh.send_command(["command1", "command2", "command3"])
        self.assertEqual(return_val, "123")
        mock_read.side_effect = ["123"]
        return_val = ssh.send_command("command1")
        self.assertEqual(return_val, "123")

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_not_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = False
        ssh.main_session = mock_ssh
        self.assertRaises(EOFError, ssh.send_command, ["command1", "command2", "command3"])

    # +-----------------------------------+
    # | Send Command Wait for Quiet Tests |
    # +-----------------------------------+
    @mock.patch.object(SshAgent, "wait_until_quiet")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_wait_for_quiet_connected(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        mock_wait.side_effect = ["1", "2", "3"]
        return_val = ssh.send_command_wait_for_quiet(["command1", "command2", "command3"])
        self.assertEqual(return_val, "123")

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_wait_for_quiet_not_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = False
        ssh.main_session = mock_ssh
        self.assertRaises(EOFError, ssh.send_command_wait_for_quiet, ["command1", "command2", "command3"])

    # +------------------------------------+
    # | Send Command Wait for Prompt Tests |
    # +------------------------------------+
    @mock.patch.object(SshAgent, "wait_for_prompt")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_wait_for_prompt_connected(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        mock_wait.side_effect = ["command11", "command22", "command33"]
        return_val = ssh.send_command_wait_for_prompt(["command1", "command2", "command3"])
        self.assertEqual(return_val, "123")

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_wait_for_prompt_not_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = False
        ssh.main_session = mock_ssh
        self.assertRaises(EOFError, ssh.send_command_wait_for_prompt, ["command1", "command2", "command3"])

    # +------------------------------------------+
    # | Send Command Wait for Confirmation Tests |
    # +------------------------------------------+
    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_wait_for_confirmation_connected(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        mock_wait.side_effect = (["0"] * 10) + ["1"] + (["0"] * 10) + ["snapshot"]
        conf_phrase_list = ["1"]
        return_val = ssh.send_command_wait_for_confirmation("command1", conf_phrase_list)
        self.assertEqual(return_val, ("00000000001", 0))
        conf_phrase_list.pop(0)
        return_val = ssh.send_command_wait_for_confirmation("command1", conf_phrase_list)
        self.assertEqual(return_val, ("0000000000snapshot", None))
        mock_wait.side_effect = (["0"] * 10) + ["1"] + (["0"] * 10)
        return_val = ssh.send_command_wait_for_confirmation("command1", "1")
        self.assertEqual(return_val, ("00000000001", 0))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_wait_for_confirmation_not_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = False
        ssh.main_session = mock_ssh
        self.assertRaises(EOFError, ssh.send_command_wait_for_confirmation, "command1", ["1"])
        self.assertRaises(EOFError, ssh.send_command_wait_for_confirmation, "command1", "1")

    # +---------------------------------------------------+
    # | Send Command Wait for Confirmation or Quiet Tests |
    # +---------------------------------------------------+
    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_wait_for_confirmation_or_quiet_connected(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        mock_wait.side_effect = (["0"] * 10) + ["1"] + (["0"] * 10)
        return_val = ssh.send_command_wait_for_confirmation_or_quiet("command1", ["1"])
        self.assertEqual(return_val, ("00000000001", 0))
        mock_wait.side_effect = (["0"] * 10) + ["1"] + (["0"] * 10)
        return_val = ssh.send_command_wait_for_confirmation_or_quiet("command1", "1")
        self.assertEqual(return_val, ("00000000001", 0))

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_send_command_wait_for_confirmation_or_quiet_not_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = False
        ssh.main_session = mock_ssh
        self.assertRaises(EOFError, ssh.send_command_wait_for_confirmation_or_quiet, "command1", ["1"])
        self.assertRaises(EOFError, ssh.send_command_wait_for_confirmation_or_quiet, "command1", "1")

    # +------------------+
    # | Read Until Tests |
    # +------------------+
    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_read_until_connected(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        mock_wait.side_effect = ["0", "0", "0", "1", "0"]
        return_val = ssh.read_until("1")
        self.assertEqual(return_val, "0001")

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_read_until_not_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = False
        ssh.main_session = mock_ssh
        self.assertRaises(EOFError, ssh.read_until, "1")

    # +-----------------------------+
    # | Read Until List Match Tests |
    # +-----------------------------+
    @mock.patch.object(SshAgent, "wait_no_parse")
    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_read_until_list_match_connected(self, mock_ssh, mock_wait):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = True
        ssh.main_session = mock_ssh
        mock_wait.side_effect = ["0", "1", "2", "3", "4", "3", "2", "1", "0"]
        return_val = ssh.read_until_list_match(["1", "2", "3"])
        self.assertEqual(return_val, "01")
        mock_wait.side_effect = ["0", "1", "2", "3", "4", "3", "2", "1", "0"]
        return_val = ssh.read_until_list_match(["3", "2", "1"])
        self.assertEqual(return_val, "01")
        mock_wait.side_effect = ["0", "1", "2", "3", "4", "3", "2", "1", "0"]
        return_val = ssh.read_until_list_match(["3", "4", "5"])
        self.assertEqual(return_val, "0123")

    @mock.patch("ExtremeAutomation.Library.Device.Common.Agents.SshAgent.ConnectHandler")
    def test_read_until_list_match_not_connected(self, mock_ssh):
        ssh = self.__test_setup(self.eos_dev)
        ssh.connected = False
        ssh.main_session = mock_ssh
        self.assertRaises(EOFError, ssh.read_until_list_match, ["1", "2", "3"])

    # ##################################################################################################################
    #   Non-test helper functions.   ###################################################################################
    # ##################################################################################################################
    @staticmethod
    def __test_setup(device):
        ssh = SshAgent(device)
        ssh.prompt_snapshot = "snapshot"
        device.prompt_handler = BasePromptHandler(device)

        return ssh


if __name__ == '__main__':
    RobotUnitTest.main()
