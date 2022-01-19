import sauceclient
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as ec
from appium import webdriver as webdriver
from selenium.webdriver.chrome.options import Options
from robot.libraries.BuiltIn import BuiltIn

from extauto.common.Utils import Utils

desired_cap = {
    "deviceName": "Google_Pixel_2_XL_real_us",
    "platformName": "Android",
    "platformVersion": "9.1.0",
    "automationName": "UiAutomator2",
    "deviceOrientation": "portrait",
    "app": "storage:filename=app-release.apk",
    "name": "Google_Pixel_3a_real"
}

desired = {
    "deviceName": "P8B4C18127007561",
    "platformName": "Android",
    "platformVersion": "9.0",
    "automationName": "UiAutomator2",
    "deviceOrientation": "portrait",
    "app": "C:\\Users\\prkumara\\Documents\\software\\appium\\app-release.apk"
}


cloud_driver = -1
job_id = -1


def load_browser(url="default", program="default"):
    global cloud_driver
    global job_id

    webdriver_ip = -1
    webdriver_port = -1
    proxy = "true"
    utils = Utils()
    browser = BuiltIn().get_variable_value("${BROWSER}")
    

    element_identify_value_name = "username"
    element_identify_value_id = "password"
    element_identify_value_css = ".eguest-username"
    element_value = ".btn"
    element_locator = "name"
    element_identify = "name"
    element_identify_value_name = "username"

    if program == 'adsp':
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

    mode = BuiltIn().get_variable_value("${WEB_DRIVER_LOC}")
    os_platform = BuiltIn().get_variable_value("${OS_PLATFORM}")
    # utils.print_info("Opening URL: ", url)

    utils.print_info("Opening URL: ", url)

    if BuiltIn().get_variable_value("${TARGET_ENV}") == "sauce":
        utils.print_info("Environment: Sauce Labs")
        sauce_os = BuiltIn().get_variable_value("${SOUCE_OS}")
        sauce_browser = BuiltIn().get_variable_value("${SOUCE_BROWSER}")
        sauce_browser_version = BuiltIn().get_variable_value("${SOUCE_BROWSER_VER}")
        sauce_resolution = BuiltIn().get_variable_value("${SOUCE_RESULATION}")
        sauce_session_name = BuiltIn().get_variable_value("${SOUCE_SESSION_NAME}") + str(datetime.now())
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

    #chrome_options = Options()
    #chrome_options.add_argument("--disable-extensions")

    if browser == "appium":
        if mode == "local":
            #cloud_driver = webdriver.Remote(url, desired_cap)
            cloud_driver = webdriver.Remote(url, desired_cap)

        if mode == "remote":
            #utils.print_info("Redirecting to Remote WebDriver at http://", webdriver_ip, ":",
                             #webdriver_port, "/wd/hub")
            #host_url = "http://" + str(webdriver_ip) + ":" + str(webdriver_port) + "/wd/hub"
            cloud_driver = webdriver.Remote(url, desired_cap)


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
        if mode == "local":
            cloud_driver = webdriver.Firefox()

        if mode == "remote":
            utils.print_info("Redirecting to Remote WebDriver at http://", webdriver_ip, ":", webdriver_port, "/wd/hub")
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
            utils.print_info("Redirecting to Remote WebDriver at http://", webdriver_ip, ":", webdriver_port, "/wd/hub")
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
            utils.print_info("Redirecting to Remote WebDriver at http://", webdriver_ip, ":", webdriver_port, "/wd/hub")
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
            utils.print_info("Redirecting to Remote WebDriver at http://", webdriver_ip, ":", webdriver_port, "/wd/hub")
            host_url = "http://" + str(webdriver_ip) + ":" + str(webdriver_port) + "/wd/hub"
            cloud_driver = webdriver.Remote(host_url, webdriver.DesiredCapabilities.EDGE)

    return cloud_driver
