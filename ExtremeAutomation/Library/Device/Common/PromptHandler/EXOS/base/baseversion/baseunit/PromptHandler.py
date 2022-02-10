from ExtremeAutomation.Library.Device.Common.PromptHandler.PromptObj import PromptObj
from ExtremeAutomation.Library.Device.Common.PromptHandler.BasePromptHandler import BasePromptHandler


class PromptHandler(BasePromptHandler):
    def __init__(self, device):
        super(PromptHandler, self).__init__(device)

        # This is where the dictionary of supported prompts is stored.
        self.prompt_dict = {self.constants.PROMPT_USER: self.handle_user,
                            self.constants.PROMPT_EXOS_BACKUP: self.handle_backup,
                            self.constants.PROMPT_EXOS_PACMAN: self.handle_pacman,
                            self.constants.PROMPT_EXOS_BCMSHELL: self.handle_bcmshell,
                            self.constants.PROMPT_EXOS_SHELL: self.handle_shell}

    # +-------------------+
    # | Handler Functions |
    # +-------------------+
    def handle_user(self, prompt, *args):
        """
        This function handles all user to <prompt> prompt changes.
        """
        if prompt == self.constants.PROMPT_USER:
            if self.device.connection_method == 'console' or self.device.connection_method == 'slot1' or \
                    self.device.connection_method == 'slot2':
                if (self.device.connection_method == 'console' or self.device.connection_method == 'slot1') and \
                        self.device.primary_connection == 'slot2':
                    return self.user_to_backup()
                elif self.device.connection_method == 'slot2' and \
                        (self.device.primary_connection == 'slot1' or self.device.primary_connection == 'console'):
                    return self.user_to_backup()
                else:
                    return True
            else:
                return True
        elif prompt == self.constants.PROMPT_EXOS_BACKUP:
            return self.user_to_backup()
        elif prompt == self.constants.PROMPT_EXOS_PACMAN:
            return self.user_to_pacman()
        elif prompt == self.constants.PROMPT_EXOS_BCMSHELL:
            return self.user_to_bcmshell()
        elif prompt == self.constants.PROMPT_EXOS_SHELL:
            return self.user_to_shell()
        return False, prompt + " is not a valid prompt for " + self.device.oper_sys

    def handle_backup(self, prompt, *args):
        """
        This function handles all backup slot to <prompt> prompt changes.
        """
        if prompt == self.constants.PROMPT_EXOS_BACKUP:
            return True
        elif prompt == self.constants.PROMPT_USER:
            return self.backup_to_user()
        elif prompt == self.constants.PROMPT_EXOS_BCMSHELL:
            return self.backup_to_bcmshell()
        elif prompt == self.constants.PROMPT_EXOS_SHELL:
            return self.backup_to_shell()
        return False, prompt + " is not a valid prompt for " + self.device.oper_sys

    def handle_pacman(self, prompt, *args):
        """
        This function handles all base role to <prompt> prompt changes.
        """
        if prompt == self.constants.PROMPT_EXOS_PACMAN:
            return True
        elif prompt == self.constants.PROMPT_USER:
            return self.pacman_to_user()
        elif prompt == self.constants.PROMPT_EXOS_BACKUP:
            return self.pacman_to_backup()
        return False, prompt + " is not a valid prompt for " + self.device.oper_sys

    def handle_bcmshell(self, prompt, *args):
        """
        This function handles all base role to <prompt> prompt changes.
        """
        if prompt == self.constants.PROMPT_EXOS_BCMSHELL:
            return True
        elif prompt == self.constants.PROMPT_USER:
            return self.bcmshell_to_user()
        elif prompt == self.constants.PROMPT_EXOS_BACKUP:
            return self.bcmshell_to_backup()
        return False, prompt + " is not a valid prompt for " + self.device.oper_sys

    def handle_shell(self, prompt, *args):
        """
        This function handles all base role to <prompt> prompt changes.
        """
        if prompt == self.constants.PROMPT_EXOS_SHELL:
            return True
        elif prompt == self.constants.PROMPT_USER:
            return self.shell_to_user()
        elif prompt == self.constants.PROMPT_EXOS_BACKUP:
            return self.shell_to_backup()
        return False, prompt + " is not a valid prompt for " + self.device.oper_sys

    # +-------------+
    # | User Prompt |
    # +-------------+
    def user_to_backup(self):
        """
        This function backup prompt needs push
        """
        prompt_obj = PromptObj(self.constants.PROMPT_EXOS_BACKUP, backup="> ")
        self.prompt_chain.append(prompt_obj)
        return True

    def user_to_bcmshell(self):
        """
        This function changes from the user prompt to the base role prompt.
        """
        prompt_obj = PromptObj(self.constants.PROMPT_EXOS_BCMSHELL, bcm_shell=">")
        if self.issue_prompt_change("!sh"):
            self.prompt_chain.append(prompt_obj)
            return True
        return False

    def user_to_shell(self):
        """
        This function changes from the user prompt to a role prompt.
        """
        prompt_obj = PromptObj(self.constants.PROMPT_EXOS_SHELL, shell=">")
        if self.issue_prompt_change("!sh"):
            self.prompt_chain.append(prompt_obj)
            return True
        return False

    def user_to_pacman(self):
        """
        This function no supp.
        """
        return True

    # +-----------------+
    # | Backup Prompt |
    # +-----------------+
    def backup_to_user(self):
        """
        This function changes from backup > to user.
        """
        self.prompt_chain = [PromptObj(self.constants.PROMPT_USER)]
        return True


    def backup_to_bcmshell(self):
        """
        This function changes from the user prompt to the base role prompt.
        """
        prompt_obj = PromptObj(self.constants.PROMPT_EXOS_BCMSHELL, bcm_shell=">")
        if self.issue_prompt_change("!sh"):
            self.prompt_chain.append(prompt_obj)
            return True
        return False

    def backup_to_shell(self):
        """
        This function changes from the user prompt to a role prompt.
        """
        prompt_obj = PromptObj(self.constants.PROMPT_EXOS_SHELL, shell=">")
        if self.issue_prompt_change("!sh"):
            self.prompt_chain.append(prompt_obj)
            return True
        return False

    # +------------------+
    # | BCM Shell Prompt |
    # +------------------+
    def bcmshell_to_user(self):
        """
        This function changes from the base role prompt to the user prompt.
        """
        if self.issue_prompt_change("exit"):
            self.prompt_chain = [PromptObj(self.constants.PROMPT_USER)]
            return True
        return False

    def bcmshell_to_backup(self):
        """
        This function changes from the base role prompt to the topology prompt.
        """
        if self.issue_prompt_change("exit"):
            self.prompt_chain = [PromptObj(self.constants.PROMPT_USER)]
            return True
        return False


    # +-------------+
    # | Shell Prompt |
    # +-------------+
    def shell_to_user(self):
        """
        This function changes from a exit debug shell prompt to the user prompt.
        """
        if self.issue_prompt_change("exit"):
            self.prompt_chain = [PromptObj(self.constants.PROMPT_USER)]
            return True
        return False

    def shell_to_backup(self):
        """
        This function changes from an exos shell prompt to the backup prompt.
        """
        if self.issue_prompt_change("exit"):
            self.prompt_chain = [PromptObj(self.constants.PROMPT_USER)]
            return True
        return False

    # +--------------------+
    # | PACMAN      Prompt |
    # +--------------------+
    def pacman_to_user(self):
        """
        This function changes from an acl filter prompt to the user prompt.
        """
        if self.issue_prompt_change("c"):
            self.prompt_chain = [PromptObj(self.constants.PROMPT_USER)]
            return True
        return False

    def pacman_to_backup(self):
        """
        This function changes from an acl filter prompt to the topology prompt.
        """
        if self.issue_prompt_change("c"):
            self.prompt_chain = [PromptObj(self.constants.PROMPT_USER)]
            return True
        return False
