

class NetworkDevicesTreePanelCreateSiteWebElementsDefinitions:

    name_field = \
        {
            'DESC': 'Name field in the Create Site dialog',
            'XPATH': '//div[contains(@id, "mapCreationRenameWindow")]//input',
            
        }

    ok_button = \
        {
            'DESC': 'OK button in the Create Site dialog',
            'XPATH': '//div[contains(@id, "mapCreationRenameWindow")]//a[contains(@class, "x-btn-blue-small")]//span[text()="OK"]/ancestor::a',
            
        }

    cancel_button = \
        {
            'DESC': 'Cancel button in the Create Site dialog',
            'XPATH': '//div[contains(@id, "mapCreationRenameWindow")]//a[contains(@class, "x-btn-default-small")]//span[text()="Cancel"]/..',
            
        }
