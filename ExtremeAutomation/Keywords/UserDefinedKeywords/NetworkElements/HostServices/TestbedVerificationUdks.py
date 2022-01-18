from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementListUtils import NetworkElementListUtils
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementConnectionVerification import NetworkElementConnectionVerification
from ExtremeAutomation.Keywords.TrafficKeywords.TrafficTransmitKeywords import TrafficTransmitKeywords


class TestbedVerificationUdks():
    def __init__(self):
        self.networkElementListUtils = NetworkElementListUtils()
        self.networkElementConnectionVerification = NetworkElementConnectionVerification()
        self.trafficTransmitKeywords = TrafficTransmitKeywords()

    def Verify_All_Testbed_Connections(self, test_vlan, all_tgen_ports, **kwargs):
        # netelem_list = self.networkElementListUtils.create_list_of_network_element_names()
        self.networkElementConnectionVerification.enable_and_configure_all_netelem_ports(test_vlan, **kwargs)
        self.networkElementConnectionVerification.create_tgen_connection_verification_packets(**kwargs)
        self.trafficTransmitKeywords.start_transmit_on_port(all_tgen_ports, **kwargs)
        self.networkElementConnectionVerification.verify_all_netelem_tgen_connections(test_vlan, **kwargs)
        self.trafficTransmitKeywords.stop_transmit_on_port(all_tgen_ports, **kwargs)
        self.networkElementConnectionVerification.verify_all_netelem_isl_connections(**kwargs)
        self.networkElementConnectionVerification.disable_and_cleanup_all_netelem_ports(test_vlan, **kwargs)
