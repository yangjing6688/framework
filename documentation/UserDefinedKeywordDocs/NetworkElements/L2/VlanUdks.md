# VlanUdks
Library Scope: N/A<br>
Named Arguments: Supported

## Introduction
Documentation for resource file VlanUdks.

## Shortcuts
[Add Port/s to Tagged Egress for VLAN and Verify it was Added](#Add_Port/s_to_Tagged_Egress_for_VLAN_and_Verify_it_was_Added) | [Add Port/s to Tagged Egress for VLAN and Verify it was Added to Static Egress](#Add_Port/s_to_Tagged_Egress_for_VLAN_and_Verify_it_was_Added_to_Static_Egress) | [Add Port/s to Untagged Egress for VLAN and Set PVID then Verify](#Add_Port/s_to_Untagged_Egress_for_VLAN_and_Set_PVID_then_Verify) | [Add Port/s to Untagged Egress for VLAN and set PVID then Verify Static Egress](#Add_Port/s_to_Untagged_Egress_for_VLAN_and_set_PVID_then_Verify_Static_Egress) | [Add Port/s to Untagged Egress for VLAN and Verify it was Added](#Add_Port/s_to_Untagged_Egress_for_VLAN_and_Verify_it_was_Added) | [Add Port/s to Untagged Egress for VLAN and Verify it was Added to Static Egress](#Add_Port/s_to_Untagged_Egress_for_VLAN_and_Verify_it_was_Added_to_Static_Egress) | [Clear PVID and Verify it was Cleared](#Clear_PVID_and_Verify_it_was_Cleared) | [Clear VLAN Description and Verify it was Removed](#Clear_VLAN_Description_and_Verify_it_was_Removed) | [Clear VLAN Name and Verify it was Removed](#Clear_VLAN_Name_and_Verify_it_was_Removed) | [Create VLAN and Add Port(s) Tagged then Verify](#Create_VLAN_and_Add_Port(s)_Tagged_then_Verify) | [Create VLAN and Add Port(s) Untagged then Verify](#Create_VLAN_and_Add_Port(s)_Untagged_then_Verify) | [Create VLAN and Expect Error](#Create_VLAN_and_Expect_Error) | [Create VLAN and Verify it Exists](#Create_VLAN_and_Verify_it_Exists) | [Create VLAN with Tag and Verify it Exists](#Create_VLAN_with_Tag_and_Verify_it_Exists) | [Create VMAN and Verify it Exists](#Create_VMAN_and_Verify_it_Exists) | [Disable VLAN and Validate it is Disabled](#Disable_VLAN_and_Validate_it_is_Disabled) | [Disable VLAN and Validate it is Still Enabled](#Disable_VLAN_and_Validate_it_is_Still_Enabled) | [Disable VLAN and Verify Error is Seen](#Disable_VLAN_and_Verify_Error_is_Seen) | [Enable VLAN and Validate it is Enabled](#Enable_VLAN_and_Validate_it_is_Enabled) | [Enable VLAN and Verify Error is Seen](#Enable_VLAN_and_Verify_Error_is_Seen) | [Remove Port/s from Tagged Egress for VLAN and Verify it was Removed](#Remove_Port/s_from_Tagged_Egress_for_VLAN_and_Verify_it_was_Removed) | [Remove Port/s from Untagged Egress for VLAN and Verify it was Removed](#Remove_Port/s_from_Untagged_Egress_for_VLAN_and_Verify_it_was_Removed) | [Remove VLAN and Expect Error](#Remove_VLAN_and_Expect_Error) | [Remove VLAN and Ignore CLI Feedback](#Remove_VLAN_and_Ignore_CLI_Feedback) | [Remove VLAN and Verify it was Removed](#Remove_VLAN_and_Verify_it_was_Removed) | [Remove VMAN and Verify it was Removed](#Remove_VMAN_and_Verify_it_was_Removed) | [Set PVID and Verify it was Set](#Set_PVID_and_Verify_it_was_Set) | [Set VLAN Description and Verify it was Set](#Set_VLAN_Description_and_Verify_it_was_Set) | [Set VLAN Name and Expect Error](#Set_VLAN_Name_and_Expect_Error) | [Set VLAN Name and Verify it was not Set](#Set_VLAN_Name_and_Verify_it_was_not_Set) | [Set VLAN Name and Verify it was Set](#Set_VLAN_Name_and_Verify_it_was_Set)
***

## Keywords
| Keyword | Arguments | Documentation |
|---------|-----------|---------------|
| <a name="Add_Port/s_to_Tagged_Egress_for_VLAN_and_Verify_it_was_Added"></a>Add Port/s to Tagged Egress for VLAN and Verify it was Added | netelem_name, vlan, port |  |
| <a name="Add_Port/s_to_Tagged_Egress_for_VLAN_and_Verify_it_was_Added_to_Static_Egress"></a>Add Port/s to Tagged Egress for VLAN and Verify it was Added to Static Egress | netelem_name, vlan, port |  |
| <a name="Add_Port/s_to_Untagged_Egress_for_VLAN_and_Set_PVID_then_Verify"></a>Add Port/s to Untagged Egress for VLAN and Set PVID then Verify | netelem_name, vlan, port |  |
| <a name="Add_Port/s_to_Untagged_Egress_for_VLAN_and_set_PVID_then_Verify_Static_Egress"></a>Add Port/s to Untagged Egress for VLAN and set PVID then Verify Static Egress | netelem_name, vlan, port |  |
| <a name="Add_Port/s_to_Untagged_Egress_for_VLAN_and_Verify_it_was_Added"></a>Add Port/s to Untagged Egress for VLAN and Verify it was Added | netelem_name, vlan, port |  |
| <a name="Add_Port/s_to_Untagged_Egress_for_VLAN_and_Verify_it_was_Added_to_Static_Egress"></a>Add Port/s to Untagged Egress for VLAN and Verify it was Added to Static Egress | netelem_name, vlan, port |  |
| <a name="Clear_PVID_and_Verify_it_was_Cleared"></a>Clear PVID and Verify it was Cleared | netelem_name, port, vlan |  |
| <a name="Clear_VLAN_Description_and_Verify_it_was_Removed"></a>Clear VLAN Description and Verify it was Removed | dut_name, vlan, vlan_name |  |
| <a name="Clear_VLAN_Name_and_Verify_it_was_Removed"></a>Clear VLAN Name and Verify it was Removed | dut_name, vlan, vlan_name |  |
| <a name="Create_VLAN_and_Add_Port(s)_Tagged_then_Verify"></a>Create VLAN and Add Port(s) Tagged then Verify | device_name, vlan_id, ports |  |
| <a name="Create_VLAN_and_Add_Port(s)_Untagged_then_Verify"></a>Create VLAN and Add Port(s) Untagged then Verify | device_name, vlan_id, ports |  |
| <a name="Create_VLAN_and_Expect_Error"></a>Create VLAN and Expect Error | netelem_name, vlan | creates vlan(s) and expect error |
| <a name="Create_VLAN_and_Verify_it_Exists"></a>Create VLAN and Verify it Exists | netelem_name, vlan | creates vlan(s) and verifies it exists |
| <a name="Create_VLAN_with_Tag_and_Verify_it_Exists"></a>Create VLAN with Tag and Verify it Exists | netelem_name, vlan, tag | creates vlan(s) and verifies it exists |
| <a name="Create_VMAN_and_Verify_it_Exists"></a>Create VMAN and Verify it Exists | netelem_name, vman | creates vman(s) and verifies it exists |
| <a name="Disable_VLAN_and_Validate_it_is_Disabled"></a>Disable VLAN and Validate it is Disabled | netelem_name, vlan |  |
| <a name="Disable_VLAN_and_Validate_it_is_Still_Enabled"></a>Disable VLAN and Validate it is Still Enabled | netelem_name, vlan |  |
| <a name="Disable_VLAN_and_Verify_Error_is_Seen"></a>Disable VLAN and Verify Error is Seen | netelem_name, vlan |  |
| <a name="Enable_VLAN_and_Validate_it_is_Enabled"></a>Enable VLAN and Validate it is Enabled | netelem_name, vlan |  |
| <a name="Enable_VLAN_and_Verify_Error_is_Seen"></a>Enable VLAN and Verify Error is Seen | netelem_name, vlan |  |
| <a name="Remove_Port/s_from_Tagged_Egress_for_VLAN_and_Verify_it_was_Removed"></a>Remove Port/s from Tagged Egress for VLAN and Verify it was Removed | netelem_name, vlan, port |  |
| <a name="Remove_Port/s_from_Untagged_Egress_for_VLAN_and_Verify_it_was_Removed"></a>Remove Port/s from Untagged Egress for VLAN and Verify it was Removed | netelem_name, vlan, port |  |
| <a name="Remove_VLAN_and_Expect_Error"></a>Remove VLAN and Expect Error | netelem_name, vlan | removes vlan(s) and expects error(s) |
| <a name="Remove_VLAN_and_Ignore_CLI_Feedback"></a>Remove VLAN and Ignore CLI Feedback | netelem_name, vlan | removes vlan(s) and expects error(s) |
| <a name="Remove_VLAN_and_Verify_it_was_Removed"></a>Remove VLAN and Verify it was Removed | netelem_name, vlan | removes vlan(s) and verifies it does not exist |
| <a name="Remove_VMAN_and_Verify_it_was_Removed"></a>Remove VMAN and Verify it was Removed | netelem_name, vman | removes vman(s) and verifies it does not exist |
| <a name="Set_PVID_and_Verify_it_was_Set"></a>Set PVID and Verify it was Set | netelem_name, port, pvid |  |
| <a name="Set_VLAN_Description_and_Verify_it_was_Set"></a>Set VLAN Description and Verify it was Set | dut_name, vlan, vlan_name |  |
| <a name="Set_VLAN_Name_and_Expect_Error"></a>Set VLAN Name and Expect Error | dut_name, vlan, vlan_name |  |
| <a name="Set_VLAN_Name_and_Verify_it_was_not_Set"></a>Set VLAN Name and Verify it was not Set | dut_name, vlan, vlan_name |  |
| <a name="Set_VLAN_Name_and_Verify_it_was_Set"></a>Set VLAN Name and Verify it was Set | dut_name, vlan, vlan_name |  |
