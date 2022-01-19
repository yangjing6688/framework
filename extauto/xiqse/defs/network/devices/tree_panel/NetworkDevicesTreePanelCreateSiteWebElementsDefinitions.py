

class NetworkDevicesTreePanelCreateSiteWebElementsDefinitions:

    name_field = \
        {
            'DESC': 'Name field in the Create Site dialog',
            'XPATH': '//div[contains(@id, "mapCreationRenameWindow")]//input',
            'wait_for': 10
        }

    ok_button = \
        {
            'DESC': 'OK button in the Create Site dialog',
            'XPATH': '//div[contains(@id, "mapCreationRenameWindow")]//a[contains(@class, "x-btn-blue-small")]//span[text()="OK"]/ancestor::a',
            'wait_for': 10
        }

    cancel_button = \
        {
            'DESC': 'Cancel button in the Create Site dialog',
            'XPATH': '//div[contains(@id, "mapCreationRenameWindow")]//a[contains(@class, "x-btn-default-small")]//span[text()="Cancel"]/..',
            'wait_for': 10
        }
