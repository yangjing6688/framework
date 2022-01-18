class MLInsightsDefinitions:

    ml_insights_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="insightsTab"]//a[contains(text(), "ML INSIGHTS")]',
            'wait_for': 2
        }

    n360_plan_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-nav-plan"]//a[contains(text(), "NETWORK 360 PLAN")]',
            'wait_for': 2
        }

    n360_monitor_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-nav-tracker"]//a[contains(text(), "NETWORK 360 MONITOR")]',
            'wait_for': 2
        }

    n360_scorecard_button = \
        {
            'XPATH': '//*[@data-dojo-attach-point="insightsScorecard"]//a[contains(text(), "NETWORK SCORECARD")]',
            'wait_for': 5
        }

    n360_client_360_button = \
        {
            'XPATH': '//*[@data-automation-tag="automation-nav-clientsoverview"]//a[contains(text(), "CLIENT 360")]',
            'wait_for': 5
        }

    n360_comparative_analytics = \
        {
            'XPATH': '//*[@data-automation-tag="automation-nav-analytics"]//a[contains(text(), "COMPARATIVE ANALYTICS")]',
            'wait_for': 5
        }

    n360_proximity_and_presence = \
        {
            'XPATH': '//*[@data-automation-tag="automation-nav-proximity"]//a[contains(text(), "PROXIMITY & PRESENCE")]',
            'wait_for': 5
        }