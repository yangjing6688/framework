class ExtremeGuestAnalyzeUsersWebElementsDefs:
    extreme_guest_analyze_users_tab = \
        {
            'XPATH': '//span[text()="Users"]',
            'wait_for': 5
        }

    extreme_guest_analyze_users_grid_location_column = \
        {
            'XPATH': '//span[@class="eguest-active_users_name"]',
            'wait_for': 5
        }

    extreme_guest_analyze_users_grid_username_column = \
        {
            'XPATH': '//span[text()="${username}"]',
            'wait_for': 5
        }