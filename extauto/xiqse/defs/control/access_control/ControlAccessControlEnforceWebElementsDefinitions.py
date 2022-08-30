

class ControlAccessControlEnforceWebElementsDefinitions:

    enforce_combo = \
        {
            'DESC': 'Enforce combo button selection',
            'XPATH': '//span[@data-ref="btnInnerEl" and text()="${element_name}"]',
            
        }

    nacenforce_combo_menu = \
        {
            'DESC': 'Menu pick from NAC enforce',
            'XPATH': '//span[contains(@id, "menuitem") and text()="${element_name}"]',
            
        }