

class AdminLicensesWebElementsDefinitions:

    licenses_panel_title = \
        {
            'DESC': 'Licenses Panel Title',
            'XPATH': '//div[contains(@class, "x-title-text") and contains(text(), "Licenses")]',
            
        }

    licenses_add_button = \
        {
            'DESC': 'Add Button in the Licenses view',
            'XPATH': '//div[@xiqse-auto-id="adminAddLicenseButton"]',
            
        }

    licenses_refresh_button = \
        {
            'DESC': 'Refresh Button in the Licenses view',
            'XPATH': '//div[@xiqse-auto-id="adminRefreshLicenseDataButton"]',
            
        }

    licenses_table_rows = \
        {
            'DESC': 'Licenses Table Rows',
            'XPATH': '//div[contains(@id, "adminLicenseGrid")]/div[contains(@id, "gridview")]//tr',
            
        }

    licenses_source_col = \
        {
            'DESC': 'Source column in the Licenses Table',
            'CSS_SELECTOR': 'td[xiqse-col-dindex="source"]',
            
        }

    licenses_feature_col = \
        {
            'DESC': 'Feature column in the Licenses Table',
            'CSS_SELECTOR': 'td[xiqse-col-dindex="feature"]',
            
        }

    licenses_type_col = \
        {
            'DESC': 'Type column in the Licenses Table',
            'CSS_SELECTOR': 'td[xiqse-col-dindex="licenseType"]',
            
        }

    licenses_quantity_col = \
        {
            'DESC': 'Quantity column in the Licenses Table',
            'CSS_SELECTOR': 'td[xiqse-col-dindex="formattedQuantity"]',
            
        }

    licenses_end_date_col = \
        {
            'DESC': 'End Date column in the Licenses Table',
            'CSS_SELECTOR': 'td[xiqse-col-dindex="formattedEndDate"]',
            
        }

    licenses_start_date_col = \
        {
            'DESC': 'Start Date column in the Licenses Table',
            'CSS_SELECTOR': 'td[xiqse-col-dindex="formattedStartDate"]',
            
        }

    licenses_description_col = \
        {
            'DESC': 'Description column in the Licenses Table',
            'CSS_SELECTOR': 'td[xiqse-col-dindex="description"]',
            
        }
