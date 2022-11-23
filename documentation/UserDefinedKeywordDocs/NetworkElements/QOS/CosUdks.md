# CosUdks
Library Scope: N/A<br>
Named Arguments: Supported

## Introduction
Documentation for resource file CosUdks.

## Shortcuts
[Add Ports to IRL Port Group and Verify it was Added](#Add_Ports_to_IRL_Port_Group_and_Verify_it_was_Added) | [Add Ports to TXQ Port Group and Verify it was Added](#Add_Ports_to_TXQ_Port_Group_and_Verify_it_was_Added) | [Configure COS Setting IRL and Verify it was Set](#Configure_COS_Setting_IRL_and_Verify_it_was_Set) | [Configure COS Setting Priority and Verify it was Set](#Configure_COS_Setting_Priority_and_Verify_it_was_Set) | [Configure COS Setting TOS and Verify it was Set](#Configure_COS_Setting_TOS_and_Verify_it_was_Set) | [Configure COS Setting TXQ and Verify it was Set](#Configure_COS_Setting_TXQ_and_Verify_it_was_Set) | [Configure Port Priority and Verify it was Set](#Configure_Port_Priority_and_Verify_it_was_Set) | [Configure Port Queue Profile and Verify](#Configure_Port_Queue_Profile_and_Verify) | [Create IRL and Verify it was Created](#Create_IRL_and_Verify_it_was_Created) | [Create IRL Port Group and Verify it was Created](#Create_IRL_Port_Group_and_Verify_it_was_Created) | [Create QOS Profile and Verify it was Created](#Create_QOS_Profile_and_Verify_it_was_Created) | [Create TXQ Port Group and Verify it was Created](#Create_TXQ_Port_Group_and_Verify_it_was_Created) | [Disable COS and Verify it was Disabled](#Disable_COS_and_Verify_it_was_Disabled) | [Enable COS and Verify it was Enabled](#Enable_COS_and_Verify_it_was_Enabled) | [Remove COS Index and Verify it was Removed](#Remove_COS_Index_and_Verify_it_was_Removed) | [Remove IRL and Verify it was Removed](#Remove_IRL_and_Verify_it_was_Removed) | [Remove IRL Port Group and Verify it was Removed](#Remove_IRL_Port_Group_and_Verify_it_was_Removed) | [Remove QOS Profile and Verify it was Removed](#Remove_QOS_Profile_and_Verify_it_was_Removed) | [Remove TXQ Port Group and Verify it was Removed](#Remove_TXQ_Port_Group_and_Verify_it_was_Removed) | [Set QOS Scheduler to Strict Priority and Verify it was Set](#Set_QOS_Scheduler_to_Strict_Priority_and_Verify_it_was_Set) | [Set QOS Scheduler to Weighted Round Robin and Verify it was Set](#Set_QOS_Scheduler_to_Weighted_Round_Robin_and_Verify_it_was_Set)
***

## Keywords
| Keyword | Arguments | Documentation |
|---------|-----------|---------------|
| <a name="Add_Ports_to_IRL_Port_Group_and_Verify_it_was_Added"></a>Add Ports to IRL Port Group and Verify it was Added | netelem_name, group, ports |  |
| <a name="Add_Ports_to_TXQ_Port_Group_and_Verify_it_was_Added"></a>Add Ports to TXQ Port Group and Verify it was Added | netelem_name, group, ports |  |
| <a name="Configure_COS_Setting_IRL_and_Verify_it_was_Set"></a>Configure COS Setting IRL and Verify it was Set | netelem_name, cos_index, irl_index, priority=${None} |  |
| <a name="Configure_COS_Setting_Priority_and_Verify_it_was_Set"></a>Configure COS Setting Priority and Verify it was Set | netelem_name, cos_index, priority |  |
| <a name="Configure_COS_Setting_TOS_and_Verify_it_was_Set"></a>Configure COS Setting TOS and Verify it was Set | netelem_name, cos_index, tos |  |
| <a name="Configure_COS_Setting_TXQ_and_Verify_it_was_Set"></a>Configure COS Setting TXQ and Verify it was Set | netelem_name, cos_index, txq |  |
| <a name="Configure_Port_Priority_and_Verify_it_was_Set"></a>Configure Port Priority and Verify it was Set | netelem_name, netelem_port, priority |  |
| <a name="Configure_Port_Queue_Profile_and_Verify"></a>Configure Port Queue Profile and Verify | netelem_name, netelem_tgen_port, qos_profile |  |
| <a name="Create_IRL_and_Verify_it_was_Created"></a>Create IRL and Verify it was Created | netelem_name, group, irl_index, rate, unit=pps |  |
| <a name="Create_IRL_Port_Group_and_Verify_it_was_Created"></a>Create IRL Port Group and Verify it was Created | netelem_name, group |  |
| <a name="Create_QOS_Profile_and_Verify_it_was_Created"></a>Create QOS Profile and Verify it was Created | netelem_name, qos_profiles |  |
| <a name="Create_TXQ_Port_Group_and_Verify_it_was_Created"></a>Create TXQ Port Group and Verify it was Created | netelem_name, group |  |
| <a name="Disable_COS_and_Verify_it_was_Disabled"></a>Disable COS and Verify it was Disabled | netelem_name |  |
| <a name="Enable_COS_and_Verify_it_was_Enabled"></a>Enable COS and Verify it was Enabled | netelem_name |  |
| <a name="Remove_COS_Index_and_Verify_it_was_Removed"></a>Remove COS Index and Verify it was Removed | netelem_name, cos_index |  |
| <a name="Remove_IRL_and_Verify_it_was_Removed"></a>Remove IRL and Verify it was Removed | netelem_name, group, irl_index |  |
| <a name="Remove_IRL_Port_Group_and_Verify_it_was_Removed"></a>Remove IRL Port Group and Verify it was Removed | netelem_name, group |  |
| <a name="Remove_QOS_Profile_and_Verify_it_was_Removed"></a>Remove QOS Profile and Verify it was Removed | netelem_name, qos_profiles |  |
| <a name="Remove_TXQ_Port_Group_and_Verify_it_was_Removed"></a>Remove TXQ Port Group and Verify it was Removed | netelem_name, group |  |
| <a name="Set_QOS_Scheduler_to_Strict_Priority_and_Verify_it_was_Set"></a>Set QOS Scheduler to Strict Priority and Verify it was Set | netelem_name, group |  |
| <a name="Set_QOS_Scheduler_to_Weighted_Round_Robin_and_Verify_it_was_Set"></a>Set QOS Scheduler to Weighted Round Robin and Verify it was Set | netelem_name, group |  |
