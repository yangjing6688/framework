from time import sleep
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.elements.GuestPasswdSettingElements import GuestPasswdSettingElements


class GuestPasswdSetting(GuestPasswdSettingElements):
    def __init__(self):
        super().__init__()
        self.auto_actions = AutoActions()
        self.utils = Utils()

    def config_password_settings(self, **passwd_config):
        """
        - This keyword used with standalone and along with user group creation
        - In stand alone mode assumes that  navigating to the user group
        - For password_setting configuration variable refer the user_group_config robot file password setting section
        - Configure the password settings
        - keyword Usage:
         - ``Config Password Setting  &{PASSWORD_CONFIG}``

        :param passwd_config:
        :return: 1 if password config setting is success
        """

        letters = passwd_config.get('letters')
        numbers = passwd_config.get('numbers')
        special_characters = passwd_config.get('special_characters')
        enforce_use_of = passwd_config.get('enforce_use_of')
        gen_passwd_len = passwd_config.get('gen_passwd_len')
        self.utils.print_info(passwd_config)

        self.utils.print_info("Letters check box:{}".format(letters))
        if letters.upper() == 'ENABLE':
            self.auto_actions.enable_check_box(self.get_letters_check_box())
            sleep(2)
        else:
            self.auto_actions.disable_check_box(self.get_letters_check_box())
            sleep(2)

        self.utils.print_info("numbers check box:{}".format(numbers))
        if numbers.upper() == 'ENABLE':
            self.auto_actions.enable_check_box(self.get_numbers_check_box())
            sleep(2)
        else:
            self.auto_actions.disable_check_box(self.get_numbers_check_box())

        self.utils.print_info("special characters check box:{}".format(special_characters))
        if special_characters.upper() == 'ENABLE':
            self.auto_actions.enable_check_box(self.get_special_character_check_box())
            sleep(2)
        else:
            self.auto_actions.disable_check_box(self.get_special_character_check_box())

        self.auto_actions.scroll_down()
        self.utils.print_info("enforce the use of :{}".format(enforce_use_of))
        self.auto_actions.click(self.get_enforce_use_of_drop_down())
        sleep(2)

        enforce_opts = self.get_enforce_use_of_options()
        self.auto_actions.select_drop_down_options(enforce_opts, enforce_use_of)

        self.utils.print_info("Generate Password length:{}".format(gen_passwd_len))
        self.auto_actions.click(self.get_generate_password_length_drop_down())
        sleep(2)

        gen_passwd_len_opts = self.get_generate_password_length_options()
        self.auto_actions.select_drop_down_options(gen_passwd_len_opts, gen_passwd_len)
        return 1
