class AdvOnboardDefs:
    devices_add_button = \
        {
            'XPATH': '//*[@class="table-action-icons table-drop-add"]',
            'wait_for': 5
         }

    adv_onboard_add_menu_item = \
        {
            'XPATH': '//ul[@class="ui-menu-list"]//a[@type="advancedAdd"]',
            'wait_for': 5
        }

    onboard_icon = \
        {
            'XPATH': '//*[@data-automation-tag="automation-header-onboard"]',
            'wait_for': 5
        }

    real_devices_radio_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="realDevice"]//input[@name="realSimDevice"]',
            'wait_for': 5
        }

    add_dev_dev_type_sim = \
        {
            'XPATH': '//*[@data-dojo-attach-point="simDevice"]//input[@name="realSimDevice"]',
            'wait_for': 5
        }

    simulated_device_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="simDeviceContainer"]//div[@data-automation-tag="chzn-container-ctn"]//a',
            'wait_for': 5,
            'index': 0
        }

    simulated_device_drop_down_opts = \
        {
            'XPATH': '//div[@data-dojo-attach-point="simDeviceContainer"]//div[@data-automation-tag="chzn-container-ctn"]//li',
            'wait_for': 5,
            'index': 0
        }

    extreme_aerohive_device_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-welcome-onboard-aerohive"]',
            'wait_for': 5
        }

    add_dev_dell_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-welcome-onboard-dell"]',
            'wait_for': 5
        }

    exos_device_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-welcome-onboard-exos"]',
            'wait_for': 5
        }

    voss_device_tab = \
        {
            'XPATH': '//*[@data-automation-tag="automation-welcome-onboard-voss"]',
            'wait_for': 5
        }

    add_dev_wing_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-welcome-onboard-wing"]',
            'wait_for': 5
        }

    adv_serial_text_area = \
        {
            'XPATH': '//textarea[@data-automation-tag="automation-welcome-onboard-ap-serial"]',
            'wait_for': 5
        }

    add_dev_ext_aerohive_import_choose = \
        {
            'XPATH': '//*[contains(@id, "ah/util/dojocover/AHUploader_0") and contains(@class, "dijitReset dijitStretch dijitButtonContents")]',
            'wait_for': 5
        }

    add_dev_dell_service_tag = \
        {
            'XPATH': '//*[@data-automation-tag="automation-welcome-onboard-dell-service"]',
            'wait_for': 5
        }

    add_dev_dell_serial_num = \
        {
            'XPATH': '//*[@data-automation-tag="automation-welcome-onboard-dell-serial"]',
            'wait_for': 5
        }

    add_dev_dell_import_choose = \
        {
            'XPATH': '//*[contains(@class, "dijitReset dijitStretch dijitButtonContents") and contains(@id, "ah/util/dojocover/AHUploader_1")]',
            'wait_for': 5
        }

    exos_serial_text_area = \
        {
            'XPATH': '//*[@data-automation-tag="automation-welcome-onboard-exos-serial"]',
            'wait_for': 5
        }

    add_dev_exos_import_choose = \
        {
            'XPATH': '//*[contains(@class, "dijitReset dijitStretch dijitButtonContents") and contains(@id, "ah/util/dojocover/AHUploader_2")]',
            'wait_for': 5
        }

    add_dev_voss_sl_num_teat_area = \
        {
            'XPATH': '//*[@data-automation-tag="automation-welcome-onboard-voss-serial"]',
            'wait_for': 5
        }

    add_dev_voss_import_choose = \
        {
            'XPATH': '//*[contains(@class, "dijitReset dijitStretch dijitButtonContents") and contains(@id, "ah/util/dojocover/AHUploader_3")]',
            'wait_for': 5
        }

    add_dev_wing_sl_num = \
        {
            'XPATH': '//*[@data-automation-tag="automation-welcome-onboard-wing-serial"]',
            'waitt_for': 5
        }

    add_dev_wing_mac = \
        {
            'XPATH': '//*[@data-dojo-attach-point="txtWingMac"]',
            'wait_for': 5
        }

    onboard_next_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="nextButton"]',
            'wait_for': 5
        }

    assign_loc_ap_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-onboard-ap-location"]',
            'wait_for': 5,
            'index': 1
        }

    assign_loc_ap_button1 = \
        {
            'XPATH': '//*[@data-automation-tag="automation-real-onboard-ap-location"]',
            'wait_for': 5,
            'index': 0
        }

    assign_loc_switch_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-real-onboard-switch-location"]',
            'wait_for': 5
        }

    assign_loc_router_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-real-onboard-router-location"]',
            'wait_for': 5
        }

    assign_loc_vpn_gateway = \
        {
            'XPATH': '//*[@data-automation-tag="automation-real-onboard-gateway-location"]',
            'wait_for': 5
        }

    assign_loc_ap_grid_rows = \
        {
            'XPATH': '//table[@class="dojoxGridRowTable"]//tr',
            'wait_for': 5
        }

    assign_loc_ap_grid_checkbox = \
        {
            'CSS_SELECTOR': '.dojoxGridRowSelectorStatusText',
            'wait_for': 5
        }

    assign_loc_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-real-onboard-assign-location-btn"]',
            'wait_for': 5
        }

    location_nodes = \
        {
            'XPATH': '//div[@data-dojo-attach-point="mapTree"]//dd[contains(@class, "generic")]',
            'wait_for': 5
        }

    building_nodes = \
        {
            'XPATH': '//div[@data-dojo-attach-point="mapTree"]//dd[contains(@class, "building")]',
            'wait_for': 5
        }

    floor_nodes = \
        {
            'XPATH': '//div[@data-dojo-attach-point="mapTree"]//dd[contains(@class, "floor")]',
            'wait_for': 5
        }

    location_node_open_icon = \
        {
            'XPATH': '/span',
            'wait_for': 5
        }

    assign_loc_search_box = \
        {
            'XPATH': '//*[@class="search_app"]//input',
            'wait_for': 5
        }

    assign_loc_search_result = \
        {
            'XPATH': '//*[@class="folder-tree clearfix"]',
            'wait_for': 5
        }

    assign_loc_assign_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnAssign"]',
            'wait_for': 5
        }

    onboard_skip_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="skipButton"]',
            'wait_for': 5
        }

    onboard_finish_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="finishButton"]',
            'wait_for': 5
        }

    assign_branch_id_rounter_button = \
        {
            'XPATH': '//*[@class="ui-tab ui-tab-updated ui-tab-active clearfix"]//a[contains(text(), "Routers")]',
            'wait_for': 5
        }

    assign_branch_id_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cmdAssignBranchID"]',
            'wait_for': 5
        }

    create_nw_policy_new_policy_radio_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-welcome-onboard-new-policy"]',
            'wait_for': 5
        }

    create_nw_policy_use_existing_policy = \
        {
            'XPATH': '//*[@data-automation-tag="automation-welcome-onboard-existing-policy"]',
            'wait_for': 5
        }

    create_nw_policy_new_policy_name_input = \
        {
            'XPATH': '//*[@data-dojo-attach-point="policyName"]',
            'wait_for': 5
        }

    create_nw_policy_type_internal_check_box = \
        {
            'XPATH': '//*[@data-dojo-attach-point="internalSSID"]',
            'wait_for': 5
        }

    create_nw_policy_type_guest_check_box = \
        {
            'XPATH': '//*[@data-dojo-attach-point="guestAccessSSID"]',
            'wait_for': 5
        }

    create_nw_policy_use_existing_policy_dropdown = \
        {
            'XPATH': '//*[@data-automation-tag="automation-welcome-onboard-policy-select"]//a[@class="chzn-single"]',
            'wait_for': 5
        }

    create_nw_policy_use_existing_policy_list = \
        {
            'XPATH': '//*[@data-automation-tag="automation-welcome-onboard-policy-select"]//ul[@class="chzn-results "]//li',
            'wait_for': 5
        }

    conf_internal_ssid_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ssidName"]',
            'wait_for': 5
        }

    internal_ssid_secure_nw_radio_btn = \
        {
            'XPATH': '//*[contains(@class, "radio-btn-selected") and contains(text(), "Secure Network")]',
            'wait_for': 5
        }

    internal_ppsk_radio_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ppskRadio"]',
            'wait_for': 5
        }

    internal_ppsk_usr_grp_select_dropdown = \
        {
            'XPATH': '//*[@data-dojo-attach-point="userGroupSelect"]',
            'wait_for': 5
        }

    internal_ppsk_usr_grp_dropdown_opts = \
        {
            'XPATH': '//*[@data-dojo-attach-point="userGroupSelect"]//option',
            'wait_for': 5
        }

    internal_ppsk_bulk_usr_prefix = \
        {
            'XPATH': '//*[@data-dojo-attach-point="bulkPrefix"]',
            'wait_for': 5
        }

    internal_ppsk_bulk_user_guest_number = \
        {
            'XPATH': '//*[@data-dojo-attach-point="bulkGuestCount"]',
            'wait_for': 5
        }

    internal_ssid_psk_radio_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="pskRadio"]',
            'wait_for': 5
        }

    internal_ssid_psk_password = \
        {
            'XPATH': '//*[@data-dojo-attach-point="pskPasswordField"]',
            'wait_for': 5
        }

    internal_ssid_usr_credentials_radio_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enterpriseRadio"]',
            'wait_for': 5
        }

    internal_ssid_usr_cred_radius_server = \
        {
            'XPATH': '//*[@data-dojo-attach-point="radiusServerField"]',
            'wait_for': 5
        }

    internal_ssid_usr_cred_ip_addr = \
        {
            'XPATH': '//*[@data-dojo-attach-point="radiusIPAddressField"]',
            'wait_for': 5
        }

    internal_ssid_usr_cred_shared_secret = \
        {
            'XPATH': '//*[@data-dojo-attach-point="sharedSecretField"]',
            'wait_for': 5
        }

    internal_ssid_unsecure_nw_radio_btn = \
        {
            'XPATH': '//*[contains(@class, "radio-btn-selected") and contains(text(), "Unsecured (Open) Network")]',
            'wait_for': 5,
            'index': 0
        }

    internal_ssid_open_nw_open_access_radio_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="openRadio"]',
            'wait_for': 5
        }

    guest_ssid_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ssidName"]',
            'wait_for': 5,
            'index': 1
        }

    guest_ssid_unsecured_nw_radio_btn = \
        {
            'XPATH': '//*[contains(@class, "radio-btn-selected") and contains(text(), "Unsecured (Open) Network")]',
            'wait_for': 5,
            'index': 1
        }

    guest_ssid_guest_access_without_login_radio_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="openOptNoLogin"]',
            'wait_for': 5
        }

    conf_guest_ssid_open_nw_guest_accept_radio = \
        {
            'XPATH': '//*[@data-dojo-attach-point="openOptUseAccept"]',
            'wait_for': 5
        }

    conf_guest_ssid_secured_nw = \
        {
            'XPATH': '//*[contains(@class, "radio-btn-selected") and contains(text(), "Secure Network")]',
            'wait_for': 5
        }

    conf_guest_ssid_secured_nw_ppsk_radio = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ppskLogin"]',
            'wait_for': 5
        }

    conf_guest_ssid_secured_nw_ppsk_max_cli_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableMaxClientsPerPpsk"]',
            'wait_for': 5
        }

    conf_guest_ssid_secured_nw_ppsk_max_cli_input = \
        {
            'XPATH': '//*[@data-dojo-attach-point="maxClientsPerPpsk"]',
            'wait_for': 5
        }

    conf_guest_ssid_secured_nw_ppsk_mac_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableMacBind"]',
            'wait_for': 5
        }

    conf_guest_ssid_secured_nw_ppsk_mac_input = \
        {
            'XPATH': '//*[@data-dojo-attach-point="maxMacsPerPpsk"]',
            'wait_for': 5
        }

    conf_guest_ssid_secured_nw_psk_radio = \
        {
            'XPATH': '//*[@data-dojo-attach-point="pskPasswordOpt"]',
            'wait_for': 5
        }

    conf_guest_ssid_secured_nw_psk_cwp_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enablePskCwp"]',
            'wait_for': 5
        }

    conf_guest_ssid_secured_nw_psk_password = \
        {
            'XPATH': '//*[@data-dojo-attach-point="pskPassword"]',
            'wait_for': 5
        }

    summary_device_success = \
        {
            'XPATH': '//*[@class="WelcomeReviewSuccessfulDevices"]',
            'wait_for': 5
        }

    summary_device_fail = \
        {
            'XPATH': '//*[@class="WelcomeReviewFailedDevices"]',
            'wait_for': 5
        }

    summary_location = \
        {
            'XPATH': '//*[@class="WelcomeReviewNoLocation"]',
            'wait_for': 5
        }

    summary_network = \
        {
            'XPATH': '//*[@class="class="WelcomeReviewNetworkTable""]//tr',
            'wait_for': 5
        }

    summary_device_details_link = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deviceDetailsLink"]',
            'wait_for': 5
        }

    summary_device_details_success = \
        {
            'XPATH': '//*[@class="WelcomeReviewDeviceDetails"]//tr',
            'index': 0,
            'wait_for': 5
        }

    summary_device_details_failure = \
        {
            'XPATH': '//*[@class="WelcomeReviewDeviceDetails"]//tr',
            'index': 1,
            'wait_for': 5
        }

    add_dev_simulated_dev_model_dropdown = \
        {
            'XPATH': '//*[@data-dojo-attach-point="simChooseDeviceForms"]//a[@class="chzn-single"]//span[contains(text(), "ATOM")]',
            'wait_for': 5
        }

    add_dev_simulated_dev_model_list = \
        {
            'XPATH': '//*[@data-dojo-attach-point="simChooseDeviceForms"]//ul[@class="chzn-results "]//li',
            'wait_for': 5
        }

    add_dev_simulated_add_more_dev = \
        {
            'XPATH': '//*[@class="table-action-icons table-add"]',
            'index': 1,
            'wait_for': 5
        }

    adv_onboard_form_error = \
        {
            'CSS_SELECTOR': '.form-error',
            'wait_for': 5
        }
