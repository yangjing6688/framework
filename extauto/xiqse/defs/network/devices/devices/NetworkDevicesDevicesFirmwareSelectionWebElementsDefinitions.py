

class NetworkDevicesDevicesFirmwareSelectionWebElementsDefinitions:

    refresh_images_button = \
        {
            'DESC': 'Refresh Images toolbar button in the Firmware Selection dialog (accessed from Assign Image button of Upgrade Firmware dialog',
            'XPATH': '//a[contains(@class, "x-btn-default-toolbar-small")]//span[text()="Refresh Images"]',
            'wait_for': 10
        }

    refresh_load_mask = \
        {
            'DESC': 'Refreshing images waiting dialog',
            'XPATH': '//div[@class="x-mask-msg-text" and text()="Refreshing Firmware..."]',
            'wait_for': 10
        }

    firmware_images_table_rows = \
        {
            'DESC': 'Firmware Images Table Rows',
            'XPATH': '//div[contains(@id, "firmwareSelection")]//table[contains(@id, "gridview")]//tr',
            'wait_for': 10
        }

    firmware_selection_ok_button = \
        {
            'DESC': 'OK Button on Firmware Selection Dialog',
            'XPATH': '//div[contains(@id, "firmwareSelectionWindow")]//span[text()="OK"]/ancestor::a',
            'wait_for': 10
        }

    firmware_selection_cancel_button = \
        {
            'DESC': 'Cancel Button on Firmware Selection Dialog',
            'XPATH': '//div[contains(@id, "firmwareSelectionWindow")]//span[text()="Cancel"]/ancestor::a',
            'wait_for': 10
        }