

class ReportsWebElementsDefinitions:

    reports_tab = \
        {
            'DESC': 'Reports> Reports Tab',
            'XPATH': '//span[text()="Reports" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    custom_report_tab = \
        {
            'DESC': 'Reports> Custom Report Tab',
            'XPATH': '//span[text()="Custom Report" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }

    report_designer_tab = \
        {
            'DESC': 'Reports> Report Designer Tab',
            'XPATH': '//span[text()="Report Designer" and contains(@class, "x-tab-inner-default")]',
            'wait_for': 10
        }
