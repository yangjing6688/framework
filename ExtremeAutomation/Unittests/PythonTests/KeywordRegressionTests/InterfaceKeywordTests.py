from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Keywords.NetworkElementKeywords.L1.NetworkElementPortSettingsKeywords import \
    NetworkElementPortSettingsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L2.NetworkElementVlanKeywords import NetworkElementVlanKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L3.NetworkElementInterfaceKeywords import \
    NetworkElementInterfaceKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.HostServices.NetworkElementHostServiceKeywords import \
    NetworkElementHostServiceKeywords
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class InterfaceKeywordRegression(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.constants = NetworkElementConstants
        cls.vlan = NetworkElementVlanKeywords()
        cls.intf = NetworkElementInterfaceKeywords()
        cls.host = NetworkElementHostServiceKeywords()
        cls.port = NetworkElementPortSettingsKeywords()
        cls.vlan_a = "222"
        cls.loop_a = "2"
        cls.vlan_a_name = "test_intf"
        cls.vlan_a_ip = "222.1.1.1"
        cls.loop_a_ip = "2.2.2.2"
        cls.vlan_a_len = "24"
        cls.loop_a_mask = "255.255.255.255"
        cls.host_a_mac = "00:AA:AA:AA:AA:AA"

        cls.keyword_connect_devices()
        # EOS Device Setup.
        cls.vlan.create_vlan(cls.netelem1, cls.vlan_a)
        cls.vlan.add_port_to_untagged_egress(cls.netelem1, cls.vlan_a, cls.eos_netelem_port)
        cls.vlan.configure_port_pvid(cls.netelem1, cls.eos_netelem_port, cls.vlan_a)
        cls.port.configure_port_enable(cls.netelem1, cls.eos_netelem_port)
        # EXOS Device Setup.
        cls.vlan.create_vlan(cls.netelem2, cls.vlan_a)
        cls.vlan.add_port_to_untagged_egress(cls.netelem2, cls.vlan_a, cls.exos_netelem_port)
        cls.vlan.configure_port_pvid(cls.netelem2, cls.exos_netelem_port, cls.vlan_a)
        cls.port.configure_port_enable(cls.netelem2, cls.exos_netelem_port)

    @classmethod
    def tearDownClass(cls):
        # EOS Cleanup.
        cls.vlan.remove_vlan(cls.netelem1, cls.vlan_a)
        cls.port.configure_port_disable(cls.netelem1, cls.eos_netelem_port)
        # EXOS Cleanup.
        cls.vlan.remove_vlan(cls.netelem2, cls.vlan_a)
        cls.port.configure_port_disable(cls.netelem2, cls.exos_netelem_port)

        cls.keyword_disconnect_devices()

    # ### EOS Device Cases ###
    # Test Case 1
    def test_eos_interface_create_delete(self):
        self.intf.create_interface(self.netelem1, self.vlan_a)
        self.intf.interface_should_exist(self.netelem1, self.vlan_a)
        self.intf.remove_interface(self.netelem1, self.vlan_a)
        self.intf.interface_should_not_exist(self.netelem1, self.vlan_a)

    # Test Case 2
    def test_eos_interface_state(self):
        self.intf.create_interface(self.netelem1, self.vlan_a)
        self.intf.interface_should_exist(self.netelem1, self.vlan_a)
        self.intf.disable_vlan_interface(self.netelem1, self.vlan_a)
        self.intf.interface_should_be_disabled(self.netelem1, self.vlan_a)
        self.intf.enable_vlan_interface(self.netelem1, self.vlan_a)
        self.intf.interface_should_be_enabled(self.netelem1, self.vlan_a)
        self.intf.remove_interface(self.netelem1, self.vlan_a)
        self.intf.interface_should_not_exist(self.netelem1, self.vlan_a)

    # Test Case 3
    def test_eos_interface_address(self):
        self.intf.create_interface(self.netelem1, self.vlan_a)
        self.intf.interface_should_exist(self.netelem1, self.vlan_a)
        self.intf.configure_primary_ipv4_address_prefix(self.netelem1, self.vlan_a, self.vlan_a_ip, self.vlan_a_len)
        self.intf.verify_interface_ip_address(self.netelem1, self.vlan_a, self.vlan_a_ip, self.vlan_a_len)
        self.intf.remove_interface(self.netelem1, self.vlan_a)
        self.intf.interface_should_not_exist(self.netelem1, self.vlan_a)

    # Test Case 4
    def test_eos_interface_mac(self):
        self.intf.create_interface(self.netelem1, self.vlan_a)
        self.intf.interface_should_exist(self.netelem1, self.vlan_a)
        self.intf.configure_interface_mac_address(self.netelem1, self.vlan_a, self.host_a_mac)
        self.intf.verify_interface_mac_address(self.netelem1, self.vlan_a, self.host_a_mac)
        self.intf.remove_interface(self.netelem1, self.vlan_a)
        self.intf.interface_should_not_exist(self.netelem1, self.vlan_a)

    # Test Case 5
    def test_eos_interface_loopback(self):
        self.intf.create_loopback(self.netelem1, self.loop_a)
        self.intf.enable_loopback(self.netelem1, self.loop_a)
        self.intf.loopback_should_exist(self.netelem1, self.loop_a)
        self.intf.configure_loopback_ipv4_address_netmask(self.netelem1, self.loop_a, self.loop_a_ip, self.loop_a_mask)
        self.intf.verify_loopback_ip_address(self.netelem1, self.loop_a, self.loop_a_ip, self.loop_a_mask)
        self.intf.disable_loopback(self.netelem1, self.loop_a)
        self.intf.delete_loopback(self.netelem1, self.loop_a)
        self.intf.loopback_should_not_exist(self.netelem1, self.loop_a)

    # ### EXOS Device Cases ###
    # Test Case 1
    def test_exos_interface_create_delete(self):
        self.intf.create_interface(self.netelem2, self.vlan_a)
        self.intf.interface_should_exist(self.netelem2, self.vlan_a)
        # self.intf.remove_interface(self.netelem2, self.vlan_a)
        # self.intf.interface_should_not_exist(self.netelem2, self.vlan_a)

    # Test Case 2
    def test_exos_interface_state(self):
        self.intf.create_interface(self.netelem2, self.vlan_a)
        self.intf.interface_should_exist(self.netelem2, self.vlan_a)
        self.intf.disable_vlan_interface(self.netelem2, self.vlan_a)
        self.intf.interface_should_be_disabled(self.netelem2, self.vlan_a)
        self.intf.enable_vlan_interface(self.netelem2, self.vlan_a)
        self.intf.interface_should_be_enabled(self.netelem2, self.vlan_a)
        # self.intf.remove_interface(self.netelem2, self.vlan_a)
        # self.intf.interface_should_not_exist(self.netelem2, self.vlan_a)

    # Test Case 3
    def test_exos_interface_address(self):
        self.intf.create_interface(self.netelem2, self.vlan_a)
        self.intf.interface_should_exist(self.netelem2, self.vlan_a)
        self.intf.configure_primary_ipv4_address_prefix(self.netelem2, self.vlan_a, self.vlan_a_ip, self.vlan_a_len)
        self.intf.verify_interface_ip_address(self.netelem2, self.vlan_a, self.vlan_a_ip, self.vlan_a_len)
        # self.intf.remove_interface(self.netelem2, self.vlan_a)
        # self.intf.interface_should_not_exist(self.netelem2, self.vlan_a)

    # Test Case 4  -  EXOS DOES NOT SUPPORT CHANGING INTERFACE MAC ADDRESSES
    # def test_exos_interface_mac(self):
    #     self.intf.create_interface(self.netelem2, self.vlan_a)
    #     self.intf.interface_should_exist(self.netelem2, self.vlan_a)
    #     self.intf.configure_interface_mac_address(self.netelem2, self.vlan_a, self.host_a_mac)
    #     self.intf.verify_interface_mac_address(self.netelem2, self.vlan_a, self.host_a_mac)
    #     self.intf.remove_interface(self.netelem2, self.vlan_a)
    #     self.intf.interface_should_not_exist(self.netelem2, self.vlan_a)

    # Test Case 5
    def test_exos_interface_loopback(self):
        self.intf.create_loopback(self.netelem2, self.loop_a)
        self.intf.enable_loopback(self.netelem2, self.loop_a)
        self.intf.loopback_should_exist(self.netelem2, self.loop_a)
        self.intf.configure_loopback_ipv4_address_netmask(self.netelem2, self.loop_a, self.loop_a_ip, self.loop_a_mask)
        self.intf.verify_loopback_ip_address(self.netelem2, self.loop_a, self.loop_a_ip, self.loop_a_mask)
        self.intf.disable_loopback(self.netelem2, self.loop_a)
        self.intf.delete_loopback(self.netelem2, self.loop_a)
        self.intf.loopback_should_not_exist(self.netelem2, self.loop_a)


if __name__ == '__main__':
    RobotUnitTest.main()
