from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.elements.admin.licenses.AdminLicensesWebElements import AdminLicensesWebElements
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.flows.admin.licenses.XIQSE_AdminLicensesAddLicense import XIQSE_AdminLicensesAddLicense


class XIQSE_AdminLicenses(AdminLicensesWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.view_el = CommonViewWebElements()
        self.xiqse_table = XIQSE_CommonTable()
        self.xiqse_add_license_dlg = XIQSE_AdminLicensesAddLicense()

    def xiqse_admin_licenses_add_legacy_license(self, legacy_license):
        """
        - Add License String in Add License Dialog on the Administration> Licenses page
        - Keyword Usage:
            - XIQSE ADMIN LICENSES ADD LEGACY LICENSE  <License String>
            - XIQSE ADMIN LICENSES ADD LEGACY LICENSE  ${get_license["${nac_license_type}"]}

        :return: returns 1 if action is successful, else -1
        """
        ret_val = -1

        add_btn = self.get_licenses_add_button()
        if add_btn:
            self.utils.print_info("Launching Add License Dialog Administration> Licenses Table")
            self.auto_actions.click(add_btn)

            ret_val = self.xiqse_add_license_dlg.xiqse_add_license_set_license(legacy_license)
            if ret_val != -1:
                ret_val = self.xiqse_add_license_dlg.xiqse_add_license_click_ok()
            else:
                self.utils.print_info("Problems entering license in Add License dialog")
                self.screen.save_screen_shot()
                self.xiqse_add_license_dlg.xiqse_add_license_click_cancel()

        else:
            self.utils.print_info("Unable to find Add License button from toolbar in Licenses page")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_admin_licenses_refresh_table(self):
        """
        - Refreshes the table on the Administration> Licenses page.

        :return: returns 1 if action is successful, else -1
        """
        ret_val = -1

        refresh_btn = self.get_licenses_refresh_button()
        if refresh_btn:
            self.utils.print_info("Refreshing Administration> Licenses Table")
            self.auto_actions.click(refresh_btn)
            self.xiqse_admin_licenses_wait_for_refresh_to_complete()
            ret_val = 1
        else:
            self.utils.print_info("Unable to find refresh button for the Administration> Licenses table")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_admin_licenses_wait_for_refresh_to_complete(self, retry_duration=2, retry_count=15):
        """
         - This keyword waits for the refresh to complete on the Licenses table
         - Keyword Usage
          - ``XIQSE Admin Licenses Wait For Refresh To Complete``
          - ``XIQSE Admin Licenses Wait For Refresh To Complete    retru_duration=5  retry_count=2``

        :param retry_duration: amount of time to wait in between each check for the refresh to be complete
        :param retry_count:    number of times to check for the search to be complete
        :return: 1 if action was successful, else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Waiting for Licenses table refresh to complete: loop {count}")
            load_mask = self.view_el.get_load_mask()
            if load_mask:
                self.utils.print_info(f"Refresh of Licenses table still in progress...")
                sleep(retry_duration)
            else:
                self.utils.print_info(f"Refresh of Licenses table has completed")
                return 1
            count += 1

        self.utils.print_info("Refresh did not complete within specified time")
        self.screen.save_screen_shot()
        return -1

    def xiqse_admin_licenses_show_columns(self, *columns):
        """
        - This keyword shows the specified list of columns if they are currently hidden.
        - Assumes already navigated to the Administration> Licenses view.
        -  Keyword Usage:
         - ``XIQSE Admin Licenses Show Columns        Feature  Start Date``

        :param columns: list of columns to show
        :return: returns 1 if successful. else -1
        """
        ret_val = -1

        self.utils.print_debug("Getting Source column header")
        the_col = self.get_licenses_source_col()
        if the_col:
            ret_val = self.xiqse_table.xiqse_table_show_columns(the_col, *columns)
        else:
            self.utils.print_info("Could not find Source column")
            self.screen.save_screen_shot()

        self.utils.print_debug("Closing Column Selection Menu")
        self.auto_actions.click(self.get_licenses_panel_title())

        return ret_val

    def xiqse_admin_licenses_hide_columns(self, *columns):
        """
        - This keyword hides the specified list of columns if they are currently shown.
        - Assumes already navigated to the Administration> Licenses view.
        -  Keyword Usage:
         - ``XIQSE Admin Licenses Hide Columns        Description  Start Date``

        :param columns: list of columns to show
        :return: returns 1 if successful. else -1
        """
        ret_val = -1

        self.utils.print_debug("Getting Source column header")
        the_col = self.get_licenses_source_col()
        if the_col:
            ret_val = self.xiqse_table.xiqse_table_hide_columns(the_col, *columns)
        else:
            self.utils.print_info("Could not find Source column")
            self.screen.save_screen_shot()

        self.utils.print_debug("Closing Column Selection Menu")
        self.auto_actions.click(self.get_licenses_panel_title())

        return ret_val

    def xiqse_get_license_quantity_for_feature(self, feature="XIQ-PIL-S-C"):
        """
        - Gets the license device count for the specified feature.
        - Keyword Usage:
         - ``${DEVICE_COUNT}=   Get License Device Count For Feature``
         - ``${DEVICE_COUNT}=   Get License Device Count For Feature    XIQ-PIL-S-C``
         - ``${DEVICE_COUNT}=   Get License Device Count For Feature    XIQ-NAV-S-C``
         - ``${DEVICE_COUNT}=   Get License Device Count For Feature    XIQ-NAC-S``

        :param feature: feature to return the device count for;  IQ-PIL-S-C or XIQ-NAV-S-C or XIQ-NAC-S
        :return: total number of devices allotted to the specified feature
        """
        license_count = 0

        table_row_list = self.get_licenses_table_rows()
        if table_row_list:
            self.utils.print_info(f"Got {len(table_row_list)} rows in Licenses table")

            for table_row in table_row_list:
                if table_row:
                    feature_val = self.get_licenses_feature_column_value_for_row(table_row)
                    if feature_val:
                        self.utils.print_debug(f"Feature: {feature_val.text}")
                        if feature_val.text == feature:
                            self.utils.print_debug(f"{feature_val.text} matches desired feature {feature}")

                            # Get the quantity value for the specified feature
                            quantity_val = self.get_licenses_quantity_column_value_for_row(table_row)
                            if quantity_val:
                                self.utils.print_debug(f"Quantity value is {quantity_val.text}")
                                license_count += int(quantity_val.text)
                            else:
                                self.utils.print_info("Unable to obtain 'Quantity' column value")
                                self.screen.save_screen_shot()
                        else:
                            self.utils.print_debug(f"{feature_val.text} does not match desired feature {feature}")
                    else:
                        self.utils.print_info("Unable to obtain 'Feature' column value")
                        self.screen.save_screen_shot()
        else:
            self.utils.print_info("Licenses table is empty")
            self.screen.save_screen_shot()

        self.utils.print_info(f"Returning quantity {license_count} for feature {feature}")
        return license_count
