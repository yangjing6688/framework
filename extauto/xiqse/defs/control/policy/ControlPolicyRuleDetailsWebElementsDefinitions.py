class ControlPolicyRuleDetailsWebElementsDefinitions:

    edit_rule_button = \
    {
        'DESC': 'Control->Policy->Service>Rule detail (right) panel>Edit button under Traffic Description',
        # need to work on this xpath for 21.9.10.x and older
        'XPATH': '//div[@xiqse-auto-id="policyRuleEditTrafDescButton"] |'
                 '//span[contains(@class, "x-btn") and text()="Edit..."]',
        'wait_for': 10
    }
