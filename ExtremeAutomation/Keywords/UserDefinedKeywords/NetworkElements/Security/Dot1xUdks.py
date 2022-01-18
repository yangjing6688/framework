from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementDot1xGenKeywords import NetworkElementDot1xGenKeywords


class Dot1xUdks():
    def __init__(self) -> None:
        self.networkElementDot1xGenKeywords = NetworkElementDot1xGenKeywords()

    def Enable_Dot1x_and_Verify_it_is_Enabled(self, netelem_name, **kwargs):
        self.networkElementDot1xGenKeywords.dot1x_enable_global(netelem_name, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_verify_enabled(netelem_name, **kwargs)

    def Enable_Dot1x_Port_and_Verify_it_is_Enabled(self, netelem_name,    port_list, **kwargs):
        self.networkElementDot1xGenKeywords.dot1x_enable_port(netelem_name,    port_list, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_verify_port_enabled(netelem_name,    port_list, **kwargs)

    def Enable_Dot1x_on_Netelem_and_Ports_and_Verify(self, netelem_name,    ports, **kwargs):
        self.networkElementDot1xGenKeywords.dot1x_enable_global(netelem_name, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_verify_enabled(netelem_name, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_enable_port(netelem_name,    ports, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_verify_port_enabled(netelem_name,    ports, **kwargs)

    def Set_Dot1x_Idle_Timeout_and_Verify(self, netelem_name,    timeout, **kwargs):
        self.networkElementDot1xGenKeywords.dot1x_set_global_idle_timeout(netelem_name,    timeout, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_verify_idle_timeout(netelem_name,    timeout, **kwargs)

    def Set_Dot1x_Session_Timeout_and_Verify(self, netelem_name,    timeout, **kwargs):
        self.networkElementDot1xGenKeywords.dot1x_set_global_session_timeout(netelem_name,    timeout, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_verify_session_timeout(netelem_name,    timeout, **kwargs)

    def Set_Dot1x_Port_Reauth_Period_and_Verify(self, netelem_name,    ports,      interval, **kwargs):
        self.networkElementDot1xGenKeywords.dot1x_set_port_reauthperiod(netelem_name,    interval,   ports, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_verify_port_reauth_period(netelem_name,    ports,      interval, **kwargs)

    def Enable_Dot1x_Port_Reauth_and_Verify(self, netelem_name,    ports, **kwargs):
        self.networkElementDot1xGenKeywords.dot1x_enable_port_reauth(netelem_name,    ports, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_verify_port_reauth_enabled(netelem_name,    ports, **kwargs)

    def Disable_Dot1x_and_Verify_it_is_Disabled(self, netelem_name, **kwargs):
        self.networkElementDot1xGenKeywords.dot1x_disable_global(netelem_name, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_verify_disabled(netelem_name, **kwargs)

    def Disable_Dot1x_Port_and_Verify_it_is_Disabled(self, netelem_name,    port_list, **kwargs):
        self.networkElementDot1xGenKeywords.dot1x_disable_port(netelem_name,    port_list, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_verify_port_disabled(netelem_name,    port_list, **kwargs)

    def Disable_Dot1x_on_Netelem_and_Ports_and_Verify(self, netelem_name,    ports, **kwargs):
        self.networkElementDot1xGenKeywords.dot1x_disable_global(netelem_name, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_verify_disabled(netelem_name, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_disable_port(netelem_name,    ports, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_verify_port_disabled(netelem_name,    ports, **kwargs)

    def Clear_Dot1x_Port_Reauth_Period_and_Verify(self, netelem_name,    ports,    interval, **kwargs):
        self.networkElementDot1xGenKeywords.dot1x_clear_port_reauthperiod(netelem_name,    ports, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_verify_port_reauth_period(netelem_name,    ports,    interval, **kwargs)

    def Disable_Dot1x_Port_Reauth_and_Verify(self, netelem_name,    ports, **kwargs):
        self.networkElementDot1xGenKeywords.dot1x_disable_port_reauth(netelem_name,    ports, **kwargs)
        self.networkElementDot1xGenKeywords.dot1x_verify_port_reauth_disabled(netelem_name,    ports, **kwargs)

