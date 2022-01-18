from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Device.Common.PromptHandler.PromptObj import PromptObj
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants


class BasePromptHandler(object):
    def __init__(self, device):
        self.logger = Logger()
        self.constants = NetworkElementConstants()
        self.prompt_chain = [PromptObj(self.constants.PROMPT_USER)]
        self.device = device
        self.debug = True
        self.prompt_dict = {self.constants.PROMPT_USER: lambda x: True}

    def set_agent_attrs(self, *args):
        """
        This function sets the following device current agent attributes, "default_sleep_between_commands",
        "wait_for_retries", and "wait_for_sleep". It returns the original values so they can be restored later.
        """
        sleep = self.device.current_agent.default_sleep_between_commands
        wait_for_retry = self.device.current_agent.wait_for_retries
        wait_for_sleep = self.device.current_agent.wait_for_sleep

        self.device.current_agent.default_sleep_between_commands_ms = args[0]
        self.device.current_agent.wait_for_retries = args[1]
        self.device.current_agent.wait_for_sleep = args[2]

        return sleep, wait_for_retry, wait_for_sleep

    def reset_agent_attrs(self, *args):
        """
        This function sets device's current agent attributes back to their original values.
        """
        self.device.current_agent.default_sleep_between_commands = args[0]
        self.device.current_agent.wait_for_retries = args[1]
        self.device.current_agent.wait_for_sleep = args[2]

    def change_prompt(self, prompt, arg_list):
        """
        This function checks which prompt the user is trying to navigate to. If it is a supported prompt
        then the corresponding handle function is called. Otherwise a ValueError is raised.
        """
        orig_vals = self.set_agent_attrs(0, 0, 0)
        error_string = ""

        current_prompt = self.prompt_chain[-1]
        arg_list = arg_list.split("||") if arg_list is not None else []

        self.log_debug("Prompt change requested")
        self.log_debug("Arg list: [" + ", ".join(arg_list) + "]")
        self.log_debug("   current prompt name: (" + current_prompt.prompt_name + ")")
        self.log_debug("   prompt requested: (" + prompt + ")")

        if prompt in self.prompt_dict:
            return_val = self.prompt_dict[current_prompt.prompt_name](prompt, *arg_list)
            if isinstance(return_val, tuple):
                error_string = return_val[1]
        else:
            return False, "Unrecognized prompt (" + self.device.oper_sys + "): " + prompt

        self.reset_agent_attrs(*orig_vals)

        return return_val, error_string

    def issue_prompt_change(self, cmd):
        """
        This method sends a command to change the prompt.

        Args:
        [cmd] - The command to be sent.
        """
        self.log_debug("Issuing prompt change")
        self.log_debug("    Command: " + cmd)

        output = self.device.current_agent.send_command_wait_for_prompt(cmd)

        self.log_debug("Prompt Change Output: ")
        self.log_debug(output)

        return_val = self.device.error_checker.check_for_errors(output)

        if return_val:
            self.log_debug("Error when changing prompt")
            return False
        return True

    def interface_has_changed(self, prompt_obj):
        """
        This method will attempt to determine if an interface prompt has changed. For example, when the
        PromptHandler gets a request to transition from interface prompt to interface prompt it can't
        make the assumption it's already at the interface prompt since there can be multiple interface
        prompts. This method attempts to determine is this a request to move from vlan.0.100 to vlan.0.100,
        or vlan.0.100 to vlan.0.200 - it does this by pulling the interface name from the prompt_obj arg
        (the prompt the user wants to go to) and looking through the prompt chain to see if there are any
        interface prompts currently in the chain. If so, it compares them to see if they match

        Args:
            prompt_obj:   A PromptObj instance
        """
        self.logger.log_debug("Checking to see if interface has changed...")

        for chain_prompt_obj in self.prompt_chain:
            if chain_prompt_obj.prompt_name == NetworkElementConstants.PROMPT_INTERFACE:
                if prompt_obj.interface_name == chain_prompt_obj.interface_name:
                    self.log_debug("   Interface has not changed")
                    return False
                else:
                    self.log_debug("   Interface has changed")
                    return True
        return False

    def router_proto_has_changed(self, prompt_obj):
        """
        This method will attempt to determine if a router proto prompt has changed. For example, when the
        PromptHandler gets a request to transition from router proto prompt to router proto prompt it can't
        make the assumption it's already at the router proto prompt since there can be multiple router proto
        prompts. This method attempts to determine is this a request to move from OSPF 1 to OSPF 1,
        or OSPF 1 to BGP 1 - it does this by pulling the interface name from the prompt_obj arg
        (the prompt the user wants to go to) and looking through the prompt chain to see if there are any
        router proto prompts currently in the chain. If so, it compares them to see if they match (based on proto,
        and instance)

        Args:
            prompt_obj:   A PromptObj instance
        """
        self.log_debug("Checking to see if router proto prompt has changed")

        for chain_prompt_obj in self.prompt_chain:
            if chain_prompt_obj.prompt_name == NetworkElementConstants.PROMPT_ROUTER_PROTO:
                if prompt_obj.router_proto == chain_prompt_obj.router_proto:
                    if prompt_obj.protocol_instance == chain_prompt_obj.protocol_instance:
                        self.log_debug("   Router proto has not changed")
                        return False
                    else:
                        self.log_debug("   Router proto has changed")
                        return True
                else:
                    self.log_debug("   Router proto has changed")
                    return True
        return False

    def role_has_changed(self, prompt_obj):
        """
        This method will attempt to determine if a role prompt has changed. For example, when the
        PromptHandler gets a request to transition from role prompt to role prompt it can't
        make the assumption it's already at the role prompt since there can be multiple role
        prompts. This method attempts to determine is this a request to move from role:Default to role:Default,
        or role:Default to role:Mgmt - it does this by pulling the interface name from the prompt_obj arg
        (the prompt the user wants to go to) and looking through the prompt chain to see if there are any
        role prompts currently in the chain. If so, it compares them to see if they match

        Args:
            prompt_obj:   A PromptObj instance
        """
        self.log_debug("Checking to see if role has changed...")

        for chain_prompt_obj in self.prompt_chain:
            if chain_prompt_obj.prompt_name == NetworkElementConstants.PROMPT_EXTR_WIRELESS_ROLE:
                if prompt_obj.role_name == chain_prompt_obj.role_name:
                    self.log_debug("   Role has not changed")
                    return False
                else:
                    self.log_debug("   Role has changed")
                    return True
        return False

    def log_debug(self, msg):
        """
        This function checks the debug flag, if it is enabled the passed <msg>
        will be written to the log.
        """
        if self.debug:
            self.logger.log_trace(msg)
