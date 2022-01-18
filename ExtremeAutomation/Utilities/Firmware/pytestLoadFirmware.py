from ExtremeAutomation.Keywords.Utils.NetworkUtils import NetworkUtils
from ExtremeAutomation.Keywords.NetworkElementKeywords.StaticKeywords.NetworkElementFirmwareUtilsKeywords import NetworkElementFirmwareUtilsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementCliSend import NetworkElementCliSend
from ExtremeAutomation.Keywords.NetworkElementKeywords.NetworkElementConnectionManager import NetworkElementConnectionManager
from ExtremeAutomation.Keywords.NetworkElementKeywords.StaticKeywords.NetworkElementResetDeviceUtilsKeywords import NetworkElementResetDeviceUtilsKeywords
import threading
import pytest

# Documentation   These are Keywords that can be used for all EXOS platforms as needed.
class PlatformLoadFirmware():
    def __init__(self):
        self.netElemFwUtils = NetworkElementFirmwareUtilsKeywords()
        self.netElemCliSend = NetworkElementCliSend()
        self.networkUtils = NetworkUtils()
        self.netElemReset = NetworkElementResetDeviceUtilsKeywords()
        self.netElemConnMgr = NetworkElementConnectionManager()

    def Upgrade_Netelem_Firmware(self, netelem_name, tftp_server_ip, build_location,
                                 mgmt_vlan, netelem_ip, targetLocation="secondary", build=None, que=None):

        download_vr = "vr-default"
        if mgmt_vlan == "mgmt":
            download_vr = "vr-mgmt"
        startLocation = "primary"
        if targetLocation == "primary":
            startLocation = "secondary"
        print("{}  {} {} mv {} vr {} -   S T A R T I N G".format(threading.currentThread().getName(),netelem_name,build_location,mgmt_vlan,download_vr))
        try:
            self.netElemConnMgr.connect_to_network_element_name(netelem_name)
        except Exception as e:
            #pytest.skip("Download Firmware Failed. DUT {} not reachable. {}".format(netelem_name, e))
            if que:
                que.put("failed")
            return 0
        try:
            self.netElemFwUtils.select_firmware_on_network_element(netelem_name,startLocation)
            self.netElemReset.reboot_network_element_now_and_wait(netelem_name, 180)
            self.netElemConnMgr.connect_to_network_element_name(netelem_name)
            self.netElemFwUtils.load_firmware_on_network_element(netelem_name, \
                                tftp_server_ip, build_location, vr=download_vr, server_type='tftp')
            self.netElemReset.reset_network_element_to_factory_defaults(netelem_name)
            self.networkUtils.wait_for_pingable(netelem_ip, 300, 20, 30)
            self.netElemConnMgr.connect_to_network_element_name(netelem_name)
            if build and str(build) != 'None':
                self.netElemFwUtils.firmware_version_should_be_equal(netelem_name, build)
        except:
            if que:
                que.put("failed")
            pass
            return 0
        if que:
            que.put("passed")
        print("{}  {} {} -   E X I T I N G".format(threading.currentThread().getName(),netelem_name,build_location))
        return 1