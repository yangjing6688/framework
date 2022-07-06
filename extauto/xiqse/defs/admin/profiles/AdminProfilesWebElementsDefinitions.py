

class AdminProfilesWebElementsDefinitions:

    snmp_credentials_tab = \
        {
            'DESC': 'SNMP Credentials Tab on the Administration> Profiles page',
            'XPATH': '//div[contains(@class, "x-tabpanel-child")]//span[text()="SNMP Credentials" and contains(@class, "x-tab-inner")]',
            
        }

    cli_credentials_tab = \
        {
            'DESC': 'CLI Credentials Tab on the Administration> Profiles page',
            'XPATH': '//div[contains(@class, "x-tabpanel-child")]//span[text()="CLI Credentials" and contains(@class, "x-tab-inner")]',
            
        }

    device_mapping_tab = \
        {
            'DESC': 'Device Mapping Tab on the Administration> Profiles page',
            'XPATH': '//div[contains(@class, "x-tabpanel-child")]//span[text()="Device Mapping" and contains(@class, "x-tab-inner")]',
            
        }

    profiles_table_rows = \
        {
            'DESC': 'Profiles Table Rows',
            'XPATH': '//div[contains(@id, "profilesCredentialsGrid")]//table[contains(@id, "gridview")]//tr',
            
        }

    profiles_refresh_table_button = \
        {
            'DESC': 'Refresh Profiles table button',
            'XPATH': '//div[contains(@id, "profilesCredentialsGrid")]//span[contains(@class, "x-tbar-loading")]',
            
        }

    profile_add_button = \
        {
            'DESC': 'Add Profile toolbar button',
            'XPATH': '//div[contains(@id, "profilesCredentialsGrid")]//span[text()="Add..."]/ancestor::a',
            
        }

    profile_edit_button = \
        {
            'DESC': 'Edit Profile toolbar button',
            'XPATH': '//div[contains(@id, "profilesCredentialsGrid")]//span[text()="Edit..."]/ancestor::a',
            
        }

    profile_delete_button = \
        {
            'DESC': 'Delete Profile toolbar button',
            'XPATH': '//div[contains(@id, "profilesCredentialsGrid")]//span[text()="Delete"]/ancestor::a',
            
        }
