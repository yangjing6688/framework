from time import sleep

from selenium import webdriver

from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from a3.elements.A3WebElements import A3WebElements
from a3.elements.GlobalSettingWebElements import GlobalSettingWebElements
from xiq.flows.common.DeviceCommon import DeviceCommon


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

    def backup_file(self):
        """
            - This keyword will take the backup
            - Keyword Usage
             - ``Backup File``

        :return: 1 if Backup created successfully else return -1
        """
        self.utils.print_info("Selecting Backup from menu...")
        if self.auto_actions.click_reference(self.get_backup) == 1:
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
        if self.auto_actions.click_reference(self.get_backup) == 1:
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
                    # self.utils.print_info("row", row.text)
                    self.utils.print_info("Found the Expected Row Text , Backup is created successfully")
                    return 1
                else:
                    self.utils.print_info("Not found bkup row ")
                    return -1
