class MLInsightsProxPresenceDefinitions:

    n360_prox_presence_proximity = \
        {
            'XPATH': '//*[@data-dojo-attach-point="tabSelector"]//li[contains(text(), "Proximity")]',
            'wait_for': 5
        }

    n360_prox_presence_presence = \
        {
            'XPATH': '//*[@data-dojo-attach-point="tabSelector"]//li[contains(text(), "Presence")]',
            'wait_for': 5
        }

    n360_prox_presence_table_select = \
        {
            'XPATH': '//*[@class="table-select-ctn"]//span[contains(text(), "Active & Detected View")]',
            'wait_for': 5
        }

    n360_prox_presence_refresh = \
        {
            'XPATH': '//*[@data-dojo-attach-point="refresh"]',
            'wait_for': 5
        }

    n360_prox_presence_table_option = \
        {
            'XPATH': '//*[@class="table-select-ctn"]//ul[@class="chzn-results qa-chzn-results-tableselector"]/li',
            'wait_for': 5
        }

    n360_prox_presence_owned = \
        {
            'CSS_SELECTOR': 'chzn-container.chzn-container-single.chzn-container-active',
            'wait_for': 5
        }

    n360_prox_presence_owned_option = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-filter-static"]//li',
            'wait_for': 5
        }

    n360_prox_presence_uuid = \
        {
            'XPATH': '//*[@class="chzn-container chzn-container-single"]',
            'wait_for': 5,
            'index': 2
        }

    n360_prox_presence_major = \
        {
            'XPATH': '//*[@class="chzn-container chzn-container-single"]',
            'wait_for': 5,
            'index': 3
        }

    n360_prox_presence_minor = \
        {
            'XPATH': '//*[@class="chzn-container chzn-container-single"]',
            'wait_for': 5,
            'index': 4
        }

    n360_prox_presence_static = \
        {
            'XPATH': '//*[@class="chzn-container chzn-container-single"]',
            'wait_for': 5,
            'index': 5
        }

    n360_prox_presence_rogue = \
        {
            'XPATH': '//*[@class="chzn-container chzn-container-single"]',
            'wait_for': 5,
            'index': 6
        }

    n360_prox_presence_uuid_search_box = \
        {
            'XPATH': '//*[@class="chzn-search"]',
            'index': 3,
            'wait_for': 5
        }

    n360_prox_presence_static_option = \
        {
            'XPATH': '//ul[@class="chzn-results qa-chzn-results-filter-static"]/li',
            'wait_for': 5
        }

    n360_prox_presence_rogue_option = \
        {
            'XPATH': '//ul[@class="class="chzn-results qa-chzn-results-filter-rogue""]/li',
            'wait_for': 5
        }

    n360_prox_presence_engage = \
        {
            'XPATH': '//*[@class="engaged"]',
            'wait_for': 5
        }

    n360_prox_presence_passers = \
        {
            'XPATH': '//*[@class="passers"]',
            'wait_for': 5
        }

    n360_prox_presence_conversion = \
        {
            'XPATH': '//*[@class="conversion"]',
            'wait_for': 5
        }

    n360_prox_presence_new_client = \
        {
            'XPATH': '//*[@class="newClient"]',
            'wait_for': 5
        }

    n360_prox_presence_ret_client = \
        {
            'XPATH': '//*[@class="returningClient"]',
            'wait_for': 5
        }

    n360_prox_presence_unassociated = \
        {
            'XPATH': '//*[@class="unassociated"]',
            'wait_for': 5
        }

    n360_prox_presence_associated = \
        {
            'XPATH': '//*[@class="associated"]',
            'wait_for': 5
        }

