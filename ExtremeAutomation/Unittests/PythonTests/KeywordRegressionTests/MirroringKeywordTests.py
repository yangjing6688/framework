from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Keywords.NetworkElementKeywords.L1.NetworkElementMirroringKeywords import \
    NetworkElementMirroringKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L1.NetworkElementPortSettingsKeywords import \
    NetworkElementPortSettingsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.L3.NetworkElementInterfaceKeywords import \
    NetworkElementInterfaceKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.HostServices.NetworkElementHostServiceKeywords import \
    NetworkElementHostServiceKeywords
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class MirroringKeywordRegression(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.constants = NetworkElementConstants
        cls.intf = NetworkElementInterfaceKeywords()
        cls.host = NetworkElementHostServiceKeywords()
        cls.mirror = NetworkElementMirroringKeywords()
        cls.port = NetworkElementPortSettingsKeywords()

        cls.keyword_connect_devices()
        # EOS Device Setup.
        cls.port.configure_port_enable(cls.netelem1, cls.eos_netelem_port)
        cls.port.configure_port_enable(cls.netelem1, cls.eos_netelem_port_b)
        # EXOS Device Setup.
        cls.port.configure_port_enable(cls.netelem2, cls.exos_netelem_port)
        cls.port.configure_port_enable(cls.netelem2, cls.exos_netelem_port_b)

    @classmethod
    def tearDownClass(cls):
        # EOS Cleanup.
        cls.port.configure_port_disable(cls.netelem1, cls.eos_netelem_port)
        cls.port.configure_port_disable(cls.netelem1, cls.eos_netelem_port_b)
        # EXOS Cleanup.
        cls.port.configure_port_disable(cls.netelem2, cls.exos_netelem_port)
        cls.port.configure_port_disable(cls.netelem2, cls.exos_netelem_port_b)

        cls.keyword_disconnect_devices()

    # ### EOS Device Cases ###
    # Test Case 1
    def test_eos_create_delete_mirror(self):
        self.mirror.create_port_mirror_ingress_egress(self.netelem1, "mirror_test", self.eos_netelem_port,
                                                      self.eos_netelem_port_b)
        self.mirror.port_mirror_should_exist(self.netelem1, "mirror_test", self.eos_netelem_port,
                                             self.eos_netelem_port_b)
        self.mirror.remove_port_mirror(self.netelem1, "mirror_test", self.eos_netelem_port, self.eos_netelem_port_b)
        self.mirror.port_mirror_should_not_exist(self.netelem1, "mirror_test", self.eos_netelem_port,
                                                 self.eos_netelem_port_b)

    def test_eos_enable_disable_mirror(self):
        self.mirror.create_port_mirror_ingress_egress(self.netelem1, "mirror_test", self.eos_netelem_port,
                                                      self.eos_netelem_port_b)
        self.mirror.port_mirror_should_exist(self.netelem1, "mirror_test", self.eos_netelem_port,
                                             self.eos_netelem_port_b)
        self.mirror.enable_port_mirror(self.netelem1, "mirror_test", self.eos_netelem_port, self.eos_netelem_port_b)
        self.mirror.port_mirror_should_be_enabled(self.netelem1, "mirror_test", self.eos_netelem_port,
                                                  self.eos_netelem_port_b)
        self.mirror.disable_port_mirror(self.netelem1, "mirror_test", self.eos_netelem_port, self.eos_netelem_port_b)
        self.mirror.port_mirror_should_be_disabled(self.netelem1, "mirror_test", self.eos_netelem_port,
                                                   self.eos_netelem_port_b)
        self.mirror.remove_port_mirror(self.netelem1, "mirror_test", self.eos_netelem_port, self.eos_netelem_port_b)
        self.mirror.port_mirror_should_not_exist(self.netelem1, "mirror_test", self.eos_netelem_port,
                                                 self.eos_netelem_port_b)

    # ### EXOS Device Cases ###
    # Test Case 1
    def test_exos_create_delete_mirror(self):
        self.mirror.create_port_mirror_ingress_egress(self.netelem2, "mirror_test", self.exos_netelem_port,
                                                      self.exos_netelem_port_b)
        self.mirror.configure_port_mirror_source(self.netelem2, "mirror_test", self.exos_netelem_port)
        self.mirror.port_mirror_should_exist(self.netelem2, "mirror_test", self.exos_netelem_port,
                                             self.exos_netelem_port_b)
        self.mirror.remove_port_mirror(self.netelem2, "mirror_test", self.exos_netelem_port, self.exos_netelem_port_b)
        self.mirror.port_mirror_should_not_exist(self.netelem2, "mirror_test", self.exos_netelem_port,
                                                 self.exos_netelem_port_b)

    def test_exos_enable_disable_mirror(self):
        self.mirror.create_port_mirror_ingress_egress(self.netelem2, "mirror_test", self.exos_netelem_port,
                                                      self.exos_netelem_port_b)
        self.mirror.configure_port_mirror_source(self.netelem2, "mirror_test", self.exos_netelem_port)
        self.mirror.port_mirror_should_exist(self.netelem2, "mirror_test", self.exos_netelem_port,
                                             self.exos_netelem_port_b)
        self.mirror.enable_port_mirror(self.netelem2, "mirror_test", self.exos_netelem_port, self.exos_netelem_port_b)
        self.mirror.port_mirror_should_be_enabled(self.netelem2, "mirror_test", self.exos_netelem_port,
                                                  self.exos_netelem_port_b)
        self.mirror.disable_port_mirror(self.netelem2, "mirror_test", self.exos_netelem_port, self.exos_netelem_port_b)
        self.mirror.port_mirror_should_be_disabled(self.netelem2, "mirror_test", self.exos_netelem_port,
                                                   self.exos_netelem_port_b)
        self.mirror.remove_port_mirror(self.netelem2, "mirror_test", self.exos_netelem_port, self.exos_netelem_port_b)
        self.mirror.port_mirror_should_not_exist(self.netelem2, "mirror_test", self.exos_netelem_port,
                                                 self.exos_netelem_port_b)


if __name__ == '__main__':
    RobotUnitTest.main()
