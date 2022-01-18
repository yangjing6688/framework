class CommandObject(object):
    def __init__(self):
        self.error_state = False
        self.error_text = None
        self.test_result = False
        self.not_supported = False
        self.start_time = None
        self.end_time = None
        self.uuid = None

        # Attributes with setter/getter
        self._command = None
        self._return_text = ""

    @property
    def command(self):
        """
        Property function for command, this function returns the private attribute _command.
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Setter function for command, this function sets _command to the passed <command>.
        """
        self._command = command

    @property
    def return_text(self):
        """
        Property function for return_text, this function returns the private attribute _return_text.
        """
        return self._return_text

    @return_text.setter
    def return_text(self, return_text):
        """
        Setter function for return_text, this function sets _return_text to the passed <return_text>.
        """
        self._return_text = return_text

    def set_error_state(self, error_text):
        """
        This enables the error_state and sets error_text ot the passed <error_text>.
        """
        self.error_state = True
        self.error_text = error_text

    def clear_error_state(self):
        """
        This function sets error state to False and sets the error text to None.
        """
        self.error_state = False
        self.error_text = None
