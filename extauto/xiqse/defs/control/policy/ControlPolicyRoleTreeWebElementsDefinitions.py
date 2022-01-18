class ControlPolicyRoleTreeWebElementsDefinitions:


    create_role_window_name_input = \
        {
            'DESC': 'Control->Policy->Create Role window input textfield',
            'XPATH': '//div[contains(@id, "window")]//input[contains(@value,"New Role")]',
            'wait_for': 10
        }

    role_tree_node_template = \
        {
            'DESC': 'Control->Policy->Roles->${roleName} tree node',
            'XPATH': '//td/div/span[text()="${roleName}"]',
            'wait_for': 10
        }

    confirm_delete_yes_button = \
        {
            'DESC': 'Control->Policy-> Confirm Delete Yes button',
            'XPATH': '//div[contains(@id, "messagebox")]//span[contains(@id, "button") and text()="Yes"]',
            'wait_for': 10
        }
