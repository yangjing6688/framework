from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObject import CommandObject


class CliCommandObject(CommandObject):
    def __init__(self):
        super(CliCommandObject, self).__init__()

        self.confirmation_args = None
        self.confirmation_phrases = None
        self.prompt = None
        self.prompt_args = None

    @property
    def return_text(self):
        """
        Property function for return_text. This function checks if _return_text is a basestring
        if it is it replaces \n\r with \r\n, otherwise it returns the _return_text unmodified.
        """
        if isinstance(self._return_text, str):
            return self._return_text.replace("\n\r", "\r\n")
        return self._return_text

    @return_text.setter
    def return_text(self, return_text):
        """
        Setter function for return_text, this function sets _return_text to the provided <return_text>.
        """
        self._return_text = return_text

    @property
    def command(self):
        """
        Property function for command, this function returns the private attribute _command.
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Setter function for command, this function sets _command to the passed <command> it also
        sets the start an end time if the command object's not supported flag is enabled.
        """
        self._command = command
        if self.not_supported:
            self.start_time = 0
            self.end_time = 0
