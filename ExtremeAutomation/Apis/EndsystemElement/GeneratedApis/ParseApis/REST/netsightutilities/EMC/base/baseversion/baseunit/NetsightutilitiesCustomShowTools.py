from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.REST.netsightutilities.base.\
    NetsightutilitiesBaseCustomShowTools import NetsightutilitiesBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetsightutilitiesCustomShowTools(NetsightutilitiesBaseCustomShowTools):
    def __init__(self, device):
        super(NetsightutilitiesCustomShowTools, self).__init__(device)

    def verify_rest_read_all(self, output, args, **kwargs):
        for item in output:
            if args['rest_inspect_data'] == item:
                return True, True
        return False, False

    def verify_rest_read(self, output, args, **kwargs):
        if args['rest_inspect_data'] == output:
            return True, True
        else:
            return False, False
