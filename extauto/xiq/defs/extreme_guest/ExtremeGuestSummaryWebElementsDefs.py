class ExtremeGuestSummaryWebElementsDefs:
    extreme_guest_summary_user_walkin_widget = \
        {
            'XPATH': '//div[text()="User Walk In"]',
        }

    extreme_guest_summary_dwell_time_widget = \
        {
            'XPATH': '//div[text()="Sessions Dwell Time"]',
        }

    extreme_guest_summary_visitors_widget = \
        {
            'XPATH': '//div[text()="Visitors"]',
        }

    extreme_guest_summary_visitors_widget_today = \
        {
            'XPATH': '(//div[contains(@class, "eguest-visitors-panel")])[1]//span[contains(@class, "eguest-today")]',
        }

    extreme_guest_summary_visitors_widget_yesterday = \
        {
            'XPATH': '(//div[contains(@class, "eguest-visitors-panel")])[1]//span[contains(@class, "eguest-yesterday")]',
        }

    extreme_guest_summary_new_user_widget = \
        {
            'XPATH': '//div[text()="New Users" and contains(@class, "x-title-text")]',
        }

    extreme_guest_summary_new_user_widget_today = \
        {
            'XPATH': '(//div[contains(@class, "eguest-visitors-panel")])[2]//span[contains(@class, "eguest-today")]',
        }

    extreme_guest_summary_new_user_widget_yesterday = \
        {
            'XPATH': '(//div[contains(@class, "eguest-visitors-panel")])[2]//span[contains(@class, "eguest-yesterday")]',
        }

    extreme_guest_summary_conversion_widget = \
        {
            'XPATH': '//div[text()="Conversion"]',
        }

    extreme_guest_summary_conversion_widget_connected = \
        {
            'XPATH': '((//div[contains(@data-automation-tag, "eguest-summary-today-conversion-chart")]/child::*/child::*)[1]/child::*)[3]',
        }

    extreme_guest_summary_conversion_widget_onboarded = \
        {
            'XPATH': '((//div[contains(@data-automation-tag, "eguest-summary-today-conversion-chart")]/child::*/child::*)[2]/child::*)[3]',
        }

    extreme_guest_summary_gender_widget = \
        {
            'XPATH': '//div[text()="Gender"]',
        }

    extreme_guest_summary_gender_widget_unspecified = \
        {
            'XPATH': '//span[@class="eguest-total-unspecified"]',
        }

    extreme_guest_summary_age_widget = \
        {
            'XPATH': '//div[text()="Age"]',
        }

    extreme_guest_summary_facebook_widget = \
        {
            'XPATH': '//span[contains(@class, "eguest-facebook-count")]',
        }

    extreme_guest_summary_google_widget = \
        {
            'XPATH': '//span[contains(@class, "eguest-google-count")]',
        }

    extreme_guest_summary_linkedin_widget = \
        {
            'XPATH': '//span[contains(@class, "eguest-linkedin-count")]',
        }

    extreme_guest_summary_total_users_widget = \
        {
            'XPATH': '//span[contains(@class, "eguest-totalusers-count")]',
        }

    extreme_guest_summary_online_users_widget = \
        {
            'XPATH': '//span[contains(@class, "eguest-onlineusers-count")]',
        }

    extreme_guest_summary_total_clients_widget = \
        {
            'XPATH': '//span[contains(@class, "eguest-totalclients-count")]',
        }

    extreme_guest_summary_online_clients_widget = \
        {
            'XPATH': '//span[contains(@class, "eguest-onlineclients-count")]',
        }
