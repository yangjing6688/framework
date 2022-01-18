

class AdminProfilesAddProfileWebElementsDefinitions:

    add_profile_dialog_name_field = \
        {
            'DESC': 'Add Profile dialog Profile Name field',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="profileName"]',
            'wait_for': 10
        }

    add_profile_dialog_version_dropdown = \
        {
            'DESC': 'Add Profile dialog SNMP Version dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="snmpVersionId"]',
            'wait_for': 10
        }

    add_profile_dialog_read_dropdown = \
        {
            'DESC': 'Add Profile dialog Read dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="readCredId"]',
            'wait_for': 10
        }

    add_profile_dialog_write_dropdown = \
        {
            'DESC': 'Add Profile dialog Write dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="writeCredId"]',
            'wait_for': 10
        }

    add_profile_dialog_max_access_dropdown = \
        {
            'DESC': 'Add Profile dialog Max Access dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="maxAccessCredId"]',
            'wait_for': 10
        }

    add_profile_dialog_read_security_dropdown = \
        {
            'DESC': 'Add Profile dialog Read Security dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="readSecLvlId"]',
            'wait_for': 10
        }

    add_profile_dialog_write_security_dropdown = \
        {
            'DESC': 'Add Profile dialog Write Security dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="writeSecLvlId"]',
            'wait_for': 10
        }

    add_profile_dialog_max_security_dropdown = \
        {
            'DESC': 'Add Profile dialog Max Security dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="maxAccessSecLvlId"]',
            'wait_for': 10
        }

    add_profile_dialog_cli_dropdown = \
        {
            'DESC': 'Add Profile dialog CLI Credential dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="cliCredId"]',
            'wait_for': 10
        }

    add_profile_dialog_cancel_btn = \
        {
            'DESC': 'Add Profile dialog Cancel button',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//a[contains(@class, "x-btn-default-small")]//span[text()="Cancel"]',
            'wait_for': 10
        }

    add_profile_dialog_save_btn = \
        {
            'DESC': 'Add SNMP Credential dialog Save button',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//a[contains(@class, "x-btn-blue-small")]//span[text()="Save"]/ancestor::a',
            'wait_for': 10
        }
