# RadiusUdks
Library Scope: N/A<br>
Named Arguments: Supported

## Introduction
Documentation for resource file RadiusUdks.

## Shortcuts
[Add a Radius Accounting Server and Globally Enable Accounting](#Add_a_Radius_Accounting_Server_and_Globally_Enable_Accounting) | [Add a Radius Accounting Server and Verify it was Added](#Add_a_Radius_Accounting_Server_and_Verify_it_was_Added) | [Add a Radius Server and Globally Enable Radius](#Add_a_Radius_Server_and_Globally_Enable_Radius) | [Add a Radius Server and Verify it was Added](#Add_a_Radius_Server_and_Verify_it_was_Added) | [Add a Radius Server and Verify Status is Active](#Add_a_Radius_Server_and_Verify_Status_is_Active) | [Cleanup Radius Accounting Server Configuration](#Cleanup_Radius_Accounting_Server_Configuration) | [Cleanup Radius Server Configuration](#Cleanup_Radius_Server_Configuration) | [Disable Radius for Management Users and Verify](#Disable_Radius_for_Management_Users_and_Verify) | [Enable Radius for Netlogin Users and Verify](#Enable_Radius_for_Netlogin_Users_and_Verify) | [Globally Disable Radius Accounting and Verify it is Disabled](#Globally_Disable_Radius_Accounting_and_Verify_it_is_Disabled) | [Globally Disable Radius and Verify it is Disabled](#Globally_Disable_Radius_and_Verify_it_is_Disabled) | [Globally Enable Radius Accounting and Verify it is Enabled](#Globally_Enable_Radius_Accounting_and_Verify_it_is_Enabled) | [Globally Enable Radius and Verify it is Enabled](#Globally_Enable_Radius_and_Verify_it_is_Enabled) | [Remove Radius Accounting Server and Verify it is Removed](#Remove_Radius_Accounting_Server_and_Verify_it_is_Removed) | [Remove Radius Server and Verify it is Removed](#Remove_Radius_Server_and_Verify_it_is_Removed) | [Restore Radius Algorithm to Default Setting and Verify](#Restore_Radius_Algorithm_to_Default_Setting_and_Verify) | [Restore Radius Retries to Default Setting and Verify](#Restore_Radius_Retries_to_Default_Setting_and_Verify) | [Restore Radius Timeout to Default Setting and Verify](#Restore_Radius_Timeout_to_Default_Setting_and_Verify) | [Set Radius Algorithm Type Round Robin and Verify Setting](#Set_Radius_Algorithm_Type_Round_Robin_and_Verify_Setting) | [Set Radius Algorithm Type Standard and Verify Setting](#Set_Radius_Algorithm_Type_Standard_and_Verify_Setting) | [Set Radius Algorithm Type Sticky Round Robin and Verify Setting](#Set_Radius_Algorithm_Type_Sticky_Round_Robin_and_Verify_Setting) | [Set Radius Retries and Verify Value](#Set_Radius_Retries_and_Verify_Value) | [Set Radius Timeout and Verify Value](#Set_Radius_Timeout_and_Verify_Value)
***

## Keywords
| Keyword | Arguments | Documentation |
|---------|-----------|---------------|
| <a name="Add_a_Radius_Accounting_Server_and_Globally_Enable_Accounting"></a>Add a Radius Accounting Server and Globally Enable Accounting | device_name, index, addr, port, secret, client_ip, vr |  |
| <a name="Add_a_Radius_Accounting_Server_and_Verify_it_was_Added"></a>Add a Radius Accounting Server and Verify it was Added | device_name, index, addr, port, secret, client_ip, vr | Note that proprietary arguments of client_ip and vr are passed in on lower level keywords. |
| <a name="Add_a_Radius_Server_and_Globally_Enable_Radius"></a>Add a Radius Server and Globally Enable Radius | device_name, index, addr, port, secret, client_ip, vr |  |
| <a name="Add_a_Radius_Server_and_Verify_it_was_Added"></a>Add a Radius Server and Verify it was Added | device_name, index, addr, port, secret, client_ip, vr | Adds a RADIUS server and verifies it was added. |
| <a name="Add_a_Radius_Server_and_Verify_Status_is_Active"></a>Add a Radius Server and Verify Status is Active | device_name, index, addr, port, secret, client_ip, vr | Adds a Radius Server and Verifies the Status is set to Active |
| <a name="Cleanup_Radius_Accounting_Server_Configuration"></a>Cleanup Radius Accounting Server Configuration | device_name, index, addr |  |
| <a name="Cleanup_Radius_Server_Configuration"></a>Cleanup Radius Server Configuration | device_name, index, addr |  |
| <a name="Disable_Radius_for_Management_Users_and_Verify"></a>Disable Radius for Management Users and Verify | device_name |  |
| <a name="Enable_Radius_for_Netlogin_Users_and_Verify"></a>Enable Radius for Netlogin Users and Verify | device_name |  |
| <a name="Globally_Disable_Radius_Accounting_and_Verify_it_is_Disabled"></a>Globally Disable Radius Accounting and Verify it is Disabled | device_name | Disable RADIUS Accounting and Verifies. |
| <a name="Globally_Disable_Radius_and_Verify_it_is_Disabled"></a>Globally Disable Radius and Verify it is Disabled | device_name | Globally Disables RADIUS and Verifies it is Disabled |
| <a name="Globally_Enable_Radius_Accounting_and_Verify_it_is_Enabled"></a>Globally Enable Radius Accounting and Verify it is Enabled | device_name | This testcase Globally Enables RADIUS on the Network Element and verifies it is Enabled. |
| <a name="Globally_Enable_Radius_and_Verify_it_is_Enabled"></a>Globally Enable Radius and Verify it is Enabled | device_name | Globally Enables RADIUS and Verifies it is Enabled |
| <a name="Remove_Radius_Accounting_Server_and_Verify_it_is_Removed"></a>Remove Radius Accounting Server and Verify it is Removed | device_name, index, addr |  |
| <a name="Remove_Radius_Server_and_Verify_it_is_Removed"></a>Remove Radius Server and Verify it is Removed | device_name, index, addr |  |
| <a name="Restore_Radius_Algorithm_to_Default_Setting_and_Verify"></a>Restore Radius Algorithm to Default Setting and Verify | device_name |  |
| <a name="Restore_Radius_Retries_to_Default_Setting_and_Verify"></a>Restore Radius Retries to Default Setting and Verify | device_name |  |
| <a name="Restore_Radius_Timeout_to_Default_Setting_and_Verify"></a>Restore Radius Timeout to Default Setting and Verify | device_name |  |
| <a name="Set_Radius_Algorithm_Type_Round_Robin_and_Verify_Setting"></a>Set Radius Algorithm Type Round Robin and Verify Setting | device_name | Sets the RADIUS Algorithm type to Round-Robin |
| <a name="Set_Radius_Algorithm_Type_Standard_and_Verify_Setting"></a>Set Radius Algorithm Type Standard and Verify Setting | device_name | Sets the RADIUS Algorithm type to Standard |
| <a name="Set_Radius_Algorithm_Type_Sticky_Round_Robin_and_Verify_Setting"></a>Set Radius Algorithm Type Sticky Round Robin and Verify Setting | device_name | Sets the RADIUS Algorithm type to Sticky-Round-Robin |
| <a name="Set_Radius_Retries_and_Verify_Value"></a>Set Radius Retries and Verify Value | device_name, num | Sets the RADIUS Server retries value and verifies setting |
| <a name="Set_Radius_Timeout_and_Verify_Value"></a>Set Radius Timeout and Verify Value | device_name, sec | Sets the RADIUS Server timeout and verifies the value |
