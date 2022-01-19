

class NetworkDevicesTreePanelDeleteSiteWebElementsDefinitions:

    confirm_delete_site_dialog = \
        {
            'DESC': 'Confirm Delete Site Dialog',
            'XPATH': '//div[contains(@class, "x-title") and text()="Delete Site"]/ancestor::div[contains(@class, "x-message-box") and @role="alertdialog"]',
            'wait_for': 10
        }

    yes_button = \
        {
            'DESC': 'Confirm Delete Site Dialog Yes Button',
            'XPATH': '//span[text()="Yes"]/ancestor::a',
            'wait_for': 10
        }

    no_button = \
        {
            'DESC': 'Confirm Delete Site Dialog No Button',
            'XPATH': '//span[text()="No"]/ancestor::a',
            'wait_for': 10
        }
