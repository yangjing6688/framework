class PromptObj(object):
    def __init__(self, prompt, **kwargs):
        self.prompt_name = prompt
        self.interface_name = kwargs.get("interface_name", PromptConstants.DEFAULT_VALUE)
        self.protocol_instance = kwargs.get("protocol_instance", 0)
        self.router_proto = kwargs.get("router_proto", PromptConstants.DEFAULT_VALUE)
        self.probe_name = kwargs.get("probe_name", PromptConstants.DEFAULT_VALUE)
        self.probe_type = kwargs.get("probe_type", PromptConstants.DEFAULT_VALUE)
        self.probe_timing = kwargs.get("probe_timing", False)
        self.role_name = kwargs.get("role_name", PromptConstants.DEFAULT_VALUE)
        self.acl_filter_name = kwargs.get("aclfilter_name", PromptConstants.DEFAULT_VALUE)


class PromptConstants(object):
    DEFAULT_VALUE = "default"
