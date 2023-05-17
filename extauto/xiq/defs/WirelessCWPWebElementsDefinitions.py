class WirelessCWPWebElementsDefinitions:

    enable_captive_web_portal_slide_button = \
        {
            'XPATH': '//div/input[@data-dojo-attach-point="enableCwp"]',
            'wait_for': 5
        }

    enable_extreme_guest_essentials_slide_button = \
        {
            'XPATH': '//div/input[@data-dojo-attach-point="enableAdvGuest"]',
            'wait_for': 5
        }

    walled_garden_add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="advGuestWalledGarden"]//span[@data-tip="Add"]',
            'wait_for': 5
        }

    walled_garden_text_area = \
        {
            'XPATH': '//*[@data-dojo-attach-point="advGuestAddGardenDefaultData"]',
            'wait_for': 5
        }

    walled_garden_text_add_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="advGuestAddGardenBtn"]',
            'wait_for': 5
        }

    cloud_captive_web_portal_radio_button = \
        {
            'XPATH': '//div/input[@data-dojo-attach-point="cloudCwpBtn"]',
            'wait_for': 5
        }

    cloud_cwp_social_login_radio_button = \
        {
            'XPATH': '//div/input[@data-dojo-attach-point="cloudCwpBtnSplashSocial"]',
            'wait_for': 5
        }

    default_cwp_add_button = \
        {
            'XPATH': '//div//button[@data-dojo-attach-point="addCWP"]',
            'wait_for': 5
        }

    default_cwp_edit_link = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cwpLink"]',
            'wait_for': 5
        }

    default_cwp_add_dialog_window = \
        {
            'CSS_SELECTOR': '.hmOverride.dijitDialog',
            'wait_for': 5
        }

    default_cwp_name_field = \
        {
            'XPATH': '//div[contains(@class, "cwp-name-ctn")]//input[@data-dojo-attach-point="cwpName"]',
            'wait_for': 5
        }

    cwp_auth_method_dropdown = \
        {
            'XPATH': '//*[@data-dojo-attach-point="dynamic-auth"]//*[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 5
        }

    cwp_auth_method_dropdown_options = \
        {
            'XPATH': '//*[@data-dojo-attach-point="dynamic-auth"]//*[@data-automation-tag="automation-chzn-results-ctn"]/li',
            'wait_for': 5
        }

    open_template_cloud_cwp_restrict_domain = \
        {
            'XPATH': '//div//input[@data-dojo-attach-point="cloudCwpAllowDomains"]',
            'wait_for': 5
        }

    open_template_cloud_cwp_cache_duration = \
        {
            'XPATH': '//div//input[@data-dojo-attach-point="cloudCwpCacheDuration"]',
            'wait_for': 5
        }

    default_cwp_add_dialog_save_cwp_button = \
        {
            'XPATH': '//div//button[@data-dojo-attach-point="saveButton" and contains(text(), "Save CWP")]',
            'wait_for': 5
        }

    default_cwp_add_dialog_cancel_cwp_button = \
        {
            'XPATH': '//div[@class="cwp-create-ctn"]//button[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5
        }

    cwp_dialog_window_cancel_button = \
        {
            'XPATH': '//div[contains(@class, "ui-dialog-bottom")]//button[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5,
        }

    default_cwp_select_button = \
        {
            'XPATH': '//div//button[@data-dojo-attach-point="reuseCWP"]',
            'wait_for': 5
        }

    default_cwp_select_dialog_window = \
        {
            'CSS_SELECTOR': '.hmOverride.dijitDialog',
            'wait_for': 1
        }

    default_select_window_cwp_rows = \
        {
            'XPATH': '//div[@data-automation-tag="automation-reusable-grid"]//table[@class="dojoxGridRowTable"]',
            
        }

    default_cwp_select_window_select_button = \
        {
            'XPATH': '//div//button[@data-automation-tag="automation-dialog-link"]',
            'wait_for': 5
        }

    default_cwp_select_window_cancel_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="containerNode"]//button[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5
        }

    default_cwp_select_window_row_select_check_box = \
        {
            'CSS_SELECTOR': '.dojoxGridRowSelector',
            'wait_for': 5
        }

    cloud_cwp_social_login_type_facebook = \
        {
            'XPATH': '//*[@data-dojo-attach-point="facebook"]',
            'wait_for': 5
        }

    cloud_cwp_name_field = \
        {
            'XPATH': '//*[@id="name"]',
            'wait_for': 1
        }

    cloud_cwp_social_login_type_google = \
        {
            'XPATH': '//*[@data-dojo-attach-point="google"]',
            'wait_for': 5
        }

    cloud_cwp_social_login_type_linkedin = \
        {
            'XPATH': '//*[@data-dojo-attach-point="linkedin"]',
            'wait_for': 5
        }

    captive_web_portal_radio_button = \
        {
            'XPATH': '//div/input[@data-dojo-attach-point="localCwpBtn"]',
            'wait_for': 5
        }

    user_auth_on_captive_web_portal = \
        {
            'XPATH': '//*[@data-dojo-attach-point="inputEl"]',
            'wait_for': 1,
            'index': 0
        }

    enable_self_registration = \
        {
            'XPATH': '//*[@data-dojo-attach-point="inputEl"]',
            'wait_for': 1,
            'index': 1
        }

    return_aerohive_private_psk = \
        {
            'XPATH': '//*[@data-dojo-attach-point="inputEl"]',
            'wait_for': 1,
            'index': 2
        }

    enable_upa = \
        {
            'XPATH': '//*[@data-dojo-attach-point="inputEl"]',
            'wait_for': 1,
            'index': 3
        }

    cloud_cwp_request_pin_radio_button = \
        {
            'NAME': 'cwpCloudOption',
            'index': 1,
            'wait_for': 1
        }

    cloud_cwp_add_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="addCWP"]',
            'CLASS_NAME': 'btn-add',
            'wait_for': 1
        }

    cloud_cwp_save_cwp_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveButton"]',
            'index': 1,
            'wait_for': 1
        }

    cloud_cwp_cancel_cwp_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 1
        }

    employee_approval_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="approval"]',
            'wait_for': 5
        }

    ppsk_setting_div = \
        {
            'XPATH': '//*[@data-dojo-attach-point="spec-enableReturnPpsk"]',
            'wait_for': 1
        }

    choose_access_ssid_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="spec-enableReturnPpsk"]//a',
            'index': 0,
            'wait_for': 5,
        }

    choose_access_ssid_options = \
        {
            'XPATH': '//div[@data-dojo-attach-point="spec-enableReturnPpsk"]//li',
            'wait_for': 5
        }

    choose_a_ppsk_server_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="spec-enableReturnPpsk"]//a',
            'wait_for': 5,
            'index': 1
        }

    choose_a_ppsk_server_options = \
        {
            'XPATH': '//div[@data-dojo-attach-point="spec-enableReturnPpsk"]//li',
            'wait_for': 5,
        }

    approve_email_domain_list_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="domainCtn"]//table[@class="dgrid-row-table"]',
            'wait_for': 5
        }

    approve_email_domain_list_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            
        }

    approve_email_domain_list_add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="domainCtn"]//span[@class="table-action-icons table-add"]',
            
        }

    approve_email_domain_list_delete_button = \
        {
            'CSS_SELECTOR': '.table-action-icons.table-remove',
            
        }

    approve_email_domain_list_domain_name = \
        {
            'XPATH': '//div[@data-dojo-attach-point="spec-enableSelfRegistration,selfReg"]'
                     '//input[@data-dojo-attach-point="dName"]',
            'wait_for': 5,
        }

    approve_email_domain_list_domain_add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="spec-enableSelfRegistration,selfReg"]'
                     '//button[@data-dojo-attach-point="addBtn"]',
            'wait_for': 5
        }

    request_pin_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="cloudCwpBtnRequestPIN"]',
            'wait_for': 5
        }

    valid_pin_time_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="cloudCwpContainerRqPinFinal"]'
                     '//div[@data-automation-tag="automation-chzn-arrow-down"]',
            
            'index': 0
        }

    valid_pin_time_drop_down_options = \
        {
            'XPATH': '//ul[contains(@class, "qa-chzn-results-pinvalidtime")]//li',
            
        }

    email_address_daily_report_field = \
        {
            'XPATH': '//div//input[@data-dojo-attach-point="emailAddressForDailyReport"]',
            'wait_for': 5
        }

    daily_report_delivery_time_hour = \
        {
            'XPATH': '//div[@data-dojo-attach-point="cloudCwpContainerRqPinFinal"]'
                     '//div[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 5,
            'index': 1
        }

    daily_report_delivery_time_hour_options = \
        {
            'XPATH': '//ul[contains(@class, "qa-chzn-results-dailyreportdeliverytimehour")]//li',
            
        }

    daily_report_delivery_time_minutes = \
        {
            'XPATH': '//div[@data-dojo-attach-point="cloudCwpContainerRqPinFinal"]'
                     '//div[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 5,
            'index': 2
        }

    daily_report_delivery_time_minutes_options = \
        {
            'XPATH': '//ul[contains(@class, "qa-chzn-results-dailyreportdeliverytimeminute")]//li',
            
        }

    customise_cwp_setting = \
        {
            'XPATH': '//div//input[@data-dojo-attach-point="cloudCwpCustomizeSwitch"]',
            'wait_for': 5
        }

    create_web_file_directory_button = \
        {
            'XPATH': '//div//button[@data-dojo-attach-point="createWebFileDirectory"]',
            'wait_for': 5
        }

    directory_name = \
        {
            'XPATH': '//div//input[@data-dojo-attach-point="createDirField"]',
            'wait_for': 5
        }

    web_file_directory_create_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="createButton"]',
            'wait_for': 5,
        }

    web_file_directory_create_done_button = \
        {
            'XPATH': '//div[contains(@class, "CreateFileDirectoy")]//button[@data-dojo-attach-point="doneButton"]',
            'wait_for': 5,
        }

    web_file_directory_remove_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="removeButton"]',
            'wait_for': 1,
        }

    web_file_directory_page_list = \
        {
            'XPATH': '//*[@data-dojo-attach-point="pageList"]',
            'wait_for': 1,
        }

    web_file_directory_drop_down = \
        {
            'XPATH': '//div[@class="field-ctn web-file-dir"]//div[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 5,
        }

    web_file_directory_drop_down_options = \
        {
            'XPATH': '//ul[contains(@class, "qa-chzn-results-webfiledirectory")]//li',
            
        }

    manage_upload_remove_files_button = \
        {
            'XPATH': '//div//button[@data-dojo-attach-point="uploadFiles"]',
            'wait_for': 1
        }

    manage_file_choose_field = \
        {
            'XPATH': '//div[@data-dojo-attach-point="importFileUploader"]//input[@name="file"]',
            'wait_for': 5
        }

    manage_file_choose_done_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="doneButton"]',
            'wait_for': 5
        }

    manage_file_choose_remove_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="removeButton"]',
            'wait_for': 5,
        }

    customise_login_page_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="loginPageCtn"]//div[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 5,
        }

    customise_login_page_drop_down_option = \
        {
            'XPATH': '//ul[contains(@class, "qa-chzn-results-loginpageselect")]//li',
            
        }

    customise_success_page_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="successPageCtn"]//div[@data-automation-tag="automation-chzn-arrow-down"]',
            'wait_for': 5
        }

    customise_success_page_drop_down_options = \
        {
            'XPATH': '//ul[contains(@class, "qa-chzn-results-successpageselect")]//li',
            'wait_for': 5
        }

    cwp_wireless_network_save_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="wirelessDetailsContentArea"]'
                     '//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5,
        }

    customise_and_preview_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="cwpCustomizeBtn"]',
            'wait_for': 5
        }

    auth_method_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="dynamic-auth"]//div[@data-automation-tag="chzn-container-ctn"]',
            'wait_for': 5
        }

    auth_method_drop_down_options = \
        {
            'XPATH': '//div[@data-dojo-attach-point="dynamic-auth"]'
                     '//div[@data-automation-tag="chzn-container-ctn"]//ul//li',
            'wait_for': 5
        }

    wir_auth_with_extiq_auth_service_slider_button = \
        {
            'XPATH': '//div//input[@data-dojo-attach-point="enableIdm"]',
            'wait_for': 5
        }

    import_html_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="cwpImportBtn"]',
            'wait_for': 10
        }

    user_auth_return_ppsk_link = \
        {
            'XPATH': '//div[@data-dojo-attach-point="cwpDownloadSample"]'
                     '//a[@data-dojo-attach-point="importDownloadLink"]',
            'wait_for': 10
        }

    wireless_network_cancel_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="wirelessDetailsContentArea"]'
                     '//button[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5,
        }

    cwp_error_message = \
        {
            'CSS_SELECTOR': '.ui-tipbox.ui-tipbox-error',
            'wait_for': 5
        }

    failure_page_container = \
        {
            'XPATH': '//div[@data-dojo-attach-point="failurePageCtn"]',
            'wait_for': 5
        }
