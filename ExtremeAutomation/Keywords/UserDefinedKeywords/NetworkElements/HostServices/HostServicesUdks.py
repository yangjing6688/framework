from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementListUtils import NetworkElementListUtils
from ExtremeAutomation.Keywords.NetworkElementKeywords.StaticKeywords.NetworkElementFirmwareUtilsKeywords import NetworkElementFirmwareUtilsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.StaticKeywords.NetworkElementResetDeviceUtilsKeywords import NetworkElementResetDeviceUtilsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.NetworkElementConnectionManager import NetworkElementConnectionManager


class HostServicesUdks():
    def __init__(self):
        self.networkElementListUtils = NetworkElementListUtils()
        self.networkElementFirmwareKeywords = NetworkElementFirmwareUtilsKeywords()
        self.networkElementResetDeviceKeywords = NetworkElementResetDeviceUtilsKeywords()
        self.networkElementConnectionManager = NetworkElementConnectionManager()

    def Upgrade_All_Network_Elements_in_Environment(self, server_address, image_filename, local_image_name=None,
                                                    version=None, mgmt_vr='vr-default', max_wait=300,
                                                    wait_before=10, wait_after=10, **kwargs):
        netelem_list = self.networkElementListUtils.create_list_of_network_element_names()
        self.networkElementFirmwareKeywords.load_firmware_on_network_element(netelem_list, server_address, 
                                                                             image_filename, version, mgmt_vr)
        self.networkElementFirmwareKeywords.select_firmware_on_network_element(netelem_list, local_image_name, version, server_address, **kwargs)
        self.networkElementResetDeviceKeywords.reboot_network_element_now_and_wait(netelem_list, max_wait, wait_before, wait_after, **kwargs)
        self.networkElementConnectionManager.close_connection_to_all_network_elements(**kwargs)
        self.networkElementConnectionManager.connect_to_all_network_elements(**kwargs)
        self.networkElementFirmwareKeywords.firmware_version_should_be_equal(netelem_list, version, **kwargs)

    def Upgrade_All_Extreme_Fabrics_in_Environment(self, env_host_endsys, server_address,  image_filename, **kwargs):
        netelem_list = self.networkElementListUtils.create_list_of_network_element_names(**kwargs)
        self.networkElementFirmwareKeywords.load_firmware_on_network_element(env_host_endsys, server_address,
                                                                             image_filename, **kwargs)
        self.networkElementFirmwareKeywords.select_firmware_on_network_element(netelem_list, **kwargs)

    def Upgrade_VOSS_Network_Element(self, filename,  answer='y', max_wait=300, wait_before=20, wait_after=120,
                                     **kwargs):
        netelem_list = self.networkElementListUtils.create_list_of_network_element_names()
        self.networkElementFirmwareKeywords.select_firmware_on_network_element(netelem_list, filename,
                                                                               answer, **kwargs)
        self.networkElementResetDeviceKeywords.reboot_network_element_now_and_wait(netelem_list, max_wait, wait_before,
                                                                                   wait_after, **kwargs)
        self.networkElementFirmwareKeywords.commit_firmware(netelem_list, **kwargs)
