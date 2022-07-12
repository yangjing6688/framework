class DeviceActionsDefs:
    device_actions_button = \
        {
            'DESC': 'Actions button in the XIQ > Manage Devices view.',
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-button"]',
            'wait_for': 2
        }

    device_actions_reboot_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-switch-reboot"]',
            'wait_for': 2
        }

    device_actions_assign_location = \
        {
            # The identifier differs depending on which type of device is selected (ap, switch, etc.),
            # so need to get all partial matches and select the displayed element
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-ap-assign-location"]',
            'wait_for': 5
        }

    device_actions_revert_device_to_template_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-switch-revert-template"]',
            'wait_for': 2
        }

    assign_devices_search_box = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-assign-location-search-field"]',
            'wait_for': 5
        }

    search_location_grid = \
        {
            'XPATH': '//*[@data-dojo-attach-point="mapTree"]',
            'wait_for': 5
        }

    assign_location_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnAssign"]',
            'wait_for': 5
        }

    locations_generic = \
        {
            'XPATH': '//*[@data-folder-type="GENERIC"]',
            'wait_for': 5
        }

    locations_building = \
        {
            'XPATH': '//*[@data-folder-type="BUILDING"]',
            'wait_for': 5
        }

    locations_floors = \
        {
            'XPATH': '//*[@data-folder-type="FLOOR"]',
            'wait_for': 5
        }

    assign_location_search_location = \
        {
            'XPATH': '//*[@data-folder-type="GENERIC"]',
            'wait_for': 5
        }

    assign_location_search_building = \
        {
            'XPATH': '//*[@data-folder-type="BUILDING"]',
            'wait_for': 5
        }

    assign_location_search_building_expand = \
        {
            'XPATH': '//*[@data-folder-type="BUILDING"]//span[@class="plan-leftnav oc-icon"]',
            'wait_for': 5
        }

    assign_location_search_floors = \
        {
            'XPATH': '//*[@data-folder-type="FLOOR"]',
            'wait_for': 5
        }

    device_actions__change_management_status = \
        {
            'XPATH': '//*[@class="ui-menu-list"]//a[@type="changeManagementStatus"]',
            'wait_for': 2
        }

    assign_location_select_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnSelect"]',
            'wait_for': 5
        }

    clear_audit_mismatch_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-ap-audit-mismatch"]',
            'wait_for': 2
        }

    device_location_ap_node = \
        {
            'CSS_SELECTOR': '.map-node',
            'wait_for': 5
        }

    device_location_floor_map_section = \
        {
            'XPATH': '//div[@data-dojo-attach-point="mapBackground"]',
            'wait_for': 5
        }

    multiple_device_reset_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-resetDevicetoDefaultMany"]',
            'wait_for': 5
        }

    reset_devices_to_default = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-utilities-reset-device-to-default"]',
            'wait_for': 5
        }

    single_device_reset_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-resetDevicetoDefault"]',
            'wait_for': 5
        }

    device_reset_dialog_yes_btn = \
        {
             'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
             'wait_for': 5
         }

    device_reset_close_dialog = \
        {
            'CSS_SELECTOR': '.device-utilities-icons.device-utilities-close',
            'XPATH': '//*[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }

    device_reset_dialog_box_msg = \
        {
            'XPATH': '//*[@class="device-utilities-page-body"]',
            'wait_for': 5
        }

    device_utilities = \
        {
            'XPATH': '//*[contains(@class, "btn btn-secondary-text") and contains(text(), "Utilities")]',
            'wait_for': 5
        }

    device_reset_warning_msg = \
        {
            'XPATH': '//*[@data-dojo-attach-point="msgWrap"]',
            'wait_for': 5
        }

    actions_update_version_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="importImageArea"]//div[@data-dojo-attach-point="templContainer"]//div[@data-automation-tag="chzn-container-ctn"]',
            'wait_for': 5,
        }

    actions_update_version_drop_down_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="importImageArea"]//div[@data-dojo-attach-point="templContainer"]//ul//li',
            'wait_for': 5
        }


    device_actions_manage_license = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-actions-manage-device-license"]',

            'wait_for': 2
        }


    activate_license = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-actions-manage-device-license-activate-license"]',
            'wait_for': 2
        }

    revoke_license = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-actions-manage-device-license-revoke-license"]',
            'wait_for': 2
        }

    act_premier_btn = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-actions-switch-activate-premier-license"]',
            'wait_for': 2
        }

    act_macsec_btn = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-actions-switch-activate-macsec-license"]',
            'wait_for': 2
        }

    rev_premier_btn = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-actions-switch-revoke-premier-license"]',
            'wait_for': 2
        }

    rev_macsec_btn = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-actions-switch-revoke-macsec-license"]',
            'wait_for': 2
        }

    yes_confirmation = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    act_10g_4p_btn = \
        {
            'XPATH': '//a[@type="activate4Port10gLicense"]',
            'wait_for': 2
        }

    act_10g_8p_btn = \
        {
            'XPATH': '//a[@type="activate8Port10gLicense"]',
            'wait_for': 2
        }

    rev_10g_4p_btn = \
        {
            'XPATH': '//a[@type="revoke4Port10gLicense"]',
            'wait_for': 2
        }

    rev_10g_8p_btn = \
        {
            'XPATH': '//a[@type="revoke8Port10gLicense"]',
            'wait_for': 2
        }

    warning_xiq_text = \
        {
            'XPATH': '//p[@data-automation-tag="automation-confirm-msg-activate10g"]',
            'wait_for': 2
        }

    warning_rvk_xiq_text = \
        {
            'XPATH': '//p[@data-automation-tag="automation-confirm-msg-revoke10g"]',
            'wait_for': 2
        }

    confirm_msg_yes = \
        {
            'XPATH': '//button[@data-automation-tag="automation-confirm-message-yes-button"]',
            'wait_for': 2
        }

    device_actions_change_management_status = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-actions-changemanagementstatus"]',
            'wait_for': 2
        }

    manage_device_btn = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-actions-switch-manage-device"]',
            'wait_for': 2
        }

    unmanage_device_btn = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-actions-switch-unmanage-device"]',
            'wait_for': 2
        }

    confirm_manage_btn_yes = \
        {
            'XPATH': '//button[@data-automation-tag="automation-confirm-message-yes-button"]',
            'wait_for': 2
        }

    confirm_manage_message_txt = \
        {
            'XPATH': '//div[@data-dojo-attach-point="mainContent"]',
            'wait_for': 2
        }

    close_message_btn = \
        {
            'XPATH': '//*[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 2
        }

    unmanage_msg_text = \
        {
            'XPATH': '//span[@data-dojo-attach-point="errorMsg"]',
            'wait_for': 2
        }

    change_os_actions_exos = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-actions-ap-os-exos"]',
            'wait_for': 5
        }

    change_os_actions_voss = \
        {
            'XPATH': '//a[@data-automation-tag="automation-manage-device-actions-ap-os-voss"]',
            'wait_for': 5
        }
