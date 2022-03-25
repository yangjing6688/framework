import os
from common.CloudDriver import CloudDriver
from extauto.common.Utils import Utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from robot.libraries.BuiltIn import BuiltIn


class WebElementHandler:
    def __init__(self):
        self.el_info = BuiltIn().get_variable_value('${ELEMENT_INFO}')
        self.utils = Utils()
        self.delay = 10
        self.desc = None
        self.driver = extauto.common.CloudDriver.cloud_driver
        self.locator = {"CSS_SELECTOR": By.CSS_SELECTOR,
                         "XPATH": By.XPATH,
                         "TAG_NAME": By.TAG_NAME,
                         "NAME": By.NAME,
                        "CLASS_NAME": By.CLASS_NAME,
                        "ID": By.ID
                        }

    def get_element(self, key_val, parent='default'):
        """
        get the web element based on the locators provided in key_val dictionary
        :param key_val: (dict) containing the locator:value ex: 'CSS_SELECTOR': '.btn.btn-primary-2.btn-dim'
        :param parent: (str)
        :return:(obj) web elements obj
        """
        _index = key_val.get('index', 0)  # web element index
        _delay = key_val.get('wait_for', self.delay)  # Explicit delay
        _desc = key_val.get('DESC', self.desc)  # Explicit delay
        _driver = self.driver if parent == "default" else parent

        for key, value in key_val.items():
            if key in self.locator.keys():  # check the key is in locator or not
                by = self.locator[key]
            else:
                continue
            try:
                if 'True' in self.el_info:
                    self.utils.print_info("Using locator Type: {} Value: {} Index: {} Wait: {} Description: {}"
                                          .format(key, value, _index, _delay, _desc))

                if _index == 0:
                    return WebDriverWait(_driver, _delay).until(ec.presence_of_element_located((by, value)))
                else:
                    return WebDriverWait(_driver, _delay).until(ec.presence_of_all_elements_located((by, value)))[_index]

            except Exception as e:
                if 'True' in self.el_info:
                    self.utils.print_info("Unable to find the element handle with: ", key, ' -- ', value)
        return None

    def get_elements(self, key_val, parent='default'):
        """
        Get the web elements
        :param key_val: (dict) containing the locator:value ex: 'CSS_SELECTOR': '.btn.btn-primary-2.btn-dim'
        :param parent: (str) driver object
        :return:(obj) web elements obj
        """
        _index = key_val.get('index', 0)  # web element index
        _delay = key_val.get('wait_for', self.delay)  # Explicit delay
        _driver = self.driver if parent == "default" else parent

        for key, value in key_val.items():
            if key in self.locator.keys():  # check the key is in locator or not
                by = self.locator[key]
            else:
                continue
            try:
                if 'True' in self.el_info:
                    self.utils.print_info(
                        "Using locator type:{} value:{} Index:{} wait:{}".format(key, value, _index, _delay))
                if _index == 0:
                    return WebDriverWait(_driver, _delay).until(ec.presence_of_all_elements_located((by, value)))
                else:
                    return WebDriverWait(_driver, _delay).until(ec.presence_of_all_elements_located((by, value)))[_index]

            except Exception as e:
                if 'True' in self.el_info:
                    self.utils.print_info(e)
                    self.utils.print_info("Unable to find the element handle with: ", key, ' -- ', value)
        return False

    def get_a_href(self, element):
        if 'True' in self.el_info:
            self.utils.print_info("Using locator TAG_NAME Index:0 Wait:0")
        return element.find_element_by_tag_name('a')

    def get_displayed_element(self, elements):
        """
        From the list of elements get the displayed element on web page

        :param elements: (list)  list of elements
        :return: (obj) displayed element
        """
        for el in elements:
            if el.is_displayed():
                return el
