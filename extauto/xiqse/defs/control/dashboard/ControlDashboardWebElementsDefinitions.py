

class ControlDashboardWebElementsDefinitions:

    dashboard_combo = \
        {
              'DESC': 'Dashboard Combo Menu for expansion using Text in the menu',
              'XPATH': '//span[@data-ref="btnInnerEl" and text()="${element_name}"]',
              
        }

    dashboard_combo_menu = \
        {
            'DESC': 'Dashboard Combo Menu using Text in the menu',
            'XPATH': '//span[contains(@id, "menuitem") and text()="${element_name}"]',
            
        }

    id_for_overview_label = \
        {
            'DESC': 'Element ID based on the label in Control Dashboard',
            'XPATH': '//div[contains(@id,"overviewPanel") and (@data-ref="bodyWrap")]/*//span[text()="${element_name}"]',
            
        }