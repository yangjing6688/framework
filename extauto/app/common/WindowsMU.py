from extauto.common.Utils import Utils
from extauto.common.Cli import Cli


class WindowsMU:
    def __init__(self):
        self.utils = Utils()
        self.cli = Cli()

    def connect_window_mu_to_wifi(self, spawn, ssid, user_name=None, password=None, profile=None, default_spawn="ssh"):
        """
            connect a window platform MU to a wifi
            @param ssid:string | SSID name
            @param user_name:string | wifi user name
            @param password:string | wifi user password
            @todo: connect wifi with username/password or profile
        """
        cmd = 'netsh wlan connect name=%s'
        result = 1
        if user_name is not None and password is not None:
            cmd = ''
        else:
            cmd = cmd % ssid
        if default_spawn == "ssh":
            spawn.sendline(cmd)
            # read 2 lines
            out = spawn.read_nonblocking(800, 10)
        else:
            output = self.cli.send_paramiko_cmd(spawn, cmd)
            out = output[0]
        if 'successfully' not in out:
            result = -1
        return result

    def disconnect_windown_mu_wifi(self, spawn, default_spawn="ssh"):
        """
            disconnect a window platform MU from wifi
        """
        result = 1
        cmd = 'netsh wlan disconnect'
        # read 2 lines
        if default_spawn == "ssh":
            spawn.sendline('netsh wlan disconnect')
            spawn.readline(400)
            out = spawn.readline(400)
        else:
            output = self.cli.send_paramiko_cmd(spawn, cmd)
            out = output[0]
        if 'successfully' not in out:
            result = -1
        return result
