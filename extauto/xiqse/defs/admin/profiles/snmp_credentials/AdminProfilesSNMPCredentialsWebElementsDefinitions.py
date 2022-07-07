

class AdminProfilesSNMPCredentialsWebElementsDefinitions:

    snmp_credentials_table_rows = \
        {
            'DESC': 'SNMP Credentials Table Rows',
            'XPATH': '//div[contains(@id, "snmpCredentialsGrid")]//table[contains(@id, "gridview")]//tr',
            
        }

    snmp_credentials_refresh_table_button = \
        {
            'DESC': 'Refresh SNMP Credentials table button',
            'XPATH': '//div[contains(@id, "snmpCredentialsGrid")]//span[contains(@class, "x-tbar-loading")]',
            
        }

    snmp_credential_add_button = \
        {
            'DESC': 'Add SNMP Credential toolbar button',
            'XPATH': '//div[contains(@id, "snmpCredentialsGrid")]//span[text()="Add..."]/ancestor::a',
            
        }

    snmp_credential_delete_button = \
        {
            'DESC': 'Delete SNMP Credential toolbar button',
            'XPATH': '//div[contains(@id, "snmpCredentialsGrid")]//span[text()="Delete"]/ancestor::a',
            
        }
