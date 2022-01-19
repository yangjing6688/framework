class ControlPolicyDomainSaveWebElementsDefinitions:

    # Save Domain
    save_ok_bttn = \
        {
            'DESC': 'OK button in Save Domain window',
            'XPATH': '//div[contains(@id,"messagebox")]//span[contains(text(),"OK")]',
            'wait_for': 10
        }

    save_success_msg = \
        {
            'DESC': '"Domain saved successfully." message',
            'XPATH': '//div[contains(text(),"Domain saved successfully.")]',
            'wait_for': 10
        }
    # end of Save Domain
