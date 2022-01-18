from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.GIM.GimsponsorsConstants import GimsponsorsConstants


class UiGimSponsorsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiGimSponsorsKeywords, self).__init__()
        self.api_const = self.constants.API_GIM_SPONSORS
        self.command_const = GimsponsorsConstants()

    def gim_sponsor_details_add(self, element_name, sponsor_type, pre_def_email, option, fixed_fn, fixed_ln,
                                fixed_email, ldap_grp, sync_dur, ot_action, **kwargs):
        """
        Keyword Arguments:
        [element_name]  - The UI element(s) the keyword should be run against.
        [sponsor_type]  - Type of the sponsor
        [pre_def_email] - Email ID address for Predefined Sponsor
        [option] - Option to choose Sponsor Email Field
        [fixed_fn]      - Fist Name for fixed Sponsor
        [fixed_ln]      - Last Name for fixed Sponsor
        [fixed_email]   - Email ID for Fixed Sponsor
        [ldap_grp] - LDAP Group Information
        [sync_dur] - Sync Duration
        [ot_action] - Save or Cancel OT

        Adding domain to predefined, fixed and ldap sponsor
        """
        args = {"sponsor_type": sponsor_type,
                "pre_def_email": pre_def_email,
                "option": option,
                "fixed_fn": fixed_fn,
                "fixed_ln": fixed_ln,
                "fixed_email": fixed_email,
                "ldap_grp": ldap_grp,
                "sync_dur": sync_dur,
                "ot_action": ot_action
                }

        return self.execute_keyword(element_name, args, self.command_const.GIM_SPONSOR_DETAILS_ADD, **kwargs)
