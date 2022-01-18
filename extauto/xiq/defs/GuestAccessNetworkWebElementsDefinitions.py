class GuestAccessNetworkWebElementsDefinitions:
    wireless_nw_add_button = \
        {
         'XPATH': '//div[@data-automation-tag="automation-wireless-networks-grid"]//span[@data-tip="Add"]',
         'wait_for': 5
         }

    guest_access_network_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 1
        }

    guest_access_network_close_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="closeButton"]',
            'wait_for': 1
        }

    guest_network_go_to_deploy_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="doneButton"]',
            'wait_for': 1
        }

    ui_menu_list = \
        {
            'CSS_SELECTOR': '.ui-menu-list',
            'wait_for': 2
        }

    guest_access_nw_menu_item = \
        {
            'XPATH': '//div[@data-automation-tag="automation-wireless-networks-grid"]'
                     '//li/a[contains(text(), "Guest Access Network (simplified)")]',
            'wait_for': 5
        }

    ssid_name_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ssidName"]',
            'wait_for': 1
        }

    ssid_broadcost_name_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ssidBroadcastName"]',
            'wait_for': 1
        }

    unsecured_network = \
        {
            'CLASS_NAME': 'openLi',
            'wait_for': 1,
            'index': 1
        }

    unsecured_network_radio_button = \
        {
            'CSS_SELECTOR': '//input[@data-automation-tag="automation-guest-access-open-network"]',
            'wait_for': 2
        }

    guest_access_nw_without_login_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="openOptNoLogin"]',
            'wait_for': 1,
        }

    guest_access_usr_policy_bf_accessing_nw = \
        {
            'XPATH': '//input[@data-dojo-attach-point="openOptUseAccept"]',
            'wait_for': 1,
        }

    customized_cwp = \
        {
            'XPATH': '//div[@class="btn-config-group"]',
            'wait_for': 5,
        }

    cwp_name_field = \
        {
            'XPATH': '//*[@data-dojo-attach-point="cwpName"]',
            'wait_for': 5
        }

    user_policy_acceptance_slide_bar = \
        {
            'XPATH': '//*[@data-dojo-attach-point="page-upa"]',
            'wait_for': 1
        }

    success_page_slide_bar = \
        {
            'XPATH': '//*[@data-dojo-attach-point="page-success"]',
            'wait_for': 1
        }

    cwp_done_button = \
        {
            'CSS_SELECTOR': '.btn.btn-small.btn-primary.CWPDone',
            'wait_for': 2
        }

    guest_self_register_sign_in_radio_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="openOptSelfReg"]',
            'wait_for': 1,
        }

    cwp_landing_page_side_bar = \
        {
            'XPATH': '//*[@data-dojo-attach-point="page-login"]',
            'wait_for': 1
        }

    user_group_drop_down = \
        {
            'XPATH': '//*[@data-dojo-attach-point="userGroupSelect"]',
            'wait_for': 1
        }

    user_group_create = \
        {
            'XPATH': '//*[@data-dojo-attach-point="defaultUserGroupSettings"]',
            'wait_for': 1
        }

    user_group_name = \
        {
            'XPATH': '//*[@data-dojo-attach-point="userGroupName"]',
            'wait_for': 1
        }

    user_group_save_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="saveButton"]',
            'wait_for': 1
        }

    add_employee_approval_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="addApprovers"]',
            'wait_for': 1,
        }

    domain_name = \
        {
            'XPATH': '//input[@data-dojo-attach-point="dName"]',
            'wait_for': 1
        }

    domain_name_add_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="addBtn"]',
            'wait_for': 1
        }
    employee_approval_domain_name_done_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="approverDone"]',
            'wait_for': 1
        }

    secured_network = \
        {
            'XPATH': '//*[@data-dojo-attach-point="ppskLi"]',
            'wait_for': 1,
            'index': 1
        }

    secured_network_radio_button = \
        {
            'XPATH': '//input[@data-automation-tag="automation-guest-access-ppsk-network"]',
            'wait_for': 2
        }

    create_guest_credentials_to_login_nw = \
        {
            'XPATH': '//input[@data-dojo-attach-point="ppskLogin"]',
            'wait_for': 1
        }

    guests_self_reg_sign_in_employee_approve = \
        {
            'XPATH': '//input[@data-dojo-attach-point="ppskSelfReg"]',
            'wait_for': 1
        }

    global_passwd_cred_for_guest_to_login = \
        {
            'XPATH': '//input[@data-dojo-attach-point="pskPasswordOpt"]',
            'wait_for': 1
        }

    max_num_clients_per_ppsk = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableMaxClientsPerPpsk"]',
            'wait_for': 1,
        }

    max_clients_per_ppsk = \
        {
            'XPATH': '//input[@data-dojo-attach-point="maxClientsPerPpsk"]',
            'wait_for': 1
        }

    mac_binding_num_per_ppsk = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableMacBind"]',
            'wait_for': 1
        }

    mac_binding_number = \
        {
            'XPATH': '//input[@data-dojo-attach-point="maxMacsPerPpsk"]',
            'wait_for': 1
        }

    auth_db_drop_down = \
        {
            'XPATH': '//*[@data-dojo-attach-point="authDb"]',
            'wait_for': 1
        }

    bulk_user_prefix = \
        {
            'XPATH': '//*[@data-dojo-attach-point="bulkPrefix"]',
            'wait_for': 1
        }

    bulk_guest_count = \
        {
            'XPATH': '//*[@data-dojo-attach-point="bulkGuestCount"]',
            'wait_for': 1
        }

    guest_self_registration_ssid = \
        {
            'XPATH': '//*[@data-dojo-attach-point="guestSelfRegInput"]',
            'wait_for': 1
        }

    enable_cwp_check_box = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enablePskCwp"]',
            'wait_for': 1
        }

    psk_password = \
        {
            'CLASS_NAME': 'pskPasswordInput',
            'wait_for': 1
        }
