class ControlPolicyDomainVerifyWebElementsDefinitions:

    # Verify Domain
    verify_domain_success_msg = \
        {
            'DESC': 'Verify Success message in the dialog',
            'XPATH': '//div[contains(text(),"Device(s) in sync with domain.")]',
            'wait_for': 1
        }

    verify_domain_success_ok_bttn = \
        {
            'DESC': 'OK button in the Verify Success dialog',
            'XPATH': '//div/a[2]/span/span/span[contains(@class,"x-btn-inner-blue-small") and contains(text(),"OK")]',
            'wait_for': 5
        }

    verify_domain_fail_msg = \
        {
            'DESC': 'Verify failure message in the dialog',
            'XPATH': '//div[contains(text(),"The following device(s) had errors or do not match the current Role set")]',
            'wait_for': 1
        }

    verify_domain_fail_ok_bttn = \
        {
            'DESC': 'OK button in the Verify Failure dialog',
            'XPATH': '//div[contains(@id,"window")]//span[contains(@class,"x-btn-inner-blue-small") and contains(text(),"OK")]',
            'wait_for': 5
        }

    cannot_verify_domain_error_msg = \
        {
            'DESC': 'Error message in the Cannot Verify Domain dialog',
            'XPATH': '//div[contains(text(),"No devices exist in this domain to verify.")]',
            'wait_for': 1
        }

    cannot_verify_domain_ok_bttn = \
        {
            'DESC': 'OK button in the Cannot Verify Domain dialog',
            'XPATH': '//span/span/span[contains(@class ,"x-btn-inner-blue-small") and contains(text(), "OK")]',
            'wait_for': 5
        }

    # end of Verify Domain