from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Keywords.NetworkElementKeywords.L1.NetworkElementPortSettingsKeywords import \
    NetworkElementPortSettingsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L2.NetworkElementVlanKeywords import \
    NetworkElementVlanKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L3.NetworkElementInterfaceKeywords import \
    NetworkElementInterfaceKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.HostServices.NetworkElementHostServiceKeywords import \
    NetworkElementHostServiceKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.Security.NetworkElementRadiusKeywords import \
    NetworkElementRadiusKeywords
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class RadiusKeywordRegression(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.constants = NetworkElementConstants
        cls.vlan = NetworkElementVlanKeywords()
        cls.intf = NetworkElementInterfaceKeywords()
        cls.host = NetworkElementHostServiceKeywords()
        cls.radius = NetworkElementRadiusKeywords()
        cls.port = NetworkElementPortSettingsKeywords()
        cls.server_id = "1"
        cls.server_secret = "radiussecret"
        cls.server_ip = "111.1.1.2"
        cls.auth_port = "1812"
        cls.acct_port = "1813"
        cls.vlan_a = "111"
        cls.vlan_a_ip = "111.1.1.1"
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
        cls.radius.disable_radius(cls.netelem1)
        # EXOS Cleanup.
        cls.intf.remove_interface(cls.netelem2, cls.vlan_a)
        cls.vlan.remove_vlan(cls.netelem2, cls.vlan_a)
        cls.port.configure_port_disable(cls.netelem2, cls.exos_netelem_port)
        cls.radius.disable_radius(cls.netelem2)

        cls.keyword_disconnect_devices()

    # ### EOS Device Cases ###
    # Test Case 1
    def test_eos_radius_server_state(self):
        self.radius.create_radius_server(self.netelem1, self.server_id, self.server_ip, self.auth_port,
                                         self.server_secret)
        self.radius.radius_server_should_exist(self.netelem1, self.server_id, self.server_ip)
        self.radius.enable_radius(self.netelem1)
        self.radius.radius_server_should_be_active(self.netelem1, self.server_id, self.server_ip)
        self.radius.disable_radius(self.netelem1)
        self.radius.remove_radius_server(self.netelem1, self.server_id)
        self.radius.radius_server_should_not_exist(self.netelem1, self.server_id, self.server_ip)

    def test_eos_radius_accounting_server(self):
        self.radius.create_radius_server(self.netelem1, self.server_id, self.server_ip, self.auth_port,
                                         self.server_secret)
        self.radius.create_radius_accounting_server(self.netelem1, self.server_id, self.server_ip, self.acct_port,
                                                    self.server_secret)
        self.radius.radius_accounting_server_should_exist(self.netelem1, self.server_id, self.server_ip)
        self.radius.enable_radius_accounting(self.netelem1)
        self.radius.radius_accounting_state_should_be_enabled(self.netelem1)
        self.radius.disable_radius_accounting(self.netelem1)
        self.radius.radius_accounting_state_should_be_disabled(self.netelem1)
        self.radius.remove_radius_accounting_server(self.netelem1, self.server_id)
        self.radius.radius_accounting_server_should_not_exist(self.netelem1, self.server_id, self.server_ip)
        self.radius.remove_radius_server(self.netelem1, self.server_id)
        self.radius.radius_server_should_not_exist(self.netelem1, self.server_id, self.server_ip)

    def test_eos_radius_retries(self):
        self.radius.create_radius_server(self.netelem1, self.server_id, self.server_ip, self.auth_port,
                                         self.server_secret)
        self.radius.radius_server_should_exist(self.netelem1, self.server_id, self.server_ip)
        self.radius.enable_radius(self.netelem1)
        self.radius.configure_radius_retries(self.netelem1, "2")
        self.radius.verify_radius_retries(self.netelem1, "2")
        self.radius.clear_radius_retries(self.netelem1)
        self.radius.verify_radius_retries(self.netelem1, "3")
        self.radius.disable_radius(self.netelem1)
        self.radius.remove_radius_server(self.netelem1, self.server_id)
        self.radius.radius_server_should_not_exist(self.netelem1, self.server_id, self.server_ip)

    # ### EXOS Device Cases ###
    # Test Case 1
    def test_exos_radius_server_state(self):
        self.radius.create_radius_server(self.netelem2, self.server_id, self.server_ip, self.auth_port,
                                         self.server_secret, self.vlan_a_ip)
        self.radius.radius_server_should_exist(self.netelem2, self.server_id, self.server_ip)
        self.radius.enable_radius(self.netelem2)
        self.radius.radius_server_should_be_active(self.netelem2, self.server_id, self.server_ip)
        self.radius.disable_radius(self.netelem2)
        self.radius.remove_radius_server(self.netelem2, self.server_id)
        self.radius.radius_server_should_not_exist(self.netelem2, self.server_id, self.server_ip)

    def test_exos_radius_accounting_server(self):
        self.radius.create_radius_server(self.netelem2, self.server_id, self.server_ip, self.auth_port,
                                         self.server_secret, self.vlan_a_ip)
        self.radius.create_radius_accounting_server(self.netelem2, self.server_id, self.server_ip, self.acct_port,
                                                    self.server_secret, self.vlan_a_ip)
        self.radius.radius_accounting_server_should_exist(self.netelem2, self.server_id, self.server_ip)
        self.radius.enable_radius_accounting(self.netelem2)
        self.radius.radius_accounting_state_should_be_enabled(self.netelem2)
        self.radius.disable_radius_accounting(self.netelem2)
        self.radius.radius_accounting_state_should_be_disabled(self.netelem2)
        self.radius.remove_radius_accounting_server(self.netelem2, self.server_id)
        self.radius.radius_accounting_server_should_not_exist(self.netelem2, self.server_id, self.server_ip)
        self.radius.remove_radius_server(self.netelem2, self.server_id)
        self.radius.radius_server_should_not_exist(self.netelem2, self.server_id, self.server_ip)

    def test_exos_radius_retries(self):
        self.radius.create_radius_server(self.netelem2, self.server_id, self.server_ip, self.auth_port,
                                         self.server_secret, self.vlan_a_ip)
        self.radius.radius_server_should_exist(self.netelem2, self.server_id, self.server_ip)
        self.radius.enable_radius(self.netelem2)
        self.radius.configure_radius_retries(self.netelem2, "2")
        self.radius.verify_radius_retries(self.netelem2, "2")
        self.radius.clear_radius_retries(self.netelem2)
        self.radius.verify_radius_retries(self.netelem2, "3")
        self.radius.disable_radius(self.netelem2)
        self.radius.remove_radius_server(self.netelem2, self.server_id)
        self.radius.radius_server_should_not_exist(self.netelem2, self.server_id, self.server_ip)


if __name__ == '__main__':
    RobotUnitTest.main()
