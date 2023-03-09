from time import sleep

from extauto.common.AutoActions import AutoActions
from extauto.common.Utils import Utils
from extauto.xiq.elements.ExpSettingsWebElements import ExpSettingsWebElements


class ExpirationSettings(ExpSettingsWebElements):
    def __init__(self):
        super().__init__()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def _config_valid_during_dates(self, **config):
        pass

    def _config_valid_for_time_period(self, **config):
        """
        - config valid for time period expiration settings

        :param config:
        :return:
        """
        in_ = config.get('in')
        in_period = config.get('in_period')
        after = config.get('after')
        renew_user_cred = config.get('renew_user_cred')
        delete_cred_after = config.get('delete_cred_after')
        delete_cred_after_time = config.get('delete_cred_after_time')
        delete_cred_imm_after_exp = config.get('delete_cred_imm_after_exp')
        after_period = config.get('after_period')
        access_key_must_be_used_within = config.get("access_key_must_be_used_within")
        access_key_must_be_used_within_period = config.get("access_key_must_be_used_within_period")

        self.utils.print_info("Enter the in period")
        self.auto_actions.send_keys(self.get_valid_for_time_period_in(), in_)

        self.auto_actions.scroll_down()
        self.utils.print_info("click on time period drop down")
        self.auto_actions.click_reference(self.get_valid_for_time_period_in_drop_down)
        sleep(2)

        self.utils.print_info("select in time period option")
        self.auto_actions.select_drop_down_options(self.get_valid_for_time_period_in_drop_down_options(), in_period)
        sleep(2)

        self.utils.print_info("click on after time period drop down")
        self.auto_actions.click_reference(self.get_valid_for_time_period_after_drop_down)
        sleep(2)

        self.utils.print_info("select after time period option")
        self.auto_actions.select_drop_down_options(self.get_valid_for_time_period_after_drop_down_options(), after)
        if after == "First Login":
            self.utils.print_info(f"Enter the access key must be used within {access_key_must_be_used_within}")
            self.auto_actions.send_keys(self.get_access_key_must_be_used_within(), access_key_must_be_used_within)

            self.utils.print_info("click on the access key must be used withing drop down")
            self.auto_actions.click_reference(self.get_access_key_must_be_used_within_period_drop_down)
            sleep(2)

            self.auto_actions.select_drop_down_options(self.get_access_key_must_be_used_within_period_optns(),
                                                       access_key_must_be_used_within_period)

        if renew_user_cred == 'Enable':
            self.utils.print_info("select the renew user credential check box")
            self.auto_actions.enable_check_box(self.get_renew_user_credentials_check_box())
        else:
            self.auto_actions.disable_check_box(self.get_renew_user_credentials_check_box())

        if delete_cred_after == 'Enable':
            self.utils.print_info("select Delete credentials after check box")
            self.auto_actions.enable_check_box(self.get_delete_cred_after_check_box())

            self.utils.print_info(f"Enter Delete Cred After Time:{delete_cred_after_time}")
            self.auto_actions.send_keys(self.get_delete_cred_after_input_field(), delete_cred_after_time)

            self.utils.print_info("Select the delete after drop down")
            self.auto_actions.click_reference(self.get_delete_cred_after_drop_down)
            sleep(2)

            self.utils.print_info(f"select delete after time period in :{after_period}")
            self.auto_actions.select_drop_down_options(self.get_delete_cred_after_drop_down_options(), after_period)

        else:
            self.auto_actions.disable_check_box(self.get_delete_cred_after_check_box())

        if delete_cred_imm_after_exp == "Enable":
            self.auto_actions.enable_check_box(self.get_dlt_cred_imm_aft_expiration_check_box())

    def _config_daily(self, **config):
        pass

    def config_expiration_settings(self, **config):
        """
        - Config the account expiration settings based on the passed config dict
        - For different combination of config parameters creation refer private_pre-shared_key_config.robot
        - Assumes that user already navigated to User group edit page or called along with user group creation
        - Keyword Usage
        - ``Config Expiration Settings   &{EXPIRATION_CONFIG}``

        :param config: configuration dict
        :return: 1 if successfully configured
        """
        account_expiration = config.get('account_expiration')
        action_at_expiration = config.get("action_at_expiration")
        db_loc = config.get('db_loc')
        req_auth_after = config.get('req_auth_after')
        req_auth_after_time = config.get('req_auth_after_time')

        if db_loc == "Local":
            if req_auth_after == "Enable":
                self.utils.print_info("selecting Require auth after check box")
                self.auto_actions.enable_check_box(self.get_req_auth_after_check_box())

                self.utils.print_info(f"Enter Require authentication after:{req_auth_after_time}")
                self.auto_actions.send_keys(self.get_req_auth_after_input_field(), req_auth_after_time)

        self.utils.print_info("Click on account expiration drop down")
        self.auto_actions.click_reference(self.get_account_expiration_drop_down)
        sleep(2)

        self.utils.print_info("select the account expiration option")
        self.auto_actions.select_drop_down_options(self.get_account_expiration_drop_down_options(), account_expiration)

        if account_expiration == "Never Expire":
            return 1

        elif account_expiration == "Valid During Dates":
            pass

        elif account_expiration == "Valid For Time Period" or account_expiration == "Gültig für den Zeitraum":
            self._config_valid_for_time_period(**config)

        elif account_expiration == "Daily":
            pass

        if action_at_expiration == "Show Expiration Message":
            self.utils.print_info(f"select Action at Expiration:{action_at_expiration}")
            self.auto_actions.click_reference(self.get_action_at_exp_show_expi_msg_radio_button)

        if action_at_expiration == "Access Rejected":
            self.utils.print_info(f"select Action at Expiration:{action_at_expiration}")
            self.auto_actions.click_reference(self.get_action_at_exp_access_rejected_radio_button)

        return 1
