from common.AutoActions import *
from a3.elements.DeviceWebElements import DeviceWebElements
from a3.elements.GlobalSettingWebElements import *
from xiq.flows.common.DeviceCommon import DeviceCommon
from common.CloudDriver import *


class DeviceWebElementsFlow(DeviceWebElements):
    def __init__(self):
        super().__init__()
        # self.CloudDriver = CloudDriver()
        # self.driver2 = None
        self.driver1 = None
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.Device_web_elements = DeviceWebElements()
        #self.driver = common.CloudDriver.cloud_driver
        self.setting = GlobalSettingWebElements()

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