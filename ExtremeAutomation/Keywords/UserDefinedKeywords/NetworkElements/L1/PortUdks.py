from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementPortGenKeywords import NetworkElementPortGenKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementSpanningtreeGenKeywords import NetworkElementSpanningtreeGenKeywords
from ExtremeAutomation.Library.Logger.Logger import Logger
import re



class PortUdks():
    def __init__(self) -> None:
        self.logger = Logger()
        self.networkElementPortGenKeywords = NetworkElementPortGenKeywords()
        self.networkElementSpanningtreeGenKeywords = NetworkElementSpanningtreeGenKeywords()

    def Enable_Port_and_Validate_Port_is_Enabled(self, netelem_name, port, **kwargs):
        self.networkElementPortGenKeywords.port_enable_state(netelem_name, port, **kwargs)
        self.networkElementPortGenKeywords.port_verify_admin_enabled(netelem_name, port, **kwargs)

    def Enable_Port_and_Validate_Port_is_Oper_Up(self, netelem_name, port, **kwargs):
        self.networkElementPortGenKeywords.port_enable_state(netelem_name, port, **kwargs)
        self.networkElementPortGenKeywords.port_verify_operational(netelem_name, port, wait_for=True)

    def Disable_Port_and_Validate_Port_is_Disabled(self, netelem_name, port, **kwargs):
        self.networkElementPortGenKeywords.port_disable_state(netelem_name, port, **kwargs)
        self.networkElementPortGenKeywords.port_verify_admin_disabled(netelem_name, port, **kwargs)

    def Enable_Jumbo_Frames_and_Verify_it_is_Enabled(self, netelem_name, port, **kwargs):
        self.networkElementPortGenKeywords.port_enable_jumbo(netelem_name, port, **kwargs)
        self.networkElementPortGenKeywords.port_verify_jumbo_frame_reception_enabled_on_port(netelem_name, port, **kwargs)

    def Disable_Jumbo_Frames_and_Verify_it_is_Disabled(self, netelem_name, port, **kwargs):
        self.networkElementPortGenKeywords.port_disable_jumbo(netelem_name, port, **kwargs)
        self.networkElementPortGenKeywords.port_verify_jumbo_frame_reception_disabled_on_port(netelem_name, port, **kwargs)
    
    # check to see if spanning tree is enabled and if it is, check to make sure the port is in the forwarding state
    def Verify_Xstp_Forwarding_State(self, netelem_name, port, **kwargs):
        spanning_tree_mode = self.networkElementSpanningtreeGenKeywords.spanningtree_verify_mode_mstp(netelem_name, get_only=True)
        regex = re.compile("[0-9]+[ ]+[0-9a-g:]+[ ]+([mstp|rstp]+)")
        return_text = spanning_tree_mode[0][0].cmd_obj.return_text
        output = re.search(regex, return_text)
        if output:
            stpMode = output.group(1)
            self.networkElementSpanningtreeGenKeywords.spanningtree_verify_port_role_forwarding(netelem_name, port=port, sid="0", stp_type=stpMode.lower(), wait_for=True, interval=5, max_wait=30)
        
