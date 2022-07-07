from ExtremeAutomation.Library.Device.NetworkElement.ErrorChecker.BaseErrorChecker import BaseErrorChecker


class ErrorChecker(BaseErrorChecker):
    def init_gen_errors(self):
        """
        This function appends all errors that we want to check for in each output.
        """
        self.gen_errors.append('does not exist')
        self.gen_errors.append('Error')
        self.gen_errors.append('ERROR')
        self.gen_errors.append('Invalid IP')
        self.gen_errors.append("% Invalid input detected at '^' marker.")
        self.gen_errors.append('Command not found / Incomplete command. Use ? to list commands.')


    def init_protocol_specific_errors(self):
        """
        Here is where you can move generic errors to more specific categories if users decide they want to
        scope the error checking to, say, only check the vlan errors when running a vlan api
        self.protocol_specific_errors['protocol'] = ['error1', 'error2', etc]
        """
        pass

    def init_json_errors(self):
        """
        This function appends all errors that we want to check for in each output.
        """
        self.json_errors.append('error-message')
