class DashboardDefinitions:

    extreme_brand_icon = {
                          "XPATH" : '//*[@data-dojo-attach-point="brandingImg"]',
                          "CSS_SELECTOR" : ".brand-img-windows",
                          "DESC" : "Extreme Log on top right corner",
                          "wait_for" : 5
                          }

    total_app_usage = {'XPATH': '//*[@data-dojo-attach-point="totalUsage"]',
                        "DESC": "Total Application Usage",
                       "wait_for": 5
                       }

    total_aps_online_count = {
                        "XPATH": '//*[@data-automation-tag="automation-dashboard-health-cards-connect-online-count"]',
                        "CSS_SELECTOR": ".dashboard-header-metric",
                        'index': 0,
                        'wait_for': 1
                        }

    total_aps_offline_count = {
                        "XPATH": '//*[@data-automation-tag="automation-dashboard-health-cards-connect-offline-count"]',
                        "CSS_SELECTOR": ".dashboard-header-metric",
                        'index': 1,
                        'wait_for': 1
                        }

    total_apps_count = {
                        "XPATH": '//*[@data-automation-tag="automation-dashboard-health-cards-total-header-count"]',
                        "CSS_SELECTOR": ".dashboard-header-metric",
                        'index': 4,
                        'wait_for': 1
                        }

    total_users_count = {
                        "XPATH": '//*[@data-automation-tag="automation-dashboard-health-cards-client-header-count"]',
                        "CSS_SELECTOR": ".dashboard-header-metric",
                        'index': 7,
                        'wait_for': 1
                        }

    total_clients_count = {
                        "XPATH": '//*[@data-automation-tag="automation-dashboard-health-cards-client-header-count"]',
                        "CSS_SELECTOR": ".dashboard-header-metric",
                        'index': 6,
                        'wait_for': 1
                        }

    total_critical_alarms_count = {
                        "XPATH": '//*[@data-automation-tag="automation-dashboard-health-cards-alarms-crit-header-count"]',
                        'wait_for': 1
                        }

    total_major_alarms_count = {
                        "XPATH": '//*[@data-automation-tag="automation-dashboard-health-cards-alarms-major-header"]',
                        'wait_for': 1
                        }

    total_minor_alarms_count = {
                        "XPATH": '//*[@data-automation-tag="automation-dashboard-health-cards-alarms-minor-header-count"]',
                        'wait_for': 1
                        }

    total_rogue_aps_count = {
                        "XPATH": '//*[@data-automation-tag="automation-dashboard-health-cards-rogue-ap-count"]',
                        'wait_for': 1
                        }

    total_rogue_clients_count = {
                        "XPATH": '//*[@data-automation-tag="automation-dashboard-health-cards-rogue-client-count"]',
                        'wait_for': 1
                        }