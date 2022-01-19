import subprocess
from common.Utils import Utils
from common.Cli import Cli


class Syslog:
    def __init__(self):
        self.utils = Utils()
        self.cli = Cli()

    def start_syslog(self, password):
        """
        Starting syslog on script host
        """
        """
        Starting syslog on script host
        """
        cmd = 'echo ' + password + ' | sudo -S '
        subprocess.call(cmd + "rm -rf /var/log/syslog", shell=True)
        subprocess.call(cmd + "touch /var/log/syslog", shell=True)
        subprocess.call(cmd + "chmod 777 /var/log/syslog", shell=True)
        subprocess.call(cmd + " /etc/init.d/rsyslog stop", shell=True)
        subprocess.call(cmd + " /etc/init.d/rsyslog start", shell=True)

    def stop_syslog(self, password):
        """
        stop syslog on script host
        """
        cmd = 'echo ' + password + ' | sudo -S '
        subprocess.call(cmd + "/etc/init.d/rsyslog stop", shell=True)
