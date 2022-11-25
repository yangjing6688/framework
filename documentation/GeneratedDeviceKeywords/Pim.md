# Keyword Library Documentation for Pim
This feature is located in this file: `pim.yaml` (in this directory: extreme_automation_framework/ExtremeAutomation/Apis/NetworkElement/ApiDefinition). If any low level keywords are missing they can be added to this file and the APIs can be generated with the following python script located here: /extreme_automation_framework/ExtremeAutomation/Apis/GenerateApisFromDefinitionFiles.py. To execute the script. CD to the repository directory (/extreme_automation_framework/ExtremeAutomation/Apis/) and type: `python GenerateApisFromDefinitionFiles.py` 

# API Function: enable
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_enable(device_name )

	Robot API Call: 

		pim_enable  device_name  

UUID: 2ea0a641-0c71-44f1-b414-f118bda2b214
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		enable pim

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip pim enable

----------------------------------------------


## REST
## SNMP
# API Function: disable
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_disable(device_name )

	Robot API Call: 

		pim_disable  device_name  

UUID: 1d82492c-8d8b-42bc-abe6-7e5a4577c68c
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		disable pim

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip pim enable

----------------------------------------------


## REST
## SNMP
# API Function: enable_sparse
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_enable_sparse(device_name )

	Robot API Call: 

		pim_enable_sparse  device_name  

UUID: 9aa86d46-68cf-4c13-a466-a93068dbbeb6
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure pim add {vlan} {exos_mode}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip pim mode sparse

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		{ip_ver} pim {mode}

----------------------------------------------


## REST
## SNMP
# API Function: disable_sparse
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_disable_sparse(device_name )

	Robot API Call: 

		pim_disable_sparse  device_name  

UUID: 0df06e63-809b-41ee-a689-9c4a00ae4998
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure pim delete {vlan}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no {ip_ver} pim {mode}

----------------------------------------------


## REST
## SNMP
# API Function: set_rp
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_set_rp(device_name, mcast_group_address, mask, ip, interface, acl)

	Robot API Call: 

		pim_set_rp  device_name  mcast_group_address  mask  ip  interface  acl

UUID: dde6ad18-c92d-4adf-ae33-bcc41017c9c2
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure pim crp {interface} {acl}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip pim rp-candidate group {mcast_group_address} {mask} rp {ip}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip pim rp-candidate {ip} group-list {acl}

----------------------------------------------


## REST
## SNMP
# API Function: set_bsr_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_set_bsr_priority(device_name, priority, interface, ip)

	Robot API Call: 

		pim_set_bsr_priority  device_name  priority  interface  ip

UUID: 1f90fadf-b3df-4e1e-930e-4fb774b9a74e
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		configure pim cbsr {interface} {priority}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {interface}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip pim bsr-candidate preference {priority}

----------------------------------------------


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip pim bsr-candidate {ip} priority {priority}

----------------------------------------------


## REST
## SNMP
# API Function: enable_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_enable_interface(device_name )

	Robot API Call: 

		pim_enable_interface  device_name  

UUID: 2f125372-eb07-4026-ac07-d8496c900dcb
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip pim enable

----------------------------------------------


## REST
## SNMP
# API Function: enable_interface_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_enable_interface_vlan(device_name )

	Robot API Call: 

		pim_enable_interface_vlan  device_name  

UUID: a29ab14c-4118-4b89-8db4-050389320a90
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {vlan}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip pim enable

----------------------------------------------


## REST
## SNMP
# API Function: enable_ssm
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_enable_ssm(device_name )

	Robot API Call: 

		pim_enable_ssm  device_name  

UUID: dbd29b01-730a-4f46-a94d-be979c9bd715
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip pim mode ssm||yes

----------------------------------------------


## REST
## SNMP
# API Function: disable_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_disable_interface(device_name )

	Robot API Call: 

		pim_disable_interface  device_name  

UUID: e0c7f6f0-1156-4df5-99a3-b6485fe02ac3
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip pim enable

----------------------------------------------


## REST
## SNMP
# API Function: disable_interface_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_disable_interface_vlan(device_name )

	Robot API Call: 

		pim_disable_interface_vlan  device_name  

UUID: f732d752-dd26-4ff5-8b4e-0572215066a0
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {vlan}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip pim enable

----------------------------------------------


