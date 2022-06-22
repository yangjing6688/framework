import json
import os
from pytest_testconfig import config
from ExtremeAutomation.Imports.pytestConfigHelper import PytestConfigHelper
from extauto.common.Cli import Cli
from ExtremeAutomation.Imports.pytestExecutionHelper import PytestExecutionHelper
from ExtremeAutomation.Imports.DefaultLibrary import DefaultLibrary

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

    @mark.p1  # Marked as a P1 test case
    def test_01_log_all_generic_devices(self):
        """ Log into All Device Types """
        self.executionHelper.testSkipCheck()
        self.defaultLibrary.apiUdks.setupTeardownUdks.Base_Test_Suite_Setup()
        self.defaultLibrary.apiUdks.setupTeardownUdks.Base_Test_Suite_Cleanup()

    @mark.p1  # Marked as a P1 test case
    def test_02_log_into_exos(self):
        """ Log into EXOS """
        self.executionHelper.testSkipCheck()
        spawn = self.cli.open_spawn(self.tb.config.netelem1.ip,
                                    self.tb.config.netelem1.port,
                                    self.tb.config.netelem1.username,
                                    self.tb.config.netelem1.password,
                                    self.tb.config.netelem1.cli_type)
        cmd_ret = self.cli.send(spawn, 'show version')
        print(cmd_ret)
        self.cli.close_spawn(spawn)

    @mark.p1  # Marked as a P1 test case
    def test_03_log_into_voss(self):
        """ Log into VOSS """
        self.executionHelper.testSkipCheck()
        spawn = self.cli.open_spawn(self.tb.config.netelem2.ip,
                                    self.tb.config.netelem2.port,
                                    self.tb.config.netelem2.username,
                                    self.tb.config.netelem2.password,
                                    self.tb.config.netelem2.cli_type)
        cmd_ret = self.cli.send(spawn, 'show sys-info uboot')
        print(cmd_ret)
        self.cli.close_spawn(spawn)

    @mark.p1  # Marked as a P1 test case
    def test_03_log_into_wing_ap(self):
        """ Log into Wing-ap """
        self.executionHelper.testSkipCheck()
        spawn = self.cli.open_spawn(self.tb.config.wing1.ip,
                                    self.tb.config.wing1.port,
                                    self.tb.config.wing1.username,
                                    self.tb.config.wing1.password,
                                    self.tb.config.wing1.cli_type)
        cmd_ret = self.cli.send(spawn, 'show boot')
        print(cmd_ret)
        self.cli.close_spawn(spawn)

    @mark.p1  # Marked as a P1 test case
    def test_03_log_into_sr_router_ap(self):
        """ Log into sr Rerouter """
        self.executionHelper.testSkipCheck()
        spawn = self.cli.open_spawn(self.tb.config.aerohive_sw1.ip,
                                    self.tb.config.aerohive_sw1.port,
                                    self.tb.config.aerohive_sw1.username,
                                    self.tb.config.aerohive_sw1.password,
                                    self.tb.config.aerohive_sw1.cli_type)
        cmd_ret = self.cli.send(spawn, 'show sysinfo')
        print(cmd_ret)
        self.cli.close_spawn(spawn)

    @mark.p1  # Marked as a P1 test case
    def test_03_log_into_xr_router_ap(self):
        """ Log into sr Rerouter """
        self.executionHelper.testSkipCheck()
        spawn = self.cli.open_spawn(self.tb.config.router1.ip,
                                    self.tb.config.router1.port,
                                    self.tb.config.router1.username,
                                    self.tb.config.router1.password,
                                    self.tb.config.router1.cli_type,
                                    connection_method = self.tb.config.router1.connection_method)
        cmd_ret = self.cli.send(spawn, 'show system disk-info')
        print(cmd_ret)
        self.cli.close_spawn(spawn)


    @mark.p1  # Marked as a P1 test case
    def test_03_log_into_ap(self):
        """ Log into ap Rerouter """
        self.executionHelper.testSkipCheck()
        spawn = self.cli.open_spawn(self.tb.config.ap1.ip,
                                    self.tb.config.ap1.port,
                                    self.tb.config.ap1.username,
                                    self.tb.config.ap1.password,
                                    self.tb.config.ap1.cli_type)
        cmd_ret = self.cli.send(spawn, 'show version')
        print(cmd_ret)
        self.cli.close_spawn(spawn)

    @mark.p1  # Marked as a P1 test case
    def test_03_log_into_win_mu(self):
        """ Log into ap Win MU """
        self.executionHelper.testSkipCheck()
        spawn = self.cli.open_spawn(self.tb.config.mu1.ip,
                                    self.tb.config.mu1.port,
                                    self.tb.config.mu1.username,
                                    self.tb.config.mu1.password,
                                    self.tb.config.mu1.cli_type)
        cmd_ret = self.cli.send(spawn, 'dir')
        print(cmd_ret)
        self.cli.close_spawn(spawn)

    @mark.p1  # Marked as a P1 test case
    def test_03_log_into_mac_mu(self):
        """ Log into ap MAC MU """
        self.executionHelper.testSkipCheck()
        spawn = self.cli.open_spawn(self.tb.config.mu2.ip,
                                    self.tb.config.mu2.port,
                                    self.tb.config.mu2.username,
                                    self.tb.config.mu2.password,
                                    self.tb.config.mu2.cli_type)
        cmd_ret = self.cli.send(spawn, 'ls -al')
        print(cmd_ret)
        self.cli.close_spawn(spawn)

    @mark.p1  # Marked as a P1 test case
    def test_03_log_into_a3(self):
        """ Log into A3 """
        self.executionHelper.testSkipCheck()
        spawn = self.cli.open_spawn(self.tb.config.a3.node1_ip,
                                    self.tb.config.a3.console_port,
                                    self.tb.config.a3.console_username,
                                    self.tb.config.a3.console_password,
                                    self.tb.config.a3.cli_type)
        cmd_ret = self.cli.send(spawn, 'ls -al')
        print(cmd_ret)
        self.cli.close_spawn(spawn)

