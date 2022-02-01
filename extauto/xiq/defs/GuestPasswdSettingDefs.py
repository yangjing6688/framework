class GuestPasswdSettingDefs:
    letters_check_box = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableLetters"]',
            'wait_for': 5
        }

    numbers_check_box = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableDigits"]',
            'wait_for': 5
        }

    special_character_check_box = \
        {
            'XPATH': '//input[@data-dojo-attach-point="enableSpecialChars"]',
            'wait_for': 5
        }

    enforce_use_of_drop_down = \
        {
            'XPATH': "//*[@data-automation-tag='automation-chzn-container-ctn']",
            'wait_for': 5,
            'index': 1
        }

    generate_password_length_drop_down = \
        {
            'XPATH': "//*[@data-automation-tag='automation-chzn-container-ctn']",
            'wait_for': 5,
            'index': 3
        }

    active_select_items = \
        {
            'CSS_SELECTOR': '.active-result',
            'wait_for': 1
        }