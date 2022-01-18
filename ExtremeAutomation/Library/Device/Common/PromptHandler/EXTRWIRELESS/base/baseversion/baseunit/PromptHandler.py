from ExtremeAutomation.Library.Device.Common.PromptHandler.PromptObj import PromptObj
from ExtremeAutomation.Library.Device.Common.PromptHandler.BasePromptHandler import BasePromptHandler


class PromptHandler(BasePromptHandler):
    def __init__(self, device):
        super(PromptHandler, self).__init__(device)

        # This is where the dictionary of supported prompts is stored.
        self.prompt_dict = {self.constants.PROMPT_USER: self.handle_user,
                            self.constants.PROMPT_EXTR_WIRELESS_TOPOLOGY: self.handle_topology,
                            self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE: self.handle_base_role,
                            self.constants.PROMPT_EXTR_WIRELESS_ROLE: self.handle_role,
                            self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER: self.handle_acl_filter}

    # +-------------------+
    # | Handler Functions |
    # +-------------------+
    def handle_user(self, prompt, *args):
        """
        This function handles all user to <prompt> prompt changes.
        """
        if prompt == self.constants.PROMPT_USER:
            return True
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE:
            return self.user_to_base_role()
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_ROLE:
            return self.user_to_role(*args)
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_TOPOLOGY:
            return self.user_to_topology()
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER:
            return self.user_to_acl_filter(*args)
        return False, prompt + " is not a valid prompt for " + self.device.oper_sys

    def handle_topology(self, prompt, *args):
        """
        This function handles all topology to <prompt> prompt changes.
        """
        if prompt == self.constants.PROMPT_EXTR_WIRELESS_TOPOLOGY:
            return True
        elif prompt == self.constants.PROMPT_USER:
            return self.topology_to_user()
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE:
            return self.topology_to_base_role()
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_ROLE:
            return self.topology_to_role(*args)
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER:
            return self.topology_to_acl_filter(*args)
        return False, prompt + " is not a valid prompt for " + self.device.oper_sys

    def handle_base_role(self, prompt, *args):
        """
        This function handles all base role to <prompt> prompt changes.
        """
        if prompt == self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE:
            return True
        elif prompt == self.constants.PROMPT_USER:
            return self.base_role_to_user()
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_ROLE:
            return self.base_role_to_role(*args)
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_TOPOLOGY:
            return self.base_role_to_topology()
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER:
            return self.base_role_to_acl_filter(*args)
        return False, prompt + " is not a valid prompt for " + self.device.oper_sys

    def handle_role(self, prompt, *args):
        """
        This function handles all role to <prompt> prompt changes.
        """
        if prompt == self.constants.PROMPT_USER:
            return self.role_to_user()
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE:
            return self.role_to_base_role()
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_TOPOLOGY:
            return self.role_to_topology()
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_ROLE:
            return self.role_to_role(*args)
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER:
            return self.role_to_acl_filter(*args)
        return False, prompt + " is not a valid prompt for " + self.device.oper_sys

    def handle_acl_filter(self, prompt, *args):
        """
        This function handles all acl filter to <prompt> prompt changes.
        """
        if prompt == self.constants.PROMPT_USER:
            return self.acl_filter_to_user()
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_TOPOLOGY:
            return self.acl_filter_to_topology()
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE:
            return self.acl_filter_to_base_role()
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_ROLE:
            return self.acl_filter_to_role(*args)
        elif prompt == self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER:
            return self.acl_filter_to_acl_filter(*args)
        return False, prompt + " is not a valid prompt for " + self.device.oper_sys

    # +-------------+
    # | User Prompt |
    # +-------------+
    def user_to_topology(self):
        """
        This function changes from the user prompt to the topology prompt.
        """
        if self.issue_prompt_change("topology"):
            self.prompt_chain.append(PromptObj(self.constants.PROMPT_EXTR_WIRELESS_TOPOLOGY))
            return True
        return False

    def user_to_base_role(self):
        """
        This function changes from the user prompt to the base role prompt.
        """
        if self.issue_prompt_change("role"):
            self.prompt_chain.append(PromptObj(self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE))
            return True
        return False

    def user_to_role(self, *args):
        """
        This function changes from the user prompt to a role prompt.
        """
        if self.user_to_base_role():
            if self.issue_prompt_change("role " + args[0]):
                self.prompt_chain.append(PromptObj(self.constants.PROMPT_EXTR_WIRELESS_ROLE, role_name=args[0]))
                return True
        return False

    def user_to_acl_filter(self, *args):
        """
        This function changes from the user prompt to an acl filter prompt.
        """
        if self.user_to_role(*args):
            if self.issue_prompt_change("acfilters"):
                self.prompt_chain.append(PromptObj(self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER))
                return True
        return False

    # +-----------------+
    # | Topology Prompt |
    # +-----------------+
    def topology_to_user(self):
        """
        This function changes from the topology prompt to the user prompt.
        """
        if self.issue_prompt_change("end"):
            self.prompt_chain = [PromptObj(self.constants.PROMPT_USER)]
            return True
        return False

    def topology_to_base_role(self):
        """
        This function changes from the topology prompt to the base role prompt.
        """
        if self.topology_to_user():
            if self.issue_prompt_change("role"):
                self.prompt_chain.append(PromptObj(self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE))
                return True
        return False

    def topology_to_role(self, *args):
        """
        This function changes from the topology prompt to a role prompt.
        """
        if self.topology_to_user():
            return self.user_to_role(*args)
        return False

    def topology_to_acl_filter(self, *args):
        """
        This function changes from the topology prompt to an acl filter prompt.
        """
        prompt_obj = PromptObj(self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER, role_name=args[0])
        if self.topology_to_role(*args):
            if self.issue_prompt_change("acfilters"):
                self.prompt_chain.append(prompt_obj)
                return True
        return False

    # +------------------+
    # | Base Role Prompt |
    # +------------------+
    def base_role_to_user(self):
        """
        This function changes from the base role prompt to the user prompt.
        """
        if self.issue_prompt_change("end"):
            self.prompt_chain = [PromptObj(self.constants.PROMPT_USER)]
            return True
        return False

    def base_role_to_topology(self):
        """
        This function changes from the base role prompt to the topology prompt.
        """
        if self.base_role_to_user():
            if self.user_to_topology():
                return True
        return False

    def base_role_to_role(self, *args):
        """
        This function changes from the base role prompt to a role prompt.
        """
        if self.issue_prompt_change("role " + args[0]):
            self.prompt_chain.append(PromptObj(self.constants.PROMPT_EXTR_WIRELESS_ROLE, role_name=args[0]))
            return True
        return False

    def base_role_to_acl_filter(self, *args):
        """
        This function changes from the base role prompt to an acl filter prompt.
        """
        if self.base_role_to_role(*args):
            if self.issue_prompt_change("acfilters"):
                self.prompt_chain.append(PromptObj(self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER))
                return True
        return False

    # +-------------+
    # | Role Prompt |
    # +-------------+
    def role_to_user(self):
        """
        This function changes from a role prompt to the user prompt.
        """
        if self.issue_prompt_change("end"):
            self.prompt_chain = [PromptObj(self.constants.PROMPT_USER)]
            return True
        return False

    def role_to_topology(self):
        """
        This function changes from a role prompt to the topology prompt.
        """
        if self.role_to_user():
            return self.user_to_topology()
        return False

    def role_to_base_role(self):
        """
        This function changes from a role prompt to the base role prompt.
        """
        if self.issue_prompt_change("exit"):
            self.prompt_chain.pop()
            return True
        return False

    def role_to_role(self, *args):
        """
        This function changes from a role prompt to another role prompt.
        """
        prompt_obj = PromptObj(self.constants.PROMPT_EXTR_WIRELESS_ROLE, role_name=args[0])

        if self.role_has_changed(prompt_obj):
            if self.role_to_base_role():
                if self.issue_prompt_change("role " + args[0]):
                    self.prompt_chain.append(prompt_obj)
                    return True
            return False
        return True

    def role_to_acl_filter(self, *args):
        """
        This function changes from a role prompt to an acl filter prompt.
        """
        prompt_obj = PromptObj(self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER)

        if self.role_has_changed(prompt_obj):
            if self.role_to_base_role():
                if self.base_role_to_role(*args):
                    if self.issue_prompt_change("acfilters"):
                        self.prompt_chain.append(prompt_obj)
                        return True
            return False
        else:
            if self.issue_prompt_change("acfilters"):
                self.prompt_chain.append(prompt_obj)
                return True
            return False

    # +--------------------+
    # | ACL Filters Prompt |
    # +--------------------+
    def acl_filter_to_user(self):
        """
        This function changes from an acl filter prompt to the user prompt.
        """
        if self.issue_prompt_change("end"):
            self.prompt_chain = [PromptObj(self.constants.PROMPT_USER)]
            return True
        return False

    def acl_filter_to_topology(self):
        """
        This function changes from an acl filter prompt to the topology prompt.
        """
        if self.acl_filter_to_user():
            return self.user_to_topology()
        return False

    def acl_filter_to_base_role(self):
        """
        This function changes from an acl filter prompt to the base role prompt.
        """
        if self.acl_filter_to_user():
            return self.user_to_base_role()
        return False

    def acl_filter_to_role(self, *args):
        """
        This function changes from an acl filter prompt to a role prompt.
        """
        if self.acl_filter_to_user():
            return self.user_to_role(*args)
        return False

    def acl_filter_to_acl_filter(self, *args):
        """
        This function changes from an acl filter prompt to another acl filter prompt.
        """
        prompt_obj = PromptObj(self.constants.PROMPT_EXTR_WIRELESS_ROLE, role_name=args[0])

        if self.role_has_changed(prompt_obj):
            if self.acl_filter_to_user():
                if self.user_to_role(*args):
                    return self.role_to_acl_filter(*args)
            return False
        return True
