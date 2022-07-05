

class NetworkDevicesSiteDiscoverAddAddressWebElementsDefinitions:

    add_address_dialog = \
        {
            'DESC': 'Add Address Dialog',
            'XPATH': '//div[text()="Add Address"]/ancestor::div[contains(@class, "x-window-default")]',
            
        }

    add_address_dialog_discover_type_dropdown = \
        {
            'DESC': 'Add Address Dialog Discover Type Dropdown',
            'XPATH': '//div[text()="Add Address"]/ancestor::div[contains(@class, "x-window-default")]//input[contains(@id, "combo")]',
            
        }

    add_address_dialog_subnet_mask_field = \
        {
            'DESC': 'Add Address Dialog Subnet Mask Text Field',
            'XPATH': '//span[text()="Subnet/Mask:"]/ancestor::div[contains(@class, "x-form-item")]//input',
            
        }

    add_address_dialog_seed_address_field = \
        {
            'DESC': 'Add Address Dialog Seed Address Text Field',
            'XPATH': '//span[text()="Seed Address:"]/ancestor::div[contains(@class, "x-form-item")]//input',
            
        }

    add_address_dialog_start_address_field = \
        {
            'DESC': 'Add Address Dialog Start Address Text Field',
            'XPATH': '//span[text()="Start Address:"]/ancestor::div[contains(@class, "x-form-item")]//input',
            
        }

    add_address_dialog_end_address_field = \
        {
            'DESC': 'Add Address Dialog End Address Text Field',
            'XPATH': '//span[text()="End Address:"]/ancestor::div[contains(@class, "x-form-item")]//input',
            
        }

    add_address_dialog_ok_button = \
        {
            'DESC': 'Add Address Dialog OK Button',
            'XPATH': '//div[text()="Add Address"]/ancestor::div[contains(@class, "x-window-default")]//a[contains(@class, "x-btn-blue-small")]//span[text()="OK"]/ancestor::a',
            
        }

    add_address_dialog_cancel_button = \
        {
            'DESC': 'Add Address Dialog Cancel Button',
            'XPATH': '//div[text()="Add Address"]/ancestor::div[contains(@class, "x-window-default")]//a[contains(@class, "x-btn-default-small")]//span[text()="Cancel"]/..',
            
        }
