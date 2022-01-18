
class MobAppWebElementsDefinition:

    qa_env_login_url_id = \
        {
            'XPATH': "(//android.widget.EditText[@text='Provide Base URL (eg: https://extremecloudiq.com/)' and @index = '4'])",
            'wait_for': 5
        }

    qa_env_save_button_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/btn_save",
            'wait_for': 5
        }

    trouble_logging_id = \
        {
            'XPATH': "(//android.widget.TextView[@text='Having trouble logging in?' and @index = '5'])",
            'wait_for': 8
        }

    support_email_id_text_field = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/txt_email_id",
            'wait_for': 3
        }

    reset_password_button_id = \
        {
            'CLASS_NAME': "android.widget.Button",
            'wait_for': 3
        }

    back_to_login_button_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/btn_back",
            'wait_for': 3
        }

    email_sent_confirmation_id = \
        {
            'XPATH': "(//android.widget.TextView[@text='Email sent confirmation' and @index = '0'])",
            'wait_for': 2
        }

    trouble_login_text_id = \
        {
            'XPATH': "(//android.widget.TextView[@text='Trouble Logging in ?' and @index = '0'])",
            'wait_for': 2
        }

    trouble_logging_close_link_id = \
        {
            'CLASS_NAME': "android.widget.ImageButton",
            'wait_for': 3
        }

    image_description_text_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/imageDesc",
            'wait_for': 3
        }

    image_title_text_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/imageTitle",
            'wait_for': 3
        }

    login_page_uname_id = \
        {
            'DESC': 'Login User',
            'ID': "com.extremenetworks.xiqmobileapp:id/txt_userid",
            'wait_for': 5
        }

    login_page_password_id = \
        {
            'DESC': 'Login Password',
            'ID': "com.extremenetworks.xiqmobileapp:id/txt_password",
            'wait_for': 5
        }

    password_toggle_id = \
        {
            'CLASS_NAME': "android.widget.ImageButton",
            'wait_for': 6
        }

    login_page_button_id = \
        {
            'DESC': 'Login Button',
            'CLASS_NAME': "android.widget.Button",
            'wait_for': 8
        }

    login_wrong_password_msg_id = \
        {
            'CLASS_NAME': "android.widget.Toast",
        }

    login_page_account_blocked_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/txt_summary",
        }

    bottom_sheet_id = \
        {
            'CLASS_NAME': "android.widget.ImageView",
            'wait_for': 5
        }

    top_button_id = \
        {
            'CLASS': "android.widget.ImageButton",
            'wait': 5
        }

    logout_device_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/logout",
            'wait_over': 10
        }

    logout_yes_button_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/yes_button",
            'wait_over': 7
        }

    logout_cancel_button_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/cancel_button",
            'wait_over': 7
        }
    multi_factor_auth_textfield_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/txt_otp",
            'wait_for': 3
        }

    multi_factor_auth_submit_button = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/btn_submit",
            'wait_for': 3
        }

    emergency_recovery_code_id = \
        {
            'XPATH': "(//android.widget.TextView[@text='emergency recovery code' and @index = '1'])",
            'wait_for': 3
        }

    cannot_enter_code_text_id = \
        {
            'XPATH': "(//android.widget.TextView[@text='Can't enter code? Use an' and @index = '0'])",
            'wait_for': 3
        }

    menu_item_id = \
        {
            'XPATH': "//android.widget.ImageButton[@content-desc='Open navigation drawer']",
            'wait_for': 5
        }

    customer_info_id_ = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/customer_id",
            'wait_for': 5
        }

    company_info_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/customer_org",
            'wait_for': 5
        }

    settings_item_id = \
        {
            'XPATH': "//android.widget.CheckedTextView[@text ='Settings' and @index = '0']",
            'wait_for': 5
        }

    settings_backward_link_id = \
        {
            'XPATH': "//android.widget.ImageButton[@content-desc='Navigate up']",
            'wait_for': 5
        }

    about_item_id = \
        {
            'XPATH': "//android.widget.CheckedTextView[@text ='About' and @index = '0']",
            'wait_for': 5
        }

    about_bw_link_id = \
        {
            'XPATH': "//android.widget.ImageButton[@content-desc='Navigate up']",
            'wait_for': 5
        }

    data_center_name_text_id = \
        {
            'XPATH': "//android.widget.CheckedTextView[@text ='Data Center Name:' and @index = '0']",
            'wait_for': 5
        }

    data_center_name_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/datacenter_name",
            'wait_for': 5
        }

    app_version_text_id = \
        {
            'XPATH': "//android.widget.CheckedTextView[@text ='App version:' and @index = '0']",
            'wait_for': 5
        }

    app_version_name_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/app_ver",
            'wait_for': 5
        }

    menu_item_logout_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/logout",
            'wait_for': 5
        }

    my_cloud_network_id = \
        {
            'XPATH': "//android.widget.TextView[@text ='My Cloud Network' and @index = '1']",
            'wait_for': 5
        }

    external_networks_id = \
        {
            'XPATH': "//android.widget.TextView[@text ='External Networks' and @index = '1']",
            'wait_for': 5
        }

    switch_button_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/btn_switch",
            'wait_for': 5
        }

    external_nw_search_field = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/search_src_text",
            'wait_for': 5
        }

    external_nw_table_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/list_view",
            'wait_for': 5
        }

    external_nw_row_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/item",
            'wait_for': 5

        }