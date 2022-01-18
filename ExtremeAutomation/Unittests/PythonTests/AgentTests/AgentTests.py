from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Keywords.UiKeywords.EMC.Browser.UiBrowserKeywords import UiBrowserKeywords
from ExtremeAutomation.Keywords.UiKeywords.UiElementConnectionManager import UiElementConnectionManager
from ExtremeAutomation.Keywords.NetworkElementKeywords.L2.NetworkElementVlanKeywords import NetworkElementVlanKeywords
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Keywords.NetworkElementKeywords.NetworkElementConnectionManager import \
    NetworkElementConnectionManager

import warnings

warnings.simplefilter("ignore", ResourceWarning)


class DeviceAgentRegressions(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.constants = NetworkElementConstants
        cls.connect = NetworkElementConnectionManager()
        cls.ui_connect = UiElementConnectionManager()
        cls.browser = UiBrowserKeywords()
        cls.vlan = NetworkElementVlanKeywords()
        cls.vlan_a = "222"
        cls.create_devices()

    @classmethod
    def tearDownClass(cls):
        cls.keyword_disconnect_devices()

    # ### EOS Device Cases ###
    # Test Case 1
    def test_eos_telnet(self):
        self.connect.connect_to_network_element(self.netelem1, self.eos_dev.hostname, self.eos_dev.username,
                                                self.eos_dev.password, "telnet", self.eos_dev.oper_sys)
        self.vlan.create_vlan(self.netelem1, self.vlan_a)
        self.vlan.remove_vlan(self.netelem1, self.vlan_a)
        self.connect.close_connection_to_network_element(self.netelem1)

    # Test Case 2
    def test_eos_console(self):
        self.connect.connect_to_network_element(self.netelem1, self.eos_dev.console_ip, self.eos_dev.username,
                                                self.eos_dev.password, "telnet", self.eos_dev.oper_sys,
                                                self.eos_dev.console_port)
        self.vlan.create_vlan(self.netelem1, self.vlan_a)
        self.vlan.remove_vlan(self.netelem1, self.vlan_a)
        self.connect.close_connection_to_network_element(self.netelem1)

    # Test Case 3
    def test_eos_ssh(self):
        self.connect.connect_to_network_element(self.netelem1, self.eos_dev.hostname, self.eos_dev.username,
                                                self.eos_dev.password, "ssh", self.eos_dev.oper_sys)
        self.vlan.create_vlan(self.netelem1, self.vlan_a)
        self.vlan.remove_vlan(self.netelem1, self.vlan_a)
        self.connect.close_connection_to_network_element(self.netelem1)

    # Test Case 4
    def test_eos_snmp(self):
        self.connect.connect_to_network_element(self.netelem1, self.eos_dev.hostname, self.eos_dev.username,
                                                self.eos_dev.password, "snmp", self.eos_dev.oper_sys,
                                                snmp_info=self.eos_snmp_info)
        self.vlan.vlan_should_exist(self.netelem1, "4000")
        self.connect.close_connection_to_network_element(self.netelem1)

    # ### EXOS Device Cases ###
    # Test Case 1
    def test_exos_telnet(self):
        self.connect.connect_to_network_element(self.netelem2, self.exos_dev.hostname, self.exos_dev.username,
                                                self.exos_dev.password, "telnet", self.exos_dev.oper_sys)
        self.vlan.create_vlan(self.netelem2, self.vlan_a)
        self.vlan.remove_vlan(self.netelem2, self.vlan_a)
        self.connect.close_connection_to_network_element(self.netelem2)

    # Test Case 2
    def test_exos_console(self):
        self.connect.connect_to_network_element(self.netelem2, self.exos_dev.console_ip, self.exos_dev.username,
                                                self.exos_dev.password, "telnet", self.exos_dev.oper_sys,
                                                self.exos_dev.console_port)
        self.vlan.create_vlan(self.netelem2, self.vlan_a)
        self.vlan.remove_vlan(self.netelem2, self.vlan_a)
        self.connect.close_connection_to_network_element(self.netelem2)

    # Test Case 3
    def test_exos_ssh(self):
        self.connect.connect_to_network_element(self.netelem2, self.exos_dev.hostname, self.exos_dev.username,
                                                self.exos_dev.password, "ssh", self.exos_dev.oper_sys)
        self.vlan.create_vlan(self.netelem2, self.vlan_a)
        self.vlan.remove_vlan(self.netelem2, self.vlan_a)
        self.connect.close_connection_to_network_element(self.netelem2)

    # Test Case 4
    def test_exos_snmp(self):
        self.connect.connect_to_network_element(self.netelem2, self.exos_dev.hostname, self.exos_dev.username,
                                                self.exos_dev.password, "snmp", self.exos_dev.oper_sys,
                                                snmp_info=self.exos_snmp_info)
        self.vlan.vlan_should_exist(self.netelem2, "1")
        self.connect.close_connection_to_network_element(self.netelem2)

    # Test Case 6
    def test_exos_rest(self):
        self.connect.connect_to_network_element(self.netelem2, self.exos_dev.hostname, self.exos_dev.username,
                                                self.exos_dev.password, "rest", self.exos_dev.oper_sys)
        self.vlan.create_vlan(self.netelem2, self.vlan_a)
        self.vlan.remove_vlan(self.netelem2, self.vlan_a)
        self.connect.close_connection_to_network_element(self.netelem2)

    # ### XMC Device Cases ###
    def test_xmc_ext_selenium(self):
        self.ui_connect.connect_to_ui_element(self.uielem1, self.xmc_dev.hostname, self.xmc_dev.connection_method,
                                              self.xmc_dev.application, self.xmc_dev.port, self.xmc_dev.app_version)
        self.browser.open_web_page(self.uielem1, self.xmc_dev.url)
        self.browser.login(self.uielem1, self.xmc_dev.username, self.xmc_dev.password)
        self.browser.close_web_page(self.uielem1)
        self.ui_connect.close_connection_to_ui_element(self.uielem1)


if __name__ == '__main__':
    RobotUnitTest.main()
