class ApSpecificSearchWebElementsDefinition:
    ap_specific_searchicon = \
        {
            'XPATH': "//*[@data-dojo-attach-point='searchBtn']",
             'wait_for': 5
        }

    ap_specific_textbox = \
        {
            'XPATH': "//*[@data-dojo-attach-point='deviceSearchInput']",
            'wait_for': 5

        }
    ap_result_list = \
        {
            'XPATH': "//*[@class='dgrid-content']",
            'wait_for': 5
        }


