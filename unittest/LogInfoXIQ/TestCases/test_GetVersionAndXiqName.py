from pytest_testconfig import config, load_yaml
from ExtremeAutomation.Imports.pytestConfigHelper import PytestConfigHelper
from pytest import mark
from pytest import fixture
import pytest
import os
import re
import sys
import time
from pprint import pprint
from ExtremeAutomation.Imports.pytestExecutionHelper import PytestExecutionHelper
from ExtremeAutomation.Imports.XiqLibrary import XiqLibrary
from ExtremeAutomation.Imports.XiqLibraryHelper import XiqLibraryHelper

@mark.testbed_none
class DefaultTests():

    @classmethod
    def setup_class(cls):
        try:
            cls.executionHelper = PytestExecutionHelper()
            # Create an instance of the helper class that will read in the test bed yaml file and provide basic methods and variable access.
            # The user can also get to the test bed yaml by using the config dictionary
            cls.tb = PytestConfigHelper(config)
            cls.cfg = config
            cls.cfg['${OUTPUT DIR}'] = os.getcwd()
            cls.cfg['${TEST_NAME}'] = 'SETUP'

            # Enable XAPI
            cls.cfg['${XAPI_ENABLE}'] = True

            cls.job_suite_uuid = cls.cfg.get('jobSuite_uuid', None)
            if cls.job_suite_uuid:
                raise Exception('Missing the command line argument -DjobSuite_uuid=<uuid>')

            # Create the new object for the XIQ / XIQSE Libraries
            cls.xiq = XiqLibrary()
            cls.xiq.login.login_user(cls.tb.config.tenant_username,
                                     cls.tb.config.tenant_password,
                                     url=cls.tb.config.test_url,
                                     IRV=True)

        except Exception as e:
            cls.executionHelper.setSetupFailure(True)


    @classmethod
    def teardown_class(cls):
        cls.xiq.login.logout_user()
        cls.xiq.login.quit_browser()


    """ Test Cases """
    def test_get_xiq_version_name(self):
        '''[Documentation]  Test_Objective: Get the XIQ name and version '''
        data_center_name = self.xiq.login.get_data_center_name()
        xiq_version = self.xiq.login.get_xiq_version()
        # XAPI Keyword
        print(f"The Data Center Name found: {data_center_name}")
        # No XAPI keyword support for this one
        print(f"The XIQ Version found: {xiq_version}")

        # Here we need to call a keyword to update the database with the information above:
        # user this cls.job_suite_uuid to get the UUID



    # Future for test beds
    # def test_get_device_version(self):
    #     # Login
    #     spawn = self.helper_login(self.tb.config.netelem1.ip,
    #                               self.tb.config.netelem1.port,
    #                               self.tb.config.netelem1.username,
    #                               self.tb.config.netelem1.password,
    #                               self.tb.config.netelem1.cli_type)
    #     # Send good command
    #     self.helper_send_command(spawn, 'show version')
    #
    #     # Close spawn
    #     self.cli.close_spawn(spawn)
    #
    # """ Helper methods """
    #
    # def helper_login(self, ip, port, username, password, cli_type, **kwargs):
    #     start_time = int(time.time())
    #     spawn = self.cli.open_spawn(ip,
    #                                 port,
    #                                 username,
    #                                 password,
    #                                 cli_type,
    #                                 **kwargs)
    #     end_time = int(time.time())
    #     total_time = end_time - start_time
    #     if total_time > 30:
    #         pytest.fail("Device took too long to log in!")
    #     return spawn
    #
    # def helper_send_command(self, spawn, cmd, **kwargs):
    #     start_time = int(time.time())
    #     cmd_ret = self.cli.send(spawn, cmd, **kwargs)
    #     end_time = int(time.time())
    #     total_time = end_time - start_time
    #     if total_time > 30:
    #         pytest.fail("Device [" + str(spawn) + "] took too long to send command: " + str(cmd))
    #     print(cmd_ret)
