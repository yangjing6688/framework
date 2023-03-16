class Network360MonitorDefinitions:
    n360_monitor_location_search_box = \
        {
            'XPATH': '//*[@data-automation-tag="automation-tracker-search-field"]',
            'wait_for': 5
        }

    n360_monitor_floors = \
        {
            'XPATH': '//*[@data-automation-tag="automation-plan-search-field"]',
            'wait_for': 5
        }

    n360_monitor_search_matches = \
        {
            'XPATH': '//*[@style="background-color: #fc0;"]',
            'wait_for': 5
        }

    n360_monitor_aps_on_floor = \
        {
            'CSS_SELECTOR': '.device-hostname',
            'wait_for': 5
        }

    n360_monitor_ap_count_on_floor = \
        {
            'XPATH': '//*[@data-dojo-attach-point="apCount"]',
            'wait_for': 2
        }

    n360_monitor_connected_clients_tab = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientMenuItem"]',
            'wait_for': 5
        }

    n360_monitor_clients_on_floor = \
        {
            'XPATH': '//*[@data-dojo-attach-point="clientMenuItem"]',
            'wait_for': 5
        }

    n360_connected_client_macs = \
        {
            'CSS_SELECTOR': '.field-macAddress',
            'wait_for': 5
        }

    n360_monitor_devices_score = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceHealthScoreLabelCtn"]',
            'wait_for': 5
        }

    n360_monitor_devices_card = \
        {
            # 'XPATH': '//*[@data-dojo-attach-point="deviceHealthScoreLabelCtn"]//span[@class="open-screen-icon ah-global-icon"]',
            # 'XPATH': '//*[@data-dojo-attach-point="automation-tracker-n360-card-device"]',
            'CSS_SELECTOR': '.open-screen-icon.ah-global-icon',
            'index': 0,
            'wait_for': 5
        }

    n360_monitor_clients_card = \
        {
            'CSS_SELECTOR': '.open-screen-icon.ah-global-icon',
            'index': 1,
            'wait_for': 5
        }

    device_health_overal_score_availability_score = \
        {
            'XPATH': '//*[@data-dojo-attach-point="scoreAvailabilityValue"]',
            'wait_for': 5
        }

    device_health_overal_score_hw_health = \
        {
            'XPATH': '//*[@data-dojo-attach-point="scoreHardwareValue"]',
            'wait_for': 5
        }

    device_health_overal_score_fw_score = \
        {
            'XPATH': '//*[@data-dojo-attach-point="scoreConfFirmwareValue"]',
            'wait_for': 5
        }

    n360_monitor_map = \
        {
            'XPATH': '//*[@data-dojo-attach-point="physicalMap"]',
            'wait_for': 5
        }

    client_health_clients_widget_count_2G = \
        {
            'XPATH': '//span[contains(text(), "2.4 GHz")]/../b',
            'wait_for': 5
        }

    client_health_clients_widget_count_5G = \
        {
            'XPATH': '//span[contains(text(),"5 GHz")]/../b',
            'wait_for': 5
        }

    client_health_clients_widget_count_6G = \
        {
            'XPATH': '//span[contains(text(),"6 GHz")]/../b',
            'wait_for': 5
        }

    graph_point = \
        {
            'XPATH': '//div[@data-dojo-attach-point="highChartCtn"]//*[name()="svg"]/*[name()="g"]/*[name()="g"] [contains(@class, "highcharts-markers highcharts-series-${color} highcharts-spline-series highcharts-tracker")]',
            'wait_for': 5
        }

    graph_point_hover = \
        {
            'XPATH': '//div[@data-dojo-attach-point="highChartCtn"]//*[name()="svg"]/*[name()="g"]/*[name()="g"] [contains(@class, "highcharts-markers highcharts-series-${color} highcharts-spline-series highcharts-tracker highcharts-series-hover")]',
            'wait_for': 5
        }

    graph_line_color = \
        {
            'XPATH': '//div[@data-dojo-attach-point="highChartCtn"]//*[name()="svg"]/*[name()="g"]/*[name()="g"] [contains(@class, "highcharts-series highcharts-series-${color} highcharts-spline-series")]',
            'wait_for': 5
        }

    graph_legend_names = \
        {
            'XPATH': '//div[@data-dojo-attach-point="highChartCtn"]//*[name()="svg"]//*[name()="g"][contains(@class, "highcharts-legend-item highcharts-spline-series highcharts-color-undefined highcharts-series-${color}")]',
            'wait_for': 5
        }

    n360_back_to_timeline = \
        {
            'CSS_SELECTOR': '.fw400.font_75.back-btn.fn-inline-block',
            'wait_for': 5
        }

    n360_graph_tooltip = \
        {
            'XPATH': '//div[@data-dojo-attach-point="highChartCtn"]//*[name()="svg"]/*[name()="g"][@class="highcharts-label highcharts-tooltip highcharts-color-undefined"]',
            'wait_for': 5
        }
    n360_graph_tooltip_info = \
        {
            'XPATH': '//div[@data-dojo-attach-point="highChartCtn"]//div[@class="highcharts-label highcharts-tooltip highcharts-color-undefined"]//div[contains (text(),*)]',
            'wait_for': 5
        }

    n360_device_health_refresh_btn = \
        {
            'XPATH': '//div[@data-dojo-attach-point="pageRefresh"]',
            'wait_for': 5
        }

    n360_device_health_pagination = \
        {
            'CSS_SELECTOR': '.J-page-size.ui-page-size',
            'wait_for': 5
        }

    n360_device_health_settings_btn = \
        {
            'CSS_SELECTOR': '[data-tip="Settings"][data-dojo-attach-point="flagSetting"]:not([style*=none])',
            'wait_for': 5
        }

    n360_device_health_events_list = \
        {
            'CSS_SELECTOR': '.entity-timeline-flag-setting-list.entity-timeline-flag-setting-list-client[style*="1"] ul li .checkbox',
            'wait_for': 5
        }
    n360_device_health_events_checkbox = \
        {
            'XPATH': '//div[@data-dojo-attach-point="flagSettingList"][@style="opacity: 1;"]/ul/li/label/input',
            'wait_for': 5
        }

    n360_device_health_search_box = \
        {
            'CSS_SELECTOR': '.search-filter[data-dojo-attach-point="inputSearch"]',
            'wait_for': 5
        }

    n360_device_health_column_headers = \
        {
            'CSS_SELECTOR': '[id="dgrid_18"] .dgrid-row-table tr th[class^="dgrid-cell dgrid-colum"][role="columnheader"]',
            'wait_for': 5
        }

    n360_device_health_column_header_mac = \
        {
            'CSS_SELECTOR': '.dgrid-cell.dgrid-column-2.field-macAddress.w175.black3.dgrid-sortable',
            'wait_for': 5
        }
    n360_device_health_column_header_hostname = \
        {
            'CSS_SELECTOR': '.dgrid-cell.dgrid-column-1.field-hostName.w175.black3.dgrid-sortable',
            'wait_for': 5
        }

    n360_device_health_total_usage = \
        {
            'CSS_SELECTOR': '.fw200',
            'wait_for': 5
        }

    n360_device_health_download_button = \
        {
            'CSS_SELECTOR': 'div[id^="ah"] .timeline-ctn-360 .table-action-icons.table-download',
            'wait_for': 5
        }

    n360_device_health_column_header = \
        {
            'CSS_SELECTOR': '.dgrid-row-table',
            'index': 3,
            'wait_for': 5
        }

    n360_monitor_port_device_health_usage_table_rows = \
        {
            "XPATH": "//div[@class='dgrid-content ui-widget-content']//div[@role='row']",
            'wait_for': 5
        }

    n360_monitor_port_connection_speed_table_grid_rows = \
        {
            "XPATH": "//div[@data-automation-tag='switches-port-connection-speed-grid-containter']//*[@data-dojo-attach-point='gridContent']//*[@class='dgrid-row-table']",
            'wait_for': 5
        }

    n360_monitor_port_connection_speed_table_td_gridcell = \
        {
            "XPATH": ".//tr//td[@role='gridcell']",
            'wait_for': 5
        }

    n360_monitor_device_health_th_columns = \
        {
            'CSS_SELECTOR': '.dgrid-row-table',
            'wait_for': 5

            # "XPATH": "//*[@role='columnheader']",
            # 'wait_for': 5
        }

    n360_monitor_drop_down_options = \
        {
            'XPATH': '//div[@data-automation-tag="automation-tracker-os-filter-chzn-drop-ctn"]//li[contains(text(),"${option}")]',
            'wait_for': 5
        }

    n360_monitor_health_selector_drop_down_arrow = \
        {
            'XPATH': '//div[@data-automation-tag="automation-tracker-os-filter-chzn-arrow-down"]',
            'wait_for': 5
        }

    n360_monitor_health_selector_drop_down_options = \
        {
            'XPATH': '//div[@data-automation-tag="automation-360-selector-chzn-drop-ctn"]//li[contains(text(),"${option}")]',
            'wait_for': 5
        }

    n360_monitor_port_connection_speed_container_down_arrow = \
        {
            'XPATH': '//*[@data-automation-tag="automation-tracker-os-filter-chzn-arrow-down"]',
            'wait_for': 5
        }

    close_n360_dialog_box = \
        {
            'XPATH': '//div[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }

    n360_show_all_btn = \
        {
            'XPATH': '//button[@data-dojo-attach-point="showAllBtn"]',
            'wait_for': 5
        }