from ExtremeAutomation.Library.Device.EndsystemElement.ErrorChecker.BaseErrorChecker import BaseErrorChecker


class ErrorChecker(BaseErrorChecker):
    def init_gen_errors(self):
        """
        This function appends all errors that we want to check for in each output.
        """
        self.gen_errors.append('does not exist')
        self.gen_errors.append('Error')
        self.gen_errors.append('Invalid IP')
        self.gen_errors.append(' is not recognized as an internal or external command')

    def init_protocol_specific_errors(self):
        """
        Here is where you can move generic errors to more specific categories if users decide they want to
        scope the error checking to, say, only check the vlan errors when running a vlan api
        self.protocol_specific_errors['protocol'] = ['error1', 'error2', etc]
        """
        self.protocol_specific_errors['vlan'] = []

    def init_json_errors(self):
        """
        This function appends all errors that we want to check for in each output.
        """
        pass