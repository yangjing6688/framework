# ----------------------------------------------------------------------
# Copyright (C) 2021... 2021 Extreme Networks Inc.
# This software is copyright protected and may not be reproduced in any
# form or fashion without the written consent of Extreme Networks Inc.
# ----------------------------------------------------------------------
#
class AdminAuthorizedUsersWebElementsDefinitions:

    administration_users_conflict_dialog = \
        {
            'DESC': 'Administration > Users Conflict dialog',
            'XPATH': '//div[contains(@class, "x-title") and text()="Conflict"]/ancestor::div[contains(@class, "x-message-box") and @role="alertdialog"]',
            'wait_for': 10
        }

    delete_authorized_user_confirm_dialog_yes_button = \
        {
            'DESC': 'Yes button for the Administration > Users Conflict dialog',
            'XPATH': '//div[text()="Conflict"]/ancestor::div[contains(@class, "x-message-box")]//a//span[text()="Yes"]',
            'wait_for': 10
        }

    delete_authorized_user_confirm_dialog_no_button = \
        {
            'DESC': 'No button for the Administration > Users Conflict dialog',
            'XPATH': '//div[text()="Conflict"]/ancestor::div[contains(@class, "x-message-box")]//a//span[text()="No"]',
            'wait_for': 10
        }

    administration_users_lock_revoked_dialog = \
        {
            'DESC': 'Administration > Users Conflict dialog',
            'XPATH': '//div[text()="Lock Revoked"]/ancestor::div[contains(@class, "x-message-box") and @role="alertdialog"]',
            'wait_for': 10
        }

    administration_users_lock_revoked_dialog_ok_button = \
        {
            'DESC': 'Administration > Users Conflict dialog OK button',
            'XPATH': '//span[contains(@class,"x-btn-inner-blue-small") and text()="OK"]',
            'wait_for': 10
        }

    authorized_user_table_rows = \
        {
            'DESC': 'Administration > Users > Authorized Users Table Rows',
            'XPATH': '//div[contains(@id,"userGrid") and (@data-ref="body")]//tr',
            'wait_for': 10
        }

    authorized_user_add_button = \
        {
            'DESC': 'Add Authorized User toolbar button',
            'XPATH': '//div[contains(@id, "userGrid")]//span[text()="Add..."]/ancestor::a',
            'wait_for': 10
        }

    authorized_user_edit_button = \
        {
            'DESC': 'Edit Authorized User toolbar button',
            'XPATH': '//div[contains(@id, "userGrid")]//span[text()="Edit..."]/ancestor::a',
            'wait_for': 10
        }

    authorized_user_delete_button = \
        {
            'DESC': 'Delete Authorized User toolbar button',
            'XPATH': '//div[contains(@id, "userGrid")]//span[text()="Delete"]/ancestor::a',
            'wait_for': 10
        }
