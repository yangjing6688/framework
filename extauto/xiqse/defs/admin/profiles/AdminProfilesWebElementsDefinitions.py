

class AdminProfilesWebElementsDefinitions:

    snmp_credentials_tab = \
        {
            'DESC': 'SNMP Credentials Tab on the Administration> Profiles page',
            'XPATH': '//div[contains(@class, "x-tabpanel-child")]//span[text()="SNMP Credentials" and contains(@class, "x-tab-inner")]',
            'wait_for': 10
        }

    cli_credentials_tab = \
        {
            'DESC': 'CLI Credentials Tab on the Administration> Profiles page',
            'XPATH': '//div[contains(@class, "x-tabpanel-child")]//span[text()="CLI Credentials" and contains(@class, "x-tab-inner")]',
            'wait_for': 10
        }

    device_mapping_tab = \
        {
            'DESC': 'Device Mapping Tab on the Administration> Profiles page',
            'XPATH': '//div[contains(@class, "x-tabpanel-child")]//span[text()="Device Mapping" and contains(@class, "x-tab-inner")]',
            'wait_for': 10
        }

    profiles_table_rows = \
        {
            'DESC': 'Profiles Table Rows',
            'XPATH': '//div[contains(@id, "profilesCredentialsGrid")]//table[contains(@id, "gridview")]//tr',
            'wait_for': 10
        }

    profiles_refresh_table_button = \
        {
            'DESC': 'Refresh Profiles table button',
            'XPATH': '//div[contains(@id, "profilesCredentialsGrid")]//span[contains(@class, "x-tbar-loading")]',
            'wait_for': 10
        }

    profile_add_button = \
        {
            'DESC': 'Add Profile toolbar button',
            'XPATH': '//div[contains(@id, "profilesCredentialsGrid")]//span[text()="Add..."]/ancestor::a',
            'wait_for': 10
        }

    profile_edit_button = \
        {
            'DESC': 'Edit Profile toolbar button',
            'XPATH': '//div[contains(@id, "profilesCredentialsGrid")]//span[text()="Edit..."]/ancestor::a',
            'wait_for': 10
        }

    profile_delete_button = \
        {
            'DESC': 'Delete Profile toolbar button',
            'XPATH': '//div[contains(@id, "profilesCredentialsGrid")]//span[text()="Delete"]/ancestor::a',
            'wait_for': 10
        }
