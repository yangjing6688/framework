from common.Utils import Utils
from common.Cli import Cli


class SNMPTraps:
    def __init__(self):
        self.utils = Utils()
        self.cli = Cli()

    def start_snmp_traps(self, spawn):
        self.utils.print_info("Go to SNMP MIBS Directory:")
        cmd1 = "cd /usr/share/snmp/mibs/"
        self.cli.send_pxssh(spawn, cmd1)

        self.utils.print_info("Remove Trap File in the Directory:")
        cmd2 = "rm -rf trap.txt"
        self.cli.send_pxssh(spawn, cmd2)

        self.utils.print_info("Remove Trap File in the Directory:")
        cmd3 = "pkill -9 snmptrapd"
        self.cli.send_pxssh(spawn, cmd3)

        self.utils.print_info("Start SNMP Traps on default udp port number 162:")
        cmd4 = "snmptrapd  -O f -L f trap.txt 0.0.0.0:162"
        self.cli.send_pxssh(spawn, cmd4)

        self.utils.print_info("List files on current Directory:")
        cmd5 = "ls -ltr"
        self.cli.send_pxssh(spawn, cmd5)
        if "trap.txt" in spawn.before:
            return 1
        else:
            return -1

    def validate_snmp_trap_messages(self, spawn, trap_string):
        self.utils.print_info("Go to SNMP MIBS Directory:")
        cmd1 = "cd /usr/share/snmp/mibs/"
        self.cli.send_pxssh(spawn, cmd1)

        self.cli.send_pxssh(spawn, "cat trap.txt")
        if trap_string in spawn.before:
            return 1
        else:
            return -1

    def start_snmp_traps_with_custom_port(self, spawn):
        self.utils.print_info("Go to SNMP MIBS Directory")
        cmd1 = "cd /usr/share/snmp/mibs/"
        self.cli.send_pxssh(spawn, cmd1)

        self.utils.print_info("Remove Trap File in the Directory:")
        cmd2 = "rm -rf trap.txt"
        self.cli.send_pxssh(spawn, cmd2)

        self.utils.print_info("Remove Trap File in the Directory:")
        cmd3 = "pkill -9 snmptrapd"
        self.cli.send_pxssh(spawn, cmd3)

        self.utils.print_info("Start SNMP Traps on default udp port number 162:")
        cmd4 = "snmptrapd  -O f -L f trap.txt 0.0.0.0:1025"
        self.cli.send_pxssh(spawn, cmd4)

        self.utils.print_info("List files on current Directory:")
        cmd5 = "ls -ltr"
        self.cli.send_pxssh(spawn, cmd5)
        if "trap.txt" in spawn.before:
            return 1
        else:
            return -1