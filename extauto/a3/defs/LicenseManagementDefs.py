class LicenseManagementDefs:

    cluster_id = \
        {
            'CSS_SELECTOR': '.systemid-title-div-license',
            'index': 0
        }

    system_id = \
        {
            'CSS_SELECTOR': '.systemid-title-div-license',
            'index': 1
        }

    licensed_capacity = \
        {
            'XPATH': '//div[@class="pad"]//div[@id="licenseCapaSpan"]//*[@id="licenseCapa"]'
        }

    used_capacity = \
        {
            'XPATH': '//div[@class="pad1"]//div[@id="usedCapacitySpan"]//*[@id="usedCapacity"]'
        }

    average_used_capacity = \
        {
            'XPATH': '//div[@class="pad2"]//div[@id="currCapacitySpan"]//*[@id="currCapacity"]'
        }

    license_management_table = \
        {
            'CSS_SELECTOR': '.ivu-table'
        }

    license_management_table_row = \
        {
            'CSS_SELECTOR': '.ivu-table-row'
        }

    license_management_table_cell = \
        {
            'CSS_SELECTOR': '.ivu-table-column-left'
        }



