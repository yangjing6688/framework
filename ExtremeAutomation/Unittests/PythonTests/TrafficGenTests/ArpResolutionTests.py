from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficPortKeywords import TrafficPortKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L3.NetworkElementArpKeywords import NetworkElementArpKeywords
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Keywords.NetworkElementKeywords.L2.NetworkElementVlanKeywords import NetworkElementVlanKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L3.NetworkElementInterfaceKeywords import \
    NetworkElementInterfaceKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L1.NetworkElementPortSettingsKeywords import \
    NetworkElementPortSettingsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.HostServices.NetworkElementHostUtilsKeywords import \
    NetworkElementHostUtilsKeywords


class TgenArpResolution(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.constants = NetworkElementConstants
        cls.vlan = NetworkElementVlanKeywords()
        cls.intf = NetworkElementInterfaceKeywords()
        cls.host = NetworkElementHostUtilsKeywords()
        cls.arp = NetworkElementArpKeywords()
        cls.port = NetworkElementPortSettingsKeywords()
        cls.traffic_port = TrafficPortKeywords()
        cls.vlan_a = "111"
        cls.vlan_a_ip = "111.1.1.1"
        cls.host_a_ip = "111.1.1.2"
        cls.vlan_a_len = "24"
        cls.host_a_mac = "00:AA:AA:AA:AA:AA"

        cls.keyword_connect_devices()
        cls.keyword_connect_tgens()
        cls.traffic_port.take_port_ownership(cls.eos_tgen_port)
        cls.vlan.create_vlan(cls.env["netelem1"]["name"], cls.vlan_a)
        cls.vlan.add_port_to_untagged_egress(cls.env["netelem1"]["name"], cls.vlan_a, cls.eos_netelem_port)
        cls.vlan.configure_port_pvid(cls.env["netelem1"]["name"], cls.eos_netelem_port, cls.vlan_a)
        cls.intf.configure_primary_ipv4_address_prefix(cls.env["netelem1"]["name"], cls.vlan_a, cls.vlan_a_ip, "24")
        cls.intf.enable_vlan_interface(cls.env["netelem1"]["name"], cls.vlan_a)
        cls.port.configure_port_enable(cls.env["netelem1"]["name"], cls.eos_netelem_port)
        cls.traffic_port.take_port_ownership(cls.exos_tgen_port)
        cls.vlan.create_vlan(cls.env["netelem2"]["name"], cls.vlan_a)
        cls.vlan.add_port_to_untagged_egress(cls.env["netelem2"]["name"], cls.vlan_a, cls.exos_netelem_port)
        cls.vlan.configure_port_pvid(cls.env["netelem2"]["name"], cls.exos_netelem_port, cls.vlan_a)
        cls.intf.configure_primary_ipv4_address_prefix(cls.env["netelem2"]["name"], cls.vlan_a, cls.vlan_a_ip, "24")
        cls.intf.enable_vlan_interface(cls.env["netelem2"]["name"], cls.vlan_a)
        cls.port.configure_port_enable(cls.env["netelem2"]["name"], cls.exos_netelem_port)

    @classmethod
    def tearDownClass(cls):
        cls.intf.remove_interface(cls.env["netelem1"]["name"], cls.vlan_a)
        cls.vlan.remove_vlan(cls.env["netelem1"]["name"], cls.vlan_a)
        cls.port.configure_port_disable(cls.env["netelem1"]["name"], cls.eos_netelem_port)
        cls.vlan.remove_vlan(cls.env["netelem2"]["name"], cls.vlan_a)
        cls.port.configure_port_disable(cls.env["netelem2"]["name"], cls.exos_netelem_port)
        cls.keyword_disconnect_devices()
        cls.keyword_disconnect_tgens()

    # ## EOS Device Cases ###
    # Test Case 1
    def test_eos_resolve_arp(self):
        self.traffic_port.configure_arp_resolution(self.eos_tgen_port, self.host_a_ip, self.host_a_mac,
                                                   self.vlan_a_len, "1", resolve_learn="resolve")
        self.host.host_address_should_be_reachable(self.env["netelem1"]["name"], self.host_a_ip, timeout="2")
        self.arp.arp_entry_should_exist(self.env["netelem1"]["name"], self.host_a_ip, self.host_a_mac)
        self.arp.remove_all_arp_entries(self.env["netelem1"]["name"])

    # Test Case 2
    def test_eos_learn_arp(self):
        self.traffic_port.configure_arp_resolution(self.eos_tgen_port, self.host_a_ip, self.host_a_mac,
                                                   self.vlan_a_len, "1", resolve_learn="learn")
        self.host.host_address_should_be_reachable(self.env["netelem1"]["name"], self.host_a_ip, timeout="2")
        self.arp.arp_entry_should_exist(self.env["netelem1"]["name"], self.host_a_ip, self.host_a_mac)
        self.arp.remove_all_arp_entries(self.env["netelem1"]["name"])

    # Test Case 3
    def test_eos_both_arp(self):
        self.traffic_port.configure_arp_resolution(self.eos_tgen_port, self.host_a_ip, self.host_a_mac,
                                                   self.vlan_a_len, "1", resolve_learn="both")
        self.host.host_address_should_be_reachable(self.env["netelem1"]["name"], self.host_a_ip, timeout="2")
        self.arp.arp_entry_should_exist(self.env["netelem1"]["name"], self.host_a_ip, self.host_a_mac)
        self.arp.remove_all_arp_entries(self.env["netelem1"]["name"])

    # ## EXOS Device Cases ###
    # Test Case 1
    def test_exos_resolve_arp(self):
        self.traffic_port.configure_arp_resolution(self.exos_tgen_port, self.host_a_ip, self.host_a_mac,
                                                   self.vlan_a_len, "1", resolve_learn="resolve")
        self.host.host_address_should_be_reachable(self.env["netelem2"]["name"], self.host_a_ip, timeout="2")
        self.arp.arp_entry_should_exist(self.env["netelem2"]["name"], self.host_a_ip, self.host_a_mac)
        self.arp.remove_all_arp_entries(self.env["netelem2"]["name"])

    # Test Case 2
    def test_exos_learn_arp(self):
        self.traffic_port.configure_arp_resolution(self.exos_tgen_port, self.host_a_ip, self.host_a_mac,
                                                   self.vlan_a_len, "1", resolve_learn="learn")
        self.host.host_address_should_be_reachable(self.env["netelem2"]["name"], self.host_a_ip, timeout="2")
        self.arp.arp_entry_should_exist(self.env["netelem2"]["name"], self.host_a_ip, self.host_a_mac)
        self.arp.remove_all_arp_entries(self.env["netelem2"]["name"])

    # Test Case 3
    def test_exos_both_arp(self):
        self.traffic_port.configure_arp_resolution(self.exos_tgen_port, self.host_a_ip, self.host_a_mac,
                                                   self.vlan_a_len, "1", resolve_learn="both")
        self.host.host_address_should_be_reachable(self.env["netelem2"]["name"], self.host_a_ip, timeout="2")
        self.arp.arp_entry_should_exist(self.env["netelem2"]["name"], self.host_a_ip, self.host_a_mac)
        self.arp.remove_all_arp_entries(self.env["netelem2"]["name"])


if __name__ == '__main__':
    RobotUnitTest.main()
