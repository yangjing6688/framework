from pytest_testconfig import config, load_yaml
from ExtremeAutomation.Imports.pytestConfigHelper import PytestConfigHelper
from ExtremeAutomation.Library.Utils.TestVersionUtils import JobsSuitesVersions
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
from ExtremeAutomation.Imports.CommonObjectUtils import CommonObjectUtils
from robot.libraries.BuiltIn import BuiltIn
from extauto.common.Utils import Utils
from extauto.common.Cli import Cli


@mark.testbed_none
class DefaultTests():

    default_type = 'XIQ'

    @classmethod
    def setup_class(cls):
        try:
            cls.executionHelper = PytestExecutionHelper()
            # Create an instance of the helper class that will read in 
            # the test bed yaml file and provide basic methods and variable access.
            # The user can also get to the test bed yaml by 
            # using the config dictionary
            #
            cls.commonObjectUtils = CommonObjectUtils()

            # Convert the device to a generic one
            cls.commonObjectUtils.convert_to_generic_device_object('device', index=1)

            cls.cli = Cli()
            cls.tb = PytestConfigHelper(config)
            cls.cfg = config
            cls.cfg['${OUTPUT DIR}'] = os.getcwd()
            cls.cfg['${TEST_NAME}'] = 'SETUP'

            # Debugging
            magic_key = cls.cfg.get('MAGIC_KEY', None)
            if magic_key:
                print(f"Debugging, setting the magic key: {magic_key}")
                os.environ["MAGIC_KEY"] = magic_key

            # Enable XAPI
            cls.cfg['${XAPI_ENABLE}'] = True

            cls.job_suite_uuid = cls.cfg.get('job_suite_uuid', None)
            if not cls.job_suite_uuid:
                raise Exception('Missing the command line argument --job_suite_uuid=<uuid>')
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


    def test_get_versions(self):
        '''[Documentation]  Test_Objective: Get the DUT version and XIQ Version '''

        post_data = {
            "name": '---',
            "resource_version": '---',
            "type": '---',
            "dut_version": '---',
            "jobsSuites_uuid": self.job_suite_uuid,
            "dut_name": '---',
            "cli_type": '---'
        }
        try:
            data_center_name = self.xiq.login.get_data_center_name()
            xiq_version = self.xiq.login.get_xiq_version()

            # XAPI Keyword
            print(f"The Data Center Name found: {data_center_name}")

            # No XAPI keyword support for this one
            print(f"The XIQ Version found: {xiq_version}")
            print("The job_suite_uuid is: ", self.job_suite_uuid)
            print("The Type is:", self.default_type)
            post_data["name"] = data_center_name
            post_data["resource_version"] =  xiq_version
            post_data["type"] =  self.default_type
        except Exception:
            print('Unable to get XIQ instance version data')

        try:
            # Check to see if there is a device to check
            if 'device1' not in self.tb.config:
                pytest.skip('There is no device for this test')

            # Login
            spawn = self.helper_login(self.tb.config.device1.ip,
                                      self.tb.config.device1.port,
                                      self.tb.config.device1.username,
                                      self.tb.config.device1.password,
                                      self.tb.config.device1.cli_type)

            # Send command based on DUT type:
            #
            cli_type = self.tb.config.device1.cli_type
            if cli_type.lower() == 'exos':
                self.helper_send_command(spawn, 'show version', post_data)
            elif cli_type.lower() == 'voss':
                self.helper_send_command(spawn, 'show sys-info | include SysDescr',post_data)

            # Close spawn
            self.cli.close_spawn(spawn)
        except Exception:
            print('Unable to get the device version information')

        # Here we need to call a keyword to update the database with
        # the information above:
        #
        print("Posting data to table: ", post_data)
        jcls = JobsSuitesVersions()

        # post the data for the device
        print(jcls.post(**post_data))
   
    # Helper methods
    def helper_login(self, ip, port, username, password, cli_type, **kwargs):
        '''[Documentation] Log in to the device to retrieve the version'''
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
    
    def helper_send_command(self, spawn, cmd, post_data, **kwargs):
        '''[Documentation]  Send a command, based on cli_type, to the device'''
        start_time = int(time.time())
        cmd_ret = self.cli.send(spawn, cmd, **kwargs)
        end_time = int(time.time())
        total_time = end_time - start_time
        if total_time > 30:
            pytest.fail("Device [" + str(spawn) + "] took too long to send command: " + str(cmd))

        exos_version_pattern = re.compile(r'IMG:[\s\d\.]+')
        voss_version_pattern = re.compile(r'\([\d\.a-zA-Z_]+\)')
        cli_type = self.tb.config.device1.cli_type
        try:
            if cli_type.lower() == 'exos':
                dut_ver = re.search(exos_version_pattern, cmd_ret).group()
                post_data['dut_version'] = dut_ver.replace('IMG:','').strip()
            elif cli_type.lower() == 'voss':
                dut_ver = re.search(voss_version_pattern, cmd_ret).group()
                post_data['dut_version'] = dut_ver.replace('(','').replace(')','').strip()
        except AttributeError:
            post_data['dut_version'] = 'N/A'
        finally:
            post_data['dut_name'] = self.tb.config.device1.name
            post_data['cli_type'] = cli_type.lower()


