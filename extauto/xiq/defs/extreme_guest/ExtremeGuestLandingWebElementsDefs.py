class ExtremeGuestLandingWebElementsDefs:
    extreme_guest_landing_user_conversion_widget = \
        {
            'XPATH': '//span[text()="User Conversion"]',
            'wait_for': 5
        }

    extreme_guest_landing_user_walkin_widget = \
        {
            'XPATH': '//span[text()="User Walk In - New Vs Return"]',
            'wait_for': 5
        }

    extreme_guest_landing_sessions_dwell_time_widget = \
        {
            'XPATH': '//span[text()="Sessions Dwell Time"]',
            'wait_for': 5
        }

    extreme_guest_landing_visitors_widget = \
        {
            'XPATH': '//span[text()="Visitors - Today Vs Yesterday"]',
            'wait_for': 5
        }

    extreme_guest_landing_new_users_widget = \
        {
            'XPATH': '//span[text()="New Users - Today Vs Yesterday"]',
            'wait_for': 5
        }

    extreme_guest_landing_client_distribution_widget = \
        {
            'XPATH': '//span[text()="Client Distribution - Device type"]',
            'wait_for': 5
        }

    extreme_guest_map_location_marker = \
        {
            'XPATH': '//img[@src="https://maps.gstatic.com/mapfiles/transparent.png"]',
            'wait_for': 5
        }

    extreme_guest_map_location_marker_header = \
        {
            'XPATH': '//div[@class="eguest-google-map-info-window"]//span[@class="eguest-header-title"]',
            'wait_for': 5
        }

    extreme_guest_map_location_marker_online_users_count = \
        {
            'XPATH': '//div[@class="eguest-google-map-info-window"]//span[@class="eguest-online-count"]',
            'wait_for': 5
        }

    extreme_guest_map_location_marker_total_users_count = \
        {
            'XPATH': '//div[@class="eguest-google-map-info-window"]//span[@class="eguest-total-online-count"]',
            'wait_for': 5
        }

    extreme_guest_map_location_marker_online_table_rows_today = \
        {
            'XPATH': '//div[@class="eguest-google-map-info-window"]//td[text()="${row}"]/parent::tr//td[@class="eguest-tbody-todayData"]',
            'wait_for': 5
        }

    extreme_guest_map_location_marker_online_table_rows_yesterday = \
        {
            'XPATH': '//div[@class="eguest-google-map-info-window"]//td[text()="${row}"]/parent::tr//td[@class="eguest-tbody-yestData"]',
            'wait_for': 5
        }
