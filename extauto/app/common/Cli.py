import re
import sys
import time
import shlex
import pexpect
import paramiko
import subprocess
from platform import system
from netmiko import ConnectHandler
from pexpect.pxssh import ExceptionPxssh
from xiq.configs.device_commands import *

from extauto.common.Utils import Utils

if "Window" not in system():
    from pexpect import pxssh


class Cli(object):

    def __init__(self):
        self.dut_platform = -1
        self.utils = Utils()

    def close_spawn(self, spawn):
        """
        Closes a spawn
        :param spawn: spawn
        :return: -1 in case of error else 1
        """
        if spawn == -9:
            return -9

        self.utils.print_info("\nClosing Connection...")
        try:
            spawn.close()
            return 1
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def set_platform(self, platform):
        """
        Sets the self.dut_platform with platform
        :param platform: DUT platform wing, identify, aerohive or linux
        """
        self.utils.print_info("Setting Platform to : ", platform)
        self.dut_platform = platform

    def get_platform(self):
        """
        Gets the self.dut_platform
        :return: platform - DUT platform wing, identify, aerohive or linux
        """
        self.utils.print_info("Returning Platform to : ", self.dut_platform)
        return self.dut_platform

    def open_ssh_spawn(self, ip, username, password, port="default"):
        if port == "default":
            return self.open_spawn(ip, 22, username, password, "linux")
        else:
            self.utils.print_info("SSH Port:", port)
            return self.open_spawn(ip, int(port), username, password, "linux")

    def open_spawn(self, ip, port, username, password, platform):

        _out = -1
        if port == '-1':
            return -9

        self.set_platform(platform)
        self.utils.print_info("Pinging the IP : ", ip)

        # try to ping to destination
        p_count = 0
        while p_count < 3:
            _cmd = "ping -c 2 %s" % str(ip)
            # self.utils.print_info("CMD: ", _cmd)
            _out =subprocess.check_output([_cmd], shell = True)
            if " 0% packet loss" in str(_out):
                break
            p_count += 1

        if " 0% packet loss" in str(_out):
            self.utils.print_info("Ping received successfully...")
        else:
            self.utils.print_info("Unable to reach the DUT/MU")
            return -1

        conn_str = 'telnet ' + ip + " " + str(port)
        if (port == 22) or (port == 8554):
            self.utils.print_info("Opening SSH Spawn...")
            conn_str = 'ssh ' + username + "@" + ip + " -p " + str(port)
            self.utils.print_info("SSH conn_str: ", conn_str)
        password_default = "admin123"
        password_cloud_default = "symbol123"

        if platform == "win":
            return self.open_windows_spawn(conn_str, username, password)

        elif platform == "linux":
            retry_count = 0
            spawn = pexpect.spawnu(conn_str)
            spawn.logfile = sys.stdout
            self.utils.print_info("Connecting to Linux Host")

            while retry_count < 10:
                self.utils.print_info("Loop: ", retry_count)
                i = spawn.expect(['login:',
                                  'assword:',
                                  'yes/no',
                                  '#',
                                  'Login incorrect',
                                  '>',
                                  pexpect.TIMEOUT,
                                  pexpect.EOF], timeout=90)
                if i == 0:
                    self.utils.print_info("Sending Username: ", username)
                    spawn.sendline(username)
                    time.sleep(2)
                    spawn.expect('assword:', timeout=30)
                    time.sleep(2)
                    spawn.sendline(password)
                    time.sleep(10)
                    j = spawn.expect('#', timeout=60)
                    if j == 0:
                        return spawn
                    if j == 1:
                        self.utils.print_info("Timeout Exiting...")
                        continue

                if i == 1:
                    self.utils.print_info("SSH Detected...")
                    spawn.sendline(password)
                    time.sleep(5)
                    j = spawn.expect(['#', '>'], timeout=60)
                    if j == 0:
                        self.utils.print_info("Got Prompt. Returning Spawn...")
                        return spawn

                    if j == 1:
                        self.utils.print_info("Got Prompt. Returning Spawn...")
                        return spawn

                    if j == 2:
                        self.utils.print_info("Timeout Exiting...")
                        continue

                if i == 2:
                    time.sleep(1)
                    spawn.sendline("yes")
                    continue

                if i == 3:
                    time.sleep(1)
                    return spawn

                if i == 4:
                    time.sleep(5)

                if i == 5:
                    time.sleep(5)

                if i == 6:
                    time.sleep(5)
                    self.utils.print_info("pexpect.EOF, Retrying...")
                    retry_count += 1
                    continue

                if i == 7:
                    time.sleep(5)
                    self.utils.print_info("Timeout, Retrying...")
                    retry_count += 1
                    continue

        elif platform == "aerohive":
            return self.open_aerohive_ap_spawn(conn_str, username, password)

        elif platform == "aerohive-switch":
            return self.open_aerohive_switch_spawn(conn_str, username, password)
        else:
            spawn = pexpect.spawn(conn_str, timeout=90)
            retry_count = 0
            self.utils.print_info("Connecting to Platform: ", platform)
            while retry_count < 10:
                self.utils.print_info("Loop : ", retry_count)
                if platform == "identifi":
                    spawn.logfile = sys.stdout
                    spawn.sendline("\r")
                else:
                    spawn.sendline("\r")

                """ pattern matches """
                i = spawn.expect(['## Booting',
                                  'Welcome.',
                                  'Please press Enter to activate this console.',
                                  'Login incorrect',
                                  'login:',
                                  ' #'
                                  '#',
                                  '\>',
                                  pexpect.TIMEOUT], timeout=60)

                if i == 0:
                    retry_count += 1
                    self.utils.print_info("Booting...")
                    time.sleep(5)

                elif i == 1:
                    retry_count += 1
                    self.utils.print_info("Got Welcome... DUT is still booting")
                    time.sleep(10)

                elif i == 2:
                    retry_count += 1
                    self.utils.print_info("Continue")

                elif i == 3:
                    retry_count += 1
                    time.sleep(65)
                    self.utils.print_info("Continue")

                elif i == 4:
                    retry_count += 1
                    self.utils.print_info("Got login: prompt..")
                    self.utils.print_info("Sending Username : ", username)
                    spawn.sendline(username)
                    spawn.expect("Password:")
                    time.sleep(1)
                    self.utils.print_info("Sending Password: ", password)
                    if password == "none":
                        self.utils.print_info("No Password. Sending a CR: ")
                        spawn.sendline("\r")
                    else:
                        spawn.sendline(password)

                    j = spawn.expect(["System is currently using the factory default login credentials",
                                      "Login incorrect",
                                      "\>",
                                      "\#"
                                      ], timeout=60)
                    """ i = spawn.expect(["Enter new password:","Login incorrect", "failed", ], timeout=60) """
                    if j == 0:
                        self.utils.print_info("Sending Cloud Default Password : ", password_cloud_default)
                        spawn.sendline(password_cloud_default)
                        spawn.expect('Confirm new password:')

                        self.utils.print_info("Confirming Cloud Default Password : ", password_cloud_default)
                        spawn.sendline(password_cloud_default)
                        spawn.expect('>')
                        spawn.sendline('en')
                        spawn.expect('#')
                    if j == 1:
                        spawn.sendline(username)
                        spawn.expect("assword:")
                        self.utils.print_info("Sending Factory Default Password : ", password_default)

                        if password_default != -1:
                            spawn.sendline(password_default)
                        else:
                            spawn.sendline(password)

                        k = spawn.expect(["Enter new password:",
                                          "Login incorrect", '>'])
                        if k == 0:
                            self.utils.print_info("Sending Cloud Default Password : ", password_cloud_default)
                            spawn.sendline(password_cloud_default)
                            spawn.expect('Confirm new password:')

                            self.utils.print_info("Sending Cloud Default Password : ", password_cloud_default)
                            spawn.sendline(password_cloud_default)
                            spawn.expect('>')
                            spawn.sendline('en')
                            spawn.expect('#')
                        if k == 1:
                            self.utils.print_info("\n\nPlease try with valid login credentials...Exiting")
                            return -2
                        if k == 2:
                            self.utils.print_info("\n\nDefault password got changed... Please check")
                            exit(0)
                    if j == 2:
                        spawn.sendline('en')
                        m = spawn.expect(["\#", "\:"], timeout=30)
                        if m == 1:
                            self.utils.print_info("Wrong > found.. Continuing..")
                            password_default = -1
                            continue
                        if m == 0:
                            self.utils.print_info("Found the prompt...")
                            break
                    if j == 3:
                        pass

                elif i == 6:
                    retry_count += 1
                    self.utils.print_info("Already Logged in")
                    spawn.sendline('\r')

                    spawn.sendline('show version')
                    time.sleep(2)
                    break

                elif i == 5:
                    pass

                elif i == 7:
                    spawn.sendline('en')
                    n = spawn.expect(["\#", "\:"], timeout=30)
                    if n == 1:
                        self.utils.print_info("Wrong > found.. Continuing..")
                        password_default = -1
                        continue
                    if n == 0:
                        self.utils.print_info("Found the prompt...")
                        break
                elif i == 8:
                    self.utils.print_info("Killing the Lantronix Port...")
                    lantronix_ip = 'telnet ' + ip
                    lspawn = pexpect.spawn(lantronix_ip)

                    lspawn.logfile = sys.stdout
                    retry_count = 0
                    m = lspawn.expect(["ETS8P", "\>"], timeout=30)
                    if m == 0:
                        self.utils.print_info("OLD Lantronix")
                        self.utils.print_info("Killing the tunnel on port : ", port)
                        lspawn.sendline("su" + '\r')
                        time.sleep(2)
                        lspawn.expect(">")

                        lspawn.sendline("su" + '\r')
                        time.sleep(2)
                        lspawn.expect(">")

                        lspawn.sendline("system" + '\r')
                        time.sleep(2)
                        lspawn.expect(">>")

                        lspawn.sendline("lo po " + str(int(port) % 2000) + '\r')
                        time.sleep(2)
                        lspawn.expect(">>")

                        lspawn.close()
                        retry_count = 0

                    if m == 1:
                        self.utils.print_info("NEW Lantronix")
                        self.utils.print_info("Killing the tunnel on port : ", port)
                        lspawn.sendline("enable" + '\r')
                        time.sleep(2)
                        lspawn.expect("#")

                        lspawn.sendline("tunnel " + str(int(port) % 10000) + '\r')
                        time.sleep(2)
                        lspawn.expect("#")

                        lspawn.sendline("accept" + '\r')
                        time.sleep(2)
                        lspawn.expect("#")

                        lspawn.sendline("kill connection" + '\r')
                        time.sleep(2)
                        lspawn.expect("#")

                        lspawn.close()

                        self.utils.print_info("Re-opening the spawn")
                        spawn = pexpect.spawn(conn_str)
                        spawn.logfile = sys.stdout
                        retry_count = 0
                    continue
                else:
                    self.utils.print_info("Retrying...")
                retry_count += 1

        self.utils.print_info("Returning spawn...")
        return spawn

    def open_aerohive_switch_spawn(self, conn_str, username, password):
        self.utils.print_info("Platform set to Aerohive Switch...")
        retry_count = 0
        spawn = -1
        while retry_count < 10:
            spawn = pexpect.spawn(conn_str, encoding='utf-8')
            time.sleep(5)
            spawn.sendline("\r")

            self.utils.print_info("Loop: ", retry_count)
            i = spawn.expect(['User:',
                              'Password:',
                              'yes/no',
                              '#',
                              'Login incorrect',
                              '>',
                              pexpect.TIMEOUT,
                              pexpect.EOF], timeout=90)
            if i == 0:
                self.utils.print_info("Sending Username: ", username)
                spawn.sendline(username)
                self.utils.print_info("Sending Password: ", password)
                spawn.expect('Password:', timeout=30)
                time.sleep(5)
                spawn.sendline(password)
                time.sleep(2)
                j = spawn.expect('>', timeout=60)
                if j == 0:
                    spawn.sendline('en')
                    return spawn
                if j == 1:
                    self.utils.print_info("Timeout Exiting...")
                    continue

            if i == 1:
                self.utils.print_info("SSH Detected...")
                spawn.sendline(password)
                time.sleep(5)
                j = spawn.expect(['#', '>'], timeout=60)
                if j == 0:
                    self.utils.print_info("Got Prompt. Returning Spawn...")
                    return spawn

                if j == 1:
                    self.utils.print_info("Got Prompt. Returning Spawn...")
                    return spawn

                if j == 2:
                    self.utils.print_info("Timeout Exiting...")
                    continue

            if i == 2:
                time.sleep(1)
                spawn.sendline("yes")
                continue

            if i == 3:
                time.sleep(1)
                return spawn

            if i == 4:
                time.sleep(5)

            if i == 5:
                spawn.sendline("en")

            if i == 6:
                time.sleep(5)
                self.utils.print_info("pexpect.EOF, Retrying...")

            if i == 7:
                time.sleep(5)
                self.utils.print_info("Timeout, Retrying...")
                spawn.sendline("\r")

            retry_count += 1
        return spawn

    def open_aerohive_ap_spawn(self, conn_str, username, password):
        self.utils.print_info("Platform set to Aerohive AP...")
        retry_count = 0
        spawn = -1
        while retry_count < 10:
            spawn = pexpect.spawn(conn_str, encoding='utf-8')
            time.sleep(5)
            spawn.sendline("\r")

            self.utils.print_info("Loop: ", retry_count)
            i = spawn.expect(['login:',
                              'assword:',
                              'yes/no',
                              '#',
                              'Login incorrect',
                              '>',
                              pexpect.TIMEOUT,
                              pexpect.EOF], timeout=90)
            if i == 0:
                self.utils.print_info("Sending Username: ", username)
                spawn.sendline(username)
                time.sleep(2)
                spawn.expect('assword:', timeout=30)
                time.sleep(2)
                spawn.sendline(password)
                time.sleep(10)
                j = spawn.expect('#', timeout=60)
                if j == 0:
                    return spawn
                if j == 1:
                    self.utils.print_info("Timeout Exiting...")
                    continue

            if i == 1:
                self.utils.print_info("SSH Detected...")
                spawn.sendline(password)
                time.sleep(5)
                j = spawn.expect(['#', '>'], timeout=60)
                if j == 0:
                    self.utils.print_info("Got Prompt. Returning Spawn...")
                    return spawn

                if j == 1:
                    self.utils.print_info("Got Prompt. Returning Spawn...")
                    return spawn

                if j == 2:
                    self.utils.print_info("Timeout Exiting...")
                    continue

            if i == 2:
                time.sleep(1)
                spawn.sendline("yes")
                continue

            if i == 3:
                time.sleep(1)
                return spawn

            if i == 4:
                time.sleep(5)

            if i == 5:
                time.sleep(5)

            if i == 6:
                time.sleep(5)
                self.utils.print_info("pexpect.EOF, Retrying...")

            if i == 7:
                time.sleep(5)
                self.utils.print_info("Timeout, Retrying...")
                spawn.sendline("\r")

            retry_count += 1
        return spawn

    def open_windows_spawn(self, conn_str, username, password):
        spawn = pexpect.spawn(conn_str)
        spawn.logfile = sys.stdout
        time.sleep(5)
        self.utils.print_info("Connecting to Windows Host")
        retry_count = 0
        while retry_count < 10:
            i = spawn.expect([':', pexpect.EOF, pexpect.TIMEOUT], timeout=20)
            if i == 0:
                self.utils.print_info("Sending Username : ", username)
                spawn.send(username + "\r")
                time.sleep(5)
                self.utils.print_info("Sending Password : ", password)
                spawn.expect('assword:', timeout=20)
                time.sleep(5)
                spawn.send(password + "\r")
                time.sleep(5)
                spawn.send("\r\n")
                time.sleep(5)
                try:
                    j = spawn.expect('>', timeout=20)
                except Exception as e:
                    self.utils.print_info(e)
                    # in case connect with a ssh server on window machine
                    j = spawn.expect('$', timeout=20)
                if j == 0:
                    return spawn
                if j == 1:
                    self.utils.print_info("Timeout Exiting...")

            if i == 1:
                time.sleep(5)
                self.utils.print_info("pexpect.EOF, Retrying...")
                continue

            if i == 2:
                time.sleep(5)
                self.utils.print_info("Timeout, Retrying...")
                continue

            retry_count += 1
        return spawn

    def send_command_to_ap1(self, command):
        ip = self.utils.get_config_value("AP1_CONSOLE_IP")
        port = self.utils.get_config_value("AP1_CONSOLE_PORT")
        username = self.utils.get_config_value("AP1_USERNAME")
        password = self.utils.get_config_value("AP1_PASSWORD")
        platform = self.utils.get_config_value("AP1_PLATFORM")

        self.utils.print_info("AP1 IP         : ", ip)
        self.utils.print_info("AP1 Port       : ", port)
        self.utils.print_info("AP1 Username   : ", username)
        self.utils.print_info("AP1 Password   : ", password)
        self.utils.print_info("AP1 Platform   : ", platform)

        _spawn = self.open_spawn(ip, port, username, password, platform)
        if _spawn:
            output = self.send(_spawn, command)
            self.close_spawn(_spawn)
            return output

    def send(self, spawn, line, expect_match="default", time_out="default", platform="default"):
        """

        :param spawn:
        :param line:
        :param expect_match:
        :param time_out:
        :param platform:
        :return:
        """
        if spawn == -9:
            return -9

        prompt = "#"
        if platform == 'adsp':
            prompt = "$"
            self.utils.print_info("Prompt set to $")
        if platform == "win":
            prompt = ">"
            self.utils.print_info("Prompt set to >")

        self.utils.print_info("Sending Command : " + "\n======================================\n" + line)
        if expect_match == "default":
            self.utils.print_debug("Expected Match: default")
            line = line.strip()
            spawn.sendline(line)
            # self.utils.print_info("----------------")
            # self.utils.print_info(spawn.before + spawn.after)
            # self.utils.print_info("----------------")
            if self.dut_platform == "win":
                spawn.sendline("\r\n")
                prompt = ">"
                self.utils.print_info("Prompt set to >")

            time.sleep(5)
            output1 = ""
            output2 = spawn.read_nonblocking(size=10000)
            if line == "exit":
                return output1 + output2

            if time_out == "default":
                self.utils.print_debug("Time Out: default")
                retry_count = 0
                while retry_count < 6:
                    self.utils.print_info("Loop: ", retry_count)
                    spawn.sendline("\r")
                    i = spawn.expect([prompt, pexpect.EOF, pexpect.TIMEOUT], timeout=90)
                    if i == 0:
                        self.utils.print_info("Breaking the Loop")
                        break
                    if i == 2:
                        output = str(spawn.before) + str(spawn.after)
                        self.utils.print_info("OUTPUT : ", output)
                        self.utils.print_info("Timeout... Retrying")
                        time.sleep(5)
                    if i == 3:
                        break
                    else:
                        retry_count += 1
            else:
                self.utils.print_info("Expecting prompt in : ", int(time_out))
                spawn.expect("#", timeout=int(time_out))
                output1 = str(spawn.before) + str(spawn.after)
        else:
            spawn.sendline(line)
            if platform == "win":
                spawn.sendline("\r\n")
            time.sleep(2)
            output1 = ''
            output2 = spawn.read_nonblocking(size=5000)
            self.utils.print_info("EXPECTING MATCH : ", expect_match)
            # if time_out == "default":
            #    spawn.expect(expect_match)
            # else:
            #    spawn.expect(expect_match, timeout=int(time_out))
            #    output1 = str(spawn.before) + str(spawn.after)

        self.utils.print_info("OUTPUT :\n======================================")

        try:
            cli_output = str(output1) + str(output2)
            self.utils.print_info("", cli_output)
            return cli_output
        except TypeError:
            self.utils.print_info("", str(output1))
            self.utils.print_info("", str(output2))

    def ping_from(self, destination, count=3):
        """
        - This method pings from the script host to the destination.
        - default count is 3

        :param destination: IP or host name
        :param count: Number of ping requests. Default is 3
        :return: returns 1 if 0 packet loss else -1
        """

        self.utils.print_info("Pinging to : ", destination)
        output = subprocess.run([" ping ", str(destination), " -c " + str(count)])
        self.utils.print_info("OUTPUT DATA:", output)

        if "100% packet loss" in output:
            return -1
        elif " 0% packet loss" in output:
            return 1
        elif "% packet loss" in output:
            return 1
        else:
            return -1

    def ping_from_spawn(self, _spawn, destination, count=3):
        """
        - This method pings from the spawn to the destination.
        - default count is 3

        :param _spawn: spawn of DUT/host from where ping should start
        :param destination: IP or host name
        :param count: Number of ping requests. Default is 3
        :return: returns 1 if 0 packet loss else -1
        """

        self.utils.print_info("Pinging to : ", destination)
        output = self.send(_spawn, "ping " + str(destination) + " -c " + str(count))
        self.utils.print_info("OUTPUT DATA:", output)

        if "100% packet loss" in output:
            return -1
        elif " 0% packet loss" in output:
            return 1
        elif "% packet loss" in output:
            return 1
        else:
            return -1

    def httping_from(self, _spawn, destination, count=3, timeout=5):
        """
        - This method pings from the spawn to the destination.
        - default count is 3

        :param _spawn: spawn of DUT/host from where ping should start
        :param destination: IP or host name
        :param count: Number of ping requests. Default is 3
        :param timeout: Timeout for the HTTP ping. Default is 5 seconds
        :return: returns 1 if 0 packet loss else -1
        """

        output = self.send(
            _spawn, "httping " + str(destination) + " -c " + str(count) + " -t " + str(timeout), "#", str(60))
        if "100.00% failed" in output:
            return 0
        elif " 0.00% failed" in output:
            return 1
        else:
            return -1

    def send_commands(self, spawn, commands_list):
        """
        Sends multiple commands separated by a ","

        :param spawn: spawn of DUT/host
        :param commands_list: list of DUT/Lunux commands separated by comma
        :return: output of the command
        """
        self.utils.print_info("Sending Commands List: ", commands_list)

        command_list = commands_list.split(",")
        output_end = ""

        for command in command_list:
            command=command.strip()
            output1 = self.send(spawn, command)
            time.sleep(2)
            output_end += output1

        return output_end

    def exec_shell_command(self, exec_shell_command):
        """
        Executes a shell command

        :param exec_shell_command: Any shell command
        :return: output of the command
        """

        self.utils.print_info("Command: ", exec_shell_command)
        args = shlex.split(exec_shell_command)
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        result = p.stdout.read()
        return result

    def open_pxssh_spawn(self, host, username, password, _port=22, prompt_reset=False):
        """
        Opens a pxssh spawn

        :param host: IP or host name
        :param username: username of host
        :param password: password of host
        :param _port: port number
        :param prompt_reset: prompt reset boolean
        :return: returns 1 if 0 packet loss else -1
        """
        try:
            pxssh_spawn = pxssh.pxssh()
            if pxssh_spawn.login(host, username, password, port=_port, auto_prompt_reset=prompt_reset, original_prompt=r"[#$>]"):
                self.utils.print_info("SSH session login successful")
                self.utils.print_info(pxssh_spawn.before)
                return pxssh_spawn
        except ExceptionPxssh:
            return -1

    def close_pxssh_spawn(self, pxssh_spawn):
        """
        Closes a pxssh spawn
        :param pxssh_spawn: pxssh spawn
        :return: -1 in case of error else 1
        """

        self.utils.print_info("Closing PXSSH spawn")
        try:
            pxssh_spawn.logout()
            return 1
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def send_pxssh(self, pxssh_spawn, command, timeout=3):
        """
        Sends a command to pxssh spawn

        :param pxssh_spawn: pxssh spawn
        :param command: command to send
        :param timeout: timeout to get the output
        :return: -1 in case of error else pxssh spawn
        """

        try:
            aa = pxssh_spawn.sendline(command)
            pxssh_spawn.prompt(timeout=timeout)
            self.utils.print_info("spawn.before: ", pxssh_spawn.before)
            self.utils.print_info("-----------------------------------")
            self.utils.print_info("spawn.after: ", pxssh_spawn.after)
            time.sleep(1)
            return pxssh_spawn.before
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def netmiko_ssh_spawn(self, **kwargs):
        """
        Creating spawn object, This will work only for extreme wing

        :param kwargs: host, username, password
        :return: returns spawn else the exception
        """
        extreme = {'device_type': 'extreme_wing'}
        extreme['host'] = self.host=kwargs.get('host')
        extreme['username'] = self.host=kwargs.get('username')
        extreme['password'] = self.host=kwargs.get('password')
        try:
            spawn = ConnectHandler(**extreme)
            spawn.find_prompt()
            return spawn
        except Exception as e:
            self.utils.print_info("Exception caught while creating sapwan is: ", str(e))

    def netmiko_send_en_command(self, spawn, command):
        """
        Sending command to spawn obj(specifically show commands of wings)

        :param spawn: netmiko spawn
        :param command: command to send
        :return: -1 in case of error else output of command
        """
        # Enable the prompt
        try:
            spawn.enable()
            output = spawn.send_command(command)
            self.utils.print_info("{} output is {}".format(command, output))
            return output
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def netmiko_send_cfg_cmd(self, spawn, config_commands):
        """
        Send the commands for configuring

        :param spawn: netmiko spawn
        :param config_commands: command to send
        :return: -1 in case of error else output of command
        """
        try:
            spawn.enable()
            output = spawn.send_config_set(config_commands)
            self.utils.print_info("Configuration:\n {}".format(output))
            return output
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def netmiko_send_timing_command(self, spawn, cmd):
        """
        Sends command to spawn

        :param spawn: netmiko spawn
        :param cmd: command
        :return: output of command if successful else -1
        """
        try:
            # send_command_timing as the router prompt is not returned
            self.utils.print_info("Sending command: ", cmd)
            output = spawn.send_command_timing(cmd, strip_command=False, strip_prompt=False)
            if "confirm" in output:
                    output += spawn.send_command_timing(
                        "\n", strip_command=False, strip_prompt=False
            )
            return output
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def netmiko_close(self, spawn):
        """
        Closes a netmiko spawn
        :param spawn: netmiko spawn
        :return: -1 in case of error else 1
        """
        try:
            spawn.disconnect()
            return 1
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def open_paramiko_ssh_spawn(self, host, username, password):
        """
        Creating ssh spawn object

        :param host: IP or host name of DUT
        :param username: username
        :param password: password
        :return: returns spawn else -1
        """
        try:
            spawn = paramiko.SSHClient()
            # Parsing an instance of the AutoAddPolicy to set_missing_host_key_policy() changes it to allow any host.
            spawn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            spawn.load_system_host_keys()
            spawn.connect(str(host), port=22, username=str(username), password=str(password))
            return spawn
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def send_paramiko_cmd(self, spawn, cmd, timeout=10):
        """
        Execute the commands on ssh spawn
        :param spawn: netmiko spawn
        :param cmd: command to send
        :param timeout: command timeout
        :return: -1 in case of error else output of command
        """
        try:
            stdin, stdout, stderr = spawn.exec_command(cmd, timeout=timeout)
            output = stdout.readlines()
            self.utils.print_info("cmd: {}".format(cmd))
            out = map(lambda s: s.strip(), output)
            for line in out:
                self.utils.print_info(line)
            return output
        except paramiko.SSHException:
            self.utils.print_info("Failed to execute the command")

    def close_paramiko_spawn(self, spawn):
        """
        Closing paramiko spawn obj

        :param spawn: paramiko spawn
        :return: returns -1 if there is any exception
        """
        self.utils.print_info("Closing paramiko spawn")
        try:
            spawn.close()
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def get_thput_value(self, ip, cli_spawn, server_spawn):
        """
        Get the throughput value form and to air
        """
        cli_cmd = 'iperf -c ' + ip + ' -i 1 -u  -b 20m -t 10'
        srvr_cmd = 'iperf -s -i 1 -u  &'

        self.utils.print_info("client_cmd:{}".format(cli_cmd))
        self.utils.print_info("Server_cmd:{}".format(srvr_cmd))

        _, stdout, _ = server_spawn.exec_command(srvr_cmd, timeout=200)
        cli_spawn.exec_command(cli_cmd, timeout=200)

        time.sleep(60)
        server_spawn.exec_command('TASKKILL /IM iperf.exe /F', timeout=200)
        server_spawn.exec_command('killall iperf', timeout=200)

        cli_spawn.exec_command('killall iperf', timeout=200)
        cli_spawn.exec_command('TASKKILL /IM iperf.exe /F', timeout=200)

        return stdout.readlines()
    
    def close_netmiko_spawn(self, spawn):
        """
        Closing netmiko spawn obj

        :param spawn: netmiko spawn
        :return: returns -1 if there is any exception
        """
        self.utils.print_info("Closing netmiko spawn")
        try:
            spawn.disconnect()
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def open_wing_spawn(self, host, username, password):
        wing_spawn = pxssh.pxssh()
        if not wing_spawn.login(host, username, password, auto_prompt_reset=False):
            self.utils.print_info("SSH session failed on login.")
            print (str(wing_spawn))
        else:
            self.utils.print_info("SSH session login successful")
            self.utils.print_info(wing_spawn.before)
            return wing_spawn

    def send_wing_cmd(self, pxssh_spawn, command):
        """
        This method will send a command to the spawn
        :param pxssh_spawn: spawn
        :param command: command to send
        :param timeout: timeout
        :return: returns the output if success else -1
        """
        try:
            aa = pxssh_spawn.sendline(command)
            pexpect.pty_spawn.SpawnBase.buffer = ""
            self.utils.print_info("-----------------------------------")
            self.utils.print_info("spawn.before: ", pxssh_spawn.before)
            self.utils.print_info("-----------------------------------")
            self.utils.print_debug("spawn.after: ", pxssh_spawn.after)
            time.sleep(1)
            return pxssh_spawn.before
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def get_ap_version(self, spawn=None):
        """
        This method returns the AP HiveOs version

        :param spawn: spawn to AP
        :return: returns the version if success else -1
        """
        output = self.send_command_to_ap1('show version | include Version')
        self.utils.print_info("Getting AP Version")
        #output = self.send(spawn, 'show version | include Version')
        try:
            self.utils.print_info("AP Version: ", output)
            ap_version = re.search('HiveOS (.*) build', output).group(1)
            return ap_version
        except Exception as e:
            self.utils.print_info(e)
            return -1

    def capwap_ap_on_off(self, ip, usr, passwd, mode):
        self.conn = self.open_spawn(ip, 22, usr, passwd, 'aerohive')
        if mode == 'off':
            self.send(self.conn, AP_CAPWAP_OFF, time_out="default", platform="aerohive")
        else:
            self.send(self.conn, AP_CAPWAP_ON, time_out="default", platform="aerohive")
        self.close_spawn(self.conn)

    def mac_wifi_connection(self, ip, usr, passwd, ssid, ssid_pass='badpassword20*rd', wifi_port='en1', mode='pass',
                            ntimes=1):

        self.conn = self.open_paramiko_ssh_spawn(ip, usr, passwd)
        self.send_paramiko_cmd(self.conn, TURN_ON_OFF_WIFI_INTERFACE + wifi_port + ' ON', 30)

        for i in range(1, 3):
            time.sleep(10)
            listSSIDs = str(self.send_paramiko_cmd(self.conn, SCAN_FOR_LIST_WIFI, 300))
            cnt = self.utils.check_match(listSSIDs, ssid)
            if cnt == 1:
                self.utils.print_info('ssid ' + ssid + ' is found')
                break
        assert self.utils.check_match(listSSIDs, ssid) == 1, "Not able to find the SSID"

        if mode == 'pass':
            rc = self.send_paramiko_cmd(self.conn, CONNECT_TO_WIFI + wifi_port + ' ' + ssid + ' ' + ssid_pass, 30)
            self.utils.print_info("RC is ---------" + str(rc))
            assert self.utils.check_match(rc, 'Failed to join') != 1, "Fail to connect"
            assert self.utils.check_match(rc, 'Error') != 1, "Fail to connect"
            self.utils.print_info('Connect successfully!')
        else:
            for i in range(1, ntimes):
                self.utils.print_info(str(i) + ' attempt(s)')
                rc = self.send_paramiko_cmd(self.conn, CONNECT_TO_WIFI + wifi_port + ' ' + ssid + ' ' + ssid_pass, 40)
        self.close_spawn(self.conn)
        return

    def get_mac_hostname(self, ip, userid, passwd):
        conn = self.open_paramiko_ssh_spawn(ip, userid, passwd)
        hostname = self.send_paramiko_cmd(conn, 'hostname')
        self.close_spawn(conn)
        return hostname
