from ExtremeAutomation.Library.Utils.Constants.Constants import Constants


class AgentConstants(Constants):
    DEFAULT_SLEEP_BETWEEN_COMMANDS = 500
    WAIT_FOR_SLEEP = 500
    WAIT_FOR_RETRIES = 10

    # Supported agents
    TYPE_SSH = "ssh"
    TYPE_TELNET = "telnet"
    TYPE_CONSOLE = "console"
    TYPE_SLOT_1 = "slot1"   # Master/Slave deprecated for primary/backup chassis or stack controller.
    TYPE_SLOT_2  = "slot2"    # primary/backup are serial/console/termserver ip+port connections
    TYPE_SERIAL = "serial"  # For using an actual serial port. Not for telnet console servers.
    TYPE_JSON = "json"
    TYPE_REST = "rest"
    TYPE_SIESTA = "siesta"
    TYPE_SELENIUM = "selenium"
    TYPE_EXT_SELENIUM = "ext_selenium"
    TYPE_BASE_SELENIUM = "base_selenium"
    TYPE_SNMP = "snmp"
    TYPE_NORTHBOUND = "northbound"
    TYPE_GIM_SELENIUM = "gim_selenium"
    TYPE_XMC_REST = "xmc_rest"
    TYPE_JSON_RPC = "json_rpc"

    # Default agent ports
    TELNET_PORT = "23"
    SSH_PORT = "22"
    SNMP_PORT = "161"
    REST_PORT = "80"
    NORTHBOUND_PORT = "8443"
    XMC_REST_PORT = "80"
