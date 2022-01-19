class ControlPolicyRuleCreateWebElementsDefinitions:

    create_rule_menu = \
        {
            'DESC': 'Create Rule menu option',
            'XPATH': '//span[contains(@class, "x-menu-item-text") and text()="Create Rule..."]',
            'wait_for': 3
        }

    create_rule_window = \
        {
            'DESC': 'Control->Policy->Create Rule Window',
            'XPATH': '//div[contains(text(),"Create Rule") and contains(@class, "x-title-text")]',
            'wait_for': 3
        }

    name_input = \
        {
            'DESC': 'Control->Policy->Create Rule Window->Name input textfield',
            'XPATH': '//div[@xiqse-auto-id="createPolicyRuleNameField"]//input[@value="New Rule"] |'
                     '//div[contains(@id,"window")]//input[contains(@id,"textfield") and @value="New Rule"]',
            'wait_for': 3
        }

    ok_button = \
        {
            'DESC': 'Control->Policy->Create Rule Window->OK button',
            'XPATH': '//div[@xiqse-auto-id="createPolicyRuleOkButton"] |'
                     '//div[contains(@id,"window")]//span[contains(@class, "x-btn-inner") and text()="OK"]',
            'wait_for': 3
        }

    cancel_button = \
        {
            'DESC': 'Control->Policy->Create Rule Window->Cancel button',
            'XPATH': '//div[@xiqse-auto-id="createPolicyRuler1CancelButton"] |'
                     '//div[contains(@id,"window")]//span[contains(@class, "x-btn-inner") and text()="Cancel"]',
            'wait_for': 3
        }
