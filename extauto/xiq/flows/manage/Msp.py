from time import sleep
import datetime
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.xiq.elements.MspWebElements import MspWebElements
from extauto.xiq.flows.manage.Devices import *
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.common.CommonValidation import CommonValidation

class Msp(MspWebElements):

    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.auto_actions = AutoActions()
        self.utils = Utils()
        self.devices = Devices()
        self.screen = Screen()
        self.common_validation = CommonValidation()

    def select_organization(self, organization_name=None, **kwargs):
        """
        - Flow: Manage--> View Organizations
        - This keyword will select Organization in MSP account
        - Keyword Usage:
         - ``Select Organization  organization_name=${ORG_NAME}   ``

        :param organization_name: Organization Name
        :return: 1 if Mentioned organization Name is Selected Successfully else -1
        """
        self.navigator.navigate_to_devices()
        self.utils.print_info(f"Clicking View All Organization")
        self.auto_actions.click(self.get_view_organization_button())

        self.utils.print_info("Click on full page view")
        if self.cobj_web_elements.get_paze_size_element():
            self.auto_actions.click_reference(self.get_paze_size_element)
            sleep(5)

        # Get the total pages
        pages = self.get_page_numbers()
        if pages.text != '':
            last_page = int(pages.text[-1])
        else:
            last_page = 1
        page_counter = 0
        self.utils.print_info(f"There are {last_page} page(s) to check")
        while page_counter < last_page:
            self.utils.print_info(f"Checking Organization Name {organization_name} in the Page {page_counter+1}")
            select_org_flag = None

            rows = self.get_organization_grid_rows()
            if rows:
                if organization_name:
                    self.utils.print_info(f"Selecting Organization Name {organization_name}")
                    for row in rows:
                        if organization_name in row.text:
                            check_box = self.get_organizations_select_check_box(row)
                            if check_box:
                                self.utils.print_info(f"Clicking Organization {organization_name} checkbox")
                                self.auto_actions.click(check_box)
                                select_org_flag = True
                                self.screen.save_screen_shot()

                                self.utils.print_info("Click Organizations close button")
                                self.auto_actions.click(self.get_view_organization_close_button())
                            else:
                                self.utils.print_info(f"Organization Name {organization_name} doesn't exist in the page {page_counter + 1}")

                            # goto the next page
                            page_counter += 1
                            self.utils.print_info(f"Move to next page {page_counter + 1}")
                            self.auto_actions.click_reference(self.cobj_web_elements.get_next_page_element)
                            sleep(5)
            if select_org_flag:

