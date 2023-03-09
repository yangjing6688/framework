from time import sleep
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.MLInsightsWebElements import MLInsightsWebElements
from extauto.xiq.elements.DialogWebElements import DialogWebElements
from extauto.common.CommonValidation import CommonValidation


class MLInsights:

    def __init__(self):
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.mlinsights_web_elements = MLInsightsWebElements()
        self.dialogue_web_elements = DialogWebElements()
        self.common_validation = CommonValidation()

    def create_location_in_ml_insights(self, **kwargs):
        """
        - Create the Location on ML Insights Network 360 Plan using Name,address and city information
        - Flow: ML Insights--> Network 360 Plan
        :param kwargs: Name ,Address,city
        :return:1 if successfully created Location on ML Insights--> Network 360 Plan
        """

        self.utils.print_info("Navigating to Network 360 plan..")
        if self.navigator.navigate_to_network360plan() == -2:
            kwargs['fail_msg'] = "Unsuccessfully navigating to Network 360 plan"
            self.common_validation.failed(**kwargs)
            return -2
        sleep(5)

        tooltip_text = self.dialogue_web_elements.get_tooltip_text()
        sleep(2)

        self.utils.print_info("tooltip_text: ", tooltip_text)
        if tooltip_text:
            if "Your account does not have permission to perform that action" in tooltip_text:
                self.auto_actions.click_reference(self.mlinsights_web_elements.get_map_close_btn)
                sleep(10)
                kwargs['fail_msg'] = "Your account does not have permission to perform that action"
                self.common_validation.failed(**kwargs)
                return -2

        self.utils.print_info("Create a new map...")
        self.auto_actions.click_reference(self.mlinsights_web_elements.get_create_new_map_btn)

        organization = kwargs.get('organization')
        street_addr = kwargs.get('street_addr')
        city = kwargs.get('city')
        # country = kwargs.get('country')

        # import sys, pdb
        # pdb.Pdb(stdout=sys.__stdout__).set_trace()

        self.utils.print_info("Entering organization: ", organization)
        self.auto_actions.send_keys(self.mlinsights_web_elements.get_map_organization_text(), organization)
        sleep(2)

        self.utils.print_info("Entering street_addr: ", street_addr)
        self.auto_actions.send_keys(self.mlinsights_web_elements.get_map_street_addr_text(), street_addr)
        sleep(2)

        self.utils.print_info("Entering city: ", city)
        self.auto_actions.send_keys(self.mlinsights_web_elements.get_map_city_text(), city)
        sleep(2)

        self.utils.print_info("Saving the configuration")
        self.auto_actions.click_reference(self.mlinsights_web_elements.get_map_save_btn)
        sleep(2)
        return 1
