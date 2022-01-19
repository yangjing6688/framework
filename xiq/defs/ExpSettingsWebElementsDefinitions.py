class ExpSettingsWebElementsDefinitions:
    account_expiration_drop_down = \
        {
            'XPATH': "//div[@data-automation-tag='automation-expiration-type-chzn-container-ctn']",
            'wait_for': 5
        }

    account_expiration_drop_down_options = \
        {
            'XPATH': '//div[@data-automation-tag="automation-expiration-type-chzn-container-ctn"]//ul//li',
            'wait_for': 5
        }

    valid_for_time_period_in = \
        {
            'XPATH': '//input[@data-dojo-attach-point="timeAfterCreateValue"]',
            'wait_for': 5,
            'index': 0
        }

    valid_for_time_period_in_drop_down = \
        {
            'XPATH': '//div[@data-automation-tag="automation-time-after-create-chzn-container-ctn"]',
            'wait_for': 5,
        }

    valid_for_time_period_in_drop_down_options = \
        {
            'XPATH': '//div[@data-automation-tag="automation-time-after-create-chzn-container-ctn"]//ul//li',
            'wait_for': 5,
        }

    valid_for_time_period_after_drop_down = \
        {
            'XPATH': '//div[@data-automation-tag="automation-login-type-chzn-container-ctn"]',
            'wait_for': 5,
        }

    valid_for_time_period_after_drop_down_options = \
        {
            'XPATH': '//div[@data-automation-tag="automation-login-type-chzn-container-ctn"]//ul//li',
            'wait_for': 5,
        }

    renew_user_credentials_check_box = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableRenew"]',
            'wait_for': 5,
            'index': 0
        }

    dlt_cred_imm_aft_expiration_check_box = \
        {
            'XPATH': '//input[@data-dojo-attach-point="deleteCredentials"]',
            'wait_for': 5,
        }

    delete_cred_after_check_box = \
        {
            'XPATH': '//input[@data-dojo-attach-point="deleteCredentialsAfter"]',
            'wait_for': 5,
        }

    delete_cred_after_input_field = \
        {
            'XPATH': '//input[@data-dojo-attach-point="deleteCredentialsAfterInput"]',
            'wait_for': 5,
        }

    delete_cred_after_drop_down = \
        {
            'XPATH': '//div[@data-automation-tag="delete-after-unit-chzn-container-ctn"]',
            'wait_for': 5,
        }

    delete_cred_after_drop_down_options = \
        {
            'XPATH': '//div[@data-automation-tag="delete-after-unit-chzn-container-ctn"]//ul//li',
            'wait_for': 5,
        }

    action_at_exp_access_rejected_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="reject"]',
            'wait_for': 5,
        }

    action_at_exp_show_expi_msg_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="giveMessage"]',
            'wait_for': 5,
        }

    access_key_must_be_used_within = \
        {
            'XPATH': '//input[@data-dojo-attach-point="dropDeadValue"]',
            'wait_for': 5,
            'index': 0
        }

    access_key_must_be_used_within_period_drop_down = \
        {
            'XPATH': '//div[@data-automation-tag="drop-dead-unit-chzn-container-ctn"]',
            'wait_for': 5,
        }

    access_key_must_be_used_within_period_optns = \
        {
            'XPATH': '//div[@data-automation-tag="drop-dead-unit-chzn-container-ctn"]//ul/li',
            'wait_for': 5,
        }

    req_auth_after_check_box = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableReauthorization"]',
            'wait_for': 5,
            'index': 0
        }

    req_auth_after_input_field = \
        {
            'XPATH': '//input[@data-dojo-attach-point="reauthorizationTime"]',
            'wait_for': 5,
            'index': 0
        }
