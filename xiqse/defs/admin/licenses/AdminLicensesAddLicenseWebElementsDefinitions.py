

class AdminLicensesAddLicenseWebElementsDefinitions:

    text_area_add_license = \
        {
            'DESC': 'Text Area in the Add License Dialog',
            'XPATH': '//textarea[@name="adminAddLicenseTextArea"]',
            'wait_for': 10
        }

    ok_button_add_license = \
        {
            'DESC': 'Ok Button in the Add License Dialog',
            'XPATH': '//div[@xiqse-auto-id="addLicenseWindowOKButton"]',
            'wait_for': 10
        }

    cancel_button_add_license = \
        {
            'DESC': 'Cancel Button in the Add License Dialog',
            'XPATH': '//div[@xiqse-auto-id="addLicenseWindowCancelButton"]',
            'wait_for': 10
        }