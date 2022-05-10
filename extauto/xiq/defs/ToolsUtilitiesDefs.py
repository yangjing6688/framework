

class ToolsUtilitiesDefs:

    utilities_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-tools-controller-troubleshoot-utilities-link"]',
            'wait_for': 5
        }

    neighbor_info_menu = \
        {
            # 'XPATH': '//*[@aria-label="Neighbor Info "]',
            'CSS_SELECTOR': '.dijitMenuActive',
            'wait_for': 2
        }

    neighbor_info_menu_item= \
    {
        # 'XPATH': '//*[@aria-label="Neighbor Info "]',
        'CSS_SELECTOR': '.dijitMenuItem',
        'wait_for': 2
    }

    device_diagnostics_menu_item= \
    {
        # 'XPATH': '//*[@aria-label="Neighbor Info "]',
        'CSS_SELECTOR': '.dijitMenuItem',
        'wait_for': 2
    }

    neighbor_info_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="toolButton"]',
            'wait_for': 2
        }

    dialog_page_body = \
        {
            'CSS_SELECTOR': '.device-utilities-page-body',
            'wait_for': 2
        }

    neighbor_page_body_grid = \
        {

        }

    neighbor_page_body_grid_rows = \
        {
            'TAG_NAME': 'tr',
            'wait_for': 10
        }

    neighbor_info_close_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 2
        }

    diagnostics_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="toolUtilities"]',
            'wait_for': 2
        }

    diagnostics_menu = \
        {
            'CSS_SELECTOR': '.ui-menu-list',
            'wait_for': 2
        }

    diagnostics_menu_items = \
        {
            'CSS_SELECTOR': '.ui-menu-item',
            'wait_for': 2
        }

    account_icon = \
        {
            'XPATH': "//*[@data-dojo-attach-point='headerUserIcon']",
            'wait_for': 5
        }

    global_settings = \
        {
            'XPATH': "//*[@data-dojo-attach-point='accountEl']",
            'wait_for': 5
        }

    SSH_availability = \
        {
            'XPATH': "//*[@data-automation-tag='automation-sider-list-sshAvailability']",
            'wait_for': 5
        }

    enable_ssh = \
        {
            'XPATH': "//*[@data-dojo-attach-point='globalEnableSSH']",
            'wait_for': 5
        }

    manage_button = \
        {
            'XPATH': '/html/body/div/div[1]/div/div/div/ul/li[3]/span/a',
            'wait_for': 5
        }

    tool_button = \
        {
            'XPATH': '/html/body/div/div[1]/div/div/div/ul/li[3]/ul/li[10]/a',
            'wait_for': 5
        }

    utilities_ssh_availability = \
        {
            #'XPATH': "//*[@id='dijit_MenuItem_2_text']",
            #'//*[@id="dijit_MenuItem_2"]'
            #'aria-label="SSH Availability "'
            'XPATH': '//*[@aria-label="SSH Availability "]',
            'wait_for': 5
        }

    ap_results_table = \
        {
            'XPATH': "//*[@class='dgrid-content ui-widget-content']",
            'wait_for': 5
        }

    ap_results_rows = \
        {
            'XPATH': "//*[@class='dgrid-row-table']",
            'wait_for': 5
        }

    run_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='toolButton']",
            'wait_for': 5
        }

    ssh_timeout_5_minutes_radio = \
        {
            'NAME': "timeout",
            'wait_for': 5,
            'index': 0
        }

    ssh_timeout_30_minutes_radio = \
        {
            'NAME': "timeout",
            'wait_for': 5,
            'index': 1
        }

    ssh_timeout_60_minutes_radio = \
        {
            'NAME': "timeout",
            'wait_for': 5,
            'index': 2
        }

    ssh_timeout_120_minutes_radio = \
        {
            'NAME': "timeout",
            'wait_for': 5,
            'index': 3
        }

    enable_ssh_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='setDeviceSSH']",
            'wait_for': 5
        }

    ip_address = \
        {
            'XPATH': "//*[@data-dojo-attach-point='ipAddress']",
            'wait_for': 5
        }

    port_num = \
        {
            'XPATH': "//*[@data-dojo-attach-point='port']",
            'wait_for': 5
        }

    command = \
        {
            'XPATH': "//*[@data-dojo-attach-point='exampleCommand']",
            'wait_for': 5
        }

    ssh_status = \
        {
            'XPATH': "//*[@data-dojo-attach-point='deviceStatus']//div[@data-dojo-attach-point='status']",
            'wait_for': 5
        }

    device_list_link = \
        {
            'XPATH': '//div[@class="dijitPopup dijitMenuPopup" and not(contains(@style, "display"))]/descendant::td[text()="Device List"]',
            'wait_for': 5
        }

    client_info_link = \
        {
            'XPATH': '//div[@class="dijitPopup dijitMenuPopup" and not(contains(@style, "display"))]/descendant::td[text()="Client Information"]',
            'wait_for': 5
        }

    device_client_info_link = \
        {
            'XPATH': '//div[@class="dijitPopup dijitMenuPopup" and not(contains(@style, "display"))]/descendant::td[text()="Device Client Information"]',
            'wait_for': 5
        }

    device_diag_link = \
        {
            'XPATH': '//div[@class="dijitPopup dijitMenuPopup" and not(contains(@style, "display"))]/descendant::td[text()="Device Diagnostics"]',
            'wait_for': 5
            }

    device_client_info_grids = \
        {
            'XPAth': '//*[contains(@id,"dojox_grid__View")]/div/div/div/div/table/tbody/tr/td',
            'wait_for': 10
        }
    device_client_info_ap_name_txt = \
        {
            'XPATH': '//*[contains(@id,"dojox_grid__View")]/div/div/div/div/table/tbody/tr/td[4]',
            'wait_for': 3
        }

    device_client_info_ap_mac_txt = \
        {
            'XPATH': '//*[contains(@id,"dojox_grid__View")]/div/div/div/div/table/tbody/tr/td[1]',
            'wait_for': 3
        }

    device_client_info_title = \
        {
            'XPATH': '//span[@data-dojo-attach-point="utilitiesTitle"]',
            'wait_for': 3
        }

    device_info_btn = \
        {
            'XPATH': '//button[@data-dojo-attach-point="toolButton"]',
            'wait_for': 5
        }

    device_title_lbl = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceTitle"]',
            'wait_for': 2
        }

    device_info_close_btn = \
        {
            'XPATH': '//span[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }

    ap_status_connect = \
        {
            'XPATH': '//span/span[@title="Connected"]',
            'wait_for': 2
        }

    ap_status_disconnect = \
        {
            'XPATH': '//span/span[@title="Disconnected"]',
            'wait_for': 2
        }

    device_connect_status = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceConnectedTest"]',
            'wait_for': 2
        }

    device_close_dlg = \
        {
            'XPATH': '//div[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 2
        }

    locked_device_link = \
        {
            'XPATH': '//div[@class="dijitPopup dijitMenuPopup" and not(contains(@style, "display"))]/descendant::td[text()="Locked Devices"]',
            'wait_for': 5
        }

    locked_device_unlock_btn = \
        {'XPATH': '//button[@data-dojo-attach-point="unlockDevices"]',
         'wait_for': 10
         }

    locked_device_tbl = \
        {'XPATH': '//*[@id="ah/comp/common/LoginPage_0"]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/form/input[2]',
         'wait_for': 15
         }

    locked_device_host = \
        {'XPATH': '//*[@id="ah/comp/common/LoginPage_0"]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/form/input[2]',
         'wait_for': 15
         }

    client_info_list = \
        {'XPATH': '//div[contains(@id,"dgrid")]/table/tr/td',
         'wait_for': 5
         }

    device_diag_btn = \
        {
            'XPATH': '//span[@data-dojo-attach-point="deviceDiagnosticsBtn"]/div/button[text()="Diagnostics"]',
            'wait_for': 3
        }
    device_diag_list = \
        {'CSS_SELECTOR': '.dgrid-row',
         'wait_for': 10
         }
    device_diag_ping_btn1 = \
        {'XPATH': '//span[@data-dojo-attach-point="deviceDiagnosticsBtn"]/div[1]/ul[1]/li/a[text() = "Ping"]',
         'wait_for': 3
         }
    device_diag_ping_btn2 = \
        {'XPATH': '//button[@data-dojo-attach-point="pingButton"]',
         'wait_for': 3
         }
    device_diag_ping_txt_area = \
        {'XPATH': '//div[contains(@id,"deviceutilities")]/div[2]/pre',
         'wait_for': 5
         }
    device_diag_ping_input_txt = \
        {'XPATH': '//input[@data-dojo-attach-point="devicePing"]',
         'wait_for': 3
         }
    device_diag_ping_close_dlg = \
        {'XPATH': '//span[@data-dojo-attach-point="closeDialog"]',
         'wait_for': 3
         }

    vlan_probe_link = \
        {
            'XPATH': '//div[@class="dijitPopup dijitMenuPopup" and not(contains(@style, "display"))]/descendant::td[text()="VLAN Probe"]',
            'wait_for': 5
        }
    vlan_probe_btn = \
        {'XPATH': '//button[@data-dojo-attach-point="toolButton" and text() = "VLAN Probe"]',
         'wait_for': 3
         }
    vlan_probe_input_range_txt = \
        {'XPATH': '//input[@data-dojo-attach-point="vlanRanges"]',
         'wait_for': 10
         }
    vlan_probe_timeout_txt = \
        {'XPATH': '//input[@data-dojo-attach-point="probeTimeout"]',
         'wait_for': 3
         }
    vlan_probe_start_btn = \
        {'XPATH': '//button[@data-dojo-attach-point="startBtn"]',
         'wait_for': 3
         }
    vlan_probe_results = \
        {'XPATH': '//div[@data-dojo-attach-point="vlanProbeResults"]/div[2]/div/div[2]/table/tr/td[1]',
         'wait_for': 3
         }
    vlan_probe_close_diag = \
        {'XPATH': '//span[@data-dojo-attach-point="closeButtonNode"]',
         'wait_for': 3
         }

    tech_data_link = \
        {
            'XPATH': '//div[@class="dijitPopup dijitMenuPopup" and not(contains(@style, "display"))]/descendant::td[text()="Get Tech Data"]',
            'wait_for': 3
            }
    tech_data_btn = \
        {'XPATH': '//button[@data-dojo-attach-point="toolButton"]',
         'wait_for': 3
         }
    tech_data_yes_btn = \
        {'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
         'wait_for': 3
         }
    tech_data_download_btn = \
        {'XPATH': '//button[@class="btn btn-primary line J-downloadTechData"]',
         'wait_for': 3
         }
    tech_data_close_diaglog = \
        {'XPATH': '//span[@data-dojo-attach-point="closeDialog"]',
         'wait_for': 3
         }

    device_utilities = \
        {
            'XPATH': '//button[@data-automation-tag="automation-manage-device-utilities-button"]',
            'wait_for': 5
        }
    device_diagnostics = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-utilities-diagnostics"]',
            'wait_for': 5
        }

    device_ping = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-utilities-diagnostics-show-ping"]',
            'wait_for': 5
        }

    device_ping_content = \
        {
            'XPATH': '//div[@data-dojo-attach-point="contentList"]',
            'wait_for': 5
        }

    device_ping_close = \
        {
            'XPATH': '//span[@data-automation-tag="automation-show-ping-dialog-close-button"]',
            'wait_for': 5
        }
