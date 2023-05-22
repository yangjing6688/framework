class ExtremeGuestLandingWebElementsDefs:
    extreme_guest_landing_user_conversion_widget = \
        {
            'XPATH': '//span[text()="User Conversion"]',
        }

    extreme_guest_landing_user_walkin_widget = \
        {
            'XPATH': '//span[text()="User Walk In - New Vs Return"]',
        }

    extreme_guest_landing_sessions_dwell_time_widget = \
        {
            'XPATH': '//span[text()="Sessions Dwell Time"]',
        }

    extreme_guest_landing_visitors_widget = \
        {
            'XPATH': '//span[text()="Visitors - Today Vs Yesterday"]',
        }

    extreme_guest_landing_new_users_widget = \
        {
            'XPATH': '//span[text()="New Users - Today Vs Yesterday"]',
        }

    extreme_guest_landing_client_distribution_widget = \
        {
            'XPATH': '//span[text()="Client Distribution - Device type"]',
        }

    extreme_guest_map_location_marker = \
        {
            'XPATH': '//img[@src="https://maps.gstatic.com/mapfiles/transparent.png"]',
        }

    extreme_guest_map_location_marker_header = \
        {
            'XPATH': '//div[@class="eguest-google-map-info-window"]//span[@class="eguest-header-title"]',
        }

    extreme_guest_map_location_marker_online_users_count = \
        {
            'XPATH': '//div[@class="eguest-google-map-info-window"]//span[@class="eguest-online-count"]',
        }

    extreme_guest_map_location_marker_total_users_count = \
        {
            'XPATH': '//div[@class="eguest-google-map-info-window"]//span[@class="eguest-total-online-count"]',
        }

    extreme_guest_map_location_marker_online_table_rows_today = \
        {
            'XPATH': '//div[@class="eguest-google-map-info-window"]//td[text()="${row}"]/parent::tr//td[@class="eguest-tbody-todayData"]',
        }

    extreme_guest_map_location_marker_online_table_rows_yesterday = \
        {
            'XPATH': '//div[@class="eguest-google-map-info-window"]//td[text()="${row}"]/parent::tr//td[@class="eguest-tbody-yestData"]',
        }
