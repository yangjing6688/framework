class UserProfileWebElementsDef:
    user_profile_add = \
        {
            'XPATH': '//span[@class="table-action-icons table-add"]',
            'wait_for': 5
        }

    user_profile_name = \
        {
            'XPATH': '//input[@data-dojo-attach-point="profileName"]',
            'wait_for': 5
        }

    user_profile_vlan_add = \
        {
            'XPATH': '//span[@data-dojo-attach-point="ipSave"]',
            'wait_for': 5
        }

    user_profile_vlan_name = \
        {
            'XPATH': '//input[@data-dojo-attach-point="nameEl"]',
            'wait_for': 5
        }

    user_profile_vlan_id = \
        {
            'XPATH': '//input[@data-dojo-attach-point="defaultVlanId"]',
            'wait_for': 5
        }

    user_profile_vlan_save = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveBtn"]',
            'wait_for': 5
        }

    user_profile_save = \
        {
            'XPATH': '//button[@data-dojo-attach-point="saveButton"]',
            'wait_for': 5
        }

    user_profile_grid_rows = \
        {
            'XPATH': '//div[@data-dojo-attach-point="additionalSettingsContentArea"]//table[@class="dgrid-row-table"]',
            'wait_for': 10
         }

    user_profile_row_cells = \
        {
            'CSS_SELECTOR': '.dgrid-cell',
            'wait_for': 15
        }