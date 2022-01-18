"""
# This Class is to create a policy profile object.
"""
from ExtremeAutomation.Library.Logger.Logger import Logger


class PolicyProfile(object):
    def __init__(self):
        self.logger = Logger()

        self.profile_id = None
        self.profile_name = None
        self.row_status = None
        self.port_vid_status = None
        self.port_vid_override = None
        self.cos_status = None
        self.cos = None
        self.mirror = None
        self.fst_class_index = None
        self.web_redirect_index = None
        self.syslog_on_use = None
        self.trap_on_use = None
        self.disable_ingress_port = None
        self.replace_tci_status = None
        self.rule_precedence = None
        self.admin_profile_usage = None
        self.oper_profile_usage = None
        self.dynamic_profile_usage = None

        # Attributes with setter methods.
        self._tagged_egress = None
        self._untagged_egress = None
        self._forbidden_egress = None

    @property
    def tagged_egress(self):
        """
        This function returns the status of _tagged_egress.
        """
        return self._tagged_egress

    @tagged_egress.setter
    def tagged_egress(self, vlans):
        if vlans is not None:
            self._tagged_egress = vlans.split(",")
        else:
            self._tagged_egress = None

    @property
    def untagged_egress(self):
        """
        This function returns the status of _untagged_egress.
        """
        return self._untagged_egress

    @untagged_egress.setter
    def untagged_egress(self, vlans):
        if vlans is not None:
            self._untagged_egress = vlans.split(",")
        else:
            self._untagged_egress = None

    @property
    def forbidden_egress(self):
        """
        This function returns the status of _forbidden_egress.
        """
        return self._forbidden_egress

    @forbidden_egress.setter
    def forbidden_egress(self, vlans):
        if vlans is not None:
            self._forbidden_egress = vlans.split(",")
        else:
            self._forbidden_egress = None

    def display_session(self):
        """
        This function logs the current Policy Profile, in device-like output.
        """
        self.logger.log_info('{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}'.format('Profile Index', ':',
                                                                              self.profile_id, 'Profile Name', ':',
                             self.profile_name))
        self.logger.log_info('{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}'.format('Row Status', ':', self.row_status,
                                                                              'Port VID status', ':',
                                                                              self.port_vid_status))
        self.logger.log_info('{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}'.format('Port VID override', ':',
                                                                              self.port_vid_override, 'COS status', ':',
                                                                              self.cos_status))
        self.logger.log_info('{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}'.format('COS', ':', self.cos,
                                                                              'Mirror', ':', self.mirror))
        self.logger.log_info('{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}'.format('FST Class Index', ':',
                                                                              self.fst_class_index,
                                                                              'Web Redirect Index', ':',
                                                                              self.web_redirect_index))
        self.logger.log_info('{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}'.format('Syslog On Use', ':', self.syslog_on_use,
                                                                              'Trap On Use', ':', self.trap_on_use))
        self.logger.log_info('{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}'.format('Disable Ingress Port', ':',
                                                                              self.disable_ingress_port,
                                                                              'Replace TCI Status', ':',
                                                                              self.replace_tci_status))
        self.logger.log_info('{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}'.format('Tagged Egress ', ':', self.tagged_egress,
                                                                              'Untagged Egress', ':',
                                                                              self.untagged_egress))
        self.logger.log_info('{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}'.format('Forbidden Egress ', ':',
                                                                              self.forbidden_egress, 'Rule Precedence',
                                                                              ':', self.rule_precedence))
        self.logger.log_info('{:<18} {:<1} {:<16} {:<22} {:<1} {:<18}'.format('Admin Profile Usage ', ':',
                                                                              self.admin_profile_usage,
                                                                              'Oper Profile Usage', ':',
                                                                              self.oper_profile_usage))
        self.logger.log_info('{:<18} {:<1} {:<16}'.format('Dyanmic Profile Usage ', ':', self.dynamic_profile_usage))
        self.logger.log_info('----------------------------------------------------------------------------')

    def is_this_the_correct_profile(self, profile_id_or_profile_name):
        """
        This function return True if the given arg is the current Profile's ID or name.
        """
        if self.profile_id == profile_id_or_profile_name or self.profile_name == profile_id_or_profile_name:
            return True
        else:
            return False
