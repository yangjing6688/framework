import json
import requests
from time import sleep
import common.CloudDriver
from common.Utils import Utils
from common.Screen import Screen
from xiq.flows.common.Navigator import Navigator
from xiq.elements.A3InventoryWebElements import A3InventoryWebElements


class A3Inventory(A3InventoryWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.driver = common.CloudDriver.cloud_driver
        self.navigator = Navigator()
        self.screen = Screen()


    def verify_a3_server_login_on_xiq(self, a3_login_username, a3_login_password):
        """
        - This keyword will verify A3 Server Access from XIQ UI using Go To A3 Button and Check A3 Login via XIQ
        - Assume that navigated to the A3 --> Inventory
        - Keyword Usage:
         - ``Verify A3 Server Login On XIQ   ${A3_IP_ADDR}   ${A3_USERNAME}  ${A3_PASSWORD}``

        :param a3_host_name: A3 Server Host Name
        :param a3_login_username: A3 Login Name to Access A3 UI
        :param a3_login_password: A3 Login Password Access A3 UI
        :return: A3 UI Page Title if Able to Login Successfully
        """


        self.utils.print_info("Logging A3 with Username : ", a3_login_username, " -- Password : ", a3_login_password)

        self.utils.print_info("Entering A3 Username...")
        self.auto_actions.send_keys(self.get_a3_login_username_field(), a3_login_username)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering A3 Password...")
        self.auto_actions.send_keys(self.get_a3_login_password_field(), a3_login_password)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking on Sign In button")
        self.auto_actions.click_reference(self.get_a3_login_button)
        sleep(8)

        self.screen.save_screen_shot()
        sleep(2)

        a3_page_title = self.driver.title
        self.utils.print_info("Page Title is : ", a3_page_title)
        return a3_page_title

