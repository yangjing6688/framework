
class DeviceRebootDefinitions:
    serial_number_text_id = \
        {
            'DESC': 'Serail Number of the AP',
            'ID': "com.extremenetworks.xiqmobileapp:id/txt_serial",
            
        }

    continue_button_id = \
        {
            'DESC': 'Clicked continue button',
            'ID': "com.extremenetworks.xiqmobileapp:id/btn_continue",
            
        }

    reboot_device_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/btn_reboot",
            'wait_for': 5
        }

    reboot_device_confirm_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/yes_button",
            'wait_for': 5
        }

    reboot_device_cancel_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/cancel_button",
            'wait_for': 5
        }