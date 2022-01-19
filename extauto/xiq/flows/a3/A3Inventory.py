import json
import requests
from time import sleep
import extauto.common.CloudDriver
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.common.AutoActions import *
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.A3InventoryWebElements import A3InventoryWebElements


class A3Inventory(A3InventoryWebElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.driver = common.CloudDriver.cloud_driver
        self.navigator = Navigator()
        self.screen = Screen()
        self.auto_actions = AutoActions()

    def enable_ssh_access_on_a3_node(self, a3_addr, account, password, ssh_pass, duration):
        """
        - This Keyword Will enable SSH Access for A3 Version 3.2 Nodes
        - Keyword Usage
         - ``Enable Ssh Access On A3 Node   ${A3_ADDR}    ${ACCOUNT}     ${PASSWORD}    ${SSH_PWD}     ${DURATION}``
        :param a3_addr: A3 Node IP Address
        :param account: A3 Login username
        :param password: A3 Login Password
        :param ssh_pass: A3 Node SSH Password
        :param duration: Duration in Days to enable SSH access
        :return: 1 if ssh enabled successfully on A3 Node else -1
        """
        url = 'https://' + a3_addr + ':1443/api/v1/login'
        headers = {'Content-Type': 'application/json', 'content-length': '66'}
        body = {
            "username": account,
            "password": password
        }

        req = requests.post(url, headers=headers, data=json.dumps(body), verify=False)
        auth_result = json.loads(req.text)
        if req.status_code == 200:
            # Get current ssh configuration
            url = 'https://' + a3_addr + ':1443/a3/api/v1/troubleshooting/sshconfig'
            headers = {'Authorization': 'Bearer ' + auth_result["token"]}
            req = requests.get(url, headers=headers, verify=False)
            if req.status_code == 200:
                # Enable ssh access
                ssh_cfg = json.loads(req.text)
                ssh_cfg['enable'] = 'yes'
                ssh_cfg['password'] = ssh_pass
                ssh_cfg['duration'] = duration
                url = 'https://' + a3_addr + ':1443/a3/api/v1/troubleshooting/sshconfig'
                headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + auth_result["token"]}
                req = requests.post(url, headers=headers, data=json.dumps(ssh_cfg), verify=False)
                if req.status_code != 200:
                    self.utils.print_info('SSH configuration change failed: ' + req.status_code)
                    return -1
                if ssh_cfg['enable'] == 'yes':
                    self.utils.print_info(
                        'SSH access has been enabled user: sshuser password:' + ssh_pass + ' duration:' + ssh_cfg[
                            'duration'] + ' days')
                else:
                    self.utils.print_info('SSH access has been disabled, existing ssh session is still working until '
                                          'it disconnect')
            else:
                self.utils.print_info('Getting current SSH configuration failed: ' + req.status_code)
                return -1
        else:
            self.utils.print_info('Login to A3 failed: ' + req.status_code)
            return -1
        return 1

    def link_a3_nodes_to_xiq(self, spawn, username, password, url="https://cloud.aerohive.com", timeout=40):
        """
        - This Keyword Executes Curl Command to Link A3 Node to XIQ
        - It assumes that already opened SSH spawn of A3 Node.
        - Keyword Usage:
         - ``Link A3 Nodes To Xiq   ${SPAWN}    ${USERNAME}     ${PASSWORD}``
        :param spawn: A3 Node ssh Spawn
        :param username: XIQ User Name
        :param password: XIQ Password
        :param url: XIQ server URL
        :param timeout: Spawn command timeout in seconds
        :return: output of the Executed Curl Command
        """
        data = {"url":url ,"user":username,"pass":password}
        json_data = json.dumps(data)
        exec_command = 'curl -d ' "'"+ str(json_data)+"'" ' http://127.0.0.1:10000/api/v1/configuration/cloud' \
                                                      ' -X POST'
        try:
            stdin, stdout, stderr = spawn.exec_command(exec_command, timeout=timeout)
            output = stdout.read().decode('ascii').strip("\n")
            self.utils.print_info("cmd: {}".format(exec_command))
            self.utils.print_info("Output: {}".format(output))
            return output
        except Exception as e:
            print(e)
            self.utils.print_info("Failed to execute the Curl command")

    def unlink_a3_nodes_from_xiq(self, spawn, timeout=30):
        """
        - This keyword executes Curl command to UnLink A3 Node to XIQ
        - It assumes that already opened SSH spawn of A3 Node.
        - Keyword Usage:
         - ``Unlink A3 Nodes From Xiq    ${SPAWN} ``
        :param spawn: A3 Node ssh Spawn
        :param timeout: Spawn command timeout in seconds
        :return: output of the Executed Curl Command
        """
        data = {"url":""}
        json_data = json.dumps(data)
        exec_command = 'curl -d ' "'"+ str(json_data)+"'" ' http://127.0.0.1:10000/api/v1/configuration/cloud' \
                                                      ' -X POST'
        try:
            stdin, stdout, stderr = spawn.exec_command(exec_command, timeout=timeout)
            output = stdout.read().decode('ascii').strip("\n")
            self.utils.print_info("cmd: {}".format(exec_command))
            self.utils.print_info("Output: {}".format(output))
            return output
        except Exception as e:
            print(e)
            self.utils.print_info("Failed to execute the Curl command")

    def _goto_a3_inventory_page(self):
        """
        - This keyword will navigates to A3 inventory refresh list
        """
        self.utils.switch_to_default(self.driver)
        sleep(5)
        self.navigator.navigate_a3_inventory()
        sleep(2)
        self.utils.switch_to_iframe(self.driver)
        sleep(5)
        self.utils.print_info("Click A3 Inventory Refresh button")
        self.auto_actions.click(self.get_refresh_a3_devices_page())
        sleep(2)
        self.screen.save_screen_shot()
        sleep(2)
        return True

    def search_a3_device(self, a3_host_name):
        """
        - Searches for A3 server Host using its Host Name
        - It Assumes that its already Navigated to A3-->inventory Grid
        - Flow  A3-->inventory Grid
        - Keyword Usage:
         - ``Search A3 Device  ${A3_HOST_NAME}``

        :param a3_host_name: A3 server Host Name
        :return: return 1 if A3 host found on A3 Inventory Grid else -1
        """
        self.utils.print_info("Click A3 Inventory Refresh button")
        self.auto_actions.click(self.get_refresh_a3_devices_page())
        sleep(2)
        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Checking rows")
        rows = self.get_grid_rows()
        if rows:
            for row in rows:
                self.utils.print_debug("row data: ", self.format_row(row.text))
                if a3_host_name in row.text:
                    self.utils.print_info("Found A3 Virtual IP Row: ", self.format_row(row.text))
                    return 1
                else:
                    return -1
        else:
            return -1

    def format_row(self, row):
        """
         - This Keyword will give formatted row data
         - Flow  A3-->Inventory
         - Keyword Usage:
          - ``Format Row  ${ROW}``

         :param Row: A3 Inventory Grid Row
         :return: return Formatted Row Information
         """
        cell_values = row.split("\n")
        formatted_row = list()
        for cell_value in cell_values:
            formatted_row.append(cell_value)
        return formatted_row

    def get_a3_node_row(self, a3_host_name):
        """
        - Get the A3 Node row object from the A3 Inventory grid
        - Flow  A3-->Inventory
        - Keyword Usage:
         - ``Get A3 Node Row  ${A3_HOST_NAME}``

        :param a3_host_name: A3 Node  Host Name
        :return: returns the row object
        """
        self.utils.print_info('Getting A3 Node row...')
        rows = self.get_a3_node_grid_rows()
        if rows:
            for row in rows:
                if a3_host_name in row.text:
                    self.utils.print_info("Found A3 Node row: ", self.format_row(row.text))
                    return row

        self.utils.print_info("Unable to find A3 Node row in grid")
        return -1

    def get_a3_server_row(self, a3_host_name):
        """
        - Get the A3 server row object from the A3 Inventory grid
        - Flow  A3-->Inventory
        - Keyword Usage:
         - ``Get A3 Server Row  ${A3_HOST_NAME}``

        :param a3_host_name: A3 server Host Name
        :return: returns the row object
        """
        self.utils.print_info('Getting A3 Node row...')
        rows = self.get_grid_rows()
        if rows:
            for row in rows:
                if a3_host_name in row.text:
                    self.utils.print_info("Found A3 Node row: ", self.format_row(row.text))
                    return row

        self.utils.print_info("Unable to find A3 Node row in grid")
        return -1

    def get_a3_server_status(self, a3_host_name):
        """
        - This keyword returns the A3 virtual server status by searching host name
        - Flow  A3-->Inventory
        - Keyword Usage:
         - ``Get A3 Server Status    ${A3_HOST_NAME}``

        :param a3_host_name: A3 Server host Name
        :return: 'green' if the A3 Server is online else return -1
        """
        self._goto_a3_inventory_page()
        a3_row = -1

        self.utils.print_info('Getting A3 Node Status using')
        if a3_host_name:
            self.utils.print_info("Getting status of A3 Node with Host Name: ", a3_host_name)
            a3_row = self.get_a3_server_row(a3_host_name)

        if a3_row:
            sleep(10)
            a3_status = self.get_status_cell(a3_row)
            self.utils.print_info("A3 Node status " + a3_status)
            if 'icon-status' in a3_status:
                self.utils.print_info("A3 Node Status: Connected")
                return 'green'

        return -1

    def _expand_a3_server_node(self, a3_host_name):
        """
        - This keyword will Expand A3 Server Nodes using Host Name
        - Assumes that already navigated to the A3 --> Inventory

        :param a3_host_name: A3 Server host name
        :return: 1 if A3 Server Node Expanded Successfully else False
        """
        self._goto_a3_inventory_page()
        sleep(2)
        rows = self.get_grid_rows()
        print(rows)
        sleep(5)
        for row in rows:
            if a3_host_name in row.text:
                self.utils.print_debug("Found A3 device Row: ", self.format_row(row.text))
                sleep(5)
                if not self.get_a3_device_expanded_status():
                    self.utils.print_info("Clicking Expand Button to View A3 Nodes")
                    sleep(5)
                    self.auto_actions.click(self.get_a3_device_expanded_button(row))
                    self.screen.save_screen_shot()
                    sleep(2)
                return 1
        return False

    def get_a3_node_status(self, a3_server_name, a3_node_name):
        """
        - This keyword returns the A3 Node status by searching host name
        - Keyword Usage:
         - ``Get A3 Node Status    ${A3_HOST_NAME}``

        :param a3_server_name: A3 Server Host Name
        :param a3_node_name: A3 Node Host Name
        :return: 'green' if the A3 Node is online else return -1
        """
        self._expand_a3_server_node(a3_server_name)
        a3_row = -1

        self.utils.print_info('Getting A3 Node Status using')
        if a3_node_name:
            self.utils.print_info("Getting status of A3 Node with Host Name: ", a3_node_name)
            a3_row = self.get_a3_node_row(a3_node_name)

        if a3_row:
            sleep(10)
            a3_status = self.get_status_cell(a3_row)
            self.utils.print_info("A3 Node status " + a3_status)
            if 'icon-status' in a3_status:
                self.utils.print_info("A3 Node Status: Connected")
                self._expand_a3_server_node(a3_server_name)
                return 'green'
        return -1

    def _access_go_to_a3_button(self, a3_host_name):
        """
        - This keyword will access Go To A3 Button on A3 Server host
        - Assumes that already navigated to the A3 --> Inventory

        :param a3_host_name: A3 Server Host Name
        :return: 1 if able to access go to A3 button else False
        """
        self._goto_a3_inventory_page()
        sleep(2)
        rows = self.get_grid_rows()
        print(rows)
        sleep(5)
        for row in rows:
            if a3_host_name in row.text:
                self.utils.print_debug("Found A3 device row: ", self.format_row(row.text))
                sleep(5)
                if not self.get_a3_device_expanded_button(row).is_selected():
                    self.utils.print_info("Clicking Expand Button to View A3 Nodes")
                    self.auto_actions.click(self.get_a3_device_expanded_button(row))
                    self.screen.save_screen_shot()
                    sleep(5)
                    self.utils.print_info("Clicking Go To A3 Button")
                    self.auto_actions.click(self.get_go_to_a3_button(row))
                return 1
        return False

    def _access_a3_node_go_to_a3_button(self, a3_server_name, a3_node_name):
        """
        - This keyword will Access Go To A3 Button on A3 Node Host
        - Assumes that already navigated to the A3 --> Inventory

        :param a3_node_name: A3 Node Host Name
        :param a3_server_name: A3 server Host Name
        :return: 1 if able to access go to A3 button else False
        """
        self._expand_a3_server_node(a3_server_name)
        sleep(5)
        self.utils.print_info("Click A3 Inventory Refresh button")
        self.auto_actions.click(self.get_refresh_a3_devices_page())
        rows = self.get_a3_node_grid_rows()
        print(rows)
        for row in rows:
            if a3_node_name in row.text:
                self.utils.print_info("Clicking Go To A3 Button")
                self.auto_actions.click(self.get_a3_node_go_to_a3_button(row))
                return 1
        return False

    def verify_a3_server_login_on_xiq(self, a3_host_name, a3_login_username, a3_login_password):
        """
        - This keyword will verify A3 Server Access from XIQ UI using Go To A3 Button and Check A3 Login via XIQ
        - Assume that navigated to the A3 --> Inventory
        - Keyword Usage:
         - ``Verify A3 Server Login On XIQ   ${A3_IP_ADDR}   ${A3_USERNAME}  ${A3_PASSWORD}``

        :param a3_host_name: A3 Server host name
        :param a3_login_username: A3 Login Name to Access A3 UI
        :param a3_login_password: A3 Login Password Access A3 UI
        :return: A3 UI Page Title if Able to Login Successfully
        """
        self._access_go_to_a3_button(a3_host_name)
        self.utils.print_info("Switching to newly opened tab")
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Logging A3 with Username : ", a3_login_username, " -- Password : ", a3_login_password)

        self.utils.print_info("Entering A3 Username...")
        self.auto_actions.send_keys(self.get_a3_login_username_field(), a3_login_username)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering A3 Password...")
        self.auto_actions.send_keys(self.get_a3_login_password_field(), a3_login_password)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking on Sign In button")
        self.auto_actions.click(self.get_a3_login_button())
        sleep(8)

        self.screen.save_screen_shot()
        sleep(2)

        a3_page_title = self.driver.title
        self.utils.print_info("Page Title is : ", a3_page_title)
        return a3_page_title

    def verify_a3_node_login_on_xiq(self, a3_server_name, a3_node_name, a3_login_username, a3_login_password):
        """
        - This keyword will verify A3 Node Access from XIQ UI using Go To A3 Button and check A3 login via XIQ
        - Assume that navigated to the A3 --> Inventory
        - Keyword Usage:
         - ``Verify A3 Node Login On XIQ   ${A3_SERVER_NAME}  ${A3_IP_ADDR}   ${A3_USERNAME}  ${A3_PASSWORD}``


        :param a3_server_name: A3 Server Name
        :param a3_node_name: A3 Node Name
        :param a3_login_username: A3 login name to Access A3 UI
        :param a3_login_password: A3 login password Access A3 UI
        :return: A3 UI Page Title if able to login successfully
        """
        self._access_a3_node_go_to_a3_button(a3_server_name, a3_node_name)
        sleep(2)

        self.utils.print_info("Switching to newly opened A3 UI tab")
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(2)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Logging A3 with Username : ", a3_login_username, " -- Password : ", a3_login_password)

        self.utils.print_info("Entering A3 username...")
        self.auto_actions.send_keys(self.get_a3_login_username_field(), a3_login_username)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Entering A3 password...")
        self.auto_actions.send_keys(self.get_a3_login_password_field(), a3_login_password)

        self.screen.save_screen_shot()
        sleep(2)

        self.utils.print_info("Clicking on Sign In button")
        self.auto_actions.click(self.get_a3_login_button())
        sleep(8)

        self.screen.save_screen_shot()
        sleep(2)

        a3_page_title = self.driver.title
        self.utils.print_info("Page Title is : ", a3_page_title)
        return a3_page_title

    def validate_a3_page_after_unlink(self, a3_host_name):
        """
        - This Keyword will validate the A3 page text after Unlinking A3 from XIQ
        - Keyword Usage:
         - ``Validate A3 Page After Unlink      ${A3_HOST_NAME}``
        :return: 1 if unlinking of A3 to xiq is success
        """
        self.navigator.navigate_a3_inventory()
        sleep(2)
        self.utils.switch_to_iframe(self.driver)
        sleep(5)
        if not self.get_refresh_a3_devices_page():
            self.utils.print_info("Checking A3 page text after unlink to XIQ")
            unlink_page_text = self.get_a3_unlink_page_text().text
            self.utils.print_info("A3 page text is : ", unlink_page_text)
            self.screen.save_screen_shot()
            sleep(2)
            return unlink_page_text
        else:
            if self.search_a3_device(a3_host_name) == 1:
                self.utils.print_info("A3 page still having the A3 cluster node entries")
                self.screen.save_screen_shot()
                sleep(2)
                return -1
        return 1


