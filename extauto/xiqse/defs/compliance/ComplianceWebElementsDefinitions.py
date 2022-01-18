

class ComplianceWebElementsDefinitions:

    dashboard_tab = \
        {
            'DESC': 'Compliance> Dashboard Tab',
            'XPATH': '//span[text()="Dashboard" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    audit_tests_tab = \
        {
            'DESC': 'Compliance> Audit Tests Tab',
            'XPATH': '//span[text()="Audit Tests" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }
