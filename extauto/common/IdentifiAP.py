import sys
import time
import pexpect
import subprocess
from extauto.common.Utils import Utils
from extauto.common.Cli import Cli


class IdentifiAP:
    def __init__(self):
        self.utils = Utils()
        self.cli = Cli()

    def factory_rest_identifi_ap(self, ip, port):
        """
        - Does factory reset of Indentifi AP
        - Keyword Usage:
         - ``Factory Rest Identifi AP    ${ip}   ${port}``

        :param ip: IP address of AP console
        :param port: AP console port
        :return: 1 if successful
        """
        username = "admin"
        password = "new2day"
        self.utils.print_info("Pinging the IP : ", ip)

        if " 0% packet loss" in subprocess.run(" ping " + ip + " -c 2 "):
            self.utils.print_info("ping received successfully...")
        else:
            self.utils.print_info("Unable to reach the DUT/MU")
            return -1

        conn_str = 'telnet ' + ip + " " + str(port)

        spawn = pexpect.spawn(conn_str)
        retry_count = 0
        while retry_count < 10:
            self.utils.print_info("Loop : ", retry_count)
            spawn.logfile = sys.stdout
            spawn.sendline("\r")
            spawn.sendline("\r")

            """ pattern matches """
            i = spawn.expect(['login:', ' #', '#', pexpect.TIMEOUT], timeout=60)

            if i == 0 or i == 1:
                retry_count += 1
                self.utils.print_info("Login Prompt Found...", i)
                self.utils.print_info("Sending Username : ", username)
                spawn.sendline(username)
                time.sleep(2)

                spawn.expect("Password:")
                time.sleep(2)

                self.utils.print_info("Sending Password : ", password)
                spawn.sendline(password)
                time.sleep(2)
                spawn.expect("#")
                time.sleep(2)

                spawn.sendline("cli")
                time.sleep(2)
                spawn.expect("#")

                self.utils.print_info("sending factory-default reboot command")
                spawn.sendline("cset fact")
                time.sleep(2)
                spawn.expect("setting factory default")
                time.sleep(2)
                break

            if i == 2:
                self.utils.print_info("Already Logged in...")
                retry_count += 1
                spawn.sendline("\r")
                spawn.expect("#")

                spawn.sendline("cset fact")
                time.sleep(2)
                spawn.expect("setting factory default")

                time.sleep(2)
                break

            if i == 3:
                retry_count += 1
                self.utils.print_info("Timeout. Retrying...")

        self.utils.print_info("AP Started Rebooting...")

        retry_count = 0
        while retry_count < 80:
            time.sleep(5)
            self.utils.print_info("Polling after 5 seconds")
            spawn.sendline('\r')
            spawn.logfile = sys.stdout
            i = spawn.expect([pexpect.TIMEOUT, 'login:'])
            if i == 0:
                self.utils.print_info("AP is still reloading...")
            if i == 1:
                self.utils.print_info("AP reloaded...")
                break
            retry_count += 1
        spawn.close()
        return 1
