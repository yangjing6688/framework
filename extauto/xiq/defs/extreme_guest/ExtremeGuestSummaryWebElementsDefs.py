class ExtremeGuestSummaryWebElementsDefs:
    extreme_guest_summary_user_walkin_widget = \
        {
            'XPATH': '//div[text()="User Walk In"]',
            'wait_for': 5
        }

    extreme_guest_summary_dwell_time_widget = \
        {
            'XPATH': '//div[text()="Sessions Dwell Time"]',
            'wait_for': 5
        }

    extreme_guest_summary_visitors_widget = \
        {
            'XPATH': '//div[text()="Visitors"]',
            'wait_for': 5
        }

    extreme_guest_summary_visitors_widget_today = \
        {
            'XPATH': '(//div[contains(@class, "eguest-visitors-panel")])[1]//span[contains(@class, "eguest-today")]',
            'wait_for': 5
        }

    extreme_guest_summary_visitors_widget_yesterday = \
        {
            'XPATH': '(//div[contains(@class, "eguest-visitors-panel")])[1]//span[contains(@class, "eguest-yesterday")]',
            'wait_for': 5
        }

    extreme_guest_summary_new_user_widget = \
        {
            'XPATH': '//div[text()="New Users" and contains(@class, "x-title-text")]',
            'wait_for': 5
        }

    extreme_guest_summary_new_user_widget_today = \
        {
            'XPATH': '(//div[contains(@class, "eguest-visitors-panel")])[2]//span[contains(@class, "eguest-today")]',
            'wait_for': 5
        }

    extreme_guest_summary_new_user_widget_yesterday = \
        {
            'XPATH': '(//div[contains(@class, "eguest-visitors-panel")])[2]//span[contains(@class, "eguest-yesterday")]',
            'wait_for': 5
        }

    extreme_guest_summary_conversion_widget = \
        {
            'XPATH': '//div[text()="Conversion"]',
            'wait_for': 5
        }

    extreme_guest_summary_conversion_widget_connected = \
        {
            'XPATH': '((//div[contains(@data-automation-tag, "eguest-summary-today-conversion-chart")]/child::*/child::*)[1]/child::*)[3]',
            'wait_for': 5
        }

    extreme_guest_summary_conversion_widget_onboarded = \
        {
            'XPATH': '((//div[contains(@data-automation-tag, "eguest-summary-today-conversion-chart")]/child::*/child::*)[2]/child::*)[3]',
            'wait_for': 5
        }

    extreme_guest_summary_gender_widget = \
        {
            'XPATH': '//div[text()="Gender"]',
            'wait_for': 5
        }

    extreme_guest_summary_gender_widget_unspecified = \
        {
            'XPATH': '//span[@class="eguest-total-unspecified"]',
            'wait_for': 5
        }

    extreme_guest_summary_age_widget = \
        {
            'XPATH': '//div[text()="Age"]',
            'wait_for': 5
        }

    extreme_guest_summary_facebook_widget = \
        {
            'XPATH': '//span[contains(@class, "eguest-facebook-count")]',
            'wait_for': 5
        }

    extreme_guest_summary_google_widget = \
        {
            'XPATH': '//span[contains(@class, "eguest-google-count")]',
            'wait_for': 5
        }

    extreme_guest_summary_linkedin_widget = \
        {
            'XPATH': '//span[contains(@class, "eguest-linkedin-count")]',
            'wait_for': 5
        }

    extreme_guest_summary_total_users_widget = \
        {
            'XPATH': '//span[contains(@class, "eguest-totalusers-count")]',
            'wait_for': 5
        }

    extreme_guest_summary_online_users_widget = \
        {
            'XPATH': '//span[contains(@class, "eguest-onlineusers-count")]',
            'wait_for': 5
        }

    extreme_guest_summary_total_clients_widget = \
        {
            'XPATH': '//span[contains(@class, "eguest-totalclients-count")]',
            'wait_for': 5
        }

    extreme_guest_summary_online_clients_widget = \
        {
            'XPATH': '//span[contains(@class, "eguest-onlineclients-count")]',
            'wait_for': 5
        }
