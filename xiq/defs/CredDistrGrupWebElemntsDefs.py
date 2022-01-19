class CredDistrGrupWebElemntsDefs:

    cred_distr_grps_grid_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="employeeGroupsListContainer"]//table[@class="dgrid-row-table"]',
            'wait_for': 5
        }

    cred_distr_grps_grid_row_check_box = \
        {
            'CSS_SELECTOR': '.dgrid-selector',
            'wait_for': 5
        }

    cred_distr_grps_row_delete_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="employeeGroupsListContainer"]//span[@data-tip="Delete"]',
            'wait_for': 5
        }

    cred_distr_grps_row_delete_confirm_yes_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 5
        }

    cred_distr_grps_add_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="employeeGroupsListContainer"]//span[@data-tip="Add"]',
            'wait_for': 5
        }

    cred_distr_grps_name_field = \
        {
            'XPATH': '//input[@data-dojo-attach-point="name"]',
            'wait_for': 5
        }

    cred_distr_grps_admin_acct_drop_down = \
        {
            'XPATH': '//div[@data-dojo-attach-point="manageEmployeeGroup"]'
                     '//div[@data-automation-tag="chzn-container-ctn"]/a',
            'wait_for': 5
        }

    cred_distr_grps_admin_acct_drop_down_opts = \
        {
            'XPATH': '//div//ul[contains(@class, "qa-chzn-results-adminaccount")]//li',
            'wait_for': 5
        }

    cred_distr_member_of_text_field = \
        {
            'XPATH': '//div[@data-dojo-attach-point="memberofDisp"]//input[@data-dojo-attach-point="inputEl"]',
            'wait_for': 5
        }

    cred_distr_guest_mgmt_usr_text_field = \
        {
            'XPATH': '//div[@data-dojo-attach-point="guestManagementUserDisp"]'
                     '//input[@data-dojo-attach-point="inputEl"]',
            'wait_for': 5
        }

    cred_restriction_check_box = \
        {
            'XPATH': '//input[@data-dojo-attach-point="restrict"]',
            'wait_for': 5
        }

    cred_restriction_number = \
        {
            'XPATH': '//input[@data-dojo-attach-point="number"]',
            'wait_for': 5
        }

    restriction_operation_check_box = \
        {
            'XPATH': '//input[@data-dojo-attach-point="emailApproval"]',
            'wait_for': 5
        }

    enable_usr_grps_check_box = \
        {
            'XPATH': '//input[@data-dojo-attach-point="selectAll"]',
            'wait_for': 5
        }

    enable_usr_grps_list = \
        {
            'XPATH': '//div[@data-dojo-attach-point="employee"]//label',
            'wait_for': 5
        }

    cred_distr_grp_save_button = \
        {
            'XPATH': '//div[@data-dojo-attach-point="manageEmployeeGroup"]'
                     '//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

