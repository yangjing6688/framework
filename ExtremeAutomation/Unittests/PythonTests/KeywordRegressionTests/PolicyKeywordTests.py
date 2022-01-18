from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Keywords.NetworkElementKeywords.L1.NetworkElementPortSettingsKeywords import \
    NetworkElementPortSettingsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L2.NetworkElementVlanKeywords import \
    NetworkElementVlanKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L3.NetworkElementInterfaceKeywords import \
    NetworkElementInterfaceKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.HostServices.NetworkElementHostServiceKeywords import \
    NetworkElementHostServiceKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.Security.NetworkElementPolicyKeywords import \
    NetworkElementPolicyKeywords
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class PolicyKeywordRegression(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.constants = NetworkElementConstants
        cls.vlan = NetworkElementVlanKeywords()
        cls.intf = NetworkElementInterfaceKeywords()
        cls.host = NetworkElementHostServiceKeywords()
        cls.policy = NetworkElementPolicyKeywords()
        cls.port = NetworkElementPortSettingsKeywords()
        cls.profile_id = "51"
        cls.profile_name = "unit_test_profile"
        cls.vlan_a = "111"
        cls.vlan_a_ip = "111.1.1.1"
        cls.vlan_a_len = "24"
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
        cls.policy.remove_all_policy_rules(cls.netelem1)
        cls.vlan.remove_vlan(cls.netelem1, cls.vlan_a)
        cls.port.configure_port_disable(cls.netelem1, cls.eos_netelem_port)
        # EXOS Cleanup.
        cls.policy.remove_all_policy_rules(cls.netelem2)
        cls.vlan.remove_vlan(cls.netelem2, cls.vlan_a)
        cls.port.configure_port_disable(cls.netelem2, cls.exos_netelem_port)

        cls.keyword_disconnect_devices()

    # ### EOS Device Cases ###
    # Test Case 1
    def test_eos_policy_state(self):
        self.policy.enable_policy(self.netelem1)
        self.policy.policy_state_should_be_enabled(self.netelem1)
        self.policy.disable_policy(self.netelem1)
        self.policy.policy_state_should_be_disabled(self.netelem1)

    # Test Case 2
    def test_eos_policy_profile_name(self):
        self.policy.create_policy_profile(self.netelem1, self.profile_id)
        self.policy.verify_policy_profile_exists(self.netelem1, self.profile_id)
        self.policy.configure_policy_profile_name(self.netelem1, self.profile_id, self.profile_name)
        self.policy.verify_policy_profile_name(self.netelem1, self.profile_id, self.profile_name)
        self.policy.remove_policy_profile(self.netelem1, self.profile_id)
        self.policy.policy_profile_should_not_exist(self.netelem1, self.profile_id)

    # Test Case 3
    def test_eos_policy_admin_macsource(self):
        self.policy.create_policy_profile(self.netelem1, self.profile_id)
        self.policy.create_mac_source_admin_profile(self.netelem1, self.host_a_mac, self.eos_netelem_port,
                                                    self.profile_id)
        self.policy.policy_mac_source_admin_profile_should_exist(self.netelem1, self.host_a_mac, self.eos_netelem_port,
                                                                 self.profile_id)
        self.policy.remove_mac_source_admin_profile(self.netelem1, self.host_a_mac, self.eos_netelem_port)
        self.policy.policy_mac_source_admin_profile_should_not_exist(self.netelem1, self.host_a_mac,
                                                                     self.eos_netelem_port, self.profile_id,
                                                                     ignore_error="No entries found")
        self.policy.remove_policy_profile(self.netelem1, self.profile_id)
        self.policy.policy_profile_should_not_exist(self.netelem1, self.profile_id)

    # Test Case 4
    def test_eos_policy_ipsource_rule(self):
        self.policy.create_policy_profile(self.netelem1, self.profile_id)
        self.policy.create_policy_rule_ipsourcesocket(self.netelem1, self.profile_id, self.vlan_a_ip, drop=True)
        self.policy.policy_rule_ipsourcesocket_should_exist(self.netelem1, self.profile_id, self.vlan_a_ip, drop=True)
        self.policy.remove_all_rules_from_profile(self.netelem1, self.profile_id)
        self.policy.policy_rule_ipsourcesocket_should_not_exist(self.netelem1, self.profile_id, self.vlan_a_ip,
                                                                ignore_error="No entries found")
        self.policy.remove_policy_profile(self.netelem1, self.profile_id)

    # ### EXOS Device Cases ###
    # Test Case 1
    def test_exos_policy_state(self):
        self.policy.enable_policy(self.netelem2)
        self.policy.policy_state_should_be_enabled(self.netelem2)
        self.policy.disable_policy(self.netelem2)
        self.policy.policy_state_should_be_disabled(self.netelem2)

    # Test Case 2
    def test_exos_policy_profile_name(self):
        self.policy.create_policy_profile(self.netelem2, self.profile_id)
        self.policy.verify_policy_profile_exists(self.netelem2, self.profile_id)
        self.policy.configure_policy_profile_name(self.netelem2, self.profile_id, self.profile_name)
        self.policy.verify_policy_profile_name(self.netelem2, self.profile_id, self.profile_name)
        self.policy.remove_policy_profile(self.netelem2, self.profile_id)
        self.policy.policy_profile_should_not_exist(self.netelem2, self.profile_id)

    # Test Case 3
    def test_exos_policy_admin_macsource(self):
        self.policy.create_policy_profile(self.netelem2, self.profile_id)
        self.policy.create_mac_source_admin_profile(self.netelem2, self.host_a_mac, self.exos_netelem_port,
                                                    self.profile_id)
        self.policy.policy_mac_source_admin_profile_should_exist(self.netelem2, self.host_a_mac, self.exos_netelem_port,
                                                                 self.profile_id)
        self.policy.remove_mac_source_admin_profile(self.netelem2, self.host_a_mac, self.exos_netelem_port)
        self.policy.policy_mac_source_admin_profile_should_not_exist(self.netelem2, self.host_a_mac,
                                                                     self.exos_netelem_port, self.profile_id)
        self.policy.remove_policy_profile(self.netelem2, self.profile_id)
        self.policy.policy_profile_should_not_exist(self.netelem2, self.profile_id)

    # Test Case 4
    def test_exos_policy_ipsource_rule(self):
        self.policy.create_policy_profile(self.netelem2, self.profile_id)
        self.policy.create_policy_rule_ipsourcesocket(self.netelem2, self.profile_id, self.vlan_a_ip, drop=True)
        self.policy.policy_rule_ipsourcesocket_should_exist(self.netelem2, self.profile_id, self.vlan_a_ip, drop=True)
        self.policy.remove_all_rules_from_profile(self.netelem2, self.profile_id)
        self.policy.policy_rule_ipsourcesocket_should_not_exist(self.netelem2, self.profile_id, self.vlan_a_ip)
        self.policy.remove_policy_profile(self.netelem2, self.profile_id)


if __name__ == '__main__':
    RobotUnitTest.main()
