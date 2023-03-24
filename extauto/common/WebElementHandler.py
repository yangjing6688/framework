import json
import os
from string import Template

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, ElementNotInteractableException

from extauto.common.CloudDriver import CloudDriver
from extauto.common.Utils import Utils
from extauto.common.ImageHandler import ImageHandler


class WebElementHandler:
    def __init__(self):
        self.utils = Utils()
        self.delay = 10 # BuiltIn().get_variable_value('${ELEMENT_DELAY}')
        self.desc = None
        self.image_handler = ImageHandler()
        self.locator = {"CSS_SELECTOR": By.CSS_SELECTOR,
                         "XPATH": By.XPATH,
                         "TAG_NAME": By.TAG_NAME,
                         "NAME": By.NAME,
                        "CLASS_NAME": By.CLASS_NAME,
                        "ID": By.ID
                        }
        self.ignored_exceptions = [NoSuchElementException,
                                   ElementNotVisibleException,
                                   ElementNotSelectableException,
                                   ElementNotInteractableException]

    def check_for_page_is_loading(self, driver):
        while True:
            x = driver.execute_script("return document.readyState")
            self.utils.print_info("Page returned: " + str(x))
            if str(x).lower() == "complete" or str(x).lower() == "interactive":
                return True
            else:
                yield False

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
        _driver = CloudDriver().cloud_driver if parent == "default" else parent

        # Log what we're searching for
        self.utils.print_info(f"get_element(): key_val: {key_val}")

        self.utils.print_debug("Waiting for page to complete loading")
        while not self.check_for_page_is_loading(_driver):
            continue
        self.utils.print_debug("Page completed loading")

        for key, value in key_val.items():
            if 'IMAGE' in key:
                icon_path = os.getenv('FRAMEWORK_PATH') + "/xiq/defs/images/" + value
                self.utils.print_info("icon_path:", icon_path)

                return self.image_handler.get_position(icon_path)
            if key in self.locator.keys():  # check the key is in locator or not
                by = self.locator[key]
            else:
                continue
            try:
                self.utils.print_debug("Using locator Type: {} Value: {} Index: {} Wait: {} Description: {}"
                                                .format(key, value, _index, _delay, _desc))
                if list:
                    if type(value) is list:
                        self.utils.print_info("Element has multiple definitions: ", value)

                if list and type(_index) is list:
                    handles_list = []
                    self.utils.print_info("Index is an array: ", _index)
                    for each_index in _index:
                        self.utils.print_info("trying with index :", each_index)
                        try:
                            handles_list.append(WebDriverWait(_driver, _delay, ignored_exceptions=self.ignored_exceptions).until(
                                ec.presence_of_all_elements_located((by, value)))[each_index])
                        except Exception:
                            self.utils.print_info("Unable to find element with Index: ", each_index)
                    self.utils.print_info("Handles List: ", handles_list)
                    if handles_list.length == 0:
                        self.utils.print_info('Unable to find web element ', json.dumps(key_val))
                    return handles_list
                if _index == 0:
                    return WebDriverWait(_driver, _delay, ignored_exceptions=self.ignored_exceptions).until(
                        ec.presence_of_element_located((by, value)))
                else:
                    return WebDriverWait(_driver, _delay, ignored_exceptions=self.ignored_exceptions).until(
                        ec.presence_of_all_elements_located((by, value)))[_index]

            except Exception:
                self.utils.print_debug("Unable to find the element handle with: ", key, ' -- ', value)
                self.utils.print_debug('Unable to find web element ', json.dumps(key_val))

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
        _driver = CloudDriver().cloud_driver if parent == "default" else parent

        # Log what we're searching for
        self.utils.print_info(f"get_element(): key_val: {key_val}")

        for key, value in key_val.items():
            if key in self.locator.keys():  # check the key is in locator or not
                by = self.locator[key]
            else:
                continue
            try:
                self.utils.print_debug(
                    "Using locator type:{} value:{} Index:{} wait:{}".format(key, value, _index, _delay))
                if _index == 0:
                    return WebDriverWait(_driver, _delay, ignored_exceptions=self.ignored_exceptions).until(
                        ec.presence_of_all_elements_located((by, value)))
                else:
                    return WebDriverWait(_driver, _delay, ignored_exceptions=self.ignored_exceptions).until(
                        ec.presence_of_all_elements_located((by, value)))[_index]

            except Exception:
                self.utils.print_debug("Unable to find the element handle with: ", key, ' -- ', value)
        return None

    def get_a_href(self, element):
        self.utils.print_debug("Using locator TAG_NAME Index:0 Wait:0")
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

    def _substitute_template_args(self, key_val_template, kwargs):
        """
        Substitutes kwargs for the kwarg names enclosed in ${} within the
        value of each key/value pair in the specified dictionary object.
        """
        key_val = {}
        for key, value in key_val_template.items():
            if isinstance(value, str):
                key_val[key] = Template(value).safe_substitute(kwargs)
            else:
                key_val[key] = value
        return key_val

    def get_template_element(self, key_val_template, parent='default', **kwargs):
        """
        Get element based on key, value pairs defined in key_val_template dictionary.
        Replaces kwarg names enclosed in ${} with kwarg values in each string
        value defined in the key_val_template dictionary.
        For example,
            Suppose the following key value dictionary definition
            template_example = \
                {
                    'DESC': 'This finds a panel with title="${title}"',
                    'XPATH': '//div[contains(@id, "panel-title") and text()="${title}"]',

                }
            self.weh.get_template_element(template_example, title="Devices")
            self.weh.get_template_element(template_example, title="Policy")
        :param key_val_template: (dict) containing the locator:value ex: 'CSS_SELECTOR': '.btn.btn-primary-2.btn-dim'
        :param parent: (str)
        :param kwargs: (dict) containing key value pairs to replace in key_val_template string values
        """
        key_val = self._substitute_template_args(key_val_template, kwargs)
        self.utils.print_debug(f"get_template_element key_val: {key_val}")
        return self.get_element(key_val, parent)

    def get_template_elements(self, key_val_template, parent='default', **kwargs):
        """
        Get elements based on key, value pairs defined in key_val_template dictionary.
        Replaces kwarg names enclosed in ${} with kwarg values in each string
        value defined in the key_val_template dictionary.
        For example,
            Suppose the following key value dictionary definition:
            list_dropdown_items = \
            {
                'DESC': 'Drop down items for a list type dropdown (li)',
                'XPATH': '//div[contains(@id, "${element_id}") and contains(@id, "-picker-listWrap")]/ul/li',

            }
            You would then get the elements by passing in the element ID:
            self.weh.get_template_elements(list_dropdown_items, element_id="combo-id")
        :param key_val_template: (dict) containing the locator:value ex: 'CSS_SELECTOR': '.btn.btn-primary-2.btn-dim'
        :param parent: (str)
        :param kwargs: (dict) containing key value pairs to replace in key_val_template string values
        """
        key_val = self._substitute_template_args(key_val_template, kwargs)
        self.utils.print_debug(f"get_template_element key_val: {key_val}")
        return self.get_elements(key_val, parent)
