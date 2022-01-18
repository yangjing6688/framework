class PolicyAdminProfile(object):
    def __init__(self):
        self.profile_index = None
        self.rule_type = None
        self.rule_data = None
        self.mask = None
        self.port = None
        self.status = None
        self.storage_type = None
        self.oper_pid = None
        self.admin_pid = None

    def rule_data_dict(self):
        """Returns a dictionary of the PolicyAdminProfile attributes."""
        ret_dict = {"ret_rule_data": self.rule_data,
                    "ret_mask": self.mask,
                    "ret_port": self.port,
                    "ret_storage_type": self.storage_type,
                    "ret_oper_pid": self.oper_pid,
                    "ret_admin_pid": self.admin_pid}
        return ret_dict
