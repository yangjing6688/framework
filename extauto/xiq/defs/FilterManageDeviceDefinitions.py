class FilterManageDeviceDefinitions:

    toggle_filter_link = \
        {
            'XPATH': '//a[@data-dojo-attach-point="filterToggle"]',
            'wait_for': 5
        }
    location_filter_link = \
        {
            'XPATH': '//span[contains(text(),"Locations")]',
            'wait_for': 5
        }

    network_policy_filter_link = \
        {
           'XPATH': '//span[contains(text(),"Network Policies") and @data-dojo-attach-point="titleNode"]',
           #'XPATH': '//div[@data-name="Network Policies"]//h4',
           'wait_for': 5
        }

    network_policy_all_filter_chkbox = \
        {  'XPATH' : '//input[@data-id="ALL_NETWORK_POLICIES"]',
           'wait_for' : 2

        }
    my_saved_list_filter = \
        {
            'XPATH': '//ul[@class="saved-filter-list"]/li',
            'wait_for': 5
        }

    device_policy_list = \
        {
            'XPATH': '//div[@data-automation-tag="automation-manage-device-list"]/descendant::td[contains(@class,"networkPolicyName")]//a',
            'wait_for': 5
        }

    device_serial_list = \
        {
            'XPATH': '//div[@data-automation-tag="automation-manage-device-list"]/descendant::td[contains(@class,"serialNumber")]/div',
            'wait_for': 5
        }

    list_del_index_filter = \
        {
            'XPATH': '//li[1]/span[@data-dojo-attach-point="closeBox"]',
            'wait_for': 5
        }
    applied_filter_btn = \
        {
            'XPATH': '//span[contains(text(),"Apply Filters") and @data-dojo-attach-point="applyFilterBtn"]',
            'wait_for': 5
        }
    apply_filters_btn = \
        {
            'XPATH': '//span[contains(text(),"Apply Filters") and @data-dojo-attach-point="applyFilterBtn"]',
            'wait_for': 5
        }
    applied_filter_link = \
        {
            'XPATH': '//span[contains(text(),"Applied Filters") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    applied_filter_clear_link = \
        {
            'XPATH': '//a[@data-dojo-attach-point="chipControlClearAll"]',
            'wait_for': 5
        }
    applied_filter_list = \
        {
            'XPATH': '//div[@data-dojo-attach-point="containerNode"]/span',
            'wait_for': 5
        }
    applied_filter_list_index = \
        {
            'XPATH': '//div[@data-dojo-attach-point="containerNode"]/span[1]',
            'wait_for': 5
        }
    network_policy_filter_chkbox = \
        {
           'XPATH': '//input[@data-name=',
           'wait_for': 5
        }

    saved_filter_chkbox = \
        {
            'XPATH': '//input[@data-name=',
            'wait_for': 5
        }

    all_policies_filter = \
        {
            'XPATH': '//input[@class="filter-loca-checked" and @data-id="ALL_NETWORK_POLICIES"]',
            'wait_for': 5
        }

    save_filter_btn = \
        {
            'XPATH': '//span[contains(text(),"Save") and @data-dojo-attach-point = "containerNode"]',
            'wait_for': 5
        }

    dialog_save_filter_btn = \
        {
            'XPATH': '//div[contains(@class,"column grid")]/button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    dialog_input_filter_filename_txt = \
        {
            'XPATH': '//input[@data-dojo-attach-point="filterName"]',
            'wait_for': 5
        }

    dialog_yes_filter_btn = \
         {
             'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
             'wait_for': 5
         }

    device_type_filter_link = \
        {
            'XPATH': '//span[contains(text(),"Device Types") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_type_filter_link_expanded = \
        {
            'XPATH': '//div[@aria-pressed="true"]//span[contains(text(),"Device Types") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_type_filter_link_collapsed = \
        {
            'XPATH': '//div[@aria-pressed="false"]//span[contains(text(),"Device Types") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    all_device_types_filter_chkbox = \
        {
            'XPATH': '//input[@data-id="ALL_DEVICE_TYPES"]',
            'wait_for': 5
        }

    plan_device_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="Plan Devices"]',
            'wait_for': 5
        }

    real_device_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="Real Devices"]',
            'wait_for': 5
        }

    simulated_device_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="Simulated Devices"]',
            'wait_for': 5
        }

    device_host_filter_list = \
        {
            'XPATH': '//div[@data-automation-tag="automation-manage-device-list"]/descendant::td[contains(@class,"hostname")]/div/a',
            'wait_for': 5
        }



    device_connection_state_filter_link = \
        {
            'XPATH': '//span[contains(text(),"Device Connection State") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_connection_state_filter_link_expanded = \
        {
            'XPATH': '//div[@aria-pressed="true"]//span[contains(text(),"Device Connection State") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_connection_state_filter_link_collapsed = \
        {
            'XPATH': '//div[@aria-pressed="false"]//span[contains(text(),"Device Connection State") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_state_all_filter_chkbox = \
        {
            'XPATH': '//input[@data-id="ALL_DEVICE_CONNECTION_STATES"]',
            'wait_for': 5
        }

    device_state_connected_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="Connected"]',
            'wait_for': 5
        }

    device_state_disconnected_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="Disconnected"]',
            'wait_for': 5
        }

    device_state_preprovisioned_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="Pre Provisioned"]',
            'wait_for': 5
        }

    # state_status_filter_list = \
    #     {
    #         'XPATH': '//div[@data-automation-tag="automation-manage-device-list"]/descendant::span[contains(@id,"Connected")]/span',
    #         'wait_for': 5
    #     }

    state_status_filter_list = \
        {
            'CSS_SELECTOR': '.hive-status',
            'wait_for': 1
        }



    device_prod_type_filter_link = \
        {
            'XPATH': '//span[contains(text(),"Device Product Type") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_prod_type_filter_link_expanded = \
        {
            'XPATH': '//div[@aria-pressed="true"]//span[contains(text(),"Device Product Type") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_prod_type_filter_link_collapsed = \
        {
            'XPATH': '//div[@aria-pressed="false"]//span[contains(text(),"Device Product Type") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_prod_type_all_filter_chkbox = \
        {
            'XPATH': '//input[@data-id="ALL_PRODUCT_TYPE_IDS"]',
            'wait_for': 5
        }

    device_prod_type_all_copilot_eligible_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="All CoPilot Eligible Devices"]',
            'wait_for': 5
        }

    # device_prod_type_more_link = \
    #     {
    #         'XPATH': '//a[@class="J-more" and @data-name="PRODUCT_TYPE_IDS"]',
    #         'wait_for': 2
    #     }

    device_prod_type_model_filter_chkbox = \
        {
            'XPATH': '//input[@data-name=',
            'wait_for': 5
        }

    device_prod_type_model_list = \
        {
            'XPATH': '//div[@data-automation-tag="automation-manage-device-list"]/descendant::td[contains(@class,"productType")]/div',
            'wait_for': 5
        }


    device_function_link = \
        {
            'XPATH': '//span[contains(text(),"Device Function") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_function_link_expanded = \
        {
            'XPATH': '//div[@aria-pressed="true"]//span[contains(text(),"Device Function") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_function_link_collapsed = \
        {
            'XPATH': '//div[@aria-pressed="false"]//span[contains(text(),"Device Function") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_function_access_point_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="Access Point"]',
            'wait_for': 5
        }

    device_function_switch_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="Switch"]',
            'wait_for': 5
        }

    device_function_xiqse_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="XIQSE"]',
            'wait_for': 5
        }

    device_function_all_filter_chkbox = \
        {
            'XPATH': '//input[@data-id="ALL_FUNCTIONS"]',
            'wait_for': 5
        }

    # device_function_filter_more_link = \
    #     {
    #         'XPATH': '//div[@data-name="Device Function"]//li/a',
    #         'wait_for': 2
    #     }


    device_data_management_link = \
        {
            'XPATH': '//span[contains(text(),"Device Management State") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_data_management_link_expanded = \
        {
            'XPATH': '//div[@aria-pressed="true"]//span[contains(text(),"Device Management State") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_data_management_link_collapsed = \
        {
            'XPATH': '//div[@aria-pressed="false"]//span[contains(text(),"Device Management State") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_data_management_managed_chkbox = \
        {
            'XPATH': '//input[@data-name="Managed"]',
            'wait_for': 5
        }

    device_data_management_unmanaged_chkbox = \
        {
            'XPATH': '//input[@data-name="Unmanaged"]',
            'wait_for': 5
        }

    device_data_management_new_chkbox = \
        {
            'XPATH': '//input[@data-name="New"]',
            'wait_for': 5
        }

    device_data_management_setting_up_chkbox = \
        {
            'XPATH': '//input[@data-name="Setting up"]',
            'wait_for': 5
        }

    device_data_management_all_chkbox = \
        {
            'XPATH': '//input[@data-id="ALL_DEVICE_MANAGEMENT_STATES"]',
            'wait_for': 5
        }

    device_all_devices_list = \
        {
            'XPATH': '//div[starts-with(@id,"dgrid")]/table/tr',
            'wait_for': 5
        }

    device_chk_list = \
        {
            'XPATH': '//div[@data-automation-tag="automation-manage-device-list"]/descendant::td[contains(@class,"elector")]/input',
            'wait_for': 5
        }

    action_managed_device_link = \
        {
            'XPATH': '//li[@data-automation-tag="automation-manage-device-actions-ap-manage-device"]/a',
            'wait_for': 5
        }

    action_close_dialog = \
        {
            'XPATH': '//span[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }

    action_unmanaged_device_link = \
        {
            'XPATH': '//li[@data-automation-tag="automation-manage-device-actions-ap-unmanage-device"]/a',
            'wait_for': 5
        }


    device_soft_ver_link = \
        {
            'XPATH': '//span[contains(text(),"Device Software Version") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_soft_ver_link_expanded = \
        {
            'XPATH': '//div[@aria-pressed="true"]//span[contains(text(),"Device Software Version") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_soft_ver_link_collapsed = \
        {
            'XPATH': '//div[@aria-pressed="false"]//span[contains(text(),"Device Software Version") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_soft_ver_all_chkbox = \
        {
            'XPATH': '//input[@data-id="ALL_DEVICE_SOFTWARE_VERSIONS"]',
            'wait_for': 5
        }

    device_soft_ver_chkbox = \
        {
            'XPATH': '//input[@data-name=',
            'wait_for': 5
        }

    device_soft_ver_chkbox_contains = \
        {
            'XPATH': '//input[contains(@data-name, ',
            'wait_for': 5
        }

    device_soft_ver_list = \
        {
            'XPATH': '//div[@data-automation-tag="automation-manage-device-list"]/descendant::td[contains(@class,"displayVer")]//div',
            'wait_for': 5
        }


    cloud_config_group_link = \
        {
            'XPATH': '//span[contains(text(),"Cloud Config Group") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    cloud_config_group_link_expanded = \
        {
            'XPATH': '//div[@aria-pressed="true"]//span[contains(text(),"Cloud Config Group") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    cloud_config_group_link_collapsed = \
        {
            'XPATH': '//div[@aria-pressed="false"]//span[contains(text(),"Cloud Config Group") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    cloud_config_group_all_checkbox = \
        {
            'XPATH': '//input[@data-id="ALL_CLOUD_CONFIG_GROUPS"]',
            'wait_for': 5
        }

    cloud_config_group_checkbox = \
        {
            'XPATH': '//input[@data-name=',
            'wait_for': 5
        }


    device_ssid_filter_link = \
        {
            'XPATH': '//span[contains(text(),"SSIDs") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_network_link = \
        {
            'XPATH': '//span[text() = "Network"]',
            'wait_for': 5
        }

    device_ssid_filter_chkbox = \
        {
            'XPATH': '//input[@data-name=',
            'wait_for': 5
        }

    device_ssid_all_filter_chkbox = \
        {   'XPATH' : '//input[@data-id="ALL_SSIDS"]',
            'wait_for' : 3
        }
    device_audit_status_link = \
        {
            'XPATH': '//span[contains(text(),"Device Audit Status") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_audit_all_filter_chkbox = \
        {
            'XPATH': '//input[@data-id="ALL_DEVICE_STATUS"]',
            'wait_for': 5
        }

    device_audit_config_match_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="Config Audit Match"]',
            'wait_for': 5
        }

    device_audit_config_mismatch_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="Config Audit Mismatch"]',
            'wait_for': 5
        }

    device_audit_config_overrride_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="Config Override"]',
            'wait_for': 5
        }

    device_user_profile_link = \
        {
            'XPATH': '//span[contains(text(),"User Profiles") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    device_default_guest_profile_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="default-guest-profile"]',
            'wait_for': 5
        }

    device_default_profile_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="default-profile"]',
            'wait_for': 5
        }

    device_user_profile_all_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="All" and @data-id="ALL_USER_PROFILES"]',
            'wait_for': 5
        }

    user_profiles_filter_link = \
        {
            'XPATH': '//span[contains(text(),"User Profiles") and @data-dojo-attach-point="titleNode"]',
            # 'XPATH': '//div[@data-name="Network Policies"]//h4',
            'wait_for': 5
        }

    user_profile_grid = \
        {
            'XPATH': '//*[@data-dojo-attach-point="filterByCtn"]//div[@id="honeycomb/ui/tree/HcTreeNode_56"]//div[@data-dojo-attach-point="containerNode"]/div//label[@class="checkbox"]',
            'wait_for': 5
        }

    checkbox = \
        {
            'CSS_SELECTOR': 'input.filter-loca-checked',
            'wait_for': 5
        }

    filter_by_title = \
        {
            'XPATH': '//span[@data-dojo-attach-point="titleNode" and contains(text(),"Filter By")]',
            'wait_for': 5
        }

    copilot_license_filter_link = \
        {
            'XPATH': '//span[contains(text(),"CoPilot") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    copilot_license_filter_link_expanded = \
        {
            'XPATH': '//div[@aria-pressed="true"]//span[contains(text(),"CoPilot") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    copilot_license_filter_link_collapsed = \
        {
            'XPATH': '//div[@aria-pressed="false"]//span[contains(text(),"CoPilot") and @data-dojo-attach-point="titleNode"]',
            'wait_for': 5
        }

    copilot_license_all_filter_chkbox = \
        {
            'XPATH': '//input[@data-id="ALL_COPILOT_LICENSE"]',
            'wait_for': 5
        }

    copilot_license_active_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="CoPilot Active"]',
            'wait_for': 5
        }

    copilot_license_expired_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="CoPilot Expired"]',
            'wait_for': 5
        }

    copilot_license_none_filter_chkbox = \
        {
            'XPATH': '//input[@data-name="CoPilot None"]',
            'wait_for': 5
        }
