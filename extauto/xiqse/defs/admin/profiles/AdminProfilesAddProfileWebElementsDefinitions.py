

class AdminProfilesAddProfileWebElementsDefinitions:

    add_profile_dialog_name_field = \
        {
            'DESC': 'Add Profile dialog Profile Name field',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="profileName"]',
            
        }

    add_profile_dialog_version_dropdown = \
        {
            'DESC': 'Add Profile dialog SNMP Version dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="snmpVersionId"]',
            
        }

    add_profile_dialog_read_dropdown = \
        {
            'DESC': 'Add Profile dialog Read dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="readCredId"]',
            
        }

    add_profile_dialog_write_dropdown = \
        {
            'DESC': 'Add Profile dialog Write dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="writeCredId"]',
            
        }

    add_profile_dialog_max_access_dropdown = \
        {
            'DESC': 'Add Profile dialog Max Access dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="maxAccessCredId"]',
            
        }

    add_profile_dialog_read_security_dropdown = \
        {
            'DESC': 'Add Profile dialog Read Security dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="readSecLvlId"]',
            
        }

    add_profile_dialog_write_security_dropdown = \
        {
            'DESC': 'Add Profile dialog Write Security dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="writeSecLvlId"]',
            
        }

    add_profile_dialog_max_security_dropdown = \
        {
            'DESC': 'Add Profile dialog Max Security dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="maxAccessSecLvlId"]',
            
        }

    add_profile_dialog_cli_dropdown = \
        {
            'DESC': 'Add Profile dialog CLI Credential dropdown',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//input[@name="cliCredId"]',
            
        }

    add_profile_dialog_cancel_btn = \
        {
            'DESC': 'Add Profile dialog Cancel button',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//a[contains(@class, "x-btn-default-small")]//span[text()="Cancel"]',
            
        }

    add_profile_dialog_save_btn = \
        {
            'DESC': 'Add SNMP Credential dialog Save button',
            'XPATH': '//div[contains(@id, "AccessProfileDlg")]//a[contains(@class, "x-btn-blue-small")]//span[text()="Save"]/ancestor::a',
            
        }