## REST
## SNMP
# API Function: set_bsr_priority_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_set_bsr_priority_vlan(device_name, vlan, priority)

	Robot API Call: 

		pim_set_bsr_priority_vlan  device_name  vlan  priority

UUID: 49b462e7-2600-49af-b40a-4ea6e2553b01
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {vlan}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip pim bsr-candidate preference {priority}

----------------------------------------------


## REST
## SNMP
# API Function: set_rp_static
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_set_rp_static(device_name )

	Robot API Call: 

		pim_set_rp_static  device_name  

UUID: a079226c-fb18-47e9-bead-fb4118ddcdf8
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip pim static-rp

----------------------------------------------


## REST
## SNMP
# API Function: set_interface_active
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_set_interface_active(device_name )

	Robot API Call: 

		pim_set_interface_active  device_name  

UUID: 522a379f-6419-453e-b276-7b22065b4040
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip pim active

----------------------------------------------


## REST
## SNMP
# API Function: set_interface_passive
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_set_interface_passive(device_name )

	Robot API Call: 

		pim_set_interface_passive  device_name  

UUID: d45d3028-1eda-492e-ada7-07139874005b
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: GigabitEthernet {port}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip pim passive

----------------------------------------------


## REST
## SNMP
# API Function: set_vlan_active
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_set_vlan_active(device_name )

	Robot API Call: 

		pim_set_vlan_active  device_name  

UUID: cb7046f0-a67b-4bd5-97a9-081a45a6c458
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {vlan}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip pim active

----------------------------------------------


## REST
## SNMP
# API Function: set_vlan_passive
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_set_vlan_passive(device_name )

	Robot API Call: 

		pim_set_vlan_passive  device_name  

UUID: b2f50332-3266-4d74-b2dd-bbe57560c93a
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: intfPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: vlan {vlan}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		ip pim passive

----------------------------------------------


## REST
## SNMP
# API Function: clear_rp
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_clear_rp(device_name )

	Robot API Call: 

		pim_clear_rp  device_name  

UUID: f70f48d0-844b-4692-b68a-1e334d3b369f
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: VOSS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: routerConfigPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		no ip pim rp-candidate group {ip} {mask}

----------------------------------------------


## REST
## SNMP
# API Function: clear_cache
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_clear_cache(device_name )

	Robot API Call: 

		pim_clear_cache  device_name  

UUID: bda40a90-b5f8-4229-a94d-bfef85b44422
## CLI
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OS`: EXOS

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`agent`: CLI

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt`: userPrompt

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Prompt Arguments`: None

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Command`:

		clear pim cache {mcast_group_address}

----------------------------------------------


## REST
## SNMP
# API Function: pim_verify_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_enabled(device_names)

	Robot API Call: 

		pim_verify_enabled  device_names

# API Function: pim_verify_disabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_disabled(device_names)

	Robot API Call: 

		pim_verify_disabled  device_names

# API Function: pim_verify_enabled_on_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_enabled_on_interface(device_names, interface, ip_version, port_type, port_num)

	Robot API Call: 

		pim_verify_enabled_on_interface  device_names  interface  ip_version  port_type  port_num

# API Function: pim_verify_disabled_on_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_disabled_on_interface(device_names, interface, ip_version, port_type, port_num, "6", "ipv6", "v6")

	Robot API Call: 

		pim_verify_disabled_on_interface  device_names  interface  ip_version  port_type  port_num  "6", "ipv6", "v6"

# API Function: pim_verify_enabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_enabled_on_vlan(device_names, vlan)

	Robot API Call: 

		pim_verify_enabled_on_vlan  device_names  vlan

# API Function: pim_verify_disabled_on_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_disabled_on_vlan(device_names, vlan)

	Robot API Call: 

		pim_verify_disabled_on_vlan  device_names  vlan

# API Function: pim_verify_sparse_mode_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_sparse_mode_enabled(device_names)

	Robot API Call: 

		pim_verify_sparse_mode_enabled  device_names

# API Function: pim_verify_ssm_enabled
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_ssm_enabled(device_names)

	Robot API Call: 

		pim_verify_ssm_enabled  device_names

# API Function: pim_verify_expected_bsr_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_expected_bsr_ip(device_names, expected_bsr_ip)

	Robot API Call: 

		pim_verify_expected_bsr_ip  device_names  expected_bsr_ip

