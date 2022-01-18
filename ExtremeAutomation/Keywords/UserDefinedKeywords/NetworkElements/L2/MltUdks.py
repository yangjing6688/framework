from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementMltGenKeywords import NetworkElementMltGenKeywords


class MltUdks():
    def __init__(self) -> None:
        self.networkElementMltGenKeywords = NetworkElementMltGenKeywords()

    def Create_Mlt_and_Verify_it_Exists(self, netelem_name,  mlt_id, **kwargs):
        """  reates_an_MLT, enables_it, and_verifies_it_exists """
        self.networkElementMltGenKeywords.mlt_create_id(netelem_name,  mlt_id, **kwargs)
        self.networkElementMltGenKeywords.mlt_verify_id_exists(netelem_name,  mlt_id, **kwargs)

    def Remove_Mlt_and_Verify_it_is_Removed(self, netelem_name,  mlt_id, **kwargs):
        """  Removes_an_MLT_and_verifies_it_is_removed  """
        self.networkElementMltGenKeywords.mlt_delete_id(netelem_name,  mlt_id, **kwargs)
        self.networkElementMltGenKeywords.mlt_verify_id_does_not_exist(netelem_name,  mlt_id, **kwargs)

    def Add_Port_to_Mlt_and_Verify_it_is_Added(self, netelem_name,  mlt_id,  port, **kwargs):
        """  Adds_a_port_to_an_MLT_and_verifies_it_is_added """
        self.networkElementMltGenKeywords.mlt_set_port_member(netelem_name,  mlt_id,  port, **kwargs)
        self.networkElementMltGenKeywords.mlt_verify_port_exists(netelem_name,  mlt_id,  port, **kwargs)

    def Remove_Port_From_Mlt_and_Verify_it_is_Removed(self, netelem_name,  mlt_id,  port, **kwargs):
        """  Removes_a_port_from_an_MLT_and_verifies_it_is_removed """
        self.networkElementMltGenKeywords.mlt_clear_port_member(netelem_name,  mlt_id,  port, **kwargs)
        self.networkElementMltGenKeywords.mlt_verify_port_does_not_exist(netelem_name,  mlt_id,  port, **kwargs)
