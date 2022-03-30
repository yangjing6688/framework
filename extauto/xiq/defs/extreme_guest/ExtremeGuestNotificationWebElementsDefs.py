class ExtremeGuestNotificationWebElementsDefs:
    extreme_guest_notification_policy_tab = \
        {
            'XPATH': '(//span[text()="Policy"])[1]',
            'wait_for': 1
        }

    extreme_guest_notification_policy_add_policy = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-add-btn")]',
            'wait_for': 1
        }

    extreme_guest_notification_policy_refresh_policy = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-refresh-btn")]',
            'wait_for': 1
        }

    extreme_guest_notification_policy_delete_policy = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-delete-btn")]',
            'wait_for': 1
        }

    extreme_guest_notification_policy_grid = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-grid")]',
            'wait_for': 1
        }

    extreme_guest_notification_grid_rows = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-grid")]//td/..',
            'wait_for': 1
        }

    extreme_guest_notification_grid_row_cells_name_list = \
        {
            'XPATH': '//span[@class="eguest-policy-name"]',
            'wait_for': 1
        }

    extreme_guest_notification_policy_add_name = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-name-txt")]//input',
            'wait_for': 1
        }

    extreme_guest_notification_policy_add_description = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-description-txt")]//input',
            'wait_for': 1
        }

    extreme_guest_notification_policy_add_policy_type_user = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-typr-user-rb")]//input',
            'wait_for': 1
        }

    extreme_guest_notification_policy_add_policy_type_sponsor = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-type-sponsor-rb")]//input',
            'wait_for': 1
        }

    extreme_guest_notification_policy_add_sms_enable = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-sms-enable-cb")]//input',
            'wait_for': 1
        }

    extreme_guest_notification_policy_add_sms_sponsor_phone_number = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-sms-sponsor-number-txt")]//input',
            'wait_for': 1
        }

    extreme_guest_notification_policy_add_sms_message = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-sms-message-txt")]//input',
            'wait_for': 1
        }

    extreme_guest_notification_policy_add_email_enable = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-email-enable-cb")]',
            'wait_for': 1
        }

    extreme_guest_notification_policy_add_email_subject = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-email-message-txt")]//input',
            'wait_for': 1
        }

    extreme_guest_notification_policy_add_email_message = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-email-message-html")]//input',
            'wait_for': 1
        }

    extreme_guest_notification_policy_add_save_button = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-save")]',
            'wait_for': 1
        }

    extreme_guest_notification_policy_add_cancel_button = \
        {
            'XPATH': '//div[contains(@data-automation-tag, "eguest-notification-policy-cancel")]',
            'wait_for': 1
        }

    extreme_guest_notification_policy_add_save_ok_button = \
        {
            'XPATH': '//span[text()="OK"]',
            'wait_for': 1
        }