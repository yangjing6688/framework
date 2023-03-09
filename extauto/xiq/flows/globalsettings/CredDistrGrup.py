from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.elements.CredDistrGrupWebElemnts import CredDistrGrupWebElemnts
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.common.CommonValidation import CommonValidation


class CredDistrGrup(CredDistrGrupWebElemnts):
    def __init__(self):
        super().__init__()
        self.navigator = Navigator()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.utils = Utils()
        self.common_validation = CommonValidation()

    def _search_cred_distr_group(self, group_name):
        """
        - Search the credentials distribution group

        :param group_name:
        :return: row if exists else None
        """
        for row in self.get_cred_distr_grps_grid_rows():
            if group_name.upper() in row.text.upper():
                self.utils.print_info(f"Credential Distribution group:{group_name} exists")
                return row

    def delete_cred_distr_group(self, group_name, **kwargs):
        """
        - Flow: Global Settings --> Credential Distribution Groups
        - Search the credentials distribution group
        - If exists delete the group
        - Keyword Usage:
        - ``Delete Cred Distr Group   ${GROUP_NAME}``

        :param group_name: group name
        :return: 1 if deleted
        """
        self.utils.print_info("Navigate to Credential Distribution page")
        self.navigator.navigate_to_credential_dist_groups()

        if row := self._search_cred_distr_group(group_name):
            self.utils.print_info(f"Credential Distribution group:{group_name} exists, delete it !!")
            self.auto_actions.click(self.get_cred_dist_grps_grid_row_check_box(row))
            sleep(2)
            self.utils.print_info("Click on delete button")
            self.auto_actions.click_reference(self.get_cred_distr_grps_row_delete_button)
            sleep(2)
            self.auto_actions.click_reference(self.get_cred_distr_grps_row_delete_confirm_yes_button)
            sleep(2)
            kwargs['pass_msg'] = "Successfully delete cred distr group"
            self.common_validation.passed(**kwargs)
            return 1

    def create_cred_distribution_group(self, group_config, **kwargs):
        """
        - Flow: Global Settings --> Credential Distribution Groups
        - Create Credential distribution Groups
        - There are two admin account type need to include the cred distribution groups
        - 1. Guest Management Role User. 2.Active directory User
        - Keyword Usage:
        - ``Create Cred Distribution Groups  &{CRED_DISTR_GROUPS_CONFIG}``
        - For Creation of &{CRED_DISTR_GROUPS_CONFIG}  refer emails_reports_config.robot file

        :param group_config: (dict) configuration parameters
        :return: 1 if group created
                -1 Configure at least one guest management user
        """
        self.utils.print_info(group_config)

        group_name = group_config.get('group_name')
        admin_account = group_config.get('admin_account')
        guest_mgmt_user = group_config.get('guest_mgmt_user')
        member_of = group_config.get('member_of', 'None')
        cred_restriction = group_config.get('cred_restriction')
        cred_restriction_num = group_config.get('cred_restriction_num', 10)
        reg_operation = group_config.get('reg_operation')
        enable_user_groups = group_config.get('enable_user_groups')
        user_group = group_config.get('user_group')

        self.utils.print_info("Navigate to Credential Distribution page")
        self.navigator.navigate_to_credential_dist_groups()

        self.delete_cred_distr_group(group_name)
        self.utils.print_info("Click on add button")
        self.auto_actions.click_reference(self.get_cred_distr_grps_add_button)
        sleep(2)

        self.utils.print_info(f"Enter group name:{group_name}")
        self.auto_actions.send_keys(self.get_cred_distr_grps_name_field(), group_name)

        self.utils.print_info("click on admin account drop down")
        self.auto_actions.click_reference(self.get_cred_distr_grps_admin_acct_drop_down)
        sleep(2)

        self.auto_actions.select_drop_down_options(self.get_cred_distr_grps_admin_acct_drop_down_opts(), admin_account)

        if admin_account == "Guest Management Role User":
            self.utils.print_info(f"Enter guest management user:{guest_mgmt_user}")
            self.auto_actions.send_keys(self.get_cred_distr_guest_mgmt_usr_text_field(), guest_mgmt_user)

        if admin_account == "Active Directory User":
            self.utils.print_info(f"Enter member of:{member_of}")
            self.auto_actions.send_keys(self.get_cred_distr_member_of_text_field(), member_of)

        if cred_restriction.upper() == "ENABLE":
            self.auto_actions.enable_check_box(self.get_cred_restriction_check_box())
            self.utils.print_info(f"Enter credential restriction numbers:{cred_restriction_num}")
            self.auto_actions.send_keys(self.get_cred_restriction_number(), cred_restriction_num)

        if reg_operation.upper() == "ENABLE":
            self.auto_actions.enable_check_box(self.get_restriction_operation_check_box())

        if enable_user_groups.upper() == "ENABLE":
            self.auto_actions.enable_check_box(self.get_enable_usr_grps_check_box())
        else:
            self.utils.print_info(f"Select user group:{user_group}")
            self.auto_actions.select_drop_down_options(self.get_enable_usr_grps_list(), user_group)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("click on credential distribution save button")
        self.auto_actions.click_reference(self.get_cred_distr_grp_save_button)

        self.screen.save_screen_shot()
        sleep(2)

        tool_tip_text = tool_tip.tool_tip_text
        self.utils.print_info(tool_tip_text)
        for text in tool_tip_text:
            if "Configure at least one guest management user" in text:
                kwargs['fail_msg'] = f"{text}"
                self.common_validation.failed(**kwargs)
                return -1
            if "The Employee Group was saved successfully" in text:
                kwargs['pass_msg'] = f"{text}"
                self.common_validation.passed(**kwargs)
                return 1
        kwargs['pass_msg'] = "Successfully create  credential distribution Groups"
        self.common_validation.passed(**kwargs)
        return 1
