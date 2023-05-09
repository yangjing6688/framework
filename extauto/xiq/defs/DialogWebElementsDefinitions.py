

class DialogWebElementsDefinitions:
    dialog_title_label = \
        {
            'CLASS_NAME': 'dijitDialogTitle',
         }

    dialog_box = \
        {
            'CSS_SELECTOR': '.quick-onboard-dialog.dijitDialogFixed.dijitDialog',
        }

    dialog_message = \
        {
            'CSS_SELECTOR': '.ui-dialog-content.quick-failure-ctn',
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

    confirm_message_dialog_box = \
        {
            'CSS_SELECTOR': '.ui-cfmsg.confirm',
            'wait_for': 3
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

    tooltip_close_button = \
        {
            'XPATH': "//div[@class='ui-tipbox ui-tipbox-error']//i[@class='ui-tipbox-close']",
        }