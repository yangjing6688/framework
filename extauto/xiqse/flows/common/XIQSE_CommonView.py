from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.elements.common.CommonViewWebElements import CommonViewWebElements
from selenium.common.exceptions import StaleElementReferenceException


class XIQSE_CommonView(CommonViewWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()

    def xiqse_wait_for_refresh_to_complete(self, retry_duration=2, retry_count=30):
        """
        - This keyword waits for the refresh to complete in the view
        - Keyword Usage
        - ``XIQSE Wait For Refresh To Complete``

        :param retry_duration: amount of time to wait in between each check for the refresh to be complete
        :param retry_count:    number of times to check for the search to be complete
        :return: 1 if action was successful, else -1
        """
        count = 1
        stale_retry = 1
        while stale_retry <= 10:
            try:
                while count <= retry_count:
                    self.utils.print_info(f"Waiting for refresh to complete: loop {count}")
                    load_mask = self.get_load_mask()
                    if load_mask:
                        self.utils.print_info("Refresh still in progress...")
                        sleep(retry_duration)
                    else:
                        self.utils.print_info("Refresh has completed")
                        return 1
                    count += 1
                break
            except StaleElementReferenceException:
                self.utils.print_info(f"Handling StaleElementReferenceException - loop {stale_retry}")
                stale_retry = stale_retry + 1

        self.utils.print_info("Refresh did not complete within specified time.")
        self.screen.save_screen_shot()

        return -1
