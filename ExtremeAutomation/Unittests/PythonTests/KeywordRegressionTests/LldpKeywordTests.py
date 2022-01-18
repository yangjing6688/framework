from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Keywords.NetworkElementKeywords.L1.NetworkElementPortSettingsKeywords import \
    NetworkElementPortSettingsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L2.NetworkElementVlanKeywords import NetworkElementVlanKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L2.NetworkElementLldpKeywords import NetworkElementLldpKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.HostServices.NetworkElementHostServiceKeywords import \
    NetworkElementHostServiceKeywords
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class LldpKeywordRegression(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.constants = NetworkElementConstants
        cls.vlan = NetworkElementVlanKeywords()
        cls.lldp = NetworkElementLldpKeywords()
        cls.host = NetworkElementHostServiceKeywords()
        cls.port = NetworkElementPortSettingsKeywords()

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
    def test_eos_lldp_state(self):
        self.lldp.enable_lldp_transmission_and_reception_on_port(self.netelem1, self.eos_netelem_port)
        self.lldp.lldp_receive_should_be_enabled_on_port(self.netelem1, self.eos_netelem_port)
        self.lldp.lldp_transmit_should_be_enabled_on_port(self.netelem1, self.eos_netelem_port)
        self.lldp.disable_lldp_transmission_and_reception_on_port(self.netelem1, self.eos_netelem_port)
        self.lldp.lldp_receive_should_be_disabled_on_port(self.netelem1, self.eos_netelem_port)
        self.lldp.lldp_transmit_should_be_disabled_on_port(self.netelem1, self.eos_netelem_port)

    # Test Case 2
    def test_eos_lldp_port_tlv_state(self):
        self.lldp.enable_lldp_transmission_and_reception_on_port(self.netelem1, self.eos_netelem_port)
        self.lldp.enable_tlv_port_desc(self.netelem1, self.eos_netelem_port)
        self.lldp.port_desc_tlv_should_be_enabled(self.netelem1, self.eos_netelem_port)
        self.lldp.disable_tlv_port_desc(self.netelem1, self.eos_netelem_port)
        self.lldp.port_desc_tlv_should_be_disabled(self.netelem1, self.eos_netelem_port)

    # Test Case 3
    def test_eos_lldp_sys_name_tlv_state(self):
        self.lldp.enable_lldp_transmission_and_reception_on_port(self.netelem1, self.eos_netelem_port)
        self.lldp.enable_tlv_sys_name(self.netelem1, self.eos_netelem_port)
        self.lldp.sys_name_tlv_should_be_enabled(self.netelem1, self.eos_netelem_port)
        self.lldp.disable_tlv_sys_name(self.netelem1, self.eos_netelem_port)
        self.lldp.sys_name_tlv_should_be_disabled(self.netelem1, self.eos_netelem_port)

    # Test Case 4
    def test_eos_lldp_sys_desc_tlv_state(self):
        self.lldp.enable_lldp_transmission_and_reception_on_port(self.netelem1, self.eos_netelem_port)
        self.lldp.enable_tlv_sys_desc(self.netelem1, self.eos_netelem_port)
        self.lldp.sys_desc_tlv_should_be_enabled(self.netelem1, self.eos_netelem_port)
        self.lldp.disable_tlv_sys_desc(self.netelem1, self.eos_netelem_port)
        self.lldp.sys_desc_tlv_should_be_disabled(self.netelem1, self.eos_netelem_port)

    # ### EXOS Device Cases ###
    # Test Case 1
    def test_exos_lldp_state(self):
        self.lldp.enable_lldp_transmission_and_reception_on_port(self.netelem2, self.exos_netelem_port)
        self.lldp.lldp_receive_should_be_enabled_on_port(self.netelem2, self.exos_netelem_port)
        self.lldp.lldp_transmit_should_be_enabled_on_port(self.netelem2, self.exos_netelem_port)
        self.lldp.disable_lldp_transmission_and_reception_on_port(self.netelem2, self.exos_netelem_port)
        self.lldp.lldp_receive_should_be_disabled_on_port(self.netelem2, self.exos_netelem_port)
        self.lldp.lldp_transmit_should_be_disabled_on_port(self.netelem2, self.exos_netelem_port)

    # Test Case 2
    def test_exos_lldp_port_tlv_state(self):
        self.lldp.enable_lldp_transmission_and_reception_on_port(self.netelem2, self.exos_netelem_port)
        self.lldp.enable_tlv_port_desc(self.netelem2, self.exos_netelem_port)
        self.lldp.port_desc_tlv_should_be_enabled(self.netelem2, self.exos_netelem_port)
        self.lldp.disable_tlv_port_desc(self.netelem2, self.exos_netelem_port)
        self.lldp.port_desc_tlv_should_be_disabled(self.netelem2, self.exos_netelem_port)

    # Test Case 3
    def test_exos_lldp_sys_name_tlv_state(self):
        self.lldp.enable_lldp_transmission_and_reception_on_port(self.netelem2, self.exos_netelem_port)
        self.lldp.enable_tlv_sys_name(self.netelem2, self.exos_netelem_port)
        self.lldp.sys_name_tlv_should_be_enabled(self.netelem2, self.exos_netelem_port)
        self.lldp.disable_tlv_sys_name(self.netelem2, self.exos_netelem_port)
        self.lldp.sys_name_tlv_should_be_disabled(self.netelem2, self.exos_netelem_port)

    # Test Case 4
    def test_exos_lldp_sys_desc_tlv_state(self):
        self.lldp.enable_lldp_transmission_and_reception_on_port(self.netelem2, self.exos_netelem_port)
        self.lldp.enable_tlv_sys_desc(self.netelem2, self.exos_netelem_port)
        self.lldp.sys_desc_tlv_should_be_enabled(self.netelem2, self.exos_netelem_port)
        self.lldp.disable_tlv_sys_desc(self.netelem2, self.exos_netelem_port)
        self.lldp.sys_desc_tlv_should_be_disabled(self.netelem2, self.exos_netelem_port)


if __name__ == '__main__':
    RobotUnitTest.main()
