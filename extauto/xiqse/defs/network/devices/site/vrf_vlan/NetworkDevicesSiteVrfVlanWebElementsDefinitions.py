
class NetworkDevicesSiteVrfVlanWebElementsDefinitions:

    vlan_add_button = \
        {
            'DESC': 'VLAN Add toolbar button',
            'XPATH': '//div[contains(@id, "deviceVlanPanel")]//span[contains(@class, "add")]/ancestor::a',
            'wait_for': 10
        }

    vlan_delete_button = \
        {
            'DESC': 'VLAN Delete toolbar button',
            'XPATH': '//div[contains(@id, "deviceVlanPanel")]//span[contains(@class, "delete")]/ancestor::a',
            'wait_for': 10
        }

    vlan_update_button = \
        {
            'DESC': 'VLAN Row-Edit Update button',
            'XPATH': '//span[text()="Update"]',
            'wait_for': 10
        }

    vlan_cancel_button = \
        {
            'DESC': 'VLAN Row-Edit Cancel button',
            'XPATH': '//span[text()="Cancel"]',
            'wait_for': 10
        }

    vlan_add_name_field = \
        {
            'DESC': 'Add VLAN Name field',
            'XPATH': '//input[@name="deviceDetailsVlanNameEditor"]',
            'wait_for': 10
        }

    vlan_add_vid_field = \
        {
            'DESC': 'Add VLAN VID field',
            'XPATH': '//input[@name="deviceDetailsVidEditor"]',
            'wait_for': 10
        }
