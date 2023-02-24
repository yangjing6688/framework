import re

from extauto.common.Cli import Cli
from extauto.common.Utils import Utils


class CoPilotUtils(Cli):
    def __init__(self):
        self.cli = Cli()
        self.utils = Utils()
        self.local_host_spawn = -1
        self.ahqa_key = None

    def connect_to_xiq_cloud_console(self, local_host_ip, local_host_username, local_host_pwd, js_ip, js_username,
                                     js_pwd, rdc_console_name, rdc_console_username, ahqa_key):
        """
        This keyword connects to XIQ Cloud Console

        :param local_host_ip: local host IP
        :param local_host_username: local host Username
        :param local_host_pwd: local host Password
        :param js_ip: Jump Station IP address
        :param js_username: Jump Station Username
        :param js_pwd: Jump Station Password
        :param rdc_console_name: RDC Console Name Ex: g7r1-console.qa.xcloudiq.com, g7r3-console.qa.xcloudiq.com
        :param rdc_console_username:
        :param ahqa_key: QA keys relative path
        :return:
        """
        self.ahqa_key = ahqa_key
        self.utils.print_info("Local Host IP: ", local_host_ip)
        self.utils.print_info("Local Host Username: ", local_host_username)
        self.utils.print_info("Local Host Password: ", local_host_pwd)

        self.utils.print_info("Jump Station IP: ", js_ip)
        self.utils.print_info("Jump Station Username: ", js_username)

        self.local_host_spawn = self.cli.open_pxssh_spawn(local_host_ip, local_host_username, local_host_pwd)

        self._clear_old_ssh_agent_process()

        self._get_existing_ssh_agent_process()

        self._start_ssh_agent()

        if self._add_ssh_key():
            self._start_js_tunnel(js_ip, js_username, js_pwd, rdc_console_name, rdc_console_username)

    def send_command_to_xiq_cloud_console(self, command, timeout=10):
        """
        This keyword sends a command to XIQ cloud console
        :param command: command to send to XIQ cloud console
        :param timeout: timout for the command
        :return: returns command output
        """
        return self.cli.send_pxssh(self.local_host_spawn, command, timeout=timeout)

    def disconnect_from_xiq_cloud_console(self):
        """
        This keyword sends a command to XIQ cloud console
        :return: 1 if success, -1 if fails
        """
        try:
            self.utils.print_info("Logout from XIQ Cloud Console...", )
            self.cli.send_pxssh(self.local_host_spawn, 'logout')

            self.utils.print_info("Logout from Jump Server...", )
            self.cli.send_pxssh(self.local_host_spawn, 'logout')

            self.utils.print_info("Logout from Local Server...", )
            self.cli.send_pxssh(self.local_host_spawn, 'logout')
            return 1
        except Exception as e:
            self.utils.print_info("Error while logging out")
            self.utils.print_info(e)
            return -1

    def _start_js_tunnel(self, js_ip, js_username, js_password, rdc_console_name, rdc_console_username):
        try:
            self.cli.send_pxssh(self.local_host_spawn, 'ssh ' + js_username + '@' + js_ip + ' -A', timeout=3, expected_output="password")
            self.cli.send_pxssh(self.local_host_spawn, js_password, timeout=3, expected_output="$")

            self.cli.send_pxssh(self.local_host_spawn, 'ssh ' + rdc_console_username + '@' + rdc_console_name + ' -i /home/' + js_username + '/ahqa_id_rsa -A', timeout=5, expected_output='Last login' )
        except Exception as e:
            self.utils.print_info("Error in _start_js_tunnel..")
            self.utils.print_info(e)

    def _clear_old_ssh_agent_process(self):
        try:
            self.utils.print_info("Clearing existing SSH-AGENT processes. Sending Command: pkill ssh-agent")
            op_old_ssh_agents = self.cli.send_pxssh(self.local_host_spawn, 'pkill ssh-agent')
            self.utils.print_info("Output for clearing existing SSH-AGENT: ", op_old_ssh_agents.encode("ascii", "ignore"))
        except Exception as e:
            self.utils.print_info("Error while clearing existing SSH-AGENT processes")
            self.utils.print_info(e)
            return -1

    def _get_existing_ssh_agent_process(self):
        try:
            self.utils.print_info("Checking Old SSH-AGENT processes. Sending Command: ps ax | grep --color=never ssh-agent")
            op_ssh_agents_list = self.cli.send_pxssh(self.local_host_spawn, 'ps ax | grep --color=never ssh-agent')
            self.utils.print_info("Checking for any SSH-AGENT: ", op_ssh_agents_list)
            return 1
        except Exception as e:
            self.utils.print_info("Error while checking existing ssh agent processes")
            self.utils.print_info(e)
            return -1

    def _start_ssh_agent(self):
        try:
            self.utils.print_info("Sending Command: eval `ssh-agent -s`")
            op_eval_agents = self.cli.send_pxssh(self.local_host_spawn, 'eval `ssh-agent -s`')
            agent_pid = re.search(r'Agent pid ([\d]+)', op_eval_agents).group(1)
            self.utils.print_info("Eval Command Output: ", op_eval_agents, " Agent PID: ", str(agent_pid))
            return agent_pid
        except Exception as e:
            self.utils.print_info("Error while starting ssh-agent")
            self.utils.print_info(e)
            return -1

    def _add_ssh_key(self):
        self.utils.print_info("Sending Command: ssh-add ahqa_id_rsa")
        op_ssh_add_keys = self.cli.send_pxssh(self.local_host_spawn, 'ssh-add ' + self.ahqa_key)
        self.utils.print_info("Eval Command Output: ", op_ssh_add_keys)
        if "Identity added:" in op_ssh_add_keys:
            self.utils.print_info("Identity Added Successfully")
            return 1
        else:
            return -1