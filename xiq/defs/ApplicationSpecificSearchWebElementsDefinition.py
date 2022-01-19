class ApplicationSpecificSearchWebElementsDefinition:
    configure_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-header-configure']",
            'wait_for': 5
        }
    configure_application_button = \
        {
            'XPATH': "//*[@data-automation-tag='automation-nav-application']",
            'wait_for': 5
        }

    app_text_box = \
        {
            'XPATH': "//*[@data-dojo-attach-point='txtFilterNode']",
            'wait_for': 5
        }

    app_result = \
        {
            'XPATH': "//*[@class='ml10']",
            'wait_for': 5
        }

    warning_result = \
        {
            'XPATH': "//*[@class='ui-tipbox-title font16 fw500 blackC']",
            'wait_for': 5
        }

    warning_close = \
        {
            'XPATH': "//*[@data-dojo-attach-point='btnContainer']",
            'wait_for': 5
        }
