from time import sleep
from common.Utils import Utils
from common.Screen import Screen
from common.AutoActions import AutoActions
from xiqse.flows.common.XIQSE_CommonTable import XIQSE_CommonTable
from xiqse.elements.analytics.configuration.AnalyticsConfigurationWebElements import AnalyticsConfigurationWebElements
from xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationAddEngine import XIQSE_AnalyticsConfigurationAddEngine
from xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationDeleteEngine import XIQSE_AnalyticsConfigurationDeleteEngine
from xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationEnforceEngine import XIQSE_AnalyticsConfigurationEnforceEngine
from xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationEnforceAllEngines import XIQSE_AnalyticsConfigurationEnforceAllEngines
from xiqse.flows.analytics.configuration.XIQSE_AnalyticsConfigurationRestartCollector import XIQSE_AnalyticsConfigurationRestartCollector
from selenium.common.exceptions import StaleElementReferenceException


class XIQSE_AnalyticsConfiguration(AnalyticsConfigurationWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.xiqse_table = XIQSE_CommonTable()
        self.add_analytics_engine_dlg = XIQSE_AnalyticsConfigurationAddEngine()
        self.delete_analytics_engine_dlg = XIQSE_AnalyticsConfigurationDeleteEngine()
        self.enforce_analytics_engine_dlg = XIQSE_AnalyticsConfigurationEnforceEngine()
        self.enforce_all_analytics_engine_dlg = XIQSE_AnalyticsConfigurationEnforceAllEngines()
        self.restart_collector_analytics_engine_dlg = XIQSE_AnalyticsConfigurationRestartCollector()
        self.enforce_engine_error_dlg = XIQSE_AnalyticsConfigurationEnforceEngine()
        self.enforce_all_engines_error_dlg = XIQSE_AnalyticsConfigurationEnforceAllEngines()
        self.restart_collector_error_dlg = XIQSE_AnalyticsConfigurationRestartCollector()

    def xiqse_analytics_click_add_engine_button(self):
        """
         - This keyword clicks the Add button in the Analytics->Configuration panel.
         - It is assumed the user is already in the Analytics> Configuration panel.
         - Keyword Usage
          - ``XIQSE Analytics Click Add Engine Button``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        add_btn = self.get_configuration_tab_add_engine_button()
        if add_btn:
            self.utils.print_info("Clicking Add button in Analytics Configuration panel")
            self.auto_actions.click(add_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'Add...' button in Analytics Configuration panel")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_analytics_click_delete_engine_button(self):
        """
         - This keyword clicks the Delete button in the Analytics->Configuration panel.
         - It is assumed the user is already in the Analytics> Configuration panel.
         - Keyword Usage
          - ``XIQSE Analytics Click Delete Engine Button``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        delete_btn = self.get_delete_engine_button()
        if delete_btn:
            self.utils.print_info("Clicking Delete button in Analytics Configuration panel")
            self.auto_actions.click(delete_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'Delete' button in Analytics Configuration panel")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_analytics_click_enforce_engine_button(self):
        """
         - This keyword clicks the Enforce button in the Analytics->Configuration panel.
         - It is assumed the user is already in the Analytics> Configuration panel.
         - Keyword Usage
          - ``XIQSE Analytics Click Enforce Engine Button``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        enforce_btn = self.get_enforce_engine_button()
        if enforce_btn:
            self.utils.print_info("Clicking Enforce button in Analytics Configuration panel")
            self.auto_actions.click(enforce_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'Enforce' button in Analytics Configuration panel")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_analytics_click_enforce_all_engine_button(self):
        """
         - This keyword clicks the Enforce All button in the Analytics->Configuration panel.
         - It is assumed the user is already in the Analytics> Configuration panel.
         - Keyword Usage
          - ``XIQSE Analytics Click Enforce All Engine Button``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        enforce_all_btn = self.get_enforce_all_engine_button()
        if enforce_all_btn:
            self.utils.print_info("Clicking Enforce All button in Analytics Configuration panel")
            self.auto_actions.click(enforce_all_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'Enforce All' button in Analytics Configuration panel")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_analytics_click_poll_engine_button(self):
        """
         - This keyword clicks the Poll button in the Analytics->Configuration panel.
         - It is assumed the user is already in the Analytics> Configuration panel.
         - Keyword Usage
          - ``XIQSE Analytics Click Poll Engine Button``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        poll_btn = self.get_poll_engine_button()
        if poll_btn:
            self.utils.print_info("Clicking Poll button in Analytics Configuration panel")
            self.auto_actions.click(poll_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'Poll' button in Analytics Configuration panel")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_analytics_click_restart_collector_engine_button(self):
        """
         - This keyword clicks the Restart Collector button in the Analytics->Configuration panel.
         - It is assumed the user is already in the Analytics> Configuration panel.
         - Keyword Usage
          - ``XIQSE Analytics Click Restart Collector Engine Button``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        restart_collector_btn = self.get_restart_collector_engine_button()
        if restart_collector_btn:
            self.utils.print_info("Clicking Restart Collector button in Analytics Configuration panel")
            self.auto_actions.click(restart_collector_btn)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find 'Restart Collector' button in Analytics Configuration panel")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_select_engine(self, engine_ip):
        """
         - This keyword selects the specified engine.
         - It is assumed the user is already on the Analytics> Configuration tab.
         - Keyword Usage
          - ``XIQSE Select Engine    ${NEXTGEN_IP}``

        :param engine_ip: IP address of the engine to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1
        self.utils.print_info(f"Selecting engine with IP {engine_ip}")

        stale_retry = 1
        while stale_retry <= 10:
            try:
                rows = self.get_engine_table_rows()
                if rows:
                    for row in rows:
                        if engine_ip in row.text:
                            self.utils.print_debug(f"Found engine {engine_ip} in row {self.xiqse_table.format_table_row(row.text)}")
                            row_selected = row.get_attribute("aria-selected")
                            if row_selected and row_selected == "true":
                                self.utils.print_info(f"Row for engine {engine_ip} is already selected")
                            else:
                                self.utils.print_info(f"Selecting engine {engine_ip}")
                                self.auto_actions.click(row)
                            ret_val = 1
                            break

                    # Break out of the Stale Element Exception loop
                    break
                else:
                    self.utils.print_info("No rows are present")
                    break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        if ret_val == -1:
            self.utils.print_info(f"Unable to select engine {engine_ip}")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_analytics_configuration_refresh_panel(self):
        """
         - This keyword clicks the refresh icon on the toolbar.
         - Keyword Usage
          - ``XIQSE Analytics Configuration Refresh Panel``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        the_btn = self.get_analytics_configuration_refresh_icon()
        if the_btn:
            self.utils.print_info("Clicking Refresh icon")
            self.auto_actions.click(the_btn)
            sleep(5)
            ret_val = 1
        else:
            self.utils.print_info("Unable to find Refresh icon")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_add_analytics_engine(self, engine_ip, engine_name, engine_profile):
        """
         - This keyword adds an analytics engine to the Analytics Configuration panel.
         - It is assumed the user is already on the Analytics> Configuration> tab.
         - Keyword Usage
          - ``XIQSE Add Analytics Engine    ${NEXTGEN_IP}  ${NEXTGEN_NAME}  ${APPLIANCE_PROFILE}``

        :param engine_ip:        IP address of the analytics engine to add
        :param engine_name:      Value to enter into the Name field
        :param engine_profile:   Value to enter into the Profile field
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        add_btn = self.get_configuration_tab_add_engine_button()
        if add_btn:
            self.utils.print_info("Clicking Add toolbar button")
            self.auto_actions.click(add_btn)
            sleep(2)

            # Enter IP Address
            ret_val = self.add_analytics_engine_dlg.xiqse_add_analytics_engine_dialog_set_ip(engine_ip)

            # Enter Name
            if ret_val != -1:
                ret_val = self.add_analytics_engine_dlg.xiqse_add_analytics_engine_dialog_set_name(engine_name)

            # Select Profile
            if ret_val != -1:
                ret_val = self.add_analytics_engine_dlg.xiqse_add_analytics_engine_dialog_set_profile(engine_profile)

            # Click OK
            if ret_val != -1:
                sleep(2)
                ret_val = self.add_analytics_engine_dlg.xiqse_add_engine_dialog_click_ok()
            else:
                self.utils.print_info("Problems entering information into Add Engine dialog")
                self.screen.save_screen_shot()
                self.add_analytics_engine_dlg.xiqse_add_engine_dialog_click_cancel()
        else:
            self.utils.print_info("Unable to find Add toolbar button")
            self.screen.save_screen_shot()
            ret_val = -1

        return ret_val

    def xiqse_delete_selected_engine(self, engine_ip):
        """
         - This keyword deletes the currently-selected engine.
         - It is assumed the user is already on the Analytics> Configuration tab and the engine to delete is selected.
         - Keyword Usage
           - ``XIQSE Delete Engine    ${NEXTGEN_IP}``
           - ``XIQSE Delete Engine    ${NEXTGEN_IP}    false``

        :param engine_ip: IP address of the engine to select
        :return: 1 if action was successful, else -1
        """
        ret_val = 1

        # Select engine in table, click Delete button and click Yes
        if self.xiqse_select_engine(engine_ip) == 1:
            delete_btn = self.get_delete_engine_button()
            if delete_btn:
                self.utils.print_info("Clicking Delete toolbar button")
                self.auto_actions.click(delete_btn)
                sleep(1)

                if self.delete_analytics_engine_dlg.xiqse_delete_engine_dialog_click_yes() == 1:
                    sleep(2)
                    self.xiqse_close_add_application_analytics_engine_dialog()
                    ret_val = 1
                else:
                    self.utils.print_info("Unable to click Yes button")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to find Delete button")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to select engine")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_enforce_selected_engine(self, engine_ip):
        """
         - This keyword enforces the currently-selected engine.
         - It is assumed the user is already on the Analytics> Configuration tab and the engine to enforce is selected.
         - Keyword Usage
           - ``XIQSE Enforce Selected Engine    ${NEXTGEN_IP}``

        :param engine_ip: IP address of the engine to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # Select engine in table, click Enforce button and click Yes
        if self.xiqse_select_engine(engine_ip) == 1:
            enforce_btn = self.get_enforce_engine_button()
            if enforce_btn:
                self.utils.print_info("Clicking Enforce toolbar button")
                self.auto_actions.click(enforce_btn)
                sleep(1)

                if self.enforce_analytics_engine_dlg.xiqse_enforce_engine_dialog_click_yes() == 1:
                    ret_val = self.xiqse_wait_for_enforce_to_complete()

                    # Close the error dialog if an error occurred
                    if self.enforce_engine_error_dlg.xiqse_close_enforce_engine_error_dialog() == -1:
                        ret_val = -1
                        self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Unable to click Yes button")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to find Enforce button")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to select engine")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_enforce_all_engines(self):
        """
         - This keyword enforces all engines.
         - It is assumed the user is already on the Analytics> Configuration tab
         - Keyword Usage
           - ``XIQSE Enforce All Engines``

        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # Click Enforce All button and click Yes
        enforce_all_btn = self.get_enforce_all_engine_button()
        if enforce_all_btn:
            self.utils.print_info("Clicking Enforce All toolbar button")
            self.auto_actions.click(enforce_all_btn)
            sleep(1)

            if self.enforce_all_analytics_engine_dlg.xiqse_enforce_all_engines_dialog_click_yes() == 1:
                ret_val = self.xiqse_wait_for_enforce_all_to_complete()

                # Close the error dialog if an error occurred
                if self.enforce_all_engines_error_dlg.xiqse_close_enforce_engines_error_dialog() == -1:
                    ret_val = -1
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to click Yes button")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to find Enforce All button")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_poll_selected_engine(self, engine_ip):
        """
         - This keyword polls the currently-selected engine.
         - It is assumed the user is already on the Analytics> Configuration tab and the engine to poll is selected.
         - Keyword Usage
           - ``XIQSE Poll Selected Engine    ${NEXTGEN_IP}``

        :param engine_ip: IP address of the engine to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # Select engine in table, click Poll button
        if self.xiqse_select_engine(engine_ip) == 1:
            poll_btn = self.get_poll_engine_button()
            if poll_btn:
                self.utils.print_info("Clicking Poll toolbar button")
                self.auto_actions.click(poll_btn)
                ret_val = self.xiqse_wait_for_poll_to_complete()
            else:
                self.utils.print_info("Unable to find Poll button")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to select engine")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_restart_collector_selected_engine(self, engine_ip):
        """
         - This keyword restarts collector on the currently-selected engine.
         - It is assumed the user is already on the Analytics> Configuration tab and the engine to restart is selected.
         - Keyword Usage
           - ``XIQSE Restart Collector Selected Engine    ${NEXTGEN_IP}``

        :param engine_ip: IP address of the engine to select
        :return: 1 if action was successful, else -1
        """
        ret_val = -1

        # Select engine in table, click Restart Collector button
        if self.xiqse_select_engine(engine_ip) == 1:
            restart_collector_btn = self.get_restart_collector_engine_button()
            if restart_collector_btn:
                self.utils.print_info("Clicking Restart Collector toolbar button")
                self.auto_actions.click(restart_collector_btn)
                sleep(1)
                if self.restart_collector_analytics_engine_dlg.xiqse_restart_collector_dialog_click_yes() == 1:
                    ret_val = self.xiqse_wait_for_restart_collector_to_complete()

                    # Close the error dialog if an error occurred
                    if self.restart_collector_error_dlg.xiqse_close_restart_collector_error_dialog() == -1:
                        ret_val = -1
                        self.screen.save_screen_shot()
                else:
                    self.utils.print_info("Unable to click Yes button")
                    self.screen.save_screen_shot()
            else:
                self.utils.print_info("Unable to find Restart Collector button")
                self.screen.save_screen_shot()
        else:
            self.utils.print_info("Unable to select engine")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_wait_until_engine_added(self, engine_ip, retry_duration=10, retry_count=30):
        """
        - This keyword is used to wait for the engine to show up in the configuration panel.
        - This keyword by default loops 10 times every 30 seconds to check if the engine exists.
        - It is assumed the Analytics> Configuration tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Engine Added    ${NEXTGEN_IP}    retry_duration=30    retry_count=12``

        :param engine_ip: engine IP to look for
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if engine added within time; else -1
        """
        self.xiqse_analytics_configuration_refresh_panel()
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Searching for engine {engine_ip}: loop {count}")
            if self.xiqse_find_engine_with_ip(engine_ip) == 1:
                self.utils.print_info(f"Engine {engine_ip} has been added")
                return 1
            else:
                self.utils.print_info(f"Engine is not yet present. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
                self.xiqse_analytics_configuration_refresh_panel()
            count += 1

        # Check for engine one last time
        self.xiqse_analytics_configuration_refresh_panel()
        if self.xiqse_find_engine_with_ip(engine_ip) == 1:
            self.utils.print_info(f"Engine {engine_ip} has been added")
            return 1

        self.utils.print_info(f"Engine does not exist. Please check.")
        self.screen.save_screen_shot()
        return -1

    def xiqse_wait_until_engine_deleted(self, engine_ip, retry_duration=10, retry_count=30):
        """
        - This keyword is used to wait for the engine to be deleted from the configuration panel.
        - This keyword by default loops 10 times every 30 seconds to check if the engine exists.
        - It is assumed the Analytics> Configuration tab is already selected.
        - Keyword Usage:
         - ``XIQSE Wait Until Engine Deleted    ${NEXTGEN_IP}    retry_duration=30    retry_count=12``
        :param engine_ip: engine IP to look for
        :param retry_duration: duration between each retry
        :param retry_count: retry count
        :return: 1 if engine added within time; else -1
        """
        self.xiqse_analytics_configuration_refresh_panel()
        self.xiqse_close_add_application_analytics_engine_dialog()
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Searching for engine {engine_ip}: loop {count}")
            if self.xiqse_find_engine_with_ip(engine_ip) != 1:
                self.utils.print_info(f"Engine {engine_ip} has been deleted")
                return 1
            else:
                self.utils.print_info(f"Engine is still present. Waiting for {retry_duration} seconds...")
                sleep(retry_duration)
                self.xiqse_analytics_configuration_refresh_panel()
            count += 1

        # Check for engine one last time
        self.xiqse_analytics_configuration_refresh_panel()
        if self.xiqse_find_engine_with_ip(engine_ip) != 1:
            self.utils.print_info(f"Engine {engine_ip} has been deleted")
            return 1

        self.utils.print_info(f"Engine was not deleted")
        self.screen.save_screen_shot()
        return -1

    def xiqse_find_engine_with_ip(self, engine_ip):
        """
        - Searches for Engine matching Engine's IP Address

        :param engine_ip: Engine IP Address to search for
        :return: return 1 if engine with specified IP address is found, else -1
        """
        ret_val = -1

        row = self.xiqse_get_engine_row(engine_ip)
        if row:
            ret_val = 1
        return ret_val

    def xiqse_get_engine_row(self, engine_ip):
        """
        - This keyword returns the row for the engine matching the IP address

        :param engine_ip: IP address of the engine to obtain the row for
        :return: returns the row object
        """
        self.utils.print_info(f'Getting engine row for engine with IP address {engine_ip}')

        stale_retry = 1
        while stale_retry <= 10:
            try:
                rows = self.get_engine_table_rows()
                if rows:
                    for row in rows:
                        if engine_ip in row.text:
                            self.utils.print_info(f"Found engine row for {engine_ip}: {self.xiqse_table.format_table_row(row.text)}")
                            return row
                    # Break out of the Stale Element Exception loop
                    break
                else:
                    self.utils.print_info("No rows are present")
                    break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        self.utils.print_info(f"Unable to find engine row in grid for IP address {engine_ip}")
        self.screen.save_screen_shot()
        return None

    def xiqse_close_add_application_analytics_engine_dialog(self):
        """
         - This keyword closes the Add Application Analytics Engine dialog which may appear when first navigating to Analytics -> Configuration panel and no engines exist
         - Keyword Usage
          - ``XIQSE Close Add Application Analytics Engine Dialog``

        :return: 1 if action successful, else -1
        """
        ret_val = 1
        the_dialog = self.get_add_application_analytics_engine_dialog()
        if the_dialog and the_dialog.is_displayed:
            cancel_btn = self.get_add_application_analytics_engine_dialog_cancel_button()
            if cancel_btn:
                self.utils.print_info("Closing 'Add Application Analytics Engine' dialog")
                self.auto_actions.click(cancel_btn)
                sleep(1)
                ret_val = 1
            else:
                self.utils.print_info("Could not find cancel button for 'Add Application Analytics Engine' dialog")
                self.screen.save_screen_shot()
                ret_val = -1
        else:
            self.utils.print_info("'Add Application Analytics Engine' dialog not displayed")
            self.screen.save_screen_shot()

        return ret_val

    def xiqse_wait_for_enforce_to_complete(self, retry_duration=10, retry_count=30):
        """
         - This keyword waits for the Enforce action to complete.
         - Keyword Usage
          - ``XIQSE Wait For Enforce To Complete``

        :param retry_duration: amount of time to wait in between each check for the enforce action to be complete
        :param retry_count:    number of times to check for the enforce action to be complete
        :return: 1 if action was successful, else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Waiting for Enforce action to complete: loop {count}")
            load_mask = self.get_enforcing_engine_load_mask()
            if load_mask:
                self.utils.print_info(f"Enforce action still in progress...")
                sleep(retry_duration)
            else:
                self.utils.print_info(f"Enforce action has completed")
                return 1
            count += 1

        self.utils.print_info("Enforce action did not complete within specified time")
        self.screen.save_screen_shot()
        return -1

    def xiqse_wait_for_enforce_all_to_complete(self, retry_duration=10, retry_count=30):
        """
         - This keyword waits for the Enforce All action to complete.
         - Keyword Usage
          - ``XIQSE Wait For Enforce All To Complete``

        :param retry_duration: amount of time to wait in between each check for the enforce all action to be complete
        :param retry_count:    number of times to check for the enforce all action to be complete
        :return: 1 if action was successful, else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Waiting for Enforce All action to complete: loop {count}")
            load_mask = self.get_enforcing_engines_load_mask()
            if load_mask:
                self.utils.print_info(f"Enforce All action still in progress...")
                sleep(retry_duration)
            else:
                self.utils.print_info(f"Enforce All action has completed")
                return 1
            count += 1

        self.utils.print_info("Enforce All action did not complete within specified time")
        self.screen.save_screen_shot()
        return -1

    def xiqse_wait_for_poll_to_complete(self, retry_duration=10, retry_count=30):
        """
         - This keyword waits for the Poll action to complete.
         - Keyword Usage
          - ``XIQSE Wait For Poll To Complete``

        :param retry_duration: amount of time to wait in between each check for the poll action to be complete
        :param retry_count:    number of times to check for the poll action to be complete
        :return: 1 if action was successful, else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Waiting for Poll action to complete: loop {count}")
            load_mask = self.get_polling_engine_load_mask()
            if load_mask:
                self.utils.print_info(f"Poll action still in progress...")
                sleep(retry_duration)
            else:
                self.utils.print_info(f"Poll action has completed")
                return 1
            count += 1

        self.utils.print_info("Poll action did not complete within specified time")
        self.screen.save_screen_shot()
        return -1

    def xiqse_wait_for_restart_collector_to_complete(self, retry_duration=10, retry_count=30):
        """
         - This keyword waits for the Restart Collector action to complete.
         - Keyword Usage
          - ``XIQSE Wait For Restart Collector To Complete``

        :param retry_duration: amount of time to wait in between each check for the restart collector action to be complete
        :param retry_count:    number of times to check for the restart collector action to be complete
        :return: 1 if action was successful, else -1
        """
        count = 1
        while count <= retry_count:
            self.utils.print_info(f"Waiting for Restart Collector action to complete: loop {count}")
            load_mask = self.get_restarting_collector_load_mask()
            if load_mask:
                self.utils.print_info(f"Restart Collector action still in progress...")
                sleep(retry_duration)
            else:
                self.utils.print_info(f"Restart Collector action has completed")
                return 1
            count += 1

        self.utils.print_info("Restart Collector action did not complete within specified time")
        self.screen.save_screen_shot()
        return -1
