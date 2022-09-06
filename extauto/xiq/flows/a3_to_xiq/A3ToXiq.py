import re
import os

import copy
from time import sleep
from datetime import datetime
import datetime as dt
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from robot.libraries.BuiltIn import BuiltIn

import a3.flows.common.Login
import xiq.flows.common.Login
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.Cli import Cli
from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.flows.common.DeviceCommon import DeviceCommon
from extauto.xiq.flows.common.Login import Login
from extauto.xiq.elements.SwitchTemplateWebElements import SwitchTemplateWebElements

from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.elements.DialogWebElements import DialogWebElements
from extauto.xiq.elements.DeviceActions import DeviceActions
from extauto.xiq.elements.DeviceUpdate import DeviceUpdate
from extauto.xiq.elements.SwitchWebElements import SwitchWebElements
from extauto.common.Cli import Cli
from extauto.common.CommonValidation import CommonValidation
from extauto.xiq.flows.globalsettings.LicenseManagement import LicenseManagement
from extauto.a3.flows.common.Login import Login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from extauto.common.CloudDriver import CloudDriver

class A3ToXiq:
    def __init__(self):
        self.utils = Utils()
        self.common_validation = CommonValidation()
        self.auto_actions = AutoActions()
        self.devices_web_elements = DevicesWebElements()
        self.dialogue_web_elements = DialogWebElements()
        self.switch_web_elements = SwitchWebElements()
        self.sw_template_web_elements = SwitchTemplateWebElements()
        self.common_validation = CommonValidation()
        self.navigator = Navigator()
        self.device_actions = DeviceActions()
        self.device_update = DeviceUpdate()
        self.device_common = DeviceCommon()
        self.cli = Cli()
        self.screen = Screen()
        self.robot_built_in = BuiltIn()
        self.custom_file_dir = os.getcwd() + '/onboard_csv_files/'
        self.login = xiq.flows.common.Login.Login()
        self.cli = Cli()
        self.licenseManagement = LicenseManagement()
        self.a3login = a3.flows.common.Login.Login()
        self.driver = CloudDriver().cloud_driver

    def configure_a3_to_xiq_instance(self,  portal_username='username', portal_password='password123', a3website='website',
                                     a3_username='username', a3_password='password', check_version_value=None, **kwargs):
        """
        - Configure A3 To Xiq Instance
        - Keyword Usage:
        - ``Configure A3 To Xiq Instance``

        :return: 1 if the connection is closed.  Note: an error will be raised if the connection fails to close
        """

        xiq_version = self.login._capture_xiq_version()
        if check_version_value:
            if xiq_version != check_version_value:
                kwargs['fail_msg'] = "XIQ Version is " + xiq_version + " does not equal expected version " + check_version_value
                self.common_validation.validate(-1, 1, **kwargs)
                return -1

        self.licenseManagement.open_license_management_page()

        link_portal_button = self.licenseManagement.lic_mgt_web_elements.get_link_to_extr_portal_btn()
        if not link_portal_button:
            kwargs['fail_msg'] = "Unable to locate Link My Extreme Portal Account button"
            self.common_validation.validate(-1, 1, **kwargs)
            return -1
        self.auto_actions.click(link_portal_button)

        portal_login_successful = self.licenseManagement.link_to_extreme_portal(portal_username, portal_password)
        if portal_login_successful == -1:
            kwargs['fail_msg'] = "Unable to log into Extreme Portal"
            self.common_validation.validate(-1, 1, **kwargs)
            return -1

        # go back to license management page and check for linked status
        WebDriverWait(self.driver, 60).until(
            ec.presence_of_element_located(
                (By.XPATH, "//*[@data-automation-tag='automation-sider-list-licenseMng']")))

        self.utils.print_info("Returning to License Management Page to check link status")
        self.licenseManagement.open_license_management_page()

        unlink_extreme_portal_btn = self.licenseManagement.get_unlink_xiq_from_extr_portal_btn()
        link_message = self.licenseManagement.get_account_successfully_linked()
        if not unlink_extreme_portal_btn or not link_message:
            kwargs['fail_msg'] = "Unable to verify that web page show linked to Extreme Portal"
            self.common_validation.validate(-1, 1, **kwargs)
            return -1
        status_unlink_extreme_portal_btn = unlink_extreme_portal_btn.get_attribute("class")
        status_link_message = link_message.get_attribute("class")
        if 'hidden' not in status_unlink_extreme_portal_btn and 'hidden' not in status_link_message:
            self.utils.print_info("Successfully linked to customer account")
        else:
            kwargs['fail_msg'] = "Status does NOT show successfully linked to customer account"
            self.common_validation.validate(-1, 1, **kwargs)
            return -1
        # log into a3
        a3_login_success = self.a3login.login_a3_user(a3_username, a3_password, url=a3website)

        return 1
