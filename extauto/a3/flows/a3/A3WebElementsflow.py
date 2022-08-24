from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions

from common.AutoActions import *
from a3.elements.A3WebElements import A3WebElements
from a3.elements.GlobalSettingWebElements import *
from a3.defs.GlobalSettingWebElementDefinitions import GlobalSettingWebElementDefinitions
from xiq.flows.common.DeviceCommon import DeviceCommon
from common.CloudDriver import *
from selenium.webdriver.common.by import By
from selenium import webdriver
import re


class A3WebElementsflow(A3WebElements):
    def __init__(self):
        super().__init__()
        self.driver1 = None
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.a3_web_elements = A3WebElements()
        self.setting = GlobalSettingWebElements()
        self.driver = webdriver.Chrome()

    # def select_radius_audit_logs(self, mac, auth_status, user_name):
    #     """
    #     - This keyword will validate the authentication with A3 in Auditing tab by selecting the auditing details
    #     - Keyword Usage
    #     - ``Select Radius Audit Logs mac auth_status client_status``
    #     :param mac:  it should be mac address of the client
    #     :param auth_status:  it should be authentication status of the client ex: Accept/Reject
    #     :param user_name:  it should be the user name ex: ad or mac id
    #     :return: 1 if Authentication is done successfully else -1
    #     """
    #     if self.auto_actions.click(self.get_radius_audit_log_ui()) == 1:
    #         sleep(2)
    #         self.utils.print_info(f"select the table")
    #         tab = self.weh.get_element(self.get_table)
    #         sleep(2)
    #         self.utils.print_info(f"select the table1")
    #         table = self.setting.get_audit_logs_grid_rows()
    #         self.utils.print_info(f"select the table2")
    #         ele_selected = tab.is_displayed
    #         self.utils.print_info(f"print status", ele_selected)
    #         sleep(5)
    #         if ele_selected:
    #             for rows in table:
    #                 for row in rows.text.splitlines():
    #                     if mac in row \
    #                         and auth_status in row \
    #                             and user_name in row:
    #                         self.utils.print_info(f"Found the Expected Row Text", row)
    #                         self.utils.print_info(f"clicked on the selected row")
    #                         sleep(5)
    #                         rows.click()
    #                         break
    #         rad_tab = self.weh.get_element(self.rad_entry_tab)
    #         self.auto_actions.click(rad_tab)
    #         radius_ent_info = self.weh.get_element(self.rad_ent_info)
    #         radius_open_info = self.weh.get_element(self.rad_open_info)
    #         sleep(5)
    #         if radius_ent_info:
    #             self.utils.print_info(f"Enterprise Authentication done successfully")
    #         elif radius_open_info:
    #             self.utils.print_info(f"Open Network Authentication done successfully")
    #         else:
    #             self.utils.print_info(f" Not Authenticated")
    #             return -1
    #         sleep(5)
    #
    #     return 1
    #
    # def select_clients_search(self, mac, client_status, owner):
    #     """
    #     - This keyword will validate the authentication with A3 in clients tab by selecting the client details
    #     - Keyword Usage
    #     - ``Select Clients Search mac owner ``
    #     :param mac:  it should be mac address of the client
    #     :param client_status:  it should be the client connection status ex: online/offline - on /unknown
    #     :param owner:  it should be the user name ex: ad or default
    #     :return: 1 if Authentication is done successfully else -1
    #     """
    #     if self.auto_actions.click(self.get_clients_search_ui()) == 1:
    #         sleep(5)
    #         self.utils.print_info(f"select the table")
    #         sleep(10)
    #         table = self.setting.get_clients_search_rows()
    #         for rows in table:
    #             for row in rows.text.splitlines():
    #                 if mac in row \
    #                     and client_status in row \
    #                         and owner in row:
    #                     self.utils.print_info(f"Found the Expected Row Text", row)
    #                     self.utils.print_info(f"clicked on the selected row")
    #                     sleep(5)
    #                     rows.click()
    #                     break
    #         info_tab = self.weh.get_element(self.client_info_tab)
    #         self.auto_actions.click(info_tab)
    #         client_ent = self.weh.get_element(self.client_ent_info)
    #         client_open = self.weh.get_element(self.client_open_info)
    #         if client_ent:
    #             self.utils.print_info(f"Enterprise Authentication done successfully")
    #         elif client_open:
    #             self.utils.print_info(f"Open Network Authentication done successfully")
    #         else:
    #             self.utils.print_info(f" Not Authenticated")
    #             return -1
    #         sleep(5)
    #
    #     return 1

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

    def select_cloud_integration(self, cloud_url, cloud_uname, cloud_pwd):
        """
            - This keyword select the Cloud Integration from the menu System Configuration ank link it to XIQ
            - Keyword Usage
             - ``Select cloud integration``

        :return: 1 if Navigation Successful to Cloud Integration else return -1
        """
        self.utils.print_info("Selecting Cloud Integration from menu...")

        if self.auto_actions.click(self.get_cloud()) == 1:
            sleep(2)
            self.utils.print_info("Entering Cloud account details ")
            element1 = self.weh.get_element(self.cloud_host_input)
            element1.clear()
            self.auto_actions.send_keys(element1, cloud_url)
            sleep(5)
            element2 = self.weh.get_element(self.cloud_admin)
            self.auto_actions.send_keys(element2, cloud_uname)
            sleep(5)
            element3 = self.weh.get_element(self.cloud_password)
            self.auto_actions.send_keys(element3, cloud_pwd)
            sleep(5)
            element4 = self.weh.get_element(self.cloud_link_button)
            self.auto_actions.click(element4)
            sleep(20)
            self.driver.get(self.driver.current_url)
            sleep(3)
            self.driver.refresh()
            sleep(10)
            self.utils.print_info("Unlinking from cloud ")
            element5 = self.weh.get_element(self.cloud_unlink_button)
            self.auto_actions.click(element5)
            sleep(10)
            self.utils.print_info("XIQ cloud linking & Unlinking is successfully done")
            sleep(5)
            return 1
        else:
            self.utils.print_info("Unable to perform Linking & unlinking to XIQ")
            self.screen.save_screen_shot()
            return -1

    def ssh_button(self):

        """
            - This keyword select the SSH checkbox and click it
            - Keyword Usage
             - ``Select SSH Checkbox``

        :return: 1 if Navigation Successful to SSH checkbox else return -1
        """

        # self.auto_actions.enable_check_box(self.get_ssh_button())
        # self.utils.print_info("Selecting Enable SSH label...")
        # ssh_btn = self.weh.get_element(self.ssh_selector)
        self.driver.find_element_by_name("check-button").click()

        # self.auto_actions.click(self.a3_web_elements.get_ssh_button())
        # ssh_btn = self.weh.get_element(self.ssh_selector)
        # ssh_btn.click()
        # self.getElementsByName('check-button')[0].click()
        # abc.click()

        # self.auto_actions.move_to_element(ssh_btn)

        # self.auto_actions.enable_check_box(ssh_btn)
        # self.utils.print_info("selected the option finally")

        # self.auto_actions.click(ssh_btn)
        sleep(10)
        return 1

    def ssh_page_entries(self):
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
        self.auto_actions.send_keys(ssh_pwd, "Extr123")
        sleep(5)
        ssh_save = self.weh.get_element(self.ssh_save_button)
        self.auto_actions.click(ssh_save)
        sleep(5)
        self.utils.print_info("SSH configuration is done")
        return 1

    def backup_file(self):
        """
            - This keyword will take the backup
            - Keyword Usage
             - ``Backup File``

        :return: 1 if Backup created successfully else return -1
        """
        self.utils.print_info("Selecting Backup from menu...")
        if self.auto_actions.click(self.get_backup()) == 1:
            sleep(5)
            self.utils.print_info("Click Backup ")
            element = self.weh.get_element(self.backup_save_config)
            self.auto_actions.click(element)
            sleep(5)
            self.utils.print_info("Enter the name of backup file")
            element8 = self.weh.get_element(self.backup_description)
            self.auto_actions.send_keys(element8, "bkup2")
            sleep(5)
            self.utils.print_info("Saving backup")
            element9 = self.weh.get_element(self.backup_save)
            self.auto_actions.click(element9)
            sleep(10)
            self.utils.print_info("Backup Created successfully")
            return 1
        else:
            self.utils.print_info("Unable to create Backup")
            self.screen.save_screen_shot()
            return -1

    def validate_backup_created(self, search_string):
        """
        - This keyword will validate the creation of the backup file
        - Keyword Usage
         - ``Validate Backup Created   ${SEARCH_STRING}``

        :param search_string:  it should be the file name of the backup which is searched on the row cell

        :return: row element if row exists else return None
        """
        self.utils.print_info("Getting Backup Table")
        if self.auto_actions.click(self.get_backup()) == 1:
            sleep(5)
            rows = self.setting.get_backup_logs_grid_rows()
            # self.auto_actions.click(rows)
            # self.utils.print_info("rows value",rows)

            #   rows = self.driver.find_elements_by_css_selector("div.pf-table-sortable.hover.striped")
            # self.utils.print_info("rows value", rows)
            # if not rows:
            #    self.utils.print_info("Authentication Logs rows are not available in the page")
            # return False
            # for row in rows:
            #    self.utils.print_info(row)
            # if search_string in row.text:
            #    self.utils.print_info("entry is present")
            #    return row
            for row in rows:
                sleep(5)
                if search_string in row.text:
                    # self.utils.print_info(f"row", row.text)
                    self.utils.print_info(f"Found the Expected Row Text , Backup is created successfully")
                    return 1
                else:
                    self.utils.print_info(f"Not found bkup row ")
                    return -1

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
