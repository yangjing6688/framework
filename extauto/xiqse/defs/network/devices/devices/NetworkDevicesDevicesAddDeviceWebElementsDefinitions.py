

class NetworkDevicesDevicesAddDeviceWebElementsDefinitions:

    ip_field = \
        {
            'DESC': 'IP Address text field in the Add Device dialog',
            'XPATH': '//div[contains(@id, "addDeviceWindow")]//input[@name="ip"]',
            
        }

    profile_dropdown = \
        {
            'DESC': 'Profile dropdown in the Add Device dialog',
            'XPATH': '//div[contains(@id, "addDeviceWindow")]//input[@name="profile_id"]',
            
        }

    nickname_field = \
        {
            'DESC': 'Nickname text field in the Add Device dialog',
            'XPATH': '//div[contains(@id, "addDeviceWindow")]//input[@name="nickname"]',
            
        }

    status_only_checkbox = \
        {
            'DESC': 'Poll Status Only checkbox in the Add Device dialog',
            'XPATH': '//div[contains(@id, "addDeviceWindow")]//input[@name="statusOnly"]',
            
        }

    run_site_add_actions_checkbox = \
        {
            'DESC': 'Run Site Add Actions checkbox in the Add Device dialog',
            'XPATH': '//input[@name="runAddActions"]',
            
        }

    ok_button = \
        {
            'DESC': 'OK button in the Add Device dialog',
            'XPATH': '//div[contains(@id, "addDeviceWindow")]//a[contains(@class, "x-btn-blue-small")]//span[text()="OK"]/../../..',
            
        }

    close_button = \
        {
            'DESC': 'Close button in the Add Device dialog',
            'XPATH': '//div[contains(@id, "addDeviceWindow")]//a[contains(@class, "x-btn-default-small")]//span[text()="Close"]',
            
        }
