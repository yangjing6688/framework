# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.XMC.webapp.baseappver.webapp \
    import Webapp as AnalyticsBase


class Analytics(AnalyticsBase):
    def select_apptelemetry_source(self, ui_cmd_obj, arg_dict):
        # self.builder.click(ui_cmd_obj, "div.fa-ellipsis-h-default", self.builder.constants.STRATEGY_CSS_SELECTOR)
        self.builder.driver.find_element_by_css_selector("div.fa-ellipsis-h-default").click()
        self._wait_for_dialog_window(ui_cmd_obj, "selectDeviceActionDialog")
        self._select_tree_node_item(ui_cmd_obj, arg_dict["tree_node"], "div[id^='deviceSelectionTree']>div>div>table")

        return ui_cmd_obj

    def collapse_all_config_tree_nodes(self, ui_cmd_obj, arg_dict):
        self._invoke_popup_menu(ui_cmd_obj, "div[id^='analyticsConfigurationTreePanel']>div>div>table:nth-child(1)")
        self._click_link_text(ui_cmd_obj, "Collapse All")

        return ui_cmd_obj

    def verify_flow_sources_added(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("Verify expected result")
        flag = self._find_a_row_from_grid(ui_cmd_obj, arg_dict["device_ip"], "div[id^='appIdSFlowSourcesPanel']"
                                                                             ">div>div>div.x-grid-with-row-lines>div>"
                                                                             "div.x-grid-item-container>table")
        # Verify device IP is found on the grid
        if flag == 1:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

            self.logger.log_info("Expected result is NOT found in Actual result... Please check screenshot.")

        return ui_cmd_obj
