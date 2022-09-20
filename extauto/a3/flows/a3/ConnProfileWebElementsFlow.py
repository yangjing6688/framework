from common.AutoActions import *
from a3.elements.ConnProfileWebElements import ConnProfileWebElements
from a3.elements.GlobalSettingWebElements import *
from xiq.flows.common.DeviceCommon import DeviceCommon
from common.CloudDriver import *


class ConnProfileWebElementsFlow(ConnProfileWebElements):
    def __init__(self):
        super().__init__()
        self.driver1 = None
        self.utils = Utils()
        self.auto_actions = AutoActions()
        self.screen = Screen()
        self.device_common = DeviceCommon()
        self.conn_profile_web_elements = ConnProfileWebElements()
        self.setting = GlobalSettingWebElements()

    def create_mac_conn_profile(self, profile_name, profile_desc):
        """
        - This keyword will create the Mac connection profile
        - Keyword Usage
        - ``Create Mac Conn Profile``
        :return: 1 if connection profile is created successfully else return -1
        """
        if self.auto_actions.click(self.select_conn_profile_menu()) == 1:
            sleep(5)
            self.utils.print_info("create a new connection profile ")
            sleep(10)
            new_profile = self.weh.get_element(self.conn_profile_new)
            self.auto_actions.click(new_profile)
            sleep(5)
            self.utils.print_info("profile name ")
            name = self.weh.get_element(self.conn_profile_name)
            self.auto_actions.send_keys(name, profile_name)
            sleep(5)
            self.utils.print_info("profile Description ")
            desc = self.weh.get_element(self.conn_profile_desc)
            self.auto_actions.send_keys(desc, profile_desc)
            sleep(5)
            self.utils.print_info("click add filter")
            auth_add_rule = self.weh.get_element(self.add_filter)
            self.auto_actions.click(auth_add_rule)
            sleep(5)
            self.utils.print_info("Select action 1 for row 1")
            act1 = self.weh.get_element(self.add_filter_act1)
            self.auto_actions.click(act1)
            sleep(5)
            drop1 = self.weh.get_element(self.drop_opt_act1)
            self.auto_actions.click(drop1)
            sleep(5)
            self.utils.print_info("Select action 2 for row 1")
            act2 = self.weh.get_element(self.add_filter_act2)
            self.auto_actions.click(act2)
            sleep(5)
            drop2 = self.weh.get_element(self.drop_opt_act2)
            self.auto_actions.click(drop2)
            sleep(5)
            self.utils.print_info("Click on Add Source")
            add_src_btn = self.weh.get_element(self.add_source)
            self.auto_actions.click(add_src_btn)
            sleep(5)
            self.utils.print_info("Select Source")
            src = self.weh.get_element(self.select_source)
            self.auto_actions.click(src)
            sleep(5)
            self.utils.print_info("Created 802.1X Connection Profile")
            create_conn_profile = self.weh.get_element(self.save_button)
            self.auto_actions.click(create_conn_profile)
            sleep(5)
            self.utils.print_info("802.1X Connection Profile is created successfully")
            return 1
        else:
            self.utils.print_info("Connection Profile is not created")
            return -1

    def create_guest_conn_profile(self, profile_name, profile_desc):
        """
        - This keyword will create the Guest connection profile
        - Keyword Usage
        - ``Create Guest Conn Profile``
        :return: 1 if connection profile is created successfully else return -1
        """
        if self.auto_actions.click(self.select_conn_profile_menu()) == 1:
            sleep(5)
            self.utils.print_info("create a new connection profile ")
            sleep(10)
            new_profile = self.weh.get_element(self.conn_profile_new)
            self.auto_actions.click(new_profile)
            sleep(5)
            self.utils.print_info("profile name ")
            name = self.weh.get_element(self.conn_profile_name)
            self.auto_actions.send_keys(name, profile_name)
            sleep(5)
            self.utils.print_info("profile Description ")
            desc = self.weh.get_element(self.conn_profile_desc)
            self.auto_actions.send_keys(desc, profile_desc)
            sleep(5)
            self.utils.print_info("click add filter")
            auth_add_rule = self.weh.get_element(self.add_filter)
            self.auto_actions.click(auth_add_rule)
            sleep(5)
            self.utils.print_info("Select action 1 for row 1")
            act1 = self.weh.get_element(self.add_filter_act1)
            self.auto_actions.click(act1)
            sleep(5)
            drop1 = self.weh.get_element(self.drop_opt_act1)
            self.auto_actions.click(drop1)
            sleep(5)
            self.utils.print_info("Select action 2 for row 1")
            act2 = self.weh.get_element(self.add_filter_act2)
            self.auto_actions.click(act2)
            sleep(5)
            drop2 = self.weh.get_element(self.drop_opt_act3)
            self.auto_actions.click(drop2)
            sleep(5)
            self.utils.print_info("Click on Add Source")
            add_src_btn = self.weh.get_element(self.add_source)
            self.auto_actions.click(add_src_btn)
            sleep(5)
            self.utils.print_info("Select Source")
            src = self.weh.get_element(self.select_source)
            self.auto_actions.click(src)
            sleep(5)
            self.utils.print_info("Created Guest Connection Profile")
            create_conn_profile = self.weh.get_element(self.save_button)
            self.auto_actions.click(create_conn_profile)
            sleep(5)
            self.utils.print_info("Guest Connection Profile is created successfully")
            return 1
        else:
            self.utils.print_info("Connection Profile is not created")
            return -1

    def select_radius_audit_logs(self, mac, auth_status, user_name):
        """
        - This keyword will validate the authentication with A3 in Auditing tab by selecting the auditing details
        - Keyword Usage
        - ``Select Radius Audit Logs mac auth_status client_status``
        :param mac:  it should be mac address of the client
        :param auth_status:  it should be authentication status of the client ex: Accept/Reject
        :param user_name:  it should be the user name ex: ad or mac id
        :return: 1 if Authentication is done successfully else -1
        """
        if self.auto_actions.click(self.get_radius_audit_log_ui()) == 1:
            sleep(2)
            self.utils.print_info(f"select the table")
            tab = self.weh.get_element(self.get_table)
            sleep(2)
            self.utils.print_info(f"select the table1")
            table = self.setting.get_audit_logs_grid_rows()
            self.utils.print_info(f"select the table2")
            ele_selected = tab.is_displayed
            self.utils.print_info(f"print status", ele_selected)
            sleep(5)
            if ele_selected:
                for rows in table:
                    for row in rows.text.splitlines():
                        if mac in row \
                            and auth_status in row \
                                and user_name in row:
                            self.utils.print_info(f"Found the Expected Row Text", row)
                            self.utils.print_info(f"clicked on the selected row")
                            sleep(5)
                            rows.click()
                            break
            rad_tab = self.weh.get_element(self.rad_entry_tab)
            self.auto_actions.click(rad_tab)
            radius_ent_info = self.weh.get_element(self.rad_ent_info)
            radius_open_info = self.weh.get_element(self.rad_open_info)
            sleep(5)
            if radius_ent_info:
                self.utils.print_info(f"Enterprise Authentication done successfully")
            elif radius_open_info:
                self.utils.print_info(f"Open Network Authentication done successfully")
            else:
                self.utils.print_info(f" Not Authenticated")
                return -1
            sleep(5)
        return 1

    def select_clients_search(self, mac, client_status, owner):
        """
        - This keyword will validate the authentication with A3 in clients tab by selecting the client details
        - Keyword Usage
        - ``Select Clients Search mac owner ``
        :param mac:  it should be mac address of the client
        :param client_status:  it should be the client connection status ex: online/offline - on /unknown
        :param owner:  it should be the user name ex: ad or default
        :return: 1 if Authentication is done successfully else -1
        """
        if self.auto_actions.click(self.get_clients_search_ui()) == 1:
            sleep(5)
            self.utils.print_info(f"select the table")
            sleep(10)
            table = self.setting.get_clients_search_rows()
            for rows in table:
                for row in rows.text.splitlines():
                    if mac in row \
                        and client_status in row \
                            and owner in row:
                        self.utils.print_info(f"Found the Expected Row Text", row)
                        self.utils.print_info(f"clicked on the selected row")
                        sleep(5)
                        rows.click()
                        break
            info_tab = self.weh.get_element(self.client_info_tab)
            self.auto_actions.click(info_tab)
            client_ent = self.weh.get_element(self.client_ent_info)
            client_open = self.weh.get_element(self.client_open_info)
            if client_ent:
                self.utils.print_info(f"Enterprise Authentication done successfully")
            elif client_open:
                self.utils.print_info(f"Open Network Authentication done successfully")
            else:
                self.utils.print_info(f" Not Authenticated")
                return -1
            sleep(5)

        return 1

