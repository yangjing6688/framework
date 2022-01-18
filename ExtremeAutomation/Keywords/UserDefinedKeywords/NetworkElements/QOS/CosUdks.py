from ExtremeAutomation.Keywords.NetworkElementKeywords.StaticKeywords.NetworkElementCosUtilsKeywords import NetworkElementCosUtilsKeywords
from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementCosGenKeywords import NetworkElementCosGenKeywords


class CosUdks():
    def __init__(self) -> None:
        self.NetworkElementCosKeywords = NetworkElementCosUtilsKeywords()
        self.NetworkElementCosGenKeywords = NetworkElementCosGenKeywords()

    def Enable_COS_and_Verify_it_was_Enabled(self, netelem_name, **kwargs):
        self.NetworkElementCosGenKeywords.cos_enable_state(netelem_name, **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_enabled(netelem_name, **kwargs)

    def Disable_COS_and_Verify_it_was_Disabled(self, netelem_name, **kwargs):
        self.NetworkElementCosGenKeywords.cos_disable_state(netelem_name, **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_disabled(netelem_name, **kwargs)

    def Create_IRL_Port_Group_and_Verify_it_was_Created(self, netelem_name,  group, **kwargs):
        self.NetworkElementCosGenKeywords.cos_create_port_group(netelem_name,  group, 'irl', **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_irl_port_group_exists(netelem_name,  group, **kwargs)

    def Remove_IRL_Port_Group_and_Verify_it_was_Removed(self, netelem_name,  group, **kwargs):
        self.NetworkElementCosGenKeywords.cos_delete_port_group(netelem_name,  group, 'irl', **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_irl_port_group_does_not_exist(netelem_name,  group, **kwargs)

    def Add_Ports_to_IRL_Port_Group_and_Verify_it_was_Added(self, netelem_name,  group,  ports, **kwargs):
        self.NetworkElementCosGenKeywords.cos_set_port_group_port(netelem_name,  group,  ports, 'irl', **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_port_in_irl_port_group(netelem_name,  group,  ports, **kwargs)

    def Create_IRL_and_Verify_it_was_Created(self, netelem_name,  group,  irl_index,  rate,  unit='pps', **kwargs):
        self.NetworkElementCosGenKeywords.cos_set_port_resource_irl(netelem_name,  group,  irl_index,  rate,  unit, **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_irl_configured(netelem_name,  group,  irl_index,  rate,  unit, **kwargs)

    def Remove_IRL_and_Verify_it_was_Removed(self, netelem_name,  group,  irl_index, **kwargs):
        self.NetworkElementCosGenKeywords.cos_clear_irl(netelem_name,  group,  irl_index, **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_irl_not_configured(netelem_name,  group,  irl_index, **kwargs)

    def Create_TXQ_Port_Group_and_Verify_it_was_Created(self, netelem_name,  group, **kwargs):
        self.NetworkElementCosGenKeywords.cos_create_port_group(netelem_name,  group,  'txq',  **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_txq_port_group_exists(netelem_name,  group, **kwargs)

    def Remove_TXQ_Port_Group_and_Verify_it_was_Removed(self, netelem_name,  group, **kwargs):
        self.NetworkElementCosGenKeywords.cos_delete_port_group(netelem_name,  group,  'txq', **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_txq_port_group_does_not_exist(netelem_name,  group, **kwargs)

    def Add_Ports_to_TXQ_Port_Group_and_Verify_it_was_Added(self, netelem_name,  group,  ports, **kwargs):
        self.NetworkElementCosGenKeywords.cos_set_port_group_port(netelem_name,  group,  ports,  'txq', **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_port_in_txq_port_group(netelem_name,  group,  ports, **kwargs)

    def Create_QOS_Profile_and_Verify_it_was_Created(self, netelem_name,  qos_profiles, **kwargs):
        self.NetworkElementCosGenKeywords.cos_create_qos_profile(netelem_name,  qos_profiles, **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_qos_profile_exists(netelem_name,  qos_profiles, **kwargs)

    def Remove_QOS_Profile_and_Verify_it_was_Removed(self, netelem_name,  qos_profiles, **kwargs):
        self.NetworkElementCosGenKeywords.cos_delete_qos_profile(netelem_name,  qos_profiles, **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_qos_profile_does_not_exist(netelem_name,  qos_profiles, **kwargs)
        self.NetworkElementCosKeywords.Set_Variabl

    def Configure_COS_Setting_IRL_and_Verify_it_was_Set(self, netelem_name,  cos_index,  irl_index,  priority=None,  qp=None, **kwargs):
        if int(cos_index) <= 7:
            cos_val = cos_index
            qp_gen = 'qp1'
        else:
            cos_val = 0
        if priority is None:
            priority = cos_val
        # qp_val = int(priority) + 1
        if int(cos_index) <= 7:
            cos_val = cos_index
        else:
            cos_val = 0
        if qp is None:
            qp = qp_gen
        if int(cos_index) <= 7:
            self.NetworkElementCosGenKeywords.cos_set_irl_settings_cos_under_seven(netelem_name,  cos_index,  irl_index,  qp, **kwargs)
        else:
            self.NetworkElementCosGenKeywords.cos_set_irl_settings(netelem_name,  cos_index,  irl_index,  priority,  qp, **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_index_txq(netelem_name,  cos_index,  irl_index, **kwargs)

    def Configure_COS_Setting_TXQ_and_Verify_it_was_Set(self, netelem_name,  cos_index,  txq,  qp=None, **kwargs):
        qp_val = int(txq) + 1
        if qp is None:
            qp = qp_val
        if int(cos_index) <= 7:
            self.NetworkElementCosGenKeywords.cos_set_txq_settings_cos_under_seven(netelem_name,  cos_index,  txq,  qp, **kwargs)
        else:
            self.NetworkElementCosGenKeywords.cos_set_txq_settings(netelem_name,  cos_index,  txq,  qp, **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_index_txq(netelem_name,  cos_index,  txq, **kwargs)

    def Configure_COS_Setting_Priority_and_Verify_it_was_Set(self, netelem_name,  cos_index,  priority,  qp=None, **kwargs):
        qp_val = int(priority) + 1
        if qp is None:
            qp = qp_val
        if int(cos_index) <= 7:
            self.NetworkElementCosGenKeywords.cos_set_priority_settings_cos_under_seven(netelem_name,  cos_index,  priority,  qp, **kwargs)
        else:
            self.NetworkElementCosGenKeywords.cos_set_priority_settings(netelem_name,  cos_index,  priority,  qp, **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_index_priority(netelem_name,  cos_index,  priority, **kwargs)

    def Configure_COS_Setting_Priority(self, netelem_name,  cos_index,  priority,  qp=None, **kwargs):
        qp_val = int(priority) + 1
        if qp is None:
            qp = qp_val
        if int(cos_index) <= 7:
            self.NetworkElementCosGenKeywords.cos_set_priority_settings_cos_under_seven(netelem_name,  cos_index,  priority,  qp, **kwargs)
        else:
            self.NetworkElementCosGenKeywords.cos_set_priority_settings(netelem_name,  cos_index,  priority,  qp, **kwargs)

    def Configure_COS_Setting_TOS_and_Verify_it_was_Set(self, netelem_name,  cos_index,  tos,  qp=None, **kwargs):
        qp_val = int(cos_index), + 1
        if qp is None:
            qp = qp_val
        if int(cos_index) <= 7:
            self.NetworkElementCosGenKeywords.cos_set_tos_settings_cos_under_seven(netelem_name,  cos_index,  tos,  qp, **kwargs)
        else:
            self.NetworkElementCosGenKeywords.cos_set_tos_settings(netelem_name,  cos_index,  tos,  qp, **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_index_tos(netelem_name,  cos_index,  tos, **kwargs)

    def Set_QOS_Scheduler_to_Strict_Priority_and_Verify_it_was_Set(self, netelem_name, group, **kwargs):
        self.NetworkElementCosGenKeywords.cos_set_qos_scheduler(netelem_name,  group,  'strict-priority',  **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_qos_scheduler_strict_priority(netelem_name,  group, **kwargs)

    def Set_QOS_Scheduler_to_Weighted_Round_Robin_and_Verify_it_was_Set(self, netelem_name, group, **kwargs):
        self.NetworkElementCosGenKeywords.cos_set_qos_scheduler(netelem_name,  group,  'weighted-round-robin',  **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_qos_scheduler_weighted_round_robin(netelem_name,  group, **kwargs)

    def Remove_COS_Index_and_Verify_it_was_Removed(self, netelem_name, cos_index, **kwargs):
        self.NetworkElementCosGenKeywords.cos_clear_index(netelem_name, cos_index, **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_index_does_not_exist(netelem_name, cos_index, **kwargs)

    def Configure_Port_Priority_and_Verify_it_was_Set(self, netelem_name, netelem_port, priority, **kwargs):
        self.NetworkElementCosGenKeywords.cos_set_port_priority(netelem_name,  netelem_port,  priority, **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_port_priority(netelem_name,  netelem_port,  priority, **kwargs)

    def Configure_Port_Queue_Profile_and_Verify(self, netelem_name,  netelem_tgen_port,  qos_profile, **kwargs):
        self.NetworkElementCosGenKeywords.cos_set_port_qos_profile(netelem_name,  netelem_tgen_port,  qos_profile, **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_port_qos_profile(netelem_name,  netelem_tgen_port,  qos_profile, **kwargs)

    def Configure_TXQ_Weights_and_Verify(self, netelem_name,  port_group,  weight_mapping, **kwargs):
        self.NetworkElementCosKeywords.configure_txq_weights(netelem_name,  port_group,  weight_mapping, **kwargs)
        self.NetworkElementCosGenKeywords.cos_verify_txq_wfq_weights(netelem_name,  port_group,  weight_mapping, **kwargs)