from time import sleep
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.common.Screen import Screen
import extauto.xiq.flows.common.ToolTipCapture as tool_tip
from extauto.xiq.elements.RSWebElements import RSWebElements
from extauto.common.CommonValidation import CommonValidation


class RadiusServer(RSWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.common_validation = CommonValidation()

    def _add_ip_address_name_to_radius_server(self, name, ip):
        """
        config radius server ip address and its name
        :param name: Name attached to IP address
        :param ip: IP address
        :return:
        """
        self.utils.print_info("click on IP/host name add button")
        self.auto_actions.click_reference(self.get_new_external_radius_server_ip_host_add_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        options = self.get_new_external_radius_server_ip_host_select_items()
        self.auto_actions.select_drop_down_options(options, "IP Address")
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Enter IP Host name:{}".format(name))
        self.auto_actions.send_keys(self.get_new_external_radius_server_host_name_field(), name)

        self.utils.print_info("Enter the IP Host IP address:{}".format(ip))
        self.auto_actions.send_keys(self.get_new_external_radius_server_ip_address_field(), ip)
        self.screen.save_screen_shot()
        sleep(2)

        self.auto_actions.click_reference(self.get_new_external_radius_server_save_ip_button)
        sleep(2)
        self.screen.save_screen_shot()
        sleep(2)

        return 1

    def _select_ip_address_radius_server(self, rs_ip_host_name):
        """
        - Select the IP address to the radius server

        :param rs_ip_host_name: IP name to select
        :return: 1
        """
        self.auto_actions.click_reference(self.get_extreme_networks_radius_server_select_button)
        self.screen.save_screen_shot()
        sleep(2)

        ip_list_el = self.get_new_external_radius_server_ip_list_items()
        ip_names = self.get_new_external_radius_server_ip_list_item(ip_list_el)

        if self.auto_actions.select_drop_down_options(ip_names, rs_ip_host_name):
            return 1

    def _create_new_external_radius_server(self, **rs_config):
        """
        - Assumes that navigated to radius server add window
        - Create new external radius server
        - refer "Creating Radius Server group profile" for rs_config dict in captive_web_portal_config.robot
        - Keyword Usage:
        - ``Create New External Radius Server   &{RS_CONFIG}``

        :param rs_config: configuration dictionary to create new external radius server
        :return: True if created
        """
        rs_name = rs_config.get('radius_server_name', 'DEMO1')
        shared_secret = rs_config.get('shared_secret')
        ip_or_host_type = rs_config.get('ip_or_host_type')

        ip_or_host_name = rs_config.get('radius_server_ip_host_name')
        ip_address = rs_config.get('radius_server_ip_address')

        self.utils.print_info("Enter new radius server name")
        self.auto_actions.send_keys(self.get_new_external_radius_server_name_field(), rs_name)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click on IP/host name select drop down")
        self.auto_actions.click_reference(self.get_new_external_radius_server_ip_host_select_drop_down)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Check the radius_server_ip_host_name:{} in drop down".format(ip_or_host_name))
        if ip_or_host_type == "IP Address":
            if self._select_ip_address_radius_server(ip_or_host_name):
                self.utils.print_info("radius server IP or host name:{} is selected".format(ip_or_host_name))
            else:
                self._add_ip_address_name_to_radius_server(ip_or_host_name, ip_address)

        elif ip_or_host_type == "Host Name":
            # @to do
            pass

        self.utils.print_info("Enter the shared secret key:{}".format(shared_secret))
        self.auto_actions.send_keys(self.get_external_radius_server_shared_secret_field(), shared_secret)
        sleep(2)

        self.utils.print_info("Click on Radius Server save button")
        self.auto_actions.click_reference(self.get_external_radius_server_save_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)
        return True

    def _select_external_radius_server(self, server_name):
        """
        Select the given external RADIUS server.
        :param server_name:
        :return:
        """
        self.utils.print_info("Check the RADIUS server name:{} in radius server grid".format(server_name))
        radius_server_rows = self.get_radius_server_list_rows()

        self.screen.save_screen_shot()
        sleep(2)

        for row in radius_server_rows:
            if server_name.upper() in row.text.upper():
                self.utils.print_info("select the RADIUS server row: {}".format(server_name))
                self.auto_actions.click(self.get_radius_server_list_row_select_checkbox(row))
                sleep(2)

                self.screen.save_screen_shot()
                sleep(2)

                self.utils.print_info("click on RADIUS server save button")
                self.auto_actions.click_reference(self.get_radius_server_save_radius_button)
                sleep(2)
                return True
        return False

    def config_external_radius_server(self, ext_server_config, **kwargs):
        """
        - This keyword is called in two ways, as standalone and as part of create network policy
        - For standalone assumes that user navigated to the RADIUS server group add dialog window
        - Create new external RADIUS server
        - refer "Creating RADIUS Server group profile" section for ext_server_config dict in
        captive_web_portal_config.robot
        - Keyword Usage:
        - ``Config External RADIUS Server   &{EXT_SERVER_CONFIG}``

        :param ext_server_config: dict to create the external RADIUS server
        :return: 1 if external RADIUS server group created else -1
        """
        ext_rs_name = ext_server_config.get('radius_server_name')

        self.utils.print_info("Click on EXTERNAL RADIUS SERVER label")
        self.auto_actions.click_reference(self.get_external_radius_server)
        sleep(2)

        select_status = self._select_external_radius_server(ext_rs_name)
        if select_status:
            kwargs['pass_msg'] = "External RADIUS server group created"
            self.common_validation.passed(**kwargs)
            return 1

        self.utils.print_info("Click on new external RADIUS server add button")
        self.auto_actions.click_reference(self.get_radius_server_list_add_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self._create_new_external_radius_server(**ext_server_config)
        select_status = self._select_external_radius_server(ext_rs_name)
        if select_status:
            kwargs['pass_msg'] = "External RADIUS server group created"
            self.common_validation.passed(**kwargs)
            return 1
        kwargs['fail_msg'] = "config_external_radius_server() failed. Failed to create external RADIUS server group"
        self.common_validation.failed(**kwargs)
        return -1

    def _add_radius_server_group(self, **group_config):
        """
        Create new server group based on the passed argument dict
        :param group_config:
        :return:
        """
        rs_group_name = group_config.get('radius_server_group_name')
        rs_config = group_config.get('radius_server_config')
        server_type = rs_config.get('server_type')

        self.utils.print_info("Click on default RADIUS server group add button")
        self.auto_actions.click_reference(self.get_default_radius_server_group_add_button)
        sleep(2)

        self.utils.print_info("Enter RADIUS Server Group name")
        self.auto_actions.send_keys(self.get_radius_server_group_name_field(), rs_group_name)

        if server_type.upper() == "EXTERNAL RADIUS SERVER":
            ext_rs_config = rs_config.get('external_radius_server_config')
            return self.config_external_radius_server(ext_rs_config)

        if server_type.upper() == "EXTREME NETWORKS RADIUS SERVER":
            extreme_rs_config = rs_config.get('extreme_radius_server_config')
            return self.config_extreme_networks_radius_server(extreme_rs_config)

    def _select_radius_server_group_row(self, rs_group_name):
        """
        - Select RADIUS server group row from select window grid
        :param rs_group_name: RADIUS server group name
        :return: True if row selected else false
        """
        self.utils.print_info("Click on default radius server group select button")
        self.auto_actions.center_element(self.get_default_radius_server_group_select_button())

        self.auto_actions.click_reference(self.get_default_radius_server_group_select_button)
        sleep(2)

        for row in self.get_default_radius_server_group_dialog_rsg_rows():
            if rs_group_name.upper() in row.text.upper():
                self.auto_actions.click(self.get_default_radius_server_group_dialog_rsg_row_checkbox(row))
                sleep(2)
                return True
        self.utils.print_info(f"default RADIUS server group: {rs_group_name} doesn't exist, Please create default")
        self.auto_actions.click_reference(self.get_default_radius_server_group_dialog_cancel_button)
        sleep(2)
        return False

    def _select_radius_server_group(self, rs_group_name):
        """
        Select the radius server in select window
        :param rs_group_name:
        :return:
        """
        if self._select_radius_server_group_row(rs_group_name):
            self.auto_actions.click_reference(self.get_default_radius_server_group_dialog_select_button)
            return True

    def delete_radius_server_group(self, rs_group_name, **kwargs):
        """
        - Select the RADIUS server group and delete it
        - Keyword Usage:
        - ``Delete RADIUS Server Group   ${RS_GROUP_NAME}``

        :param rs_group_name:
        :return: True if deleted else False
        """
        if self._select_radius_server_group_row(rs_group_name):
            self.utils.print_info("Click delete Button to delete RADIUS Group Name")
            self.auto_actions.click_reference(self.get_radius_server_group_delete_button)
            sleep(2)

            self.utils.print_info("Click Confirm Delete Button")
            self.auto_actions.click_reference(self.get_radius_server_group_delete_confirm_button)
            sleep(3)

            tool_tp_text = tool_tip.tool_tip_text
            self.utils.print_info(tool_tp_text)
            sleep(2)

            self.utils.print_info("Click Cancel Button")
            self.auto_actions.click_reference(self.get_default_radius_server_group_dialog_cancel_button)
            sleep(2)
            for value in tool_tp_text:
                if "The item was deleted successfully" in value:
                    kwargs['pass_msg'] = "The item was deleted successfully"
                    self.common_validation.passed(**kwargs)
                    return True

            kwargs['fail_msg'] = "delete_radius_server_group() failed. Failed to delete radius server group"
            self.common_validation.failed(**kwargs)
            return False
        else:
            self.utils.print_info("default RADIUS server group:{} doesn't exist, create it..".format(rs_group_name))
            self.auto_actions.click_reference(self.get_default_radius_server_group_dialog_cancel_button)
            kwargs['fail_msg'] = "delete_radius_server_group() failed. RADIUS server group doesn't exist"
            self.common_validation.failed(**kwargs)
            return False

    def config_radius_server(self, **rs_group_config):
        """
        - Configuring the RADIUS server
        :param rs_group_config:
        :return: 1 if RADIUS server already exists else add the radius server group
        """
        rs_group_name = rs_group_config.get('radius_server_group_name')

        self.utils.print_info("select RADIUS server group in select windows")
        if self._select_radius_server_group(rs_group_name):
            self.utils.print_info("Selected RADIUS server group:{}".format(rs_group_name))
            return 1
        return self._add_radius_server_group(**rs_group_config)

    def config_extreme_networks_radius_server(self, extreme_networks_server_config, **kwargs):
        """
        - This keyword called two ways standalone way and as part of crete network policy keyword
        - for standalone assumes that user navigated the RADIUS server group add window
        - Assumes that navigated to RADIUS server add window
        - Create new external RADIUS server
        - refer "Creating RADIUS Server group profile" section for ext_server_config dict in
            enterprise_dot11x_config.robot
        - Keyword Usage:
        - ``Config Extreme Network RADIUS Server   ${extreme_networks_server_config}``

        :param extreme_networks_server_config: dict to create the extreme radius server
        :return: 1 if external RADIUS server group created else -1
        """
        ext_rs_name = extreme_networks_server_config.get('radius_server_name')

        self.utils.print_info("Click on EXTREME NETWORKS RADIUS SERVER label")
        self.auto_actions.click_reference(self.get_extreme_networks_radius_server)
        sleep(2)

        # select Local Database as use DB
        self.utils.print_info("Select Use Database Type as Local Database")
        self.utils.print_info("Click Use Database Type scroll down box")
        self.auto_actions.click_reference(self.get_extreme_networks_radius_server_db_scroll_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        db_items = self.get_extreme_networks_radius_server_db_drop_down_items()
        for item in db_items:
            if "LOCAL DATABASE" in item.text.upper():
                self.utils.print_info("Selecting local Database from drop down")
                self.auto_actions.click(item)
                sleep(2)
                break
        # select the radius server if it exists in the list
        select_status = self._select_extreme_networks_radius_server(ext_rs_name)
        if select_status:
            return 1

        self.utils.print_info("Click on new external RADIUS server add button")
        self.auto_actions.click_reference(self.get_extreme_networks_device_as_radius_server_list_add_button)

        self.screen.save_screen_shot()
        sleep(2)

        sleep(2)
        self._create_new_extreme_networks_radius_server(**extreme_networks_server_config)

        select_status = self._select_extreme_networks_radius_server(ext_rs_name)
        if select_status:
            kwargs['pass_msg'] = "External RADIUS server group created"
            self.common_validation.passed(**kwargs)
            return 1
        kwargs['fail_msg'] = "config_extreme_networks_radius_server() failed. " \
                             "Failed to create external RADIUS server group"
        self.common_validation.failed(**kwargs)
        return -1

    def _select_extreme_networks_radius_server(self, server_name):
        """
        Selects extreme networks RADIUS server
        :param server_name:
        :return: True is selected else False
        """
        self.utils.print_info("Check the RADIUS server name: {} in radius server table".format(server_name))
        radius_server_rows = self.get_extreme_networks_radius_server_list_rows()
        for row in radius_server_rows:
            if server_name.upper() in row.text.upper():
                self.utils.print_info("select the RADIUS server row: {}".format(server_name))
                self.auto_actions.click(self.get_extreme_networks_radius_server_list_row_select_checkbox(row))
                sleep(2)
                self.utils.print_info("click on RADIUS server save button")
                self.auto_actions.click_reference(self.get_radius_server_save_radius_button)
                sleep(2)
                return True
        return False

    def _create_new_extreme_networks_radius_server(self, **new_rs_config):
        """
        - Create new extreme_networks_radius_server passed config dict
        :param new_rs_config:
        :return:
        """
        aaa_profile_name = new_rs_config.get('aaa_profile_name', 'Test_AAA_profile')
        rs_ip_host_name = new_rs_config['radius_server_ip_host_name']
        user_database = new_rs_config['user_db_type']
        shared_secret = new_rs_config['shared_secret']
        host_ip_type = new_rs_config['host_ip_type_opt']
        server_name = new_rs_config['radius_server_name']
        user_group = new_rs_config['user_group']

        self.utils.print_info("Check the Device name: {} in RADIUS server table".format(server_name))
        radius_server_rows = self.get_extreme_networks_device_as_radius_server_list_rows()
        for row in radius_server_rows:
            if server_name.upper() in row.text.upper():
                self.utils.print_info("select the Device as RADIUS server row: {}".format(server_name))
                self.auto_actions.click(self.get_extreme_networks_device_as_radius_server_list_row_select_checkbox(row))
                sleep(2)

                self.screen.save_screen_shot()
                sleep(2)
        sleep(2)
        self.utils.print_info("Enter new RADIUS server aaa profile name")
        self.auto_actions.send_keys(self.get_extreme_networks_radius_server_aaa_name(), aaa_profile_name)

        self.screen.save_screen_shot()
        sleep(2)

        self.auto_actions.scroll_down()
        sleep(4)

        self.utils.print_info("Disabling Default user Database config")
        if self.get_user_db_active_directory_checkbox().is_selected():
            self.auto_actions.click_reference(self.get_user_db_active_directory_checkbox)
            sleep(2)

        if user_database.upper() == "LOCAL DATABASE":
            self.utils.print_info("Select the Local Database check box")
            if not self.get_user_db_local_database_checkbox().is_selected():
                self.auto_actions.click_reference(self.get_user_db_local_database_checkbox)
                sleep(2)

                self.screen.save_screen_shot()
                sleep(2)

        if user_database.upper() == "LDAP":
            self.utils.print_info("Select the LDAP Database check box")
            if not self.get_user_db_ldap_database_checkbox().is_selected():
                self.auto_actions.click_reference(self.get_user_db_ldap_database_checkbox)
                sleep(2)

        if user_database.upper() == "ACTIVE DIRECTORY":
            self.utils.print_info("Select the active directory Database check box")
            if not self.get_user_db_active_directory_checkbox().is_selected():
                self.auto_actions.click_reference(self.get_user_db_active_directory_checkbox)
                sleep(2)

        sleep(2)
        self.utils.print_info("Selecting User group for the Database")
        self._select_user_group_for_database(user_group)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click Approved Radius Clients ")
        self.auto_actions.click_reference(self.get_extreme_networks_radius_server_approved_clients_tab)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Click Add Button")
        self.auto_actions.click_reference(self.get_extreme_networks_radius_server_add_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Check the radius_server_ip_host_name:{} in drop down".format(rs_ip_host_name))
        if host_ip_type == "IP Address":
            if self._select_ip_address_radius_server(rs_ip_host_name):
                self.utils.print_info("radius server ip name: {} is selected".format(rs_ip_host_name))
                sleep(2)

                self.screen.save_screen_shot()
                sleep(2)
            else:
                ip_name = new_rs_config['radius_server_ip_host_name']
                ip_address = new_rs_config['radius_server_ip_address']
                self._add_ip_address_name_to_extreme_networks_radius_server(ip_name, ip_address)
                sleep(2)

        elif host_ip_type == "Host Name":
            # @to do
            pass

        sleep(2)
        self.utils.print_info("Enter the shared secret key:{}".format(shared_secret))
        send_status = self.auto_actions.send_keys(self.get_extreme_networks_device_as_radius_server_shared_secret_field(), shared_secret)
        self.screen.save_screen_shot()
        sleep(2)
        if not send_status:
            self.auto_actions.send_keys(self.get_extreme_networks_radius_server_shared_secret_field1(), shared_secret)

        sleep(2)
        self.utils.print_info("Click on RADIUS Server save button")
        self.auto_actions.click_reference(self.get_external_radius_server_save_button)
        sleep(2)
        self.screen.save_screen_shot()
        sleep(2)
        return True

    def _add_ip_address_name_to_extreme_networks_radius_server(self, ip_name, ip):
        """
        Add ip address and name to extreme networks radius server.
        :param ip_name: Name given to the ip radius server
        :param ip: ip address
        :return:
        """
        self.utils.print_info("click on IP/host name add button")
        self.auto_actions.click_reference(self.get_extreme_networks_radius_server_ip_host_add_button)
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        options = self.get_new_external_radius_server_ip_host_select_items()
        for opt in options:
            if "IP Address".upper() in opt.text.upper():
                self.auto_actions.click(opt)
                sleep(2)
                self.screen.save_screen_shot()
                sleep(2)
                break

        self.utils.print_info("Enter IP Host name:{}".format(ip_name))
        self.auto_actions.send_keys(self.get_new_external_radius_server_host_name_field(), ip_name)

        self.utils.print_info("Enter the IP Host IP address:{}".format(ip))
        self.auto_actions.send_keys(self.get_new_external_radius_server_ip_address_field(), ip)

        self.screen.save_screen_shot()
        sleep(2)

        self.auto_actions.click_reference(self.get_new_external_radius_server_save_ip_button)
        sleep(2)
        return 1

    def _select_user_group_for_database(self, group_name):
        """
        select the user group
        :param group_name: Name of the group to select
        :return:
        """
        self.utils.print_info("Click on user group select button")
        self.auto_actions.click_reference(self.get_user_group_select_button)
        sleep(8)

        self.utils.print_info("Check user group present in  user group select windows")
        user_group_rows = self.get_user_group_select_dialog_usergroup_rows()

        if not user_group_rows:
            self.utils.print_info("User group:{} not present in select window ".format(group_name))
            self.auto_actions.click_reference(self.get_user_group_dialog_cancel_button)
            sleep(2)
            self.screen.save_screen_shot()
            sleep(2)
            return -1
        for row in user_group_rows:
            if group_name.upper() in row.text.upper():
                self.auto_actions.click(self.get_usergroup_dialog_usergroup_row_checkbox(row))
                sleep(2)
                self.auto_actions.click_reference(self.get_usergroup_dialog_select_button)
                sleep(2)
                self.screen.save_screen_shot()
                sleep(2)
                return 1
        self.utils.print_info("User group:{} not present in select window ".format(group_name))
        self.auto_actions.click_reference(self.get_user_group_dialog_cancel_button)
        return -1
