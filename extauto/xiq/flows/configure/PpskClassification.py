from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.common.CommonValidation import CommonValidation

from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.PpskClassificationWebElements import PpskClassificationWebElements


class PpskClassification(object):

    def __init__(self):
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.screen = Screen()
        self.common_validation = CommonValidation()
        self.ppsk_classification_web_elements = PpskClassificationWebElements()

    def add_ppsk_classification_rule_to_user(self, network_name, user_name, classification_rule, **kwargs):
        """

        - Flow: Configure --> Users --> User Management --> PPSK Classification
        - Select mentioned network from dropdown
        - Add PPSK Classification Rule for the mentioned Network
        - Keyword Usage
        ``Add PPSK Classification rule to User     ${Network_Policy}        ${PPSK_USER}        ${Classification_Rule}``

        :param network_name: Name of the Network Policy
        :param user_name: Name of the PPSK User created in the User Group
        :param classification_rule: Classification Rule to be attached to User
        :return: 1 if success else -1

        """
        self.utils.print_info("Click on Network Policy card view button")
        self.navigator.navigate_to_configure_ppsk_classification()

        self.auto_actions.click_reference(self.ppsk_classification_web_elements.get_ppsk_classification_network_dropdown)
        sleep(2)

        network_list = self.ppsk_classification_web_elements.get_all_networks_from_dropdown()
        if self.auto_actions.select_drop_down_options(network_list, network_name):
            self.utils.print_info("Selected network: %s from dropdown" % network_name)
        else:
            kwargs['fail_msg'] = " add_ppsk_classification_rule_to_user() failed. Network not present in the dropdown"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)

        self.utils.print_info("Clicking on PPSK Classification Rule Add Button")
        self.auto_actions.click_reference(self.ppsk_classification_web_elements.get_ppsk_classification_rule_add_button)
        sleep(2)

        self.utils.print_info("Clicking on PPSK Classification User Select Dropdown")
        self.auto_actions.click_reference(self.ppsk_classification_web_elements.get_ppsk_classification_users_dropdown)
        sleep(2)

        ppsk_users = self.ppsk_classification_web_elements.get_ppsk_classification_users_list()
        if self.auto_actions.select_drop_down_options(ppsk_users, user_name):
            self.utils.print_info("Selected user: %s from dropdown" % user_name)
        else:
            kwargs['fail_msg'] = " add_ppsk_classification_rule_to_user() failed. User not present in the dropdown"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)

        self.utils.print_info("Clicking on Add User Button")
        self.auto_actions.click_reference(self.ppsk_classification_web_elements.get_add_user_button)
        sleep(2)

        self.utils.print_info("Clicking on Select ClassificationRule Icon")
        self.auto_actions.click_reference(self.ppsk_classification_web_elements.get_select_classification_rule_button)
        sleep(2)

        self.utils.print_info("Selecting ClassificationRule Rule")
        classification_rule_all = self.ppsk_classification_web_elements.get_classification_all_rule()
        self.auto_actions.select_drop_down_options(classification_rule_all, classification_rule)
        sleep(1)

        self.auto_actions.click_reference(self.ppsk_classification_web_elements.get_link_button)
        sleep(1)

        self.auto_actions.click_reference(self.ppsk_classification_web_elements.get_save_button)

        if self.verify_ppsk_classification_rule_to_user(network_name, user_name, classification_rule):
            kwargs['pass_msg'] = "Classification Rule attached to User"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "add_ppsk_classification_rule_to_user() failed. " \
                                 "PPSK ClassificationRule not added correctly"
            self.common_validation.failed(**kwargs)
            return -1

    def edit_ppsk_classification_rule_to_user(self, network_name, user_name, classification_rule, **kwargs):
        """

        - Flow: Configure --> Users --> User Management --> PPSK Classification
        - Select mentioned network from dropdown
        - Edit the row Select new PPSK Classification Rule for the mentioned user
        - Keyword Usage
        ``Edit Ppsk Classification rule to User  ${Network_Policy}  ${PPSK_USER}  ${Classification_Rule}``

        :param network_name: Name of the Network Policy
        :param user_name: Name of the PPSK User created in the User Group
        :param classification_rule: Classification Rule to be attached to User
        :return: 1 if success else -1

        """
        self.utils.print_info("Click on Network Policy card view button")
        self.navigator.navigate_to_configure_ppsk_classification()

        self.auto_actions.click_reference(self.ppsk_classification_web_elements.get_ppsk_classification_network_dropdown)
        sleep(2)

        network_list = self.ppsk_classification_web_elements.get_all_networks_from_dropdown()
        if self.auto_actions.select_drop_down_options(network_list, network_name):
            self.utils.print_info("Selected network: %s from dropdown" % network_name)
        else:
            kwargs['fail_msg'] = "edit_ppsk_classification_rule_to_user() failed. Network not present in the dropdown"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)

        users_rule = self.ppsk_classification_web_elements.get_ppsk_classification_users_row()
        for user_rule in users_rule:
            if user_name in user_rule.text:
                self.utils.print_info("Found user: %s, Clicking on Edit Button" % user_name)
                self.auto_actions.click(self.ppsk_classification_web_elements.get_edit_button(user_rule))
                sleep(2)

                self.utils.print_info("Clicking on Select ClassificationRule Icon")
                self.auto_actions.click_reference(
                    self.ppsk_classification_web_elements.get_select_classification_rule_button)
                sleep(2)

                self.utils.print_info("Selecting ClassificationRule Rule")
                classification_rule_all = self.ppsk_classification_web_elements.get_classification_all_rule()
                self.auto_actions.select_drop_down_options(classification_rule_all, classification_rule)
                sleep(1)

                self.auto_actions.click_reference(self.ppsk_classification_web_elements.get_link_button)
                sleep(1)

                self.auto_actions.click_reference(self.ppsk_classification_web_elements.get_save_button)

        if self.verify_ppsk_classification_rule_to_user(network_name, user_name, classification_rule):
            kwargs['pass_msg'] = "PPSK ClassificationRule edited correctly"
            self.common_validation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "edit_ppsk_classification_rule_to_user() failed. " \
                                 "PPSK ClassificationRule not edited correctly"
            self.common_validation.failed(**kwargs)
            return -1

    def verify_ppsk_classification_rule_to_user(self, network_name, user_name, classification_rule, **kwargs):
        """
        - Flow: Configure --> Users --> User Management --> PPSK Classification
        - Select mentioned network from dropdowm
        - Select the row and verify PPSK Classification Rule for the mentioned user
        - Keyword Usage
        - ``Verify Ppsk Classification rule to User     ${NETWORK_NAME}     ${PPSK_USER}      ${CLASSIFICATION_RULE}``

        :param network_name: Name of the Network Policy
        :param user_name: Name of the PPSK User created in the User Group
        :param classification_rule: Classification Rule to be attached to User
        :return: 1 if success else -1
        """
        self.utils.print_info("Click on Network Policy card view button")
        self.navigator.navigate_to_configure_ppsk_classification()

        self.auto_actions.click_reference(self.ppsk_classification_web_elements.get_ppsk_classification_network_dropdown)
        sleep(3)

        network_list = self.ppsk_classification_web_elements.get_all_networks_from_dropdown()
        if self.auto_actions.select_drop_down_options(network_list, network_name):
            self.utils.print_info("Selected network: %s from dropdown" % network_name)
        else:
            kwargs['fail_msg'] = "verify_ppsk_classification_rule_to_user() failed. " \
                                 "Network not present in the dropdown"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)

        users_rule = self.ppsk_classification_web_elements.get_ppsk_classification_users_row()
        for user_rule in users_rule:
            if user_name in user_rule.text:
                self.utils.print_info("Found user: %s" % user_name)
                if self.ppsk_classification_web_elements.get_user_assigned_classification_rule(user_rule).text.strip()\
                        == classification_rule:

                    self.utils.print_info("PPSK Classification rule %s attached to user: %s"
                                          % (classification_rule, user_name))
                    return 1
                else:
                    self.utils.print_info(
                        "PPSK Classification rule %s not attached to user: %s" % (classification_rule, user_name))
                    kwargs['fail_msg'] = f"verify_ppsk_classification_rule_to_user() failed. " \
                                         f"PPSK Classification rule {classification_rule} not attached to user: {user_name}"
                    self.common_validation.fault(**kwargs)
                    return -1

        kwargs['fail_msg'] = f"verify_ppsk_classification_rule_to_user() failed. " \
                             f"user: {user_name} not found in PPSK Classification Rule Table"
        self.common_validation.failed(**kwargs)
        return -1

    def delete_all_ppsk_classification_rule_user(self, network_name, **kwargs):
        """

        - Flow: Configure --> Users --> User Management --> PPSK Classification
        - Select mentioned network from dropdown
        - Delete all the PPSK classification users entries for the mentioned network
        - Keyword Usage
        - ``Delete all PPSK Classification rule User     ${NETWORK_NAME} ``

        :param network_name: Name of the Network Policy
        :return: 1 if success

        """
        self.utils.print_info("Click on Network Policy card view button")
        self.navigator.navigate_to_configure_ppsk_classification()

        self.auto_actions.click_reference(self.ppsk_classification_web_elements.get_ppsk_classification_network_dropdown)
        sleep(2)

        network_list = self.ppsk_classification_web_elements.get_all_networks_from_dropdown()
        if self.auto_actions.select_drop_down_options(network_list, network_name):
            self.utils.print_info("Selected network: %s from dropdown" % network_name)
        else:
            kwargs['fail_msg'] = "delete_all_ppsk_classification_rule_user() failed. " \
                                 "Network not present in the dropdown"
            self.common_validation.fault(**kwargs)
            return -1
        sleep(2)

        self.utils.print_info("Selecting all ppsk users")
        self.auto_actions.click_reference(self.ppsk_classification_web_elements.get_select_all_ppsk_users)
        sleep(1)

        self.utils.print_info("Deleting all ppsk users")
        self.auto_actions.click_reference(self.ppsk_classification_web_elements.get_delete_ppsk_user)
        sleep(2)

        self.auto_actions.click_reference(self.ppsk_classification_web_elements.get_yes_confirmation_button)
        kwargs['pass_msg'] = "Deleted all PPSK Classification rule User"
        self.common_validation.passed(**kwargs)
        return 1
