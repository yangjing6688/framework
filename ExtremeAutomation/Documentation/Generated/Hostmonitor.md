# Keyword Library Documentation for Hostmonitor
This feature is located in this file: `hostmonitor.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: hostmonitor_verify_cpu_monitor_interval
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_cpu_monitor_interval(device_names, interval)

	Robot API Call: 

		hostmonitor_verify_cpu_monitor_interval  device_names  interval

# API Function: hostmonitor_verify_cpu_total_utilization
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_cpu_total_utilization(device_names, percent, operator)

	Robot API Call: 

		hostmonitor_verify_cpu_total_utilization  device_names  percent  operator

# API Function: hostmonitor_verify_cpu_threshold
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_cpu_threshold(device_names, threshold)

	Robot API Call: 

		hostmonitor_verify_cpu_threshold  device_names  threshold

# API Function: hostmonitor_verify_cpu_5_minute_system_utilization
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_cpu_5_minute_system_utilization(device_name, slot, percentage, operator)

	Robot API Call: 

		hostmonitor_verify_cpu_5_minute_system_utilization  device_name  slot  percentage  operator

# API Function: hostmonitor_verify_cpu_max_system_utilization
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_cpu_max_system_utilization(device_name, slot, percentage, operator)

	Robot API Call: 

		hostmonitor_verify_cpu_max_system_utilization  device_name  slot  percentage  operator

# API Function: hostmonitor_verify_free_system_memory
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_free_system_memory(device_name, slot, k_bytes, operator)

	Robot API Call: 

		hostmonitor_verify_free_system_memory  device_name  slot  k_bytes  operator

# API Function: hostmonitor_verify_used_system_service_memory
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_used_system_service_memory(device_name, slot, k_bytes, operator)

	Robot API Call: 

		hostmonitor_verify_used_system_service_memory  device_name  slot  k_bytes  operator

# API Function: hostmonitor_verify_used_application_memory
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_used_application_memory(device_name, slot, k_bytes, operator)

	Robot API Call: 

		hostmonitor_verify_used_application_memory  device_name  slot  k_bytes  operator

# API Function: hostmonitor_verify_cpu_current_total_utilization
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_cpu_current_total_utilization(device_name, slot, percentage, operator)

	Robot API Call: 

		hostmonitor_verify_cpu_current_total_utilization  device_name  slot  percentage  operator

# API Function: hostmonitor_verify_cpu_5_minute_total_utilization
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_cpu_5_minute_total_utilization(device_name, slot, percentage, operator)

	Robot API Call: 

		hostmonitor_verify_cpu_5_minute_total_utilization  device_name  slot  percentage  operator

# API Function: hostmonitor_verify_cpu_5_minute_highest_total_utilization
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_cpu_5_minute_highest_total_utilization(device_name, slot, percentage, operator)

	Robot API Call: 

		hostmonitor_verify_cpu_5_minute_highest_total_utilization  device_name  slot  percentage  operator

# API Function: hostmonitor_verify_free_total_memory
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_free_total_memory(device_name, slot, k_bytes, operator)

	Robot API Call: 

		hostmonitor_verify_free_total_memory  device_name  slot  k_bytes  operator

# API Function: hostmonitor_verify_used_total_memory
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_used_total_memory(device_name, slot, k_bytes, operator)

	Robot API Call: 

		hostmonitor_verify_used_total_memory  device_name  slot  k_bytes  operator

# API Function: hostmonitor_verify_memory_current_total_utilization
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_memory_current_total_utilization(device_name, slot, percentage, operator)

	Robot API Call: 

		hostmonitor_verify_memory_current_total_utilization  device_name  slot  percentage  operator

# API Function: hostmonitor_verify_memory_5_minute_total_utilization
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_memory_5_minute_total_utilization(device_name, slot, percentage, operator)

	Robot API Call: 

		hostmonitor_verify_memory_5_minute_total_utilization  device_name  slot  percentage  operator

# API Function: hostmonitor_verify_memory_5_minute_highest_total_utilization
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_memory_5_minute_highest_total_utilization(device_name, slot, percentage, operator)

	Robot API Call: 

		hostmonitor_verify_memory_5_minute_highest_total_utilization  device_name  slot  percentage  operator

# API Function: hostmonitor_verify_used_fbuffs
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_used_fbuffs(device_name, slot, value, operator)

	Robot API Call: 

		hostmonitor_verify_used_fbuffs  device_name  slot  value  operator

# API Function: hostmonitor_verify_free_fbuffs
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_free_fbuffs(device_name, slot, value, operator)

	Robot API Call: 

		hostmonitor_verify_free_fbuffs  device_name  slot  value  operator

# API Function: hostmonitor_verify_exhausted_fbuffs
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_exhausted_fbuffs(device_name, slot, value, operator)

	Robot API Call: 

		hostmonitor_verify_exhausted_fbuffs  device_name  slot  value  operator

# API Function: hostmonitor_verify_network_stack_system_free_mbuffs
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_network_stack_system_free_mbuffs(device_name, slot, value, operator)

	Robot API Call: 

		hostmonitor_verify_network_stack_system_free_mbuffs  device_name  slot  value  operator

# API Function: hostmonitor_verify_network_stack_system_used_mbuffs
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_network_stack_system_used_mbuffs(device_name, slot, value, operator)

	Robot API Call: 

		hostmonitor_verify_network_stack_system_used_mbuffs  device_name  slot  value  operator

# API Function: hostmonitor_verify_network_stack_data_free_mbuffs
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_network_stack_data_free_mbuffs(device_name, slot, value, operator)

	Robot API Call: 

		hostmonitor_verify_network_stack_data_free_mbuffs  device_name  slot  value  operator

# API Function: hostmonitor_verify_network_stack_data_used_mbuffs
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_network_stack_data_used_mbuffs(device_name, slot, value, operator)

	Robot API Call: 

		hostmonitor_verify_network_stack_data_used_mbuffs  device_name  slot  value  operator

# API Function: hostmonitor_verify_network_stack_system_socket_mbuffs
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_network_stack_system_socket_mbuffs(device_name, slot, value, operator)

	Robot API Call: 

		hostmonitor_verify_network_stack_system_socket_mbuffs  device_name  slot  value  operator

# API Function: hostmonitor_verify_highest_queue_entries_consumed
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_highest_queue_entries_consumed(device_name, slot, value, operator)

	Robot API Call: 

		hostmonitor_verify_highest_queue_entries_consumed  device_name  slot  value  operator

# API Function: hostmonitor_verify_current_queue_entries_consumed
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_current_queue_entries_consumed(device_name, slot, value, operator)

	Robot API Call: 

		hostmonitor_verify_current_queue_entries_consumed  device_name  slot  value  operator

# API Function: hostmonitor_verify_free_queue_entries
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_free_queue_entries(device_name, slot, value, operator)

	Robot API Call: 

		hostmonitor_verify_free_queue_entries  device_name  slot  value  operator

# API Function: hostmonitor_verify_used_process_memory
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_used_process_memory(device_name, slot, process_name, k_bytes, operator)

	Robot API Call: 

		hostmonitor_verify_used_process_memory  device_name  slot  process_name  k_bytes  operator

# API Function: hostmonitor_verify_cpu_process_state
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_cpu_process_state(device_name, slot, process_name, state)

	Robot API Call: 

		hostmonitor_verify_cpu_process_state  device_name  slot  process_name  state

# API Function: hostmonitor_verify_cpu_5_minute_process_utilization
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_cpu_5_minute_process_utilization(device_name, slot, process_name, percentage, operator)

	Robot API Call: 

		hostmonitor_verify_cpu_5_minute_process_utilization  device_name  slot  process_name  percentage  operator

# API Function: hostmonitor_verify_slot_operational
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.hostmonitor.hostmonitor_verify_slot_operational(device_names, slot)

	Robot API Call: 

		hostmonitor_verify_slot_operational  device_names  slot

