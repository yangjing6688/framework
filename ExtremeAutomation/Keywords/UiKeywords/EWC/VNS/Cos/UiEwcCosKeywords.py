from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EWC.EwccosConstants import EwccosConstants


class UiEwcCosKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEwcCosKeywords, self).__init__()
        self.api_const = self.constants.API_EWC_COS
        self.command_const = EwccosConstants()

    def cos_create_cos_profile(self, element_name, cos_profile, priority_override, priority, irl, orl, txq, tos,
                               tos_mask=None, **kwargs):
        """Returns the result of cos_create_cos_profile."""
        args = {"cos_profile": cos_profile,
                "priority_override": priority_override,
                "priority": priority,
                "irl": irl,
                "orl": orl,
                "txq": txq,
                "tos": tos,
                "tos_mask": tos_mask}

        return self.execute_keyword(element_name, args, self.command_const.COS_CREATE_COS_PROFILE, **kwargs)

    def cos_delete_cos_profile(self, element_name, cos_profile, **kwargs):
        """Returns the result of cos_delete_cos_profile."""
        args = {"cos_profile": cos_profile}

        return self.execute_keyword(element_name, args, self.command_const.COS_DELETE_COS_PROFILE, **kwargs)

    def cos_edit_cos_profile_priority_override_from_wlan(self, element_name, cos_profile, priority_override, **kwargs):
        """Returns the result of cos_edit_cos_profile_priority_override_from_wlan."""
        args = {"cos_profile": cos_profile,
                "priority_override": priority_override}

        return self.execute_keyword(element_name, args,
                                    self.command_const.COS_EDIT_COS_PROFILE_PRIORITY_OVERRIDE_FROM_WLAN, **kwargs)

    def cos_edit_cos_profile_priority(self, element_name, cos_profile, priority, **kwargs):
        """Returns the result of cos_edit_cos_profile_priority."""
        args = {"cos_profile": cos_profile,
                "priority": priority}

        return self.execute_keyword(element_name, args, self.command_const.COS_EDIT_COS_PROFILE_PRIORITY, **kwargs)

    def cos_edit_cos_profile_tos(self, element_name, cos_profile, tos, tos_mask=None, **kwargs):
        """Returns the result of cos_edit_cos_profile_tos."""
        args = {"cos_profile": cos_profile,
                "tos": tos,
                "tos_mask": tos_mask}

        return self.execute_keyword(element_name, args, self.command_const.COS_EDIT_COS_PROFILE_TOS, **kwargs)

    def cos_edit_cos_profile_txq(self, element_name, cos_profile, txq, **kwargs):
        """Returns the result of cos_edit_cos_profile_txq."""
        args = {"cos_profile": cos_profile,
                "txq": txq}

        return self.execute_keyword(element_name, args, self.command_const.COS_EDIT_COS_PROFILE_TXQ, **kwargs)

    def cos_create_cos_irl(self, element_name, cos_profile, irl_name, rate, **kwargs):
        """Returns the result of cos_create_cos_irl."""
        args = {"cos_profile": cos_profile,
                "irl_name": irl_name,
                "rate": rate}

        return self.execute_keyword(element_name, args, self.command_const.COS_CREATE_COS_IRL, **kwargs)

    def cos_edit_cos_irl(self, element_name, cos_profile, irl_name, rate, **kwargs):
        """Returns the result of cos_edit_cos_irl."""
        args = {"cos_profile": cos_profile,
                "irl_name": irl_name,
                "rate": rate}

        return self.execute_keyword(element_name, args, self.command_const.COS_EDIT_COS_IRL, **kwargs)

    def cos_create_cos_orl(self, element_name, cos_profile, orl_name, rate, **kwargs):
        """Returns the result of cos_create_cos_orl."""
        args = {"cos_profile": cos_profile,
                "orl_name": orl_name,
                "rate": rate}

        return self.execute_keyword(element_name, args, self.command_const.COS_CREATE_COS_ORL, **kwargs)

    def cos_edit_cos_orl(self, element_name, cos_profile, orl_name, rate, **kwargs):
        """Returns the result of cos_edit_cos_orl."""
        args = {"cos_profile": cos_profile,
                "orl_name": orl_name,
                "rate": rate}

        return self.execute_keyword(element_name, args, self.command_const.COS_EDIT_COS_ORL, **kwargs)

    def cos_edit_cos_profile_irl(self, element_name, cos_profile, irl_name, **kwargs):
        """Returns the result of cos_edit_cos_profile_irl."""
        args = {"cos_profile": cos_profile,
                "irl_name": irl_name}

        return self.execute_keyword(element_name, args, self.command_const.COS_EDIT_COS_PROFILE_IRL, **kwargs)

    def cos_edit_cos_profile_orl(self, element_name, cos_profile, orl_name, **kwargs):
        """Returns the result of cos_edit_cos_profile_orl."""
        args = {"cos_profile": cos_profile,
                "orl_name": orl_name}

        return self.execute_keyword(element_name, args, self.command_const.COS_EDIT_COS_PROFILE_ORL, **kwargs)

    def cos_cos_profile_priority_override_should_be_enabled(self, element_name, cos_profile, **kwargs):
        """Returns the result of cos_cos_profile_priority_override_should_be_enabled."""
        args = {"cos_profile": cos_profile}

        return self.execute_keyword(element_name, args,
                                    self.command_const.COS_PROFILE_PRIORITY_OVERRIDE_SHOULD_BE_ENABLED, **kwargs)

    def cos_verify_cos_profile_priority(self, element_name, cos_profile, priority, **kwargs):
        """Returns the result of cos_verify_cos_profile_priority."""
        args = {"cos_profile": cos_profile,
                "priority": priority}

        return self.execute_keyword(element_name, args, self.command_const.COS_VERIFY_COS_PROFILE_PRIORITY, **kwargs)

    def cos_verify_cos_profile_tos(self, element_name, cos_profile, tos, tos_mask=None, **kwargs):
        """Returns the result of cos_verify_cos_profile_tos."""
        args = {"cos_profile": cos_profile,
                "tos": tos,
                "tos_mask": tos_mask}

        return self.execute_keyword(element_name, args, self.command_const.COS_VERIFY_COS_PROFILE_TOS, **kwargs)

    def cos_verify_cos_profile_irl(self, element_name, cos_profile, irl_name, **kwargs):
        """Returns the result of cos_verify_cos_profile_irl."""
        args = {"cos_profile": cos_profile,
                "irl_name": irl_name}

        return self.execute_keyword(element_name, args, self.command_const.COS_VERIFY_COS_PROFILE_IRL, **kwargs)

    def cos_verify_cos_profile_orl(self, element_name, cos_profile, orl_name, **kwargs):
        """Returns the result of cos_verify_cos_profile_orl."""
        args = {"cos_profile": cos_profile,
                "orl_name": orl_name}

        return self.execute_keyword(element_name, args, self.command_const.COS_VERIFY_COS_PROFILE_ORL, **kwargs)

    def cos_verify_cos_profile_txq(self, element_name, cos_profile, txq, **kwargs):
        """Returns the result of cos_verify_cos_profile_txq."""
        args = {"cos_profile": cos_profile,
                "txq": txq}

        return self.execute_keyword(element_name, args, self.command_const.COS_VERIFY_COS_PROFILE_TXQ, **kwargs)

    def cos_click_save_button(self, element_name, **kwargs):
        """Returns the result of cos_click_save_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.COS_CLICK_SAVE_BUTTON, **kwargs)
