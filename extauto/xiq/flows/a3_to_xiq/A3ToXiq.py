import os
from time import sleep

from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from extauto.common.AutoActions import AutoActions
from extauto.common.Cli import Cli
from extauto.common.CloudDriver import CloudDriver
from extauto.common.CommonValidation import CommonValidation
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.a3.flows.a3.CIWebElementsFlow import CIWebElementsFlow as A3CIWebElementsFlow
from extauto.a3.flows.a3.LicenseManagementFlow import LicenseManagementFlow as A3LicenseManagementFlow
from extauto.a3.flows.common.Login import Login as A3Login
from extauto.a3.flows.common.Navigator import Navigator as A3Navigator
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.flows.common.DeviceCommon import DeviceCommon
from extauto.xiq.flows.common.Login import Login as CommonLogin
from extauto.xiq.elements.SwitchTemplateWebElements import SwitchTemplateWebElements
from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
from extauto.xiq.elements.DialogWebElements import DialogWebElements
from extauto.xiq.elements.DeviceActions import DeviceActions
from extauto.xiq.elements.DeviceUpdate import DeviceUpdate
from extauto.xiq.elements.SwitchWebElements import SwitchWebElements
from extauto.xiq.flows.globalsettings.LicenseManagement import LicenseManagement


class A3ToXiq:
    def __init__(self):
        self.utils = Utils()
        self.common_validation = CommonValidation()
        self.auto_actions = AutoActions()
        self.devices_web_elements = DevicesWebElements()
        self.dialogue_web_elements = DialogWebElements()
        self.switch_web_elements = SwitchWebElements()
        self.sw_template_web_elements = SwitchTemplateWebElements()
        self.navigator = Navigator()
        self.device_actions = DeviceActions()
        self.device_update = DeviceUpdate()
        self.device_common = DeviceCommon()
        self.cli = Cli()
        self.screen = Screen()
        self.robot_built_in = BuiltIn()
        self.custom_file_dir = os.getcwd() + '/onboard_csv_files/'
        self.login = CommonLogin()
        self.cli = Cli()
        self.licenseManagement = LicenseManagement()
        self.a3login = A3Login()
        self.a3_navigator = A3Navigator()
        self.a3_license_management = A3LicenseManagementFlow()
        self.a3_cloud_web_flow = A3CIWebElementsFlow()
        self.driver = None

    def configure_a3_to_xiq_instance(self, xiq_username='', xiq_password='', xiq_website='', portal_username='',
                                     portal_password='', a3website='', a3_username='', a3_password='',
                                     check_version_value=None, confirm_cluster_id=False, **kwargs):
        """
        - Configure A3 To Xiq Instance
        - Keyword Usage:
        - ``Configure A3 To Xiq Instance``

        :param xiq_username: Username to log into XIQ
        :param xiq_password: Password to log into XIQ
        :param xiq_website:  XIQ website to use
        :param portal_username: Username to use to link to Extreme Portal
        :param portal_password: Password to use to link to Extreme Portal
        :param a3website: A3 website to link to XIQ
        :param a3_username: Username to log into A3
        :param a3_password: Password to log into A3
        :param check_version_value: Used to determine if version should be checked
        :param confirm_cluster_id: Used to determine if A3 has valid cluster id (successfully linked)

        :return: 1 if the connection is closed.  Note: an error will be raised if the connection fails to close
        """

        self.login.login_user(xiq_username, xiq_password, url=xiq_website)

        self.driver = CloudDriver().cloud_driver

        xiq_version = self.login.get_xiq_version()
        if check_version_value:
            if xiq_version != check_version_value:
                kwargs[
                    'fail_msg'] = "configure_a3_to_xiq_instance() failed." \
                                  "XIQ Version is " + xiq_version + " does not equal expected version " + check_version_value
                self.common_validation.failed(**kwargs)
                return -1

        self.licenseManagement.open_license_management_page()

        link_portal_button = self.licenseManagement.lic_mgt_web_elements.get_link_to_extr_portal_btn()
        if not link_portal_button:
            kwargs['fail_msg'] = "configure_a3_to_xiq_instance() failed. " \
                                 "Unable to locate Link My Extreme Portal Account button"
            self.common_validation.fault(**kwargs)
            return -1
        self.auto_actions.click(link_portal_button)

        portal_login_successful = self.licenseManagement.link_to_extreme_portal(portal_username, portal_password)
        if portal_login_successful == -1:
            kwargs['fail_msg'] = "configure_a3_to_xiq_instance() failed. Unable to log into Extreme Portal"
            self.common_validation.fault(**kwargs)
            return -1

        # go back to license management page and check for linked status
        WebDriverWait(self.driver, 120).until(
            ec.presence_of_element_located(
                (By.XPATH, "//*[@data-automation-tag='automation-sider-list-licenseMng']")))

        self.utils.print_info("Returning to License Management Page to check link status")
        self.licenseManagement.open_license_management_page()
        sleep(5)

        unlink_extreme_portal_btn = self.licenseManagement.get_unlink_xiq_from_extr_portal_btn()
        link_message = self.licenseManagement.get_account_successfully_linked()
        if not unlink_extreme_portal_btn or not link_message:
            kwargs['fail_msg'] = "configure_a3_to_xiq_instance() failed. " \
                                 "Unable to verify that web page show linked to Extreme Portal"
            self.common_validation.failed(**kwargs)
            return -1

        status_unlink_extreme_portal_btn = unlink_extreme_portal_btn.get_attribute("class")
        status_link_message = link_message.get_attribute("class")
        if 'hidden' not in status_unlink_extreme_portal_btn and 'hidden' not in status_link_message:
            self.utils.print_info("Successfully linked to customer account")
        else:
            kwargs['fail_msg'] = "configure_a3_to_xiq_instance() failed. " \
                                 "Status does NOT show successfully linked to customer account"
            self.common_validation.failed(**kwargs)
            return -1

        self.login.logout_user()
        self.login.quit_browser()

        if a3_username and a3website:
            # log into a3
            a3_login_success = self.a3login.login_a3_user(a3_username, a3_password, url=a3website)
            if a3_login_success == -1:
                kwargs['fail_msg'] = "configure_a3_to_xiq_instance() failed. Unable to log into A3 Server"
                self.common_validation.fault(**kwargs)
                return -1
            if confirm_cluster_id:
                self.a3_navigator.navigate_to_license_management_page()
                cluster_id = self.a3_license_management.get_a3_cluster_id()
                if cluster_id == -1:
                    kwargs['fail_msg'] = "configure_a3_to_xiq_instance() failed. Invalid value for Cluster Id"
                    self.common_validation.fault(**kwargs)
                    return -1
            else:
                self.a3_navigator.navigate_to_cloud_integration_page()
                self.a3_cloud_web_flow.a3_link_with_extreme_cloud_iq_account(a3website, a3_username, a3_password)
            self.a3login.logout_a3_user()
            self.a3login.quit_browser()

        kwargs['pass_msg'] = "Successfully able to Configure A3 To Xiq Instance"
        self.common_validation.passed(**kwargs)
        return 1
