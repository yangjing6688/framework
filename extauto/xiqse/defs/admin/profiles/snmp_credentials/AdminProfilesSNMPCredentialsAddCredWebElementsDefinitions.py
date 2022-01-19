

class AdminProfilesSNMPCredentialsAddCredWebElementsDefinitions:

    add_snmp_credential_dialog_name_field = \
        {
            'DESC': 'Add SNMP Credential dialog Credential Name field',
            'XPATH': '//div[contains(@id, "credentialDlg")]//input[@name="credentialName"]',
            'wait_for': 10
        }

    add_snmp_credential_dialog_version_dropdown = \
        {
            'DESC': 'Add SNMP Credential dialog SNMP Version dropdown',
            'XPATH': '//div[contains(@id, "credentialDlg")]//input[@name="snmpVersionId"]',
            'wait_for': 10
        }

    add_snmp_credential_dialog_community_field = \
        {
            'DESC': 'Add SNMP Credential dialog Community Name field',
            'XPATH': '//div[contains(@id, "credentialDlg")]//input[@name="communityNameId"]',
            'wait_for': 10
        }

    add_snmp_credential_dialog_user_name_field = \
        {
            'DESC': 'Add SNMP Credential dialog User Name field (SNMPv3)',
            'XPATH': '//div[contains(@id, "credentialDlg")]//input[@name="usernameId"]',
            'wait_for': 10
        }

    add_snmp_credential_dialog_auth_type_dropdown = \
        {
            'DESC': 'Add SNMP Credential dialog Authentication Type dropdown (SNMPv3)',
            'XPATH': '//div[contains(@id, "credentialDlg")]//input[@name="authenticationId"]',
            'wait_for': 10
        }

    add_snmp_credential_dialog_auth_pwd_field = \
        {
            'DESC': 'Add SNMP Credential dialog Authentication Password field (SNMPv3)',
            'XPATH': '//div[contains(@id, "credentialDlg")]//input[@name="authPasswdId"]',
            'wait_for': 10
        }

    add_snmp_credential_dialog_privacy_type_dropdown = \
        {
            'DESC': 'Add SNMP Credential dialog Privacy Type dropdown (SNMPv3)',
            'XPATH': '//div[contains(@id, "credentialDlg")]//input[@name="privTypeId"]',
            'wait_for': 10
        }

    add_snmp_credential_dialog_privacy_pwd_field = \
        {
            'DESC': 'Add SNMP Credential dialog Privacy Password field (SNMPv3)',
            'XPATH': '//div[contains(@id, "credentialDlg")]//input[@name="privacyPasswdId"]',
            'wait_for': 10
        }

    add_snmp_credential_dialog_cancel_btn = \
        {
            'DESC': 'Add SNMP Credential dialog Cancel button',
            'XPATH': '//div[contains(@id, "credentialDlg")]//a[contains(@class, "x-btn-default-small")]//span[text()="Cancel"]',
            'wait_for': 10
        }

    add_snmp_credential_dialog_save_btn = \
        {
            'DESC': 'Add SNMP Credential dialog Save button',
            'XPATH': '//div[contains(@id, "credentialDlg")]//a[contains(@class, "x-btn-blue-small")]//span[text()="Save"]/ancestor::a',
            'wait_for': 10
        }
