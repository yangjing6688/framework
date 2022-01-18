from ExtremeAutomation.Library.Utils.DotDict import DotDict
from ExtremeAutomation.Library.Device.Common.PlatformVariables.Library.BasePlatformVariables \
    import BasePlatformVariables


def create_instance():
    return ExosPlatformVariables()


class ExosPlatformVariables(BasePlatformVariables):
    def __init__(self):
        super(ExosPlatformVariables, self).__init__()

        # multiauth Platform Variables
        self.vars["multiauth"] = DotDict()
        self.vars["multiauth"]["agent_type_dot1x"] = "dot1x"
        self.vars["multiauth"]["agent_type_mac"] = "mac"
        self.vars["multiauth"]["agent_type_web"] = "web-based"
        self.vars["multiauth"]["default_idle_timeout"] = "300"
        self.vars["multiauth"]["default_session_timeout"] = "0"

        # radius Platform Variables
        self.vars["radius"] = DotDict()
        self.vars["radius"]["radius_max_index"] = "2147483641"

        # policy Platform Variables
        self.vars["policy"] = DotDict()
        self.vars["policy"]["allowed_types"] = \
            "[1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1]"

        # port Platform Variables
        self.vars["port"] = DotDict()
        self.vars["port"]["maximum_untagged_length"] = "1518"
        self.vars["port"]["maximum_untagged_length_plus_1"] = "1519"
        self.vars["port"]["minimum_tagged_length"] = "64"
        self.vars["port"]["maximum_tagged_length"] = "1522"
        self.vars["port"]["maximum_tagged_length_plus_1"] = "1523"
        self.vars["port"]["max_s_tag_length"] = "1518"
        self.vars["port"]["jumbo_max_length_untagged"] = "9220"
        self.vars["port"]["jumbo_max_length_untagged_plus_1"] = "9221"
        self.vars["port"]["jumbo_max_length_tagged"] = "9220"
        self.vars["port"]["jumbo_max_length_tagged_plus_1"] = "9221"

        # cos Platform Variables
        self.vars["cos"] = DotDict()
        self.vars["cos"]["rl_port_group"] = "cos_group"
        self.vars["cos"]["txq_port_group"] = "cos_group"
        self.vars["cos"]["wfq_weights"] = "5,5,10,10,15,15,20,20"

        # lldp Platform Variables
        self.vars["lldp"] = DotDict()
        self.vars["lldp"]["enh_tx_rec_tlv_message"] = "0x000000000700000000000000000000000000000000"
        self.vars["lldp"]["enh_tx_con_tlv_message"] = "0x400000000700000000000000000000000000000000"
        self.vars["lldp"]["link_aggr_tlv_message"] = "0x0000000000"
        self.vars["lldp"]["link_aggr_tlv_subtype"] = "0x03"
        self.vars["lldp"]["mac_phy_tlv_message"] = "0x0100000024"

        # vlan Platform Variables
        self.vars["vlan"] = DotDict()
        self.vars["vlan"]["mgmt_vlan_name"] = "mgmt"
        self.vars["vlan"]["default_vlan_name"] = "Default"
        self.vars["vlan"]["default_vlan"] = "1"
        self.vars["vlan"]["default_description"] = "None"
