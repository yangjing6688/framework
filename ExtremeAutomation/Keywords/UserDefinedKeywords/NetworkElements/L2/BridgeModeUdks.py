from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementBridgemodeGenKeywords import NetworkElementBridgemodeGenKeywords


class BridgeModeUdks():
    def __init__(self) -> None:
        self.networkElementBridgemodeGenKeywords = NetworkElementBridgemodeGenKeywords()

    def Set_Bridge_Mode_to_Provider_and_Verify_it_was_Set(self, netelem_name, **kwargs):
        self.networkElementBridgemodeGenKeywords.bridgemode_set_mode(netelem_name,  'provider-bridge', **kwargs)
        self.networkElementBridgemodeGenKeywords.bridgemode_verify_provider_bridge(netelem_name, wait_for=True, max_wait=10)

    def Set_Bridge_Mode_to_Customer_and_Verify_it_was_Set(self, netelem_name, **kwargs):
        self.networkElementBridgemodeGenKeywords.bridgemode_set_mode(netelem_name, 'customer-bridge', **kwargs)
        self.networkElementBridgemodeGenKeywords.bridgemode_verify_customer_bridge(netelem_name,  wait_for=True, max_wait=10)
