from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import *
from a3.elements.ToolsWebElements import ToolsWebElements
from a3.elements.GlobalSettingWebElements import *
from xiq.flows.common.DeviceCommon import DeviceCommon
from common.CloudDriver import *
from selenium import webdriver
import re


class ToolsWebElementsflow(ToolsWebElements):
    def __init__(self):
        super().__init__()
        self.driver1 = None
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.tool_opt_web_elements = toolsWebElements()
        self.setting = GlobalSettingWebElements()
        self.driver = webdriver.Chrome()

    def connection_profile_test(self, mac_add):
        """
            - This keyword select the connection profile test from tools menu and takes mac as input and give
                profile in use
            - Keyword Usage
             - ``Connection Profile Test``
        :return: 1 if profile test is successful else return -1
        """
        self.utils.print_info("Selecting Connection Profile Test from Menu...")

        if self.auto_actions.click(self.get_conn_profile_test_ui()) == 1:
            sleep(2)
            self.utils.print_info("Entering the MAC address ")
            element = self.weh.get_element(self.mac_input)
            self.auto_actions.send_keys(element, mac_add)
            sleep(5)
            start_test_button = self.weh.get_element(self.test_start)
            self.auto_actions.click(start_test_button)
            sleep(5)
            test_output_text = self.weh.get_elements(self.test_output)
            test_output_lines = test_output_text[0].text
            self.utils.print_info(test_output_lines)
            if re.search(r'802.1X', test_output_lines):
                self.utils.print_info("Found 802.1X profile")
            elif re.search(r'guest', test_output_lines):
                self.utils.print_info("Found guest profile")
            else:
                self.utils.print_info("No profile found")
            sleep(10)
            return 1
        else:
            self.utils.print_info("No appropriate profile found")
            return -1

    def select_ssh(self):
        """
         - This keyword selects SSH option in Tools Page
         - Keyword Usage
          - ``Selects SSH option in Tools Page``

        :return: 1 if Navigation Successful to SSH Option else return -1
        """
        element = self.weh.get_element(self.ssh_option_ui)
        self.auto_actions.click(element)
        sleep(5)
        element1 = self.weh.get_element(self.ssh_selector)
        status = element1.is_selected()
        self.utils.print_info(status)
        if status:
            self.utils.print_info("SSH option is enabled, disabling it")
            self.auto_actions.click(element1)
            self.utils.print_info("SSH option is disabled now")
        else:
            self.utils.print_info("SSH option is disabled, enabling it")
            sleep(5)
            self.auto_actions.click(element1)
            self.utils.print_info("SSH option is enabled now")

    def ssh_page_entries(self, ssh_password):
        """
        - This keyword will enter the values into SSH page tools
        - Keyword Usage
        - ``SSH Page Entries``

        :return: 1 if Navigation Successful to SSH inputs else return -1
        """
        self.utils.print_info("Select Duration")
        ssh_drop = self.weh.get_element(self.select_duration)
        self.auto_actions.click(ssh_drop)
        sleep(5)
        self.utils.print_info("Selected Drop Down")
        self.utils.print_info(ssh_drop)
        drop_options = self.weh.get_elements(self.input_drop_down_options)
        self.auto_actions.select_drop_down_options(drop_options, "5 days")
        sleep(5)
        self.utils.print_info("Enter password")
        ssh_pwd = self.weh.get_element(self.ssh_password)
        ssh_pwd.clear()
        self.auto_actions.send_keys(ssh_pwd, ssh_password)
        sleep(5)
        ssh_save = self.weh.get_element(self.ssh_save_button)
        self.auto_actions.click(ssh_save)
        sleep(5)
        self.utils.print_info("SSH configuration is done")
        return 1

    def select_tech_data(self):
        """
         - This keyword selects Tech data in Tools Page
         - Keyword Usage
          - ``Select Tech Data``

        :return: 1 if Tech data is selected & downloaded successfully else return -1
        """
        self.utils.print_info("Select Tech Data")
        element = self.weh.get_element(self.tech_data_ui)
        self.auto_actions.click(element)
        sleep(5)
        ele1 = self.weh.get_element(self.lite_mode)
        status = ele1.is_selected()
        if status:
            self.utils.print_info("Lite mode is Enabled")
            sleep(5)
            self.utils.print_info("Start Downloading")
            st_button = self.weh.get_element(self.start_button)
            self.auto_actions.click(st_button)
            sleep(15)
            self.utils.print_info("Download the file in Lite Mode")
            download = self.weh.get_element(self.download_button)
            self.auto_actions.click(download)
            sleep(10)
            self.auto_actions.click(ele1)
            self.utils.print_info("lite mode is disabled")
            st_button = self.weh.get_element(self.start_button)
            self.auto_actions.click(st_button)
            sleep(30)
            download = self.weh.get_element(self.download_button)
            self.auto_actions.click(download)
            sleep(30)
            self.utils.print_info("Downloaded in Normal mode")
            sleep(10)
            return 1
        else:
            self.utils.print_info("lite mode is disabled")
            st_button = self.weh.get_element(self.start_button)
            self.auto_actions.click(st_button)
            sleep(30)
            download = self.weh.get_element(self.download_button)
            self.auto_actions.click(download)
            sleep(30)
            self.utils.print_info("Downloaded in Normal mode")
            sleep(10)
            self.utils.print_info("Enable Lite mode")
            self.auto_actions.click(ele1)
            sleep(5)
            self.utils.print_info("Lite mode is Enabled")
            self.utils.print_info("Start Downloading")
            st_button = self.weh.get_element(self.start_button)
            self.auto_actions.click(st_button)
            sleep(30)
            self.utils.print_info("Downloaded the file in Lite Mode")
            download = self.weh.get_element(self.download_button)
            self.auto_actions.click(download)
            sleep(10)
            return -1

    def select_logs(self, search_string):
        """
        - This keyword will select the log in Tools tab
        - Keyword Usage
        - ``Select Logs   ${SEARCH_STRING}``

        :param search_string:  it should be the name of the log file which is searched on the row cell
        :return: row element if row exists else return None
        """
        self.utils.print_info("Getting logs rows")
        if self.auto_actions.click(self.get_log_ui()) == 1:
            sleep(2)
            rows = self.setting.get_logs_grid_rows()

            for row in rows:
                sleep(5)
                if search_string in row.text:
                    self.utils.print_info(f"Found the Expected Row Text")
                    row.click()
                    self.utils.print_info(f"clicked on the selected --  ", search_string)
                    sleep(5)
                    return 1
                else:
                    self.utils.print_info(f"Not found the log file")
                    sleep(5)
                    continue
            return -1
