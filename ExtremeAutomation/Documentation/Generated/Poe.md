# Command Keyword Library Documentation for Poe
This feature is located in this file: `poe.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` * Note if you are looking for a verify (show + parsing command) keyword please refer to the verification documentaion.

# API Function: enable_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_enable_port(device_name )

	Robot API Call: 

		poe_enable_port  device_name  

UUID: d85ded5e-243f-4062-bd8d-ac66eb95dda9
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no poe-shutdown

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable inline-power ports {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.105.1.1.1.3.{port}

----------------------------------------------


# API Function: disable_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_disable_port(device_name )

	Robot API Call: 

		poe_disable_port  device_name  

UUID: 5147e9d2-fd97-4272-b558-aa5299f90122
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		poe poe-shutdown

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable inline-power ports {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.105.1.1.1.3.{port}

----------------------------------------------


# API Function: set_power_usage_threshold
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_set_power_usage_threshold(device_name, threshold, slot)

	Robot API Call: 

		poe_set_power_usage_threshold  device_name  threshold  slot

UUID: 142af738-8794-4d20-ab2d-9786dbeeda98
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		poe poe-power-usage-threshold {threshold}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure inline-power usage-threshold {threshold}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.105.1.3.1.1.5.{slot}

----------------------------------------------


# API Function: set_port_power_limit
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_set_port_power_limit(device_name, port, power_limit)

	Robot API Call: 

		poe_set_port_power_limit  device_name  port  power_limit

UUID: d7b94cad-7944-4f3e-8d18-13f8fb4588f1
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		poe poe-limit {power_limit}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure inline-power operator-limit {power_limit} port {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.5.8.1.1.1.3.{port}

----------------------------------------------


# API Function: set_port_power_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_set_port_power_priority(device_name, port, power_priority)

	Robot API Call: 

		poe_set_port_power_priority  device_name  port  power_priority

UUID: c1d24df9-00f0-496a-b3f8-29e7b1e5ff8f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		poe poe-priority {power_priority}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure inline-power priority {power_priority} ports {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.2.1.105.1.1.1.7.{port}

----------------------------------------------


# API Function: set_port_detect_type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_set_port_detect_type(device_name, port, detect_type)

	Robot API Call: 

		poe_set_port_detect_type  device_name  port  detect_type

UUID: a1bb7007-736f-4b7f-ae63-16df0afdc9a2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure inline-power detection {detect_type} port {port}

----------------------------------------------


## REST
## SNMP
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: SNMP

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action`: set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OID`: 1.3.6.1.4.1.45.1.6.15.1.1.1.6.{port}

----------------------------------------------


# API Function: enable_inline_power
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_enable_inline_power(device_name )

	Robot API Call: 

		poe_enable_inline_power  device_name  

UUID: 8ec88be4-58f4-4d2f-9fd5-9094f40fd3bb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable inline-power

----------------------------------------------


## REST
## SNMP
# API Function: disable_inline_power
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_disable_inline_power(device_name )

	Robot API Call: 

		poe_disable_inline_power  device_name  

UUID: 9025539e-fe7f-4b90-b9bf-e4a958e6cf1b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable inline-power

----------------------------------------------


## REST
## SNMP
# API Function: enable_inline_power_legacy
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_enable_inline_power_legacy(device_name )

	Robot API Call: 

		poe_enable_inline_power_legacy  device_name  

UUID: 6da49954-b1d9-4dd8-b905-15fd0609d2b6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable inline-power legacy

----------------------------------------------


## REST
## SNMP
# API Function: disable_inline_power_legacy
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_disable_inline_power_legacy(device_name )

	Robot API Call: 

		poe_disable_inline_power_legacy  device_name  

UUID: 249d5f97-4872-4bad-b56c-2b60459937b0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable inline-power legacy

----------------------------------------------


## REST
## SNMP
# API Function: set_inline_power_disconnect_deny_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_set_inline_power_disconnect_deny_port(device_name )

	Robot API Call: 

		poe_set_inline_power_disconnect_deny_port  device_name  

UUID: fa8aaf1d-1d6d-4282-b05d-2c793c090fa7
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure inline-power disconnect deny-port

----------------------------------------------


## REST
## SNMP
# API Function: set_inline_power_disconnect_lowest_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_set_inline_power_disconnect_lowest_priority(device_name )

	Robot API Call: 

		poe_set_inline_power_disconnect_lowest_priority  device_name  

UUID: f9469e5c-858b-47d7-95a0-7e84b457c937
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure inline-power disconnect lowest-priority

----------------------------------------------


## REST
## SNMP
# API Function: clear_inline_power_disconnect
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_clear_inline_power_disconnect(device_name )

	Robot API Call: 

		poe_clear_inline_power_disconnect  device_name  

UUID: a88c6ba4-5483-4c51-ba5b-7e5ac5a4bdac
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		unconfigure inline-power disconnect

----------------------------------------------


## REST
## SNMP
# API Function: set_inline_power_label
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_set_inline_power_label(device_name, port, test_label)

	Robot API Call: 

		poe_set_inline_power_label  device_name  port  test_label

UUID: 83510d13-fdc3-4f04-8fb4-2cdaaa20beb5
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure inline-power label {test_label} port {port}

----------------------------------------------


## REST
## SNMP
# API Function: poe_verify_power_threshold
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_power_threshold(device_name, threshold, slot)

	Robot API Call: 

		poe_verify_power_threshold  device_name  threshold  slot

# API Function: poe_verify_power_invalid_threshold
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_power_invalid_threshold(device_name, threshold, slot)

	Robot API Call: 

		poe_verify_power_invalid_threshold  device_name  threshold  slot

# API Function: poe_verify_port_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_port_enabled(device_name, ports)

	Robot API Call: 

		poe_verify_port_enabled  device_name  ports

# API Function: poe_verify_port_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_port_disabled(device_name, ports)

	Robot API Call: 

		poe_verify_port_disabled  device_name  ports

# API Function: poe_verify_port_power_limit
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_port_power_limit(device_name, ports, power_limit)

	Robot API Call: 

		poe_verify_port_power_limit  device_name  ports  power_limit

# API Function: poe_verify_port_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_port_priority(device_name, ports, power_priority)

	Robot API Call: 

		poe_verify_port_priority  device_name  ports  power_priority

# API Function: poe_verify_port_detect_type
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_port_detect_type(device_name, ports, detect_type)

	Robot API Call: 

		poe_verify_port_detect_type  device_name  ports  detect_type

# API Function: poe_verify_port_measured_voltage
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_port_measured_voltage(device_name, ports, decivolts, value_operator)

	Robot API Call: 

		poe_verify_port_measured_voltage  device_name  ports  decivolts  value_operator

# API Function: poe_verify_port_measured_current
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_port_measured_current(device_name, ports, milliamps, value_operator)

	Robot API Call: 

		poe_verify_port_measured_current  device_name  ports  milliamps  value_operator

# API Function: poe_verify_port_measured_power
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_port_measured_power(device_name, ports, milliwatts, value_operator)

	Robot API Call: 

		poe_verify_port_measured_power  device_name  ports  milliwatts  value_operator

# API Function: poe_verify_port_detection_status
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_port_detection_status(device_name, ports, detect_status)

	Robot API Call: 

		poe_verify_port_detection_status  device_name  ports  detect_status

# API Function: poe_verify_port_power_classification
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_port_power_classification(device_name, ports, power_class)

	Robot API Call: 

		poe_verify_port_power_classification  device_name  ports  power_class

# API Function: poe_verify_port_power_pairs_on_signal
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_port_power_pairs_on_signal(device_name, ports)

	Robot API Call: 

		poe_verify_port_power_pairs_on_signal  device_name  ports

# API Function: poe_verify_port_power_pairs_on_spare
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_port_power_pairs_on_spare(device_name, ports)

	Robot API Call: 

		poe_verify_port_power_pairs_on_spare  device_name  ports

# API Function: poe_verify_main_available_power
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_main_available_power(device_name, power, slot)

	Robot API Call: 

		poe_verify_main_available_power  device_name  power  slot

# API Function: poe_verify_main_consumption_power
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_main_consumption_power(device_name, power, value_operator, slot)

	Robot API Call: 

		poe_verify_main_consumption_power  device_name  power  value_operator  slot

# API Function: poe_verify_inline_power_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_inline_power_disabled()

	Robot API Call: 

		poe_verify_inline_power_disabled  

# API Function: poe_verify_inline_power_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_inline_power_enabled()

	Robot API Call: 

		poe_verify_inline_power_enabled  

# API Function: poe_verify_inline_power_port_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_inline_power_port_disabled()

	Robot API Call: 

		poe_verify_inline_power_port_disabled  

# API Function: poe_verify_inline_power_port_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_inline_power_port_enabled()

	Robot API Call: 

		poe_verify_inline_power_port_enabled  

# API Function: poe_verify_inline_power_legacy_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_inline_power_legacy_enabled()

	Robot API Call: 

		poe_verify_inline_power_legacy_enabled  

# API Function: poe_verify_inline_power_legacy_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_inline_power_legacy_disabled()

	Robot API Call: 

		poe_verify_inline_power_legacy_disabled  

# API Function: poe_verify_inline_power_disconnect_deny_port
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_inline_power_disconnect_deny_port()

	Robot API Call: 

		poe_verify_inline_power_disconnect_deny_port  

# API Function: poe_verify_inline_power_disconnect_lowest_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_inline_power_disconnect_lowest_priority()

	Robot API Call: 

		poe_verify_inline_power_disconnect_lowest_priority  

# API Function: poe_verify_inline_power_unconfigure_disconnect
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_inline_power_unconfigure_disconnect()

	Robot API Call: 

		poe_verify_inline_power_unconfigure_disconnect  

# API Function: poe_verify_inline_power_label
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_inline_power_label()

	Robot API Call: 

		poe_verify_inline_power_label  

# API Function: poe_verify_inline_power_operator_limit
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.poe.poe_verify_inline_power_operator_limit()

	Robot API Call: 

		poe_verify_inline_power_operator_limit  

