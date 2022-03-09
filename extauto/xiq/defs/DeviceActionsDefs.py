class DeviceActionsDefs:
    device_actions_button = \
        {
            # The XPATH value for the ACTIONS button was updated in XIQ 22.1.20.x
            # Previous XPATH value:
            # 'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-actions_normal-btn"]',
            'DESC': 'Actions button in the XIQ > Manage Devices view.',
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-button"]',
            'wait_for': 2
        }

    device_actions_reboot_menu_item = \
        {
            'XPATH': '//*[@data-automation-tag="automation-manage-device-actions-ap-reboot"]',
            'wait_for': 2
        }

    device_actions_assign_location = \
        {
            # The identifier differs depending on which type of device is selected (ap, switch, etc.),
            # so need to get all partial matches and select the displayed element
            'XPATH': '//li[contains(@data-automation-tag, "automation-manage-device-actions-") and contains(@data-automation-tag,"-assign-location")]',
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
            'XPATH': '//*[@class="ui-menu ui-menu-medium ui-menu-rt"]//a[contains(text(), "Reset Device to Default")]',
            'index': 3,
            'wait_for': 5
        }

    single_device_reset_button = \
        {
            'XPATH': '//*[@class="ui-menu ui-menu-medium ui-menu-rt"]//a[contains(text(), "Reset Device to Default")]',
            'index': 0,
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
            'XPATH': '//li[@data-automation-tag="automation-manage-device-actions-manage-device-license"]',
            'wait_for': 2
        }

    activate_license = \
        {
            'XPATH': '//li[@data-automation-tag="automation-manage-device-actions-manage-device-license-activate-license"]',
            'wait_for': 2
        }

    revoke_license = \
        {
            'XPATH': '//li[@data-automation-tag="automation-manage-device-actions-manage-device-license-revoke-license"]',
            'wait_for': 2
        }

    act_premier_btn = \
        {
            'XPATH': '//li[@data-automation-tag="automation-manage-device-actions-manage-device-license"]//a[@type="activatePremierLicense"]',
            'wait_for': 2
        }

    act_macsec_btn = \
        {
            'XPATH': '//li[@data-automation-tag="automation-manage-device-actions-manage-device-license"]//a[@type="activateMacsecLicense"]',
            'wait_for': 2
        }

    rev_premier_btn = \
        {
            'XPATH': '//li[@data-automation-tag="automation-manage-device-actions-manage-device-license"]//a[@type="revokePremierLicense"]',
            'wait_for': 2
        }

    rev_macsec_btn = \
        {
            'XPATH': '//li[@data-automation-tag="automation-manage-device-actions-manage-device-license"]//a[@type="revokeMacsecLicense"]',
            'wait_for': 2
        }

    yes_confirmation = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }



