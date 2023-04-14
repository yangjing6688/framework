from time import sleep
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.CloudDriver import CloudDriver
from extauto.common.WebElementController import WebElementController
from extauto.common.CommonValidation import CommonValidation

class AutoActions:
    def __init__(self):
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.retries = 5
        self.utils = Utils()
        self.screen = Screen()
        self.builtin = BuiltIn()
        self.common_validation = CommonValidation()
        self.web_element_ctrl = WebElementController()

    def click_reference(self, element_object_ref):
        return self.web_element_ctrl.action_method(self.click, element_object_ref)

    def click(self, element):
        """
        - This Keyword Uses to Click the Mentioned Web Element
        - If the Element is not visible into view it Scroll element into view and Scroll down into page to click Element
        :param element: Web Element to Click on Web Page
        :return: None
        """

        if element is None:
            self.screen.save_screen_shot()
            self.builtin.fail(msg="Unable to Click the Element. The element is passed in is 'None'. No WebElement Handler Present for the Element.")
            return -1

        else:
            # this line should be uncommented only when debugging
            # self.utils.print_debug("Clicking Element: ", element)
            attempt_count = 0
            wait_time = 5
            while attempt_count < self.retries:
                try:
                    if type(element) is tuple:
                        self.click_image(element)
                    elif type(element) is list:
                        self.utils.print_info("Element is list...")
                        for ele in element:
                            ele.click()
                    else:
                        element.click()

                    # Click was successful.  If we previously failed print a message to confirm success
                    if attempt_count:
                        self.utils.print_info("Element click successful after previous failed attempt")
                    return 1
                except ElementClickInterceptedException:
                    # The ElementClickIntercepted exception happens when selenium cannot click on the element.  An
                    # example would be if an element is not in view due to the element being off the screen.  Another
                    # example is when the element is covered up by another element preventing the user from seeing the
                    # element and therefore preventing the user from clicking the element.
                    #
                    # In this case we'll use DOM to click the element via a Javascript method.
                    java_script = """
                                  function do_click(element_to_click)
                                  {
                                    try {
                                       element_to_click.click();
                                       return true;
                                    }
                                    catch(err) {
                                      return false;
                                    }
                                  }
                                  return do_click(arguments[0])
                                  """
                    self.utils.print_info("'Element Click Intercepted Exception': trying javascript click().")
                    click_successful = CloudDriver().cloud_driver.execute_script(java_script, element)
                    if click_successful:
                        self.utils.print_info("Javascript click was successful")
                        return 1
                    self.utils.print_info("Error: Javascript click was not successful. Retrying after {} seconds...".format(wait_time))

                except StaleElementReferenceException:
                    self.utils.print_info("Error: StaleElementReferenceException. Retrying after {} seconds...".format(wait_time))
                    # If you are experiencing StaleElementReference exceptions it's an indication that the element
                    # changed after you obtained it.  If you called click_reference() instead of click() the code will
                    # attempt to get a fresh copy of the element that changed.  If not using click_reference() changing
                    # from click() to click_reference() should resolve this issue.
                    #
                    # Return immediately so we aren't trying to click 5 times before attempting to get a fresh copy
                    # of the element
                    return -1

                except ElementNotInteractableException:
                    self.utils.print_debug("Error: ElementNotInteractableException. Retrying after {} seconds...".format(wait_time))

                except Exception as e:
                    self.utils.print_info("An exception occurred while attempting a click. Retrying after {} seconds Error: {}".format(wait_time, e))

                attempt_count = attempt_count + 1
                sleep(wait_time)
                if attempt_count >= self.retries:
                    kwargs = {}
                    kwargs['fail_msg'] = "FAIL - Unable to click the element"
                    self.common_validation.fault(**kwargs)

        return -1

    def click_with_js(self, element):
        CloudDriver().cloud_driver.execute_script("arguments[0].click(); ", element)
        sleep(2)

    def move_to_element(self, element):
        """
        - This Keyword Uses to Move the Mentioned Web Element using Mouse Actions

        :param element: Web Element to Move the Mouse Cursor on Web Page
        :return: None
        """
        action = ActionChains(CloudDriver().cloud_driver)
        sleep(2)

        # Reset the cursor before moving to the element.  This is necessary in cases where the cursor is already
        # hovering over the element.  In some cases (like menus) moving to the same location will not have the desired
        # affect (like redrawing the menu)
        action.reset_actions()

        # Now move to the element
        action.move_to_element(element)
        action.perform()
        sleep(2)

    def send_keys(self, element, value, allow_fail=False):
        """
        - This Keyword Uses to Send Clear the Text Area and Input the Mentioned Value on Text Field Web Element.

        :param element: Web Element To enter Text Field
        :param value: Element Text Field Value
        :param allow_fail: default False. True= Instead of force FAIL on error, return -1
        :return: None
        """
        self.utils.print_info("Sending Value to Element: ", value)
        if element is None:
            self.screen.save_screen_shot()
            if not allow_fail:
                self.builtin.fail(msg="Unable to Send value to the Element..No WebElement Handler Present for the Element."
                                  "So Exiting the Testcase")
            else:
                return -1
        else:
            count = 0
            while count < self.retries:
                try:
                    element.clear()
                    element.send_keys(value)
                    return 1
                except Exception as e:
                    self.utils.print_warning("Exception while sending text: ", e)
                    self.utils.print_info("Retrying after 2 seconds...")
                    sleep(2)

                    count += 1
                    if count == self.retries:
                        self.utils.print_warning("Unable to enter text to element. Saving Screenshot...")
                        self.screen.save_screen_shot()

    def send_enter(self, element):
        """
        - This Keyword Uses to press enter Key on Web Page from mentioned Web Element

        :param element: Web Element To enter Send Key
        :return: None
        """
        self.utils.print_info("Sending ENTER Key")
        element.send_keys(Keys.ENTER)

    def send_page_down(self, element):
        """
        - This Keyword Uses to press Page down Key on Web Page from mentioned Web Element

        :param element: Web Element To enter Page Down Key
        :return: None
        """
        self.utils.print_info("Sending ENTER Key")
        element.send_keys(Keys.PAGE_DOWN)

    def scroll_by(self):
        """
        - This Keyword Uses to Scroll the page by 250 pixels y-coordinate

        :return: None
        """
        CloudDriver().cloud_driver.execute_script("javascript:window.scrollBy(0,250)")

    def scroll_by_horizontal(self, element):
        """
        - This Keyword Uses to Scroll the page ro end in x-coordinate

        :return: None
        """
        self.utils.print_info("Scrolling horizontal bar to end")
        coordinates = element.location_once_scrolled_into_view  # returns dict of X, Y coordinates
        CloudDriver().cloud_driver.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))

    def scroll_down(self):
        """
        - This Keyword Uses to Scroll Down the page.

        :return: None
        """
        CloudDriver().cloud_driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

    def scroll_down_table(self, element_def):
        """
        This method is used to scroll down a table until all elements are visible
        :param element_def: the definition of the last element of a table. It must be an CSS_SELECTOR
        :return: None
        """

        last_elem = ''
        driver = CloudDriver().cloud_driver
        while True:
            try:
                WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                                                               element_def['CSS_SELECTOR'])))
            except Exception as e:
                self.utils.print_warning("Exception while scrolling table: ", e)

            current_last_elem = driver.find_element(By.CSS_SELECTOR, element_def['CSS_SELECTOR'])
            driver.execute_script("document.querySelector(\'" + element_def['CSS_SELECTOR'] + "\').scrollIntoView();")
            sleep(3)
            if last_elem == current_last_elem:
                break
            else:
                last_elem = current_last_elem

    def scroll_up(self):
        """
        - This Keyword Uses to Scroll Up the page.

        :return: None
        """
        CloudDriver().cloud_driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)

    def click_image(self, position):
        actions = ActionChains(CloudDriver().cloud_driver)
        (x, y) = position
        actions.move_to_element_with_offset(CloudDriver().cloud_driver.find_element_by_tag_name('body'), 0, 0)
        sleep(5)
        actions.move_by_offset(x, y).click().perform()
        return

    def center_element(self, element):
        """
        :param element:
        :return:
        """
        desired_y = (element.size['height'] / 2) + element.location['y']
        window_h = CloudDriver().cloud_driver.execute_script('return window.innerHeight')
        window_y = CloudDriver().cloud_driver.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y
        CloudDriver().cloud_driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

    def select_options(self, element, item, by='value'):
        """
        - Select the available options from drop down

        :param element:
        :param by:
        :param item:
        :return:
        """
        items = Select(element)
        for opt in items.options:
            if item in opt.text:
                self.utils.print_info(opt.text)

        select_by = {'value': items.select_by_value,
                     'index': items.select_by_index,
                     'visible_text': items.select_by_visible_text,
                     }
        try:
            select_by[by](item)
            return True
        except Exception:
            self.utils.print_info("Selecting item:{} not present in available options".format(item))
            return False

    def enable_check_box(self, element):
        """
        - Enable the check box

        :param element: check box locator element
        :return:None
        """
        if not element.is_selected():
            self.click(element)

    def disable_check_box(self, element):
        """
        - Disable the check box

        :param element:  check box locator element
        :return: None
        """
        if element.is_selected():
            self.click(element)

    def select_radio_button(self, element):
        """
        - Select the radio button

        :param element: radio button element
        :return:None
        """
        if not element.is_selected():
            self.click(element)

    def select_drop_down_options(self, options, item):
        """
        - Select the item from the drop down options
        - loop over the options and compare the text with item to be selected.
        - if item text present in options select that item element

        :param options: list of options
        :param item: element to be select based on item string
        :return: True if selected else None
        """
        if options:
            item_count = len(options)
            self.utils.print_debug(f"Iterating through {item_count} options to find {item.upper()}")
            for opt in options:
                self.utils.print_debug(f"Looking at dropdown option {opt.text.upper()}")
                if opt.text.upper() == item.upper():
                    self.utils.print_info("Selected opt:{}".format(opt.text))
                    self.click(opt)
                    return True

    def select_drop_down_options_partial_match(self, options, item):
        """
        - Select the item from the drop down options using a partial match - if the item is a sub string of
        - one of the options, the first found will be selected.
        - loop over the options and compare the text with item to be selected.
        - if item text present in options select that item element

        :param options: list of options
        :param item: element to be select based on item string using partial match
        :return: True if selected else None
        """
        if options:
            item_count = len(options)
            self.utils.print_debug(f"Iterating through {item_count} options to find {item.upper()} using a partial match")
            for opt in options:
                self.utils.print_debug(f"Looking at dropdown option {opt.text.upper()}")
                if item.upper() in opt.text.upper():
                    self.utils.print_info("Selected opt:{} using a partial match".format(opt.text))
                    self.click(opt)
                    return True

    def drag_and_drop_element(self, source_el, target_el):
        """
        - Drag and drop the element from Source Element to Target Element

        :param source_el: source element
        :param target_el: target element
        :return:1 if Element Drag and Drag successful else -1
        """
        try:
            actions = ActionChains(CloudDriver().cloud_driver)
            actions.drag_and_drop(source_el, target_el).perform()
            sleep(2)
            return 1
        except Exception:
            self.utils.print_info("drag and drop failed...")
            return -1

    def click_and_hold_element(self, source_el, offset_value=40):
        """
        - Click and hold the element

        :param source_el: source element
        :param offset_value: offset value
        :return:if Element Click and Hold successful else -1
        """
        try:
            actions = ActionChains(CloudDriver().cloud_driver)
            actions.click_and_hold(source_el).move_by_offset(offset_value, 0).release().perform()
            sleep(2)
            return 1
        except Exception:
            self.utils.print_info("Click and Hold element failed...")
            return -1

    def select_table_range(self, start_row, end_row):
        """
        - Selects a range in the table by clicking the first row, holding Shift, and clicking the last row.

        :param start_row: first row to select in the range
        :param end_row: last row to select in the range
        :return:  1 if action was successful, else -1
        """
        try:
            actions = ActionChains(CloudDriver().cloud_driver)
            actions.click(start_row).key_down(Keys.SHIFT).click(end_row).key_up(Keys.SHIFT).perform()
            sleep(2)
            return 1
        except Exception:
            self.utils.print_info("Select table range failed")
            return -1

    def enable_radio_button(self, element):
        """
        - This Keyword Uses to Enable Radio Button.

        :param element:  Radio Button locator element
        :return: None
        """
        if not element.is_selected():
            self.click(element)

    def disable_radio_button(self, element):
        """
        - This Keyword Uses to Disable Radio Button.

        :param element:  Radio Button locator element
        :return: None
        """
        if element.is_selected():
            self.click(element)

    def right_click(self, source_el):
        """
        - Right click (context click) the element

        :param source_el: source element
        :return: 1 if action was successful, else -1
        """
        if source_el is None:
            self.utils.print_info("Element to right click is not available - please check")
            self.screen.save_screen_shot()
            return -1
        else:
            try:
                actions = ActionChains(CloudDriver().cloud_driver)
                actions.context_click(source_el).perform()
                sleep(2)
                return 1
            except Exception:
                self.utils.print_info("Right click element failed")
                return -1

    def double_click(self, source_el):
        """
        - Double click the element

        :param source_el: source element
        :return: 1 if action was successful, else -1
        """
        try:
            actions = ActionChains(CloudDriver().cloud_driver)
            actions.double_click(source_el).perform()
            sleep(2)
            return 1
        except Exception:
            self.utils.print_info("Double click element failed")
            return -1

    def shift_click(self, source_el):
        """
        - Holds Shift while performing the click.  This is useful for multi-selecting items in a table.

        :param source_el: element to click with the Shift modifier
        :return:  1 if action was successful, else -1
        """
        try:
            actions = ActionChains(CloudDriver().cloud_driver)
            actions.key_down(Keys.SHIFT).click(source_el).key_up(Keys.SHIFT).perform()
            sleep(2)
            return 1
        except Exception:
            self.utils.print_info("Shift+click element failed")
            return -1

    def scroll_bottom(self):

        """
        - This Keyword Uses to Scroll to the bottom of a page.

        :return: None
        """
        CloudDriver().cloud_driver.find_element_by_tag_name('body').send_keys(Keys.END)
    def move_mouse_with_offset(self, x_offset, y_offset):
        """
        - Moves the mouse cursor with x ,y offsets from the current mouse position.

        :param y_offset:
        :param x_offset:
        :return: n/a
        """

        actions = ActionChains(CloudDriver().cloud_driver)
        actions.move_by_offset(x_offset, y_offset)
        actions.perform()

    def mouse_left_click(self):
        actions = ActionChains(CloudDriver().cloud_driver)
        actions.click().perform()

