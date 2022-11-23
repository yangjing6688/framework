# TrafficPortKeywords
Library Scope: test suite<br>
Named Arguments: Supported

## Introduction
Documentation for test library TrafficPortKeywords.

## Shortcuts
[Reset Port To Factory Defaults](#Reset_Port_To_Factory_Defaults) | [Set Port To Normal Mode](#Set_Port_To_Normal_Mode) | [Set Port To Qos Mode](#Set_Port_To_Qos_Mode) | [Take Port Ownership](#Take_Port_Ownership)
***

## Keywords
| Keyword | Arguments | Documentation |
|---------|-----------|---------------|
| <a name="Reset_Port_To_Factory_Defaults"></a>Reset Port To Factory Defaults | ports, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br><br>Resets the given traffic device's port to factory defaults. |
| <a name="Set_Port_To_Normal_Mode"></a>Set Port To Normal Mode | ports, **kwargs | [ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br><br>Sets a given ports statistic mode to QOS. |
| <a name="Set_Port_To_Qos_Mode"></a>Set Port To Qos Mode | ports, mode=vlan, qos_byte_offset=None, pattern_match_offset=None, pattern_match=None, pattern_match_mask=None, **kwargs | [ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[mode] - The QOS mode that should be used. Valid options are "vlan", "iptos", "snaptos", and "custom".<br>         Default and invalid options will be set to "vlan".<br>[qos_byte_offset] - Byte offset where QOS information is located.<br>[pattern_match_offset] - Byte offset of the pattern to match before checking for QOS info.<br>[pattern_match] - The pattern that must be matched before checking for QOS info.<br>[pattern_match_mask] - The mask that is applied to the pattern match.<br><br>Sets a given ports statistic mode to QOS. |
| <a name="Take_Port_Ownership"></a>Take Port Ownership | ports, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br><br>Takes ownership of the given traffic generator port(s). |
