
class RemoveDeviceDefinitions:
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

    remove_device_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/btn_remove_dev",
            'wait_for': 5
        }

    remove_device_confirm_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/yes_button",
            'wait_for': 6
        }

    remove_device_cancel_id = \
        {
            'ID': "com.extremenetworks.xiqmobileapp:id/cancel_button",
            'wait_for': 6
        }