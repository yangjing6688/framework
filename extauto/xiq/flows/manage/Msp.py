from time import sleep

from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.xiq.elements.MspWebElements import MspWebElements
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.common.CommonValidation import CommonValidation

class Msp(MspWebElements):

    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.auto_actions = AutoActions()
        self.utils = Utils()
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
        self.utils.print_info("Clicking View All Organization")
        self.auto_actions.click_reference(self.get_view_organization_button)
        self.screen.save_screen_shot()

        self.utils.print_info(f"Enter Organization Name {organization_name} in search field")
        self.auto_actions.send_keys(self.get_organization_search_text_field(), organization_name)
        sleep(2)
        self.auto_actions.click_reference(self.get_organization_search_result_option)
        self.screen.save_screen_shot()

        rows = self.get_organization_grid_rows()
        if rows:
            if organization_name:
                self.utils.print_info(f"Selecting Organization Name {organization_name}")
                for row in rows:
                    if organization_name in row.text:
                        self.utils.print_info(f"Organization Name {organization_name} exist")

                        configure_radio_button = self.get_organizations_select_radio_button()
                        self.utils.print_info(f"Clicking Organization {organization_name} Configure Radio Button")
                        if not configure_radio_button.is_selected():
                            self.auto_actions.click_reference(self.get_organizations_select_radio_button)
                            self.screen.save_screen_shot()

                        check_box = self.get_organizations_select_check_box()
                        if check_box:
                            if not check_box.is_selected():
                                self.utils.print_info(f"Clicking Organization {organization_name} View checkbox")
                                self.auto_actions.click_reference(self.get_organizations_select_check_box)
                                self.screen.save_screen_shot()


                        self.utils.print_info("Click Organizations close button")
                        self.auto_actions.click_reference(self.get_view_organization_close_button)
                        self.screen.save_screen_shot()

                        kwargs['pass_msg'] = f"Given Organization Name {organization_name} Selected Sucessfully " \
                                             f"on MSP Account"
                        self.common_validation.passed(**kwargs)
                        return 1

        else:
            kwargs['fail_msg'] = f"Given Organization Name {organization_name} Row Not Found and Not Selected " \
                                 f"Sucessfully on MSP Account"
            self.common_validation.failed(**kwargs)
            return -1

    def unselect_organization(self, organization_name=None, **kwargs):
        """
        - Flow: Manage--> View Organizations
        - This keyword will unselect Organization in MSP account
        - Keyword Usage:
        - ``UnSelect Organization  organization_name=${ORG_NAME}   ``

        :param organization_name: Organization Name
        :return: 1 if Mentioned organization Name is UnSelected Successfully else -1
        """

        self.navigator.navigate_to_devices()
        self.utils.print_info("Clicking View All Organization")
        self.auto_actions.click_reference(self.get_view_organization_button)
        self.screen.save_screen_shot()

        self.utils.print_info(f"Enter Organization Name {organization_name} in search field")
        self.auto_actions.send_keys(self.get_organization_search_text_field(), organization_name)
        sleep(2)
        self.auto_actions.click_reference(self.get_organization_search_result_option)
        self.screen.save_screen_shot()

        rows = self.get_organization_grid_rows()
        if rows:
            if organization_name:
                self.utils.print_info(f"Selecting Organization Name {organization_name}")
                for row in rows:
                    if organization_name in row.text:
                        self.utils.print_info(f"Organization Name {organization_name} exist")

                        configure_radio_button = self.get_organizations_select_radio_button()
                        self.utils.print_info(f"Disabling Organization {organization_name} Configure Radio Button")
                        if configure_radio_button.is_selected():
                            self.auto_actions.click_reference(self.get_organizations_select_radio_button)
                            self.screen.save_screen_shot()
                            sleep(2)

                        check_box_status = self.get_organizations_check_box_enabled_status()
                        if check_box_status:
                            self.utils.print_info(f"Unchecking Organization {organization_name} View checkbox")
                            self.auto_actions.click_reference(self.get_organizations_select_check_box)
                            self.screen.save_screen_shot()
                            sleep(2)

                        self.utils.print_info("Click Organizations close button")
                        self.auto_actions.click_reference(self.get_view_organization_close_button)
                        self.screen.save_screen_shot()

                        kwargs['pass_msg'] = f"Given Organization Name {organization_name} UnSelected Sucessfully " \
                                             f"on MSP Account"
                        self.common_validation.passed(**kwargs)
                        return 1

        else:
            kwargs['fail_msg'] = f"Given Organization Name {organization_name} Row Not Found and Not UnSelected " \
                                 f"Sucessfully on MSP Account"
            self.common_validation.failed(**kwargs)
            return -1