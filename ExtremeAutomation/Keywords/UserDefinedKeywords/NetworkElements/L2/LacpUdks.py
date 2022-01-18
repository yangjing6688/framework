from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementLacpGenKeywords import NetworkElementLacpGenKeywords


class LacpUdks():
    def __init__(self):
        self.networkElementLacpGenKeywords = NetworkElementLacpGenKeywords()

    def Create_Two_Port_LAG_on_Single_Netelem_and_Verify(self, netelem_name, netelem_lag_id_or_main_port,
                                                         netelem_lag_key_or_main_port, netelem_port_a, netelem_port_b, **kwargs):
        self.networkElementLacpGenKeywords.lacp_create_lag(netelem_name,  netelem_lag_id_or_main_port,  netelem_port_a, netelem_lag_key_or_main_port, **kwargs)
        self.networkElementLacpGenKeywords.lacp_set_lag_port(netelem_name,  netelem_lag_id_or_main_port, netelem_port_b, netelem_lag_key_or_main_port, **kwargs)
        self.networkElementLacpGenKeywords.lacp_verify_port_in_lag_group(netelem_name,  netelem_lag_id_or_main_port,  netelem_port_a, wait_for=True)
        self.networkElementLacpGenKeywords.lacp_verify_port_in_lag_group(netelem_name,  netelem_lag_id_or_main_port,  netelem_port_b, wait_for=True)

    def Delete_Multi_Port_LAG_on_Single_Netelem_and_Verify(self, netelem_name,  netelem_lag_id,  netelem_port_list, **kwargs):
        self.networkElementLacpGenKeywords.lacp_delete_lag(netelem_name,  netelem_lag_id,  netelem_port_list, ignore_cli_feedback=True)
        self.networkElementLacpGenKeywords.lacp_verify_port_not_in_lag_group(netelem_name,  netelem_lag_id,  netelem_port_list, **kwargs)

    def Create_Two_Port_LAG_on_Two_Netelems_and_Verify(self, netelem_a_name, netelem_a_lag_id_or_main_port, netelem_a_lag_key_or_main_port,
                                                       netelem_a_port_a, netelem_a_port_b,
                                                       netelem_b_name, netelem_b_lag_id_or_main_port,
                                                       netelem_b_lag_key_or_main_port,
                                                       netelem_b_port_a, netelem_b_port_b, **kwargs):
        self.Create_Two_Port_LAG_on_Single_Netelem_and_Verify(
                  netelem_a_name,    netelem_a_lag_id_or_main_port,    netelem_a_lag_key_or_main_port,
                  netelem_a_port_a,  netelem_a_port_b, **kwargs)
        self.Create_Two_Port_LAG_on_Single_Netelem_and_Verify(
                  netelem_b_name,    netelem_b_lag_id_or_main_port,    netelem_b_lag_key_or_main_port,
                  netelem_b_port_a,  netelem_b_port_b, **kwargs)

    def Delete_Multi_Port_LAG_on_Two_Netelems_and_Verify(self, netelem_a_name,  netelem_a_lag_id,  netelem_a_port_list,
                                                         netelem_b_name,  netelem_b_lag_id,  netelem_b_port_list, **kwargs):
        self.Delete_Multi_Port_LAG_on_Single_Netelem_and_Verify(netelem_a_name,  netelem_a_lag_id,  netelem_a_port_list, **kwargs)
        self.Delete_Multi_Port_LAG_on_Single_Netelem_and_Verify(netelem_b_name,  netelem_b_lag_id,  netelem_b_port_list, **kwargs)
