# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
class AdminAuthorizedUsersDeleteUserWebElementsDefinitions:

    confirm_delete_authorized_user_dialog = \
        {
            'DESC': 'Confirmation dialog for Delete Authorized User action',
            'XPATH': '//div[contains(@class, "x-title") and text()="Confirm Delete"]/ancestor::div[contains(@class, "x-message-box") and @role="alertdialog"]',
            'wait_for': 10
        }

    delete_authorized_user_confirm_dialog_yes_button = \
        {
            'DESC': 'Yes button for the Confirm Delete Authorized User dialog',
            'XPATH': '//div[text()="Confirm Delete"]/ancestor::div[contains(@class, "x-message-box")]//a//span[text()="Yes"]',
            'wait_for': 10
        }

    delete_authorized_user_confirm_dialog_no_button = \
        {
            'DESC': 'No button for the Confirm Delete Authorized User dialog',
            'XPATH': '//div[text()="Confirm Delete"]/ancestor::div[contains(@class, "x-message-box")]//a//span[text()="No"]',
            'wait_for': 10
        }
