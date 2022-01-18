

class CommonBannerWebElementsDefinitions:

    connection_lost_with_xiq_banner = \
        {
            'DESC': 'Connection Lost Message Banner',
            'XPATH': '//h3[contains(text(), "Connection Lost with ExtremeCloud IQ")]',
            'wait_for': 10
        }

    connection_lost_with_xiq_banner_close_button = \
        {
            'DESC': 'Close Button for the Connection Lost Message Banner',
            'XPATH': '//h3[contains(text(), "Connection Lost with ExtremeCloud IQ")]/b/a[text()="X"]',
            'wait_for': 10
        }

    license_limit_warning_banner = \
        {
            'DESC': 'License Limit Warning Message Banner',
            'XPATH': '//h3[contains(text(), "License Limit Warning")]',
            'wait_for': 10
        }

    license_limit_warning_banner_close_button = \
        {
            'DESC': 'Close Button for the License Limit Warning Message Banner',
            'XPATH': '//h3[contains(text(), "License Limit Warning")]/b/a[text()="X"]',
            'wait_for': 10
        }

    licensed_device_limit_exceeded_banner = \
        {
            'DESC': 'Licensed Device Limit Exceeded Message Banner',
            'XPATH': '//h3[contains(text(), "Licensed Device Limit Exceeded")]',
            'wait_for': 10
        }

    licensed_device_limit_exceeded_banner_close_button = \
        {
            'DESC': 'Close Button for the Licensed Device Limit Exceeded Message Banner',
            'XPATH': '//h3[contains(text(), "Licensed Device Limit Exceeded")]/b/a[text()="X"]',
            'wait_for': 10
        }

    license_expiration_banner = \
        {
            'DESC': 'License Expiration Message Banner',
            'XPATH': '//h3[contains(text(), "License Expiration")]',
            'wait_for': 10
        }

    license_expiration_banner_close_button = \
        {
            'DESC': 'Close Button for the License Expiration Message Banner',
            'XPATH': '//h3[contains(text(), "License Expiration")]/b/a[text()="X"]',
            'wait_for': 10
        }

    license_enforcement_banner = \
        {
            'DESC': 'License Enforcement Message Banner',
            'XPATH': '//h3[contains(text(), "License Enforcement") or contains(text(), "License enforcement")]',
            'wait_for': 10
        }

    license_enforcement_banner_close_button = \
        {
            'DESC': 'Close Button for the License Enforcement Message Banner',
            'XPATH': '//h3[contains(text(), "License Enforcement") or contains(text(), "License enforcement")]/b/a[text()="X"]',
            'wait_for': 10
        }

    location_data_unavailable_banner = \
        {
            'DESC': 'Location Data Unavailable Message Banner',
            'XPATH': '//h3[contains(text(), "Location Data Unavailable")]',
            'wait_for': 10
        }

    location_data_unavailable_banner_close_button = \
        {
            'DESC': 'Close Button for the Location Data Unavailable Message Banner',
            'XPATH': '//h3[contains(text(), "Location Data Unavailable")]/b/a[text()="X"]',
            'wait_for': 10
        }

    no_data_available_banner = \
        {
            'DESC': 'No Data Available Message Banner',
            'XPATH': '//h3[contains(text(), "No Data Available")]',
            'wait_for': 10
        }

    no_data_available_banner_close_button = \
        {
            'DESC': 'Close Button for the No Data Available Message Banner',
            'XPATH': '//h3[contains(text(), "No Data Available")]/b/a[text()="X"]',
            'wait_for': 10
        }

    motd_window = \
        {
            'DESC': 'Message of the Day window element',
            'CSS_SELECTOR':'.x-window.x-message-box[role=alertdialog]',
            'wait_for' : 3
        }

    motd_window_ok_button = \
        {
            'DESC': 'OK button in the message of the day window',
            'CSS_SELECTOR':'.x-window.x-message-box[role=alertdialog] a.x-btn-blue-small[aria-hidden=false]',
            'wait_for' : 3
        }

    banner_close_button = \
        {
            'DESC': 'Close Button for banner message panels (this will return a match for every open panel)',
            'XPATH': '//h3/b/a[text()="X"]',
            'wait_for': 10
        }
