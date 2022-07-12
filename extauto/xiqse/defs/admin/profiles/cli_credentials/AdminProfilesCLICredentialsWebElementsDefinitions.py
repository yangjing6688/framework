

class AdminProfilesCLICredentialsWebElementsDefinitions:

    cli_credentials_table_rows = \
        {
            'DESC': 'CLI Credentials Table Rows',
            'XPATH': '//div[contains(@id, "authCredentialsGrid")]//table[contains(@id, "gridview")]//tr',
            
        }

    cli_credentials_refresh_table_button = \
        {
            'DESC': 'Refresh CLI Credentials table button',
            'XPATH': '//div[contains(@id, "authCredentialsGrid")]//span[contains(@class, "x-tbar-loading")]',
            
        }

    cli_credential_add_button = \
        {
            'DESC': 'Add CLI Credential toolbar button',
            'XPATH': '//div[contains(@id, "authCredentialsGrid")]//span[text()="Add..."]/ancestor::a',
            
        }

    cli_credential_edit_button = \
        {
            'DESC': 'Edit CLI Credential toolbar button',
            'XPATH': '//div[contains(@id, "authCredentialsGrid")]//span[text()="Edit..."]/ancestor::a',
            
        }

    cli_credential_delete_button = \
        {
            'DESC': 'Delete CLI Credential toolbar button',
            'XPATH': '//div[contains(@id, "authCredentialsGrid")]//span[text()="Delete"]/ancestor::a',
            
        }
