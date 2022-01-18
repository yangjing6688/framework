

class NetworkDevicesDevicesAddDeviceWebElementsDefinitions:

    ip_field = \
        {
            'DESC': 'IP Address text field in the Add Device dialog',
            'XPATH': '//div[contains(@id, "addDeviceWindow")]//input[@name="ip"]',
            'wait_for': 10
        }

    profile_dropdown = \
        {
            'DESC': 'Profile dropdown in the Add Device dialog',
            'XPATH': '//div[contains(@id, "addDeviceWindow")]//input[@name="profile_id"]',
            'wait_for': 10
        }

    nickname_field = \
        {
            'DESC': 'Nickname text field in the Add Device dialog',
            'XPATH': '//div[contains(@id, "addDeviceWindow")]//input[@name="nickname"]',
            'wait_for': 10
        }

    status_only_checkbox = \
        {
            'DESC': 'Poll Status Only checkbox in the Add Device dialog',
            'XPATH': '//div[contains(@id, "addDeviceWindow")]//input[@name="statusOnly"]',
            'wait_for': 10
        }

    ok_button = \
        {
            'DESC': 'OK button in the Add Device dialog',
            'XPATH': '//div[contains(@id, "addDeviceWindow")]//a[contains(@class, "x-btn-blue-small")]//span[text()="OK"]/../../..',
            'wait_for': 10
        }

    close_button = \
        {
            'DESC': 'Close button in the Add Device dialog',
            'XPATH': '//div[contains(@id, "addDeviceWindow")]//a[contains(@class, "x-btn-default-small")]//span[text()="Close"]',
            'wait_for': 10
        }
