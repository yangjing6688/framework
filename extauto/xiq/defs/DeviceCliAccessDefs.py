class DeviceCliAccessDefs:
    cli_cmd_input_field = \
        {
            'XPATH': '//input[@data-dojo-attach-point="cli"]',
            'wait_for': 5
        }

    cli_cmd_input_apply_button = \
        {
            'XPATH': '//button[@data-dojo-attach-point="apply"]',
            'wait_for': 5
        }

    cli_cmd_output_field = \
        {
            'XPATH': '//*[@class="cli-command-result"]',
            'wait_for': 5
        }

    cli_dialog_window_close_button = \
        {
            'XPATH': '//div//a[@data-dojo-attach-point="closeDialog"]',
            'wait_for': 5
        }

    cli_device_access_list = \
        {
            'XPATH': '//ul[@data-dojo-attach-point="deviceList"]//li',
            'wait_for': 5
        }

    cli_command_output_error_tool_tip = \
        {
            'XPATH': '//div[@data-dojo-attach-point="containerNode"]//h3[@data-dojo-attach-point="textEl"]',
            'wait_for': 5
        }
