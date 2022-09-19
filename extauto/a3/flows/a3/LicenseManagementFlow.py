from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import *
from a3.elements.LicenseManagementElements import LicenseManagementElements
from a3.elements.GlobalSettingWebElements import *
from xiq.flows.common.DeviceCommon import DeviceCommon
from common.CloudDriver import *
from selenium import webdriver
from extauto.common.CommonValidation import CommonValidation

class LicenseManagementFlow(LicenseManagementElements):
    def __init__(self):
        super().__init__()
        self.driver1 = None
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.driver = webdriver.Chrome()
        self.common_validation = CommonValidation()

    def get_a3_cluster_id(self, **kwargs):
        """
            - This keyword will get get the a3 cluster id
            - Keyword Usage
             - ``Get A3 Cluster Id``

        :return: cluster id value if successfully else return -1
        """
        self.utils.print_info("Getting a3 cluster id...")

        self.utils.print_info("Attempting to locate Cluster Id on the  License Management Page")
        cluster_id_element = self.get_cluster_id()
        if not cluster_id_element:
            kwargs['fail_msg'] = "Unable to locate Cluster Id Element"
            self.common_validation.validate(-1, 1, **kwargs)
            return -1
        cluster_id_value = cluster_id_element.text.strip()
        self.utils.print_info("Cluster ID value is " + cluster_id_value)

        kwargs['pass_msg'] = "Successfully able to A3 Cluster Id"
        self.common_validation.passed(**kwargs)
        return cluster_id_value

    def get_a3_system_id(self, **kwargs):
        """
            - This keyword will get get the a3 system id
            Keyword assumes that system is already on the License Management Page
            - Keyword Usage
             - ``Get A3 System Id``

        :return: system id value if successfully else return -1
        """
        self.utils.print_info("Getting a3 system id...")

        self.utils.print_info("Attempting to locate System Id on the  License Management Page")
        system_id_element = self.get_system_id()
        if not system_id_element:
            kwargs['fail_msg'] = "Unable to locate System Id Element"
            self.common_validation.validate(-1, 1, **kwargs)
            return -1
        system_id_element_value = system_id_element.text.strip()

        kwargs['pass_msg'] = "Successfully able to A3 System Id"
        self.common_validation.passed(**kwargs)
        return system_id_element_value
