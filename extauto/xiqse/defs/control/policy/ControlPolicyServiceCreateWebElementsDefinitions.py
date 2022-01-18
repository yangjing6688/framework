class ControlPolicyServiceCreateWebElementsDefinitions:

    create_service_menu = \
        {
            'DESC': 'Create Service menu option',
            'XPATH': '//span[contains(@class, "x-menu-item-text") and text()="Create Service..."]',
            'wait_for': 3
        }

    create_service_window = \
        {
            'DESC': 'Control->Policy->Create Service Window',
            'XPATH': '//div[contains(text(),"Create Service") and contains(@class, "x-title-text")]',
            'wait_for': 3
        }

    name_input = \
        {
            'DESC': 'Control->Policy->Create Service Window->Name input textfield',
            'XPATH': '//div[@xiqse-auto-id="createPolicyServiceNameField"]//input[@value="New Service"] |'
                     '//div[contains(@id,"window")]//input[contains(@id,"textfield") and @value="New Service"]',
            'wait_for': 3
        }

    ok_button = \
        {
            'DESC': 'Control->Policy->Create Service Window->OK button',
            'XPATH': '//div[@xiqse-auto-id="createPolicyServiceOkButton"] |'
                     '//div[contains(@id,"window")]//span[contains(@class, "x-btn-inner") and text()="OK"]',
            'wait_for': 3
        }

    cancel_button = \
        {
            'DESC': 'Control->Policy->Create Service Window->Cancel button',
            'XPATH': '//div[@xiqse-auto-id="createPolicyServiceCancelButton"] |'
                     '//div[contains(@id,"window")]//span[contains(@class, "x-btn-inner") and text()="Cancel"]',
            'wait_for': 3
        }

    name_in_use_error = \
        {
            'DESC': 'Control->Policy->Create Service Window - name already in use error',
            'XPATH': '//div[contains(@id, "messagebox") and text()="Name is already in use."]',
            'wait_for': 3
        }

    error_ok_button = \
        {
            'DESC': 'Control->Policy->Create Service Window - name already in use error',
            'XPATH': '//div[contains(@id,"messagebox")]//span[text()="OK"]',
            'wait_for': 3
        }
