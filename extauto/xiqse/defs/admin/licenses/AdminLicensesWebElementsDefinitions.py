

class AdminLicensesWebElementsDefinitions:

    licenses_panel_title = \
        {
            'DESC': 'Licenses Panel Title',
            'XPATH': '//div[contains(@class, "x-title-text") and contains(text(), "Licenses")]',
            'wait_for': 10
        }

    licenses_add_button = \
        {
            'DESC': 'Add Button in the Licenses view',
            'XPATH': '//div[@xiqse-auto-id="adminAddLicenseButton"]',
            'wait_for': 10
        }

    licenses_refresh_button = \
        {
            'DESC': 'Refresh Button in the Licenses view',
            'XPATH': '//div[@xiqse-auto-id="adminRefreshLicenseDataButton"]',
            'wait_for': 10
        }

    licenses_table_rows = \
        {
            'DESC': 'Licenses Table Rows',
            'XPATH': '//div[contains(@id, "adminLicenseGrid")]/div[contains(@id, "gridview")]//tr',
            'wait_for': 10
        }

    licenses_source_col = \
        {
            'DESC': 'Source column in the Licenses Table',
            'CSS_SELECTOR': 'td[xiqse-col-dindex="source"]',
            'wait_for': 10
        }

    licenses_feature_col = \
        {
            'DESC': 'Feature column in the Licenses Table',
            'CSS_SELECTOR': 'td[xiqse-col-dindex="feature"]',
            'wait_for': 10
        }

    licenses_type_col = \
        {
            'DESC': 'Type column in the Licenses Table',
            'CSS_SELECTOR': 'td[xiqse-col-dindex="licenseType"]',
            'wait_for': 10
        }

    licenses_quantity_col = \
        {
            'DESC': 'Quantity column in the Licenses Table',
            'CSS_SELECTOR': 'td[xiqse-col-dindex="formattedQuantity"]',
            'wait_for': 10
        }

    licenses_end_date_col = \
        {
            'DESC': 'End Date column in the Licenses Table',
            'CSS_SELECTOR': 'td[xiqse-col-dindex="formattedEndDate"]',
            'wait_for': 10
        }

    licenses_start_date_col = \
        {
            'DESC': 'Start Date column in the Licenses Table',
            'CSS_SELECTOR': 'td[xiqse-col-dindex="formattedStartDate"]',
            'wait_for': 10
        }

    licenses_description_col = \
        {
            'DESC': 'Description column in the Licenses Table',
            'CSS_SELECTOR': 'td[xiqse-col-dindex="description"]',
            'wait_for': 10
        }
