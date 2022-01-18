from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObject import CommandObject


class SnmpCommandObject(CommandObject):
    def __init__(self):
        super(SnmpCommandObject, self).__init__()

        self.data_type = None
        self.value = None
        self.return_text = None
        self.return_data = None
        self.return_error_indication = None
        self.return_error_status = None

        # Attributes with setter/getter methods.
        self._command_type = None
        self._oid = None

    @property
    def command_type(self):
        """
        Property function for command_type, returns the private attribute _command_type.
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        """
        Setter function for command_type. This function sets _command_type to the passed
        <command_type> and creates a command based on the command_type and oid (as long
        as they are both set).
        """
        self._command_type = command_type
        self.__set_command()

    @property
    def oid(self):
        """
        Property function for oid, returns the private attribute _oid.
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """
        Setter function for oid. This function sets _oid to the passed
        <oid> and creates a command based on the command_type and oid (as long
        as they are both set).
        """
        self._oid = oid
        self.__set_command()

    def __set_command(self):
        """
        This function returns a command string using the oid and request_type as long as neither is
        currently set ot None.

        For example:
        oid = 1.2.3.4.5.1.2321.1.421
        request_type = walk

        Return:
        walk 1.2.3.4.5.1.2321.1.421
        """
        if self.oid is not None and self.command_type is not None:
            if isinstance(self.command_type, str):
                self.command = self.command_type + " " + self.oid
