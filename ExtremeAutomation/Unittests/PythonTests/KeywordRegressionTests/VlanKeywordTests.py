from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Keywords.NetworkElementKeywords.L1.NetworkElementPortSettingsKeywords import \
    NetworkElementPortSettingsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L2.NetworkElementVlanKeywords import NetworkElementVlanKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.HostServices.NetworkElementHostServiceKeywords import \
    NetworkElementHostServiceKeywords
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class VlanKeywordRegression(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.constants = NetworkElementConstants
        cls.vlan = NetworkElementVlanKeywords()
        cls.host = NetworkElementHostServiceKeywords()
        cls.port = NetworkElementPortSettingsKeywords()
        cls.vlan_a = "111"
        cls.vlan_name = "Test VLAN"
        cls.vlan_list = ["151", "152", "155"]
        cls.name_list = ["test_vlan_a", "test_vlan_b", "test_vlan_c"]

        cls.keyword_connect_devices()
        # EOS Device Setup.
        cls.port.configure_port_enable(cls.netelem1, cls.eos_netelem_port)
        # EXOS Device Setup.
        cls.port.configure_port_enable(cls.netelem2, cls.exos_netelem_port)

    @classmethod
    def tearDownClass(cls):
        # EOS Cleanup.
        cls.port.configure_port_disable(cls.netelem1, cls.eos_netelem_port)
        # EXOS Cleanup.
        cls.port.configure_port_disable(cls.netelem2, cls.exos_netelem_port)

        cls.keyword_disconnect_devices()

    # ### EOS Device Cases ###
    # Test Case 1
    def test_eos_vlan_create_delete(self):
        self.vlan.create_vlan(self.netelem1, self.vlan_list)
        self.vlan.vlan_should_exist(self.netelem1, self.vlan_list)
        self.vlan.remove_vlan(self.netelem1, self.vlan_list)
        self.vlan.vlan_should_not_exist(self.netelem1, self.vlan_list)

    # Test Case 2
    def test_eos_vlan_name(self):
        self.vlan.create_vlan(self.netelem1, self.vlan_list)
        self.vlan.vlan_should_exist(self.netelem1, self.vlan_list)
        self.vlan.configure_vlan_name(self.netelem1, self.vlan_list, self.name_list)
        self.vlan.vlan_name_should_be(self.netelem1, self.vlan_list, self.name_list)
        self.vlan.remove_vlan(self.netelem1, self.vlan_list)
        self.vlan.vlan_should_not_exist(self.netelem1, self.vlan_list)

    # Test Case 3
    def test_eos_vlan_state(self):
        self.vlan.create_vlan(self.netelem1, self.vlan_a)
        self.vlan.vlan_should_exist(self.netelem1, self.vlan_a)
        self.vlan.disable_vlan(self.netelem1, self.vlan_a)
        self.vlan.vlan_should_be_disabled(self.netelem1, self.vlan_a)
        self.vlan.enable_vlan(self.netelem1, self.vlan_a)
        self.vlan.vlan_should_be_enabled(self.netelem1, self.vlan_a)
        self.vlan.remove_vlan(self.netelem1, self.vlan_a)
        self.vlan.vlan_should_not_exist(self.netelem1, self.vlan_a)

    # Test Case 4
    def test_eos_vlan_add_remove_port(self):
        self.vlan.create_vlan(self.netelem1, self.vlan_a)
        self.vlan.vlan_should_exist(self.netelem1, self.vlan_a)
        self.vlan.add_port_to_tagged_egress(self.netelem1, self.vlan_a, self.eos_netelem_port)
        self.port.port_should_be_operational(self.netelem1, self.eos_netelem_port, wait_for=True)
        self.vlan.port_should_be_on_tagged_egress(self.netelem1, self.vlan_a, self.eos_netelem_port)
        self.vlan.remove_port_from_vlan_egress(self.netelem1, self.vlan_a, self.eos_netelem_port)
        self.vlan.port_should_not_be_on_tagged_egress(self.netelem1, self.vlan_a, self.eos_netelem_port, wait_for=True,
                                                      max_wait="10")
        self.vlan.remove_vlan(self.netelem1, self.vlan_a)
        self.vlan.vlan_should_not_exist(self.netelem1, self.vlan_a)

    # ### EXOS Device Cases ###
    # Test Case 1
    def test_exos_vlan_create_delete(self):
        self.vlan.create_vlan(self.netelem2, self.vlan_list)
        self.vlan.vlan_should_exist(self.netelem2, self.vlan_list)
        self.vlan.remove_vlan(self.netelem2, self.vlan_list)
        self.vlan.vlan_should_not_exist(self.netelem2, self.vlan_list)

    # Test Case 2
    def test_exos_vlan_name(self):
        self.vlan.create_vlan(self.netelem2, self.vlan_list)
        self.vlan.vlan_should_exist(self.netelem2, self.vlan_list)
        self.vlan.configure_vlan_name(self.netelem2, self.vlan_list, self.name_list)
        self.vlan.vlan_name_should_be(self.netelem2, self.vlan_list, self.name_list)
        self.vlan.remove_vlan(self.netelem2, self.vlan_list)
        self.vlan.vlan_should_not_exist(self.netelem2, self.vlan_list)

    # Test Case 3
    def test_exos_vlan_state(self):
        self.vlan.create_vlan(self.netelem2, self.vlan_a)
        self.vlan.vlan_should_exist(self.netelem2, self.vlan_a)
        self.vlan.disable_vlan(self.netelem2, self.vlan_a)
        self.vlan.vlan_should_be_disabled(self.netelem2, self.vlan_a)
        self.vlan.enable_vlan(self.netelem2, self.vlan_a)
        self.vlan.vlan_should_be_enabled(self.netelem2, self.vlan_a)
        self.vlan.remove_vlan(self.netelem2, self.vlan_a)
        self.vlan.vlan_should_not_exist(self.netelem2, self.vlan_a)

    # Test Case 4
    def test_exos_vlan_add_remove_port(self):
        self.vlan.create_vlan(self.netelem2, self.vlan_a)
        self.vlan.vlan_should_exist(self.netelem2, self.vlan_a)
        self.vlan.add_port_to_tagged_egress(self.netelem2, self.vlan_a, self.exos_netelem_port)
        self.port.port_should_be_operational(self.netelem2, self.exos_netelem_port, wait_for=True)
        self.vlan.port_should_be_on_tagged_egress(self.netelem2, self.vlan_a, self.exos_netelem_port)
        self.vlan.remove_port_from_vlan_egress(self.netelem2, self.vlan_a, self.exos_netelem_port)
        self.vlan.port_should_not_be_on_tagged_egress(self.netelem2, self.vlan_a, self.exos_netelem_port)
        self.vlan.remove_vlan(self.netelem2, self.vlan_a)
        self.vlan.vlan_should_not_exist(self.netelem2, self.vlan_a)


if __name__ == '__main__':
    RobotUnitTest.main()
