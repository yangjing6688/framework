

class ToolsUtilitiesDefs:

    diagnostics_ping_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-ping"]'
        }

    utilities_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-button"]'
        }

    neighbor_info_menu = \
        {
            'CSS_SELECTOR': '.ui-menu-item'
        }

    neighbor_info_menu_item= \
    {
        'XPATH':  "//*[@data-automation-tag='automation-manage-device-utilities-tools-layer-neighbor-info']"
    }

    device_diagnostics_menu_item= \
    {
        'XPATH': "//*[@data-automation-tag='automation-manage-device-utilities-diagnostics']"
    }

    neighbor_info_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="toolButton"]'
        }

    dialog_page_body = \
        {
            'XPATH': '//*[@data-dojo-attach-point="contentList"]'
            # 'CSS_SELECTOR': '.device-utilities-page-body'
        }

    neighbor_page_body_grid = \
        {

        }

    neighbor_page_body_grid_rows = \
        {
            'TAG_NAME': 'tr'
        }

    neighbor_info_close_button = \
        {
            #'XPATH': '//*[@data-dojo-attach-point="closeDialog"]'
            'XPATH': "//*[@data-automation-tag='automation-neighbor-info-dialog-close-button']"
        }

    diagnostics_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="toolUtilities"]'
        }

    diagnostics_menu = \
        {
            'CSS_SELECTOR': '.ui-menu-list'
        }

    diagnostics_menu_items = \
        {
            'CSS_SELECTOR': '.ui-menu-item'
        }

    account_icon = \
        {
            'XPATH': "//*[@data-dojo-attach-point='headerUserIcon']"
        }

    global_settings = \
        {
            'XPATH': "//*[@data-dojo-attach-point='accountEl']"
        }

    SSH_availability = \
        {
            'XPATH': "//*[@data-automation-tag='automation-sider-list-sshAvailability']"
        }

    enable_ssh = \
        {
            'XPATH': "//*[@data-dojo-attach-point='globalEnableSSH']"
        }

    manage_button = \
        {
            'XPATH': '/html/body/div/div[1]/div/div/div/ul/li[3]/span/a'
        }

    tool_button = \
        {
            'XPATH': '/html/body/div/div[1]/div/div/div/ul/li[3]/ul/li[10]/a'
        }

    utilities_ssh_availability = \
        {
            'XPATH': '//*[@aria-label="SSH Availability "]'
        }

    ap_results_table = \
        {
            'XPATH': "//*[@class='dgrid-content ui-widget-content']"
        }

    ap_results_rows = \
        {
            'XPATH': "//*[@class='dgrid-row-table']"
        }

    run_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='toolButton']"
        }

    ssh_timeout_5_minutes_radio = \
        {
            'NAME': "timeout",
            'index': 0
        }

    ssh_timeout_30_minutes_radio = \
        {
            'NAME': "timeout",
            'index': 1
        }

    ssh_timeout_60_minutes_radio = \
        {
            'NAME': "timeout",
            'index': 2
        }

    ssh_timeout_120_minutes_radio = \
        {
            'NAME': "timeout",
            'index': 3
        }

    enable_ssh_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='setDeviceSSH']"
        }

    ip_address = \
        {
            'XPATH': "//*[@data-dojo-attach-point='ipAddress']"
        }

    port_num = \
        {
            'XPATH': "//*[@data-dojo-attach-point='port']"
        }

    command = \
        {
            'XPATH': "//*[@data-dojo-attach-point='exampleCommand']"
        }

    ssh_status = \
        {
            'XPATH': "//*[@data-dojo-attach-point='deviceStatus']//div[@data-dojo-attach-point='status']"
        }

    device_list_link = \
        {
            'XPATH': '//div[@class="dijitPopup dijitMenuPopup" and not(contains(@style, "display"))]/descendant::td[text()="Device List"]'
        }

    client_info_link = \
        {
            'XPATH': '//div[@class="dijitPopup dijitMenuPopup" and not(contains(@style, "display"))]/descendant::td[text()="Client Information"]'
        }

    device_client_info_link = \
        {
            'XPATH': '//div[@class="dijitPopup dijitMenuPopup" and not(contains(@style, "display"))]/descendant::td[text()="Device Client Information"]'
        }

    device_diag_link = \
        {
            'XPATH': '//div[@class="dijitPopup dijitMenuPopup" and not(contains(@style, "display"))]/descendant::td[text()="Device Diagnostics"]'
        }

    device_client_info_grids = \
        {
            'XPAth': '//*[contains(@id,"dojox_grid__View")]/div/div/div/div/table/tbody/tr/td'
        }
    device_client_info_ap_name_txt = \
        {
            'XPATH': '//*[contains(@id,"dojox_grid__View")]/div/div/div/div/table/tbody/tr/td[4]'
        }

    device_client_info_ap_mac_txt = \
        {
            'XPATH': '//*[contains(@id,"dojox_grid__View")]/div/div/div/div/table/tbody/tr/td[1]'
        }

    device_client_info_title = \
        {
            'XPATH': '//span[@data-dojo-attach-point="utilitiesTitle"]'
        }

    device_info_btn = \
        {
            'XPATH': '//button[@data-dojo-attach-point="toolButton"]'
        }

    device_title_lbl = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceTitle"]'
        }

    device_info_close_btn = \
        {
            'XPATH': '//span[@data-dojo-attach-point="closeDialog"]'
        }

    ap_status_connect = \
        {
            'XPATH': '//span/span[@title="Connected"]'
        }

    ap_status_disconnect = \
        {
            'XPATH': '//span/span[@title="Disconnected"]'
        }

    device_connect_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceConnectedTest"]'
        }

    device_close_dlg = \
        {
            'XPATH': '//div[@data-dojo-attach-point="closeDialog"]'
        }

    locked_device_link = \
        {
            'XPATH': '//div[@class="dijitPopup dijitMenuPopup" and not(contains(@style, "display"))]/descendant::td[text()="Locked Devices"]'
        }

    locked_device_unlock_btn = \
        {
            'XPATH': '//button[@data-dojo-attach-point="unlockDevices"]'
         }

    locked_device_tbl = \
        {
            'XPATH': '//*[@id="ah/comp/common/LoginPage_0"]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/form/input[2]'
         }

    locked_device_host = \
        {
            'XPATH': '//*[@id="ah/comp/common/LoginPage_0"]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/form/input[2]'
         }

    client_info_list = \
        {
            'XPATH': '//div[contains(@id,"dgrid")]/table/tr/td'
         }

    device_diag_btn = \
        {
            'XPATH': '//span[@data-dojo-attach-point="deviceDiagnosticsBtn"]/div/button[text()="Diagnostics"]'
        }

    device_diag_list = \
        {
            'CSS_SELECTOR': '.dgrid-row'
         }

    device_diag_ping_btn1 = \
        {
            'XPATH': '//span[@data-dojo-attach-point="deviceDiagnosticsBtn"]/div[1]/ul[1]/li/a[text() = "Ping"]'
         }

    device_diag_ping_btn2 = \
        {
            'XPATH': '//button[@data-dojo-attach-point="pingButton"]'
         }

    device_diag_ping_txt_area = \
        {
            'XPATH': '//div[contains(@id,"deviceutilities")]/div[2]/pre'
         }

    device_diag_ping_input_txt = \
        {
            'XPATH': '//input[@data-dojo-attach-point="devicePing"]'
         }

    device_diag_ping_close_dlg = \
        {
            # 'XPATH': '//span[@data-dojo-attach-point="closeDialog"]'
            'XPATH': '//*[@data-automation-tag="automation-show-ping-dialog-close-button"]'
         }

    vlan_probe_link = \
        {
            'XPATH': '//div[@class="dijitPopup dijitMenuPopup" and not(contains(@style, "display"))]/descendant::td[text()="VLAN Probe"]'
        }

    vlan_probe_btn = \
        {
            'XPATH': '//button[@data-dojo-attach-point="toolButton" and text() = "VLAN Probe"]'
         }

    vlan_probe_input_range_txt = \
        {
            'XPATH': '//input[@data-dojo-attach-point="vlanRanges"]'
         }

    vlan_probe_timeout_txt = \
        {
            'XPATH': '//input[@data-dojo-attach-point="probeTimeout"]'
         }

    vlan_probe_start_btn = \
        {
            'XPATH': '//button[@data-dojo-attach-point="startBtn"]'
         }

    vlan_probe_results = \
        {
            'XPATH': '//div[@data-dojo-attach-point="vlanProbeResults"]/div[2]/div/div[2]/table/tr/td[1]'
         }

    vlan_probe_close_diag = \
        {
            'XPATH': '//span[@data-dojo-attach-point="closeButtonNode"]'
         }

    tech_data_link = \
        {
            'XPATH': '//div[@class="dijitPopup dijitMenuPopup" and not(contains(@style, "display"))]/descendant::td[text()="Get Tech Data"]'
        }
    tech_data_btn = \
        {
            'XPATH': '//button[@data-dojo-attach-point="toolButton"]'
         }

    tech_data_yes_btn = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]'
         }

    tech_data_download_btn = \
        {
            'XPATH': '//button[@class="btn btn-primary line J-downloadTechData"]'
         }

    tech_data_close_diaglog = \
        {
            'XPATH': '//span[@data-dojo-attach-point="closeDialog"]'
         }

    device_utilities = \
        {
            'XPATH': '//button[@data-automation-tag="automation-manage-device-utilities-button"]'
        }

    device_diagnostics = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-utilities-diagnostics"]'
        }

    device_ping = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-ping"]'
        }

    device_ping_content = \
        {
            'XPATH': '//div[@data-dojo-attach-point="contentList"]'
        }

    device_ping_close = \
        {
            'XPATH': '//span[@data-automation-tag="automation-show-ping-dialog-close-button"]'
        }
