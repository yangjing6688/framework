# PolicyUdks
Library Scope: N/A<br>
Named Arguments: Supported

## Introduction
Documentation for resource file PolicyUdks.

## Shortcuts
[Clear Policy Invalid Action and Verify](#Clear_Policy_Invalid_Action_and_Verify) | [Clear Policy Maptable Response and Verify](#Clear_Policy_Maptable_Response_and_Verify) | [Create Mac Source Admin Profile and Verify it was Created](#Create_Mac_Source_Admin_Profile_and_Verify_it_was_Created) | [Create Policy Profile and Verify it Exists](#Create_Policy_Profile_and_Verify_it_Exists) | [Create Policy Profile Untagged Vlan With Pvid and Verify](#Create_Policy_Profile_Untagged_Vlan_With_Pvid_and_Verify) | [Create Policy Profile with COS and COS Status Enabled](#Create_Policy_Profile_with_COS_and_COS_Status_Enabled) | [Create Policy Profile with COS, COS Status, and TCI Overwrite Enabled](#Create_Policy_Profile_with_COS,_COS_Status,_and_TCI_Overwrite_Enabled) | [Create Policy Profile with Name and Verify it Exists](#Create_Policy_Profile_with_Name_and_Verify_it_Exists) | [Create Policy Profile With PVID and PVID Status Enabled](#Create_Policy_Profile_With_PVID_and_PVID_Status_Enabled) | [Create Policy Profile with PVID and PVID Status Enabled and TCI-Overwrite Disabled](#Create_Policy_Profile_with_PVID_and_PVID_Status_Enabled_and_TCI-Overwrite_Disabled) | [Create Policy Profile with PVID and PVID Status Enabled and TCI-Overwrite Enabled](#Create_Policy_Profile_with_PVID_and_PVID_Status_Enabled_and_TCI-Overwrite_Enabled) | [Create Policy Profile with PVID, PVID Status, COS, and COS Status Enabled](#Create_Policy_Profile_with_PVID,_PVID_Status,_COS,_and_COS_Status_Enabled) | [Create Policy Profile with PVID, PVID Status, COS, COS Status, and TCI Overwrite Enabled](#Create_Policy_Profile_with_PVID,_PVID_Status,_COS,_COS_Status,_and_TCI_Overwrite_Enabled) | [Create Port Admin Profile and Verify it Exists](#Create_Port_Admin_Profile_and_Verify_it_Exists) | [Disable Policy and Verify it is Disabled](#Disable_Policy_and_Verify_it_is_Disabled) | [Enable Policy and Verify it is Enabled](#Enable_Policy_and_Verify_it_is_Enabled) | [Remove Mac Source Admin Profile and Verify it was Removed](#Remove_Mac_Source_Admin_Profile_and_Verify_it_was_Removed) | [Remove Policy Profile and Verify it was Removed](#Remove_Policy_Profile_and_Verify_it_was_Removed) | [Remove Port Admin Profile and Verify it was Removed](#Remove_Port_Admin_Profile_and_Verify_it_was_Removed) | [Set Policy Access Control and Verify](#Set_Policy_Access_Control_and_Verify) | [Set Policy Invalid Action and Verify](#Set_Policy_Invalid_Action_and_Verify) | [Set Policy Maptable Response and Verify](#Set_Policy_Maptable_Response_and_Verify)
***

## Keywords
| Keyword | Arguments | Documentation |
|---------|-----------|---------------|
| <a name="Clear_Policy_Invalid_Action_and_Verify"></a>Clear Policy Invalid Action and Verify | netelem_name, policy_action |  |
| <a name="Clear_Policy_Maptable_Response_and_Verify"></a>Clear Policy Maptable Response and Verify | netelem_name, policy_maptable_response |  |
| <a name="Create_Mac_Source_Admin_Profile_and_Verify_it_was_Created"></a>Create Mac Source Admin Profile and Verify it was Created | netelem_name, mac_source, port, profile_id |  |
| <a name="Create_Policy_Profile_and_Verify_it_Exists"></a>Create Policy Profile and Verify it Exists | netelem_name, profile_id |  |
| <a name="Create_Policy_Profile_Untagged_Vlan_With_Pvid_and_Verify"></a>Create Policy Profile Untagged Vlan With Pvid and Verify | netelem_name, profile_id, pvid, profile_name |  |
| <a name="Create_Policy_Profile_with_COS_and_COS_Status_Enabled"></a>Create Policy Profile with COS and COS Status Enabled | netelem_name, profile_id, cos_value |  |
| <a name="Create_Policy_Profile_with_COS,_COS_Status,_and_TCI_Overwrite_Enabled"></a>Create Policy Profile with COS, COS Status, and TCI Overwrite Enabled | netelem_name, profile_id, cos_value |  |
| <a name="Create_Policy_Profile_with_Name_and_Verify_it_Exists"></a>Create Policy Profile with Name and Verify it Exists | netelem_name, profile_id, name |  |
| <a name="Create_Policy_Profile_With_PVID_and_PVID_Status_Enabled"></a>Create Policy Profile With PVID and PVID Status Enabled | netelem_name, profile_id, pvid |  |
| <a name="Create_Policy_Profile_with_PVID_and_PVID_Status_Enabled_and_TCI-Overwrite_Disabled"></a>Create Policy Profile with PVID and PVID Status Enabled and TCI-Overwrite Disabled | netelem_name, profile_id, pvid |  |
| <a name="Create_Policy_Profile_with_PVID_and_PVID_Status_Enabled_and_TCI-Overwrite_Enabled"></a>Create Policy Profile with PVID and PVID Status Enabled and TCI-Overwrite Enabled | netelem_name, profile_id, pvid |  |
| <a name="Create_Policy_Profile_with_PVID,_PVID_Status,_COS,_and_COS_Status_Enabled"></a>Create Policy Profile with PVID, PVID Status, COS, and COS Status Enabled | netelem_name, profile_id, pvid, cos_value |  |
| <a name="Create_Policy_Profile_with_PVID,_PVID_Status,_COS,_COS_Status,_and_TCI_Overwrite_Enabled"></a>Create Policy Profile with PVID, PVID Status, COS, COS Status, and TCI Overwrite Enabled | netelem_name, profile_id, pvid, cos_value |  |
| <a name="Create_Port_Admin_Profile_and_Verify_it_Exists"></a>Create Port Admin Profile and Verify it Exists | netelem_name, port, profile_id |  |
| <a name="Disable_Policy_and_Verify_it_is_Disabled"></a>Disable Policy and Verify it is Disabled | netelem_name |  |
| <a name="Enable_Policy_and_Verify_it_is_Enabled"></a>Enable Policy and Verify it is Enabled | netelem_name |  |
| <a name="Remove_Mac_Source_Admin_Profile_and_Verify_it_was_Removed"></a>Remove Mac Source Admin Profile and Verify it was Removed | netelem_name, mac_source, port, profile_id |  |
| <a name="Remove_Policy_Profile_and_Verify_it_was_Removed"></a>Remove Policy Profile and Verify it was Removed | netelem_name, profile_id |  |
| <a name="Remove_Port_Admin_Profile_and_Verify_it_was_Removed"></a>Remove Port Admin Profile and Verify it was Removed | netelem_name, port, profile_id |  |
| <a name="Set_Policy_Access_Control_and_Verify"></a>Set Policy Access Control and Verify | netelem_name, name, policy_action |  |
| <a name="Set_Policy_Invalid_Action_and_Verify"></a>Set Policy Invalid Action and Verify | netelem_name, policy_action |  |
| <a name="Set_Policy_Maptable_Response_and_Verify"></a>Set Policy Maptable Response and Verify | netelem_name, policy_maptable_response |  |
