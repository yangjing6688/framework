from time import sleep
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from xiq.elements.PasswdSettingsWebElements import PasswdSettingsWebElements


class PasswdSettings(PasswdSettingsWebElements):

    def __init__(self):
        super().__init__()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def _config_psk_gen_method(self, psk_gen_method='Password Only', concatenating_str="auto"):
        """
        - If password type is PPSK we have to mention the psk generation method
        - PSK Generation method takes below two values
         - Password Only
         - User String Password

        :param psk_gen_method:  PSK gen method
        :param concatenating_str: concatenate the user string to password
        :return: None
        """
        self.utils.print_info("PSK generation method:{}".format(psk_gen_method))
        self.auto_actions.click(self.get_psk_generation_method_drop_down())
        sleep(2)

        psk_gen_opts = self.get_psk_generation_method_options()
        for opt in psk_gen_opts:
            if psk_gen_method.upper() in opt.text.upper():
                self.auto_actions.click(opt)
                break

        if psk_gen_method.upper() == "USER STRING PASSWORD":
            self.utils.print_info("Concatenating String is:{}".format(concatenating_str))
            self.auto_actions.send_keys(self.get_concatenating_string(), concatenating_str)

    def config_password_settings(self, **passwd_config):
        """
        - Configure the user group password settings
        - This keyword is called along with user group creation
        - For standalone call, assumes that navigated to configure-->users-->user groups --> add user
        - Keyword Usage:
         - ``Config Password Settings   &{PASSWORD_CONFIG}``
         - for &{PASSWORD_CONFIG} creation refer user_groups_config.robot "Password Settings" section

        :param passwd_config: password config parameters
        :return: 1 if configured else None
        """
        passwd_type = passwd_config.get('passwd_type')
        letters = passwd_config.get('letters')
        numbers = passwd_config.get('numbers')
        special_characters = passwd_config.get('special_characters')

        enforce_use_of = passwd_config.get('enforce_use_of')

        psk_gen_method = passwd_config.get('psk_gen_method')
        gen_passwd_len = passwd_config.get('gen_passwd_len')
        concatenating_str = passwd_config.get('concatenating_str')

        self.utils.print_info("letters check box:{}".format(letters))
        if letters.upper() == 'ENABLE':
            self.auto_actions.enable_check_box(self.get_letters_check_box())
        else:
            self.auto_actions.disable_check_box(self.get_letters_check_box())

        self.utils.print_info("numbers check box:{}".format(numbers))
        if numbers.upper() == 'ENABLE':
            self.auto_actions.enable_check_box(self.get_numbers_check_box())
        else:
            self.auto_actions.disable_check_box(self.get_numbers_check_box())

        self.utils.print_info("special characters check box:{}".format(special_characters))
        if special_characters.upper() == 'ENABLE':
            self.auto_actions.enable_check_box(self.get_special_character_check_box())
        else:
            self.auto_actions.disable_check_box(self.get_special_character_check_box())

        self.utils.print_info("enforce the use of :{}".format(enforce_use_of))
        self.auto_actions.click(self.get_enforce_use_of_drop_down())
        sleep(2)

        enforce_opts = self.get_enforce_use_of_options()
        self.auto_actions.select_drop_down_options(enforce_opts, enforce_use_of)

        if passwd_type.upper() == "PPSK":
            self._config_psk_gen_method(psk_gen_method, concatenating_str)

        self.utils.print_info("Generate Password length:{}".format(gen_passwd_len))
        self.auto_actions.click(self.get_generate_password_length_drop_down())
        sleep(2)

        gen_passwd_len_opts = self.get_generate_password_length_options()
        self.auto_actions.select_drop_down_options(gen_passwd_len_opts, gen_passwd_len)
        return 1
