class PrivateClientGroupsDefinitions:
    private_client_grp_default_network_policy = \
        {
            'XPATH': '//div[@data-automation-tag="automation-chzn-container-ctn"]',

            'wait_for': 1
        }

    private_client_grp_network_policy_drop_down_list_items = \
        {
            'XPATH': '//ul[@data-automation-tag="automation-chzn-results-ctn"]/li',
            'wait_for': 1
        }

    private_client_grp_ap_based_groups_tab = \
        {
            'XPATH': '//div[@class="clearfix ui-tab-updated-parent"]/div[1]',
            'wait_for': 1
        }

    private_client_grp_key_based_groups_tab = \
        {
            'XPATH': '//div[@class="clearfix ui-tab-updated-parent"]/div[2]',
            'wait_for': 1
        }

    private_client_grp_enable_ap_based_on_off_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enablePrivateClientGroups"]',
            'wait_for': 1
        }

    private_client_grp_enable_key_based_on_off_button = \
        {
            'XPATH': '//input[@data-dojo-attach-point="keyBasedToggle"]',
            'wait_for': 1
        }

    private_client_grp_delete_room_button = \
        {
            'XPATH': '//span[@data-dojo-attach-point="deleteRoom"]',
            'wait_for': 1
        }

    private_client_grp_add_room_button = \
        {
            'XPATH': '//div[@class="room-assignment-list"]//div[@data-dojo-attach-point="actionLeft"]/span[1]',
            'wait_for': 1
        }

    private_client_grp_all_rooms_checkbox = \
        {
            'XPATH': '//input[@class="pcg-select-all-rooms"]',
            'wait_for': 1
        }

    diag_confirm_yes_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="yesBtn"]',
            'wait_for': 1
        }

    private_ap_based_room_table_headers = \
        {
            'XPATH': '//div[@componentpath="RoomAssignment"]//div[@class="room-assignment-list"]//table/tr/th',
            'wait_for': 1
        }

    private_ap_based_room_total_cells = \
        {
            'XPATH': '//div[@componentpath="RoomAssignment"]//div[@class="room-assignment-list"]//table/tr/td',
            'wait_for': 1
        }

    private_ap_based_room_input_text = \
        {
            'XPATH': '//div[@class="edit-controls room-name"]/input',
            'wait_for': 1
        }


    private_ap_based_room_user_assigned_drop_down = \
        {
            'XPATH': '//div[@data-automation-tag="automation-chzn-container-ctn"]//span[contains(text(),"unassigned")]',
            'wait_for': 1
        }

    private_ap_based_room_user_assigned_enter_text = \
        {
            'XPATH': '//div[@class="edit-controls"]//input[@type="text"]',
            'wait_for': 1
        }

    room_user_assigned_drop_down_items = \
        {
            'XPATH': '//ul[@class="chzn-results "]',
            'wait_for': 1
        }


    private_client_grp_save_setting_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveInfo"]',
            'wait_for': 1
        }


    private_key_based_group_add_button = \
        {
            'XPATH': '//div[@class="key-user-list"]//span[@data-tip="Add"]',
            'wait_for': 1
        }

    private_key_based_group_delete_button = \
        {
            'XPATH': '//div[@class="key-user-list"]//span[@data-tip="Delete"]',
            'wait_for': 1
        }

    private_key_based_save_info_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="keySaveInfo"]',
            'wait_for': 1
        }

    private_key_based_delete_checkbox_all = \
        {
            'XPATH': '//th[@class="dgrid-cell dgrid-column-0 w30 dgrid-selector"]',
            'wait_for': 1
        }

    private_key_based_table_header = \
        {
            'XPATH': '//div[@data-dojo-attach-point="keyBasedContent"]//div[@class="dgrid-header dgrid-header-row ui-widget-header"]//table//th',
            'wait_for': 1
        }

    private_key_based_all_cells = \
        {
            'XPATH': '//div[@data-dojo-attach-point="keyBasedContent"]//div[@class="dgrid-scroller"]//table/tr/td',
            'wait_for': 1
        }

    private_user_select_key_based_group = \
        {
            'XPATH': '//div[@data-automation-tag="automation-chzn-container-ctn"]/a/span[contains(text(), "Select One")]',
            'wait_for': 1
        }

    private_user_search_key_based_group_text = \
        {
            'XPATH': '//div[@class="pcg-key-user-edit"]//input',
            'wait_for': 1
        }

    private_user_key_based_group_items = \
        {
            'XPATH': '//div[@class="pcg-key-user-edit"]//ul/li',
            'wait_for': 1
        }