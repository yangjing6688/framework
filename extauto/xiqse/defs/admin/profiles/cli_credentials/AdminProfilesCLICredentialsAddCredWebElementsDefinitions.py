

class AdminProfilesCLICredentialsAddCredWebElementsDefinitions:

    add_cli_credential_dialog_desc_field = \
        {
            'DESC': 'Add CLI Credential dialog Description field',
            'XPATH': '//div[contains(@id, "cliCredentialDlg")]//label//span[contains(text(), "Description")]/ancestor::div[contains(@class, "x-form-item")]//input',
            
        }

    add_cli_credential_dialog_user_name_field = \
        {
            'DESC': 'Add CLI Credential dialog User Name field',
            'XPATH': '//div[contains(@id, "cliCredentialDlg")]//input[@name="usernameId"]',
            
        }

    add_cli_credential_dialog_type_dropdown = \
        {
            'DESC': 'Add CLI Credential dialog Type dropdown',
            'XPATH': '//div[contains(@id, "cliCredentialDlg")]//input[@name="typeId"]',
            
        }

    add_cli_credential_dialog_login_pwd_field = \
        {
            'DESC': 'Add CLI Credential dialog Login Password field',
            'XPATH': '//div[contains(@id, "cliCredentialDlg")]//input[@name="loginPasswdId"]',
            
        }

    add_cli_credential_dialog_enable_pwd_field = \
        {
            'DESC': 'Add CLI Credential dialog Enable Password field',
            'XPATH': '//div[contains(@id, "cliCredentialDlg")]//input[@name="enablePasswdId"]',
            
        }

    add_cli_credential_dialog_config_pwd_field = \
        {
            'DESC': 'Add CLI Credential dialog Configuration Password field',
            'XPATH': '//div[contains(@id, "cliCredentialDlg")]//input[@name="configPasswordId"]',
            
        }

    add_cli_credential_dialog_cancel_btn = \
        {
            'DESC': 'Add CLI Credential dialog Cancel button',
            'XPATH': '//div[contains(@id, "cliCredentialDlg")]//a[contains(@class, "x-btn-default-small")]//span[text()="Cancel"]',
            
        }

    add_cli_credential_dialog_save_btn = \
        {
            'DESC': 'Add CLI Credential dialog Save button',
            'XPATH': '//div[contains(@id, "cliCredentialDlg")]//a[contains(@class, "x-btn-blue-small")]//span[text()="Save"]/ancestor::a',
            
        }
