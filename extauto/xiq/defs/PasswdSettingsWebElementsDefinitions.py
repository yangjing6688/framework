class PasswdSettingsWebElementsDefinitions:
    letters_check_box = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableLetters"]',
            'wait_for': 5
        }

    numbers_check_box = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableDigits"]',
            'wait_for': 5
        }

    special_character_check_box = \
        {
            'XPATH': '//*[@data-dojo-attach-point="enableSpecialChars"]',
            'wait_for': 5
        }

    enforce_use_of_drop_down = \
        {
            'XPATH': "//*[@data-automation-tag='automation-enforce-use-chzn-container-ctn']",
            'wait_for': 5
        }

    psk_generation_method_drop_down = \
        {
            'XPATH': "//*[@data-automation-tag='password-generate-chzn-container-ctn']",
            'wait_for': 5
        }

    generate_password_length_drop_down = \
        {
            'XPATH': "//*[@data-automation-tag='automation-password-length-chzn-container-ctn']",
            'wait_for': 5
        }

    active_select_items = \
        {
            'CSS_SELECTOR': '.active-result',
            'wait_for': 1
        }

    concatenating_string = \
        {
            'XPATH': '//*[@data-dojo-attach-point="concatString"]',
            'wait_for': 5
        }

