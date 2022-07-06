class GlobalSettingWebElementDefinitions:
    backup_logs_grid_rows = \
        {
            'XPATH': '//*[@id="blacklistTbl"]',
            #'CSS_SELECTOR': '#blacklistTbl > div:nth-child(2)',
            
        }

    audit_logs_grid_rows = \
        {
            'XPATH': '//table',
            # 'CSS_SELECTOR': '#blacklistTbl > div:nth-child(2)',
            
         }

    clients_search_rows = \
        {
            'XPATH': '//table',
            # 'CSS_SELECTOR': '#blacklistTbl > div:nth-child(2)',
            
         }

    logs_grid_rows = \
        {
            #'XPATH': '///div[@class="table-responsive"]//table[@class="table b-table table-striped table-hover"]',
            'XPATH': '//*[@role="table"]',
            #'CSS_SELECTOR': '#blacklistTbl > div:nth-child(2)',
            
        }

    log_rows = \
        {
            'XPATH': '//div[@class="table-responsive"]//table[@class="table b-table table-striped table-hover"]',
            'wait_for': 5
        }

    create_button = \
        {
            'XPATH': '//*[@data-automation-tag="saveButton"]',
            'wait_for': 2
        }

    reset_button = \
        {
            'XPATH': '//*[@data-automation-tag="resetButton"]',
            'wait_for': 2
        }

    role_create_button = \
        {
            'XPATH': '//button[text()=" Create "]',
            'wait_for': 2
        }

    close_button = \
        {
            'XPATH': '//button[@title = "Close [ESC]"]',
            'wait_for': 2
        }
