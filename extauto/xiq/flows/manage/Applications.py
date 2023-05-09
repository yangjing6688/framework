from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.elements.ApplicationsWebElements import ApplicationsWebElements
from extauto.common.CommonValidation import CommonValidation


class Applications(object):

    def __init__(self):
        self.utils = Utils()
        self.screen = Screen()
        self.auto_actions = AutoActions()
        self.navigator = Navigator()
        self.app_web_elements = ApplicationsWebElements()
        self.commonValidation = CommonValidation()

    def add_custom_applications(self, application_name, group_name, **kwargs):
        """
        - This keyword will create Custom Application under Manage > Applications.
        - Flow: Manage --> Applications --> Manage Applications --> ADD CUSTOM
        - Keyword Usage:
        - ``Add Custom Applications  ${APPLICATION_NAME}  ${GROUP_NAME}``

        :param application_name: Custom application name
        :param group_name: group name
        :return: 1 if success and -1 if fails
        """

        self.utils.print_info("Click on Manage Applications Tab")
        self.auto_actions.click_reference(self.app_web_elements.get_manage_applications)

        self.utils.print_info("Click on Add Custom button")
        self.auto_actions.click_reference(self.app_web_elements.get_manage_add_custom)

        self.utils.print_info("Enter Application name")
        self.auto_actions.send_keys(self.app_web_elements.get_manage_add_custom_name_textfield(), application_name)
        self.screen.save_screen_shot()

        self.utils.print_info("Click on Add Custom applications")
        self.auto_actions.click_reference(self.app_web_elements.get_manage_add_custom_add_app)

        self.utils.print_info("Enter Group name")
        self.auto_actions.send_keys(self.app_web_elements.get_manage_add_custom_group_name_textfield(), group_name)
        self.screen.save_screen_shot()

        self.utils.print_info("clicking Save Button")
        self.auto_actions.click_reference(self.app_web_elements.get_manage_add_custom_group_name_save)
        sleep(5)

        self.utils.print_info("clicking Save Button")
        self.auto_actions.click_reference(self.app_web_elements.get_manage_add_custom_app_save)
        sleep(3)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        self.utils.print_info("clicking on application dialog box close button")
        self.auto_actions.click_reference(self.app_web_elements.get_application_dialogbox_close_tab)

        if "Add Custom Application successfully." in tool_tp_text[-1]:
            kwargs['pass_msg'] = "Add Custom Application successfully."
            self.commonValidation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unable to add custom application"
            self.commonValidation.failed(**kwargs)
            return -1

    def edit_custom_applications(self, application_name, application_name_modified, **kwargs):
        """
        - This keyword will modify Custom Application under Manage > Applications.
        - Flow: Manage --> Applications --> Manage Applications --> Search and select an application --> Edit application
        - Keyword Usage:
        - ``Edit Custom Application  ${APPLICATION_NAME}  ${APPLICATION_NAME_MODIFIED}``

        :param application_name: Custom application name
        :param application_name_modified: Modified application name
        :return: 1 if success and -1 if fails
        """

        self.utils.print_info("Click on Manage Applications Tab")
        self.auto_actions.click_reference(self.app_web_elements.get_manage_applications)

        self.utils.print_info("Click on Search Application field")
        self.auto_actions.click_reference(self.app_web_elements.get_manage_add_custom_app_search)

        self.utils.print_info("Enter the Application name")
        self.auto_actions.send_keys(self.app_web_elements.get_manage_add_custom_search_text(), application_name)
        self.utils.wait_till(self.app_web_elements.get_manage_apps_cell, timeout=20, delay=5)

        self.utils.print_info("Click on Application Check box")
        self.auto_actions.click_reference(self.app_web_elements.get_manage_apps_cell)

        self.utils.print_info("Click on Edit button")
        self.auto_actions.click_reference(self.app_web_elements.get_manage_add_custom_edit)

        self.utils.print_info("Enter the modified name")
        self.auto_actions.send_keys(self.app_web_elements.get_manage_add_custom_name_textfield(),
                                    application_name_modified)
        self.screen.save_screen_shot()

        self.utils.print_info("clicking Save Button")
        self.auto_actions.click_reference(self.app_web_elements.get_manage_add_custom_app_save)
        sleep(3)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        self.utils.print_info("clicking on application dialog box close button")
        self.auto_actions.click_reference(self.app_web_elements.get_application_dialogbox_close_button)

        if "Edit Custom Application successfully." in tool_tp_text[-1]:
            kwargs['pass_msg'] = "Edit Custom Application successfully."
            self.commonValidation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unable to edit custom application"
            self.commonValidation.failed(**kwargs)
            return -1

    def delete_custom_applications(self, application_name_modified, **kwargs):
        """
        - This keyword will delete Custom Application under Manage > Applications.
        - Flow: Manage --> Applications --> Manage Applications --> Search and select an application --> Delete application
        - Keyword Usage:
        - ``Delete Custom Applications  ${APPLICATION_NAME_MODIFIED}``

        :param application_name_modified: Modified application name
        :return: 1 if success and -1 if fails
        """

        self.utils.print_info("Click on Manage Applications Tab")
        self.auto_actions.click_reference(self.app_web_elements.get_manage_applications)

        self.utils.print_info("Click on Search Application field")
        self.auto_actions.click_reference(self.app_web_elements.get_manage_add_custom_app_search)

        self.utils.print_info("Enter the Application name")
        self.auto_actions.send_keys(self.app_web_elements.get_manage_add_custom_search_text(), application_name_modified)
        self.utils.wait_till(self.app_web_elements.get_manage_apps_cell, timeout=20, delay=5)

        self.utils.print_info("Click on Application Check box")
        self.auto_actions.click_reference(self.app_web_elements.get_manage_apps_cell)

        self.utils.print_info("Click on Delete button")
        self.auto_actions.click_reference(self.app_web_elements.get_manage_add_custom_delete)

        self.utils.print_info("clicking on Yes to confirm delete operation")
        self.auto_actions.click_reference(self.app_web_elements.get_manage_add_custom_delete_confirm)
        sleep(3)

        tool_tp_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tp_text)

        self.utils.print_info("clicking on application dialog box close button")
        self.auto_actions.click_reference(self.app_web_elements.get_application_dialogbox_close_button)

        if "Custom Application was successfully deleted." in tool_tp_text[-1]:
            kwargs['pass_msg'] = "Custom Application was successfully deleted."
            self.commonValidation.passed(**kwargs)
            return 1
        else:
            kwargs['fail_msg'] = "Unable to delete custom application"
            self.commonValidation.failed(**kwargs)
            return -1
