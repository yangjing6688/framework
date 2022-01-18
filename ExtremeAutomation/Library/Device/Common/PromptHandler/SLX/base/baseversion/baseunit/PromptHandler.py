from ExtremeAutomation.Library.Device.Common.PromptHandler.PromptObj import PromptObj
from ExtremeAutomation.Library.Device.Common.PromptHandler.BasePromptHandler import BasePromptHandler


class PromptHandler(BasePromptHandler):
    def __init__(self, device):
        super(PromptHandler, self).__init__(device)

        # This is where the dictionary of supported prompts is stored.
        self.prompt_dict = {self.constants.PROMPT_USER: self.handle_user,
                            self.constants.PROMPT_ROUTER_CONFIG: self.handle_router_config,
                            self.constants.PROMPT_INTERFACE: self.handle_interface,
                            self.constants.PROMPT_ROUTER_PROTO: self.handle_router_proto}

    # +-------------------+
    # | Handler Functions |
    # +-------------------+
    def handle_user(self, prompt, *args):
        """
        This function handles all user to <prompt> prompt changes.
        """
        if prompt == self.constants.PROMPT_USER:
            return True
        elif prompt == self.constants.PROMPT_ROUTER_CONFIG:
            return self.user_to_config()
        elif prompt == self.constants.PROMPT_INTERFACE:
            return self.user_to_interface(*args)
        elif prompt is self.constants.PROMPT_ROUTER_PROTO:
            return self.user_to_router_proto(*args)
        return False, prompt + " is not a valid prompt for " + self.device.oper_sys

    def handle_router_config(self, prompt, *args):
        """
        This function handles all router to <prompt> prompt changes.
        """
        if prompt == self.constants.PROMPT_ROUTER_CONFIG:
            return True
        elif prompt == self.constants.PROMPT_USER:
            return self.config_to_user()
        elif prompt == self.constants.PROMPT_INTERFACE:
            return self.config_to_interface(*args)
        elif prompt == self.constants.PROMPT_ROUTER_PROTO:
            return self.config_to_router_proto(*args)
        return False, prompt + " is not a valid prompt for " + self.device.oper_sys

    def handle_interface(self, prompt, *args):
        """
        This function handles all interface to <prompt> prompt changes.
        """
        if prompt == self.constants.PROMPT_USER:
            return self.interface_to_user()
        elif prompt == self.constants.PROMPT_ROUTER_CONFIG:
            return self.interface_to_config()
        elif prompt == self.constants.PROMPT_INTERFACE:
            return self.interface_to_interface(*args)
        elif prompt == self.constants.PROMPT_ROUTER_PROTO:
            return self.interface_to_router_proto(*args)
        return False, prompt + " is not a valid prompt for " + self.device.oper_sys

    def handle_router_proto(self, prompt, *args):
        """
        This function handles all router proto to <prompt> prompt changes.
        """
        if prompt == self.constants.PROMPT_USER:
            return self.router_proto_to_user()
        elif prompt == self.constants.PROMPT_ROUTER_CONFIG:
            return self.router_proto_to_config()
        elif prompt == self.constants.PROMPT_INTERFACE:
            return self.router_proto_to_interface(*args)
        elif prompt == self.constants.PROMPT_ROUTER_PROTO:
            return self.router_proto_to_router_proto(*args)
        return False, prompt + " is not a valid prompt for " + self.device.oper_sys

    # +-------------+
    # | User Prompt |
    # +-------------+
    def user_to_config(self):
        """
        This function changes from the user prompt to the config prompt.
        """
        if self.issue_prompt_change("config t"):
            self.prompt_chain.append(PromptObj(self.constants.PROMPT_ROUTER_CONFIG))
            return True
        return False

    def user_to_interface(self, *args):
        """
        This function changes from the user prompt to an interface prompt.
        """
        if self.user_to_config():
            if self.issue_prompt_change("interface " + args[0]):
                self.prompt_chain.append(PromptObj(self.constants.PROMPT_INTERFACE, interface_name=args[0]))
                return True
        return False

    def user_to_router_proto(self, *args):
        """
        This function changes from the user prompt to a router protocol prompt.
        """
        if self.user_to_config():
            if self.issue_prompt_change("router " + " ".join(args)):
                self.prompt_chain.append(PromptObj(self.constants.PROMPT_ROUTER_PROTO, router_proto=args[0],
                                                   protocol_instance=args[1]))
                return True
        return False

    # +---------------+
    # | Config Prompt |
    # +---------------+
    def config_to_user(self):
        """
        This function changes from the config prompt to the user prompt.
        """
        if self.issue_prompt_change("exit"):
            self.prompt_chain.pop()
            return True
        return False

    def config_to_interface(self, *args):
        """
        This function changes from the config prompt to the an interface prompt.
        """
        if self.issue_prompt_change("interface " + args[0]):
            self.prompt_chain.append(PromptObj(self.constants.PROMPT_INTERFACE, interface_name=args[0]))
            return True
        return False

    def config_to_router_proto(self, *args):
        """
        This function changes from the config prompt to a router protocol prompt.
        """
        if self.issue_prompt_change("router " + " ".join(args)):
            self.prompt_chain.append(PromptObj(self.constants.PROMPT_ROUTER_PROTO, router_proto=args[0],
                                               protocol_instance=args[1]))
            return True
        return False

    # +------------------+
    # | Interface Prompt |
    # +------------------+
    def interface_to_user(self):
        """
        This function changes from an interface prompt to the user prompt.
        """
        if self.interface_to_config():
            return self.config_to_user()
        return False

    def interface_to_config(self):
        """
        This function changes from an interface prompt to the config prompt.
        """
        if self.issue_prompt_change("exit"):
            self.prompt_chain.pop()
            return True
        return False

    def interface_to_interface(self, *args):
        """
        This function changes from an interface prompt to another interface prompt.
        """
        prompt_obj = PromptObj(self.constants.PROMPT_INTERFACE, interface_name=args[0])

        if self.interface_has_changed(prompt_obj):
            if self.interface_to_config():
                if self.issue_prompt_change("interface " + args[0]):
                    self.prompt_chain.append(prompt_obj)
                    return True
            return False
        return True

    def interface_to_router_proto(self, *args):
        """
        This function changes from an interface prompt to a router protocol prompt.
        """
        prompt_obj = PromptObj(self.constants.PROMPT_ROUTER_PROTO, router_proto=args[0], protocol_instance=args[1])

        if self.interface_to_config():
            if self.issue_prompt_change("router " + " ".join(args)):
                self.prompt_chain.append(prompt_obj)
                return True
        return False

    # +-----------------+
    # | Router Protocol |
    # +-----------------+
    def router_proto_to_user(self):
        """
        This function changes from a router protocol prompt to the user prompt.
        """
        if self.router_proto_to_config():
            return self.config_to_user()
        return False

    def router_proto_to_config(self):
        """
        This function changes from a router protocol prompt to the config prompt.
        """
        if self.issue_prompt_change("exit"):
            self.prompt_chain.pop()
            return True
        return False

    def router_proto_to_interface(self, *args):
        """
        This function changes from a router protocol prompt to an interface prompt.
        """
        if self.router_proto_to_config():
            return self.config_to_interface(*args)
        return False

    def router_proto_to_router_proto(self, *args):
        """
        This function changes from a router protocol prompt to another router protocol prompt.
        """
        prompt_obj = PromptObj(self.constants.PROMPT_ROUTER_PROTO, router_proto=args[0], protocol_instance=args[1])

        if self.router_proto_has_changed(prompt_obj):
            if self.router_proto_to_config():
                return self.config_to_router_proto(*args)
            return False
        return True
