from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Keywords.NetworkElementKeywords.L1.NetworkElementPortSettingsKeywords import \
    NetworkElementPortSettingsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L2.NetworkElementVlanKeywords import NetworkElementVlanKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L3.NetworkElementInterfaceKeywords import \
    NetworkElementInterfaceKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.HostServices.NetworkElementHostServiceKeywords import \
    NetworkElementHostServiceKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L3.NetworkElementArpKeywords import NetworkElementArpKeywords
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class ArpKeywordRegression(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.constants = NetworkElementConstants
        cls.vlan = NetworkElementVlanKeywords()
        cls.intf = NetworkElementInterfaceKeywords()
        cls.host = NetworkElementHostServiceKeywords()
        cls.arp = NetworkElementArpKeywords()
        cls.port = NetworkElementPortSettingsKeywords()
        cls.vlan_a = "111"
        cls.vlan_a_ip = "111.1.1.1"
        cls.host_a_ip = "111.1.1.2"
        cls.vlan_a_len = "24"
        cls.host_a_mac = "00:AA:AA:AA:AA:AA"

        cls.keyword_connect_devices()
        # EOS Device Setup.
        cls.vlan.create_vlan(cls.netelem1, cls.vlan_a)
        cls.vlan.add_port_to_untagged_egress(cls.netelem1, cls.vlan_a, cls.eos_netelem_port)
        cls.vlan.configure_port_pvid(cls.netelem1, cls.eos_netelem_port, cls.vlan_a)
        cls.intf.create_interface(cls.netelem1, cls.vlan_a)
        cls.intf.configure_primary_ipv4_address_prefix(cls.netelem1, cls.vlan_a, cls.vlan_a_ip, cls.vlan_a_len)
        cls.intf.enable_vlan_interface(cls.netelem1, cls.vlan_a)
        cls.port.configure_port_enable(cls.netelem1, cls.eos_netelem_port)
        # EXOS Device Setup.
        cls.vlan.create_vlan(cls.netelem2, cls.vlan_a)
        cls.vlan.add_port_to_untagged_egress(cls.netelem2, cls.vlan_a, cls.exos_netelem_port)
        cls.vlan.configure_port_pvid(cls.netelem2, cls.exos_netelem_port, cls.vlan_a)
        cls.intf.create_interface(cls.netelem2, cls.vlan_a)
        cls.intf.configure_primary_ipv4_address_prefix(cls.netelem2, cls.vlan_a, cls.vlan_a_ip, cls.vlan_a_len)
        cls.intf.enable_vlan_interface(cls.netelem2, cls.vlan_a)
        cls.port.configure_port_enable(cls.netelem2, cls.exos_netelem_port)

    @classmethod
    def tearDownClass(cls):
        # EOS Cleanup.
        cls.intf.remove_interface(cls.netelem1, cls.vlan_a)
        cls.vlan.remove_vlan(cls.netelem1, cls.vlan_a)
        cls.port.configure_port_disable(cls.netelem1, cls.eos_netelem_port)
        # EXOS Cleanup.
        cls.intf.remove_interface(cls.netelem2, cls.vlan_a)
        cls.vlan.remove_vlan(cls.netelem2, cls.vlan_a)
        cls.port.configure_port_disable(cls.netelem2, cls.exos_netelem_port)

        cls.keyword_disconnect_devices()

    # ### EOS Device Cases ###
    # Test Case 1
    def test_eos_static_arp(self):
        self.arp.create_static_arp(self.netelem1, self.host_a_ip, self.host_a_mac, self.vlan_a)
        self.arp.arp_entry_should_exist(self.netelem1, self.host_a_ip, self.host_a_mac, self.vlan_a)
        self.arp.remove_arp_entry(self.netelem1, self.host_a_ip)
        self.arp.arp_entry_should_not_exist(self.netelem1, self.host_a_ip, self.host_a_mac)

    # ### EXOS Device Cases ###
    # Test Case 1
    def test_exos_static_arp(self):
        self.arp.create_static_arp(self.netelem2, self.host_a_ip, self.host_a_mac, self.vlan_a)
        self.arp.arp_entry_should_exist(self.netelem2, self.host_a_ip, self.host_a_mac, self.vlan_a)
        self.arp.remove_arp_entry(self.netelem2, self.host_a_ip)
        self.arp.arp_entry_should_not_exist(self.netelem2, self.host_a_ip, self.host_a_mac)


if __name__ == '__main__':
    RobotUnitTest.main()
