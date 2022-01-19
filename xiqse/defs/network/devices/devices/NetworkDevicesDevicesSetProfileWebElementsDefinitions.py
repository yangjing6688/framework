

class NetworkDevicesDevicesSetProfileWebElementsDefinitions:

    profile_dropdown = \
        {
            'DESC': 'Profile dropdown in the Set Device Profile dialog',
            'XPATH': '//div[contains(@id, "setProfileWindow-")]//input[@name="profile_id"]',
            'wait_for': 10
        }

    ok_btn = \
        {
            'DESC': 'OK button in the Set Device Profile dialog',
            'XPATH': '//div[contains(@id, "setProfileWindow-")]//a[contains(@class, "x-btn-blue-small")]//span[text()="OK"]',
            'wait_for': 10
        }

    cancel_btn = \
        {
            'DESC': 'Cancel button in the Set Device Profile dialog',
            'XPATH': '//div[contains(@id, "setProfileWindow-")]//a[contains(@class, "x-btn-default-small")]//span[text()="Cancel"]',
            'wait_for': 10
        }
