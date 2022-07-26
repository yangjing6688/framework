from app.elements.AssignPolicyWebElements import *
from app.elements.NewDeviceOnboardWebElements import *
from extauto.common.AutoActions import *
import time


class AssignPolicy:
    def __init__(self):
        self.mob_login_web_elements = AssignPolicyWebElements()
        self.scan_web_elements = NewDeviceOnboardWebElements()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def assign_update_policy(self, policy):
        self.auto_actions.click(self.mob_login_web_elements.get_assign_policy())
        self.utils.print_info("user clicked on assign policy widget")
        self.auto_actions.click(self.mob_login_web_elements.get_np_backward_link())
        self.utils.print_info("user clicked on backward link")
        self.auto_actions.click(self.mob_login_web_elements.get_assign_policy())
        self.utils.print_info("user clicked on assign policy widget")
        time.sleep(1)
        self.auto_actions.send_keys(self.scan_web_elements.get_searched_np(), policy)
        self.utils.print_info("user searched policy name")
        time.sleep(3)
        np_rows = self.scan_web_elements.get_np_grid_rows()
        for np_row in np_rows:
            print(np_row.text)
            if policy in np_row.text:
                self.auto_actions.click(np_row)
                print(np_row)
                time.sleep(2)
                return 1

    def cancel_assign_policy(self):
        self.auto_actions.click(self.mob_login_web_elements.assign_policy_cancel_button())
        self.utils.print_info("user canceled the assign policy")
        time.sleep(5)

    def confirm_assign_policy(self):
        self.utils.print_info("user is on AP details screen")
        self.auto_actions.click(self.mob_login_web_elements.assign_policy_yes_button())
        self.utils.print_info("user confirmed the assign policy")
        time.sleep(10)
        self.auto_actions.click(self.mob_login_web_elements.get_update_policy())
        self.utils.print_info("user clicked on update policy widget")
        time.sleep(2)
        self.auto_actions.click(self.mob_login_web_elements.get_update_policy_cancel())
        self.utils.print_info("user canceled the update policy")
        time.sleep(8)
        self.auto_actions.click(self.mob_login_web_elements.get_update_policy())
        self.utils.print_info("user clicked on update policy widget")
        time.sleep(5)
        self.auto_actions.click(self.mob_login_web_elements.get_update_policy_confirm())
        self.utils.print_info("user confirmed the update policy")
        time.sleep(5)

