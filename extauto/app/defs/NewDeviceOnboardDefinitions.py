
class NewDeviceOnboardDefinitions:

    grouping_icon_id =  \
        {
            'DESC': 'Grouping',
            'ID': "com.extremenetworks.xiqmobileapp:id/sort_btn",
            'wait_for': 5
        }

    connected_first_id = \
        {
            'DESC': 'ConnectedFirst',
            'ID': "com.extremenetworks.xiqmobileapp:id/cnctd_first_grp",
            'wait_for': 5
        }

    default_first_id = \
        {
            'ID' : "com.extremenetworks.xiqmobileapp:id/default_group",
            'wait_for': 5
        }

    disconnected_first_id = \
        {
            'DESC': 'DisconnectedFirst',
            'ID': "com.extremenetworks.xiqmobileapp:id/discnctd_first_grp",
            'wait_for': 5
        }

    grouping_close_id = \
        {
            'ID' : "com.extremenetworks.xiqmobileapp:id/btn_close",
            'wait_for': 5
        }

    device_hostname_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/host_nme",
            'wait_for': 5
        }

    device_sl_no_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/device_sno",
            'wait_for': 5
        }

    onboard_symbol_id = \
        {
            'DESC': 'Refresh cache',
            'ID': "com.extremenetworks.xiqmobileapp:id/onboard_button",
            'wait_for': 5
        }

    device_search_field_id = \
        {
            'DESC': 'search device',
            'ID': "com.extremenetworks.xiqmobileapp:id/search_src_text",
            'wait_for': 5
        }

    device_list_close_link_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/search_close_btn",
            'wait_for': 5
        }

    return_to_device_list_id = \
        {
            'XPATH': "//android.widget.ImageButton[@content-desc='Navigate up']",
            'wait_for': 5
        }

    device_filter_id = \
        {
            'DESC': 'device model',
            'ID': "com.extremenetworks.xiqmobileapp:id/device_sno",
            'wait_for': 5
        }

    device_list_table_id = \
        {
            'DESC': 'device list',
            'ID': "com.extremenetworks.xiqmobileapp:id/nested_scroll_view",
            'wait_for': 5
        }

    refresh_option_id = \
        {
            'DESC': 'Refresh cache',
            'ID': "com.extremenetworks.xiqmobileapp:id/refresh",
            

        }

    serial_number_text_id = \
        {
            'DESC': 'Serail Number of the AP',
            'ID': "com.extremenetworks.xiqmobileapp:id/txt_serial",
            
        }

    continue_button_id = \
        {
            'DESC': 'Clicked continue button',
            'CLASS_NAME': "android.widget.Button",
            
        }

    device_make_dropdown_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/sel_make",
            
        }

    device_make_table = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/select_dialog_listview",
            'wait_for': 5
        }

    device_make_row = \
        {
            'ID': "android:id/text1",
            'wait_for': 5
        }

    reenter_serial_no_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/btn_serial",
            'wait_for': 5
        }

    reenter_serial_number_field_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/onboard_txt_serial",
            'wait_for': 5
        }

    onboard_button_id = \
        {
            'DESC': 'Clicked Onboard button',
            'ID': 'com.extremenetworks.xiqmobileapp:id/btn_onboard',
            'wait_for': 12
        }

    device_model_no_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/device_model",
            
        }

    serial_no_of_ap_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/serial_no",
            'wait_for': 6
        }

    next_location_option_id = \
        {
            'DESC': 'Clicked Next option location',
            'CLASS_NAME': "android.widget.Button",
            'wait_for': 5
        }

    skip_location_id = \
        {
            'CLASS_NAME': "android.widget.Button",
            'wait_for': 5
        }

    search_location_id = \
        {
            'DESC': 'search sent location',
            'ID': "com.extremenetworks.xiqmobileapp:id/search_src_text",
            'wait_for': 5
        }


    location_table_id = \
        {
            'CLASS_NAME': "android.widget.ListView",
            
        }

    location_grid_rows = \
        {
            'DESC': 'Get all the locations rows',
            'ID': "com.extremenetworks.xiqmobileapp:id/item",
            
        }

    building_backward_link_id = \
        {
            'CLASS_NAME': "android.widget.ImageButton",
            'wait_for': 5
        }

    search_building_id = \
        {
            'DESC': 'Search sent building',
            'ID': "com.extremenetworks.xiqmobileapp:id/search_src_text",
            'wait_for': 5
        }

    building_table_id = \
        {
            'CLASS_NAME': "android.widget.ListView",
            
        }

    building_grid_rows = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/item",
            
        }

    floor_backward_link_id = \
        {
            'CLASS_NAME': "android.widget.ImageButton",
            'wait_for': 5
        }

    search_floor_id = \
        {
            'DESC': 'Search sent floor',
            'ID': "com.extremenetworks.xiqmobileapp:id/search_src_text",
            'wait_for': 5
        }

    floor_table_id = \
        {
            'CLASS_NAME': "android.widget.ListView",
            
        }

    floor_grid_rows = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/item",
            
        }

    exit_onboard_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/license_close",
            'wait_for': 6
        }

    exit_onboard_yes_button_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/yes_button",
            'wait_for': 6
        }

    exit_onboard_cancel_button_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/cancel_button",
            'wait_for': 6
        }

    go_previous_device_details_id = \
        {
            'DESC': 'clicked on next nw option',
            'XPATH': "(//android.widget.Button[@text='PREV: Device' and @index = '0'])",
            'wait_for': 6
        }

    next_network_option_id = \
        {
            'DESC': 'clicked on next nw option',
            'XPATH': "(//android.widget.Button[@text='NEXT : Network Policy' and @index = '1'])",
            'wait_for': 6
        }

    go_previous_location_details_id = \
        {
            'DESC': 'clicked on next nw option',
            'XPATH': "(//android.widget.Button[@text='PREV: Location' and @index = '0'])",
            'wait_for': 6
        }

    np_backward_link_id = \
        {
            'CLASS_NAME': "android.widget.ImageButton",
            'wait_for': 5
        }

    network_policy_dropdown = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/edit_npol",
            'wait_for': 5
        }

    network_policy_info_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/edit_npol",
            'wait_for': 5
        }

    search_np_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/search_src_text",
            'wait_for': 6
        }

    np_table_id = \
        {
            'CLASS_NAME': "android.widget.ListView",
            
        }

    np_grid_rows = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/item",
            
        }

    done_button_id = \
        {
            'DESC': 'Clicked on done button',
            'XPATH': "(//android.widget.Button[@text='DONE' and @index = '1'])",
            'wait_for': 6
        }

    policy_details_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/policy",
            'wait_for': 5
        }

    location_details_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/location",
            'wait_for': 5
        }

    finish_button_id = \
        {
            'DESC': 'Clicked on finish button',
            'XPATH': "(//android.widget.Button[@text='FINISH' and @index = '1'])",
            'wait_for': 6
        }
    refresh_popup_checkbox_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/checkbox",
            'wait-for': 5
        }

    refresh_popup_dismiss_button_id = \
        {
            'ID': "android:id/button2",
            'wait-for': 5
        }


    add_another_button_id = \
        {
            'XPATH': "(//android.widget.Button[@text='ADD ANOTHER' and @index = '0'])",
            'wait_for': 6
        }

    policy_save_yes_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/yes_button",
            'wait_for': 5
        }

    policy_save_no_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/no_button",
            'wait_for': 5
        }

    loc_details_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/edit_loc",
            'wait_for': 5
        }

    loc_dropdown_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/edit_loc",
            'wait_for': 5
        }

    build_details_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/edit_bldg",
            'wait_for': 5
        }

    floor_detail_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/edit_bldg",
            'wait_for': 5
        }

    device_home_backward_id = \
        {
            'XPATH': "(//android.widget.ImageButton[@content-desc='Navigate up'])",
            'wait_for': 5
        }

    device_home_policy_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/policy",
            'wait_for': 5
        }

    device_home_location_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/location",
            'wait_for': 5
        }
    