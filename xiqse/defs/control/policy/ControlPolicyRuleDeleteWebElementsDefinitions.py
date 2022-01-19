class ControlPolicyRuleDeleteWebElementsDefinitions:

    delete_rule_menu = \
        {
            'DESC': 'Delete menu option from a user-defined rule',
            'XPATH': '//span[contains(@class, "x-menu-item-text") and text()="Delete"]',
            'wait_for': 3
        }

    confirm_window = \
        {
            'DESC': 'Confirm window (with "Are you sure?" message) for delete rule',
            'XPATH': '//div[contains(@class, "x-title-text") and text()="Confirm Delete"]',
            'wait_for': 3
        }

    yes_button = \
        {
            'DESC': 'Yes button in the Confirm Delete window for deleting a rule',
            'XPATH': '//span[contains(@class, "x-btn-inner") and text()="Yes"]',
            'wait_for': 3
        }

    no_button = \
        {
            'DESC': 'No button in the Confirm Delete window for deleting a rule',
            'XPATH': '//span[contains(@class, "x-btn-inner") and text()="No"]',
            'wait_for': 3
        }
