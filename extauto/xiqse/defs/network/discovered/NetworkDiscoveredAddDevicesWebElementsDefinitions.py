

class NetworkDiscoveredAddDevicesWebElementsDefinitions:

    add_button = \
        {
            'DESC': 'Add Button',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="Add"]/ancestor::a',
            'wait_for': 10
        }

    cancel_button = \
        {
            'DESC': 'Cancel Button',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="Cancel"]/ancestor::a',
            'wait_for': 10
        }

    # Tabs
    device_tab = \
        {
            'DESC': 'Device Tab in the Add Device dialog',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="Device"]',
            'wait_for': 10
        }

    add_device_actions_tab = \
        {
            'DESC': 'Add Device Actions Tab in the Add Device dialog',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="Add Device Actions"]',
            'wait_for': 10
        }

    device_annotation_tab = \
        {
            'DESC': 'Device Annotation Tab in the Add Device dialog',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="Device Annotation"]',
            'wait_for': 10
        }

    ports_tab = \
        {
            'DESC': 'Ports Tab in the Add Device dialog',
            'XPATH': '//div[contains(@id, "editDeviceDataWindow")]//span[text()="Ports"]',
            'wait_for': 10
        }

    # Device Annotation Tab Fields
    nickname_field = \
        {
            'DESC': 'Nickname field on the Device Annotations tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceNotePanel")]//input[@name="nickname"]',
            'wait_for': 5
        }

    asset_tag_field = \
        {
            'DESC': 'Asset Tag field on the Device Annotations tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceNotePanel")]//input[@name="assetTag"]',
            'wait_for': 5
        }

    user_data_1_field = \
        {
            'DESC': 'User Data 1 field on the Device Annotations tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceNotePanel")]//input[@name="userData1"]',
            'wait_for': 5
        }

    user_data_2_field = \
        {
            'DESC': 'User Data 2 field on the Device Annotations tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceNotePanel")]//input[@name="userData2"]',
            'wait_for': 5
        }

    user_data_3_field = \
        {
            'DESC': 'User Data 3 field on the Device Annotations tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceNotePanel")]//input[@name="userData3"]',
            'wait_for': 5
        }

    user_data_4_field = \
        {
            'DESC': 'User Data 4 field on the Device Annotations tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceNotePanel")]//input[@name="userData4"]',
            'wait_for': 5
        }

    note_field = \
        {
            'DESC': 'Notes field on the Device Annotations tab of the Configure Device dialog',
            'XPATH': '//div[contains(@id, "deviceNotePanel")]//textarea[@name="note"]',
            'wait_for': 5
        }
