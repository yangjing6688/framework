from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.REST.demo.base.DemoBaseCustomShowTools import \
    DemoBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


class DemoCustomShowTools(DemoBaseCustomShowTools):
    def __init__(self, device):
        super(DemoCustomShowTools, self).__init__(device)

    def verify_guest_onboarding_template(self, output, args, **kwargs):
        found_template = None
        if output['GuestUser']:
            found_template = output['GuestUser']["onboardingTemplate"]
            if found_template == args['onboarding_template']:
                return True, {"ret_template": found_template}
        return False, {"ret_template": found_template}
