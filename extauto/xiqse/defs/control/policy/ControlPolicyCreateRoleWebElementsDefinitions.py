class ControlPolicyCreateRoleWebElementsDefinitions:

    window = \
        {
            'DESC': 'Control->Policy->Create Role Window',
            'XPATH': '//div[contains(text(),"Create Role")]/ancestor::div[contains(@class, "x-window ")]',
            
        }

    name_input = \
        {
            'DESC': 'Control->Policy->Create Role Window->Name input textfield',
            'XPATH': '//div[contains(@id,"window")]//input[contains(@id,"textfield")]',
            
        }

    ok_button = \
        {
            'DESC': 'Control->Policy->Create Role Window->Name input textfield',
            'XPATH': '//div[@xiqse-auto-id="createPolicyRoleOkButton"] |'
                     '//div[contains(@id, "window")]//span[text()="OK"]/ancestor::a',
            
        }