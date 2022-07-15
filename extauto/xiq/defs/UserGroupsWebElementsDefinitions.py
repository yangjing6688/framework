class UserGroupsWebElementsDefinitions:
    user_groups_grid_rows = \
        {
            'XPATH': '//div[@data-automation-tag="automation-user-groups-grid"]//table[@class="dgrid-row-table"]',
            
         }
    user_group_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 15
        }

    user_management_side_menu = \
        {
            'XPATH': '//div[@data-automation-tag="automation-header-label-User-Management"]',
            'wait_for': 5
        }

    user_group_side_nav_item = \
        {
            'XPATH': "//*[@data-automation-tag='automation-sider-list-usergroups']",
            'wait_for': 5
        }

    user_group_add_button = \
        {
            'XPATH': '//div[@data-automation-tag="automation-user-groups-grid"]//span[@data-tip="Add"]',
            'wait_for': 5
         }
    deutcshe_user_group_add_button = \
        {
            'XPATH': '//div[@data-automation-tag="automation-user-groups-grid"]//span[@data-tip="Hinzufügen"]',
            'wait_for': 5
         }

    user_group_name_field = \
        {
            'XPATH': '//*[@data-automation-tag="automation-user-group-name"]',
            'wait_for': 5
        }

    password_db_loc_drop_down_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-password-db-location-chzn-arrow-down"]',
            'wait_for': 5
        }

    password_db_loc_drop_down_items = \
        {
            'XPATH': '//div[@data-automation-tag="automation-password-db-location-chzn-drop-ctn"]//ul//li',
            'wait_for': 5
        }

    password_type_drop_down_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-security-type-chzn-arrow-down"]',
            'wait_for': 5
        }

    password_type_drop_down_items = \
        {
            'XPATH': '//*[@data-automation-tag="automation-security-type-chzn-container-ctn"]//ul/li',
            'wait_for': 5
        }

    max_num_of_clients_per_ppsk_check_box = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableMaxClientsPerPpskUserGroup"]',
            'wait_for': 5
        }

    max_num_of_clients_per_ppsk_input_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="maxClientsPerPpskUserGroup"]',
            'wait_for': 5
        }

    input_field_form_error = \
        {
            "CLASS_NAME": "form-error",
            'wait_for': 5
        }

    ppsk_classification_use_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ppskUseOnly"]',
            'wait_for': 5
        }

    cwp_register_check_box = \
        {
            'XPATH': '//div[@data-dojo-attach-point="enableSelfRegDisplay"]'
                     '//input[@data-dojo-attach-point="enableSelfReg"]',
            'wait_for': 5
        }
    pcg_use_checkbox = \
        {
            'XPATH': '//*[@data-dojo-attach-point="pcgUseOnly"]',
            'wait_for': 5
        }

    ap_based_radio_button = \
        {
            'XPATH': '//*[@id="apBasedPCG"]',
            'wait_for': 5
        }

    key_based_radio_button = \
        {
            'XPATH': '//*[@id="keyBasedPCG"]',
            'wait_for': 5
        }

    add_user_toggle_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="usersToggle"]//h3',
            'wait_for': 5
        }

    single_user_add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="usersContent"]//span[contains(@class, "table-add")]',
            'wait_for': 1,
         }

    guest_mgmt_account_single_usr_add_button = \
        {
            'XPATH': '//div[@data-automation-tag="automation-users-grid"]//span[@data-tip="Add"]',
            'wait_for': 1,
        }

    bulk_user_add_button = \
        {
            'CSS_SELECTOR': '.table-action-buttons.table-action-icons.table-bulkCreate',
            'wait_for': 1
        }

    bulk_create_users_username_prefix = \
        {
            'XPATH': '//div/input[@data-dojo-attach-point="bulkPrefix"]',
            'wait_for': 5
        }

    bulk_create_users_number_of_accounts = \
        {
            'XPATH': '//div/input[@data-dojo-attach-point="bulkCount"]',
            'wait_for': 5
        }

    bulk_create_users_email_user_account_info_to = \
        {
            'XPATH': '//div/input[@data-dojo-attach-point="emailAccountsTo"]',
            'wait_for': 5
        }

    bulk_create_users_done_button = \
        {
            'XPATH': '//div/button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 1
        }

    bulk_create_users_cancel_button = \
        {
            'XPATH': '//div[@class="bulk-create"]//button[@data-dojo-attach-point="cancelBtn"]',
            'wait_for': 1
        }

    user_group_save_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-user-group-save']",
            'wait_for': 5
        }

    user_group_delete_button = \
        {
            'XPATH': '//div[@data-automation-tag="automation-user-groups-grid"]//span[@data-tip="Delete"]',
            'wait_for': 1
        }

    user_group_delete_confirm_yes_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    single_user_name_text_field = \
        {
            'XPATH': '//input[@data-dojo-attach-point="name"]',
            'wait_for': 5
        }

    single_user_org_text_field = \
        {
            'XPATH': "//div[@data-dojo-attach-point='organizationDisp']//input[@data-dojo-attach-point='organization']",
            'wait_for': 5
        }

    single_user_purpose_of_visit_field = \
        {
            'XPATH': "//input[@data-dojo-attach-point='purpose']",
            'wait_for': 5
        }

    single_user_email_address_field = \
        {
            'XPATH': "//input[@data-dojo-attach-point='email']",
            'wait_for': 5
        }
    single_user_country_code_drop_down_section = \
        {
            'CSS_SELECTOR': ".column.last",
            'wait_for': 5,
            'index': 5
        }

    single_user_country_code_drop_down = \
        {

            'XPATH': '//div[@data-dojo-attach-point="phoneContainer"]/div',
            'wait_for': 5,
        }

    single_user_country_code_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="phoneContainer"]//li[contains(@class, "active-result")]',
            'wait_for': 5
        }

    single_user_phone_number = \
        {
            'XPATH': '//div[@data-dojo-attach-point="phoneContainer"]/input[@data-dojo-attach-point="phone"]',
            'wait_for': 5
        }

    single_user_user_name_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="userNameSelectContainer"]'
                     '//div[@data-automation-tag="automation-chzn-container-ctn"]',
            'wait_for': 5,
        }

    single_user_user_name_items = \
        {
            'XPATH': '//div[@data-dojo-attach-point="userNameSelectContainer"]//li[contains(@class,"active-result")]',
            'wait_for': 5
        }

    single_user_password_field = \
        {
            'XPATH': '//div[contains(@class, "idm-user-password")]//input[@data-dojo-attach-point="norEl"]',
            'wait_for': 5
        }

    single_user_password_generate_button = \
        {
            'XPATH': '//div[contains(@class, "idm-user-password")]//button[@data-dojo-attach-point="genBtn"]',
            'wait_for': 5
        }

    single_user_description = \
        {
            'XPATH': "//*[@data-dojo-attach-point='desc']",
            'wait_for': 5
        }

    single_user_create_done_button = \
        {
            'XPATH': '//div/button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 1
        }

    single_user_create_cancel_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="containerNode"]//button[@data-dojo-attach-point="cancelBtn"]',
            'wait_for': 1
        }

    single_user_create_text_field_error = \
        {
            'XPATH': '//div[@class="ui-dialog-content"]//span[@class="form-error"]',
            'wait_for': 1
        }

    bulk_user_create_text_field_error = \
        {
            'XPATH': '//div[@class="bulk-create"]//span[@class="form-error"]',
            'wait_for': 1
        }

    single_user_deliver_password_check_box = \
        {
            'XPATH': "//input[@data-dojo-attach-point='deliver-email']",
            'wait_for': 5
        }

    single_user_deliver_password_field = \
        {
            'XPATH': "//input[@data-dojo-attach-point='dEmail']",
            'wait_for': 5
        }

    user_group_text_field_form_error = \
        {
            'XPATH': '//div[@data-dojo-attach-point="ugCtn"]//span[@class="form-error"]',
            'wait_for': 5
        }

    page_size_element = \
        {
            'CSS_SELECTOR': '.J-page-size.ui-page-size',
            'wait_for': 2
        }

    wireless_user_group_select_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="userGroups"]//span[@data-tip="Select"]',
            'wait_for': 5
        }

    wireless_user_group_select_window_group_rows = \
        {
            'XPATH': '//div[@data-automation-tag="automation-reusable-grid"]//table[@class="dojoxGridRowTable"]',
            'wait_for': 5
        }

    wireless_usr_grp_select_wind_grp_row_check_box = \
        {
            'CSS_SELECTOR': '.dojoxGridRowSelector',
            'wait_for': 5
        }

    wireless_usr_grp_select_wind_select_button = \
        {
            'XPATH': '//button[@data-automation-tag="automation-dialog-link"]',
            'wait_for': 5
        }

    wireless_usr_grp_select_wind_cancel_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="containerNode"]//button[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5
        }

    wireless_usr_grp_select_wind_local_tab = \
        {
            'XPATH': '//div[@data-dojo-attach-point="containerNode"]//div[contains(@class, "ui-tab")]//a',
            'wait_for': 5,
            'index': 0
        }

    wireless_usr_grp_select_wind_cloud_tab = \
        {
            'XPATH': '//div[@data-dojo-attach-point="containerNode"]//div[contains(@class, "ui-tab")]//a',
            'wait_for': 5,
            'index': 1
        }

    wireless_usr_group_add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="userGroups"]//span[@data-tip="Add"]',
            'wait_for': 5
        }

    guest_mgmt_account_create_acct_user_grp_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="templContainer"]//div[@data-automation-tag="chzn-container-ctn"]',
            'wait_for': 5,
            'index':1
        }

    add_user_button_users_sub_tab = \
        {
            'XPATH': '//div[@class="user-mgmt-filters"]//span[@data-tip="Add"]',
            'wait_for': 5
        }

    select_user_group_from_dropdown = \
        {
            'XPATH': '//div[@class="idm-user-container"]//div[@data-dojo-attach-point="templContainer"]//ul'
                     '[@data-automation-tag="chzn-results-ctn"]//li',
            'wait_for': 5
        }

    user_group_dropdown = \
        {
            'XPATH': '//div[@class="last column"]//div[@data-dojo-attach-point="templContainer"]',
            'wait_for': 5
        }

    users_subtab_user_row = \
        {
            'XPATH': '//div[@class="idm-management"]//div[@role="row"]',
            'wait_for': 5
        }

    username_in_users_subtab = \
        {
            'CSS_SELECTOR': ".dgrid-cell.dgrid-column-1.field-name",
            'wait_for': 5
        }

    select_user_in_users_subtab = \
        {
            'CSS_SELECTOR': ".dgrid-cell.dgrid-column-0.w30.dgrid-selector",
            'wait_for': 5
        }

    delete_user_from_users_subtab = \
        {
            'XPATH': '//div[@class="idm-management"]//span[@data-tip="Delete"]',
            'wait_for': 5
        }

    edit_user_from_users_subtab = \
        {
            'XPATH': '//div[@class="idm-management"]//span[@data-tip="Edit"]',
            'wait_for': 5
        }

    user_delete_confirm_yes_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="confirmButton"]',
            'wait_for': 5
        }

    wireless_user_profile_select_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-user-access-select-user-profile-btn"]',
            'wait_for': 5
        }

    wireless_user_profile_select_window_group_rows = \
        {
            'XPATH': '//div[@componentpath="SelectUserProfiles"]//table[@class="dojoxGridRowTable"]',
            'wait_for': 5
        }

    wireless_usr_profile_select_wind_grp_row_check_box = \
        {
            'CSS_SELECTOR': '.dojoxGridRowSelector',
            'wait_for': 5
        }

    wireless_usr_profile_select_wind_select_button = \
        {
            'XPATH': '//div[@componentpath="SelectUserProfiles"]//button[@data-dojo-attach-point="selectButton"]',
            'wait_for': 5
        }

    wireless_usr_profile_select_wind_cancel_button = \
        {
            'XPATH': '//div[@componentpath="SelectUserProfiles"]//button[@data-dojo-attach-point="cancelButton"]',
            'wait_for': 5
        }

    usr_group_select_all_checkbox = \
        {
            'XPATH': '//*[contains(@id,"dgrid")]//tr//th//input',
            'wait_for': 5
        }

    ssid_user_group_item = \
        {
            'CSS_SELECTOR': '.J-auth-con.ssid-user-group-ctn',
            'wait_for': 5
        }
