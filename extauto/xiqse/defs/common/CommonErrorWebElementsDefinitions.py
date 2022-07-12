

class CommonErrorWebElementsDefinitions:

    connection_lost_error_dialog = \
        {
            'DESC': 'Connection to server lost error dialog',
            'XPATH': '//div[contains(@id, "messagebox")]//div[contains(text(), "Connection to server lost.")]',
            
        }

    session_terminated_dialog = \
        {
            'DESC': 'Session Terminated dialog',
            'XPATH': '//div[contains(@id, "messagebox")]//div[text()="Session Terminated"]',
            
        }

    message_box_ok_button = \
        {
            'DESC': 'OK Button for the Message Box',
            'XPATH': '//div[contains(@id, "messagebox")]//span[text()="OK"]',
            
        }

    message_box_yes_button = \
        {
            'DESC': 'Yes Button for the Message Box',
            'XPATH': '//div[contains(@id, "messagebox")]//span[text()="Yes"]',
            
        }
