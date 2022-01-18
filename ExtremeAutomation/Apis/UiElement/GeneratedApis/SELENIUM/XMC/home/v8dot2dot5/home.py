# All imports above this line will be removed after generation.
# User imports must be added below.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ExtremeAutomation.Apis.UiElement.GeneratedApis.SELENIUM.XMC.webapp.baseappver.webapp \
    import Webapp as HomeBase


class Home(HomeBase):

    # Reusable common SBI (Sout Bound Interface) for XMC
    # These are specific to XMC but not specific to a particular feature
    # Can be consumed at Tests and low-level keywords
    def open_operation_panel(self, ui_cmd_obj, arg_dict):
        webelement = self.builder.find_element(ui_cmd_obj, "div[id^='basic-statusbar']>a.operationStatusBtn",
                                               self.builder.constants.STRATEGY_CSS_SELECTOR)
        if webelement.get_attribute("aria-pressed") == "true":
            self._wait_for_loading(ui_cmd_obj, 30)
        else:
            self.click_partial_link_text(ui_cmd_obj, "Operations")

        self._wait_for(ui_cmd_obj, 45)

        return ui_cmd_obj

    def close_operation_panel(self, ui_cmd_obj, arg_dict):
        webelement = self.builder.find_element(ui_cmd_obj, "div[id^='basic-statusbar']>a.operationStatusBtn",
                                               self.builder.constants.STRATEGY_CSS_SELECTOR)
        if webelement.get_attribute("aria-pressed") == "true":
            self.click_partial_link_text(ui_cmd_obj, "Operations")

        return ui_cmd_obj

    def wait_for_operation(self, ui_cmd_obj, arg_dict):
        flag = "false"
        prog_status = "Progress: 100%"

        wait = WebDriverWait(self.builder.driver, 60)
        # search for 10 minutes max
        for count in range(1, 60):
            # Get first line of operation panel
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id^='operationStatusGrid']>div>"
                                                                            "div>table")))
                operation = self.builder.find_element(ui_cmd_obj, "div[id^='operationStatusGrid']>div>div>"
                                                      "table:nth-child(1)",
                                                      self.builder.constants.STRATEGY_CSS_SELECTOR)
                operation_status = operation.text
                # self.browser.find_elements_by_css_selector("div[id^='operationStatusGrid']>div>div>table")
                self.logger.log_info(operation_status)
            except Exception:
                self._wait_for(ui_cmd_obj, 10)
                continue
            # Check if it's expected status
            if arg_dict["operation_name"] in operation_status:
                self.logger.log_info(operation_status)
                if prog_status in operation_status:
                    flag = "true"
                else:
                    self._wait_for(ui_cmd_obj, 10)
                    continue
            else:
                self._wait_for(ui_cmd_obj, 10)
                continue

            # Check if progress is 100 percentage
            if flag == "true":
                break

        return ui_cmd_obj

    def verify_operation_status(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("Verify expected result")
        operation_status = self._get_operation_status(ui_cmd_obj, arg_dict["operation_name"])
        # Verify device IP is found on the grid
        if arg_dict["status_message"] in operation_status:
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True

            self.logger.log_info("EXPECTED RESULT: " + arg_dict["status_message"])
            self.logger.log_info("ACTUAL RESULT: " + operation_status)

        return ui_cmd_obj

    def _get_operation_status(self, ui_cmd_obj, operation_name):
        message = None

        wait = WebDriverWait(self.builder.driver, 60)
        # get list of operations
        for count in range(1, 5):
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id^='operationStatusGrid']"
                                                          ">div>div>table")))
                operation = self.builder.find_element(ui_cmd_obj,
                                                      "div[id^='operationStatusGrid']>div>div>table:nth-child(1)",
                                                      self.builder.constants.STRATEGY_CSS_SELECTOR)
                operation_status = operation.text
                break
            except Exception:
                self._wait_for(ui_cmd_obj, 10)
                continue

        # Look for Governance Audit message at the top
        if operation_name == "Performing Governance Audit":
            if operation_name in operation_status:
                operation.click()
                self._move_mouse_out_of(ui_cmd_obj, "CSS", "div[id^='operationStatusGrid']")
                self._wait_for(ui_cmd_obj, 5)
                expanded_status = self.builder.driver.find_element_by_css_selector(
                    "div[id^='operationStatusGrid']>div>div>table:nth-child(1)")
                message = expanded_status.text
                # Collapse
                expanded_status.click()
            else:
                message = operation_status
        self.logger.log_info(message)

        return message
