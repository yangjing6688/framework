from extauto.common.WebElementHandler import WebElementHandler
from xiqse.defs.analytics.configuration.AnalyticsConfigurationWebElementsDefinitions import AnalyticsConfigurationWebElementsDefinitions


class AnalyticsConfigurationWebElements(AnalyticsConfigurationWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_configuration_tab_add_engine_button(self):
        """
        :return: Add Engine Button on the Analytics Configuration panel
        """
        return self.weh.get_element(self.configuration_add_button)

    def get_delete_engine_button(self):
        """
        :return: Delete Engine Button on the Analytics Configuration panel
        """
        return self.weh.get_element(self.delete_engine_button)

    def get_enforce_engine_button(self):
        """
        :return: Enforce Engine Button on the Analytics Configuration panel
        """
        return self.weh.get_element(self.enforce_engine_button)

    def get_enforce_all_engine_button(self):
        """
        :return: Enforce All Engine Button on the Analytics Configuration panel
        """
        return self.weh.get_element(self.enforce_all_engine_button)

    def get_poll_engine_button(self):
        """
        :return: Poll Engine Button on the Analytics Configuration panel
        """
        return self.weh.get_element(self.poll_engine_button)

    def get_restart_collector_engine_button(self):
        """
        :return: Enforce All Engine Button on the Analytics Configuration panel
        """
        return self.weh.get_element(self.restart_collector_engine_button)

    def get_analytics_configuration_refresh_icon(self):
        """
        :return: Refresh icon in the configuration panel
        """
        elements = self.weh.get_elements(self.panel_refresh_icon)
        return self.weh.get_displayed_element(elements)

    def get_engines_table(self):
        """
        :return: The engines table
        """
        return self.weh.get_element(self.engines_table)

    def get_engine_table_rows(self):
        """
        :return: All the rows in the engines table
        """
        return self.weh.get_elements(self.engine_table_rows)

    def get_add_application_analytics_engine_dialog(self):
        """
        :return: Gets the dialog for 'Add Application Analytics Engine'
        """
        return self.weh.get_element(self.add_application_analytics_engine_dialog)

    def get_add_application_analytics_engine_dialog_cancel_button(self):
        """
        :return: Gets the cancel button for the 'Add Application Analytics Engine' dialog
        """
        return self.weh.get_element(self.add_application_analytics_engine_dialog_cancel_button)

    def get_enforcing_engine_load_mask(self):
        """
        :return: Gets the "Enforcing Engine..." load mask (from Enforce action) if displayed; else, None
        """
        elements = self.weh.get_elements(self.enforcing_engine_load_mask)
        return self.weh.get_displayed_element(elements)

    def get_enforcing_engines_load_mask(self):
        """
        :return: Gets the "Enforcing Engines..." load mask (from Enforce All action) if displayed; else, None
        """
        elements = self.weh.get_elements(self.enforcing_engines_load_mask)
        return self.weh.get_displayed_element(elements)

    def get_polling_engine_load_mask(self):
        """
        :return: Gets the "Polling Engine..." load mask (from Poll action) if displayed; else, None
        """
        elements = self.weh.get_elements(self.polling_engine_load_mask)
        return self.weh.get_displayed_element(elements)

    def get_restarting_collector_load_mask(self):
        """
        :return: Gets the "Restarting Collector..." load mask (from Restart Collector action) if displayed; else, None
        """
        elements = self.weh.get_elements(self.restarting_collector_load_mask)
        return self.weh.get_displayed_element(elements)
