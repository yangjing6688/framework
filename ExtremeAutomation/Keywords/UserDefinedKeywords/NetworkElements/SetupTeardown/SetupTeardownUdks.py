
from ExtremeAutomation.Keywords.NetworkElementKeywords.StaticKeywords.NetworkElementFileManagementUtilsKeywords import NetworkElementFileManagementUtilsKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPortKeywords import TrafficPortKeywords
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficGeneratorConnectionManager import TrafficGeneratorConnectionManager
from ExtremeAutomation.Keywords.NetworkElementKeywords.NetworkElementConnectionManager import NetworkElementConnectionManager
from ExtremeAutomation.Keywords.UserDefinedKeywords.NetworkElements.HostServices.HealthCheckUdks import HealthCheckUdks
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementListUtils import NetworkElementListUtils
from ExtremeAutomation.Keywords.NetworkElementKeywords.StaticKeywords.NetworkElementResetDeviceUtilsKeywords import NetworkElementResetDeviceUtilsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.StaticKeywords.NetworkElementFirmwareUtilsKeywords import NetworkElementFirmwareUtilsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementHealthCheck import NetworkElementHealthCheck
from ExtremeAutomation.Keywords.EndsystemKeywords.EndsystemConnectionManager import EndsystemConnectionManager

from pytest_testconfig import config
from ExtremeAutomation.Imports.pytestConfigHelper import PytestConfigHelper

class SetupTeardownUdks():
    def __init__(self) -> None:
        self.healthCheckUdks = HealthCheckUdks()
        self.networkElementListUtils = NetworkElementListUtils()
        self.networkElementConnectionManager = NetworkElementConnectionManager()

        self.trafficGeneratorConnectionManager = TrafficGeneratorConnectionManager()
        self.trafficPortKeywords = TrafficPortKeywords()
        self.networkElementFileManagementKeywords = NetworkElementFileManagementUtilsKeywords()
        self.networkElementResetDeviceUtilsKeywords = NetworkElementResetDeviceUtilsKeywords()
        self.endsystemConnectionManager = EndsystemConnectionManager();

    ########################################################
    ##############  Suite_Setup_Keywords  ##################
    ########################################################
    def Base_Test_Suite_Setup(self, baseline=False,**kwargs):
        all_tgen_ports = self.networkElementListUtils.create_list_of_all_tgen_ports()
        self.networkElementConnectionManager.connect_to_all_network_elements()
        self.endsystemConnectionManager.connect_to_all_endsystem_elements()
        self.trafficGeneratorConnectionManager.connect_to_all_traffic_generators()
        self.trafficPortKeywords.take_port_ownership(all_tgen_ports)
        try:
            self.Get_Base_Test_Suite_Platform_Values()
        except:
            pass
        # if baseline is True:
            # self.Suite_Setup_Baseline()
    #    Store_Health_Check_for_Suite_Setup

    def Unit_Test_Suite_Setup(self, **kwargs):
        """  Used_only_for_unit_level_test_cases """
        self.networkElementConnectionManager.connect_to_all_network_elements()
        self.trafficGeneratorConnectionManager.connect_to_all_traffic_generators()

    #######################################################
    ##############  Suite_Cleanup_Keywords  ###############
    #######################################################
    def Base_Test_Suite_Cleanup(self, **kwargs):
        self.networkElementConnectionManager.close_connection_to_all_network_elements()
        self.endsystemConnectionManager.close_connection_to_all_endsystem_elements()
        self.trafficGeneratorConnectionManager.close_connection_to_all_traffic_generators()

    def Unit_Test_Suite_Cleanup(self, **kwargs):
        """  Used_only_for_unit_level_test_cases """
        self.networkElementConnectionManager.close_connection_to_all_network_elements()
        self.trafficGeneratorConnectionManager.close_connection_to_all_traffic_generators()

    def Suite_Setup_Baseline(self, base_config="base", **kwargs):
        #self.networkElementFileManagementKeywords.copy_configuration_all_netelems(testengine.ipv4_address, new_filename=base.cfg, overwrite=y, slot=1)
        self.networkElementResetDeviceUtilsKeywords.baseline_testbed(base_config, wait_after_success=30)
        self.networkElementConnectionManager.close_connection_to_all_network_elements()
        self.networkElementConnectionManager.connect_to_all_network_elements()
        self.networkElementConnectionManager.Configure_and_Verify_NTP_Server_All_Netelems("134.141.79.190")
        self.networkElementConnectionManager.Verify_All_Testbed_Connections("222")

    def Get_Base_Test_Suite_Platform_Values(self, **kwargs):
        self.nefw = NetworkElementFirmwareUtilsKeywords()
        self.nehc = NetworkElementHealthCheck()
        # Gather running FW version on all netelems
        self.nefw.save_running_firmware()
        # Gather sysType/model of all netelems
        self.nehc.store_device_model()

