from ExtremeAutomation.Library.Device.Common.CommandObjects.CommandObject import CommandObject


class UiCommandObject(CommandObject):
    def __init__(self):
        super(UiCommandObject, self).__init__()

        self.action = None
        self.args = None

    @property
    def return_data(self):
        """
        Property function for return_data, this function returns return_text.
        """
        return self.return_text

    @return_data.setter
    def return_data(self, return_data):
        """
        Setter function for return_data, this function sets return_text to <return_data>.
        """
        self.return_text = return_data
