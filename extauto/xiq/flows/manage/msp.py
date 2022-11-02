from time import sleep
import datetime
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.xiq.elements.MspWebElements import *
from extauto.xiq.flows.manage.Devices import *
from extauto.xiq.flows.common.Navigator import Navigator

class Msp(MspWebElements):

    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.auto_actions = AutoActions()
        self.utils = Utils()
        self.devices = Devices()
        self.screen = Screen()

    def select_organization(self, organization_name=None):
        """

        """
        self.utils.wait_till(self.get_organization_grid_rows, timeout=20, delay=1, is_logging_enabled=True)
        rows = self.get_organization_grid_rows()
        if rows:
            if organization_name:
                self.utils.print_info(f"Selecting Organization Name {organization_name}")
                for row in rows:
                    self.utils.print_info("All rows: ", self.format_row(row.text))
                    if organization_name in row.text:
                        self.utils.print_info("Found organization name Row: ", self.format_row(row.text))
                        check_box = self.get_organizations_select_check_box(row)
                        if check_box:
                            self.auto_actions.click(check_box)
                            self.utils.print_info("checkbox selected ")
                            return 1
                        else:
                            self.utils.print_info("checkbox not found ")
                        self.screen.save_screen_shot()
        else:
            self.utils.print_info("No rows present")

        self.utils.print_info("Did not find specified row")
        self.screen.save_screen_shot()

        return 1