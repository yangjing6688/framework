from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Keywords.NetworkElementKeywords.L1.NetworkElementPortSettingsKeywords import \
    NetworkElementPortSettingsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L2.NetworkElementVlanKeywords import NetworkElementVlanKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L2.NetworkElementSpanningTreeKeywords import \
    NetworkElementSpanningTreeKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.HostServices.NetworkElementHostServiceKeywords import \
    NetworkElementHostServiceKeywords
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class SpanningTreeKeywordRegression(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.constants = NetworkElementConstants
        cls.vlan = NetworkElementVlanKeywords()
        cls.stp = NetworkElementSpanningTreeKeywords()
        cls.host = NetworkElementHostServiceKeywords()
        cls.port = NetworkElementPortSettingsKeywords()
        cls.vlan_a = "111"

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
        cls.stp.disable_spanning_tree(cls.netelem1)
        # EXOS Cleanup.
        cls.vlan.remove_vlan(cls.netelem2, cls.vlan_a)
        cls.port.configure_port_disable(cls.netelem2, cls.exos_netelem_port)
        cls.stp.disable_spanning_tree(cls.netelem2)

        cls.keyword_disconnect_devices()

    # ### EOS Device Cases ###
    # Test Case 1
    def test_eos_stp_state(self):
        self.stp.enable_spanning_tree(self.netelem1)
        self.stp.spanning_tree_should_be_enabled(self.netelem1)
        self.stp.disable_spanning_tree(self.netelem1)
        self.stp.spanning_tree_should_be_disabled(self.netelem1)

    # Test Case 2
    def test_eos_stp_port_admin_state(self):
        self.stp.enable_spanning_tree(self.netelem1)
        self.stp.enable_spanning_tree_portadmin(self.netelem1, self.eos_netelem_port)
        self.stp.spanning_tree_portadmin_should_be_enabled(self.netelem1, self.eos_netelem_port)
        self.stp.disable_spanning_tree_portadmin(self.netelem1, self.eos_netelem_port)
        self.stp.spanning_tree_portadmin_should_be_disabled(self.netelem1, self.eos_netelem_port)
        self.stp.disable_spanning_tree(self.netelem1)
        self.stp.spanning_tree_should_be_disabled(self.netelem1)

    # Test Case 3
    def test_eos_stp_mode(self):
        self.stp.configure_spanning_tree_mode_dot1d(self.netelem1)
        self.stp.spanning_tree_mode_should_be_dot1d(self.netelem1)
        self.stp.configure_spanning_tree_mode_mstp(self.netelem1)
        self.stp.spanning_tree_mode_should_be_mstp(self.netelem1)
        self.stp.configure_spanning_tree_mode_default(self.netelem1)

    # ### EXOS Device Cases ###
    # Test Case 1
    def test_exos_stp_state(self):
        self.stp.enable_spanning_tree(self.netelem2)
        self.stp.spanning_tree_should_be_enabled(self.netelem2)
        self.stp.disable_spanning_tree(self.netelem2)
        self.stp.spanning_tree_should_be_disabled(self.netelem2)

    # Test Case 2
    def test_exos_stp_port_admin_state(self):
        self.stp.configure_vlan_mapping_to_msti(self.netelem2, self.vlan_a)
        self.stp.enable_spanning_tree(self.netelem2)
        self.stp.enable_spanning_tree_portadmin(self.netelem2, self.exos_netelem_port)
        self.stp.spanning_tree_portadmin_should_be_enabled(self.netelem2, self.exos_netelem_port)
        self.stp.disable_spanning_tree_portadmin(self.netelem2, self.exos_netelem_port)
        self.stp.spanning_tree_portadmin_should_be_disabled(self.netelem2, self.exos_netelem_port)
        self.stp.disable_spanning_tree(self.netelem2)
        self.stp.spanning_tree_should_be_disabled(self.netelem2)
        self.stp.delete_vlan_to_msti_mapping(self.netelem2, self.vlan_a)

    # Test Case 3
    def test_exos_stp_mode(self):
        self.stp.configure_spanning_tree_mode_dot1d(self.netelem2)
        self.stp.spanning_tree_mode_should_be_dot1d(self.netelem2)
        self.stp.configure_spanning_tree_mode_mstp(self.netelem2)
        self.stp.spanning_tree_mode_should_be_mstp(self.netelem2)
        self.stp.configure_spanning_tree_mode_default(self.netelem2)


if __name__ == '__main__':
    RobotUnitTest.main()
