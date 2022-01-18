from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Keywords.NetworkElementKeywords.L1.NetworkElementPortSettingsKeywords import \
    NetworkElementPortSettingsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L2.NetworkElementVlanKeywords import NetworkElementVlanKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L2.NetworkElementFdbKeywords import NetworkElementFdbKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.HostServices.NetworkElementHostServiceKeywords import \
    NetworkElementHostServiceKeywords
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class FdbKeywordRegression(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.constants = NetworkElementConstants
        cls.vlan = NetworkElementVlanKeywords()
        cls.host = NetworkElementHostServiceKeywords()
        cls.fdb = NetworkElementFdbKeywords()
        cls.port = NetworkElementPortSettingsKeywords()
        cls.agetime = "500"
        cls.vlan_a = "111"
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
    def test_eos_fdb_agetime_config(self):
        self.fdb.configure_fdb_agetime(self.netelem1, self.agetime)
        self.fdb.fdb_agetime_should_be(self.netelem1, self.agetime)
        self.fdb.clear_fdb_agetime(self.netelem1)

    # Test Case 2
    def test_eos_fdb_entry_config_inspect(self):
        self.fdb.create_fdb_entry(self.netelem1, self.host_a_mac, self.vlan_a, self.eos_netelem_port)
        self.fdb.fdb_entry_should_exist(self.netelem1, self.host_a_mac, self.vlan_a, self.eos_netelem_port)
        self.fdb.remove_fdb_entry(self.netelem1, self.host_a_mac, self.vlan_a)
        self.fdb.fdb_entry_should_not_exist(self.netelem1, self.host_a_mac, self.vlan_a, self.eos_netelem_port)

    # ### EXOS Device Cases ###
    # Test Case 1
    def test_exos_fdb_agetime_config(self):
        self.fdb.configure_fdb_agetime(self.netelem2, self.agetime)
        self.fdb.fdb_agetime_should_be(self.netelem2, self.agetime)
        self.fdb.clear_fdb_agetime(self.netelem2)

    # Test Case 2
    def test_exos_fdb_entry_config_inspect(self):
        self.fdb.create_fdb_entry(self.netelem2, self.host_a_mac, self.vlan_a, self.exos_netelem_port)
        self.fdb.fdb_entry_should_exist(self.netelem2, self.host_a_mac, self.vlan_a, self.exos_netelem_port)
        self.fdb.remove_fdb_entry(self.netelem2, self.host_a_mac, self.vlan_a)
        self.fdb.fdb_entry_should_not_exist(self.netelem2, self.host_a_mac, self.vlan_a, self.exos_netelem_port)


if __name__ == '__main__':
    RobotUnitTest.main()
