from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from extauto.common.Screen import Screen


class LoadBrowser:
    def __init__(self):
        self.driver = None
        self.screen = Screen()

    def load_browser(self, url, remote_host=None):
        try:
            caps = webdriver.DesiredCapabilities.CHROME.copy()
            ops = Options()
            ops.add_argument('--disable-notifications')
            self.driver = webdriver.Remote(desired_capabilities=caps,
                                           command_executor="http://" + remote_host + ":4444/wd/hub", options=ops)
        except Exception as e:
            print(e)
            print("Unable to load the URL.. Exiting..")
            sleep(2)

        print("Loading Page with URL: ", url)
        self.driver.maximize_window()
        try:
            self.driver.get(url)
        except Exception as e:
            pass
        sleep(3)
        got_title = self.driver.title
        print("Page Title: ", got_title)
        self.screen.save_screen_shot(self.driver)
        sleep(2)
        return got_title

    def quite_approve_browser(self):
        self.driver.quit()
