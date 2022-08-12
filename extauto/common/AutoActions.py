from time import sleep
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.CloudDriver import CloudDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AutoActions:
    def __init__(self):
        # self.driver = extauto.common.CloudDriver.cloud_driver
        self.retries = 5
        self.utils = Utils()
        self.screen = Screen()
        self.builtin = BuiltIn()

    def click(self, element):
        """
        - This Keyword Uses to Click the Mentioned Web Element
        - If the Element is not visible into view it Scroll element into view and Scroll down into page to click Element

        :param element: Web Element to Click on Web Page
        :return: None
        """

        if element is None:
            self.screen.save_screen_shot()
            self.builtin.fail(msg="Unable to Click the Element..No WebElement Handler Present for the Element."
                                  "So Exiting the Testcase")

        else:
            self.utils.print_debug("Clicking Element: ", element)
            count = 0
            while count < self.retries:
                try:
                    if type(element) is tuple:
                        self.click_image(element)
                    elif type(element) is list:
                        self.utils.print_info("Element is list...")
                        for ele in element:
                            ele.click()
                    else:
                        element.click()
                    return 1
                except ElementClickInterceptedException:
                    # To Overcome the Click Intercepted Exception we need to wait either explicit or implicit wait
                    # due to Xiq Application limitation we need to scroll the el into view, which is not visible on the page
                    # If scroll the el into view is not working will scroll down to the end of the page.
                    if count < 2:
                        self.utils.print_info("'Element Click Intercepted Exception': Scroll element into view")
                        CloudDriver().cloud_driver.execute_script("arguments[0].scrollIntoView(true); ", element)
                        sleep(2)
                    elif 2 < count < 4:
                        self.utils.print_info("'Element Click Intercepted Exception': Scroll down to page")
                        self.scroll_down()
                        sleep(2)
                    elif count == 4:
                        self.utils.print_info("'Element Click Intercepted Exception': trying javascript click().")
                        CloudDriver().cloud_driver.execute_script("arguments[0].click(); ", element)
                        sleep(2)
                    count += 1

                except StaleElementReferenceException:
                    self.utils.print_debug("Error: StaleElementReferenceException. Retrying after 5 seconds...")
                    count += 1
                    sleep(5)

                except ElementNotInteractableException:
                    self.utils.print_debug("Error: ElementNotInteractableException. Retrying after 5 seconds...")
                    count += 1
                    sleep(5)

                except Exception as e:
                    self.utils.print_info("Exception while click: ", e)
                    self.utils.print_info("Retrying after 5 seconds...")
                    sleep(5)
                    count += 1
                    if count == self.retries:
                        self.utils.print_warning("Unable to click the element. Saving Screenshot...")
                        self.screen.save_screen_shot()

    def move_to_element(self, element):
        """
        - This Keyword Uses to Move the Mentioned Web Element using Mouse Actions

        :param element: Web Element to Move the Mouse Cursor on Web Page
        :return: None
        """
        action = ActionChains(CloudDriver().cloud_driver)
        sleep(2)

        action.move_to_element(element)
        action.perform()
        sleep(2)

    def send_keys(self, element, value):
        """
        - This Keyword Uses to Send Clear the Text Area and Input the Mentioned Value on Text Field Web Element.

        :param element: Web Element To enter Text Field
        :param value: Element Text Field Value
        :return: None
        """
        self.utils.print_info("Sending Value to Element: ", value)
        if element is None:
            self.screen.save_screen_shot()
            self.builtin.fail(msg="Unable to Send value to the Element..No WebElement Handler Present for the Element."
                                  "So Exiting the Testcase")
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
        Select the available options from drop down
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
        except Exception as e:
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
        - select the radio button
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
        except:
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
        except:
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
        except:
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
            except:
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
        except:
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
        except:
            self.utils.print_info("Shift+click element failed")
            return -1
