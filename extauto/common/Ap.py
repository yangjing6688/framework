import re
import time
import shlex
import subprocess
from extauto.common.Cli import Cli
from extauto.common.Utils import Utils


class Ap:
    def __init__(self):
        self.cli = Cli()
        self.utils = Utils()

    def load_cloud_certificate_on_ap(self, spawn, mac):
        """
        - Load Cloud Certificate on Access Point
        - Keyword Usage:
         - ``Load Cloud Certificate On AP    ${AP_SPAWN}   ${MAC_ADDRESS}``

        :param spawn: AP Spawn to Open Console
        :param mac: Wing AP Mac Address
        :return: None
        """
        last_password = -1

        self.cli.send(spawn, "copy ftp://root:symbol@20.1.1.145//tftpboot/cloudca.cert .")
        time.sleep(5)

        output = self.cli.send(spawn, "service show last-passwd")

        m = re.search('used:(.+?)with', output)
        if m:
            last_password = m.group(1).strip()

        if last_password != -1:
            self.utils.print_info("Last Password :", last_password)
            mac1 = mac.replace("-", ":")

            self.utils.print_info("Generating ROOT password")
            command_line1 = "chmod +x passwd_gen"
            command_line = "./passwd_gen " + mac1 + " " + last_password

            args1 = shlex.split(command_line1)
            p1 = subprocess.Popen(args1, stdout=subprocess.PIPE)
            chmod_result = p1.stdout.read()
            self.utils.print_info("Chmod Result: ", chmod_result)

            args = shlex.split(command_line)
            p = subprocess.Popen(args, stdout=subprocess.PIPE)
            result = p.stdout.read()

            n = re.search('Next Password is (.[a-z]+)', result)
            if m:
                next_password = n.group(1).strip()

                spawn.sendline("service start-shell")
                self.utils.print_info("*INFO*", spawn.before + spawn.after)

                spawn.expect("Password:")
                self.utils.print_info("*INFO*", spawn.before + spawn.after)

                spawn.sendline(next_password)
                self.utils.print_info("*INFO*", spawn.before + spawn.after)

                spawn.read_nonblocking(size=5000)
                self.utils.print_info("*INFO*", spawn.before + spawn.after)

                self.cli.send(spawn, "ls")
                self.cli.send(spawn, "rw")
                self.cli.send(spawn, "cd /flash/")
                self.cli.send(spawn, "cp cloudca.cert /usr/ssl/certs/")
                self.cli.send(spawn, "cd /usr/ssl/certs/")
                self.cli.send(spawn, "ls -ltr")

                self.cli.send(spawn, "date")
                self.cli.send(spawn, "exit")

    def get_ap_last_root_password(self, ap_spawn):
        """
        - This keyword will Get Wing AP Last used Root Password
        - Keyword Usage:
         - ``Get AP Last Root Password    ${AP_SPAWN}``

        :param ap_spawn: AP Spawn to Open Console
        :return: Last used Password of Wing AP else -1
        """
        self.utils.print_info("Getting Last Password Used...")
        output = self.cli.send(ap_spawn, "service show last-passwd")

        flag = re.search('used:(.+?)with', output)
        if flag:
            last_password = flag.group(1).strip()
            self.utils.print_info("Last Password Used: ", last_password)
            return last_password
        else:
            return -1

    def access_ap_root_prompt(self, ap_spawn, ap_mac):
        """
        - This keyword will Get Wing AP Root Prompt
        - Keyword Usage:
         - ``Access AP Root Prompt    ${AP_SPAWN}   ${AP_MAC}``

        :param ap_spawn: AP Spawn to Open Console
        :param ap_mac: AP Mac Address
        :return: 1 if Wing AP root Prompt Access Successful
        """
        next_password = self.generate_root_password(ap_mac, self.get_ap_last_root_password(ap_spawn))

        ap_spawn.sendline("service start-shell")
        self.utils.print_info("*INFO*", ap_spawn.before + ap_spawn.after)

        ap_spawn.expect("Password:")
        self.utils.print_info("*INFO*", ap_spawn.before + ap_spawn.after)

        ap_spawn.sendline(next_password)
        self.utils.print_info("*INFO*", ap_spawn.before + ap_spawn.after)

        ap_spawn.read_nonblocking(size=5000)
        self.utils.print_info("*INFO*", ap_spawn.before + ap_spawn.after)
        return 1

    def send_command_to_ap_root(self, ap_spawn, ap_mac, command):
        """
        - This keyword will uses to send CLI Command to Win g AP
        - Keyword Usage:
         - ``Send Command To AP Root    ${AP_SPAWN}   ${AP_MAC}   ${CLI_COMMAND}``

        :param ap_spawn: AP Spawn to Open Console
        :param ap_mac: AP Mac Address
        :param command: Wing AP CLI Command
        :return: Wing AP CLI command Output
        """
        self.utils.print_info("Sending Command to AP wit MAC: ", ap_mac)
        return self.cli.send(ap_spawn, command)
