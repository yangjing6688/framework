from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementHostinformationGenKeywords import NetworkElementHostinformationGenKeywords


class HostInformationUdks():
    def __init__(self):
        self.host = NetworkElementHostinformationGenKeywords()

    def Configure_System_Prompt_and_Verify_it_is_Set(self, netelem_name, prompt, **kwargs):
        """  Configures the system prompt and verifies the setting
        ...              This has the same effect as configuring the host name """
        self.host.hostinformation_set_prompt(netelem_name, prompt, **kwargs)
        self.host.Hostinformation_verify_system_prompt(netelem_name, prompt, **kwargs)

    def Restore_System_Prompt_to_Default_and_Verify(self,  netelem_name, prompt, **kwargs):
        """  Restores the system prompt to the factory default setting and verifies the setting """
        self.host.hostinformation_clear_prompt(netelem_name, prompt, **kwargs)
        self.host.hostinformation_verify_system_prompt(netelem_name, prompt, **kwargs)
