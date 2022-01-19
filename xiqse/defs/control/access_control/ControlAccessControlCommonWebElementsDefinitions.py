

class ControlAccessControlCommonWebElementsDefinitions:

    click_innerel_button = \
        {
            'DESC': 'Clicking Button using btnInnerEl',
            'XPATH': '//span[@data-ref="btnInnerEl" and starts-with(text(), "${element_name}")]',
            'wait_for': 10
        }

    element_field = \
        {
            'DESC': 'Define XPATH using element id',
            'XPATH': '//*[@id="${element_name}"]',
            'wait_for': 10
        }

    tab_panel = \
        {
            'DESC': 'Selecting Tab in the right panel',
            'XPATH': '//div[starts-with(@id,"panel")]//span[@data-ref="btnInnerEl" and contains(@id, "tab") and starts-with(text(), "${element_name}")]',
            'wait_for': 10
        }