from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementGvrpGenKeywords import NetworkElementGvrpGenKeywords


class GvrpUdks():
    def __init__(self) -> None:
        self.networkElementGvrpGenKeywords = NetworkElementGvrpGenKeywords()

    def Enable_GVRP_and_Verify_it_is_Enabled(self, device_names, **kwargs):
        self.networkElementGvrpGenKeywords.gvrp_enable_global(device_names, **kwargs)
        self.networkElementGvrpGenKeywords.gvrp_verify_enabled(device_names, **kwargs)

    def Disable_GVRP_and_Verify_it_was_Disabled(self, device_names, **kwargs):
        self.networkElementGvrpGenKeywords.gvrp_disable_global(device_names, **kwargs)
        self.networkElementGvrpGenKeywords.gvrp_verify_disabled(device_names, **kwargs)

    def Enable_GVRP_on_Port_and_Verify_it_was_Enabled(self, device_names,  ports, **kwargs):
        self.networkElementGvrpGenKeywords.gvrp_enable_port(device_names,  ports, **kwargs)
        self.networkElementGvrpGenKeywords.gvrp_verify_port_enabled(device_names,  ports, **kwargs)

    def Disable_GVRP_on_Port_and_Verify_it_was_Disabled(self, device_names,  ports, **kwargs):
        self.networkElementGvrpGenKeywords.gvrp_disable_port(device_names,  ports, **kwargs)
        self.networkElementGvrpGenKeywords.gvrp_verify_port_disabled(device_names,  ports, **kwargs)
