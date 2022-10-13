import json
import os
from pytest_testconfig import config
from ExtremeAutomation.Imports.pytestConfigHelper import PytestConfigHelper
from extauto.common.Cli import Cli
from ExtremeAutomation.Imports.pytestExecutionHelper import PytestExecutionHelper
from ExtremeAutomation.Imports.DefaultLibrary import DefaultLibrary
import time

from pytest import mark

@mark.testbed_1_node # Marked all test cases as 1 node
class DefaultTests:
    
    # [Setup]  Test class Setup
    @classmethod
    def setup_class(cls):
        try:
            # Create the pytest execution helper
            cls.executionHelper = PytestExecutionHelper()
            config['${OUTPUT DIR}'] = os.getcwd()
            config['${TEST_NAME}'] = 'SETUP'
            cls.tb = PytestConfigHelper(config)
            cls.defaultLibrary = DefaultLibrary()


            cls.cli = Cli()
        
        except Exception :
            cls.executionHelper.setSetupFailure(True)

    def helper_login(self, ip, port, username, password, cli_type, **kwargs):
        start_time = int(time.time())
        spawn = self.cli.open_spawn(ip,
                                    port,
                                    username,
                                    password,
                                    cli_type,
                                    **kwargs)
        end_time = int(time.time())
        total_time = end_time - start_time
        if total_time > 30:
            pytest.fail("Device took too long to log in!")
        return spawn

    def helper_send_command(self, spawn, cmd, **kwargs):
        start_time = int(time.time())
        cmd_ret = self.cli.send(spawn, cmd, **kwargs)
        end_time = int(time.time())
        total_time = end_time - start_time
        if total_time > 30:
            pytest.fail("Device [" + str(spawn) + "] took too long to send command: " + str(cmd))
        print(cmd_ret)

    @mark.p1  # Marked as a P1 test case
    def test_02_log_into_exos(self):
        """ Log into EXOS """
        self.executionHelper.testSkipCheck()
        # Login
        self.defaultLibrary.deviceNetworkElement.networkElementConnectionManager.connect_to_network_element('test', '10.148.35.102', 'rwa', 'rwa', 'telnet', 'VOSS')
        self.defaultLibrary.deviceNetworkElement.networkElementCliSend.send_cmd('test', 'show ?')
        self.defaultLibrary.deviceNetworkElement.networkElementConnectionManager.connect_to_network_element('test',
                                                                                                        '10.148.35.102',
                                                                                                        'rwa', 'rwa',
                                                                                                        'telnet',
                                                                                                        'VOSS')
        self.defaultLibrary.deviceNetworkElement.networkElementCliSend.send_cmd('test', 'show ?')

    # @mark.p1  # Marked as a P1 test case
    # def test_01_log_all_generic_devices(self):
    #     """ Log into All Device Types """
    #     self.executionHelper.testSkipCheck()
    #     self.defaultLibrary.apiUdks.setupTeardownUdks.Base_Test_Suite_Setup()
    #     self.defaultLibrary.apiUdks.setupTeardownUdks.Base_Test_Suite_Cleanup()
    #
    # @mark.p1  # Marked as a P1 test case
    # def test_02_log_into_exos(self):
    #     """ Log into EXOS """
    #     self.executionHelper.testSkipCheck()
    #     # Login
    #     spawn = self.helper_login(self.tb.config.netelem1.ip,
    #                               self.tb.config.netelem1.port,
    #                               self.tb.config.netelem1.username,
    #                               self.tb.config.netelem1.password,
    #                               self.tb.config.netelem1.cli_type)
    #     # Send good command
    #     self.helper_send_command(spawn, 'show version')
    #     # Send Bad command
    #     self.helper_send_command(spawn, 'error commmand isssued', expect_error=True)
    #     # Close spawn
    #     self.cli.close_spawn(spawn)
    #
    # @mark.p1  # Marked as a P1 test case
    # def test_03_log_into_voss(self):
    #     """ Log into VOSS """
    #     self.executionHelper.testSkipCheck()
    #     # Login
    #     spawn = self.helper_login(self.tb.config.netelem2.ip,
    #                               self.tb.config.netelem2.port,
    #                               self.tb.config.netelem2.username,
    #                               self.tb.config.netelem2.password,
    #                               self.tb.config.netelem2.cli_type)
    #     # Send good command
    #     self.helper_send_command(spawn, 'show sys-info uboot')
    #     # Send Bad command
    #     self.helper_send_command(spawn, 'error commmand isssued', expect_error=True)
    #     # Close spawn
    #     self.cli.close_spawn(spawn)
    #
    # @mark.p1  # Marked as a P1 test case
    # def test_04_log_into_wing_ap(self):
    #     """ Log into Wing-ap """
    #     self.executionHelper.testSkipCheck()
    #     # Login
    #     spawn = self.helper_login(self.tb.config.wing1.ip,
    #                               self.tb.config.wing1.port,
    #                               self.tb.config.wing1.username,
    #                               self.tb.config.wing1.password,
    #                               self.tb.config.wing1.cli_type)
    #     # Send good command
    #     self.helper_send_command(spawn, 'show boot')
    #     # Send Bad command
    #     self.helper_send_command(spawn, 'error commmand isssued', expect_error=True)
    #     # Close spawn
    #     self.cli.close_spawn(spawn)
    #
    # @mark.p1  # Marked as a P1 test case
    # def test_05_log_into_sr_router_ap(self):
    #     """ Log into sr router """
    #     self.executionHelper.testSkipCheck()
    #     # Login
    #     spawn = self.helper_login(self.tb.config.aerohive_sw1.ip,
    #                               self.tb.config.aerohive_sw1.port,
    #                               self.tb.config.aerohive_sw1.username,
    #                               self.tb.config.aerohive_sw1.password,
    #                               self.tb.config.aerohive_sw1.cli_type)
    #     # Send good command
    #     self.helper_send_command(spawn, 'show sysinfo')
    #     # Send Bad command
    #     self.helper_send_command(spawn, 'error commmand isssued', expect_error=True)
    #     # Close spawn
    #     self.cli.close_spawn(spawn)
    #
    # @mark.p1  # Marked as a P1 test case
    # def test_06_log_into_xr_router_ap(self):
    #     """ Log into xr router """
    #     self.executionHelper.testSkipCheck()
    #     # Login
    #     spawn = self.helper_login(self.tb.config.router1.ip,
    #                               self.tb.config.router1.port,
    #                               self.tb.config.router1.username,
    #                               self.tb.config.router1.password,
    #                               self.tb.config.router1.cli_type,
    #                               connection_method = self.tb.config.router1.connection_method)
    #     # Send good command
    #     self.helper_send_command(spawn, 'show system disk-info')
    #     # Send Bad command
    #     self.helper_send_command(spawn, 'error commmand isssued', expect_error=True)
    #     # Close spawn
    #     self.cli.close_spawn(spawn)
    #
    #
    # @mark.p1  # Marked as a P1 test case
    # def test_07_log_into_ap(self):
    #     """ Log into ap """
    #     self.executionHelper.testSkipCheck()
    #     # Login
    #     spawn = self.helper_login(self.tb.config.ap1.ip,
    #                               self.tb.config.ap1.port,
    #                               self.tb.config.ap1.username,
    #                               self.tb.config.ap1.password,
    #                               self.tb.config.ap1.cli_type)
    #     # Send good command
    #     self.helper_send_command(spawn, 'show version')
    #     # Send Bad command
    #     self.helper_send_command(spawn, 'error commmand isssued', expect_error=True)
    #     # Close spawn
    #     self.cli.close_spawn(spawn)
    #
    # @mark.p1  # Marked as a P1 test case
    # def test_08_log_into_win_mu(self):
    #     """ Log into Win MU """
    #     self.executionHelper.testSkipCheck()
    #     # Login
    #     spawn = self.helper_login(self.tb.config.mu1.ip,
    #                               self.tb.config.mu1.port,
    #                               self.tb.config.mu1.username,
    #                               self.tb.config.mu1.password,
    #                               self.tb.config.mu1.cli_type)
    #     # Send good command
    #     self.helper_send_command(spawn, 'dir')
    #     # Send Bad command
    #     self.helper_send_command(spawn, 'error commmand isssued', expect_error=True)
    #     # Close spawn
    #     self.cli.close_spawn(spawn)
    #
    # @mark.p1  # Marked as a P1 test case
    # def test_09_log_into_mac_mu(self):
    #     """ Log into MAC MU """
    #     self.executionHelper.testSkipCheck()
    #     # Login
    #     spawn = self.helper_login(self.tb.config.mu2.ip,
    #                               self.tb.config.mu2.port,
    #                               self.tb.config.mu2.username,
    #                               self.tb.config.mu2.password,
    #                               self.tb.config.mu2.cli_type)
    #     # Send good command
    #     self.helper_send_command(spawn, 'ls -al')
    #     # Send bad command
    #     self.helper_send_command(spawn, 'error commmand isssued', expect_error=True)
    #     # Close spawn
    #     self.cli.close_spawn(spawn)
    #
    # @mark.p1  # Marked as a P1 test case
    # def test_10_log_into_a3(self):
    #     """ Log into A3 """
    #     self.executionHelper.testSkipCheck()
    #     # Login
    #     spawn = self.helper_login(self.tb.config.a3.node1_ip,
    #                               self.tb.config.a3.console_port,
    #                               self.tb.config.a3.console_username,
    #                               self.tb.config.a3.console_password,
    #                               self.tb.config.a3.cli_type)
    #     # Send good command
    #     self.helper_send_command(spawn, 'ls -al')
    #     # Send Bad command
    #     self.helper_send_command(spawn, 'error commmand isssued', expect_error=True)
    #     # Close spawn
    #     self.cli.close_spawn(spawn)
    #
    # @mark.p1  # Marked as a P1 test case
    # def test_11_log_into_linux(self):
    #     """ Log into Linux MU """
    #     self.executionHelper.testSkipCheck()
    #     # Login
    #     spawn = self.helper_login(self.tb.config.mu3.ip,
    #                               self.tb.config.mu3.port,
    #                               self.tb.config.mu3.username,
    #                               self.tb.config.mu3.password,
    #                               self.tb.config.mu3.cli_type)
    #     # Send good command
    #     self.helper_send_command(spawn, 'ls -al')
    #     # Send bad command
    #     self.helper_send_command(spawn, 'error commmand isssued', expect_error=True)
    #     # Close spawn
    #     self.cli.close_spawn(spawn)

