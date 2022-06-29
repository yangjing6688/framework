

class DialogWebElementsDefinitions:
    dialog_title_label = \
        {'CLASS_NAME': 'dijitDialogTitle',
         'wait_for': 10
         }

    dialog_box = \
        {'CSS_SELECTOR': '.quick-onboard-dialog.dijitDialogFixed.dijitDialog',
         'wait_for': 10
        }

    dialog_message = \
        {'CSS_SELECTOR': '.ui-dialog-content.quick-failure-ctn',
         'wait_for': 10
         }

    dialog_ok_button = \
        {
         'XPATH': "//*[@data-dojo-attach-point='okBtn']",
         'wait_for': 5
         }

    tooltip = \
        {'CSS_SELECTOR': '.ui-tipbox-title',
         'wait_for': 5
         }

    confirm_yes_button = \
        {
            'XPATH': "//*[@data-dojo-attach-point='yesBtn']",
            'wait_for': 5
        }

    confirm_cancel_button = \
        {
            'XPATH': "//button[@data-dojo-attach-point='noBtn']",
            'wait_for': 5
        }

    confirm_deploy_button = \
        {
            'XPATH': "//button[@data-dojo-attach-point='deployBtn']",
            'wait_for': 5
        }

    confirm_yes_button_reboot = \
        {
            'XPATH': "//button[@class='btn btn-secondary']",
            'wait_for': 5
        }
