

class NetworkDevicesDevicesDeleteDeviceWebElementsDefinitions:

    yes_button = \
        {
            'DESC': 'Yes button in the Delete Device confirmation dialog',
            'XPATH': '//div[contains(@id, "deleteDeviceWindow")]//span[text()="Yes"]/ancestor::a',
            'wait_for': 10
        }

    no_button = \
        {
            'DESC': 'No button in the Delete Device confirmation dialog',
            'XPATH': '//div[contains(@id, "deleteDeviceWindow")]//span[text()="No"]/ancestor::a',
            'wait_for': 10
        }
