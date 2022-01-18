from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementMultiauthGenKeywords import NetworkElementMultiauthGenKeywords


class MultiAuthUdks():
    def __init__(self) -> None:
        self.networkElementMultiauthGenKeywords = NetworkElementMultiauthGenKeywords()

    def Configure_Dot1x_Idle_Timeout_and_Verify(self, netelem_name,  timeout, **kwargs):
        self.networkElementMultiauthGenKeywords.multiauth_set_idle_type_timeout(netelem_name,  timeout, **kwargs)
        self.networkElementMultiauthGenKeywords.multiauth_verify_dot1x_idle_timeout(netelem_name,  timeout,  **kwargs)

    def Configure_Dot1x_Session_Timeout_and_Verify(self, netelem_name,  timeout, **kwargs):
        self.networkElementMultiauthGenKeywords.multiauth_set_session_type_timeout(netelem_name,  'dot1x', timeout, **kwargs)
        self.networkElementMultiauthGenKeywords.multiauth_verify_dot1x_session_timeout(netelem_name,  timeout, **kwargs)

    def Configure_MacAuth_Idle_Timeout_and_Verify(self, netelem_name,  timeout, **kwargs):
        self.networkElementMultiauthGenKeywords.multiauth_set_idle_type_timeout(netelem_name,  'mac', timeout, **kwargs)
        self.networkElementMultiauthGenKeywords.multiauth_verify_mac_idle_timeout(netelem_name,  timeout, **kwargs)

    def Configure_MacAuth_Session_Timeout_and_Verify(self, netelem_name,  timeout, **kwargs):
        self.networkElementMultiauthGenKeywords.multiauth_set_session_type_timeout(netelem_name,  'mac', timeout, **kwargs)
        self.networkElementMultiauthGenKeywords.multiauth_verify_mac_session_timeout(netelem_name,  timeout, **kwargs)

    def Configure_WebAuth_Idle_Timeout_and_Verify(self, netelem_name,  timeout, **kwargs):
        self.networkElementMultiauthGenKeywords.multiauth_set_idle_type_timeout(netelem_name,  'web', timeout, **kwargs)
        self.networkElementMultiauthGenKeywords.multiauth_verify_web_idle_timeout(netelem_name,  timeout, **kwargs)

    def Configure_WebAuth_Session_Timeout_and_Verify(self, netelem_name,  timeout, **kwargs):
        self.networkElementMultiauthGenKeywords.multiauth_set_session_type_timeout(netelem_name,  'web', timeout, **kwargs)
        self.networkElementMultiauthGenKeywords.multiauth_verify_web_session_timeout(netelem_name,  timeout, **kwargs)

    def Clear_Dot1x_Idle_Timeout_and_Verify(self, netelem_name,  timeout, **kwargs):
        self.networkElementMultiauthGenKeywords.multiauth_clear_idle_type_timeout(netelem_name,  'dot1x', **kwargs)
        self.networkElementMultiauthGenKeywords.multiauth_verify_dot1x_idle_timeout(netelem_name,  timeout, **kwargs)

    def Clear_Dot1x_Session_Timeout_and_Verify(self, netelem_name,  timeout, **kwargs):
        self.networkElementMultiauthGenKeywords.multiauth_clear_session_type_timeout(netelem_name,  'dot1x', **kwargs)
        self.networkElementMultiauthGenKeywords.multiauth_verify_dot1x_session_timeout(netelem_name,  timeout, **kwargs)

    def Clear_MacAuth_Idle_Timeout_and_Verify(self, netelem_name,  timeout, **kwargs):
        self.networkElementMultiauthGenKeywords.multiauth_clear_idle_type_timeout(netelem_name,  'mac', **kwargs)
        self.networkElementMultiauthGenKeywords.multiauth_verify_mac_idle_timeout(netelem_name,  timeout, **kwargs)

    def Clear_MacAuth_Session_Timeout_and_Verify(self, netelem_name,  timeout, **kwargs):
        self.networkElementMultiauthGenKeywords.multiauth_clear_session_type_timeout(netelem_name,  'mac', **kwargs)
        self.networkElementMultiauthGenKeywords.multiauth_verify_mac_session_timeout(netelem_name,  timeout, **kwargs)

    def Clear_WebAuth_Idle_Timeout_and_Verify(self, netelem_name,  timeout, **kwargs):
        self.networkElementMultiauthGenKeywords.multiauth_clear_idle_type_timeout(netelem_name,  'web', **kwargs)
        self.networkElementMultiauthGenKeywords.multiauth_verify_web_idle_timeout(netelem_name,  timeout, **kwargs)

    def Clear_WebAuth_Session_Timeout_and_Verify(self, netelem_name,  timeout, **kwargs):
        self.networkElementMultiauthGenKeywords.multiauth_clear_session_type_timeout(netelem_name,  'web', **kwargs)
        self.networkElementMultiauthGenKeywords.multiauth_verify_web_session_timeout(netelem_name,  timeout, **kwargs)

    def Restore_Timeout_Setting_to_Default_for_All_Auth_Methods(self, netelem_name, default_idle_timeout, default_session_timeout, **kwargs):
        self.Clear_Dot1x_Idle_Timeout_and_Verify(netelem_name,  default_idle_timeout, **kwargs)
        self.Clear_Dot1x_Session_Timeout_and_Verify(netelem_name,  default_session_timeout, **kwargs)
        self.Clear_MacAuth_Idle_Timeout_and_Verify(netelem_name,  default_idle_timeout, **kwargs)
        self.Clear_MacAuth_Session_Timeout_and_Verify(netelem_name,  default_session_timeout, **kwargs)
        self.Clear_WebAuth_Idle_Timeout_and_Verify(netelem_name,  default_idle_timeout, **kwargs)
        self.Clear_WebAuth_Session_Timeout_and_Verify(netelem_name,  default_session_timeout, **kwargs)
