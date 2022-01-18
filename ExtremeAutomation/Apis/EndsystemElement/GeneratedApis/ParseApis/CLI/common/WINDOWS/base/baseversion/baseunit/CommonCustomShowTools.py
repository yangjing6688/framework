from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.CLI.common.base.CommonBaseCustomShowTools import \
    CommonBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class CommonCustomShowTools(CommonBaseCustomShowTools):
    def __init__(self, device):
        CommonBaseCustomShowTools.__init__(self, device)

    def check_file_exists(self, output, arg_dict):
        for line in output.splitlines():
            if arg_dict["file_name"] == self.pw.get_value_by_offset(line, "", 4):
                return True, {"ret_file": self.pw.get_value_by_offset(line, "", 4)}
        return False, {"ret_file": None}
