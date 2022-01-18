# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.XMC.webapp.baseappver.webapp \
    import Webapp as GovernanceBase


class Governance(GovernanceBase):

    def add_regime(self, ui_cmd_obj, arg_dict):
        # Click on Add Regime button
        # self._click_on_button(ui_cmd_obj, "Add Regime")
        # self.builder.driver.find_element_by_css_selector("a[id='governanceLeftPanel_header-title']").click()
        self.builder.click(ui_cmd_obj, "a[id='governanceLeftPanel_header-title']",
                           self.builder.constants.STRATEGY_CSS_SELECTOR)
        # Enter name and description
        self._enter_regime_details(ui_cmd_obj, arg_dict["regime_name"], arg_dict["regime_desc"])

        return ui_cmd_obj

    def select_regime(self, ui_cmd_obj, arg_dict):
        # self._select_tree_node_item(ui_cmd_obj, arg_dict["regime_name"], "div#governanceLeftPanel-body>div>div>table")

        # get all regimes instance
        regimes = self.builder.find_elements(ui_cmd_obj, "//div[@id='governanceLeftPanel-body']//div[@role='rowgroup']"
                                                         "//div//table")
        # iterate through regimes
        for regime in regimes:
            if arg_dict["regime_name"] == regime.text.strip():
                regime.click()
                break
        self._wait_for_loading(ui_cmd_obj, 60)

        return ui_cmd_obj

    def run_regime(self, ui_cmd_obj, arg_dict):
        """Run Regime"""
        row = 0

        # get all regimes instance
        regimes = self.builder.find_elements(ui_cmd_obj, "//div[@id='governanceLeftPanel-body']//div[@role='rowgroup']"
                                                         "//div//table")
        # iterate through regimes
        for regime in regimes:
            row += 1
            if arg_dict["regime_name"] == regime.text.strip():
                regime.click()
                self._wait_for_loading(ui_cmd_obj, 60)
                # Click on Run Regime button
                self.builder.driver.find_element_by_css_selector(
                    "div#governanceLeftPanel-body>div>div>table:nth-child(" + str(
                        row) + ")>tbody>tr>td:nth-child(2)").click()
                break

        return ui_cmd_obj

    def edit_regime(self, ui_cmd_obj, arg_dict):
        row = 0
        # get all regimes instance
        regimes = self.builder.find_elements(ui_cmd_obj, "//div[@id='governanceLeftPanel-body']//div[@role='rowgroup']"
                                                         "//div//table")
        # iterate through regimes
        for regime in regimes:
            row += 1
            if arg_dict["regime_name"] == regime.text.strip():
                regime.click()
                self._wait_for_loading(ui_cmd_obj, 60)
                # Click on Edit Regime button
                self.builder.driver.find_element_by_css_selector(
                    "div#governanceLeftPanel-body>div>div>table:nth-child(" + str(
                        row) + ")>tbody>tr>td:nth-child(3)").click()
                break

        return ui_cmd_obj

    def delete_regime(self, ui_cmd_obj, arg_dict):
        row = 0
        # get all regimes instance
        regimes = self.builder.find_elements(ui_cmd_obj, "//div[@id='governanceLeftPanel-body']//div[@role='rowgroup']"
                                                         "//div//table")
        # iterate through regimes
        for regime in regimes:
            row += 1
            if arg_dict["regime_name"] == regime.text.strip():
                regime.click()
                self._wait_for_loading(ui_cmd_obj, 60)
                # Click on Delete Regime button
                self.builder.driver.find_element_by_css_selector(
                    "div#governanceLeftPanel-body>div>div>table:nth-child(" + str(
                        row) + ")>tbody>tr>td:nth-child(4)").click()
                break

        # Confirm delete
        self._click_on_button(ui_cmd_obj, "Yes")

        return ui_cmd_obj

    def select_and_move_single_device(self, ui_cmd_obj, arg_dict):
        # Expand a All Devices node
        self.builder.driver.find_element_by_css_selector("div[id^='deviceSelectionTree']>div>div>div>div."
                                                         "x-grid-item-container>table:nth-child(2)>tbody>tr>td>div>"
                                                         "div.x-tree-expander").click()
        self._move_mouse_out_of(ui_cmd_obj, "CSS", "div[id^='deviceSelectionTree']")
        # Select a device from tree view
        self._select_tree_node_item(ui_cmd_obj, arg_dict["tree_node"], "div[id^='deviceSelectionTree']>div>div>div>"
                                                                       "div.x-grid-item-container>table")
        # Move selected device into Test Devices
        self.builder.driver.find_element_by_css_selector("a[data-qtip='Move selected from tree to list']").click()

        return ui_cmd_obj

    def verify_regime_exists(self, ui_cmd_obj, arg_dict):
        exists = self._select_regime(ui_cmd_obj, arg_dict["regime_name"])
        # Verify if regime exists
        if arg_dict["flag"].lower() == "true":
            if exists == "true":
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True

            self.logger.log_info("EXPECTED RESULT: true")
            self.logger.log_info("ACTUAL RESULT: " + exists)
        else:
            if exists != "true":
                ui_cmd_obj.error_state = False
            else:
                ui_cmd_obj.error_state = True

            self.logger.log_info("EXPECTED RESULT: false")
            self.logger.log_info("ACTUAL RESULT: " + exists)

        return ui_cmd_obj

    def verify_system_regime_is_non_editable(self, ui_cmd_obj, arg_dict):
        webelement = None
        row = 0
        # get all regimes instance
        regimes = self.builder.find_elements(ui_cmd_obj, "//div[@id='governanceLeftPanel-body']//div[@role='rowgroup']"
                                                         "//div//table")
        # iterate through regimes
        for regime in regimes:
            row += 1
            if arg_dict["regime_name"] == regime.text.strip():
                # Click on Edit Regime button
                webelement = self.builder.driver.find_element_by_css_selector(
                    "div#governanceLeftPanel-body>div>div>table:nth-child(" + str(
                        row) + ")>tbody>tr>td:nth-child(3)>div>a")
                break

        enabled = webelement.get_attribute("Class")
        # Verify edit button is disabled
        if "x-btn-disabled" in enabled:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        self.logger.log_info("EXPECTED RESULT: Disabled")
        self.logger.log_info("ACTUAL RESULT: " + enabled)

        return ui_cmd_obj

    def verify_system_regime_is_non_removable(self, ui_cmd_obj, arg_dict):
        webelement = None
        row = 0
        # get all regimes instance
        regimes = self.builder.find_elements(ui_cmd_obj, "//div[@id='governanceLeftPanel-body']//div[@role='rowgroup']"
                                                         "//div//table")
        # iterate through regimes
        for regime in regimes:
            row += 1
            if arg_dict["regime_name"] == regime.text.strip():
                # Click on Edit Regime button
                webelement = self.builder.driver.find_element_by_css_selector(
                    "div#governanceLeftPanel-body>div>div>table:nth-child(" + str(
                        row) + ")>tbody>tr>td:nth-child(4)>div>a")
                break

        enabled = webelement.get_attribute("Class")
        # Verify edit button is disabled
        if "x-btn-disabled" in enabled:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

        self.logger.log_info("EXPECTED RESULT: Disabled")
        self.logger.log_info("ACTUAL RESULT: " + enabled)

        return ui_cmd_obj

    def enter_regime_details(self, ui_cmd_obj, arg_dict):
        # Click on Add Regime button
        self._wait_for_dialog_window(ui_cmd_obj, "addEditRegimeDialog")
        # Enter name and description
        self._enter_regime_details(ui_cmd_obj, arg_dict["regime_name"], arg_dict["regime_desc"])

        return ui_cmd_obj

    def _select_regime(self, ui_cmd_obj, regime_name):
        flag = "false"
        # get all regimes instance
        regimes = self.builder.find_elements(ui_cmd_obj, "//div[@id='governanceLeftPanel-body']//div[@role='rowgroup']"
                                                         "//div//table")
        # iterate through regimes
        for regime in regimes:
            if regime_name == regime.text.strip():
                regime.click()
                flag = "true"
                self._wait_for_loading(ui_cmd_obj, 60)
                break

        return flag

    def _enter_regime_details(self, ui_cmd_obj, name, desc):
        # Enter name and description
        self.builder.driver.find_element_by_name("name").clear()
        self.builder.driver.find_element_by_name("name").send_keys(name)
        self.builder.driver.find_element_by_name("description").clear()
        self.builder.driver.find_element_by_name("description").send_keys(desc)
        #  Save it
        self._click_on_button(ui_cmd_obj, "Save")

        return ui_cmd_obj