# API Function: pim_verify_expected_bsr_ip_is_not_present
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_expected_bsr_ip_is_not_present(device_names, expected_bsr_ip)

	Robot API Call: 

		pim_verify_expected_bsr_ip_is_not_present  device_names  expected_bsr_ip

# API Function: pim_verify_candidate_bsr_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_candidate_bsr_ip(device_names, interface, ip_address)

	Robot API Call: 

		pim_verify_candidate_bsr_ip  device_names  interface  ip_address

# API Function: pim_verify_candidate_bsr_ip_not_present
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_candidate_bsr_ip_not_present(device_names, interface, ip_address)

	Robot API Call: 

		pim_verify_candidate_bsr_ip_not_present  device_names  interface  ip_address

# API Function: pim_verify_candidate_rp_ip
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_candidate_rp_ip(device_name, interface, ip_address, acl)

	Robot API Call: 

		pim_verify_candidate_rp_ip  device_name  interface  ip_address  acl

# API Function: pim_verify_candidate_rp_ip_group_mask
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_candidate_rp_ip_group_mask(device_name, interface, ip_address, acl)

	Robot API Call: 

		pim_verify_candidate_rp_ip_group_mask  device_name  interface  ip_address  acl

# API Function: pim_verify_rp_set
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_rp_set(device_name, mcast_group_address, ip)

	Robot API Call: 

		pim_verify_rp_set  device_name  mcast_group_address  ip

# API Function: pim_verify_rp_set_is_not_present
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_rp_set_is_not_present(device_name, mcast_group_address, ip_address)

	Robot API Call: 

		pim_verify_rp_set_is_not_present  device_name  mcast_group_address  ip_address

# API Function: pim_verify_candidate_rp_ip_not_present
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_candidate_rp_ip_not_present(device_names, interface, ip_address)

	Robot API Call: 

		pim_verify_candidate_rp_ip_not_present  device_names  interface  ip_address

# API Function: pim_verify_candidate_rp_static
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_candidate_rp_static(device_names)

	Robot API Call: 

		pim_verify_candidate_rp_static  device_names

# API Function: pim_verify_current_bsr_priority
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_current_bsr_priority(device_name, priority)

	Robot API Call: 

		pim_verify_current_bsr_priority  device_name  priority

# API Function: pim_verify_current_mode
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_current_mode(device_name, pim_mode)

	Robot API Call: 

		pim_verify_current_mode  device_name  pim_mode

# API Function: pim_verify_candidate_bsr_priority_interface
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_candidate_bsr_priority_interface(device_name, interface, priority)

	Robot API Call: 

		pim_verify_candidate_bsr_priority_interface  device_name  interface  priority

# API Function: pim_verify_candidate_bsr_priority_vlan
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_candidate_bsr_priority_vlan(device_name, vlan, priority)

	Robot API Call: 

		pim_verify_candidate_bsr_priority_vlan  device_name  vlan  priority

# API Function: pim_verify_any_source_group_entry
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_any_source_group_entry(device_name, dest_group)

	Robot API Call: 

		pim_verify_any_source_group_entry  device_name  dest_group

# API Function: pim_verify_any_source_group_entry_is_not_present
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_any_source_group_entry_is_not_present(device_name, dest_group)

	Robot API Call: 

		pim_verify_any_source_group_entry_is_not_present  device_name  dest_group

# API Function: pim_verify_source_group_entry
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_source_group_entry(device_name, source_ip, dest_group)

	Robot API Call: 

		pim_verify_source_group_entry  device_name  source_ip  dest_group

# API Function: pim_verify_source_group_entry_is_not_present
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_source_group_entry_is_not_present(device_name, source_ip, dest_group)

	Robot API Call: 

		pim_verify_source_group_entry_is_not_present  device_name  source_ip  dest_group

# API Function: pim_verify_cache_entry
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_cache_entry(device_name, mcast_group_address)

	Robot API Call: 

		pim_verify_cache_entry  device_name  mcast_group_address

# API Function: pim_verify_cache_entry_is_not_present
	Pytest API Call: 

		self.defaultLibrary.apiLowLevelApis.pim.pim_verify_cache_entry_is_not_present(device_name, mcast_group_address)

	Robot API Call: 

		pim_verify_cache_entry_is_not_present  device_name  mcast_group_address

