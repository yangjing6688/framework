from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as WebappBase
# All imports above this line will be removed after generation.
# User imports must be added below.

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException

import time
import autoit
import pyautogui


class Webapp(WebappBase):
    # Reusable generic SBI (Sout Bound Interface) for web application
    # These are feature and application agnostic ones
    # Can be consumed at Tests and low-level keywords
    def open_page(self, ui_cmd_obj, arg_dict):
        self.builder.open_web_page(ui_cmd_obj, arg_dict["browser"], arg_dict["url"])

        return ui_cmd_obj

    def close_page(self, ui_cmd_obj, arg_dict):
        self.builder.close_web_page(ui_cmd_obj)

        return ui_cmd_obj

    def launch_xmc(self, ui_cmd_obj, arg_dict):
        # self.builder.open_web_page(ui_cmd_obj, arg_dict["browser"], arg_dict["url"])
        self._open_page(ui_cmd_obj, arg_dict["browser"], arg_dict["url"])

        return ui_cmd_obj

    def login_to_xmc(self, ui_cmd_obj, arg_dict):
        # Enter Username and Password
        self.builder.enter_text(ui_cmd_obj, arg_dict["username"], "j_username", self.builder.constants.STRATEGY_NAME)
        self.builder.enter_text(ui_cmd_obj, arg_dict["password"], "j_password", self.builder.constants.STRATEGY_NAME)
        # Click on Submit button
        self.builder.click(ui_cmd_obj, "button[type='submit']", self.builder.constants.STRATEGY_CSS_SELECTOR)

        return ui_cmd_obj

    def switch_tab(self, ui_cmd_obj, arg_dict):
        # Define a link element
        if arg_dict["partial"] is None:
            webelement = self.builder.driver.find_element_by_link_text(arg_dict["link_text"])
        else:
            webelement = self.builder.driver.find_element_by_partial_link_text(arg_dict["link_text"])

        # click on the link
        webelement.click()

        return ui_cmd_obj

    def select_page(self, ui_cmd_obj, arg_dict):
        # Define a link element
        if arg_dict["partial"] is None:
            webelement = self.builder.driver.find_element_by_link_text(arg_dict["link_text"])
        else:
            webelement = self.builder.driver.find_element_by_partial_link_text(arg_dict["link_text"])

        # click on the link
        webelement.click()

        return ui_cmd_obj

    def click_on_button(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_link_text(arg_dict["link_text"]).click()

        return ui_cmd_obj

    def click_link_text(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_link_text(arg_dict["link_text"]).click()

        return ui_cmd_obj

    def click_nth_link_text(self, ui_cmd_obj, arg_dict):
        if arg_dict["partial"] is None:
            webelements = self.builder.driver.find_elements_by_link_text(arg_dict["link_text"])
        else:
            webelements = self.builder.driver.find_elements_by_partial_link_text(arg_dict["link_text"])

        # click on the link
        webelements[int(arg_dict["x_link_text"]) - 1].click()

        return ui_cmd_obj

    def element_exists(self, ui_cmd_obj, arg_dict):
        wait = WebDriverWait(self.builder.driver, arg_dict["timeout"])
        if arg_dict["by"].lower() == "link_text":
            try:
                wait.until(EC.element_to_be_clickable((By.LINK_TEXT, arg_dict["locator"])))
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as ex:
                self.logger.log_info(ex)
        elif arg_dict["by"].lower() == "partial_link_text":
            try:
                wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, arg_dict["locator"])))
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as ex:
                self.logger.log_info(ex)
        elif arg_dict["by"].lower() == "css":
            try:
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, arg_dict["locator"])))
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as ex:
                self.logger.log_info(ex)
        elif arg_dict["by"].lower() == "id":
            try:
                wait.until(EC.element_to_be_clickable((By.ID, arg_dict["locator"])))
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as ex:
                self.logger.log_info(ex)
        elif arg_dict["by"].lower() == "name":
            try:
                wait.until(EC.element_to_be_clickable((By.NAME, arg_dict["locator"])))
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as ex:
                self.logger.log_info(ex)
        elif arg_dict["by"].lower() == "class":
            try:
                wait.until(EC.element_to_be_clickable((By.CLASS_NAME, arg_dict["locator"])))
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as ex:
                self.logger.log_info(ex)
        elif arg_dict["by"].lower() == "xpath":
            try:
                wait.until(EC.element_to_be_clickable((By.XPATH, arg_dict["locator"])))
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as ex:
                self.logger.log_info(ex)
        else:
            raise ValueError("Invalid locator type")

        return ui_cmd_obj

    def wait_for(self, ui_cmd_obj, arg_dict):
        # self.builder.delay(ui_cmd_obj, arg_dict["seconds"])
        self._wait_for(ui_cmd_obj, float(arg_dict["seconds"]))

        return ui_cmd_obj

    def wait_for_page_to_load(self, ui_cmd_obj, arg_dict):
        wait = WebDriverWait(self.builder.driver, arg_dict["timeout"])
        wait.until(EC.title_contains(arg_dict["title"]))
        # Wait for document status to Complete
        for timeout in range(0, 15):
            self.builder.delay(ui_cmd_obj, 2)
            doc_status = self.builder.driver.execute_script('return document.readyState;')
            if doc_status.lower() == 'complete':
                break

        return ui_cmd_obj

    def wait_for_loading(self, ui_cmd_obj, arg_dict):
        # time.sleep(5)
        self._wait_for(ui_cmd_obj, 2)
        # Wait for element to disappear
        for sec in range(0, int(arg_dict["timeout"])):
            try:
                self.builder.driver.find_element_by_css_selector(
                    ".x-border-box.x-mask[role='progressbar'][aria-hidden='false']").click()
            except Exception as ex:
                self.logger.log_info(ex)
                self._wait_for(ui_cmd_obj, 2)
                break
            finally:
                self._wait_for(ui_cmd_obj, 2)

        return ui_cmd_obj

    def wait_for_message_box(self, ui_cmd_obj, arg_dict):
        wait = WebDriverWait(self.builder.driver, arg_dict["timeout"])
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.x-message-box')))
        self._wait_for(ui_cmd_obj, 1)

        return ui_cmd_obj

    def wait_for_dialog_window(self, ui_cmd_obj, arg_dict):
        wait = WebDriverWait(self.builder.driver, arg_dict["timeout"])
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id^='" + arg_dict["windowid"] + "']")))
        self._wait_for(ui_cmd_obj, 1)

        return ui_cmd_obj

    def accept_dialog_box(self, ui_cmd_obj, arg_dict):
        self._click_link_text(ui_cmd_obj, arg_dict["accept_button"])

        return ui_cmd_obj

    def reject_dialog_box(self, ui_cmd_obj, arg_dict):
        self._click_link_text(ui_cmd_obj, arg_dict["reject_button"])

        return ui_cmd_obj

    def invoke_popup_menu(self, ui_cmd_obj, arg_dict):
        # webelement = self.builder.driver.find_element_by_link_text(arg_dict["locator"])

        actions = ActionChains(self.builder.driver)
        actions.context_click(arg_dict["webelement"])
        actions.perform()

        return ui_cmd_obj

    def select_tree_node_item(self, ui_cmd_obj, arg_dict):
        # Split tree nodes
        items = arg_dict["treenodes"].split("|")
        # Expand each tree node items
        for index in range(0, len(items) - 1):
            # Get all tree view items
            tvnodes = self.builder.driver.find_elements_by_css_selector(arg_dict["css_locator"])
            # Work around for handling duplicate nodes
            tvnodes.reverse()
            # Expand parent nodes
            for node in tvnodes:
                if items[index] == node.text:
                    self.logger.log_info(node.text)
                    # node.click()
                    self._double_click(ui_cmd_obj, node)
                    self._wait_for_loading(ui_cmd_obj)
                    self._move_mouse_out_of(ui_cmd_obj, "CSS", arg_dict["css_locator"])
                    break
        # Get tree view items
        tvnodes = self.builder.driver.find_elements_by_css_selector(arg_dict["css_locator"])
        # Work around for handling duplicate leaf nodes
        if arg_dict["search_order"].lower() == "bottom-up":
            count = len(tvnodes) + 1
            tvnodes.reverse()
            # Select the leaf node
            for node in tvnodes:
                count -= 1
                if items[len(items) - 1] == node.text:
                    leafnode = self.builder.driver.find_element_by_css_selector(
                        arg_dict["css_locator"] + ":nth-child(" + str(count) + ")")
                    leafnode.click()
                    self._wait_for_loading(ui_cmd_obj)
                    self._move_mouse_out_of(ui_cmd_obj, "CSS", arg_dict["css_locator"])
                    break
        else:
            index = 0
            # Select the leaf node
            for node in tvnodes:
                index += 1
                if items[len(items) - 1] == node.text:
                    leafnode = self.builder.driver.find_element_by_css_selector(
                        arg_dict["css_locator"] + ":nth-child(" + str(index) + ")")
                    leafnode.click()
                    self._wait_for_loading(ui_cmd_obj)
                    self._move_mouse_out_of(ui_cmd_obj, "CSS", arg_dict["css_locator"])
                    break

        return ui_cmd_obj

    def double_click(self, ui_cmd_obj, arg_dict):
        actions = ActionChains(self.builder.driver)
        actions.double_click(arg_dict["webelement"])
        actions.perform()

        return ui_cmd_obj

    def invoke_dropdown(self, ui_cmd_obj, arg_dict):
        if arg_dict["by"].lower() == "link_text":
            element = self.builder.driver.find_element_by_link_text(arg_dict["locator"])
        elif arg_dict["by"].lower() == "partial_link_text":
            element = self.builder.driver.find_element_by_partial_link_text(arg_dict["locator"])
        elif arg_dict["by"].lower() == "css":
            element = self.builder.driver.find_element_by_css_selector(arg_dict["locator"])
        elif arg_dict["by"].lower() == "id":
            element = self.builder.driver.find_element_by_id(arg_dict["locator"])
        elif arg_dict["by"].lower() == "name":
            element = self.builder.driver.find_element_by_tag_name(arg_dict["locator"])
        elif arg_dict["by"].lower() == "class":
            element = self.builder.driver.find_element_by_class(arg_dict["locator"])
        else:
            raise AssertionError("ERROR: invalid %s locator type" % (arg_dict["locator"]))

        element.click()

        return ui_cmd_obj

    def select_boundlist_item(self, ui_cmd_obj, arg_dict):
        items = self.builder.driver.find_elements_by_css_selector(".x-boundlist-item")
        for item in items:
            if arg_dict["itemname"] in item.text:
                item.click()
                break

        return ui_cmd_obj

    def select_boundlist_item_by_index(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_css_selector(
            ".x-boundlist-item:nth-child(" + str(arg_dict["index"]) + ")").click()

        return ui_cmd_obj

    def select_x_collapsed_panel(self, ui_cmd_obj, arg_dict):
        xpanels = self.builder.driver.find_elements_by_css_selector(arg_dict["css_locator"])
        for xpanel in xpanels:
            if xpanel.text == arg_dict["panel_title"]:
                xpanel.click()
                self._wait_for(ui_cmd_obj, 1)
                break

        return ui_cmd_obj

    def move_mouse_out_of(self, ui_cmd_obj, arg_dict):
        if arg_dict["by"].lower() == "link_text":
            element = self.builder.driver.find_element_by_link_text(arg_dict["locator"])
        elif arg_dict["by"].lower() == "partial_link_text":
            element = self.builder.driver.find_element_by_partial_link_text(arg_dict["locator"])
        elif arg_dict["by"].lower() == "css":
            element = self.builder.driver.find_element_by_css_selector(arg_dict["locator"])
        elif arg_dict["by"].lower() == "id":
            element = self.builder.driver.find_element_by_id(arg_dict["locator"])
        elif arg_dict["by"].lower() == "name":
            element = self.builder.driver.find_element_by_tag_name(arg_dict["locator"])
        elif arg_dict["by"].lower() == "class":
            element = self.builder.driver.find_element_by_class(arg_dict["locator"])
        else:
            raise AssertionError("ERROR: invalid %s locator type" % (arg_dict["locator"]))

        size = element.size
        offsetx = (size['width'] / 2) + 1
        offsety = (size['height'] / 2) + 1

        actions = ActionChains(self.builder.driver)
        actions.move_to_element(element).move_by_offset(offsetx, offsety)
        actions.perform()
        self._wait_for(ui_cmd_obj, 1)

        return ui_cmd_obj

    def move_mouse_over_img(self, ui_cmd_obj, arg_dict):
        if arg_dict["by"].lower() == "link_text":
            element = self.builder.driver.find_element_by_link_text(arg_dict["locator"])
        elif arg_dict["by"].lower() == "partial_link_text":
            element = self.builder.driver.find_element_by_partial_link_text(arg_dict["locator"])
        elif arg_dict["by"].lower() == "css":
            element = self.builder.driver.find_element_by_css_selector(arg_dict["locator"])
        elif arg_dict["by"].lower() == "id":
            element = self.builder.driver.find_element_by_id(arg_dict["locator"])
        elif arg_dict["by"].lower() == "name":
            element = self.builder.driver.find_element_by_tag_name(arg_dict["locator"])
        elif arg_dict["by"].lower() == "class":
            element = self.builder.driver.find_element_by_class(arg_dict["locator"])
        else:
            raise AssertionError("ERROR: invalid %s locator type" % (arg_dict["locator"]))

        location = element.location
        size = element.size
        offsetx = location['x'] + size['height'] / 2
        offsety = location['y'] + 125

        actions = ActionChains(self.builder.driver)
        actions.move_to_element(element)
        actions.perform()

        pyautogui.FAILSAFE = False
        pyautogui.moveTo(offsetx, offsety)
        self._wait_for(ui_cmd_obj, 2)

        return ui_cmd_obj

    def move_mouse_over_element(self, ui_cmd_obj, arg_dict):
        location = arg_dict["webelement"].location
        size = arg_dict["webelement"].size
        offsetx = location['x'] + size['height'] / 2
        offsety = location['y'] + 125

        actions = ActionChains(self.builder.driver)
        actions.move_to_element(arg_dict["webelement"])
        actions.perform()

        pyautogui.FAILSAFE = False
        pyautogui.moveTo(offsetx, offsety)
        self._wait_for(ui_cmd_obj, 1)

        return ui_cmd_obj

    def close_tab(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_css_selector("span.x-tab-close-btn").click()

        return ui_cmd_obj

    def close_dialog_box(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_element_by_css_selector("div.x-tool-img.x-tool-close").click()

        return ui_cmd_obj

    def drag_and_drop_element(self, ui_cmd_obj, arg_dict):
        actions = ActionChains(self.builder.driver)
        actions.drag_and_drop_by_offset(arg_dict["webelement"], int(arg_dict["x"]), int(arg_dict["y"]))
        actions.perform()

        return ui_cmd_obj

    def click_stale_element(self, ui_cmd_obj, arg_dict):
        wait = WebDriverWait(self.builder.driver, arg_dict["timeout"])
        if arg_dict["by"].lower() == "link_text":
            webelement = wait.until(EC.presence_of_element_located((By.LINK_TEXT, arg_dict["locator"])))
        elif arg_dict["by"].lower() == "partial_link_text":
            webelement = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, arg_dict["locator"])))
        elif arg_dict["by"].lower() == "css":
            webelement = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, arg_dict["locator"])))
        elif arg_dict["by"].lower() == "id":
            webelement = wait.until(EC.presence_of_element_located((By.ID, arg_dict["locator"])))
        elif arg_dict["by"].lower() == "name":
            webelement = wait.until(EC.presence_of_element_located((By.NAME, arg_dict["locator"])))
        elif arg_dict["by"].lower() == "class":
            webelement = wait.until(EC.presence_of_element_located((By.CLASS_NAME, arg_dict["locator"])))
        else:
            raise ValueError("Invalid locator type")

        actions = ActionChains(self.builder.driver)
        actions.move_to_element_with_offset(webelement, 25, 5).click()
        actions.perform()

        return ui_cmd_obj

    def find_a_row_from_grid(self, ui_cmd_obj, arg_dict):
        rows = self.builder.driver.find_elements_by_css_selector(arg_dict["grid_table_css_locator"])
        for row in rows:
            if arg_dict["row_content"] in row.text:
                self.logger.log_info(row.text)
                row.click()
                break

        return ui_cmd_obj

    def get_a_row_from_grid(self, ui_cmd_obj, arg_dict):
        rows = self.builder.driver.find_elements_by_css_selector(arg_dict["grid_table_css_locator"])
        row_content = rows[int(arg_dict["row_no"]) - 1].text
        self.logger.log_info(row_content)

        return ui_cmd_obj

    def select_a_row_on_the_grid(self, ui_cmd_obj, arg_dict):
        rows = self.builder.driver.find_elements_by_css_selector(arg_dict["grid_table_css_locator"])
        rows[int(arg_dict["row_no"]) - 1].click()

        return ui_cmd_obj

    def get_a_column_from_grid(self, ui_cmd_obj, arg_dict):
        column_content = []
        rows = self.builder.driver.find_elements_by_css_selector(arg_dict["grid_table_css_locator"])
        for row in rows:
            row_content = row.text
            cell_value = self._get_field(row_content, '\n', arg_dict["col_no"])
            column_content.append(cell_value)
        self.logger.log_info(column_content)

        return ui_cmd_obj

    def get_a_cell_value_from_grid(self, ui_cmd_obj, arg_dict):
        rows = self.builder.driver.find_elements_by_css_selector(arg_dict["grid_table_css_locator"])
        row_content = rows[int(arg_dict["row_no"]) - 1].text
        cell_value = self._get_field(row_content, '\n', arg_dict["col_no"])
        self.logger.log_info(cell_value)

        return ui_cmd_obj

    def get_row_count_from_grid(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj.return_text = self.builder.driver.find_elements_by_css_selector(arg_dict["grid_table_css_locator"])
        # count = len(rows)

        return ui_cmd_obj

    def click_on_a_cell_on_the_grid(self, ui_cmd_obj, arg_dict):
        self.builder.driver.find_elements_by_css_selector(
            arg_dict["grid_table_css_locator"] + ">tbody>tr:nth-child(" + arg_dict["row_no"] + ")>td:nth-child(" +
            arg_dict["col_no"] + ")").click()

        return ui_cmd_obj

    def filter_grid_column_values(self, ui_cmd_obj, arg_dict):
        column_header = self.builder.driver.find_element_by_css_selector(
            "[data-qtip='" + arg_dict["column_tooltip"] + "']")
        column_header.click()
        self.builder.driver.find_element_by_css_selector("div.x-column-header-trigger").click()
        self._click_linktext(ui_cmd_obj, "Filters")
        self.builder.driver.find_element_by_css_selector("input[placeholder='Enter Filter Text...']").send_keys(
            arg_dict["filter_text"])
        column_header.click()

        return ui_cmd_obj

    def get_list_item(self, ui_cmd_obj, arg_dict):
        ui_cmd_obj.return_text = self.builder.driver.find_element_by_css_selector(
            arg_dict["css_locator"] + ":nth-child(" + str(arg_dict["index"]) + ")").text

        return ui_cmd_obj

    def browser_full_screen(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("Full screen of browser (headless one)")
        pyautogui.FAILSAFE = False
        pyautogui.press('f11')

        return ui_cmd_obj

    def browser_zoom_out(self, ui_cmd_obj, arg_dict):
        self.logger.log_info("Full screen of browser (headless one)")
        for x in range(10, int(arg_dict["percentage"])):
            self.builder.driver.send_keys(Keys.CONTROL, Keys.ADD)

        return ui_cmd_obj

    # Protected methods
    def _open_page(self, ui_cmd_obj, browser, url):
        self.builder.open_web_page(ui_cmd_obj, browser, url)

        return ui_cmd_obj

    def _select_tree_node_item(self, ui_cmd_obj, treenodes, css_locator, search_order="bottom-up"):
        leafnode = None

        # Split tree nodes
        items = treenodes.split("|")
        # Expand each tree node items
        for index in range(0, len(items) - 1):
            # Get all tree view items
            tvnodes = self.builder.driver.find_elements_by_css_selector(css_locator)
            # Work around for handling duplicate nodes
            tvnodes.reverse()
            # Expand parent nodes
            for node in tvnodes:
                if items[index] == node.text:
                    self.logger.log_info(node.text)
                    # node.click()
                    self._double_click(ui_cmd_obj, node)
                    self._wait_for_loading(ui_cmd_obj)
                    self._move_mouse_out_of(ui_cmd_obj, "CSS", css_locator)
                    break
        # Get tree view items
        tvnodes = self.builder.driver.find_elements_by_css_selector(css_locator)
        # Work around for handling duplicate leaf nodes
        if search_order.lower() == "bottom-up":
            count = len(tvnodes) + 1
            tvnodes.reverse()
            # Select the leaf node
            for node in tvnodes:
                count -= 1
                if items[len(items) - 1] == node.text:
                    leafnode = self.builder.driver.find_element_by_css_selector(
                        css_locator + ":nth-child(" + str(count) + ")")
                    leafnode.click()
                    self._wait_for_loading(ui_cmd_obj)
                    self._move_mouse_out_of(ui_cmd_obj, "CSS", css_locator)
                    break
        else:
            index = 0
            # Select the leaf node
            for node in tvnodes:
                index += 1
                if items[len(items) - 1] == node.text:
                    leafnode = self.builder.driver.find_element_by_css_selector(
                        css_locator + ":nth-child(" + str(index) + ")")
                    leafnode.click()
                    self._wait_for_loading(ui_cmd_obj)
                    self._move_mouse_out_of(ui_cmd_obj, "CSS", css_locator)
                    break

        return leafnode

    def _element_exists(self, ui_cmd_obj, by, locator, timeout=10):
        flag = 1
        wait = WebDriverWait(self.builder.driver, timeout)
        if by.lower() == "link_text":
            try:
                wait.until(EC.element_to_be_clickable((By.LINK_TEXT, locator)))
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as ex:
                self.logger.log_info(ex)
                flag = 0
        elif by.lower() == "partial_link_text":
            try:
                wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, locator)))
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as ex:
                self.logger.log_info(ex)
                flag = 0
        elif by.lower() == "css":
            try:
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as ex:
                self.logger.log_info(ex)
                flag = 0
        elif by.lower() == "id":
            try:
                wait.until(EC.element_to_be_clickable((By.ID, locator)))
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as ex:
                self.logger.log_info(ex)
                flag = 0
        elif by.lower() == "name":
            try:
                wait.until(EC.element_to_be_clickable((By.NAME, locator)))
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as ex:
                self.logger.log_info(ex)
                flag = 0
        elif by.lower() == "class":
            try:
                wait.until(EC.element_to_be_clickable((By.CLASS_NAME, locator)))
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as ex:
                self.logger.log_info(ex)
                flag = 0
        elif by.lower() == "xpath":
            try:
                wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
            except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as ex:
                self.logger.log_info(ex)
                flag = 0
        else:
            raise ValueError("Invalid locator type")

        return flag

    def _wait_for(self, ui_cmd_obj, seconds):
        self.logger.log_info("INFO: Waiting for:  " + str(seconds))
        time.sleep(float(seconds))

    def _wait_for_loading(self, ui_cmd_obj, timeout=10):
        self._wait_for(ui_cmd_obj, 2)
        # Wait for element to disappear
        for sec in range(0, timeout):
            try:
                self.builder.driver.find_element_by_css_selector(
                    ".x-border-box.x-mask[role='progressbar'][aria-hidden='false']").click()
            except Exception as ex:
                self.logger.log_info(ex)
                self._wait_for(ui_cmd_obj, 2)
                break
            finally:
                self._wait_for(ui_cmd_obj, 2)

    def _wait_for_dialog_window(self, ui_cmd_obj, windowid, timeout=10):
        wait = WebDriverWait(self.builder.driver, timeout)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id^='" + windowid + "']")))
        self._wait_for(ui_cmd_obj, 1)

    def _double_click(self, ui_cmd_obj, webelement):
        actions = ActionChains(self.builder.driver)
        actions.double_click(webelement)
        actions.perform()

        return ui_cmd_obj

    def _move_mouse_out_of(self, ui_cmd_obj, by, locator):
        if by.lower() == "link_text":
            element = self.builder.driver.find_element_by_link_text(locator)
        elif by.lower() == "partial_link_text":
            element = self.builder.driver.find_element_by_partial_link_text(locator)
        elif by.lower() == "css":
            element = self.builder.driver.find_element_by_css_selector(locator)
        elif by.lower() == "id":
            element = self.builder.driver.find_element_by_id(locator)
        elif by.lower() == "name":
            element = self.builder.driver.find_element_by_tag_name(locator)
        elif by.lower() == "class":
            element = self.builder.driver.find_element_by_class(locator)
        else:
            raise AssertionError("ERROR: invalid %s locator type" % locator)

        size = element.size
        offsetx = (size['width'] / 2) + 1
        offsety = (size['height'] / 2) + 1

        actions = ActionChains(self.builder.driver)
        actions.move_to_element(element).move_by_offset(offsetx, offsety)
        actions.perform()
        self._wait_for(ui_cmd_obj, 1)

    def _move_mouse_over_img(self, ui_cmd_obj, by, locator):
        if by.lower() == "link_text":
            element = self.builder.driver.find_element_by_link_text(locator)
        elif by.lower() == "partial_link_text":
            element = self.builder.driver.find_element_by_partial_link_text(locator)
        elif by.lower() == "css":
            element = self.builder.driver.find_element_by_css_selector(locator)
        elif by.lower() == "id":
            element = self.builder.driver.find_element_by_id(locator)
        elif by.lower() == "name":
            element = self.builder.driver.find_element_by_tag_name(locator)
        elif by.lower() == "class":
            element = self.builder.driver.find_element_by_class(locator)
        else:
            raise AssertionError("ERROR: invalid %s locator type" % (locator))

        location = element.location
        size = element.size
        offsetx = location['x'] + size['height'] / 2
        offsety = location['y'] + 90

        actions = ActionChains(self.builder.driver)
        actions.move_to_element(element)
        actions.perform()

        pyautogui.FAILSAFE = False
        pyautogui.moveTo(offsetx, offsety)
        self._wait_for(ui_cmd_obj, 2)

        return ui_cmd_obj

    def _move_mouse_over_element(self, ui_cmd_obj, webelement):
        location = webelement.location
        size = webelement.size
        offsetx = location['x'] + size['height'] / 2
        offsety = location['y'] + 90

        actions = ActionChains(self.builder.driver)
        actions.move_to_element(webelement)
        actions.perform()

        pyautogui.FAILSAFE = False
        pyautogui.moveTo(offsetx, offsety)
        self._wait_for(ui_cmd_obj, 1)

        return ui_cmd_obj

    def _invoke_popup_menu(self, ui_cmd_obj, css_locator):
        webelement = self.builder.find_element(ui_cmd_obj,
                                               css_locator,
                                               self.builder.constants.STRATEGY_CSS_SELECTOR)
        actions = ActionChains(self.builder.driver)
        actions.context_click(webelement)
        actions.perform()

        return ui_cmd_obj

    def _invoke_popup_menu_for_webelement(self, ui_cmd_obj, webelement):
        actions = ActionChains(self.builder.driver)
        actions.context_click(webelement)
        actions.perform()

        return ui_cmd_obj

    def _click_on_button(self, ui_cmd_obj, button_name):
        self.builder.driver.find_element_by_link_text(button_name).click()

        return ui_cmd_obj

    def _click_link_text(self, ui_cmd_obj, link_text):
        self.builder.driver.find_element_by_link_text(link_text).click()

        return ui_cmd_obj

    def _click_partial_link_text(self, ui_cmd_obj, link_text):
        self.builder.driver.find_element_by_partial_link_text(link_text).click()

        return ui_cmd_obj

    def _find_a_row_from_grid(self, ui_cmd_obj, row_content, grid_css_locator):
        flag = 0
        # rows = self.builder.find_elements(ui_cmd_obj, grid_css_locator, self.builder.constants.STRATEGY_CSS_SELECTOR)
        rows = self.builder.driver.find_elements_by_css_selector(grid_css_locator)
        for row in rows:
            if row_content in row.text:
                self.logger.log_info(row.text)
                flag = 1
                row.click()
                break

        return flag

    def _drag_and_drop_element(self, ui_cmd_obj, webelement, x, y):
        actions = ActionChains(self.builder.driver)
        actions.drag_and_drop_by_offset(webelement, int(x), int(y))
        actions.perform()

        return ui_cmd_obj

    def _find_elements_by_css(self, ui_cmd_obj, css_locator):
        # rows = self.builder.find_elements(ui_cmd_obj, grid_css_locator, self.builder.constants.STRATEGY_CSS_SELECTOR)
        try:
            webelements = self.builder.driver.find_elements_by_css_selector(css_locator)
        except Exception:
            self.logger.log_info("INFO: Execute Javascript statement")
            webelements = self.builder.driver.execute_script(
                "return document.querySelectorAll(" + """+css_locator+""" + ")")

        return webelements

    def _open_file(self, ui_cmd_obj, filename):
        autoit.auto_it_set_option("WinTitleMatchMode", 2)
        autoit.win_wait("Open", 10)
        self._wait_for(ui_cmd_obj, 2)
        # Send file
        autoit.control_send("Open", "[CLASS:Edit]", filename + "{Enter}")
        self._wait_for(ui_cmd_obj, 2)

        return ui_cmd_obj

    def _get_a_column_from_grid(self, ui_cmd_obj, grid_css_locator, column_no):
        column_content = []
        rows = self.builder.driver.find_elements_by_css_selector(grid_css_locator)
        for row in rows:
            row_content = row.text
            cell_value = self._get_field(row_content, '\n', column_no)
            column_content.append(cell_value)
        self.logger.log_info(column_content)

        return column_content

    def _get_field(self, item, delimeter, xfield):
        self.logger.log_info("INFO: Geting a x field from a list of fields")
        field = item.split(delimeter)
        return field[int(xfield) - 1]
