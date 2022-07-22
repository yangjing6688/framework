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

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class A3WebElementsflow(A3WebElements):
    def __init__(self):
        super().__init__()
        #self.CloudDriver = CloudDriver()
        # self.driver2 = None
        self.driver1 = None
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.a3_web_elements = A3WebElements()
        #self.driver = common.CloudDriver.cloud_driver
        self.setting = GlobalSettingWebElements()
        self.driver = webdriver.Chrome()

    def create_new_conn_profile(self):
        """
        - This keyword will create the connection profile
        - Keyword Usage
        - ``Create New Conn Profile``
        :return: 1 if connection profile is created successfully else return -1
        """
        if self.auto_actions.click(self.select_conn_profile_menu()) == 1:
            sleep(5)
            self.utils.print_info("create a new connection profile ")
            sleep(10)
            self.driver.find_element_by_xpath("//a[contains(@href,'#/configuration/connection_profiles/new')]").click()
            sleep(5)
            self.utils.print_info("profile name ")
            description = self.weh.get_element(self.conn_profile_name)
            self.auto_actions.send_keys(description, "802.1X")
            sleep(10)
            self.utils.print_info("click add filter")
            auth_add_rule = self.weh.get_element(self.add_filter)
            self.auto_actions.click(auth_add_rule)
            sleep(10)
            self.utils.print_info("Select action 1 for row 1")
            self.driver.find_element_by_xpath('//*[@data-automation-tag="automation-filter,0,type"]//input').click()
            sleep(10)
            self.driver.maximize_window()
            drop_options = self.driver.find_elements_by_xpath(
                '//*[@data-automation-tag="automation-filter,0,type"]//span//span')
            self.auto_actions.select_drop_down_options(drop_options, "Connection Type")
            sleep(5)
            self.utils.print_info("Select action 2 for row 1")
            self.driver.find_element_by_xpath('//*[@data-automation-tag="automation-filter,0,match"]//input').click()
            sleep(10)
            drop_options = self.driver.find_elements_by_xpath(
                '//*[@data-automation-tag="automation-filter,0,match"]//span//span')
            self.auto_actions.select_drop_down_options(drop_options, "Wireless-802.11-EAP")
            sleep(5)
            self.utils.print_info("Click on Add Source")
            add_src_btn = self.weh.get_element(self.add_source)
            self.auto_actions.click(add_src_btn)
            sleep(5)
            self.utils.print_info("Select Source")
            self.driver.find_element_by_xpath('//*[@data-automation-tag="automation-sources,0"]//input').click()
            sleep(10)
            drop_options = self.driver.find_elements_by_xpath(
                '//*[@data-automation-tag="automation-sources,0"]//span//span')
            self.auto_actions.select_drop_down_options(drop_options, "AS154")
            sleep(5)
            self.utils.print_info("Created Connection Profile")
            create_conn_profile = self.weh.get_element(self.save_button)
            self.auto_actions.click(create_conn_profile)
            sleep(5)
            self.utils.print_info("Connection Profile is created successfully")
            return 1
        else:
            self.utils.print_info("Connection Profile is not created")
            return -1

    def add_device(self):
        """
        - This keyword will add the device in Device section
        - Keyword Usage
        - ``Add Device``
        :return: 1 if device is been added successfully else return -1
        """
        if self.auto_actions.click(self.select_device_ui()) == 1:
            sleep(5)
            self.utils.print_info("Add a new device ")
            new = self.weh.get_element(self.new_dev_btn)
            self.auto_actions.click(new)
            sleep(5)
            drop_options = self.driver.find_elements_by_xpath('//ul[@class="dropdown-menu show"]/li')
            self.auto_actions.select_drop_down_options(drop_options, "Aerohive_AP")
            sleep(10)
            self.utils.print_info("Select Advanced Mode")
            toggle_mode = self.driver.find_element_by_xpath(
                '//*[@class="base-input-range-label col-form-label text-nowrap mr-2"]').click()
            status = self.driver.find_element_by_xpath(
                '//*[@data-automation-tag="automation-toggle-advanced-mode"]').is_selected()
            sleep(5)
            self.utils.print_info("Enter IP")
            dev_ip = self.weh.get_element(self.device_ip)
            self.auto_actions.send_keys(dev_ip, "10.234.63.13")
            sleep(5)
            self.utils.print_info("Enter Description")
            dev_desc = self.weh.get_element(self.device_description)
            self.auto_actions.send_keys(dev_desc, "AP305C")
            sleep(5)
            self.utils.print_info("Select device type")
            dev_type = self.weh.get_element(self.device_type)
            self.auto_actions.click(dev_type)
            drop_options = self.driver.find_elements_by_xpath(
                '//*[@data-automation-tag="automation-type"]//span//span')
            self.auto_actions.select_drop_down_options(drop_options, "Aerohive AP")
            sleep(5)
            self.utils.print_info("Select Mode")
            dev_mode = self.weh.get_element(self.device_mode)
            self.auto_actions.click(dev_mode)
            drop_options = self.driver.find_elements_by_xpath(
                '//*[@data-automation-tag="automation-mode"]//span//span')
            self.auto_actions.select_drop_down_options(drop_options, "Production")
            sleep(5)
            self.utils.print_info("Select De authentication Method")
            dev_de_auth = self.weh.get_element(self.device_de_auth_method)
            self.auto_actions.click(dev_de_auth)
            drop_options = self.driver.find_elements_by_xpath(
                '//*[@data-automation-tag="automation-deauthMethod"]//span//span')
            self.auto_actions.select_drop_down_options(drop_options, "RADIUS")
            sleep(5)
            #self.utils.print_info("Select Advanced Mode")
            # toggle_mode = self.driver.find_element_by_xpath(
            #     '//*[@class="base-input-range-label col-form-label text-nowrap mr-2"]').click()
            # status = self.driver.find_element_by_xpath(
            #     '//*[@data-automation-tag="automation-toggle-advanced-mode"]').is_selected()
            self.utils.print_info("Configure & create Device")
            create_dev = self.weh.get_element(self.save_button)
            self.auto_actions.click(create_dev)
            sleep(5)
            self.utils.print_info("Save the configuration")
            save_dev = self.weh.get_element(self.save_button)
            self.auto_actions.click(save_dev)
            sleep(10)
            self.utils.print_info("Switch to Device Role")
            dev_roles = self.weh.get_element(self.device_roles)
            self.driver.execute_script("arguments[0].click();", dev_roles)
            #self.auto_actions.click(dev_roles)
            sleep(5)
            self.utils.print_info("Enter the Vlan")
            g_vlan = self.weh.get_element(self.emp_vlan)
            self.auto_actions.send_keys(g_vlan, "10")
            sleep(5)
            self.utils.print_info("Create role with vlan")
            create_role = self.weh.get_element(self.save_button)
            self.auto_actions.click(create_role)
            sleep(15)
            self.utils.print_info("Switch to Radius Tab ")
            radius_input = self.weh.get_element(self.radius_tab)
            self.driver.execute_script("arguments[0].click();", radius_input)
            #self.auto_actions.click(radius_input)
            sleep(5)
            self.utils.print_info("Enter Radius Password")
            radius_pp = self.weh.get_element(self.radius_SC)
            self.auto_actions.send_keys(radius_pp, "aerohive")
            sleep(5)
            self.utils.print_info("Save the configuration")
            save_radius_pp = self.weh.get_element(self.save_button)
            self.auto_actions.click(save_radius_pp)
            sleep(5)
            self.utils.print_info("Device is created successfully")
            sleep(5)
            return 1
        else:
            self.utils.print_info("Device is not created")
            return -1

    def select_radius_audit_logs(self, mac, auth_status, user_name):
        """
        - This keyword will validate the authentication with A3 in Auditing tab by selecting the auditing details
        - Keyword Usage
        - ``Select Radius Audit Logs mac auth_status client_status``
        :param mac:  it should be mac address of the client
        :param auth_status:  it should be authentication status of the client ex: Accept/Reject
        :param user_name:  it should be the user name ex: ad or mac id
        :return: 1 if Authentication is done successfully else -1
        """
        if self.auto_actions.click(self.get_radius_audit_log_ui()) == 1:
            sleep(2)
            self.utils.print_info(f"select the table")
            tab = self.weh.get_element(self.get_table)
            sleep(2)
            self.utils.print_info(f"select the table1")
            table = self.setting.get_audit_logs_grid_rows()
            self.utils.print_info(f"select the table2")
            ele_selected = tab.is_displayed
            self.utils.print_info(f"print status", ele_selected)
            sleep(5)
            if ele_selected:
                for rows in table:
                    for row in rows.text.splitlines():
                        if mac in row \
                            and auth_status in row \
                                and user_name in row:
                            self.utils.print_info(f"Found the Expected Row Text", row)
                            self.utils.print_info(f"clicked on the selected row")
                            sleep(5)
                            rows.click()
                            break
            rad_tab = self.weh.get_element(self.rad_entry_tab)
            self.auto_actions.click(rad_tab)
            radius_ent_info = self.weh.get_element(self.rad_ent_info)
            radius_open_info = self.weh.get_element(self.rad_open_info)
            sleep(5)
            if radius_ent_info:
                self.utils.print_info(f"Enterprise Authentication done successfully")
            elif radius_open_info:
                self.utils.print_info(f"Open Network Authentication done successfully")
            else:
                self.utils.print_info(f" Not Authenticated")
                return -1
            sleep(5)

        return 1

    def select_clients_search(self, mac, client_status, owner):
        """
        - This keyword will validate the authentication with A3 in clients tab by selecting the client details
        - Keyword Usage
        - ``Select Clients Search mac owner ``
        :param mac:  it should be mac address of the client
        :param client_status:  it should be the client connection status ex: online/offline - on /unknown
        :param owner:  it should be the user name ex: ad or default
        :return: 1 if Authentication is done successfully else -1
        """
        if self.auto_actions.click(self.get_clients_search_ui()) == 1:
            sleep(5)
            self.utils.print_info(f"select the table")
            sleep(10)
            table = self.setting.get_clients_search_rows()
            for rows in table:
                for row in rows.text.splitlines():
                    if mac in row \
                        and client_status in row \
                            and owner in row:
                        self.utils.print_info(f"Found the Expected Row Text", row)
                        self.utils.print_info(f"clicked on the selected row")
                        sleep(5)
                        rows.click()
                        break
            info_tab = self.weh.get_element(self.client_info_tab)
            self.auto_actions.click(info_tab)
            client_ent = self.weh.get_element(self.client_ent_info)
            client_open = self.weh.get_element(self.client_open_info)
            if client_ent:
                self.utils.print_info(f"Enterprise Authentication done successfully")
            elif client_open:
                self.utils.print_info(f"Open Network Authentication done successfully")
            else:
                self.utils.print_info(f" Not Authenticated")
                return -1
            sleep(5)

        return 1

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
        # driver = webdriver.Chrome()
        # self.driver.implicitly_wait(10)
        element = self.weh.get_element(self.ssh_option_ui)
        self.auto_actions.click(element)
        sleep(5)

        #ele1 = self.driver.find_element_by_name("check-button")
        element1 = self.weh.get_element(self.ssh_selector)
        status = self.driver.find_element_by_name("check-button").is_selected()
        # ele2 = self.driver.find_element_by_class_name("custom-control-label")
        # status = self.driver.find_element_by_class_name("custom-control-label").is_selected()
        self.utils.print_info(status)
        # wait_for = WebDriverWait(self.driver, 5)
        # xypath = "/html/body/div/div[2]/div[2]/div/div[2]/div/div/div/form/div[3]/div/div/label"
        # wait_for.until(EC.element_to_be_clickable((By.XPATH, xypath)))
        # invisible = wait_for.until(EC.invisibility_of_element_located((By.XPATH, xypath)))
        # self.utils.print_info(type(invisible))
        if status:
            self.utils.print_info("SSH option is enabled, disabling it")
            self.driver.execute_script("arguments[0].click();", ele1)
        else:
            self.utils.print_info("SSH option is disabled, enabling it")
            self.driver.execute_script("arguments[0].click();", ele1)

            # self.driver.execute_script(document.getElementsByName('check-button')[0].click())
            # self.auto_actions.click(ele1)
            # self.driver.find_element_by_name("check-button").click()

    def select_cloud_integration(self):
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
            self.auto_actions.send_keys(element1, 'https://gcp1.qa.xcloudiq.com')
            sleep(5)
            element2 = self.weh.get_element(self.cloud_admin)
            self.auto_actions.send_keys(element2, "testrach17+gcp1r1acc@gmail.com")
            sleep(5)
            element3 = self.weh.get_element(self.cloud_password)
            self.auto_actions.send_keys(element3, "Aerohive123")
            sleep(5)
            element4 = self.weh.get_element(self.cloud_link_button)
            element4.click()
            #self.auto_actions.click(element4)
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
        # self.utils.print_info(type(ssh_drop))
        drop_options = self.weh.get_elements(self.input_drop_down_options)
        # self.utils.print_info(drop_options)
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
        # status = self.driver.find_element_by_name("check-button")
        # self.utils.print_info(status)
        self.utils.print_info("Enable Lite mode")
        self.driver.execute_script("arguments[0].click();", ele1)
        sleep(5)
        self.utils.print_info("Start Downloading")
        st_button = self.weh.get_element(self.start_button)
        self.auto_actions.click(st_button)
        sleep(15)
        self.utils.print_info("Download the file in Lite Mode")
        download = self.weh.get_element(self.download_button)
        self.auto_actions.click(download)
        sleep(10)
        # done = self.weh.get_element(self.done_button)
        # self.auto_actions.click(done)
        # sleep(5)
        status = self.driver.find_element_by_name("check-button").is_selected()
        ele1 = self.weh.get_element(self.lite_mode)
        self.utils.print_info(status)
        sleep(10)

        if status:
            self.utils.print_info("lite mode is enabled")
            self.driver.execute_script("arguments[0].click();", ele1)
            sleep(10)
            self.utils.print_info("lite mode is disabled")
            st_button = self.weh.get_element(self.start_button)
            self.auto_actions.click(st_button)
            sleep(30)
            download = self.weh.get_element(self.download_button)
            self.auto_actions.click(download)
            sleep(30)
            # done = self.weh.get_element(self.done_button)
            # self.auto_actions.click(done)
            # sleep(5)
            self.utils.print_info("Downloaded in Normal mode")
            sleep(10)
            return 1
        else:
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
