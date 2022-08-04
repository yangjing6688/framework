import re
import os

import copy
from time import sleep
from datetime import datetime
import datetime as dt
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from robot.libraries.BuiltIn import BuiltIn
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
        self.login = Login()
        self.cli = Cli()
        self.licenseManagement = LicenseManagement()

    def configure_a3_to_xiq_instance(self, check_version_value=None, **kwargs):
        """
        - Configure A3 To Xiq Instance
        - Keyword Usage:
        - ``Configure A3 To Xiq Instance``

        :return: 1 if the connection is closed.  Note: an error will be raised if the connection fails to close
        """
        # check xiq version steps 1-2
        xiq_version = self.login._capture_xiq_version()
        if check_version_value:
            if xiq_version != check_version_value:
                kwargs['fail_msg'] = "XIQ Version is " + xiq_version + " does not equal expected version " + check_version_value
                self.common_validation.validate(-1, 1, **kwargs)
                return -1
        # navigate to License Management page step 3
        self.licenseManagement.open_license_management_page()

        # get_link_to_extr_portal_btn
        #  Select "Link My Extreme Portal account " and provide customer account - a3extremeqa+directcust005@gmail.com/Extreme@123 step 4
        link_portal_button = self.licenseManagement.lic_mgt_web_elements.get_link_to_extr_portal_btn()
        if not link_portal_button:
            kwargs['fail_msg'] = "Unable to locate Link My Extreme Portal Account button"
            self.common_validation.validate(-1, 1, **kwargs)
            return -1
        self.auto_actions.click(link_portal_button)



        return 1
