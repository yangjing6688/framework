class MLInsightsWebElementsDefinitions:

    ml_insight_nav = \
        {
            'XPATH': '//*[@id="appHeader"]/ul/li[4]/span/a',
            'wait_for': 2
        }

    network_360_plan = \
        {
            'XPATH': '//*[@data-automation-tag="automation-nav-plan"]',
            'wait_for': 2
        }

    network_360_monitor = \
        {
            'XPATH': '//*[@data-automation-tag="automation-nav-tracker"]',
            'wait_for': 2
        }

    create_new_map_nw_360_plan = \
        {
            'XPATH': '//*[@data-dojo-attach-point="btnCreateNewMap"]',
            'CSS_SELECTOR': '.addLocationBtn',
            'wait_for': 2
        }

    create_new_map_window = \
        {
            'XPATH': '//*[@id="ah/util/dojocover/AHDialog_1_title"]',
            'wait_for': 2
        }

    maps_organization = \
        {
            'XPATH': '//*[@data-dojo-attach-point="organization"]',
            'wait_for': 2
        }

    maps_street_addr = \
        {
            'XPATH': '//*[@data-dojo-attach-point="street"]',
            'wait_for': 2
        }

    maps_city_state = \
        {
            'XPATH': "//*[@data-dojo-attach-point='city']",
            'wait_for': 2
        }

    maps_get_started = \
        {
            'XPATH': "//*[@data-dojo-attach-point='btnSave']",
            'wait_for': 2
        }

    maps_close_btn = \
        {
            'XPATH': "//*[@data-dojo-attach-point='btnCancelLocation']",
            'wait_for': 2
        }