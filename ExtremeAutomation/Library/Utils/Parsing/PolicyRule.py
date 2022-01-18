"""
This Class is to create a policy rule object
"""
from ExtremeAutomation.Library.Logger.Logger import Logger


class PolicyRule(object):

    def __init__(self):
        self.logger = Logger()

        self.policy_id = None
        self.rule_type = None
        self.rule_data = None
        self.rule_data_hex = None
        self.mask = None
        self.port = None
        self.status = None
        self.storage_type = None
        self.vlan = None
        self.cos = None
        self.mirror = None
        self.quarantine_profile = None
        self.audit_syslog_status = None
        self.audit_trap_status = None
        self.disable_port_status = None
        self.replace_tci_status = None

    def is_this_the_correct_rule(self, policy_id, rule_type, rule_data):
        """
        This function return True if the given args match the current Profile Rule.
        """
        new_rule_data = rule_data.upper()
        if rule_type == "MAC source address" or rule_type == "MAC destination address":
            newest_rule_data = new_rule_data.replace(":", "-")
        else:
            newest_rule_data = new_rule_data
        self.logger.log_info(newest_rule_data)
        if self.policy_id == policy_id and self.rule_type == rule_type and self.rule_data == newest_rule_data:
            return True
        else:
            return False

    def display_session(self):
        """
        This function logs the current Policy Rule, in device-like output.
        """
        self.logger.log_info("{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}".format("Profile Index", ":", self.policy_id,
                                                                              "Rule Type", ":", self.rule_type))
        self.logger.log_info("{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}".format("Rule Data", ":", self.rule_data,
                                                                              "Rule Mask", ":", self.mask))
        self.logger.log_info("{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}".format("Rule Port", ":", self.port, "Status",
                                                                              ":", self.status))
        self.logger.log_info("{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}".format("Vlan", ":", self.vlan, "COS",
                                                                              ":", self.cos))
        self.logger.log_info("{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}".format("Mirror", ":", self.mirror,
                                                                              "Quarantine Profile", ":",
                                                                              self.quarantine_profile))
        self.logger.log_info("{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}".format("Audit Syslog Status", ":",
                                                                              self.audit_syslog_status,
                                                                              "Audit Trap Status", ":",
                                                                              self.audit_trap_status))
        self.logger.log_info("{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}".format("Disable Port Status ", ":",
                                                                              self.disable_port_status,
                                                                              "Replace TCI status", ":",
                                                                              self.replace_tci_status))

    def rule_data_dict(self):
        """Returns a dictionary of the PolicyRule attributes."""
        ret_dict = {"ret_rule_data": self.rule_data,
                    "ret_mask": self.mask,
                    "ret_port": self.port,
                    "ret_storage_type": self.storage_type,
                    "ret_vlan": self.vlan,
                    "ret_cos": self.cos,
                    "ret_mirror": self.mirror,
                    "ret_quarantine_profile": self.quarantine_profile,
                    "ret_syslog_status": self.audit_syslog_status,
                    "ret_trap_status": self.audit_trap_status,
                    "ret_disable_port_status": self.disable_port_status,
                    "ret_tci_overwrite": self.replace_tci_status}
        return ret_dict
