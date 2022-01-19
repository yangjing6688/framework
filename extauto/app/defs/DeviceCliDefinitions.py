
class DeviceCliDefinitions:
    serial_number_text_id = \
        {
            'DESC': 'Serail Number of the AP',
            'ID': "com.extremenetworks.xiqmobileapp:id/txt_serial",
            'wait_for': 10
        }

    continue_button_id = \
        {
            'DESC': 'Clicked continue button',
            'ID': "com.extremenetworks.xiqmobileapp:id/btn_continue",
            'wait_for': 10
        }

    device_cli_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/btn_cli",
            'wait_for': 5
        }

    device_cli_command_entry_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/txt_cli_cmd",
            'wait_for': 5
        }

    device_cli_apply_id = \
        {
            'CLASS_NAME': "android.widget.Button",
            'wait_for': 5
        }

    device_cli_exit_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/btn_exit",
            'wait_for': 5
        }

    device_cli_text_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/txt_cli_window",
            'wait_for': 5
        }
