from time import sleep
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import AutoActions
from xiqse.flows.control.policy.XIQSE_ControlPolicyService import XIQSE_ControlPolicyService
from xiqse.elements.control.policy.ControlPolicyServiceCreateWebElements import ControlPolicyServiceCreateWebElements


class XIQSE_ControlPolicyServiceCreate(ControlPolicyServiceCreateWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.serv_els = XIQSE_ControlPolicyService()

    def xiqse_control_policy_create_service(self, service_name, service_type="local"):
        """
        - This keyword creates a service (local or global).
        :param service_name:
        :param service_type: local or global
        :return: 1 if success, else -1
        """
        ret_val = -1
        go = 1

        # actions:
        #  For Global service: expand "Service Repository", and then "Global Services (All Domains)"
        #  For Local service: expand "Service Repository", and then "Local Services"
        #   launch "Create Service" window from the popup menu of the "Services" node and create the service
        if self.serv_els.expand_service_tree_node("Service Repository") == 1:
            if service_type == "global":
                self.serv_els.expand_service_tree_node("Global Services (All Domains)")
                self.serv_els.collapse_service_tree_node("Local Services")
            elif service_type == "local":
                self.serv_els.expand_service_tree_node("Local Services")
                self.serv_els.collapse_service_tree_node("Global Services (All Domains)")
            else:
                self.utils.print_info("Unknown service type.  A service should either be 'local' or 'global')")
                go = -1

        if (go == 1 and
                self.serv_els.right_click_service_tree_node("Services") and
                self._launch_create_service_window() and
                self._create_service(service_name) and
                self._check_name_in_use_error(service_name)):
            ret_val = 1
            self.utils.print_info(f"Successfully created '{service_type}' service - {service_name}")
            sleep(1)
        return ret_val

    def _launch_create_service_window(self):
        ret_val = -1
        create_menu = self.get_create_service_menu()
        if create_menu:
            self.utils.print_info("Launching the 'Create Service' window")
            self.auto_actions.click(create_menu)
            ret_val = 1
        else:
            self.utils.print_info("Unable to launch the 'Create Service' window")
        return ret_val

    def _create_service(self, service_name):
        ret_val = -1
        input_name = self.get_name_input()
        if input_name:
            self.utils.print_info(f"Entering '{service_name}' in the Name input field in Create Service window")
            self.auto_actions.send_keys(input_name, service_name)
            self._click_ok_button()
            # check for "service name is in-use" error
            if self._check_name_in_use_error(service_name) == 1:
                ret_val = 1
        else:
            self.utils.print_info(f"Unable to find 'Name' input field in Create Service window")
            self.screen.save_screen_shot()
        return ret_val

    def _click_ok_button(self):
        ret_val = -1
        ok_bttn = self.get_ok_button()
        if ok_bttn:
            self.utils.print_info(f"Clicking the 'OK' button in Create Service window")
            self.auto_actions.click(ok_bttn)
            ret_val = 1
        else:
            self.utils.print_info(f"Unable to locate the 'OK' button in Create Service window")
            self.screen.save_screen_shot()
        return ret_val

    def _check_name_in_use_error(self, service_name):
        """
        :param service_name:
        :return:  -1 if error is present, else 1
        """
        ret_val = -1

        self.utils.print_info(f"Checking if the service name '{service_name}' is already in-use")
        err_msg = self.get_name_in_use_error()
        if err_msg:
            self.utils.print_info(f"A service with name '{service_name}' already exists")
            self.screen.save_screen_shot()
            self.auto_actions.click(self.get_error_ok_button())
            self.auto_actions.click(self.get_cancel_button())
        else:
            self.utils.print_info(f"A service with name '{service_name}' is not in-use. Continue...")
            ret_val = 1

        return ret_val
