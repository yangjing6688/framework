from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from extauto.common.Utils import *
from extauto.common.Screen import *
import extauto.app.common.CloudDriver


class AutoActions:
    def __init__(self):
        self.driver = app.common.CloudDriver.cloud_driver
        self.retries = 3
        self.utils = Utils()
        self.screen = Screen()

    def click(self, element):
        self.utils.print_debug("Clicking Element: ", element)
        count = 0
        while count < self.retries:
            try:
                if type(element) is tuple:
                    self.click_image(element)
                else:
                    element.click()
                return 1

            except Exception as e:
                self.utils.print_info("Exception while click: ", e)
                self.utils.print_info("Retrying after 5 seconds...")
                sleep(5)
                count += 1
                if count == self.retries:
                    self.utils.print_warning("Unable to click the element. Saving Screenshot...")
                    self.screen.save_screen_shot()

    def move_to_element(self, element):
        action = ActionChains(self.driver)
        time.sleep(2)

        action.move_to_element(element)
        action.perform()
        time.sleep(2)

    def send_keys(self, element, value):
        self.utils.print_info("Sending Value to Element: ", value)
        count = 0
        while count < self.retries:
            try:
                element.clear()
                element.send_keys(value)
                return 1
            except Exception as e:
                self.utils.print_warning("Exception while sending text: ", e)
                self.utils.print_info("Retrying after 2 seconds...")
                time.sleep(2)

                count += 1
                if count == self.retries:
                    self.utils.print_warning("Unable to enter text to element. Saving Screenshot...")
                    self.screen.save_screen_shot()

    def send_enter(self, element):
        self.utils.print_info("Sending ENTER Key")
        element.send_keys(Keys.ENTER)

    def send_page_down(self, element):
        self.utils.print_info("Sending ENTER Key")
        element.send_keys(Keys.PAGE_DOWN)

    def scroll_by(self):
        """
        Scroll the page by 250 pixels y-coordinate
        :return:
        """
        self.driver.execute_script("javascript:window.scrollBy(0,250)")

    def scroll_down(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

    def click_image(self, position):
        actions = ActionChains(self.driver)
        (x, y) = position
        actions.move_to_element_with_offset(self.driver.find_element_by_tag_name('body'), 0, 0)
        time.sleep(5)
        actions.move_by_offset(x, y).click().perform()
        return

    def center_element(self, element):
        """
        :param element:
        :return:
        """
        desired_y = (element.size['height'] / 2) + element.location['y']
        window_h = self.driver.execute_script('return window.innerHeight')
        window_y = self.driver.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y
        self.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

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
        :return:
        """
        if not element.is_selected():
            self.click(element)

    def disable_check_box(self, element):
        """
        - Disable the check box
        :param element:  check box locator element
        :return:
        """
        if element.is_selected():
            self.click(element)

    def select_radio_button(self, element):
        """
        - select the radio button
        :param element: radio button element
        :return:
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
        for opt in options:
            if opt.text.upper() == item.upper():
                self.utils.print_info("Selected opt:{}".format(opt.text))
                self.click(opt)
                return True
