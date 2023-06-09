

class NetworkDevicesDevicesRestartDeviceWebElementsDefinitions:

    start_restart_button_item = \
        {
            'DESC':  'Start Device Restart Button Item',
            'XPATH': '//a[@role="button"]//span[text()="Start"]',
            
        }

    start_restart_yes_button = \
        {
            'DESC':  'Yes button to start restart of device',
            'XPATH':  '//a[@role="button"]//span[text()="Yes"]',
            
        }

    restart_operation_complete = \
        {
            'DESC': 'Restart Operation Complete dialog',
            'CSS_SELECTOR': '[data-qtip^="Restart Operation Complete."]',
            #'XPATH': '//div[@class="x-autocontainer-innerCt" and text()="Restart Operation Complete."]',
            
        }

    restart_devices_close_button = \
        {
            'DESC':  'Restart Devices Close button',
            'XPATH':  '//a[@role="button"]//span[text()="Close"]',
            'wait_for':  10
        }
