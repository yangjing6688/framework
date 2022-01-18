from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementListUtils import NetworkElementListUtils
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementHealthCheck import NetworkElementHealthCheck


class HealthCheckUdks():
    def __init__(self):
        self.networkElementListUtils = NetworkElementListUtils()
        self.networkElementHealthCheck = NetworkElementHealthCheck()

    def Store_Health_Check_for_Suite_Setup(self):
        netelem_list = self.networkElementListUtils.create_list_of_network_element_names()
        self.networkElementHealthCheck.store_current_corefile_list(netelem_list)
        self.networkElementHealthCheck.store_current_boot_date(netelem_list)

    def Health_Check_for_All_Attributes(self):
        netelem_list = self.networkElementListUtils.create_list_of_network_element_names()
        self.networkElementHealthCheck.check_system_cpu_usage(netelem_list)
        self.networkElementHealthCheck.compare_and_store_boot_date(netelem_list)
        self.networkElementHealthCheck.compare_and_store_corefiles(netelem_list)

    def Health_Check_for_Boot_Date_and_Cores(self):
        netelem_list = self.networkElementListUtils.create_list_of_network_element_names()
        self.networkElementHealthCheck.compare_and_store_boot_date(netelem_list)
        self.networkElementHealthCheck.compare_and_store_corefiles(netelem_list)
        