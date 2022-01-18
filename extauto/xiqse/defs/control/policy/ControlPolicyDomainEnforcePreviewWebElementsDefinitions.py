class ControlPolicyDomainEnforcePreviewWebElementsDefinitions:
    # Enforce Preview
    enforce_preview_enforce_button = \
        {
            'DESC': 'Enforce button in the Enforce Preview window',
            'XPATH': '//span[contains(@class,"x-btn-inner-blue-small") and contains(text(),"Enforce")]',
            'wait_for': 10
        }

    enforce_preview_cancel_button = \
        {
            'DESC': 'Cancel button in the Enforce Preview window',
            'XPATH': '//div[contains(@id,"ext-comp")]//span[contains(text(),"Cancel")]',
            'wait_for': 10
        }

    enforce_preview_close_button = \
        {
            'DESC': 'Close button in the Enforce Preview window',
            'XPATH': '//span[contains(@id,"button") and contains(text(),"Close")]',
            'wait_for': 10
        }

    show_on_enforce_checkbox = \
        {
        'DESC': 'show-on-enforce checkbox in the Enforce Preview window',
        'XPATH': '//input[@checked="checked"]',
        'wait_for': 3
        }

    enforce_preview_device = \
        {
            'DESC': 'Device in the Enforce Preview window, as specified by IP',
            'XPATH': '//span[@class ="x-tree-node-text " and contains(text(), "${ip}")]',
            'wait_for': 10
        }


    # end of Enforce Preview