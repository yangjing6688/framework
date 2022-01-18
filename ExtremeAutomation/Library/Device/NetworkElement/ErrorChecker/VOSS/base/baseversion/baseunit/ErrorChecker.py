from ExtremeAutomation.Library.Device.NetworkElement.ErrorChecker.BaseErrorChecker import BaseErrorChecker


class ErrorChecker(BaseErrorChecker):
    def init_gen_errors(self):
        """
        This function appends all errors that we want to check for in each output.
        """
        self.gen_errors.append('Error ')
        self.gen_errors.append('Command failed')
        self.gen_errors.append('changes first')
        self.gen_errors.append('not found')
        self.gen_errors.append('Could not')
        self.gen_errors.append('% Invalid')
        self.gen_errors.append('interface first')
        self.gen_errors.append('Bad access list number:')
        self.gen_errors.append('does not exist')
        self.gen_errors.append('contains no valid ports.')
        self.gen_errors.append('no entries found')
        self.gen_errors.append('Usage:')
        self.gen_errors.append('is not mapped')
        self.gen_errors.append('There are no')
        self.gen_errors.append('Error:')
        self.gen_errors.append('Unknown:')
        self.gen_errors.append('No Port')
        self.gen_errors.append('No Learning')
        self.gen_errors.append('No entries found')
        self.gen_errors.append('There is no server')
        self.gen_errors.append('Invalid')
        self.gen_errors.append('No such file')
        self.gen_errors.append('No Constraints')
        self.gen_errors.append('does not support')
        self.gen_errors.append('There are no licenses configured')
        self.gen_errors.append('No mirrors')
        self.gen_errors.append('mac to vlan association exists')
        self.gen_errors.append('Unable to convert')

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
        pass
