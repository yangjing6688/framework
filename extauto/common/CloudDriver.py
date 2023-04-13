import sauceclient
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from robot.libraries.BuiltIn import BuiltIn
from urllib3.exceptions import MaxRetryError
from extauto.common.Utils import Utils

class CloudDriver():
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(CloudDriver, cls).__new__(cls)
            cls.__instance.__initialized = False
            print(cls.__instance)
        return cls.__instance

    def __init__(self):
        if (self.__initialized): return
        self.cloud_driver = None
        self.__initialized = True

    def close_browser(self):
        if self.cloud_driver:
            self.cloud_driver.quit()
        self.__initialized = False

    def start_browser(self, url="default", program="default", incognito_mode="False"):
        self.cloud_driver = self.load_browser(url, program=program, incognito_mode=incognito_mode)
        return self

    def load_browser(self, url="default", program="default", incognito_mode="False"):
        """
        - This keyword will Load the default Test URL on Browser Mentioned in the topology file and environment file
        - Otherwise It Loads the Mentioned URL
        - By default it will not open the URL in Incognito Window
        - Keyword Usge:
             - ``Load Browser  url=${URL}``
             - ``Load Browser  url=${URL}   program=${PROGRAM}   incognito_mode=${INCOGNITO_MODE}``
        :param url: URL to Load on Browser
        :param program: cloud url by default othewise adsp,xiqse etc
        :param incognito_mode: Incognito Mode flag to open the browser
        :return: Cloud Driver
        """
        webdriver_ip = -1
        webdriver_port = -1
        proxy = "true"
        utils = Utils()
        browser = BuiltIn().get_variable_value("${BROWSER}")

        element_identify_value_name = "username"
        element_identify_value_id = "password"
        element_identify_value_css = ".eguest-username"
        element_identify_value_xpath = "//*[@class='success_text']"
        # Commented on 1/18/23 because they are unused
        # element_value = ".btn"
        # element_locator = "name"
        element_identify = "name"
        element_identify_value_name = "username"

        if program == 'approval':
            element_identify_value_xpath = "//*[@class='success_text']"
            element_identify = "xpath"
            utils.print_info("Approval")
        elif program == 'a3':
            if "admin" in url and "login" in url:
                element_identify = "class-name"
                element_identify_value_css = ".secondary-button"
            else:
                element_identify = "id"
                element_identify_value_id = "username"
        elif program == 'adsp':
            element_identify_value_name = "j_username"
            element_identify = "name"
        elif program == 'xiqse':
            if "xiqLicenseSetup.jsp" in url:
                xiqse_version = BuiltIn().get_variable_value("${XIQSE_OS_VERSION}")
                if xiqse_version:
                    if "21.4." in xiqse_version:
                        element_identify_value_id = "licenseContentDiv"
                        element_identify = "id"
                    else:
                        element_identify_value_id = "xiqLicSetupDiv"
                        element_identify = "id"
                else:
                    utils.print_info("XIQSE_OS_VERSION was not specified - defaulting to latest version")
                    element_identify_value_id = "xiqLicSetupDiv"
                    element_identify = "id"
            else:
                element_identify_value_name = "j_username"
                element_identify = "name"
        elif program == "clientmode":
            element_identify = 'name'
            element_identify_value_name = 'userName'

        if url == "default":
            url = BuiltIn().get_variable_value("${TEST_URL}")

        if "hotmail" in url:
            element_identify_value_name = "loginfmt"
            element_identify = "name"

        if "eguest" in url:
            element_identify = "class-name"
            element_identify_value_css = ".eguest-username"

        if "setupverify" in url:
            element_identify = "class-name"
            element_identify_value_css = ".btn"

        if "resetverify" in url:
            element_identify = "class-name"
            element_identify_value_css = ".btn"

        if "sso" in url:
            element_identify_value_name = "UserName"
            element_identify = "name"

        if "google" in url:
            element_identify = 'q'

        mode = BuiltIn().get_variable_value("${WEB_DRIVER_LOC}")
        os_platform = BuiltIn().get_variable_value("${OS_PLATFORM}")

        utils.print_info("Opening URL: ", url)
        if BuiltIn().get_variable_value("${WEB_DRIVER_LOC}") == "bstack":
            bstack_os = BuiltIn().get_variable_value("${BSTACK_OS}")
            bstack_os_version = BuiltIn().get_variable_value("${BSTACK_OS_VERSION}")
            bstack_browser = BuiltIn().get_variable_value("${BSTACK_BROWSER}")
            bstack_browser_version = BuiltIn().get_variable_value("${BSTACK_BROWSER_VERSION}")
            bstack_url = BuiltIn().get_variable_value("${BSTACK_URL}")

            caps = {
                'os_version': bstack_os_version,
                'os': bstack_os,
                'browser': bstack_browser,
                'browser_version': bstack_browser_version,
                'name': 'ExtAuto-BStack',
                'build': 'BStack-TestBuild'
            }

            utils.print_info("Browser Stack URL: ", bstack_url)
            cloud_driver = webdriver.Remote(desired_capabilities=caps, command_executor=bstack_url)

        if BuiltIn().get_variable_value("${WEB_DRIVER_LOC}") == "sauce":
            utils.print_info("Environment: Sauce Labs")
            sauce_os = BuiltIn().get_variable_value("${SAUCE_OS}")
            sauce_browser = BuiltIn().get_variable_value("${SAUCE_BROWSER}")
            sauce_browser_version = BuiltIn().get_variable_value("${SAUCE_BROWSER_VER}")
            sauce_resolution = BuiltIn().get_variable_value("${SAUCE_RESULATION}")
            sauce_session_name = BuiltIn().get_variable_value("${SAUCE_SESSION_NAME}") + str(datetime.now())
            sauce_build = utils.get_config_value("sauce_build")

            sauce_url = BuiltIn().get_variable_value("${SAUCE_URL}")
            sauce_idle_timeout = BuiltIn().get_variable_value("${SAUCE_IDLE_TIMEOUT}")

            sauce_tags = os_platform + " " + sauce_browser + "-" + sauce_browser_version + " " + sauce_resolution

            caps = dict()
            caps['browserName'] = sauce_browser
            caps['platform'] = sauce_os
            caps['version'] = sauce_browser_version
            caps['screenResolution'] = sauce_resolution
            caps['name'] = sauce_session_name
            caps['tags'] = sauce_tags
            caps['build'] = sauce_build
            caps['idleTimeout'] = sauce_idle_timeout

            utils.print_info("Sauce Labs URL: ", sauce_url)
            cloud_driver = webdriver.Remote(desired_capabilities=caps, command_executor=sauce_url)

            sauce_username = BuiltIn().get_variable_value("${SAUCE_USERNAME}")
            sauce_access_key = BuiltIn().get_variable_value("${SAUCE_KEY}")
            sc = sauceclient.SauceClient(sauce_username, sauce_access_key)
            jobs = sc.jobs.get_jobs(full=True, limit=1)

            utils.print_info("Sauce Labs Job Details: ", jobs)
            utils.print_info("Sauce Labs Username: ", sauce_username)
            utils.print_info("Sauce Labs Password: ", sauce_access_key)

        if mode == "remote":
            if os_platform == "windows":
                utils.print_info("Windows 7 OS selected")
                webdriver_ip = BuiltIn().get_variable_value("${WINDOWS7}")

            if os_platform == "windows10":
                utils.print_info("Windows 10 OS selected")
                webdriver_ip = BuiltIn().get_variable_value("${WINDOWS10}")

            if os_platform == "linux":
                utils.print_info("Linux OS selected")
                webdriver_ip = BuiltIn().get_variable_value("${LINUX}")

            if os_platform == "mac":
                utils.print_info("MAC OS selected")
                webdriver_ip = BuiltIn().get_variable_value("${MAC}")

            webdriver_port = BuiltIn().get_variable_value("${WEBDRIVER_PORT}")

        print("WebDriver Mode: ", mode)

        proxy_enable = BuiltIn().get_variable_value("${PROXY_STATUS}")

        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        if incognito_mode == "True":
            chrome_options.add_argument("--incognito")

        if browser == "chrome":
            if proxy_enable == "true":
                utils.print_info("Proxy is set")
                if proxy != "none":
                    proxy_url = utils.get_config_value("proxy_url")
                    utils.print_info("Proxy URL: ", proxy_url)

                    webdriver.DesiredCapabilities.CHROME['proxy'] = {
                        "httpProxy": proxy_url,
                        "ftpProxy": proxy_url,
                        "sslProxy": proxy_url,
                        "noProxy": None,
                        "proxyType": "MANUAL",
                        "class": "org.openqa.selenium.Proxy",
                        "autodetect": False,
                    }

            if incognito_mode == "True":
                utils.print_info("Adding incognito mode to chromeOptions")
                webdriver.DesiredCapabilities.CHROME['chromeOptions'] = {
                    "args": ["--disable-extensions", "--ignore-certificate-errors", "--incognito",
                             "--disable-geolocation"]
                }
            else:
                webdriver.DesiredCapabilities.CHROME['chromeOptions'] = {
                    "args": ["--disable-extensions", "--ignore-certificate-errors", "--disable-geolocation"]
                }

            try:
                chrome_options.add_argument('--allow-running-insecure-content')
                chrome_options.add_argument('--ignore-certificate-errors')

                if mode == "local":
                    cloud_driver = webdriver.Chrome(chrome_options=chrome_options)

                if mode == "remote":
                    try:
                        utils.print_info(f"Redirecting to Remote WebDriver at http://{str(webdriver_ip)}:",
                                         str(webdriver_port), "/wd/hub")
                        host_url = "http://" + str(webdriver_ip) + ":" + str(webdriver_port) + "/wd/hub"
                        cloud_driver = webdriver.Remote(host_url, webdriver.DesiredCapabilities.CHROME)
                    except (MaxRetryError, WebDriverException) as err:
                        utils.print_info("Issue in loading browser in Remote host ", err)
                        return -2

            except Exception as e:
                utils.print_info("Unable to load the URL. Error: ", str(e))
                return -1

        if browser == "firefox":
            if proxy_enable == "true":
                utils.print_info("Proxy is set")
                if proxy != "none":
                    proxy_url = utils.get_config_value("proxy_url")
                    utils.print_info("Proxy URL : " + proxy_url)

                    webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
                        "httpProxy": proxy_url,
                        "ftpProxy": proxy_url,
                        "sslProxy": proxy_url,
                        "noProxy": None,
                        "proxyType": "MANUAL",
                        "class": "org.openqa.selenium.Proxy",
                        "autodetect": False
                    }

            ff_profile = webdriver.FirefoxProfile()
            if incognito_mode == "True":
                ff_profile.set_preference("browser.privatebrowsing.autostart", True)
                utils.print_info("Adding incognito mode to firefoxOptions")
                webdriver.DesiredCapabilities.FIREFOX['moz:firefoxOptions'] = {
                    "args": ["--private"]
                }

            if mode == "local":
                cloud_driver = webdriver.Firefox(firefox_profile=ff_profile)

            if mode == "remote":
                utils.print_info("Redirecting to Remote WebDriver at http://", webdriver_ip, ":", webdriver_port,
                                 "/wd/hub")
                host_url = "http://" + str(webdriver_ip) + ":" + str(webdriver_port) + "/wd/hub"
                cloud_driver = webdriver.Remote(host_url, webdriver.DesiredCapabilities.FIREFOX)

        if browser == "safari":
            if proxy_enable == "true":
                utils.print_info("Proxy is set")
                if proxy != "none":
                    proxy_url = utils.get_config_value("proxy_url")
                    utils.print_info("Proxy URL : " + proxy_url)

                    webdriver.DesiredCapabilities.SAFARI['proxy'] = {
                        "httpProxy": proxy_url,
                        "ftpProxy": proxy_url,
                        "sslProxy": proxy_url,
                        "noProxy": None,
                        "proxyType": "MANUAL",
                        "class": "org.openqa.selenium.Proxy",
                        "autodetect": False
                    }
            if mode == "local":
                cloud_driver = webdriver.Safari()

            if mode == "remote":
                utils.print_info("Redirecting to Remote WebDriver at http://", webdriver_ip, ":", webdriver_port,
                                 "/wd/hub")
                host_url = "http://" + str(webdriver_ip) + ":" + str(webdriver_port) + "/wd/hub"
                cloud_driver = webdriver.Remote(host_url, webdriver.DesiredCapabilities.SAFARI)

        if browser == "ie":
            if proxy_enable == "true":
                utils.print_info("Proxy is set")

                if proxy != "none":
                    proxy_url = utils.get_config_value("proxy_url")
                    utils.print_info("Proxy URL : " + proxy_url)

                    webdriver.DesiredCapabilities.INTERNETEXPLORER['proxy'] = {
                        "httpProxy": proxy_url,
                        "ftpProxy": proxy_url,
                        "sslProxy": proxy_url,
                        "noProxy": None,
                        "proxyType": "MANUAL",
                        "class": "org.openqa.selenium.Proxy",
                        "autodetect": False,
                        "acceptSslCerts": True,
                        "trustAllSSLCertificates": True
                    }
            if mode == "local":
                cloud_driver = webdriver.Ie()

            if mode == "remote":
                utils.print_info("Redirecting to Remote WebDriver at http://", webdriver_ip, ":", webdriver_port,
                                 "/wd/hub")
                host_url = "http://" + str(webdriver_ip) + ":" + str(webdriver_port) + "/wd/hub"
                cloud_driver = webdriver.Remote(host_url, webdriver.DesiredCapabilities.INTERNETEXPLORER)

        if browser == "edge":
            if proxy_enable == "true":
                utils.print_info("Proxy is set")

                if proxy != "none":
                    proxy_url = utils.get_config_value("proxy_url")
                    utils.print_info("Proxy URL : " + proxy_url)

                    webdriver.DesiredCapabilities.EDGE['proxy'] = {
                        "httpProxy": proxy_url,
                        "ftpProxy": proxy_url,
                        "sslProxy": proxy_url,
                        "noProxy": None,
                        "proxyType": "MANUAL",
                        "class": "org.openqa.selenium.Proxy",
                        "autodetect": False
                    }

            if mode == "local":
                cloud_driver = webdriver.Edge()

            if mode == "remote":
                utils.print_info("Redirecting to Remote WebDriver at http://", webdriver_ip, ":", webdriver_port,
                                 "/wd/hub")
                host_url = "http://" + str(webdriver_ip) + ":" + str(webdriver_port) + "/wd/hub"
                cloud_driver = webdriver.Remote(host_url, webdriver.DesiredCapabilities.EDGE)

        cloud_driver.maximize_window()
        cloud_driver.get(url)

        utils.print_info(f"Waiting for {url} page to load...")

        if element_identify == "name":
            WebDriverWait(cloud_driver, 60).until(
                ec.presence_of_element_located((By.NAME, element_identify_value_name)))

        if element_identify == "id":
            WebDriverWait(cloud_driver, 60).until(ec.presence_of_element_located((By.ID, element_identify_value_id)))

        if element_identify == "class-name":
            WebDriverWait(cloud_driver, 60).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, element_identify_value_css)))

        if element_identify == "xpath":
            WebDriverWait(cloud_driver, 60).until(
                ec.presence_of_element_located((By.XPATH, element_identify_value_xpath)))

        utils.print_info("Page Loaded Successfully")

        return cloud_driver

    def open_window(self, url="default", program="default"):
        """
        - This keyword will Load the default Test URL mentioned in topology file on new windows handles
         - Keyword Usage:
            - ``Open Window  url=${URL}``
            - ``Open Window  url=${URL}   program=${PROGRAM}``
        :param url: URL to Load on Browser
        :param program: cloud url by default othewise adsp,xiqse etc
        :return: Windows Index
        """
        utils = Utils()

        element_identify_value_name = "username"
        element_identify_value_id = "password"
        element_identify_value_css = ".eguest-username"
        # Commented on 1/18/23 because they are unused
        # element_value = ".btn"
        # element_locator = "name"
        element_identify = "name"
        element_identify_value_name = "username"
        element_identify_value_xpath = "//app-auth-failure"

        if "airdefense" in url:
            element_identify = "xpath"
            element_identify_value_xpath = "//app-auth-failure"

        if program == 'adsp':
            element_identify_value_name = "j_username"
            element_identify = "name"

        if program == 'xiqse':
            element_identify_value_name = "j_username"
            element_identify = "name"

        if url == "default":
            url = BuiltIn().get_variable_value("${TEST_URL}")

        if "hotmail" in url:
            element_identify_value_name = "loginfmt"
            element_identify = "name"

        if "eguest" in url:
            element_identify = "class-name"
            element_identify_value_css = ".eguest-username"

        if "setupverify" in url:
            element_identify = "class-name"
            element_identify_value_css = ".btn"

        if "resetverify" in url:
            element_identify = "class-name"
            element_identify_value_css = ".btn"

        if program == 'a3':
            element_identify = "id"
            element_identify_value_id = "username"

        if "admin" in url and "login" in url:
            element_identify = "class-name"
            element_identify_value_css = ".secondary-button"

        utils.print_info("Opening New Window")
        self.cloud_driver.execute_script("window.open();")
        window_handles = self.cloud_driver.window_handles
        win_count = len(window_handles)
        utils.print_debug(f"Window Handle Count: {win_count}")
        window_index = win_count - 1
        self.cloud_driver.switch_to.window(self.cloud_driver.window_handles[window_index])

        utils.print_info("Opening URL: ", url)
        self.cloud_driver.get(url)
        utils.print_debug(f"New Window Title: {self.cloud_driver.title}")

        utils.print_info("Waiting for login page to load...")

        if element_identify == "name":
            WebDriverWait(self.cloud_driver, 60).until(
                ec.presence_of_element_located((By.NAME, element_identify_value_name)))

        if element_identify == "xpath":
            WebDriverWait(self.cloud_driver, 60).until(
                ec.presence_of_element_located((By.XPATH, element_identify_value_xpath)))

        if element_identify == "id":
            WebDriverWait(self.cloud_driver, 60).until(
                ec.presence_of_element_located((By.ID, element_identify_value_id)))

        if element_identify == "class-name":
            WebDriverWait(self.cloud_driver, 60).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, element_identify_value_css)))

        utils.print_info("Page Loaded Successfully")

        utils.print_debug(f"Returning Window Index {window_index}")
        return window_index

    def switch_to_window(self, win_index=0):
        """
        - This keyword will switch to Windows handles based on windows index value
        - By default it will switch to windows handles index 0
        - Keyword Usage:
          - ``Switch To Window``
          - ``Switch To Window  win_index=${INDEX_VALUE}``
        :param win_index: windows index value
        :return:None
        """
        utils = Utils()
        win_index=int(win_index)
        window_handles = self.cloud_driver.window_handles
        win_count = len(window_handles)
        utils.print_debug(f"Window Handle Count: {win_count}")
        if win_index < win_count:
            utils.print_info(f"Switching to Window Index {win_index}")
            self.cloud_driver.switch_to.window(self.cloud_driver.window_handles[win_index])
        else:
            utils.print_info(f"Window Index {win_index} out of range ({win_count})")

    def close_window(self, win_index=0):
        """
        - This keyword will close Windows handles based on windows index value
        - By default it will close windows handles index 0
        - Keyword Usage:
          - ``Close Window``
          - ``Close Window  win_index=${INDEX_VALUE}``
        :param win_index: windows index value
        :return:None
        """
        utils = Utils()
        win_index=int(win_index)
        window_handles = self.cloud_driver.window_handles
        win_count = len(window_handles)
        utils.print_debug(f"Window Handle Count: {win_count}")
        if win_index < win_count:
            utils.print_info(f"Closing window with Window Index {win_index}")
            self.cloud_driver.switch_to.window(self.cloud_driver.window_handles[win_index])
            self.cloud_driver.close()
            # If the last window was closed, reset the cloud driver to -1
            if win_count == 1:
                self.cloud_driver = -1
        else:
            utils.print_info(f"Window Index {win_index} out of range ({win_count})")

    def get_child_window_list(self, win_index=0):
        """
        - This keyword will obtain the Windows handles for any child windows that are open.
        - The order of the list is reversed to handle the conditional test within 'Switch To Window'
        - The parent window is not included in the returned list.
        - Keyword Usage:
          - ``Get Child Window List``
        :param: win_index - XIQ Window Index value
        :return: List of Child Window Indexes (list order reversed)
        """
        utils = Utils()
        index = 0
        window_list = []
        window_handles = self.cloud_driver.window_handles
        win_count = len(window_handles)
        utils.print_debug(f"get_child_window_list: Window Handle Count: {win_count}")
        utils.print_debug("get_child_window_list: Iterating through the Window Handles...")
        for window_handle in window_handles:
            utils.print_debug(f"Window Index: {index} || Window Handle: {window_handle}")
            if index > win_index:
                window_list.append(index)
            index += 1

        if len(window_list) > 0:
            window_list.sort(reverse=True)

        return window_list

    def refresh_page(self):
        utils = Utils()
        utils.print_info("Refreshing page")
        self.cloud_driver.refresh()