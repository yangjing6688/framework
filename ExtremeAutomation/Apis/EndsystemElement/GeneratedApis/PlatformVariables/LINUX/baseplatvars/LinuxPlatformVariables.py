from ExtremeAutomation.Library.Utils.DotDict import DotDict
from ExtremeAutomation.Library.Device.Common.PlatformVariables.Library.BasePlatformVariables \
    import BasePlatformVariables


def create_instance():
    return LinuxPlatformVariables()


class LinuxPlatformVariables(BasePlatformVariables):
    def __init__(self):
        super(LinuxPlatformVariables, self).__init__()

        # placeholder Platform Variables
        self.vars["placeholder"] = DotDict()
        self.vars["placeholder"]["placeholder_var_1"] = "var_1"
        self.vars["placeholder"]["placeholder_var_2"] = "var_2"
        self.vars["placeholder"]["placeholder_var_3"] = "var_3"
