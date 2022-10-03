
class DeviceUpdateDefs:

    update_devices_button = \
        {
            'XPATH': '//span[@data-automation-tag="automation-manage-update-config"]',
            'wait_for': 5
        }

    update_nw_policy_and_config_checkbox = \
        {
            'NAME': 'updateNP',
            'wait_for': 5
        }

    delta_config_update_radio = \
        {
            'XPATH': '//*[@data-dojo-attach-point="update-delta" and @value="delta"]',
            'wait_for':10
        }

    complete_config_update_radio = \
        {
            'XPATH': '//*[@data-dojo-attach-point="update-complete" and @value="complete"]',
            'wait_for':10
        }

    upgrade_iq_engine_checkbox = \
        {
            'XPATH': '//input[@data-automation-tag="automation-config-download-options-update-hive-os"]',
            'wait_for': 5
        }

    upgrade_to_latest_version_radio = \
        {
            'XPATH': '//*[@data-dojo-attach-point="downloadFirmwareOption-latest"]',
            'wait_for': 2
        }

    upgrade_to_latest_version_label = \
        {
            'XPATH': '//*[@data-dojo-attach-point="downloadFirmwareOptionLatestDes"]',
            'wait_for': 2
        }

    upgrade_to_specific_version_radio = \
        {
            'XPATH': '//*[@data-dojo-attach-point="downloadFirmwareOption-specific"]',
            'wait_for': 2
        }

    upgrade_to_specific_version_dropdown = \
        {
            'XPATH': '//*[contains(@class,"upgrade-version-select")] //*[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 2
        }

    is_specific_version_dropdown_open = \
        {
            'XPATH': '//*[contains(@class,"upgrade-version-select")] //*[contains(@class,"chzn-single-with-drop")]',
            'wait_for': 2
        }

    xiq_upgrade_to_specific_version_dropdown = \
        {
            'XPATH': '//*[@data-dojo-attach-point="gridContent"]//*[@data-dojo-attach-point="templContainer"]',
            'wait_for': 2
        }

    upgrade_to_specific_version_dropdown_option = \
        {
            'TAG_NAME': 'option',
            'wait_for': 5
        }

    enable_distributed_image_upgrade_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableDistributedImageUpgrade"]',
            'wait_for': 5
        }

    upgrade_to_specific_version_add_remove_button = \
        {
            'XPATH': "//button[contains(text(), 'Add/Remove']",
            'wait_for': 2
        }

    upgrade_even_if_versions_same_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="forceDownloadImage"]',
            'wait_for': 2
        }
        
    upgrade_even_if_versions_same_checkbox_input = \
        {
            'XPATH': '//*[@data-dojo-attach-point="forceDownloadImage"]//input',
            'wait_for': 2
        }
       

    activate_at_next_reboot_radio = \
        {
            'XPATH': '//*[@data-dojo-attach-point="reboot-next"]',
            'wait_for': 2
        }

    activate_after_radio = \
        {
            'XPATH': '//*[@data-dojo-attach-point="reboot-sec"]',
            'wait_for': 2
        }

    activate_after_textfield = \
        {
            'XPATH': '//*[@data-dojo-attach-point="rebootAfter"]',
            'wait_for': 2
        }

    activate_at_time_radio = \
        {
            'XPATH': '//*[@data-dojo-attach-point="reboot-time"]',
            'wait_for': 2
        }

    activate_at_time_date_picker = \
        {
            'XPATH': '/html/body/div[2]/div[2]/div/div[1]/div/div[2]/ul/li[3]/div/div[1]/div[1]/input',
            'wait_for': 2
        }

    activate_at_time_date_picker_menu = \
        {
            'CSS_SELECTOR': '.widget_dijit_form_DateTextBox_2_dropdown',
            'wait_for': 5
        }

    activate_at_time_picker = \
        {
            'IMAGE': 'device_update_time_picker.PNG',
            'wait_for': 2
        }

    activate_at_time_picker_menu = \
        {
            'CSS_SELECTOR': '.widget_dijit_form_TimeTextBox_4_dropdown',
            'wait_for': 5
        }

    save_as_defaults_button = \
        {
            'XPATH': "//button[contains(text(), 'Save as Defaults']",
            'wait_for': 2
        }

    perform_update_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="uploadBtn"]',
            'wait_for': 2
        }

    time_pikcker_menu_item = \
        {
            'CSS_SELECTOR': '.dijitTimePickerItem',
            'wait_for': 5
        }

    activate_at_time_textfield = \
        {
            'XPATH': '//*[@data-validid="activeTime.focusNode"]',
            'wait_for': 5
        }

    activate_at_date_textfield = \
        {
           'XPATH': '//*[@data-validid="activeDate.focusNode"]',
           'wait_for': 5
        }

    upgrade_to_specific_version_dropdown_options = \
        {
            'XPATH': '//*[@data-dojo-attach-point="gridContent"]//*[@data-dojo-attach-point="templContainer"]//ul/li',
            'wait_for': 5
        }

    device_update_form_error = \
        {
            'CSS_SELECTOR': '.form-error',
            'wait_for': 5
        }

    device_update_form_error = \
    {
        'CSS_SELECTOR': '.form-error',
        'wait_for': 5
    }

    update_close_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 2
        }

    update_devices_button_from_d360 = \
        {
            'XPATH': '//*[@data-dojo-attach-point="deployNowBtn"]',
            'wait_for': 2
        }

    upgrade_IQ_engine_and_extreme_network_switch_images_checkbox = \
        {
            'XPATH': '//*[@data-automation-tag="automation-config-download-options-update-hive-os"]',
            'wait_for': 5
        }

    perform_upgrade_if_the_versions_are_the_same_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="forceDownloadImage"]',
            'wait_for': 5
        }

    config_download_options_checkbox = \
        {
            'XPATH': '//*[@data-automation-tag="automation-config-download-options-checkbox-network-policy-configuration"]',
            'wait_for': 5
        }

    config_download_options_checkbox = \
        {
            'XPATH': '//*[@data-automation-tag="automation-config-download-options-checkbox-network-policy-configuration"]',
            'wait_for': 5
        }

    upgrade_specific_firmware_drop_down_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="importImageArea"]//div[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 5
        }

    upgrade_specific_firmware_drop_down_items = \
        {
            'XPATH': '//ul[@class="chzn-results "]//li[contains(@class,"active-result")]',
            'wait_for': 2
        }
