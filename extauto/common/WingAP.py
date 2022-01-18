import sys
import time
import pexpect
import subprocess
from common.Utils import Utils
from common.Cli import Cli


class WingAP:
    def __init__(self):
        self.utils = Utils()
        self.cli = Cli()

    def factory_rest_wing_ap(self, ip, port):
        """
        - This Keyword is used to reset wing ap to factory defaults

        :param ip:  Wing AP IP
        :param port: Console port of AP
        :return: returns 1 if success
        """
        username = "reset"
        password = "FactoryDefault"

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

            """ pattern matches """
            i = spawn.expect(['## Booting',
                              'Welcome.',
                              'Please press Enter to activate this console.',
                              'Login incorrect',
                              'login:',
                              '#',
                              '>',
                              pexpect.TIMEOUT], timeout=60)

            if i == 0:
                """
                Booting
                """
                retry_count += 1
                self.utils.print_info("Booting...")
                time.sleep(5)

            elif i == 1:
                """
                Booting
                """
                retry_count += 1
                self.utils.print_info("Got Welcome... DUT is still booting")
                time.sleep(10)

            elif i == 2:
                """
                Completed Booting
                """
                retry_count += 1
                self.utils.print_info("Continue")

            elif i == 3 or i == 4:
                """
                Wrong Credentials
                """
                retry_count += 1
                self.utils.print_info("Sending Username : ", username)
                spawn.sendline("reset")
                spawn.expect("Password:")
                time.sleep(1)
                self.utils.print_info("Sending Password : ", password)
                spawn.sendline("FactoryDefault")

            elif i == 5 or i == 6:
                """
                Login prompt
                """
                spawn.sendline("exit")
                time.sleep(5)

            retry_count += 1

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

    def reload_wing_ap(self, spawn):
        """
        - This Keyword is used to reload wing ap

        :param spawn:  Wing AP SPAWN
        :return: returns 1 if success
        """
        spawn.sendline('reload')
        retry_count = 0
        while retry_count < 80:
            i = spawn.expect(['Save current configuration',
                              'The system will be rebooted, do you want to continue',
                              'The system is going down NOW!',
                              ], timeout=60)
            if i == 0:
                time.sleep(2)
                spawn.sendline('y')

            if i == 1:
                time.sleep(5)
                spawn.sendline('y')
                time.sleep(5)

            if i == 2:
                break

            retry_count += 1

        retry_count_2 = 0
        while retry_count_2 < 80:
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
            retry_count_2 += 1
        spawn.close()
        return 1

    def associate_ap(self, ap_spawn, retries=2):
        """
        :param ap_spawn:
        :param retries:
        :return:
        """
        retry_count = 1
        while retry_count <= retries:
            self.utils.print_info("Associating AP - Loop : ", retry_count)
            self.cli.send(ap_spawn, "configure")
            time.sleep(1)
            self.cli.send(ap_spawn, "self")
            self.cli.send(ap_spawn, "adoption-mode cloud")
            time.sleep(1)
            self.cli.send(ap_spawn, "adoption-mode cloud")
            time.sleep(1)
            return 1
