class Device360WebElementDefs:

    ports_from_device360_up_lldp_neighbour = \
        {
            'XPATH': '//div[@class="port-info port-lldp-neighbor  "]',
            'wait_for': 5
        }

    ports_from_device360_up = \
        {
            'XPATH': '//div[@data-dojo-attach-point="portFlexWrap"]//ul//li//ul//li',
            'wait_for': 5
        }

    lldp_neigbour_from_table = \
        {
            'XPATH': '//td[@class="dgrid-cell dgrid-column-2 field-lldpSystemName w75"]',
            'wait_for': 5
        }

    system_info_button = \
        {
            'XPATH': '//*[@data-id="systeminfo"]',
            'wait_for': 5
        }

    system_info_device_host_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceHostName"]',
            'wait_for': 5
        }

    system_info_network_policy = \
        {
            'XPATH': '//*[@data-dojo-attach-point="networkPolicyName"]',
            'wait_for': 5
        }

    system_info_device_model = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceModel"]',
            'wait_for': 5
        }

    system_info_device_function = \
        {
            'XPATH': '//span[@data-dojo-attach-point="deviceFunction"]',
            'wait_for': 5
        }

    system_info_device_template = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceTemplateName"]',
            'wait_for': 5
        }

    system_info_conf_type = \
        {
            'XPATH': '//*[@data-dojo-attach-point="configurationType"]',
            'wait_for': 5
        }

    system_info_serial_num = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceserialNumber"]',
            'wait_for': 5
        }

    system_info_iq_engine = \
        {
            'XPATH': '//*[@data-dojo-attach-point="displayVer"]',
            'wait_for': 5
        }

    system_info_dev_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceAdminStatus"]',
            'wait_for': 5
        }

    system_info_mgt0_ipv4 = \
        {
            'XPATH': '//*[@data-dojo-attach-point="mgmtIpAddress"]',
            'wait_for': 5
        }

    system_info_mgt0_ipv6 = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipv6Address"]',
            'wait_for': 5
        }

    system_info_ipv6_subnet = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipv6Netmask"]',
            'wait_for': 5
        }

    system_info_ipv4_subnet = \
        {
            'XPATH': '//*[@data-dojo-attach-point="subnetMask"]',
            'wait_for': 5
        }

    system_info_ipv4_default = \
        {
            'XPATH': '//*[@data-dojo-attach-point="defaultGateway"]',
            'wait_for': 5
        }

    system_info_ipv6_default = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipv6Gateway"]',
            'wait_for': 5
        }

    system_info_mgt0_mac = \
        {
            'XPATH': '//*[@data-dojo-attach-point="mgmtMacAddress"]',
            'wait_for': 5
        }

    system_info_dns = \
        {
            'XPATH': '//*[@data-dojo-attach-point="dnsSrvAddress"]',
            'wait_for': 5
        }

    system_info_ntp = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ntpSrvAddress"]',
            'wait_for': 5
        }

    close_dialog = \
        {
            'XPATH': "//div[@data-dojo-attach-point='closeDialog']",
            'wait_for': 10
        }

    select_100_elements_display_on_page = \
        {
            'XPATH': '//a[@data-size="100"]',
            'wait_for': 5
        }

    actions_adv_cli_access_cmd_input = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cli"]',
            'wait_for': 5
        }

    actions_adv_cli_access_cmd_apply = \
        {
            'XPATH': '//*[@data-dojo-attach-point="apply"]',
            'wait_for': 5
        }

    actions_adv_cli_access_cmd_output = \
        {
            'XPATH': '//*[@class="cli-command-result-pre"]',
            'wait_for': 5
        }

    device360_cells_href = \
        {
            'TAG_NAME': 'a',
            'wait_for': 5
        }

    device_active_clients_grid = \
        {
            'XPATH': '//*[@class="entity-content-ctn device-entity-connected-ctn"]//table[@class="dgrid-row-table"]',
            'index': 1,
            'wait_for': 5
        }

    device_active_clients_grid_rows = \
        {
            'XPATH': 'tr',
            'wait_for': 5
        }

    device_utilities_status = \
        {
            'XPATH': '//*[@class="ui-menu ui-menu-medium ui-menu-rt"]//a[contains(text(), "Status")]',
            'wait_for': 5
        }

    utilities_status_interface = \
        {
            'XPATH': '//*[@class="ui-menu ui-menu-medium ui-menu-rt"]//a[contains(text(), "Interface")]',
            'wait_for': 5
        }

    utilities_status_adv_channel_sel = \
        {
            'XPATH': '//*[@class="ui-menu ui-menu-medium ui-menu-rt"]//a[contains(text(), "Advanced Channel Selection Protocol")]',
            'wait_for': 5
        }

    utilities_status_wifi_status_summary = \
        {
            'XPATH': '//*[@class="ui-menu ui-menu-medium ui-menu-rt"]//a[contains(text(), "Wi-Fi Status Summary")]',
            'wait_for': 5
        }

    utilities_status_interface_name_dropdown = \
        {
            'XPATH': '//*[@class="option-list-ctn"]//span[contains(text(), "All")]',
            'wait_for': 5
        }

    utilities_status_interface_name_dropdown_opt = \
        {
            'XPATH': '//*[@class="chzn-results qa-chzn-results-optionlist"]//li',
            'wait_for': 5
        }

    utilities_status_interface_contents = \
        {
            'XPATH': '//*[@data-dojo-attach-point="contentList"]//pre',
            'wait_for': 5
        }

    utilities_status_adv_channel_sel_contents = \
        {
            'XPATH': '//*[@data-dojo-attach-point="contentList"]',
            'wait_for': 5
        }

    utilities_status_wifi_summary_station_btn = \
        {
            'XPATH': '//*[@class="ui-tab ui-tab-updated ui-tab-inactive clearfix"]//a[contains(text(), "Station")]',
            'wait_for': 5
        }

    utilities_status_wifi_summary_station_content = \
        {
            'XPATH': '//*[@data-dojo-attach-point="statusTabs"]//div[@class="ui-tab-panel-wrap clearfix "]',
            # 'index': 22,
            'wait_for': 5
        }

    device360_configure_button = \
        {
            'XPATH': '//li[@data-dojo-attach-point="configureViewSelect"]',
            'wait_for': 5
        }

    device360_unlock_port_config_button = \
        {
            'XPATH': "//span[@data-dojo-attach-point='unlockButton' and text()='UNLOCK']",
            'wait_for': 5
        }

    device360_unlock_port_config_confirmation_button = \
        {
            'XPATH': "//button[@data-dojo-attach-point='saveBtn' and text()='UNLOCK']",
            'wait_for': 5
        }
    
    device360_configure_ssh_cli_tab = \
        {
            'XPATH': '//*[@data-id="sshavailability"]',
            'wait_for': 5
        }

    device360_configure_ssh_web_tab = \
        {
            'XPATH': '//*[@data-id="sshavailability1"]',
            'wait_for': 5
        }

    device360_configure_ssh_cli_5min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-5"]',
            'wait_for': 5
        }

    device360_configure_ssh_cli_30min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-30"]',
            'wait_for': 5
        }

    device360_configure_ssh_cli_60min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-60"]',
            'wait_for': 5
        }

    device360_configure_ssh_cli_120min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-120"]',
            'wait_for': 5
        }

    device360_configure_ssh_cli_240min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-240"]',
            'wait_for': 5
        }

    device360_configure_ssh_cli_enable_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="setDeviceSSH"]',
            'wait_for': 15
        }

    device360_configure_ssh_cli_ip = \
        {
            'XPATH': '//*[@data-dojo-attach-point="addressInfo"]//*[@data-dojo-attach-point="ipAddress"]',
            'wait_for': 15
        }

    device360_configure_ssh_cli_port = \
        {
            'XPATH': '//*[@data-dojo-attach-point="port"]',
            'wait_for': 15
        }

    device360_configure_ssh_web_ip = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipAddress"]',
            'wait_for': 5,
            'index': 1
        }

    device360_configure_ssh_web_port = \
        {
            'XPATH': '//*[@data-dojo-attach-point="port"]',
            'wait_for': 5,
            'index': 1
        }

    device360_configure_ssh_web_url = \
        {
            'XPATH': '//*[@data-dojo-attach-point="exampleCommand"]',
            'wait_for': 5,
            'index': 1
        }

    device360_configure_ssh_web_enable_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="setDeviceSSH"]',
            'wait_for': 5,
            'index': 1
        }

    device360_configure_ssh_web_disable_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="setDeviceSSH" and contains(text(), "Disable SSH Web")]',
            'wait_for': 5,
        }

    device360_configure_ssh_web_5min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-5"]',
            'wait_for': 5
        }

    device360_configure_ssh_web_30min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-30"]',
            'wait_for': 5
        }

    device360_configure_ssh_web_60min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-60"]',
            'wait_for': 5
        }

    device360_configure_ssh_web_120min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-120"]',
            'wait_for': 5
        }

    device360_configure_ssh_web_240min_radio = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-ssh-240"]',
            'wait_for': 5
        }

    device360_device_configuration_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="configNav"]',
            'wait_for': 5
        }

    device360_port_configuration_button = \
        {
            'XPATH': '//li[contains(text(),"Port Configuration")]',
            'wait_for': 5
        }

    device360_port_configuration_title = \
        {
            'CSS_SELECTOR': '.port-configuration-title',
            'wait_for': 5
        }

    device360_configure_device_host_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="hostName"]',
            'wait_for': 5
        }

    device360_configure_device_snmp_location = \
        {
            'XPATH': '//*[@data-dojo-attach-point="snmpLocation"]',
            'wait_for': 5
        }

    device360_configure_device_network_policy = \
        {
            'XPATH': '//*[@data-dojo-attach-point="networkPolicyArea"]//a[contains(@class, "chzn-single")]/span',
            'wait_for': 5
        }

    device360_configure_device_device_template = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceTemplateArea"]//a[contains(@class, "chzn-single")]/span',
            'wait_for': 5
        }

    device360_configure_device_cancel_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceConfigNode"]//a[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5
        }

    device360_configure_device_save_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceConfigNode"]//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    device_info_ip_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipAddress"]',
            'wait_for': 5
        }

    device_info_mac_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="macAddress"]',
            'wait_for': 5
        }

    device_info_software_version = \
        {
            'XPATH': '//*[@data-dojo-attach-point="softwareVersion"]',
            'wait_for': 5
        }

    device_info_model = \
        {
            'XPATH': '//*[@data-dojo-attach-point="productType"]',
            'wait_for': 5
        }

    device_info_serial = \
        {
            # Commented on 1/18/23 because key names need to be unique so second XPATH value will always be taken
            # 'XPATH': '//*[@class="health-item service-tag data-item"]',
            'XPATH': '//*[@data-dojo-attach-point="portCtn"]//div[@data-dojo-attach-point="switchPortsPanelContainer"]//span[@data-dojo-attach-point="serviceTag"]',
            'wait_for': 5
        }

    device_info_make = \
        {
            'XPATH': '//*[@data-dojo-attach-point="make"]',
            'wait_for': 5
        }

    device_info_iqagent_version = \
        {
            'XPATH': '//*[@data-dojo-attach-point="hiveAgent"]',
            'wait_for': 5
        }

    device_info_device_policy = \
        {
            'XPATH': '//*[@data-dojo-attach-point="devicePolicy"]',
            'wait_for': 5
        }

    device360_configure_ssh_disable_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="setDeviceSSH"][@value="disable"]',
            'wait_for': 5
        }

    device360_events_link = \
        {
            'XPATH': '//*[@data-dojo-attach-point="eventsNav"]',
            'wait_for': 5
        }

    device360_events_grid = \
        {
            'XPATH': '//div[@data-dojo-attach-point="eventsList"]//div[contains(@class, "dgrid-content")]',
            'wait_for': 5
        }

    device360_events_grid_rows = \
        {
            'XPATH': 'div[@role="row"]',
            'wait_for': 5
        }

    device360_events_grid_cells = \
        {
            'XPATH': 'table[@class="dgrid-row-table"]/tr/td',
        }

    device360_event_timestamp = \
        {
            'XPATH': 'table[@class="dgrid-row-table"]/tr/td[contains(@class, "field-timestamp")]',
        }

    device360_event_description = \
        {
            'XPATH': 'table[@class="dgrid-row-table"]/tr/td[contains(@class, "field-description")]',

        }

    device360_event_severity = \
        {
            'XPATH': 'table[@class="dgrid-row-table"]/tr/td[contains(@class, "field-severity")]',

        }

    device360_alarms_link = \
        {
            'XPATH': '//*[@data-dojo-attach-point="alarmsTab"]',
            'wait_for': 5
        }

    device360_alarms_grid = \
        {
            'XPATH': '//div[@data-dojo-attach-point="alarmsList"]//table[@class="dgrid-row-table" and not(contains(@id, "-header"))]',
            'wait_for': 5
        }

    device360_alarms_grid_rows = \
        {
            'XPATH': 'tr',
            'wait_for': 5
        }

    device360_alarms_grid_cells = \
        {
            'XPATH': 'td',

         }

    device360_alarm_timestamp = \
        {
            'XPATH': '//div[@data-dojo-attach-point="alarmsList"]//td[contains(@class, "field-timestamp")]',
            'index': 0,
        }

    device360_alarm_category = \
        {
            'XPATH': '//div[@data-dojo-attach-point="alarmsList"]//td[contains(@class, "field-category")]',
            'index': 0,
        }

    device360_configure_port_list = \
        {
            'XPATH': '//div[@data-dojo-attach-point="listArea"]',
            'wait_for': 5
        }

    device360_configure_port_rows = \
        {
            # 'XPATH': '//div[contains(@class, "port-details-entry")]',
            'CSS_SELECTOR': '.port-details-entry',
            'wait_for': 5
        }

    device360_configure_port_row_cells = \
        {
            'CSS_SELECTOR': '.column',
            'wait_for': 5
        }

    device360_configure_port_row_state_toggle = \
        {
            'CSS_SELECTOR': '.port-enabled input[data-repeater-bind-to-field="enabled"]',
            'wait_for': 5
        }

    device360_configure_port_row_state_enabled = \
        {
            'CSS_SELECTOR': '.port-enabled input[checked]',
            'wait_for': 5
        }

    device360_configure_port_row_state_disabled = \
        {
            'CSS_SELECTOR': '.port-enabled input:not([checked])',
            'wait_for': 5
        }

    device360_configure_port_save_button = \
        {
            # 'XPATH': '//button[@data-dojo-attach-point="saveButton"]',
            'XPATH': '//button[@data-automation-tag="automation-port-config-save"] | //button[@data-automation-tag="automation-port-configuration-save-button"]',
            'wait_for': 5
        }

    device360_refresh_page_button = \
        {
            'XPATH': '//div[@class="entity-page-actions"]//div[@data-dojo-attach-point="pageRefresh"]',
            'wait_for': 5
        }

    device360_monitor_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="monitorViewSelect"]',
            'wait_for': 5
        }

    device360_monitor_overview_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="monitorOverviewTab"]',
            'wait_for': 5
        }

    device360_switch_system_info_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoNav"]',
            'wait_for': 5
        }

    device360_monitor_clients_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientNav"]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="diagnosticsNav"]',
            'wait_for': 5
        }

    device360_time_range_drop_down = \
        {
            'XPATH': '//div[@class="timeline-select-ctn"]//div[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 5
        }

    device360_time_range_drop_down_selection = \
        {
            'XPATH': '//div[@class="timeline-select-ctn"]//div[@data-automation-tag="automation-chzn-container-ctn"]//span',
            'wait_for': 5
        }

    device360_time_range_drop_down_items = \
        {
            'XPATH': '//div[@class="timeline-select-ctn"]//div[@data-automation-tag="automation-chzn-container-ctn"]//ul/li',
            'wait_for': 5
        }

    device360_day_time_range_one_hour_button = \
        {
            'XPATH': '//ul[@class="time-range-picker day-range"]//li[@data-dojo-attach-point="oneHour"]',
            'wait_for': 5
        }

    device360_day_time_range_two_hour_button = \
        {
            'XPATH': '//ul[@class="time-range-picker day-range"]//li[@data-dojo-attach-point="twoHour"]',
            'wait_for': 5
        }

    device360_day_time_range_four_hour_button = \
        {
            'XPATH': '//ul[@class="time-range-picker day-range"]//li[@data-dojo-attach-point="fourHour"]',
            'wait_for': 5
        }

    device360_day_time_range_eight_hour_button = \
        {
            'XPATH': '//ul[@class="time-range-picker day-range"]//li[@data-dojo-attach-point="eightHour"]',
            'wait_for': 5
        }

    device360_day_time_range_twenty_four_hour_button = \
        {
            'XPATH': '//ul[@class="time-range-picker day-range"]//li[@data-dojo-attach-point="twentyFourHour"]',
            'wait_for': 5
        }

    device360_week_time_range_one_day_button = \
        {
            'XPATH': '//ul[@class="time-range-picker week-range"]//li[@data-dojo-attach-point="oneDay"]',
            'wait_for': 5
        }

    device360_week_time_range_two_day_button = \
        {
            'XPATH': '//ul[@class="time-range-picker week-range"]//li[@data-dojo-attach-point="twoDay"]',
            'wait_for': 5
        }

    device360_week_time_range_seven_day_button = \
        {
            'XPATH': '//ul[@class="time-range-picker week-range"]//li[@data-dojo-attach-point="sevenDay"]',
            'wait_for': 5
        }

    device360_month_time_range_seven_day_button = \
        {
            'XPATH': '//ul[@class="time-range-picker month-range"]//li[@data-dojo-attach-point="oneWeek"]',
            'wait_for': 5
        }

    device360_month_time_range_fourteen_day_button = \
        {
            'XPATH': '//ul[@class="time-range-picker month-range"]//li[@data-dojo-attach-point="twoWeek"]',
            'wait_for': 5
        }

    device360_month_time_range_thirty_day_button = \
        {
            'XPATH': '//ul[@class="time-range-picker month-range"]//li[@data-dojo-attach-point="thirtyDay"]',
            'wait_for': 5
        }

    device360_month_time_range_ninety_day_button = \
        {
            'XPATH': '//ul[@class="time-range-picker month-range"]//li[@data-dojo-attach-point="ninetyDay"]',
            'wait_for': 5
        }

    device360_port_diagnostics_select_all_ports_button = \
        {
            'XPATH': '//div[@class="selection-buttons"]//button[@data-dojo-attach-point="selectAllButton"]',
            'wait_for': 5
        }

    device360_port_diagnostics_deselect_all_ports_button = \
        {
            'XPATH': '//div[@class="selection-buttons"]//button[@data-dojo-attach-point="deselectAllButton"]',
            'wait_for': 5
        }

    device360_port_diagnostics_selected_ports = \
        {
            'XPATH': '//div[contains(@class, "device-ports")]/ul//li/ul/li/div[(contains(@class, "active"))]',
            'wait_for': 5
        }

    device360_port_diagnostics_deselected_ports = \
        {
            'XPATH': '//div[contains(@class, "device-ports")]/ul//li/ul/li/div[not(contains(@class, "active"))]',
            'wait_for': 5
        }

    device360_monitor_overview_chart_graph = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceoverview"]//div[@data-dojo-attach-point="highChartCtn"]',
            'wait_for': 5
        }

    device360_monitor_clients_chart_graph = \
        {
            'XPATH': '//div[@data-dojo-attach-point="connectedclients"]//div[@data-dojo-attach-point="highChartCtn"]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_chart_graph = \
        {
            'XPATH': '//div[contains(@class, "device-diagnostics")]//div[@data-dojo-attach-point="highChartCtn"]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_chart_graph_port_errors = \
        {
            'XPATH': '//div[contains(@class, "device-diagnostics")]//div[@data-dojo-attach-point="portErrorsCtn"]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_chart_graph_port_casts = \
        {
            'XPATH': '//div[contains(@class, "device-diagnostics")]//div[@data-dojo-attach-point="portCastsCtn"]',
            'wait_for': 5
        }

    overview_ip_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipAddress"]',
            'wait_for': 5
        }

    overview_mac_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="macAddress"]',
            'wait_for': 5
        }

    overview_software_version = \
        {
            'XPATH': '//*[@data-dojo-attach-point="softwareVersion"]',
            'wait_for': 5
        }

    overview_model = \
        {
            'XPATH': '//*[@data-dojo-attach-point="productType"]',
            'wait_for': 5
        }

    overview_serial = \
        {
            'XPATH': '//*[@data-dojo-attach-point="serviceTag"]',
            'wait_for': 5
        }

    overview_make = \
        {
            'XPATH': '//*[@data-dojo-attach-point="make"]',
            'wait_for': 5
        }

    device360_configure_device_function_dropdown = \
        {
            'XPATH': '//div[@class="device-config-section"]//select[@data-dojo-attach-point="deviceFunction"]/../div[@data-automation-tag="chzn-container-ctn"]',
            'wait_for': 5
        }

    device360_configure_device_function_dropdown_items = \
        {
            'XPATH': '//div[@class="device-config-section"]//select[@data-dojo-attach-point="deviceFunction"]/../div[@data-automation-tag="chzn-container-ctn"]//ul/li',
            'wait_for': 5
        }

    device360_device_title = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceTitle"]',
            'wait_for': 5
        }

    device360_sidebar_model = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceModel"]',
            'wait_for': 5
        }

    device360_sidebar_device_image = \
        {
            'XPATH': '//div[@data-dojo-attach-point="deviceImg"]/img',
            'wait_for': 5
        }

    device360_sidebar_host_name = \
        {
            'XPATH': '//strong[@data-dojo-attach-point="deviceHostName"]',
            'wait_for': 5
        }

    device360_sidebar_enabled_ports = \
        {
            'XPATH': '//strong[@data-dojo-attach-point="portEnable"]',
            'wait_for': 5
        }

    device360_sidebar_disabled_ports = \
        {
            'XPATH': '//strong[@data-dojo-attach-point="portDisable"]',
            'wait_for': 5
        }

    device360_sidebar_connected_state = \
        {
            'XPATH': '//p[@data-dojo-attach-point="deviceConnectedTest"]',
            'wait_for': 5
        }

    device360_sidebar_active_since = \
        {
            'XPATH': '//p[@data-dojo-attach-point="connectedTime"]',
            'wait_for': 5
        }

    device360_sidebar_active_alarms = \
        {
            'XPATH': '//span[@data-id="alarmDetails"]',
            'wait_for': 5
        }

    device360_sidebar_unique_clients = \
        {
            'XPATH': '//span[@data-id="connectedclients"]',
            'wait_for': 5
        }

    device360_sidebar_cpu_usage = \
        {
            'XPATH': '//div[@class="title" and text()="CPU Usage"]/../div[@data-dojo-attach-point="metricElem"]',
            'wait_for': 5
        }

    device360_sidebar_memory_usage = \
        {
            'XPATH': '//div[@class="title" and text()="Memory Usage"]/../div[@data-dojo-attach-point="metricElem"]',
            'wait_for': 5
        }

    device360_tooltip_content = \
        {
            'XPATH': '//div[@class="tooltip-content"]',
            'wait_for': 5
        }

    device360_topbar_cpu = \
        {
            'XPATH': '//div[@data-dojo-attach-point="cpuElement"]',
            'wait_for': 5
        }

    device360_topbar_memory = \
        {
            'XPATH': '//div[@data-dojo-attach-point="memoryElement"]',
            'wait_for': 5
        }

    device360_topbar_mac_usage = \
        {
            'XPATH': '//div[@data-dojo-attach-point="macElement"]',
            'wait_for': 5
        }

    device360_topbar_uptime = \
        {
            'XPATH': '//div[@data-dojo-attach-point="uptimeElement"]',
            'wait_for': 5
        }

    device360_topbar_temperature = \
        {
            'XPATH': '//span[@class="temperature-digits"]',
            'wait_for': 5
        }

    device360_topbar_power = \
        {
            'XPATH': '//div[@data-dojo-attach-point="powerElement"]',
            'wait_for': 5
        }

    device360_topbar_fan = \
        {
            'XPATH': '//div[@data-dojo-attach-point="fanElement"]',
            'wait_for': 5
        }

    device360_topbar_ip_address = \
        {
            'XPATH': '//span[@data-dojo-attach-point="ipAddress"]',
            'wait_for': 5
        }

    device360_topbar_mac_address = \
        {
            'XPATH': '//span[@data-dojo-attach-point="macAddress"]',
            'wait_for': 5
        }

    device360_topbar_software_version = \
        {
            'XPATH': '//span[@data-dojo-attach-point="softwareVersion"]',
            'wait_for': 5
        }

    device360_topbar_model = \
        {
            'XPATH': '//span[@data-dojo-attach-point="productType"]',
            'wait_for': 5
        }

    device360_topbar_serial = \
        {
            'XPATH': '//span[@data-dojo-attach-point="serviceTag"]',
            'wait_for': 5
        }

    device360_topbar_make = \
        {
            'XPATH': '//span[@data-dojo-attach-point="make"]',
            'wait_for': 5
        }

    device360_open_site_engine_link = \
        {
            'XPATH': '//a[@data-dojo-attach-point="seLink"]',
            'wait_for': 5
        }

    device360_overview_port_icons = \
        {
            'XPATH': '//div[@class="device-ports"]/ul/li/ul/li',
            'wait_for': 5
        }

    device360_overview_port_details_table = \
        {
            'XPATH': '//div[@data-dojo-attach-point="portDetailsContainer"]/ul[@class="portdetails-table"]',
            'wait_for': 5
        }

    device360_overview_total_active_alarms = \
        {
            'XPATH': '//h1[@data-dojo-attach-point="totalMetric"]',
            'wait_for': 5
        }

    system_info_device_ssids = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ssids"]',
            'wait_for': 5
        }

    switch_system_info_archived = \
        {
            'XPATH': '//td[contains(@class, "field-archived")]',
            'wait_for': 5
        }

    switch_system_info_asset_tag = \
        {
            'XPATH': '//td[contains(@class, "field-assetTag")]',
            'wait_for': 5
        }

    switch_system_info_user_data_1 = \
        {
            'XPATH': '//td[contains(@class, "field-userData1")]',
            'wait_for': 5
        }

    switch_system_info_user_data_2 = \
        {
            'XPATH': '//td[contains(@class, "field-userData2")]',
            'wait_for': 5
        }

    switch_system_info_user_data_3 = \
        {
            'XPATH': '//td[contains(@class, "field-userData3")]',
            'wait_for': 5
        }

    switch_system_info_user_data_4 = \
        {
            'XPATH': '//td[contains(@class, "field-userData4")]',
            'wait_for': 5
        }

    switch_system_info_note = \
        {
            'XPATH': '//td[contains(@class, "field-note")]',
            'wait_for': 5
        }

    hyper_link_device_template = \
        {
            'CSS_SELECTOR': '.link-item',
            'wait_for': 5
        }

    device360_stack_configure_device_snmp_location = \
        {
            'XPATH': '//*[@data-dojo-attach-point="snmpLocationInput"]',
            'wait_for': 5
        }

    device360_dev_config_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    device360_title_stack_info = \
        {
            'XPATH': '//*[@data-dojo-attach-point="numStackMembers"]',
            'wait_for': 5
        }

    device360_topbar_iqagent_version = \
        {
            'XPATH': '//span[@data-dojo-attach-point="hiveAgent"]',
            'wait_for': 5
        }

    device360_topbar_stack_mem_status = \
        {
            'XPATH': '//span[@data-dojo-attach-point="stackMemberStatus"]',
            'wait_for': 5
        }

    device360_switch_sidebar_active_alarms = \
        {
            'XPATH': '//*[@data-automation-tag="device-entity-active-alarms-number"]',
            'wait_for': 5
        }

    device360_switch_sidebar_unique_clients = \
        {
            'XPATH': '//*[@data-automation-tag="device-entity-unique-clients-number"]',
            'wait_for': 5
        }

    device360_stack_topbar_power = \
        {
            'XPATH': '//div[@data-dojo-attach-point="powerElement"]',
            'wait_for': 5
        }

    device360_stack_topbar_fan = \
        {
            'XPATH': '//div[@data-dojo-attach-point="fanElement"]',
            'wait_for': 5
        }

    device360_fan_tooltip_content = \
        {
            'CSS_SELECTOR': '.ui-tipbox-ctn',
            'wait_for': 5
        }

    device360_stack_overview_port_icons = \
        {
            'XPATH': '//div[@class="device-ports"]/ul/li/ul/li//div',
            'wait_for': 5
        }

    device360_stack_overview_sl_ports_row = \
        {
            'CSS_SELECTOR': '[class="stack-ports-ctn switch-ports-panel-ctn"] [data-dojo-attach-point="switchDom"]',
            'wait_for': 5
        }

    device360_stack_overview_slot_ports = \
        {
            'CLASS_NAME': 'AH-ports-icons',
            'wait_for': 5
        }

    device360_stack_select_port_group = \
        {
            'XPATH': '//div[@class="device-ports"]//li[contains(@class, "port-group")',
            'wait_for': 5
        }

    device360_asic_port_groups = \
        {
            'XPATH': '//li[contains(@class, "port-group port-group-") and not(contains(@class, "active-result"))]'
        }

    device360_ports_each_asic_port_group = \
        {
            'XPATH': './/div[contains(@data-automation-tag, "automation-port-")]',
            'wait_for': 5
        }

    device360_asic_port_groups_stack = \
        {
            'XPATH': '//li[contains(@class, "port-group port-group-")]'
        }

    device360_ports_each_asic_port_group_stack = \
        {
            'XPATH': './/div[contains(@data-automation-tag, "automation-port-${slot}")]',
            'wait_for': 5
        }

    device360_stack_port_table_port_name = \
        {
            'XPATH': '//*[@class="portdetails-table"]//span[contains(text(), "Port Name")]//following-sibling::span[contains(text(), "")]',
            'wait_for': 5
        }

    device360_stack_port_table_port_type = \
        {
            'XPATH': '//*[@class="portdetails-table"]//span[contains(text(),"Type")]/following-sibling::span[contains(text(),"")]',
            'wait_for': 5
        }

    device360_stack_port_table_port_status = \
        {
            'XPATH': '//*[@class="portdetails-table"]//span[contains(text(),"Port Status")]/following-sibling::span[contains(text(),"")]',
            'wait_for': 5
        }

    device360_stack_port_table_port_mode = \
        {
            'XPATH': '//*[@class="portdetails-table"]//span[contains(text(),"Port Mode")]/following-sibling::span[contains(text(),"")]',
            'wait_for': 5
        }

    device360_stack_port_table_port_vlan = \
        {
            'XPATH': '//*[@class="portdetails-table"]//span[contains(text(),"VLAN")]/following-sibling::span[contains(text(),"")]',
            'wait_for': 5
        }

    device360_stack_port_table_port_speed = \
        {
            'XPATH': '//*[@class="portdetails-table"]//span[contains(text(),"Port Speed")]/following-sibling::span[contains(text(),"")]',
            'wait_for': 5
        }

    device360_stack_system_info_button = \
        {
            'XPATH': '//li[@data-dojo-attach-point="stackSystemInfoNav"]',
            'wait_for': 5
        }

    stack_system_info_unit_number = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-unitNumber")]',
            'wait_for': 5
        }

    stack_system_info_ip_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-ipAddress")]',
            'wait_for': 5
        }

    stack_system_info_netmask = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-netMask")]',
            'wait_for': 5
        }

    stack_system_info_mac = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-macAddress")]',
            'wait_for': 5
        }

    stack_system_info_serial_num = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-serialNumber")]',
            'wait_for': 5
        }

    stack_system_info_prod_type = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-productType")]',
            'wait_for': 5
        }

    stack_system_info_make = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-make")]',
            'wait_for': 5
        }

    stack_system_info_admin_state = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-adminState")]',
            'wait_for': 5
        }

    stack_system_info_software_ver = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-softwareVersion")]',
            'wait_for': 5
        }

    stack_system_info_stack_mgmt_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackSystemInfoWrapper"]//*[contains(@class, "field-stackManagementStatus")]',
            'wait_for': 5
        }

    sw_template_stack_add_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="switchesMenu"]//ul/li/a',
            'wait_for': 5
        }

    sw_template_stack_added_items = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="templateElements"]/li',
            'wait_for': 5
        }

    sw_template_stack_first_page = \
        {
            'CSS_SELECTOR': '.stack-template',
            'wait_for': 5
        }

    device360_device_configuration_stack_template_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackTemplateArea"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    device360_device_configuration_stack_template_items = \
        {
            'XPATH': '//*[@data-dojo-attach-point="stackTemplateArea"]//div[@class="chzn-drop"]/ul/li',
            'wait_for': 5
        }

    device360_device_configuration_save_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    device360_device_configuration_update_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="deployNowBtn"]',
            'wait_for': 5
        }

    device360_device_configuration_exit_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }

    d360Event_search_textbox = \
        {
            'XPATH': '//input[@data-dojo-attach-point="eventSearchInput"]',
            'wait_for': 3
        }

    device360_configure_vlan_port_one = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portOverrideNode"]//input[@data-dojo-attach-point="accessPortVLAN"]',
            'wait_for': 5
        }

    d360_configure_port_row_override_revert = \
        {
            'CSS_SELECTOR': '.override-revert',
            'wait_for': 5
        }

    d360_configure_port_row_revert_button = \
        {
            'XPATH': '//*[@class="revert-tip-button"]',
            'wait_for': 3
        }

    device360_configure_port_settings_aggregation_rows = \
        {
            'XPATH': '//div[contains(@class, "port-settings-entry")]',
            'wait_for': 5
        }

    device360_configure_stp_rows = \
        {
            'XPATH': '//div[contains(@class, "port-stp-entry")] | //div[@data-dojo-attach-point="listArea"]//div[contains(@componentpath, "STPEntry")]',
            'wait_for': 5
        }

    device360_configure_storm_control_rows = \
        {
            'XPATH': '//div[contains(@class, "port-storm-control-entry")]',
            'wait_for': 5
        }

    d360_configure_port_state_override_revert = \
        {
            'XPATH': '//div[@class="port-enabled"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_port_usage_override_revert = \
        {
            'XPATH': '//div[@class="port-type-choose"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_vlan_override_revert = \
        {
            'XPATH': '//div[@class="port-vlan-type port-vlan-type-trunk"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_description_override_revert = \
        {
            'XPATH': '//div[@class="port-description"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_transmission_override_revert = \
        {
            'XPATH': '//div[@class="port-transmission-type"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_speed_override_revert = \
        {
            'XPATH': '//div[@class="port-transmission-speed"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_flow_override_revert = \
        {
            'XPATH': '//div[@class="port-flow-control "]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_transmit_override_revert = \
        {
            'XPATH': '//div[@class="port-lldp-transmit cb-field"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_receive_override_revert = \
        {
            'XPATH': '//div[@class="port-lldp-recieve cb-field"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_cdp_override_revert = \
        {
            'XPATH': '//div[@class="port-cdp-receive cb-field "]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_client_reporting_override_revert = \
        {
            'XPATH': '//div[@class="port-client-reporting cb-field"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_stp_status_override_revert = \
        {
            'XPATH': '//div[@class="port-stp-status"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_edge_port_override_revert = \
        {
            'XPATH': '//div[@class="port-stp-edge-port"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_bpdu_protection_override_revert = \
        {
            'XPATH': '//div[@class="port-stp-bpdu-protection "]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_priority_override_revert = \
        {
            'XPATH': '//div[@class="port-stp-priority"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_path_cost_override_revert = \
        {
            'XPATH': '//div[@class="port-stp-path-cost"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_broadcast_override_revert = \
        {
            'XPATH': '//div[@class="port-broadcast-traffic"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_unknown_unicast_override_revert = \
        {
            'XPATH': '//div[@class="port-unknown-unicast"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_multicast_override_revert = \
        {
            'XPATH': '//div[@class="port-multicast"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_value_override_revert = \
        {
            'XPATH': '//div[@class="port-rate-limit-value"]//*[@class="override-revert"]',
            'wait_for': 5
        }

    d360_configure_port_details_tab_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ahTabContainer"]//a[contains(text(), "Port Details")]',
            'wait_for': 5
        }

    d360_configure_port_settings_aggregation_tab_button = \
        {
            'CSS_SELECTOR': '.ui-tab[data-automation-tag="automation-port-config-port-settings"]',
            'wait_for': 5
        }

    d360_configure_port_stp_tab_button = \
        {
            'XPATH': "//a[text()='STP'] | //div[@data-automation-tag='automation-port-configuration-stp']//a[contains(text(), 'STP')]",
            'wait_for': 5
        }

    d360_configure_port_storm_control_tab_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ahTabContainer"]//a[contains(text(), "Storm Control")]',
            'wait_for': 5
        }

    d360_configure_port_state_click_button = \
        {
            'CSS_SELECTOR': '.port-enabled input[data-repeater-bind-to-field="enabled"]',
            'wait_for': 5
        }

    d360_configure_transmit_click_checkbox = \
        {
            'CSS_SELECTOR': '.port-lldp-transmit input[data-repeater-bind-to-field="enableLldpTransmit"]',
            'wait_for': 5
        }

    d360_configure_receive_click_checkbox = \
        {
            'CSS_SELECTOR': '.port-lldp-recieve input[data-repeater-bind-to-field="enableLldpReceive"]',
            'wait_for': 5
        }

    d360_configure_cdp_click_checkbox = \
        {
            'CSS_SELECTOR': '.port-cdp-receive input[data-repeater-bind-to-field="enableCdpReceive"]',
            'wait_for': 5
        }

    d360_configure_client_reporting_click_checkbox = \
        {
            'CSS_SELECTOR': '.port-client-reporting input[data-repeater-bind-to-field="enableClientReporting"]',
            'wait_for': 5
        }

    d360_configure_stp_status_click_button = \
        {
            'CSS_SELECTOR': '.port-stp-status input[data-repeater-bind-to-field="enabled"]',
            'wait_for': 5
        }

    d360_configure_edge_port_click_button = \
        {
            'CSS_SELECTOR': '.port-stp-edge-port input[data-repeater-bind-to-field="enableEdgePort"]',
            'wait_for': 5
        }

    d360_configure_broadcast_click_checkbox = \
        {
            'CSS_SELECTOR': '.checkbox input[data-repeater-bind-to-field="enableBroadcastTraffic"]',
            'wait_for': 5
        }

    d360_configure_unknown_unicast_click_checkbox = \
        {
            'CSS_SELECTOR': '.checkbox input[data-repeater-bind-to-field="enableUnknownUnicastTraffic"]',
            'wait_for': 5
        }

    d360_configure_multicast_click_checkbox = \
        {
            'CSS_SELECTOR': '.checkbox input[data-repeater-bind-to-field="enableMuticastTraffic"]',
            'wait_for': 5
        }

    d360_switch_port_view_all_pages_button = \
        {
            'XPATH': '//div[@class="pagination-size-ctn"]//span[contains(text(),"100")]',
            'wait_for': 3
        }

    d360_switch_ports_table_port_name_cell = \
        {
            'CSS_SELECTOR': '.field-ifName',
            'wait_for': 3
        }

    d360_switch_ports_table_grid_rows = \
        {
            'XPATH': '//*[@data-dojo-attach-point="portGridNode"]//*[@class="dgrid-row-table"]',
        }

    d360_switch_ports_table_last_row_of_table = \
        {
            'CSS_SELECTOR': '[data-dojo-attach-point="portGridNode"] '
                            '[class="dgrid-content ui-widget-content"]>:last-child',
            'wait_for': 5
        }

    device360_switch_port_table_port_name = \
        {
            'CSS_SELECTOR': '.field-ifName',
            'wait_for': 5
        }

    device360_switch_port_table_port_type = \
        {
            'CSS_SELECTOR': '.field-pType',
            'wait_for': 5
        }

    device360_switch_port_table_lacp_neighbor = \
        {
            'CSS_SELECTOR': '.field-lldpSystemName',
            'wait_for': 5
        }

    device360_switch_port_table_lacp_status = \
        {
            'CSS_SELECTOR': '.field-lacpActive',
            'wait_for': 5
        }

    device360_switch_port_table_port_status = \
        {
            'CSS_SELECTOR': '.field-status',
            'wait_for': 5
        }

    device360_switch_port_table_transmission_mode = \
        {
            'CSS_SELECTOR': '.field-transmissionMode',
            'wait_for': 5
        }

    device360_switch_port_table_port_mode = \
        {
            'CSS_SELECTOR': '.field-portMode',
            'wait_for': 5
        }

    device360_switch_port_table_access_vlan = \
        {
            'CSS_SELECTOR': '.field-vlan',
            'wait_for': 5
        }

    device360_switch_port_table_tagged_vlans = \
        {
            'CSS_SELECTOR': '.field-taggedVlans',
            'wait_for': 5
        }

    device360_switch_port_table_traffic_received = \
        {
            'CSS_SELECTOR': '.field-rxByteCount',
            'wait_for': 5
        }

    device360_switch_port_table_traffic_transmitted = \
        {
            'CSS_SELECTOR': '.field-txByteCount',
            'wait_for': 5
        }

    device360_switch_port_table_power_used = \
        {
            'CSS_SELECTOR': '.field-powerUsed',
            'wait_for': 5
        }

    device360_switch_port_table_port_speed = \
        {
            'CSS_SELECTOR': '.field-portSpeed',
            'wait_for': 5
        }

    d360_monitor_items_rows = \
        {
            'XPATH': '//div[contains(@class, "dgrid-row  ui-state-default")]',
            'wait_for': 5
        }

    d360_monitor_transmission_mode = \
        {
            'CSS_SELECTOR': '.field-transmissionMode',
            'wait_for': 5
        }

    d360_monitor_port_speed = \
        {
            'CSS_SELECTOR': '.field-portSpeed',
            'wait_for': 5
        }
    device360_port_settings_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-port-configuration-port-settings"]',
            'wait_for': 5
        }

    icon_ports_items = \
        {
            'XPATH': '//li[contains(@class,"port-rel")]',
            'wait_for': 5
        }

    port_click = \
        {
            'CSS_SELECTOR': '.AH-ports-icons',
            'wait_for': 5
        }

    d360_interface_transmission_mode = \
        {
            'XPATH': '//*[@class="port-info port-trans-mode  "]/b',
            'wait_for': 5
        }
    d360_interface_port_speed = \
        {
            'XPATH': '//*[@class="port-info port-speed  low "]/b',
            'wait_for': 5
        }

    d360_view_100_rows_on_page = \
        {
            'XPATH': '//div[@class="pagination-size-ctn"]//span[contains(text(), "100")]',
            'wait_for': 5
        }
    d360_monitor_port_name = \
        {
            'XPATH': 'table[@class="dgrid-row-table"]/tr/td[contains(@class, "field-ifName")]',
        }

    d360_monitor_lldp_neighbor_header = \
        {
            'XPATH': '//th[contains(@class, "field-lldpSystemName")]',
            'wait_for': 5
        }

    d360_monitor_interface_name = \
        {
            'CSS_SELECTOR': '.field-ifName',
            'wait_for': 5
        }

    d360_vim_model = \
        {
            'XPATH': '//div[@data-dojo-attach-point="portBlockWrap"]//li[@class="port-group-label"]',
            'wait_for': 5
        }

    device360_stack_slot_vim_ports = \
        {
            'CSS_SELECTOR': '[class="switch-panel switch-stack-panel"] [data-automation-tag^="vim-port-group"] [data-automation-tag^="automation-port-"]',
            'wait_for': 5
        }

    device360_get_ports_by_type_slot = \
        {
            'XPATH': '//div[contains(@class, "${type}") and starts-with(@data-automation-tag,"automation-port-${slot}:")]',
            'wait_for': 5
        }

    d360_vim_ports = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="utilPortWrap"]//span[contains(@class,"port-desc")]',
            'wait_for': 5
        }

    d360_wireframe_port = \
        {
            'XPATH': '//div[@class="device-ports device-ports--padding"]/ul/li/ul/li',
            'wait_for': 5
        }

    d360_wireframe_sfp28_port = \
        {
            'XPATH': '//div[@class="device-ports device-ports--padding"]/ul/li/ul/li[contains(@class,"port-theme-qsfp28")]',
            'wait_for': 5
        }

    d360_wireframe_ether_port = \
        {
            'XPATH': '//div[@class="device-ports device-ports--padding"]/ul/li/ul/li[contains(@class,"port-theme-gray") or contains(@class,"port-theme-white")]',
            'wait_for': 5
        }
    d360_automation_port = \
        {
            'XPATH': '//div[@class="device-ports device-ports--padding"]/ul/li/ul/li/div',
            'wait_for': 5
        }

    d360_port_leftclick_interface_name = \
        {
            'XPATH': '//div[@class="port-info interface-name"]',
            'wait_for': 5
        }

    d360_port_leftclick_interface_type = \
        {
            'XPATH': '//div[@class="port-info port-type "]',
            'wait_for': 5
        }

    d360_port_leftclick_port_mode = \
        {
            'XPATH': '//div[starts-with(@class, "port-info port-mode")]',
            'wait_for': 5
        }

    d360_port_leftclick_access_vlan = \
        {
            'XPATH': '//div[@class="port-info port-vlan  "]',
            'wait_for': 5
        }

    d360_port_leftclick_tagged_vlan = \
        {
            'XPATH': '//div[@class="port-info port-tagged-vlan   "]',
            'wait_for': 5
        }

    d360_port_leftclick_port_status = \
        {
            'XPATH': '//div[@class="port-info port-status-a "]',
            'wait_for': 5
        }

    device360_create_auto_template_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="createStackTemplate"]',
            'wait_for': 5
        }

    d360_pagination_next_button = \
        {
            'XPATH': '//div[@class="pagination-num-ctn"]//span[@class="ui-page-item J-page-next ui-page-item-next "]',
            'wait_for': 3
        }

    d360_pagination_page_button = \
        {
            'XPATH': '//span[@class="pagination-page"]',
            'wait_for': 3
        }

    device360_port_configuration_content = \
        {
            # 'CSS_SELECTOR': '.port-configuration',
            # 'wait_for': 5
            'XPATH': '//*[@data-dojo-attach-point="portconfiguration"]',
            'wait_for': 5
        }

    device360_configure_port_configuration_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="configureNav"]//li[@data-id="portconfiguration"]',
            'wait_for': 5
        }

    sw_template_stack_sw_item = \
        {
            'XPATH': '//span[@data-dojo-attach-point="deviceType"]',
            'wait_for': 5
        }

    device360_configure_port_usage_drop_down_button = \
        {
            'CSS_SELECTOR': '.chzn-single',
            'wait_for': 5
        }

    device360_configure_port_usage_drop_down_options = \
        {
            'CSS_SELECTOR': '.active-result',
            'wait_for': 5
        }

    device360_configure_port_access_vlan_textfield = \
        {
            'CSS_SELECTOR': '.port-type-vlan-value',
            'wait_for': 5
        }

    device360_configure_onboarding_port_vlan_textfield = \
        {
            'CSS_SELECTOR': '.portUsageVLANfield.onboardingVLAN',
            'wait_for': 5
        }

    device360_configure_disabled_port_vlan_textfield = \
        {
            'CSS_SELECTOR': '.portUsageVLANfield.disabledVLAN',
            'wait_for': 5
        }

    device360_configure_port_trunk_native_vlan_textfield = \
        {
            'CSS_SELECTOR': '.native-vlan',
            'index': 1,
            'wait_for': 5
        }

    device360_configure_port_trunk_vlan_textfield = \
        {
            'CSS_SELECTOR': '.allowed-vlan',
            'index': 1,
            'wait_for': 5
        }

    device360_port_configuration_port_settings_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-port-configuration-port-settings"]',
            'wait_for': 5
        }

    device360_port_settings_transmission_mode_drop_down_button = \
        {
            'CSS_SELECTOR': '.chzn-single',
            'wait_for': 5
        }

    device360_port_settings_transmission_mode_drop_down_options = \
        {
            'CSS_SELECTOR': '.chzn-results.qa-chzn-results-transmissiontype li',
            'wait_for': 5
        }

    device360_port_settings_speed_drop_down_button = \
        {
            'CSS_SELECTOR': '.chzn-single',
            'index': 1,
            'wait_for': 5
        }

    device360_port_settings_speed_drop_down_options = \
        {
            'CSS_SELECTOR': '.chzn-results.qa-chzn-results-speed li',
            'wait_for': 5
        }

    device360_configure_port_pse_poe_state_enabled = \
        {
            'CSS_SELECTOR': '.grid_2 column.not-master-content input[checked]',
            'wait_for': 5
        }

    device360_configure_port_pse_poe_state_disabled = \
        {
            'CSS_SELECTOR': '..grid_2 column.not-master-content input:not([checked])',
            'wait_for': 5
        }

    device360_port_configuration_pse_tab = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-config-pse" or @data-automation-tag="automation-port-configuration-pse"]',
            'wait_for': 5
        }

    device360_port_configuration_pse_profile_select_button = \
        {
            'CSS_SELECTOR': '.ui-ip-mark',
            'wait_for': 5
        }

    device360_port_configuration_pse_profile_drop_down_options = \
        {
            'XPATH': '//ul[@class="item-area"]/li[@class="J-ip-item"]',
            'wait_for': 5
        }

    device360_wireframe_cpu_utilization_tooltip_content = \
        {
            'XPATH': '//*[contains(text(), "CPU Usage:")]',
            'wait_for': 5
        }

    device360_wireframe_cpu_utilization_piechart = \
        {
            'CSS_SELECTOR': '.highcharts-point.highcharts-color-0',
            'wait_for': 5
        }

    result_area = \
        {
            'XPATH': '//div[@data-dojo-attach-point="cliPaneResutArea"]',
            'wait_for': 5
        }

    advanced_button = \
        {
            'XPATH': '//div[@data-automation-tag="automation-manage-device-actions"]//li[@class="ui-menu-item ui-menu-item-pa"]//a',
            'wait_for': 5
        }

    actions_button = \
        {
            'XPATH': '//button[contains(text(),"Actions")]',
            'wait_for': 5
        }

    cli_command_line = \
        {
            'XPATH': '//div[@data-dojo-attach-point="mainContent"]//input[@data-dojo-attach-point="cli"]',
            'wait_for': 5
        }

    device_rows = \
        {
            'XPATH': '//div[@class="dgrid-content ui-widget-content"]//tr',
            'wait_for': 5
        }

    row_check_box = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 5
        }

    cli_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-switch-cli-access"]',
            'wait_for': 5
        }

    cli_close_button = \
        {
            'XPATH': '//span[@data-dojo-attach-point="closeDialogTop"]',
            'wait_for': 5
        }

    cli_apply = \
        {
            'XPATH': '//button[@data-dojo-attach-point="apply"]',
            'wait_for': 5
        }

    device360_select_supplemental_cli = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipMark"]',
            'wait_for': 3
        }

    device360_apply_supplemental_cli_radio_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="supplementalCliOverrideGUIType-keep"]',
            'wait_for': 3
        }

    device360_override_supplemental_cli_radio_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="supplementalCliOverrideGUIType-override"]',
            'wait_for': 3
        }

    device360_supplemental_cli_list = \
        {
            'XPATH': '//*[@class="item-area"]//li',
            'wait_for': 3
        }

    device_360_supplemental_cli_new_profile = \
        {
            'XPATH': "//span[@ah-text-tip='Add']",
            'wait_for': 3
        }

    device_360_supplemental_cli_profile_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="name"]',
            'wait_for': 3
        }
    device_360_supplemental_cli_profile_commands = \
        {
            'XPATH': '//textarea[@data-dojo-attach-point="cli"]',
            'wait_for': 3
        }

    device360_supplemental_cli_save_profile = \
        {
            'XPATH': '//*[@data-dojo-attach-point="buttonEl"]//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 3
        }

    device360_supplemental_cli_edit_profile = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ipEdit"]',
            'wait_for': 3
        }

    device360_thunderbold_icon = \
        {
            'XPATH': '//div[@data-dojo-attach-point="portCtn"]//div[@data-automation-tag="automation-entity-health-status-power"]',
            'wait_for': 5
        }

    device360_power_details = \
        {
            'XPATH': '//div[@data-dojo-attach-point="contentEl"]',
            'wait_for': 5
        }

    device360_pse_settings_for_device_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="showPSESettingsBtn"]',
            'wait_for': 5
        }

    device360_edit_threshold_poe = \
        {
            'XPATH': '//div[@class="field-container max-power-budget"]//input[@type="text"]',
            'wait_for': 5
        }

    device360_save_threshold_poe_value = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    device360_device_configuration_description = \
        {
            'XPATH': '//*[@data-dojo-attach-point="description"]',
            'wait_for': 5
        }

    device360_device_configuration_mac_address = \
        {
            'XPATH': '//*[@data-dojo-attach-point="macAddress"]',
            'wait_for': 5
        }

    device360_device_configuration_device_model = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceconfiguration"]//input[@data-dojo-attach-point="deviceModel"]',
            'wait_for': 5
        }

    device360_device_configuration_iq_engine = \
        {
            'XPATH': '//*[@data-dojo-attach-point="softwareVersion"]',
            'wait_for': 5
        }

    device360_device_configuration_override_acsp_network_policy = \
        {
            'XPATH': '//*[@data-dojo-attach-point="overrideAcspLogging"]',
            'wait_for': 5
        }

    device360_device_configuration_production_option = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deploymentState-production"]',
            'wait_for': 5
        }

    device360_device_configuration_pre_provision_option = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deploymentState-preprovisioned"]',
            'wait_for': 5
        }

    device360_device_configuration_device_template = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceTemplateStatic"]',
            'wait_for': 5
        }

    device360_configure_device_network_policy_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="networkPolicyArea"]//div/ul/li',
            'wait_for': 5
        }

    device360_configure_dhcp_ip_address_link = \
        {
            'XPATH': '//li[@data-automation-tag="automation-device-entity-ip-addressing-tab"]',
            'wait_for': 5
        }

    device360_configure_subnetworks_all_cells = \
        {
            'XPATH': '//div[@data-automation-tag="automation-ipaddressing-area-subnet-list"]//div[@class="dgrid-content ui-widget-content"]//table/tr/td',
            'wait_for': 5
        }

    device360_configure_subnetworks_header = \
        {
            'XPATH': '//div[@data-automation-tag="automation-ipaddressing-area-subnet-list"]//div/table/tr/th',
            'wait_for': 5
        }
    device360_click_particular_client = \
        {
            'XPATH': '//td[contains(@class,"field-clientMac")]//a[contains(@class,"open-client-entity")]',
            'wait_for': 5
        }
    close_client360_dialog = \
        {
            'XPATH': '//div[@class="entity-page-icon entity-page-close"][@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }
    device360_hyperlink_client = \
        {
            'XPATH': '//*[@class="entity-content-ctn device-entity-connected-ctn"]//table[@class="dgrid-row-table"]//*[@data-mac]',
            'wait_for': 5
        }
    device360_column_picker_scroll_bar = \
        {
            'XPATH': '//*[@class="dgrid-hider-menu"]',
            'wait_for': 5
        }

    device360_column_picker_icon = \
        {
            'XPATH': '//*[@class="ui-icon dgrid-hider-toggle"]',
            'wait_for': 5
        }

    d360_create_port_type = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-add',
            'wait_for': 5
        }

    policy_edit_port_type = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-edit',
            'wait_for': 5
        }

    close_port_type_box = \
        {
            'XPATH': '//button[@data-automation-tag="port-type-editor-save"]',
            'wait_for': 5
        }

    close_port_type_dialog_box = \
        {
            'XPATH': '//div[@id="dijit_Dialog_1"]//span[@data-automation-tag="automation-dialog-close-button"]'
        }

    cancel_port_type_box = \
        {
            'XPATH': '//button[@data-automation-tag="port-type-editor-cancel"]',
            'wait_for': 5
        }

    # tab
    select_element_port_type_tab_usage = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-info"]',
            'wait_for': 5
        }

    select_element_port_type_tab_vlan = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-vlan"]',
            'wait_for': 5
        }

    select_element_port_type_tab_transmission = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-trans"]',
            'wait_for': 5
        }

    select_element_port_type_tab_stp = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-stp"]',
            'wait_for': 5
        }

    select_element_port_type_tab_storm_control = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-storm-control"]',
            'wait_for': 5
        }

    select_element_port_type_tab_pse_settings = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-pse"]',
            'wait_for': 5
        }

    select_element_port_type_tab_summary = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-summary"]',
            'wait_for': 5
        }

    select_element_port_type_tab_maclocking = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-mac-locking"]',
            'wait_for': 5
        }

    select_element_port_type_tab_elrp = \
        {
            'XPATH': '//div[@data-automation-tag="port-type-editor-step-elrp"]',
            'wait_for': 5
        }

    # page Name
    select_element_port_type_name = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-name"]',
            'wait_for': 5
        }

    select_element_port_type_description = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-description"]',
            'wait_for': 5
        }

    select_element_port_type_status = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-status"]',
            'wait_for': 5
        }

    select_element_port_type_auto_sense = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-auto-sense-status"]',
            'wait_for': 5
        }

    select_element_port_type_port_usage_access = \
        {
            'XPATH': '//input[@data-dojo-attach-point="accessType"]',
            'wait_for': 5
        }

    select_element_port_type_port_usage_trunk = \
        {
            'XPATH': '//input[@data-dojo-attach-point="trunkType"]',
            'wait_for': 5
        }

    # page Vlan
    select_element_port_type_next_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="wizardNext"]',
            'wait_for': 5
        }

    select_element_port_type_vlan_name_vlan = \
        {
            'XPATH': '//input[@data-dojo-attach-point="nameEl"]',
            'wait_for': 5
        }

    select_element_port_type_vlan_add_vlan = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanArea"]//span[@data-dojo-attach-point="ipSave"]',
            'wait_for': 5
        }

    select_element_port_type_vlan_id_vlan = \
        {
            'XPATH': '//input[@data-dojo-attach-point="defaultVlanId"]',
            'wait_for': 5
        }

    select_element_port_type_vlan_select_button = \
        {
            'XPATH': '//span[@data-automation-tag="automation-port-type-editor-vlan-select-btn"]',
            'wait_for': 5
        }

    select_element_port_type_vlan_dropdown_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipList"]//ul/li',
            'wait_for': 5
        }

    select_element_port_type_native_vlan_name_vlan = \
        {
            'XPATH': '//input[@data-dojo-attach-point="nameEl"]',
            'wait_for': 5
        }

    select_element_port_type_native_vlan_add_vlan = \
        {
            'XPATH': '//div[@data-dojo-attach-point="nativeVlanArea"]//span[@data-dojo-attach-point="ipSave"]',
            'wait_for': 5
        }

    select_element_port_type_native_vlan_id_vlan = \
        {
            'XPATH': '//input[@data-dojo-attach-point="defaultVlanId"]',
            'wait_for': 5
        }

    select_element_port_type_native_vlan_select_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="nativeVlanArea"]//span[@data-dojo-attach-point="ipMark"]',
            'wait_for': 5
        }

    select_element_port_type_native_vlan_dropdown_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipList"]//ul//li',
            'wait_for': 5
        }

    select_element_port_type_save_vlan = \
        {
            'XPATH': '//button[@data-automation-tag="vlan-form-save-button"]',
            'wait_for': 5
        }

    select_element_port_type_allowed_vlans = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-allowed-vlans"]',
            'wait_for': 5
        }

    # Page Transmission
    select_element_port_type_transmission_type = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-type-editor-duplex-chzn-container-ctn"]',
            'wait_for': 5
        }

    select_element_port_type_transmission_type_dropdown_items = \
        {
            'XPATH': '//ul[@data-automation-tag="automation-port-type-editor-duplex-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    select_element_port_type_transmission_speed = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-type-editor-speed-chzn-container-ctn"]',
            'wait_for': 5
        }

    select_element_port_type_transmission_speed_dropdown_items = \
        {
            'XPATH': '//ul[@data-automation-tag="automation-port-type-editor-speed-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    select_element_port_type_cdp_receive = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-cdp"]',
            'wait_for': 5
        }

    select_element_port_type_lldp_transmit = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-lldp-tx"]',
            'wait_for': 5
        }

    select_element_port_type_lldp_receive = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-lldp-rx"]',
            'wait_for': 5
        }

    # page STP
    select_element_port_type_stp_enable = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-stp-enable"]',
            'wait_for': 5
        }
    select_element_port_type_edge_port = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-stp-edge-port"]',
            'wait_for': 5
        }
    select_element_port_type_bpdu_protection = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-type-editor-stp-bpdu-prot-chzn-container-ctn"]',
            'wait_for': 5
        }

    select_element_port_type_bpdu_protection_items = \
        {
            'XPATH': '//ul[@data-automation-tag="automation-port-type-editor-stp-bpdu-prot-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    select_element_port_type_priority = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-type-editor-stp-priority-chzn-container-ctn"]',
            'wait_for': 5
        }

    select_element_port_type_priority_items = \
        {
            'XPATH': '//ul[@data-automation-tag="automation-port-type-editor-stp-priority-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    select_element_port_type_path_cost = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-stp-path-cost"]',
            'wait_for': 5
        }

    # page Storm
    select_element_port_type_broadcast = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-sc-broadcast"]',
            'wait_for': 5
        }
    select_element_port_type_unknown_unicast = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-sc-unicast"]',
            'wait_for': 5
        }
    select_element_port_type_multicast = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-sc-multicast"]',
            'wait_for': 5
        }
    select_element_port_type_rate_limit_value = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-sc-rate-limit-value"]',
            'wait_for': 5
        }
    # page ELRP (ONLY FOR EXOS)
    select_element_port_type_elrp_status = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-elrp-enable"]',
            'wait_for': 5
        }

    # page PSE
    select_element_port_type_pse_profile = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-type-editor-pse-profile"]//span[@data-dojo-attach-point="ipMark"]',
            'wait_for': 5
        }
    select_element_port_type_pse_profile_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ipList"]//ul//li',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_add = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-type-editor-pse-profile"]//span[@data-dojo-attach-point="ipSave"]',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_name = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanObjForm"]//input[@data-dojo-attach-point="nameEl"]',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_power_mode_items = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-powermode"]//li',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_power_limit = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanObjForm"]//input[@data-dojo-attach-point="powerLimit"]',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_priority = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanObjForm"]//div[contains(@class,"priority")]//div[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_priority_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanObjForm"]//div[contains(@class,"priority")]//ul[@data-automation-tag="automation-chzn-results-ctn"]//li',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_power_mode_dropdown = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanObjForm"]//div[@class="line clearfix"]//div[@data-automation-tag="automation-chzn-arrow-down"]',
            'index': 0
        }

    select_element_port_type_pse_profile_description = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanObjForm"]//input[@data-dojo-attach-point="description"]',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_save = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_close = \
        {
            'XPATH': '//button[@data-dojo-attach-point="cancelBtn"]',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_save_error = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanObjForm"]//*[@data-dojo-attach-point="textEl"]',
            'wait_for': 5
        }

    select_element_port_type_poe_status = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-pse-enable"]',
            'wait_for': 5
        }

    select_element_port_type_pse_edit = \
        {
            'XPATH': '//span[@data-automation-tag="automation-port-type-editor-pse-profile-edit-btn"]',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_error_text = \
        {
            'XPATH': '//div[@data-dojo-attach-point="powerLimitContainer"]//span',
            'wait_for': 5
        }

    # Page summary
    select_element_port_type_name_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-name"]',
            'wait_for': 5
        }

    select_element_port_type_description_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-desc"]',
            'wait_for': 5
        }

    select_element_port_type_status_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-status"]',
            'wait_for': 5
        }

    select_element_port_type_port_usage_access_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-usage"]',
            'wait_for': 5
        }

    select_element_port_type_vlan_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-vlan"]',
            'wait_for': 5
        }

    select_element_port_type_native_vlan_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-native-vlan"]',
            'wait_for': 5
        }

    select_element_port_type_allowed_vlans_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-allowed-vlans"]',
            'wait_for': 5
        }

    select_element_port_type_transmission_type_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-duplex"]',
            'wait_for': 5
        }

    select_element_port_type_transmission_speed_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-speed"]',
            'wait_for': 5
        }

    select_element_port_type_cdp_receive_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-cdp"]',
            'wait_for': 5
        }

    select_element_port_type_lldp_transmit_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-lldp-tx"]',
            'wait_for': 5
        }

    select_element_port_type_lldp_receive_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-lldp-rx"]',
            'wait_for': 5
        }

    select_element_port_type_stp_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-stp-status"]',
            'wait_for': 5
        }

    select_element_port_type_edge_port_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-stp-edge-port"]',
            'wait_for': 5
        }

    select_element_port_type_bpdu_protection_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-stp-bpdu-prot"]',
            'wait_for': 5
        }

    select_element_port_type_priority_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-stp-priority"]',
            'wait_for': 5
        }

    select_element_port_type_path_cost_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-stp-path-cost"]',
            'wait_for': 5
        }

    select_element_port_type_broadcast_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-sc-broadcast"]',
            'wait_for': 5
        }

    select_element_port_type_unknown_unicast_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-sc-unicast"]',
            'wait_for': 5
        }

    select_element_port_type_multicast_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-sc-multicast"]',
            'wait_for': 5
        }

    select_element_port_type_rate_limit_type_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-sc-rate-limit-type"]',
            'wait_for': 5
        }

    select_element_port_type_rate_limit_value_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-sc-rate-limit-value"]',
            'wait_for': 5
        }

    select_element_port_type_elrp_status_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-elrp-enabled"]',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-pse-profile"]',
            'wait_for': 5
        }

    select_element_port_type_poe_status_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-pse-status"]',
            'wait_for': 5
        }

    device_d360_save_port_configuration = \
        {
            'XPATH': '//button[@data-automation-tag="automation-port-configuration-save-button"] | //button[@data-automation-tag="automation-port-config-save"]',
            'wait_for': 5
        }

    device_d360_cancel_port_configuration = \
        {
            'XPATH': '//*[@data-automation-tag="automation-port-configuration-cancel-button"]',
            'wait_for': 5
        }

    device360_configure_port_usage_drop_down_options_presence = \
        {
            'CSS_SELECTOR': '.chzn-single-with-drop',
            'wait_for': 5
        }

    device360_port_configuration_stack_units_dropdown = \
        {
            'XPATH': '//div[@class="port-configuration-view"]'
                     '//div[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 5
        }

    device360_port_configuration_stack_units_rows = \
        {
            "XPATH": '//div[@data-dojo-attach-point="stackMemberChooserArea"]//li[contains(text(),"Unit")]',
            'wait_for': 5
        }

    policy_configure_port_rows = \
        {
            'XPATH': '//tabset[@data-dojo-attach-point="configuration-ports-tabs"]//portdetails//portentry-row',
            'wait_for': 5
        }

    device360_port_config_pse_tab_slot_stack = \
        {
            'XPATH': '//*[@data-automation-tag="automation-port-config-pse"]',
            'wait_for': 5
        }

    device360_pse_settings_for_device_button_stack = \
        {
            'XPATH': '//button[@data-dojo-attach-point="showPSESettingsBtn"]',
            'wait_for': 5
        }

    device360_edit_threshold_poe_stack = \
        {
            'XPATH': '//div[@class="field-container max-power-budget"]//input[@type="text"]',
            'wait_for': 5
        }

    device360_save_threshold_poe_value_stack = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    device360_configure_port_save_button_stack = \
        {
            'XPATH': '//button[@data-automation-tag="automation-port-config-save"]',
            'wait_for': 5
        }

    device360_stack_overview_slot_details_rows = \
        {
            'XPATH': '//*[@data-dojo-attach-point="switchStackPortsPanelContainer"]',
            'wait_for': 5
        }

    device360_thunderbold_icon_stack = \
        {
            'CSS_SELECTOR': '.power-supply',
            'wait_for': 5
        }

    device360_configure_aggregated_port_settings_aggregation_rows = \
        {
            'XPATH': '//aggregate-ports/div[@class="port-settings-entry "]',
            'wait_for': 5
        }

    device360_port_settings_click_checkbox = \
        {
            'XPATH': '//input[contains(@data-automation-tag,"automation-port-settings-port-check") and @value=${port}]',
            'wait_for': 5
        }

    device360_aggregate_selected_ports_button = \
        {
            'XPATH': '//div[@class="multi-edit-controls"]/button[@data-automation-tag="port-settings-aggregate"]',
            'wait_for': 5
        }

    device360_lacp_toggle = \
        {
            'XPATH': '//span[@data-automation-tag="automation-lag-lacp-toggle"]//input[@data-dojo-attach-point="inputNode"]',
            'wait_for': 5
        }

    device360_lag_cancel_button = \
        {
            'XPATH': '//div[@class="view-btn-area"]/span[@data-automation-tag="automation-lag-cancel-button"]',
            'wait_for': 5
        }

    device360_lag_save_button = \
        {
            'XPATH': '//div[@class="view-btn-area"]/span[@data-automation-tag="automation-lag-save-button"]',
            'wait_for': 5
        }

    device360_save_port_config = \
        {
            'XPATH': '//div[@class="btn-area"]/button[@data-automation-tag="automation-port-config-save"]',
            'wait_for': 5
        }

    device360_lacp_label = \
        {
            'XPATH': '//div[@class ="port-settings-entry link-type-agg link-type-agg-prime state-expanded" and @data-agg-master-id="${port}"]/div[@class ="port-entry"]//label[@class ="control-label"]',
            'wait_for': 5
        }

    device360_port_from_aggregation_list = \
        {
            'XPATH': '//*[@data-automation-tag="lag-selected-port-${port}"]',
            'wait_for': 5
        }

    device360_aggregate_remove_button = \
        {
            'XPATH': '//div/button[@data-dojo-attach-point="removeButton"]',
            'wait_for': 5
        }

    device360_aggregate_add_button = \
        {
            'XPATH': '//div/button[@data-dojo-attach-point="addButton"]',
            'wait_for': 5
        }

    device360_perform_update_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-config-download-options-update-btn"]',
            'wait_for': 5
        }

    device360_port_config_stack_slots_dropdown = \
        {
            'XPATH': '//div[@class="stack-member-chooser"][@data-dojo-attach-point="stackMemberChooserArea"]//div[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 5
        }

    device360_slot_from_dropdown = \
        {
            'XPATH': '//div[@data-automation-tag="automation-chzn-drop-ctn"]//li[starts-with(@data-automation-tag, "Unit_${unit}_-")]',
            'wait_for': 5
        }

    device360_aggregate_choose_slot = \
        {
            'XPATH': '//select[@data-dojo-attach-point="slotsAvailable"]/option[@data-automation-tag="lag-available-slot-${unit}"]',
            'wait_for': 5
        }

    device360_aggregate_available_port = \
        {
            'XPATH': '//select[@data-dojo-attach-point="portsAvailable"]/option[@data-automation-tag="lag-available-port-${port}"]',
            'wait_for': 5
        }
    device360_aggregate_selected_port = \
        {
            'XPATH': '//select[@data-dojo-attach-point="portsInAgg"]/option[@data-automation-tag="lag-selected-port-${port}"]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_stack_drop_down = \
        {
            'XPATH': '//div[@class="stack-member-chooser fn-right"]//div[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_health_item_ip_address_stack_active_unit = \
        {
            'XPATH': '//div[@data-automation-tag="automation-entity-health-status-ipAddr"]//span[contains(text(), "${ip_address}")]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_health_item_mac_address_stack_active_unit = \
        {
            'XPATH': '//div[@data-automation-tag="automation-entity-health-status-macAddr"]//span[contains(text(),"${mac_address}")]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_health_item_soft_version_stack_active_unit = \
        {
            'XPATH': '//div[@data-automation-tag="automation-entity-health-status-version"]//span[contains(text(),"${soft_version}")]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_health_item_model_stack_active_unit = \
        {
            'XPATH': '//div[@data-automation-tag="automation-entity-health-status-type"]//span[contains(text(),"${model}")]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_health_item_serial_number_stack_active_unit = \
        {
            'XPATH': '//div[@data-automation-tag="automation-entity-health-status-tag"]//span[contains(text(),"${serial_number}")]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_health_item_make_stack_active_unit = \
        {
            'XPATH': '//div[@data-automation-tag="automation-entity-health-status-make"]//span[contains(text(),"${make}")]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_health_item_iqagent_version_stack_active_unit = \
        {
            'XPATH': '//div[@data-automation-tag="automation-entity-health-status-agent"]//span[contains(text(),"${iqagent_version}")]',
            'wait_for': 5
        }

    device360_monitor_diagnostics_stack_drop_down_unit = \
        {
            'XPATH': '//div[@data-automation-tag="diagnostics-stack-member-chooser-area-with-container"]//a',
            'wait_for': 5
        }

    device360_monitor_diagnostics_stack_drop_down_unit_options = \
        {
            'XPATH': '//li[@data-automation-tag="Unit_${unit}_-_${unit_role}"]',
            'wait_for': 5
        }

    select_element_port_type_macLock_status = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableMacLocking"]',
            'wait_for': 5

        }

    select_element_port_type_macLock_max_first_arrival = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-ml-maxfa"]',
            'wait_for': 5
        }

    select_element_port_type_macLock_disable_port = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-ml-shutdown"]',
            'wait_for': 5
        }

    select_element_port_type_macLock_link_down_clear = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-ml-clear"]',
            'wait_for': 5
        }

    select_element_port_type_macLock_link_down_retain = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-ml-retain"]',
            'wait_for': 5
        }

    select_element_port_type_macLock_remove_aged_MACs = \
        {
            'XPATH': '//input[@data-automation-tag="port-type-editor-ml-remove-aged"]',
            'wait_for': 5
        }

    select_mac_locking_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-ml-enable"]'
        }

    select_mac_locking_first_arrival_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-ml-max-fa-limit"]'
        }

    select_mac_locking_port_disable_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-ml-disable-port"]'
        }

    select_mac_locking_link_down_action_clear_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-ml-link-down-action"][@title="Clear"]'
        }

    select_mac_locking_link_down_action_retain_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-ml-link-down-action"][@title="Retain"]'
        }

    select_mac_locking_remove_aged_macs_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-ml-remove-aged-macs"]'
        }

    device360_cpu_utilized_button = \
        {
            'XPATH': '//*[@class="timeline-legend-label" and text()="CPU UTILIZED"]',
            'wait_for': 5
        }

    device360_memory_utilized_button = \
        {
            'XPATH': '//*[@class="timeline-legend-label" and text()="MEMORY UTILIZED"]',
            'wait_for': 5
        }

    device360_rx_counter_button = \
        {
            'XPATH': '//*[@class="timeline-legend-label" and text()="RX COUNTER"]',
            'wait_for': 5
        }

    device360_tx_counter_button = \
        {
            'XPATH': '//*[@class="timeline-legend-label" and text()="TX COUNTER"]',
            'wait_for': 5
        }

    device360_ports_list_graph = \
        {
            'XPATH': '//li[contains(@class, "port-rel")]//div[contains(@data-automation-tag, "automation-port") and not(contains(@class, "active"))]',
            'wait_for': 5
        }

    device360_columns_toggle_button = \
        {
            'XPATH': '//div[@aria-label="Show or hide columns" and @type="button"]',
            'wait_for': 5
        }

    device360_coluns_toggle_checkboxes = \
        {
            'XPATH': '//input[contains(@id, "hcgrid_") and @type="checkbox"]',
            'wait_for': 5
        }

    device360_ports_description_table_header = \
        {
            'XPATH': "//div[@data-automation-tag='automation-port-list-grid']//div[@role='row' and contains(@class, 'dgrid-header')]",
            'wait_for': 5
        }

    device360_ports_table_pagination_sizes = \
        {
            "XPATH": "//span[contains(@class, 'pagination-size')]",
            'wait_for': 5
        }

    device360_ports_table_current_pagination_size = \
        {
            "XPATH": "//span[@class='pagination-size current-pagination']",
            'wait_for': 5
        }

    device360_ports_table_th_columns = \
        {
            "XPATH": ".//th[@role='columnheader']",
            'wait_for': 5
        }
    device360_ports_table_td_gridcell = \
        {
            "XPATH": ".//tr//td[@role='gridcell']",
            'wait_for': 5
        }

    device360_ah_icons = \
        {
            "XPATH": '//li/div[contains(@class,"AH-ports-icons")][@data-index="${index}"]',
            'wait_for': 5
        }

    device360_ports_table_scroll = \
        {
            "XPATH": "//div[@data-automation-tag='automation-port-list-grid']//div[@class='dgrid-scroller']",
            'wait_for': 5
        }

    device360_ports_table_current_pagin_number = \
        {
            "XPATH": "//div[@class='pagination-num-ctn']//span[@class='pagination-page current-pagination']",
            'wait_for': 5
        }

    device360_connected_clients_count = \
        {
            'XPATH': '//*[@data-dojo-attach-point="connectedTotal"]',
            'wait_for': 5
        }

    device360_leftpane_unique_clients = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientsNum"]',
            'wait_for': 15
        }

    device360_wireless_interface_tab = \
        {
            'XPATH': '//*[@data-automation-tag="device-entity-nav-menu-wireless-interfaces"]',
            'wait_for': 15
        }

    device360_total_wireless_clients = \
        {
            'XPATH': '//*[@data-automation-tag="wirelessinterfaces-total-client-count-ctn"]//div[@data-dojo-attach-point="totalClientCount"]',
            'wait_for': 15
        }

    device360_total_clients_clientspage = \
        {
            'XPATH': '//*[@data-automation-tag="connectedclients-client-counts"]//div[@data-dojo-attach-point="totalClientCount"]',
            'wait_for': 15
        }

    device360_wireless_wifi6gscore = \
        {
            'XPATH': '//div[@class="health-column"]//span[@data-dojo-attach-point="overallScoreValue"]',
            'wait_for': 15
        }

    device360_wireless_combinedscore = \
        {
            'XPATH': '//div[@class="health-column"]//span[@data-dojo-attach-point="overallScoreValue"]',
            'wait_for': 15
        }

    device360_wireless_wifi2widgetclient = \
        {
            'XPATH': '//*[@class="wireless-data-value"]//*[@data-dojo-attach-point="clients_3"]',
            'wait_for': 15
        }

    device360_wireless_combinedscoretab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="widgetCtn"]//*[@for="radio-healthCardOptions-4"]',
            'wait_for': 15
        }

    device360_wireless_wifi6gscoretab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="widgetCtn"]//*[@for="radio-healthCardOptions-3"]',
            'wait_for': 15
        }

    device360_wireless_wifi5gscoretab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="widgetCtn"]//*[@for="radio-healthCardOptions-2"]',
            'wait_for': 15
        }

    device360_wireless_wifi2gscoretab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="widgetCtn"]//*[@for="radio-healthCardOptions-1"]',
            'wait_for': 15
        }

    cancel_button_port_type = \
        {
            'XPATH': '//button[@data-automation-tag="port-type-editor-cancel"]',
            'wait_for': 5
        }

    device360_event = \
        {
            'XPATH': '//*[@data-automation-tag="device-entity-nav-menu-events"]',
            'wait_for': 5
        }

    device360_digital_twin_status_icon = \
        {
            'DESC': 'D360 > Digital Twin Status Icon',
            'XPATH': '//span[@data-dojo-attach-point="digitalTwinIcon"]'
        }

    device360_digital_twin_relaunch_button = \
        {
            'DESC': 'D360 > Relaunch Digital Twin button',
            'XPATH': '//button[@data-automation-tag="automation-switch-config-relaunch-dt-btn"]'
        }

    device360_digital_twin_shutdown_button = \
        {
            'DESC': 'D360 > Shutdown Digital Twin button',
            'XPATH': '//button[@data-automation-tag="automation-switch-config-shutdown-dt-btn"]'
        }

    device_ssh_ui_tip_close = \
        {
            'XPATH': '//div[contains(@widgetid,"MessageBase_1")]//div/i[@data-dojo-attach-point="xEl"]'
        }

    device_ssh_ui_tip_error = \
        {
            'XPATH': '//div[@class="ui-tipbox ui-tipbox-error"]//div[@class="ui-tipbox-icon"]'
        }

    device360_port_configuration_path_cost_stp = \
        {
            'XPATH': './/input[contains(@data-automation-tag, "automation-port-stp-port-path-cost")]',
            'wait_for': 5
        }

    device360_overview_select_port = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-$index"]'
        }

    device360_overview_port_info_bounce_port = \
        {
            'XPATH': '//div[@class="port-action action-bounce-port "]'
        }

    device360_overview_port_info_bounce_poe = \
        {
            'XPATH': '//div[@class="port-action action-bounce-poe "]'
        }

    device360_ports_table_rows = \
        {
            "XPATH": "//div[@data-automation-tag='automation-port-list-grid']//div[@role='row' and contains(@class, 'dgrid-row')]",
            'wait_for': 5
        }

    d360_pagination_current_page = \
        {
            'XPATH': '//span[@class="pagination-page current-pagination"]',
            'wait_for': 3
        }

    d360_configure_port_mac_locking_tab_button = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-config-mac-locking"]',
            'wait_for': 5
        }

    d360_monitor_mac_locking_checkbox_interface = \
        {
            'XPATH': "//div[@class='port-mac-locking']//label/input[@type='checkbox'][@value='${port_number}']",
            'wait_for': 5
        }

    d360_monitor_mac_locking_on_off = \
        {
            'XPATH': '//div[@data-entry-index="${port_number}"]//input[@data-automation-tag="port-maclock-status"]',
            'wait_for': 5
        }

    d360_monitor_mac_locking_max_first_arrival_limit = \
        {
            'XPATH': '//div[@data-entry-index="${port_number}"]//input[@data-automation-tag="port-maclock-first-arrival-limit"]',
            'wait_for': 5
        }

    d360_monitor_mac_locking_disable_port = \
        {
            'XPATH': '//div[@data-entry-index="${port_number}"]//input[@data-automation-tag="port-maclock-disable-port"]',
            'wait_for': 5
        }

    d360_monitor_mac_locking_remove_aged_macs = \
        {
            'XPATH': '//div[@data-entry-index="${port_number}"]//input[@data-automation-tag="port-maclock-remove-aged-macs"]',
            'wait_for': 5
        }

    d360_save_port_configuration = \
        {
            'XPATH': '//button[@data-automation-tag="automation-port-config-save"]',
            'wait_for': 5
        }

    d360_cancel_port_configuration_stack = \
        {
            'XPATH': '//div[@class="btn-area"]//button[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5
        }

    d360_monitor_mac_locking_interface_edit_button = \
        {
            'XPATH': '//div[@class="mac-locking-global-controls"]//button[@class="btn btn-primary multi-edit-btn"]',
            'wait_for': 5
        }

    d360_monitor_mac_locking_multi_edit_max_first_arrival_limit_checkbox = \
        {
            'XPATH': '//input[@data-automation-tag="medit-maclock-max-fa-cb"]',
            'wait_for': 5
        }

    d360_monitor_mac_locking_input_max_first_arrival_limit_value = \
        {
            'XPATH': '//div[@class="field port-max-learn-limit"]//input[@data-automation-tag="medit-maclock-max-fa"]',
            'wait_for': 5
        }

    d360_monitor_mac_locking_multi_edit_save_button = \
        {
            'XPATH': '//button[@data-automation-tag="medit-maclock-save"]',
            'wait_for': 5
        }

    d360_monitor_mac_locking_multi_edit_warning_max_limit_arrival = \
        {
            'XPATH': '//div[@role="dialog"]//div[@data-dojo-attach-point="containerNode"]//div[@class="ui-tipbox ui-tipbox-error"]',
            'wait_for': 5
        }

    d360_monitor_mac_locking_multi_edit_close_button = \
        {
            'XPATH': '//div[@id="dijit_Dialog_0"]//span[@data-automation-tag="automation-dialog-close-button"]',
            'wait_for': 5
        }

    d360_monitor_mac_locking_header = \
        {
            'XPATH': '//th[contains(@class, "field-macLock")]',
            'wait_for': 5
        }

    device360_event_expand_more = \
        {
            "XPATH": 'table[@class="dgrid-row-table"]/tr/td[contains(@class, "field-description")]//span[@class = "more"]',
            'wait_for': 5
        }

    device360_event_more_expand_value = \
        {
            'XPATH': '//div[@data-dojo-attach-point="msgContainer"]/p[@data-dojo-attach-point="desEl"]',
            'wait_for': 5
        }

    device360_event_more_close_btn = \
        {
            'XPATH': '//button[@data-automation-tag="automation-notification-no-btn"]',
            'wait_for': 5
        }

    select_element_port_type_pse_profile_power_limit = \
        {
              'XPATH': '//div[@data-dojo-attach-point="vlanObjForm"]//input[@data-dojo-attach-point="powerLimit"]',
              'wait_for': 5
        }

    select_element_port_type_pse_profile_power_mode_dropdown = \
        {
            'XPATH': '//div[@class="column last"]//a[@class="chzn-single"]',
            'index': 0
        }

    select_element_port_type_pse_edit = \
        {
            'XPATH': '//span[@data-automation-tag="automation-port-type-editor-pse-profile-edit-btn"]'
        }

    select_more_button_pse_profile = \
        {
            'XPATH': '//div[@class="J-ip-more"]'
        }

    device360_configure_port_access_vlan_textfield_VOSS = \
        {
            'CSS_SELECTOR': '.accessVLAN',
            'index': 1,
            'wait_for': 5
        }

    device360_configure_port_trunk_native_vlan_textfield_VOSS = \
        {
            'CSS_SELECTOR': '.trunkNativeVLAN',
            'index': 2,
            'wait_for': 5
        }

    device360_configure_port_trunk_vlan_textfield_VOSS = \
        {
            'CSS_SELECTOR': '.trunkAllowedVLAN',
            'index': 2,
            'wait_for': 5
        }

    select_element_port_type_port_usage_phone = \
        {
            'XPATH': '//input[@data-dojo-attach-point="phoneType"]',
            'wait_for': 5
        }
    select_element_port_type_voice_lldp_advertisment_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-lldp-advertisements"]',
            'wait_for': 5
        }

    select_802_1_vlan_and_port_protocol_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-lldp-advert-vlan"]',
            'wait_for': 5
        }

    select_med_voice_vlan_dscp_value_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-advert-med-vlan"]',
            'wait_for': 5
        }

    select_med_voice_signaling_dscp_value_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-advert-med-sig-vlan"]',
            'wait_for': 5
        }

    select_cdp_advertisment_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-cdp-advertisements"]',
            'wait_for': 5
        }

    select_cdp_voice_vlan_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-cdp-advert-vlan"]',
            'wait_for': 5
        }

    select_cdp_power_available_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-cdp-advert-power"]',
            'wait_for': 5
        }

    select_voice_vlan_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-voice-vlan"]'
        }

    select_data_vlan_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-data-vlan"]'
        }
    select_element_port_type_voice_vlan_add_vlan = \
        {
            'XPATH': '//span[@data-automation-tag="automation-port-type-editor-voice-vlan-add-btn"]',
            'wait_for': 5
        }

    select_element_port_type_voice_vlan_select_button = \
        {
            'XPATH': '//span[@data-automation-tag="automation-port-type-editor-voice-vlan-select-btn"]',
            'wait_for': 5
        }

    select_element_port_type_data_vlan_add_vlan = \
        {
            'XPATH': '//span[@data-automation-tag="automation-port-type-editor-data-vlan-add-btn"]',
            'wait_for': 5
        }

    select_element_port_type_data_vlan_select_button = \
        {
            'XPATH': '//span[@data-automation-tag="automation-port-type-editor-data-vlan-select-btn"]',
            'wait_for': 5
        }

    select_element_lldp_voice_vlan_options = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableLldpAdvertToggle"]',
            'wait_for': 5
        }

    select_element_enable_advertisment_of_dot1_vlan = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableAdvertDot1Vlan"]',
            'wait_for': 5
        }

    select_element_enable_advertisment_of_med_voice_vlan = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableAdvertMedVoiceVlan"]',
            'wait_for': 5
        }

    select_element_enable_advertisment_of_med_voice_signaling_vlan = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableAdvertMedSigVoiceVlan"]',
            'wait_for': 5
        }

    select_element_med_voice_vlan_dscp = \
        {
            'XPATH': '//input[@data-dojo-attach-point="medVoiceVlanDscp"]',
            'wait_for': 5
        }

    select_element_med_sig_voice_vlan_dscp = \
        {
            'XPATH': '//input[@data-dojo-attach-point="medSigVoiceVlanDscp"]',
            'wait_for': 5
        }

    select_element_cdp_voice_vlan_options = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableCdpAdvertToggle"]',
            'wait_for': 5
        }

    select_element_enable_advertisment_of_voice_vlan = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableAdvertVoiceVlan"]',
            'wait_for': 5
        }

    select_element_enable_advertisment_of_power_available = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableAdvertPowerAvailable"]',
            'wait_for': 5
        }

    select_element_data_vlan_input = \
        {
            'XPATH': "//input[@data-automation-tag='automation-port-type-editor-data-vlan-input']",
            'wait_for': 5
        }

    select_element_voice_vlan_input = \
        {
            'XPATH': "//input[@data-automation-tag='automation-port-type-editor-voice-vlan-input']",
            'wait_for': 5
        }

    select_element_dscp_values_validation_span = \
        {
            'XPATH': '//span[@data-tooltip="${validation_message}"]',
            'wait_for': 5
        }

    select_form_errors_elements = \
        {
            'XPATH': '//p[@class="form-error"]',
            'wait_for': 5
        }

    cancel_port_type_editor = \
        {
            'XPATH': '//button[@data-automation-tag="port-type-editor-cancel"]',
            'wait_for': 5
        }
    select_cdp_advertisment_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-cdp-advertisements"]',
            'wait_for': 5
        }

    select_cdp_voice_vlan_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-cdp-advert-vlan"]',
            'wait_for': 5
        }

    select_cdp_power_available_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-cdp-advert-power"]',
            'wait_for': 5
        }

    select_voice_vlan_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-voice-vlan"]'
        }

    select_data_vlan_summary = \
        {
            'XPATH': '//a[@data-automation-tag="port-type-editor-summary-data-vlan"]'
        }
    device360_voip_port_rows = \
        {
            'XPATH': '//div[contains(@class, "port-voice-vlan-entry")]',
            'wait_for': 5
        }
    device360_voip_tab_data = \
        {
            'XPATH': '//div[@class="port-voice-vlan"]',
            'wait_for': 5
        }
    device360_voip_tab = \
        {
            'XPATH':'//div[@data-automation-tag="automation-port-config-voice"]',
            'wait_for': 5
        }
    device360_vlan_lldp_capabilities = \
        {
            # 'XPATH': '//input[@data-automation-tag="automation-port-voice-vlan-lldp-capabilities"]',
            'CSS_SELECTOR': '.port-voice-vlan-toggle input[data-repeater-bind-to-field="enableLldpCapabilites"]',
            'wait_for': 5
        }
    device360_802_1_voice_vlan = \
        {
            'CSS_SELECTOR': '.port-voice-vlan-col input[data-repeater-bind-to-field="enableAdvertDot1Vlan"]',
            'wait_for': 5
        }
    d360_port_voice_vlan_med_dscp = \
        {
            'CSS_SELECTOR': '.port-med-voice input[data-repeater-bind-to-field="medVoiceVlanDscp"]',
            'wait_for': 5
        }
    d360_port_voice_vlan_med_sig_dscp = \
        {
            'CSS_SELECTOR': '.port-med-voice input[data-repeater-bind-to-field="medSigVoiceVlanDscp"]',
            'wait_for': 5
        }
    d360_port_voice_vlan_cdp_capabilities = \
        {
            'CSS_SELECTOR': '.port-voice-vlan-toggle input[data-repeater-bind-to-field="enableCdpCapabilities"]',
            'wait_for': 5
        }
    d360_cdp_voice_vlan = \
        {
            'CSS_SELECTOR': '.port-cdp-voicevlan input[data-repeater-bind-to-field="enableAdvertVoiceVlan"]',
            'wait_for': 5
        }
    d360_advert_power_available = \
        {
            'CSS_SELECTOR': '.port-cdp-voicevlan input[data-repeater-bind-to-field="enableAdvertPowerAvailable"]',
            'wait_for': 5
        }
    d360_port_type_dropdown = \
        {
            'CSS_SELECTOR': '.port-type-choose div[class="chzn-container chzn-container-single"]',
            'wait_for': 5
        }
    d360_port_type_options = \
        {
            'CSS_SELECTOR': '.active-result',
            'wait_for': 5
        }

    device360_configure_port_usage_drop_down_options_presence = \
        {
            'CSS_SELECTOR': '.chzn-single-with-drop',
            'wait_for': 5
        }

    device360_port_configuration_stack_units_dropdown = \
        {
            'XPATH': '//div[@class="stack-member-chooser"]//div[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 5
        }

    device360_port_configuration_stack_units_dropdown_parent_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="stackMemberChooserArea"]//ul[@data-automation-tag="automation-chzn-results-ctn"]',
            'index': 0,
            'wait_for': 5
        }

    select_element_dscp_values_validation_span = \
        {
            'XPATH': '//span[@data-tooltip="${validation_message}"]',
            'wait_for': 5
        }

    select_form_errors_elements = \
        {
            'XPATH': '//p[@class="form-error"]',
            'wait_for': 5
        }

    cancel_port_type_editor = \
        {
            'XPATH': '//button[@data-automation-tag="port-type-editor-cancel"]',
            'wait_for': 5
        }

    summary_tab_confirmation = \
        {
            'XPATH':'//*[contains(@class,"summary active")]',
            'wait_for': 5
        }

    vlan_tab_confirmation = \
        {
            'XPATH': '//*[contains(@class,"vlan active")]',
            'wait_for': 5
        }

    transmission_tab_confirmation = \
        {
            'XPATH': '//*[contains(@class,"transmission-settings active")]',
            'wait_for': 5
        }

    device360_port_configuration_pse_profile_add_button = \
        {
            'CSS_SELECTOR': '.ui-ip-save',
            'wait_for': 5
        }

    device360_port_configuration_pse_profile_edit_button = \
        {
            'CSS_SELECTOR': '.ui-ip-edit-active',
            'wait_for': 5
        }

    device360_configure_port_pse_rows = \
        {
            'XPATH': '//div[@class="port-pse-entry " or @class="clearfix entry-in-line"]',
            'wait_for': 5
        }

    device360_port_configuration_pse_profile_port_interface = \
        {
            'CSS_SELECTOR': '.port-interface',
            'wait_for': 5
        }

    device360_port_configuration_pse_profile_port_interface_voss = \
        {
            'CSS_SELECTOR': '.portInterface',
            'wait_for': 5
        }

    common_save_button = \
        {
            'XPATH': '//button[@data-automation-tag="port-type-editor-save"]',
            'wait_for': 5
        }

    common_cancel_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="cancelBtn"]',
            'wait_for': 5
        }

    save_and_close_port_type_box = \
        {
            'XPATH': '//button[@data-automation-tag="port-type-editor-save"]',
        }

    d360_multi_edit_checkbox_status = \
        {
            'XPATH': '//input[@data-automation-tag="automation-port-details-multi-edit-checkbox-status" and @type="checkbox"]',
            'wait_for': 5
        }

    d360_multi_edit_status_toggle = \
        {
            'XPATH': '//input[@data-automation-tag="automation-port-details-multi-edit-status-toggle" and @type="checkbox"]',
            'wait_for': 5
        }

    d360_multi_edit_checkbox_port_type = \
        {
            'XPATH': '//input[@data-automation-tag="automation-port-details-multi-edit-checkbox-port-type" and @type="checkbox"]',
            'wait_for': 5
        }

    d360_multi_edit_port_type_dropdown = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-details-multi-edit-port-type-chzn-arrow-down"]',
            'wait_for': 5
        }

    d360_multi_edit_port_type_drop_down_list = \
        {
            'CSS_SELECTOR': '.active-result',
            'wait_for': 5
        }

    d360_multi_edit_checkbox_vlan = \
        {
            'XPATH': '//input[@data-automation-tag="automation-port-details-multi-edit-checkbox-vlan" and @type="checkbox"]',
            'wait_for': 5
        }

    d360_multi_edit_vlan_input = \
        {
            'XPATH': '//input[@data-automation-tag="automation-port-details-multi-edit-vlan-input"]',
            'wait_for': 5
        }

    d360_multi_edit_checkbox_native_vlan = \
        {
            'XPATH': '//input[@data-automation-tag="automation-port-details-multi-edit-checkbox-native" and @type="checkbox"]',
            'wait_for': 5
        }

    d360_multi_edit_native_vlan_input = \
        {
            'XPATH': '//input[@data-dojo-attach-point="nativeVlanField"]',
            'wait_for': 5
        }

    d360_multi_edit_checkbox_allowed_vlan = \
        {
            'XPATH': '//input[@data-automation-tag="automation-port-details-multi-edit-checkbox-allowed" and @type="checkbox"]',
            'wait_for': 5
        }

    d360_multi_edit_allowed_vlan_input = \
        {
            'XPATH': '//input[@data-dojo-attach-point="allowedVlanField"]',
            'wait_for': 5
        }

    d360_multi_edit_checkbox_voice_vlan = \
        {
            'XPATH': '//input[@data-automation-tag="automation-port-details-multi-edit-checkbox-voice-vlan" and @type="checkbox"]',
            'wait_for': 5
        }

    d360_multi_edit_voice_vlan_input = \
        {
            'XPATH': '//input[@data-automation-tag="automation-port-details-multi-edit-voice-vlan-input"]',
            'wait_for': 5
        }

    d360_multi_edit_checkbox_data_vlan = \
        {
            'XPATH': '//input[@data-automation-tag="automation-port-details-multi-edit-checkbox-data-vlan" and @type="checkbox"]',
            'wait_for': 5
        }

    d360_multi_edit_data_vlan_input = \
        {
            'XPATH': '//input[@data-automation-tag="automation-port-details-multi-edit-data-vlan-input"]',
            'wait_for': 5
        }

    d360_multi_edit_checkbox_port_description = \
        {
            'XPATH': '//input[@data-automation-tag="automation-port-details-multi-edit-checkbox-description" and @type="checkbox"]',
            'wait_for': 5
        }

    d360_multi_edit_port_description_input = \
        {
            'XPATH': '//input[@data-automation-tag="automation-port-details-multi-edit-description-input"]',
            'wait_for': 5
        }

    d360_close_multi_edit = \
        {
            'XPATH': '//button[@data-automation-tag="automation-port-details-multi-edit-close-btn"]',
            'wait_for': 5
        }

    d360_save_multi_edit = \
        {
            'XPATH': '//button[@data-automation-tag="automation-port-details-multi-edit-save-btn"]',
            'wait_for': 5
        }

    d360_monitor_port_details_checkbox_interface = \
        {
            'XPATH': '//input[@type="checkbox"][@data-automation-tag="automation-port-details-port-check-${port_number}"]',
            'wait_for': 5
        }

    d360_monitor_port_details_edit = \
        {
            'XPATH': '//button[@data-automation-tag="automation-port-details-edit"]',
            'wait_for': 5
        }

    vlan_error_message_close_multi_edit = \
        {
            'XPATH': '//div[@class="ui-tipbox ui-tipbox-error"]//i[@class="ui-tipbox-close"]'
        }

    d360_save_port_configuration_message_multi_edit = \
        {
            'XPATH': '//div[@class="ui-tipbox ui-tipbox-success"]//*[@data-dojo-attach-point="textEl"]',
            'wait_for': 5
        }

    d360_save_port_configuration_message_config = \
        {
            'XPATH': '//div[@class="ui-tipbox ui-tipbox-success"]//*[contains(text(), "Port Configuration Saved")]',
            'wait_for': 5
        }

    d360_save_port_configuration_message_voss = \
        {
            'XPATH': '//div[@class="ui-tipbox ui-tipbox-success"]//*[contains(text(), "Port Configuration Saved")]',
            'wait_for': 5
        }

    add_port_type_port_usage_multi_edit = \
        {
            'XPATH': '//span[@data-automation-tag="automation-port-details-multi-edit-multi-edit-add-new-vlan"]',
            'wait_for': 5
        }

    d360_multi_edit_port_count = \
        {
            'XPATH': '//span[@data-dojo-attach-point="portCount"]',
            'wait_for': 5
        }

    device360_stack_slot_sfp_ports = \
        {
            'CSS_SELECTOR': '[class="switch-panel switch-stack-panel"] [class*="AH-ports-icons qsfp28-port"]:not([class$="active"])',
            'wait_for': 5

        }

    d360_config_events = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="hcPills"]/li[@data-automation-tag="automation-pills-configuration"]',
            'wait_for': 5
        }

    device360_port_details_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-port-diagnostics-port-details"]',
            'wait_for': 5
        }

    device360_diagnostics_select_port = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-$index"]',
            'index': 1
        }

    device360_monitor_diagnostics_port_details_table = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridDiagnostics"]',
        }

    device360_monitor_diagnostics_port_details_table_empty = \
        {
            'XPATH': '//div[@id="hcgrid_1"]//div[@class="dgrid-no-data"]',
        }

    device360_monitor_diagnostics_port_details_table_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridDiagnostics"]//div[@class="dgrid-scroller"]//div[contains(@class,"dgrid-row")]',
        }

    device360_monitor_diagnostics_select_all_ports_button = \
        {
            'XPATH': '//div[@class="switch-ports-panel-ctn"]//button[@data-dojo-attach-point="selectAllButton"]',
            'wait_for': 5
        }
    device360_diagnostics_ports_table_scroll = \
        {
            "XPATH": "//div[@data-dojo-attach-point='gridDiagnostics']//div[@class='dgrid-scroller']",
            'wait_for': 5
        }

    device360_diagnostics_select_all_ports_button = \
        {
            'XPATH': '//div[contains(@id, "SwitchPortsPanel_0")]//button[@data-dojo-attach-point="selectAllButton"]',
            'wait_for': 5
        }

    device360_diagnostics_port_details_actions_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-diagnostics-port-details-actions-button"]',
            'wait_for': 5
        }

    device360_diagnostics_actions_bounce_port_button = \
        {
            'XPATH': '//a[@data-automation-tag="automation-diagnostics-port-details-actions-bounce-port"]',
            'wait_for': 5
        }

    device360_diagnostics_port_details_select_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="gridDiagnostics"]//td[contains(@class, "dgrid-column-0")]//input[@type="checkbox"]',
            'wait_for': 5
        }

    device360_diagnostics_actions_bounce_poe_button = \
        {
            'XPATH': '//a[@data-automation-tag="automation-diagnostics-port-details-actions-bounce-poe"]',
            'wait_for': 5
        }
    device360_diagnostics_wireframe_port = \
        {
            'XPATH': '(//div[@data-dojo-attach-point="diagnostics"]//div[@data-dojo-attach-point="portEl"])[$index]',
            'wait_for': 5
        }

    device360_diagnostics_bounce_port_message = \
        {
            'XPATH': '//div[contains(@class, "ui-tipbox-success")]//h3[@data-dojo-attach-point="textEl"]',
            'wait_for': 5
        }

    device360_diagnostics_ah_icons = \
        {
            "XPATH": '//div[@data-dojo-attach-point="diagnostics"]//li/div[contains(@class,"AH-ports-icons")][@data-index="${index}"]',
            'wait_for': 5
        }

    device360_diagnostics_current_unit = \
        {
            "XPATH": '//div[@data-automation-tag="diagnostics-stack-member-chooser-area-with-container"]',
            'wait_for': 5
        }

    device360_diagnostics_dropdown_unit = \
        {
            "XPATH": '(//div[@data-automation-tag="diagnostics-stack-member-chooser-area-with-container"]//li[contains(@data-automation-tag,"Unit")])[$index]',
            'wait_for': 5
        }

    device360_diagnostics_error_message = \
        {
            "XPATH": '//div[contains(@class, "ui-tipbox-error")]',
            'wait_for': 5
        }

    device360_diagnostics_actions_clear_mac_locking = \
        {
            "XPATH": '//a[@data-automation-tag="automation-diagnostics-port-details-actions-clear-MAC-locking"]',
            'wait_for': 5
        }

    device360_diagnostics_port_details_port_status = \
        {
            "XPATH": '(//div[@data-dojo-attach-point="gridDiagnostics"]//table[@class="dgrid-row-table"]//td[contains(@class, "dgrid-column-5")])[$index]',
            'wait_for': 5
        }

    device360_diagnostics_port_details_refresh_button = \
        {
            "XPATH": '//div[@data-dojo-attach-point="deviceEntityCtn"]//div[@class="entity-page-actions"]//div[@data-dojo-attach-point="pageRefresh"]',
            'wait_for': 5
        }

    device360_diagnostics_actions_enable_port_button = \
        {
            "XPATH": '//a[@data-automation-tag="automation-diagnostics-port-details-actions-enable-port"]',
            'wait_for': 5
        }

    device360_diagnostics_bounce_port_error_message = \
        {
            'XPATH': '//div[contains(@class, "ui-tipbox-error")]//h3[@data-dojo-attach-point="textEl"]',
            'wait_for': 5
        }

    device360_diagnostics_port_details_port_name = \
        {
            "XPATH": '(//div[@data-dojo-attach-point="gridDiagnostics"]//table[@class="dgrid-row-table"]//td[contains(@class,"ifName")])[$index]',
            'wait_for': 5
        }

    device360_diagnostics_port_table_select_checkbox= \
        {
            "XPATH": '(//div[@data-dojo-attach-point="gridDiagnostics"]//input[@type="checkbox"])[$index]',
            'wait_for': 5
        }

    device360_diagnostics_port_details_actions_button_disabled = \
        {
            "XPATH": '//div[@data-automation-tag="automation-diagnostics-port-details-actions"]//button[contains(@class, "btn-disabled")]',
            'wait_for': 5
        }

    device360_diagnostics_deselect_all_button = \
        {
            "XPATH": '(//div[@class="device-diagnostics"]//button[@data-dojo-attach-point="deselectAllButton"])[$index]',
            'wait_for': 5
        }

    device360_diagnostics_select_all_button = \
        {
            "XPATH": '(//div[@class="device-diagnostics"]//button[@data-dojo-attach-point="selectAllButton"])[$index]',
            'wait_for': 5
        }

    d360_port_status_overview = \
        {
            'CSS_SELECTOR': '.field-status',
            'wait_for': 5
        }

    d360_mac_locking_overview = \
        {
            'CSS_SELECTOR': '.field-macLock',
            'wait_for': 5
        }

    d360_port_config_option_tab = \
        {
            'XPATH': '//div[@data-automation-tag="automation-port-config-${option}"]',
            'wait_for': 5
        }

    mac_locking_exceed_limit_error = \
        {
            'CSS_SELECTOR': '.form-error.form-error-msg',
            'wait_for': 5
        }

    d360_mac_locking_disable_port = \
        {
            'XPATH': '//div[@data-entry-index="${port_number}"]//input[@data-automation-tag="port-maclock-disable-port"]',
            'wait_for': 5
        }

    d360_mac_locking_link_down_action = \
        {
            'XPATH': '//div[@data-entry-index="${port_number}"]//div[@data-automation-tag="automation-port-maclock-link-down-action-chzn-container-ctn"]',
            'wait_for': 5
        }

    wait_for_port_config_to_load = \
        {
            'XPATH': '//div[@data-dojo-attach-point="spinner"]',
            'wait_for': 5
        }

    d360_mac_locking_remove_mac_toggle = \
        {
            'XPATH': '//div[@data-entry-index="${port_number}"]//input[@data-automation-tag="port-maclock-remove-aged-macs"]',
            'wait_for': 5
        }

    configuration_events_button = \
        {
            "XPATH": "//li[@data-automation-tag='automation-pills-configuration']"
        }

    device360_lag_popup_spinner = \
        {
            'CSS_SELECTOR': '.lag-view .grid-mark',
            'wait_for': 5
        }