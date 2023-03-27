class AccntMgmtWebElementsDefs:
    account_mgmt_grid_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="adminlistArea"]//table[@class="dgrid-row-table"]',
            'wait_for': 5
        }

    account_mgmt_grid_row_check_box = \
        {
            'CSS_SELECTOR': '.dgrid-selector',
            'wait_for': 5
        }

    account_mgmt_delete_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="adminlistArea"]//span[@data-tip="Delete"]',
            'wait_for': 5
        }

    account_mgmt_delete_conf_yes_button = \
        {
            'XPATH': '//div//button[@data-dojo-attach-point="confirmButton"]',
            'wait_for': 5
        }

    account_mgmt_add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="adminlistArea"]//span[@data-tip="Add"]',
            'wait_for': 5
        }

    account_mgmt_email_text = \
        {
            'XPATH': '//div//input[@data-dojo-attach-point="emailAddressInput"]',
            'wait_for': 5
        }

    account_mgmt_name_text = \
        {
            'XPATH': '//div//input[@data-dojo-attach-point="adminNameInput"]',
            'wait_for': 5
        }

    account_mgmt_organisation_sec = \
        {
            'XPATH': '//div[@data-dojo-attach-point="organizationSection"]',
            'wait_for': 5
        }

    account_mgmt_org_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="organizationSection"]'
                     '//div[@data-automation-tag="chzn-container-ctn"]',
            'wait_for': 5
        }

    account_mgmt_org_drop_down_opt = \
        {
            'XPATH': '//div[@data-dojo-attach-point="organizationSection"]//li',
            'wait_for': 5
        }

    account_mgmt_timeout = \
        {
            'XPATH': '//div//input[@data-dojo-attach-point="idleTimeoutInput"]',
            'wait_for': 5
        }

    account_mgmt_operator_radio_btn = \
        {
            'XPATH': '//*[@data-name="Operator"]',
            'wait_for': 5
        }

    administrator_role_radio_button = \
        {
            'XPATH': '//*[@data-name="Administrator"]',
            'wait_for': 5
        }

    operator_role_radio_button = \
        {
            'XPATH': '//*[@data-name="Operator"]',
            'wait_for': 5
        }

    application_operator_role_radio_button = \
        {
            'XPATH': '//*[@data-name="Operator"]',
            'wait_for': 5
        }

    monitor_role_radio_button = \
        {
            'XPATH': '//*[@data-name="Monitor"]',
            'wait_for': 5
        }

    help_desk_role_radio_button = \
        {
            'XPATH': '//*[@data-name="Help Desk"]',
            'wait_for': 5
        }

    guest_management_role_radio_button = \
        {
            'XPATH': '//*[@data-name="Guest Management"]',
            'wait_for': 5
        }

    observer_role_radio_button = \
        {
            'XPATH': '//*[@data-name="Observer"]',
            'wait_for': 5
        }

    account_mgmt_save_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="manageAdminUser"]//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    packet_capture = \
        {
            'XPATH': "//*[@data-automation-tag='automation-tools-controller-packet-capture-link']",
            'wait_for': 2
        }

    config_error = \
        {
            'CSS_SELECTOR': '.ui-tipbox-error',
            'wait_for': 2
        }
    Rbac_Assign_Location_checkbox = \
        {
            'XPATH': "//div[@class='lbl fn-ellipsis']"
        }

    credential_distribution_groups_add_button = \
        {
            'XPATH': "//*[@data-tip='Add']",
            'index': 2,
            'wait_for': 2
        }

    credential_distribution_groups_name_textfield = \
        {
            'XPATH': "//*[@data-dojo-attach-point='name']",
            'wait_for': 2
        }

    credential_distribution_groups_admin_account_dropdown = \
        {
            'XPATH': "//*[@data-automation-tag='automation-chzn-container-ctn']",
            'index': 8,
            'wait_for': 2
        }

    credential_distribution_groups_credential_restriction_checkbox = \
        {
            'XPATH': "//*[@data-dojo-attach-point='restrict']",
            'wait_for': 2
        }
    credential_distribution_groups_credential_restriction_count = \
        {
            'XPATH': "//*[@data-dojo-attach-point='number']",
            'wait_for': 2
        }

    credential_distribution_groups_registration_operation_checkbox = \
        {
            'XPATH': "//*[@data-dojo-attach-point='emailApproval']",
            'wait_for': 2
        }

    credential_distribution_groups_select_all_checkbox = \
        {
            'XPATH': "//*[@data-dojo-attach-point='selectAll']",
            'wait_for': 2
        }

    credential_distribution_groups_save_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='saveButton']",
            'wait_for': 2
        }

    credential_distribution_groups_active_directory_user_option = \
        {
            'XPATH': "//*[@data-automation-tag='Active_Directory_User']",
            'wait_for': 2
        }
    credential_distribution_groups_guest_management_role_user_option = \
        {
            'XPATH': "//*[@data-automation-tag='Guest_Management_Role_User']",
            'wait_for': 2
        }

    credential_distribution_groups_user_group_checkboxes_parent = \
        {
            'XPATH': "//*[@data-dojo-attach-point='employee']",
            'wait_for': 2
        }

    credential_distribution_groups_user_group_checkboxes = \
        {
            'XPATH': "//*[@class='checkbox']",
            'wait_for': 2
        }

    credential_distribution_groups_member_of_parent = \
        {
            'XPATH': "//*[@id='ah/util/layout/list/TextBoxList_1']",
            'wait_for': 2
        }

    credential_distribution_groups_member_of = \
        {
            'XPATH': "//*[@data-dojo-attach-point='inputEl']",
            'wait_for': 2
        }
