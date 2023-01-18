from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from extauto.common.tools.remote.captiveportal.CPWebElementDefinitions import CPWebElementDefinitions


class CPWebElements(CPWebElementDefinitions):

    def __init__(self):
        self.delay = 20
        self.driver = None
        self.locator = {"CSS_SELECTOR": By.CSS_SELECTOR,
                         "XPATH": By.XPATH,
                         "TAG_NAME": By.TAG_NAME,
                         "NAME": By.NAME,
                        "CLASS_NAME": By.CLASS_NAME,
                        }

    def rm_open_cp_browser(self, mu_ip, url=None):
        """
        Open captive portal browser on the remote mu
        :param mu_ip: Ip of the remote mu
        :param url: url to open
        :return:
        """
        if not url:
            url = 'http://www.cnn.com/'
        print("Opening CP Web browser on MU")
        try:
            caps = webdriver.DesiredCapabilities.CHROME.copy()
            ops = Options()
            ops.add_argument('--disable-notifications')
            self.driver = webdriver.Remote(desired_capabilities=caps,
                                           command_executor="http://" + mu_ip + ":4444/wd/hub", options=ops)
        except Exception as e:
            print(e)
            print("Unable to load the URL.. Exiting..")
            sleep(2)

        print("Loading Page with URL: ", url)
        self.driver.maximize_window()
        self.driver.get(url)
        sleep(2)
        got_title = self.driver.title
        print("Page Title: ", got_title)
        return 1

    def _get_element(self, key_val, parent='default'):
        """
        get the web element based on the locators provided in key_val dictionary
        :param key_val: (dict) containing the locator:value ex: 'CSS_SELECTOR': '.btn.btn-primary-2.btn-dim'
        :param parent: (str)
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
                print(
                    "Using locator type:{} value:{} Index:{} wait:{}".format(key, value, _index, _delay))
                if _index == 0:
                    return WebDriverWait(_driver, _delay).until(ec.presence_of_element_located((by, value)))
                else:
                    return WebDriverWait(_driver, _delay).until(ec.presence_of_all_elements_located((by, value)))[_index]

            except Exception:
                print("Unable to find the element handle with: ", key, ' -- ', value)
        return None

    @property
    def get_page_title(self):
        return self.driver.title

    def get_acceptance_button(self):
        """
        Get acceptance button element
        :return:
        """
        return self._get_element(self.user_acceptance_page_accept_button)
