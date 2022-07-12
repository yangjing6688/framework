

class ControlAccessControlCommonWebElementsDefinitions:

    click_innerel_button = \
        {
            'DESC': 'Clicking Button using btnInnerEl',
            'XPATH': '//span[@data-ref="btnInnerEl" and starts-with(text(), "${element_name}")]',
            
        }

    element_field = \
        {
            'DESC': 'Define XPATH using element id',
            'XPATH': '//*[@id="${element_name}"]',
            
        }

    tab_panel = \
        {
            'DESC': 'Selecting Tab in the right panel',
            'XPATH': '//div[starts-with(@id,"panel")]//span[@data-ref="btnInnerEl" and contains(@id, "tab") and starts-with(text(), "${element_name}")]',
            
        }