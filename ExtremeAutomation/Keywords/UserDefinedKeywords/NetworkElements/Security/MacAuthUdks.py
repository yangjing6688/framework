from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementMacauthGenKeywords import NetworkElementMacauthGenKeywords


class MacAuthUdks():

    def __init__(self) -> None:
        self.networkElementMacauthGenKeywords = NetworkElementMacauthGenKeywords()

    def Enable_Macauth_and_Verify_it_is_Enabled(self, netelem_name, **kwargs):
        self.networkElementMacauthGenKeywords.macauth_enable(netelem_name, **kwargs)
        self.networkElementMacauthGenKeywords.macauth_verify_enabled(netelem_name, **kwargs)

    def Enable_Macauth_Port_and_Verify_it_is_Enabled(self, netelem_name,  ports, **kwargs):
        self.networkElementMacauthGenKeywords.macauth_set_port_state(netelem_name,  ports,  'enable', **kwargs)
        self.networkElementMacauthGenKeywords.macauth_verify_enabled_on_port(netelem_name,  ports, **kwargs)

    def Disable_Macauth_and_Verify_it_is_Disabled(self, netelem_name,  ports, **kwargs):
        self.networkElementMacauthGenKeywords.macauth_disable(netelem_name, **kwargs)
        self.networkElementMacauthGenKeywords.macauth_verify_disabled(netelem_name, **kwargs)

    def Disable_Macauth_Port_and_Verify_it_is_Disabled(self, netelem_name,  ports, **kwargs):
        self.networkElementMacauthGenKeywords.macauth_set_port_state(netelem_name,  ports,  'disable', **kwargs)
        self.networkElementMacauthGenKeywords.macauth_verify_disabled_on_port(netelem_name,  ports, **kwargs)

    def Enable_Macauth_on_Netelem_and_Ports_and_Verify(self, netelem_name,  ports, **kwargs):
        self.networkElementMacauthGenKeywords.macauth_enable(netelem_name, **kwargs)
        self.networkElementMacauthGenKeywords.macauth_set_port_state(netelem_name,  ports,  'enable', **kwargs)
        self.networkElementMacauthGenKeywords.macauth_verify_enabled(netelem_name, **kwargs)
        self.networkElementMacauthGenKeywords.macauth_verify_enabled_on_port(netelem_name,  ports, **kwargs)

    def Disable_Macauth_on_Netelem_and_Ports_and_Verify(self, netelem_name,  ports, **kwargs):
        self.networkElementMacauthGenKeywords.macauth_disable(netelem_name, **kwargs)
        self.networkElementMacauthGenKeywords.macauth_set_port_state(netelem_name,  ports,  'disable', **kwargs)
        self.networkElementMacauthGenKeywords.macauth_verify_disabled(netelem_name, **kwargs)
        self.networkElementMacauthGenKeywords.macauth_verify_disabled_on_port(netelem_name,  ports, **kwargs)

    def Configure_Macauth_Port_Reauth_Period_and_Verify(self, netelem_name,  ports,  interval, **kwargs):
        self.networkElementMacauthGenKeywords.macauth_set_port_reauthperiod(netelem_name,  ports,  interval, **kwargs)
        self.networkElementMacauthGenKeywords.macauth_verify_port_reauth_period(netelem_name,  ports,  interval, **kwargs)

    def Clear_Macauth_Port_Reauth_Period_and_Verify(self, netelem_name,  ports,  interval, **kwargs):
        self.networkElementMacauthGenKeywords.macauth_clear_port_reauthperiod(netelem_name,  ports, **kwargs)
        self.networkElementMacauthGenKeywords.macauth_verify_port_reauth_period_default(netelem_name,  ports,  interval, **kwargs)

    def Enable_Macauth_Port_Reauth_and_Verify(self, netelem_name,  ports, **kwargs):
        self.networkElementMacauthGenKeywords.macauth_enable_port_reauthentication(netelem_name,  ports, **kwargs)
        self.networkElementMacauthGenKeywords.macauth_verify_reauth_state_enabled(netelem_name,  ports, **kwargs)

    def Disable_Macauth_Port_Reauth_and_Verify(self, netelem_name,  ports, **kwargs):
        self.networkElementMacauthGenKeywords.macauth_disable_port_reauthentication(netelem_name,  ports, **kwargs)
        self.networkElementMacauthGenKeywords.macauth_verify_reauth_state_disabled(netelem_name,  ports, **kwargs)

    def Configure_Macauth_Reauth_Period_Globally_and_Verify(self, netelem_name,  interval, **kwargs):
        self.networkElementMacauthGenKeywords.macauth_set_reauthperiod(netelem_name,  interval, **kwargs)
        self.networkElementMacauthGenKeywords.macauth_verify_reauth_period(netelem_name,  interval, **kwargs)
